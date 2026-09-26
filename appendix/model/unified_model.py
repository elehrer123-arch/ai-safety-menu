"""35-policy endpoint model. All effects are relative to matched no-obligation paths.
Run with Python3 + NumPy. Country-production state unit: log effective compute.
"""
from pathlib import Path
import json,sys
import numpy as np
from production_model import simulate,integrate_resource_effect
from regulation_sampler import sample_regulation,training_chain_penalty
from china_model import china_paths
from country_dynamics import triangular,common_diffusion,propagate,endpoint_summary
YEAR=365.25
BASE=Path(__file__).parent

def make_inputs(n=8192,seed=260925,steps=52,years=3):
    prod=simulate(n=n,seed=seed,horizon_years=years,steps_per_year=steps)
    reg=sample_regulation(n=n,seed=seed+1)
    ts=prod['times'];s=prod['shared']
    china=china_paths(n=n,seed=seed+2,times=ts,g_total=s['g_total'],g_algo=s['g_A'])
    extra={}
    for row in json.loads((BASE/'integration-calibration.json').read_text())['inputs']:
        d=row['distribution'];extra[row['name']]=triangular(row['name'],d['low'],d['mode'],d['high'],n,seed+3)
    return dict(production=prod,regulation=reg,china=china,extra=extra)

def _reg_paths(pid,r,inputs):
    prod,reg,extra=(inputs[k] for k in ['production','regulation','extra'])
    ts,s=prod['times'],prod['shared'];n=len(s['g_total']);T=len(ts)
    meta=reg['policy_metadata'].get(pid,{})
    ramp=np.minimum(1,ts[None,:]*YEAR/extra['gate_ramp_days'][:,None])
    f=r['annual_rd_input_loss_fraction'];inv=r['annual_investment_input_loss_fraction']
    rr=((1-f)**s['labor_share']*(1-inv)**(1-s['labor_share']))[:,None]*np.ones((n,T))
    annual=r['annual_event_internal_equivalent_days'].copy()
    setup=r.get('first_year_setup_internal_equivalent_days',np.zeros(n))
    # Internal model-use gates affect access to the newest research assistant;
    # existing models remain usable. Only actual suspended research is a direct
    # production clock. The same fallback/uplift model prices internal-deploy.
    components=next((x['components'] for x in json.loads((BASE/'regulation-calibration.json').read_text())['bundles'] if x['policy_id']==pid),[pid])
    actual_annual=np.zeros(n)
    if 'whistleblower' in components:
        actual_annual+=reg['policies']['whistleblower']['annual_event_internal_equivalent_days']
    if pid=='frontier-act':actual_annual+=r['annual_emergency_equivalent_delay_days']
    actual_annual=np.minimum(annual,actual_annual)
    access_annual=np.maximum(0,annual-actual_annual)
    internal=actual_annual[:,None]*ts[None,:]+setup[:,None]*np.minimum(ts,1)[None,:]
    fallback=prod['policies']['internal-deploy']['parameters']
    new_gain=fallback['research_work_exposure']*fallback['new_model_incremental_uplift']/(1+fallback['new_model_incremental_uplift'])
    lost_use=np.minimum(1,r['recurring_internal_use_lag_days']/fallback['model_generation_days']+access_annual/YEAR)*new_gain
    rr=rr*np.power(1-lost_use[:,None]*ramp,s['labor_share'][:,None])
    serial=reg['shared']['critical_training_stages_per_year']
    d=r['training_lag_per_affected_run_days'];raw=r.get('raw_training_wait_calendar_days',d)
    preserved=1-np.divide(d,raw,out=np.zeros_like(d),where=raw>0)
    exposure=np.maximum(0,ts[None,:]*YEAR-extra['first_training_effect_days'][:,None])
    training=training_chain_penalty(raw[:,None],preserved[:,None],serial[:,None],exposure)
    direct=-s['g_total'][:,None]*(internal+training)/YEAR
    recurring=r['recurring_release_lag_days'][:,None]
    annual_rel=r['annual_event_release_equivalent_days'][:,None]
    setup_rel=r['first_year_setup_release_equivalent_days'][:,None]
    recovery=np.exp(-np.maximum(0,ts[None,:]-1)*YEAR/extra['one_time_release_recovery_days'][:,None])
    # Cycle-average public availability approximation; no multiplication by release count.
    release=(recurring+(annual_rel+setup_rel*recovery)/reg['shared']['releases_per_year'][:,None])*ramp
    params={**reg['policy_inputs'].get(pid,reg['bundle_inputs'].get(pid,{})),**extra,
      'annual_rd_input_loss_fraction':f,'annual_investment_input_loss_fraction':inv,
      'internal_gate_days':r['internal_use_lag_excluding_training_days'],
      'public_release_gate_days':r['release_lag_excluding_training_days'],
      'effective_training_wait_per_run_days':d,'critical_serial_runs_per_year':serial}
    return dict(us_c=direct,us_rr=rr,cn_c=np.zeros((n,T)),cn_rr=np.ones((n,T)),release=release,parameters=params)

