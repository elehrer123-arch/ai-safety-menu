"""Vectorized local-frontier counterfactuals. No country diffusion in this module.

simulate(n, seed, horizon_years, steps_per_year) returns absolute log effective
compute relative to today's baseline, plus decompositions and all parameter draws.
integrate_resource_effect permits root to use identical shared draws for other policies.
"""
from pathlib import Path
import json
import numpy as np

BASE=Path(__file__).parent
YEAR=365.25

def _draw(inputs,rng,n,use_modes=False):
    out={}
    for row in inputs:
        d=row['distribution']
        if use_modes or d['type']=='point': a=np.full(n,d['mode'],dtype=float)
        else: a=rng.triangular(d['low'],d['mode'],d['high'],size=n)
        out[row['name']]=a
    return out

def integrate_resource_effect(shared,times,resource_ratio,direct_log_shock=None):
    """Returns algorithmic log difference a(t), shapeN×T.

    resource_ratio is already aggregated effective R&D effort relative to baseline;
    do NOT pass a raw labor fraction without the labor elasticity. Positive direct
    shocks/resource increases are supported. RK2(midpoint), piecewise-linear inputs.
    """
    times=np.asarray(times,float)
    rr=np.asarray(resource_ratio,float)
    if rr.ndim!=2: raise ValueError('resource_ratio must be N x T')
    if len(times)!=rr.shape[1] or np.any(rr<=0): raise ValueError('invalidtimes/resource')
    c=np.zeros_like(rr) if direct_log_shock is None else np.asarray(direct_log_shock,float)
    if c.shape!=rr.shape: raise ValueError('directlogshockshape')
    a=np.zeros_like(rr)
    ga,lam,beta,eta=(shared[k] for k in ['g_A','lambda_R','beta','eta'])
    def f(state,logr,ct):
        return ga*np.expm1(lam*(logr+eta*(state+ct))-beta*state)
    logr=np.log(rr)
    for j,dt in enumerate(np.diff(times)):
        # Substeps keep high-growth/long-horizon draws stable without clipping states.
        sub=max(1,int(np.ceil(dt/(1/104))))
        h=dt/sub; state=a[:,j].copy()
        for k in range(sub):
            w=k/sub; wm=(k+.5)/sub
            r0=(1-w)*logr[:,j]+w*logr[:,j+1]
            c0=(1-w)*c[:,j]+w*c[:,j+1]
            rm=(1-wm)*logr[:,j]+wm*logr[:,j+1]
            cm=(1-wm)*c[:,j]+wm*c[:,j+1]
            first=f(state,r0,c0)
            state+=h*f(state+.5*h*first,rm,cm)
        a[:,j+1]=state
    return a

def _ramp(t,days):
    return np.minimum(1,np.maximum(0,t*YEAR)/np.maximum(days,1.e-10))

def _data_loss(unique,rd,rn,alpha,grid_points=121):
    """Optimize normalized N*D=1 under saturation; constants normalized atoptimum."""
    ns=np.exp(np.linspace(-3,3,grid_points))
    u=unique[:,None]
    def eff(z,R):
        z=np.broadcast_to(z,(len(unique),len(ns)))
        return np.where(z<=u,z,u*(1+R[:,None]*(-np.expm1(-np.maximum(0,z/u-1)/R[:,None]))))
    ne=eff(ns[None,:],rn);de=eff((1/ns)[None,:],rd)
    loss=np.power(ne,-alpha[:,None])+np.power(de,-alpha[:,None])
    return loss.min(axis=1)

def _override(draws, values, n):
    for key, value in (values or {}).items():
        if key not in draws:
            raise KeyError(f'Unknown parameter override: {key}')
        draws[key]=np.broadcast_to(np.asarray(value,float),(n,)).copy()