def paths_for_policy(pid,inputs,feedback=True,diffusion_scale=1.):
    prod,reg,cn=(inputs[k] for k in ['production','regulation','china'])
    ts,s=prod['times'],dict(prod['shared']);n=len(s['g_total']);T=len(ts)
    if not feedback:s['eta']=np.zeros(n)
    z=np.zeros((n,T));ones=np.ones((n,T))
    if pid in prod['policies']:
        p=prod['policies'][pid]
        r=dict(us_c=p['direct_log_effect'],us_rr=p['resource_ratio'],cn_c=z,cn_rr=ones,release=z,
               parameters={**p['parameters'],**p['diagnostics']})
    elif pid in reg['policies']:
        r=_reg_paths(pid,reg['policies'][pid],inputs)
    elif pid in cn['policies']:
        p=cn['policies'][pid]
        # china paths return LABOR fractions, not already aggregated research inputs.
        r=dict(us_c=p['direct_us_logcompute'],us_rr=p['us_labor_ratio']**s['labor_share'][:,None]*p.get('us_compute_ratio',ones)**(1-s['labor_share'][:,None]),
          cn_c=p['direct_cn_logcompute'],cn_rr=p['cn_labor_ratio']**s['labor_share'][:,None]*p.get('cn_compute_ratio',ones)**(1-s['labor_share'][:,None]),release=z,parameters=cn['parameters'][pid])
        if pid=='anti-distillation':r['cn_c']=r['cn_c']*diffusion_scale
    elif pid=='pause-letter':
        return paths_for_policy('pause-6',inputs,feedback,diffusion_scale)
    elif pid in reg['bundles']:
        r=_reg_paths(pid,reg['bundles'][pid],inputs)
        for component in reg['bundles'][pid]['unowned_components']:
            p=cn['policies'][component]
            r['us_c']=r['us_c']+p['direct_us_logcompute']
            r['cn_c']=r['cn_c']+p['direct_cn_logcompute']
            r['us_rr']=r['us_rr']*p['us_labor_ratio']**s['labor_share'][:,None]*p.get('us_compute_ratio',ones)**(1-s['labor_share'][:,None])
            r['cn_rr']=r['cn_rr']*p['cn_labor_ratio']**s['labor_share'][:,None]*p.get('cn_compute_ratio',ones)**(1-s['labor_share'][:,None])
            r['parameters'].update({component+'.'+k:v for k,v in cn['parameters'][component].items()})
    else:raise KeyError(pid)
    us_a=integrate_resource_effect(s,ts,r['us_rr'],r['us_c'])
    cn_a=integrate_resource_effect(s,ts,r['cn_rr'],r['cn_c'])
    # The same research equation is used for China as a normalization approximation.
    # Knowledge-flow restrictions and theft differences are already capability effects;
    # their induced effect on research productivity enters through eta, never twice directly.
    return dict(us=r['us_c']+us_a,china=r['cn_c']+cn_a,release=r['release'],parameters=r['parameters'],
                us_direct=r['us_c'],us_algorithm=us_a,china_direct=r['cn_c'],china_algorithm=cn_a,us_rr=r['us_rr'],china_rr=r['cn_rr'],shared=s)