def simulate(n=20000,seed=260925,horizon_years=3,steps_per_year=52,use_modes=False,overrides=None):
    """Optional overrides={'shared': {calibration_input_name: value},
    'policies': {policy_id: {input_name: value}}}; scalar or N-vector values.
    Override values are scenario choices, not constrained to prior supports.
    """
    spec=json.loads((BASE/'production-calibration.json').read_text())
    rng=np.random.default_rng(seed)
    overrides=overrides or {}
    raw=_draw(spec['shared_inputs'],rng,n,use_modes)
    _override(raw,overrides.get('shared'),n)
    s=dict(g_C=raw['raw_compute_log_growth'],g_A=raw['algorithmic_log_growth'],
      g_R=raw['research_input_log_growth'],lambda_R=raw['research_flow_elasticity'],
      eta=raw['feedback_to_research'],labor_share=raw['research_labor_share'])
    s['g_total']=s['g_C']+s['g_A'];s['beta']=s['lambda_R']*s['g_R']/s['g_A']
    times=np.linspace(0,horizon_years,round(horizon_years*steps_per_year)+1)
    baseline=s['g_total'][:,None]*times
    out={}
    for row in spec['policies']:
        pid=row['policy_id']; p=_draw(row['inputs'],rng,n,use_modes)
        _override(p,overrides.get('policies',{}).get(pid),n)
        c=np.zeros_like(baseline);rr=np.ones_like(baseline)
        aux={}
        if pid=='safety-compute-share':
            k=p['safety_capability_cobenefit']; s0=p['baseline_safety_share'];s1=p['mandated_safety_share']
            ratio=(1+p['budget_expansion'])*(1-s1+k*s1)/(1-s0+k*s0)
            aux['effective_input_ratio']=ratio
            for j,t in enumerate(times):
                c[:,j]=_ramp(t,p['implementation_ramp_days'])*np.log(ratio)
                rr[:,j]=np.exp(c[:,j])
        elif pid=='internal-deploy':
            f=np.minimum(1,p['incremental_gate_days']/p['model_generation_days'])*p['research_work_exposure']*p['new_model_incremental_uplift']/(1+p['new_model_incremental_uplift'])
            aux['cognitive_labor_loss_fraction']=f
            for j,t in enumerate(times):
                rr[:,j]=np.power(1-_ramp(t,p['implementation_ramp_days'])*f,s['labor_share'])
        elif pid=='ai-rnd-limits':
            review=p['review_service_hours']/(1-p['reviewer_utilization'])+p['handoff_hours']
            h=review/(p['autonomous_cycle_hours']+review)
            aux['checkpoint_total_hours']=review;aux['affected_chain_throughput_loss']=h
            for j,t in enumerate(times):
                yy=min(t,1)
                s5=yy*p['endyear_fully_autonomous_share']
                s4=np.minimum(1-s5,(1-yy)*p['current_ai_leads_share']+yy*p['endyear_ai_leads_share'])
                f=s4*p['incremental_checkpoint_share']*h+s5*p['autonomy_uplift_over_supervised']/(1+p['autonomy_uplift_over_supervised'])
                rr[:,j]=np.power(1-_ramp(t,p['implementation_ramp_days'])*f,s['labor_share'])
            aux['endyear_cognitive_labor_loss_fraction']=1-np.power(rr[:,np.argmin(abs(times-1))],1/s['labor_share'])
        elif pid=='compute-cap':
            for j,t in enumerate(times):
                gap=np.maximum(0,s['g_C']*t-p['cap_headroom_log'])*p['binding_compliance']
                c[:,j]=-(1-p['scale_gap_recovered_other_channels'])*gap
                rex=1-p['frontier_scale_dependent_experiments']*(-np.expm1(-gap))*(1-p['blocked_compute_redeployed']*p['substitute_experiment_value'])
                rr[:,j]=np.power(rex,1-s['labor_share'])
        elif pid=='pause-6':
            duration=p['pause_days']/YEAR
            k=-np.log(1-p['scale_gap_recovered_by_yearend'])/(1-duration)
            for j,t in enumerate(times):
                paused=t<duration
                direct=-s['g_C']*np.minimum(t,duration)*(1-p['permitted_progress_offset'])
                c[:,j]=direct*np.exp(-k*np.maximum(0,t-duration))
                rex=1-p['blocked_research_compute_share']*(1-p['blocked_compute_redeployed']*p['substitute_experiment_value'])
                rr[:,j]=np.where(paused,np.power(rex,1-s['labor_share']),1)
            # Policy begins immediately; initial direct gap remains zero.
        elif pid=='data-licensing':
            quality=1-p['data_needing_new_permission']+p['data_needing_new_permission']*p['affected_data_recovered']*p['replacement_quality']
            ub=1/p['baseline_epochs']; up=quality*ub
            lb=_data_loss(ub,p['repeat_data_saturation'],p['parameter_saturation'],p['loss_exponent'])
            lp=_data_loss(up,p['repeat_data_saturation'],p['parameter_saturation'],p['loss_exponent'])
            de=-2/p['loss_exponent']*np.log(lp/lb)*p['pretraining_dependency']
            aux['quality_adjusted_unique_data_ratio']=quality;aux['data_log_effective_compute_effect']=de
            for j,t in enumerate(times):
                ramp=_ramp(t,p['transition_days'])
                dur=p['transition_days']/YEAR
                # Delay accrues during transition; partial recovery reaches specifiedresidual atyear1.
                after=np.minimum(1,np.maximum(0,(t-dur)/(1-dur)))
                delay=p['transition_days']*p['transition_critical_share']*ramp*(1-(1-p['transition_gap_remaining'])*after)
                c[:,j]=ramp*(de+np.log(1-p['licensing_budget_share']))-s['g_total']*delay/YEAR
                rr[:,j]=1-ramp*p['licensing_budget_share']
        else:raise ValueError(pid)
        a=integrate_resource_effect(s,times,rr,c)
        out[pid]=dict(log_effective_compute=baseline+a+c,log_effective_compute_effect=a+c,
          algorithmic_log_effect=a,direct_log_effect=c,resource_ratio=rr,
          release_delay_days=np.zeros(n),parameters=p,diagnostics=aux)
    return dict(times=times,shared=s,baseline_log_effective_compute=baseline,policies=out,
      metadata=dict(n=n,seed=seed,year_days=YEAR,units='log effectivecompute relative totoday',
        headline='endpointdeficit on fixed baselineU.S.ruler; no exacthittingtime claim',
        extended_horizon='Afteryear1 inputpriors fixed, autonomyshares frozen; pause expires and directgap continues exponentialrecovery; data transition residual held.'))

def summarize(result):
    s=result['shared'];ts=result['times'];out={}
    for pid,p in result['policies'].items():
        row={}
        for y in [1,3]:
            if ts[-1]<y:continue
            j=np.argmin(abs(ts-y));lag=-p['log_effective_compute_effect'][:,j]/s['g_total']*YEAR
            row[f'year{y}']=dict(mean_days=float(lag.mean()),median_days=float(np.median(lag)),
                p10_days=float(np.quantile(lag,.1)),p90_days=float(np.quantile(lag,.9)),
                mean_log_gap=float(-p['log_effective_compute_effect'][:,j].mean()),
                mean_direct_log_gap=float(-p['direct_log_effect'][:,j].mean()),
                mean_algorithm_log_gap=float(-p['algorithmic_log_effect'][:,j].mean()))
        out[pid]=row
    return out

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=20000);ap.add_argument('--seed',type=int,default=260925)
    ap.add_argument('--years',type=float,default=3);ap.add_argument('--steps',type=int,default=52)
    ar=ap.parse_args();res=simulate(ar.n,ar.seed,ar.years,ar.steps)
    summary=summarize(res)
    (BASE/'production-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