def evaluate(inputs,policy_ids=None,feedback=True,diffusion_scale=1.,reverse=True,universal_pause=False):
    prod,cn=(inputs[k] for k in ['production','china'])
    s,ts=prod['shared'],prod['times'];n=len(s['g_total'])
    d=common_diffusion(n,260925)
    d['teacher_spillover']=cn['shared']['phi_T']*diffusion_scale
    d['research_spillover']=cn['shared']['phi_A']*diffusion_scale
    # A common lag/absorption filter; channel-specific source priors are averaged
    # in proportion to irreducible channel reliance, preserving zero-reliance limits.
    if 'absorption_days' in cn['shared']:d['absorption_days']=cn['shared']['absorption_days']
    elif 'diffusion' in cn['shared']:
        x=cn['shared']['diffusion'];w=cn['shared']['phi_A']+cn['shared']['phi_T']
        d['absorption_days']=(cn['shared']['phi_A']*x['public_research_absorption_days']+cn['shared']['phi_T']*x['teacher_data_absorption_days'])/np.maximum(w,1.e-12)
    d['reverse_spillover']=inputs['extra']['reverse_spillover'] if reverse else np.zeros(n)
    ids=policy_ids or list(prod['policies'])+list(inputs['regulation']['policies'])+list(cn['policies'])+list(inputs['regulation']['bundles'])
    result={};draws={};drivers={}
    for pid in ids:
        p=paths_for_policy(pid,inputs,feedback,diffusion_scale)
        if universal_pause and pid in ['pause-6','pause-letter']:
            exposure=inputs['extra']['china_pause_relative_exposure'][:,None]
            p['china_direct']=p['us_direct']*exposure
            p['china_rr']=p['us_rr']**exposure
            p['china_algorithm']=integrate_resource_effect(p['shared'],ts,p['china_rr'],p['china_direct'])
            p['china']=p['china_direct']+p['china_algorithm']
        q=propagate(ts,p['us'],p['china'],p['release'],s['g_total'],d)
        converged=not feedback
        delta=0.
        # Solve incoming spillovers and research feedback jointly. propagate
        # alone adds the spillover level; integrate sees it only as AI input.
        for iteration in range(1,13) if feedback else []:
            ua=integrate_resource_effect(p['shared'],ts,p['us_rr'],p['us_direct']+q['us_reverse_spillover'])
            ca=integrate_resource_effect(p['shared'],ts,p['china_rr'],p['china_direct']+q['china_spillover'])
            ub=p['us_direct']+ua;cb=p['china_direct']+ca
            new=propagate(ts,ub,cb,p['release'],s['g_total'],d)
            delta=float(max(np.max(abs(new['us']-q['us'])/s['g_total'][:,None]*YEAR),np.max(abs(new['china']-q['china'])/s['g_total'][:,None]*YEAR)))
            p['us_algorithm']=ua;p['china_algorithm']=ca;q=new
            if delta<.001:converged=True;break
        if not converged:raise RuntimeError(f'Spillover/research fixed point failed for {pid}: {delta}days')
        horizons={}
        for h in [.5,1,3]:
            if ts[-1]<h:continue
            v=endpoint_summary(q,s['g_total'],ts,h)
            nd=v.pop('draws');horizons[str(h)]=v
            if h==1:draws[pid]=nd
        j=np.argmin(abs(ts-1));r=horizons['1']
        r['us_direct_days']=float(np.mean(-p['us_direct'][:,j]/s['g_total']*YEAR))
        r['us_research_days']=float(np.mean(-p['us_algorithm'][:,j]/s['g_total']*YEAR))
        r['china_direct_days']=float(np.mean(-p['china_direct'][:,j]/s['g_total']*YEAR))
        r['china_research_days']=float(np.mean(-p['china_algorithm'][:,j]/s['g_total']*YEAR))
        r['china_spillover_days']=float(np.mean(-q['china_spillover'][:,j]/s['g_total']*YEAR))
        r['us_reverse_spillover_days']=float(np.mean(-q['us_reverse_spillover'][:,j]/s['g_total']*YEAR))
        horizons['convergence']=dict(converged=converged,max_last_change_days=delta,iterations=iteration if feedback else 0)
        result[pid]=horizons
        pars={**p['parameters'],'algorithmic_growth':s['g_A'],'compute_growth':s['g_C'],
          'research_flow_elasticity':s['lambda_R'],'feedback_elasticity':s['eta'],
          'teacher_reliance':d['teacher_spillover'],'research_reliance':d['research_spillover']}
        rows=[]
        for k,v in pars.items():
            a=np.asarray(v)
            if a.shape!=(n,) or np.std(a)<1e-12:continue
            corr=float(np.corrcoef(a,draws[pid])[0,1])
            if np.isfinite(corr):rows.append(dict(parameter=k,pearson_correlation=corr,mean=float(a.mean())))
        drivers[pid]=sorted(rows,key=lambda x:-abs(x['pearson_correlation']))[:6]
    return dict(estimates=result,draws=draws,drivers=drivers)

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=8192);ap.add_argument('--seed',type=int,default=260925);ap.add_argument('--steps',type=int,default=52)
    ar=ap.parse_args();inputs=make_inputs(ar.n,ar.seed,ar.steps)
    out=evaluate(inputs)
    np.savez_compressed(BASE/'policy-draws.npz',**out.pop('draws'))
    out['run']=dict(n=ar.n,seed=ar.seed,steps_per_year=ar.steps,year_days=YEAR)
    (BASE/'model-results.json').write_text(json.dumps(out,indent=2)+'\n')
    for pid,h in out['estimates'].items():
        r=h['1'];print(f"{pid:28s} {r['mean_days']:9.3f}  [{r['p05_days']:9.3f}, {r['p95_days']:9.3f}]")
