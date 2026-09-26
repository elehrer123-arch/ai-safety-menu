"""Callable resource calibration for the shared 12-month fixed-U.S.-ruler engine.

sample(n=1000, seed=20260925, g_total=None, g_algo=None) yields one dictionary
per Monte Carlo draw. Each dictionary has shared and policies entries. Scalars
g_total/g_algo use log effective-compute growth/year; absent values independently
draw the root-provided log-growth priors. No days headline is computed here.

US research losses are average first-year effective-input fractions. Compute
effects include explicitly labeled endpoint and average-year fields. Security
cn_log_effect_direct is the negative of expected retained Chinese theft uplift
avoided at day365, using the SAME g_total ruler. It is already horizon-integrated;
do not multiply it by theft probability, rollout or gap again.
"""
import json, math, random
from pathlib import Path

DATA=json.loads((Path(__file__).parent/'china-calibration.json').read_text())

def _draw(items,rng):
    return {x['name']:rng.triangular(x['distribution']['low'],x['distribution']['high'],x['distribution']['mode']) for x in items}

def _modes(items):
    return {x['name']:x['distribution']['mode'] for x in items}

def _security_values(pid,x,s,g_total):
    if pid=='weight-security':
        cut=[x['newly_changed_risk_weighted_share']*x[k] for k in ('remote_risk_cut_in_changed_exposures','insider_risk_cut_in_changed_exposures','other_risk_cut_in_changed_exposures')]
    elif pid=='light-vetting':
        cut=[0,x['insider_risk_cut_in_newly_screened_exposures']*x['newly_screened_risk_weighted_share'],0]
    elif pid=='personnel-security':
        cut=[0,x['insider_risk_cut'],0]
    else:
        cut=[x[k] for k in ('remote_risk_cut','insider_risk_cut','other_risk_cut')]
    insider=s['insider_hazard_share']; other=(1-insider)*s['other_nonremote_hazard_share']
    shares=[1-insider-other,insider,other]
    mature_cut=sum(sh*c for sh,c in zip(shares,cut))
    onset=365*(1-s['security_rollout_fraction_year'])
    lam=-math.log1p(-s['annual_useful_frontier_compromise_probability'])/365
    lam_after=lam*(1-mature_cut)
    cutoff=365-s['compromise_absorption_days']
    k=math.log(2)/s['compromise_advantage_half_life_days']
    def segment(start,end,hazard,survival):
        if end<=start: return 0.
        v=k-hazard
        integral=math.expm1(v*(end-start))/v if abs(v)>1e-12 else end-start
        return survival*hazard*math.exp(-k*(cutoff-start))*integral
    base=segment(0,cutoff,lam,1)
    before=segment(0,min(cutoff,onset),lam,1)
    after=segment(onset,cutoff,lam_after,math.exp(-lam*onset))
    value=s['relevant_asset_gap_days']/365*g_total*s['compromise_gap_fraction_recovered']
    effect=(base-before-after)*value
    p_after=1-math.exp(-lam*onset-lam_after*(365-onset))
    return dict(cn_log_effect_direct=-effect,security_avoided_expected_endpoint_log_uplift=effect,
                annual_compromise_probability_reduction=s['annual_useful_frontier_compromise_probability']-p_after,
                mature_route_hazard_cuts=dict(zip(('remote','insider','other'),cut)),
                security_control_onset_day=onset)

def evaluate_draw(inputs,s,d,g_total,g_algo,include_paths=False):
    shares=['public_research_channel_share','frontier_teacher_channel_share','released_weights_channel_share','researcher_transfer_channel_share']
    scale=min(1,.9/sum(d[k] for k in shares))
    d=dict(d)
    for key in shares:d[key]*=scale
    phi_t=(g_algo/g_total)*d['frontier_teacher_channel_share']*(1-d['teacher_substitution_recovery'])
    phi_a=(g_algo/g_total)*d['public_research_channel_share']*(1-d['public_research_substitution_recovery'])
    out={}
    for pid,x in inputs.items():
        z={}
        if pid=='export-controls':
            lag=x['deployment_lag_days']/365;f=.5*(1-lag)**2
            annual=(x['nvidia_annual_output_h100e']*x['incremental_china_purchase_share']+x['extra_domestic_output_after_relaxation'])*x['usable_fraction_of_added_rated_compute']
            add_avg=annual*f;add_end=annual*(1-lag)
            base_end=x['baseline_china_average_usable_compute']*x['endpoint_to_average_compute_ratio']
            relevance=x['share_relevant_to_frontier_progress']
            # Partial relevance is an elasticity on log compute, not an extra multiplication of delay.
            cn_log=-relevance*math.log1p(add_end/base_end)
            redirected=x['redirected_share_to_us_under_controls']*x['nvidia_annual_output_h100e']*x['incremental_china_purchase_share']*x['usable_fraction_of_added_rated_compute']
            usbaseend=x['baseline_us_average_usable_compute']*x['endpoint_to_average_compute_ratio']
            usgain_end=redirected*(1-lag)/usbaseend
            z=dict(cn_compute_log_effect_endpoint=cn_log,cn_compute_loss_fraction_endpoint=1-math.exp(cn_log),
                   cn_compute_loss_fraction_average=relevance*add_avg/(x['baseline_china_average_usable_compute']+add_avg),
                   us_compute_log_effect_endpoint=math.log1p(usgain_end),us_compute_gain_fraction_endpoint=usgain_end,
                   us_research_input_loss_fraction=x['supplier_innovation_loss_us'])
            if include_paths:
                z['cn_compute_log_effect_monthly']=[-relevance*math.log1p(annual*max(t/12-lag,0)/(x['baseline_china_average_usable_compute']*(2-x['endpoint_to_average_compute_ratio']+2*(x['endpoint_to_average_compute_ratio']-1)*t/12))) for t in range(13)]
        elif pid=='kyc-compute':
            loss=x['cn_covered_cloud_compute_share']*x['incremental_detection']*x['denial_after_detection']*(1-x['replacement_share'])
            z=dict(cn_compute_loss_fraction_endpoint=loss,cn_compute_log_effect_endpoint=math.log1p(-loss),cn_compute_loss_fraction_average=loss*x['rollout_fraction_year'],us_compute_loss_fraction_average=x['us_new_contract_exposure']*x['check_elapsed_days']*x['blocking_fraction']/365,rollout_onset_day=365*(1-x['rollout_fraction_year']))
        elif pid=='anti-distillation':
            z=dict(cn_algorithmic_knowledge_flow_loss_fraction=d['frontier_teacher_channel_share']*x['additional_blocked_teacher_access']*(1-d['teacher_substitution_recovery'])*x['rollout_fraction_year'],
                   cn_log_effect_direct=-g_total*phi_t*x['additional_blocked_teacher_access']*x['rollout_fraction_year'],
                   us_research_input_loss_fraction=x['us_research_staff_reassigned_share']*x['implementation_work_days']/365+x['us_research_product_friction'])
        elif pid=='weight-security':
            z['us_research_input_loss_fraction']=x['us_research_staff_reassigned_share']*x['implementation_work_days']/365+x['ongoing_research_friction']
        elif pid=='light-vetting':
            z['us_research_input_loss_fraction']=(x['annual_hires_relative_to_staff']*x['newly_screened_share']*x['screening_calendar_days']*x['screening_blocks_start_fraction']+x['newly_screened_incumbent_share']*x['incumbent_productive_days_lost'])/365
        elif pid=='personnel-security':
            a=x['sensitive_research_role_share']*(1-x['already_equivalently_vetted_share']);w=min(x['clearance_process_days'],365)/365
            dep=a*x['covered_staff_departure_or_foregone_hire_fraction']*x['departure_year_exposure_fraction']
            z['us_research_input_loss_fraction']=min(.95,a*x['annual_hires_relative_to_staff']*x['new_hire_productivity_blocked_fraction']*(w-w*w/2)+a*x['incumbent_blocked_share']*x['incumbent_productivity_blocked_fraction']*w+dep*x['lost_capacity_unreplaced_fraction'])
            z['cn_research_input_gain_fraction']=dep*x['china_destination_share']*x['us_to_cn_research_capacity_ratio']*x['china_first_year_transfer_productivity']
        elif pid=='secure-dev-env':
            z['us_research_input_loss_fraction']=x['newly_affected_research_share']*x['within_environment_productivity_loss']*s['security_rollout_fraction_year']+x['migration_research_input_loss']
        if pid in ('weight-security','light-vetting','personnel-security','secure-dev-env'):
            z.update(_security_values(pid,x,s,g_total))
        out[pid]=z
    return dict(shared=dict(g_total=g_total,g_algo=g_algo,phi_T=phi_t,phi_A=phi_a,security=s,diffusion=d),policies=out)

def sample(n=1000,seed=20260925,g_total=None,g_algo=None,include_inputs=False,include_paths=False):
    rng=random.Random(seed)
    for _ in range(n):
        s=_draw(DATA['shared_security_inputs'],rng);d=_draw(DATA['diffusion_inputs'],rng)
        p={z['id']:_draw(z['inputs'],rng) for z in DATA['policies']}
        # Correlate same hiring-flow construct instead of drawing incompatible lab populations.
        p['light-vetting']['annual_hires_relative_to_staff']=p['personnel-security']['annual_hires_relative_to_staff']
        ga=g_algo if g_algo is not None else rng.triangular(math.log(1.5),math.log(10),math.log(3.5))
        gt=g_total if g_total is not None else ga+rng.triangular(math.log(2),math.log(8),math.log(4.5))
        value=evaluate_draw(p,s,d,gt,ga,include_paths)
        if include_inputs:value['inputs']=p
        yield value

def mode_result(g_total=math.log(4.5)+math.log(3.5),g_algo=math.log(3.5)):
    return evaluate_draw({p['id']:_modes(p['inputs']) for p in DATA['policies']},_modes(DATA['shared_security_inputs']),_modes(DATA['diffusion_inputs']),g_total,g_algo,True)

def china_paths(n, seed, times, g_total, g_algo):
    """Vectorized root integration. `times` is years, using 365.25 days/year.

    Returns shared phi_T, phi_A arrays and per-policy N x T arrays:
      direct_us_logcompute, direct_cn_logcompute, us_labor_ratio, cn_labor_ratio,
      us_compute_ratio, cn_compute_ratio.
    Direct includes expected theft/teacher knowledge effects in the shared
    log-effective-compute units, not just physical GPU stock. Root must not add
    those terms again. Root maps labor ratios via its production function.
    Compute ratios are physical/resource-channel ratios for research capital;
    they equal one for teacher and security effects. Export China ratios use
    the same frontier-relevance exponent as the direct training-compute effect.

    Compute-stock extension: positive exponential baseline; its growth rate is
    solved from end-year/average-year stock ratio. Additional deliveries follow
    this same growth rate, normalized to calibrated first-year purchase flow,
    after delivery lag. This is a current-technology scenario beyond year1.

    Labor ratios: constant first-year-equivalent input changes over positive
    horizons, explicitly a reduced-form proxy. Thus repeated first-year setup
    burden in 36mo is a conservative continuation assumption, not observed data.

    Security default: most recent useful compromise, bounded by one current
    gap transfer, which preserves monotonicity under hazard reduction. Also
    returns first-event diagnostic to expose event-selection/depreciation issue.
    """
    import numpy as np
    rng=np.random.default_rng(seed);Y=365.25
    t=np.asarray(times,dtype=float)
    if t.ndim!=1 or np.any(t<0):raise ValueError('times must be nonnegative one-dimensional years')
    def draws(items):
        out={}
        for it in items:
            a,m,b=(it['distribution'][k] for k in ('low','mode','high'))
            out[it['name']]=np.full(n,a,dtype=float) if a==b else rng.triangular(a,m,b,n)
        return out
    def vec(x):
        a=np.asarray(x,dtype=float)
        if a.ndim==0:return np.full(n,float(a))
        if a.shape!=(n,):raise ValueError('growth arrays must have shape (n,)')
        return a
    gt=vec(g_total);ga=vec(g_algo)
    if np.any(gt<=0) or np.any(ga<0) or np.any(ga>gt):raise ValueError('require 0<=g_algo<=g_total and g_total>0')
    s=draws(DATA['shared_security_inputs']);d=draws(DATA['diffusion_inputs'])
    pp={p['id']:draws(p['inputs']) for p in DATA['policies']}
    pp['light-vetting']['annual_hires_relative_to_staff']=pp['personnel-security']['annual_hires_relative_to_staff'].copy()
    keys=['public_research_channel_share','frontier_teacher_channel_share','released_weights_channel_share','researcher_transfer_channel_share']
    scale=np.minimum(1,.9/sum(d[k] for k in keys))
    for k in keys:d[k]*=scale
    pt=(ga/gt)*d['frontier_teacher_channel_share']*(1-d['teacher_substitution_recovery'])
    pa=(ga/gt)*d['public_research_channel_share']*(1-d['public_research_substitution_recovery'])
    T=t[None,:];zero=np.zeros((n,len(t)));one=np.ones_like(zero)
    policies={}
    def const(v):return np.broadcast_to(v[:,None],zero.shape).copy()
    for pid,x in pp.items():
        z=dict(direct_us_logcompute=zero.copy(),direct_cn_logcompute=zero.copy(),us_labor_ratio=one.copy(),cn_labor_ratio=one.copy(),us_compute_ratio=one.copy(),cn_compute_ratio=one.copy())
        if pid=='export-controls':
            # Positive exponential stock, preserving the calibrated mean and endpoint/mean ratio.
            lo=np.full(n,1e-8);hi=np.full(n,5.)
            for _ in range(50):
                k=(lo+hi)/2;r=k/(-np.expm1(-k))
                lo=np.where(r<x['endpoint_to_average_compute_ratio'],k,lo)
                hi=np.where(r>=x['endpoint_to_average_compute_ratio'],k,hi)
            k=(lo+hi)/2
            c0=x['baseline_china_average_usable_compute']*k/np.expm1(k)
            u0=x['baseline_us_average_usable_compute']*k/np.expm1(k)
            elapsed=np.maximum(T-x['deployment_lag_days'][:,None]/Y,0)
            delivery_factor=np.expm1(k[:,None]*elapsed)/np.expm1(k)[:,None]
            annual=(x['nvidia_annual_output_h100e']*x['incremental_china_purchase_share']+x['extra_domestic_output_after_relaxation'])*x['usable_fraction_of_added_rated_compute']
            extra=annual[:,None]*delivery_factor
            baseline=c0[:,None]*np.exp(k[:,None]*T)
            z['direct_cn_logcompute']=-x['share_relevant_to_frontier_progress'][:,None]*np.log1p(extra/baseline)
            redirect=x['redirected_share_to_us_under_controls']*x['nvidia_annual_output_h100e']*x['incremental_china_purchase_share']*x['usable_fraction_of_added_rated_compute']
            z['direct_us_logcompute']=np.log1p(redirect[:,None]*delivery_factor/(u0[:,None]*np.exp(k[:,None]*T)))
            z['us_labor_ratio']=const(1-x['supplier_innovation_loss_us'])
            z['diagnostics']={'positive_initial_china_compute_million_h100e':c0,'positive_initial_us_compute_million_h100e':u0,'baseline_stock_log_growth_per_year':k}
        elif pid=='kyc-compute':
            onset=1-x['rollout_fraction_year'];active=T>=onset[:,None]
            loss=x['cn_covered_cloud_compute_share']*x['incremental_detection']*x['denial_after_detection']*(1-x['replacement_share'])
            z['direct_cn_logcompute']=np.log1p(-loss)[:,None]*active
            usloss=x['us_new_contract_exposure']*x['check_elapsed_days']*x['blocking_fraction']/Y
            z['direct_us_logcompute']=np.log1p(-usloss)[:,None]*active
        elif pid=='anti-distillation':
            active_years=np.maximum(T-(1-x['rollout_fraction_year'])[:,None],0)
            z['direct_cn_logcompute']=-(gt*pt*x['additional_blocked_teacher_access'])[:,None]*active_years
            usloss=x['us_research_staff_reassigned_share']*x['implementation_work_days']/Y+x['us_research_product_friction']
            z['us_labor_ratio']=const(1-usloss)
        elif pid=='weight-security':
            usloss=x['us_research_staff_reassigned_share']*x['implementation_work_days']/Y+x['ongoing_research_friction']
            z['us_labor_ratio']=const(1-usloss)
        elif pid=='light-vetting':
            usloss=(x['annual_hires_relative_to_staff']*x['newly_screened_share']*x['screening_calendar_days']*x['screening_blocks_start_fraction']+x['newly_screened_incumbent_share']*x['incumbent_productive_days_lost'])/Y
            z['us_labor_ratio']=const(1-usloss)
        elif pid=='personnel-security':
            a=x['sensitive_research_role_share']*(1-x['already_equivalently_vetted_share']);w=np.minimum(x['clearance_process_days'],Y)/Y
            dep=a*x['covered_staff_departure_or_foregone_hire_fraction']*x['departure_year_exposure_fraction']
            usloss=np.minimum(.95,a*x['annual_hires_relative_to_staff']*x['new_hire_productivity_blocked_fraction']*(w-w*w/2)+a*x['incumbent_blocked_share']*x['incumbent_productivity_blocked_fraction']*w+dep*x['lost_capacity_unreplaced_fraction'])
            gain=dep*x['china_destination_share']*x['us_to_cn_research_capacity_ratio']*x['china_first_year_transfer_productivity']
            z['us_labor_ratio']=const(1-usloss);z['cn_labor_ratio']=const(1+gain)
        elif pid=='secure-dev-env':
            usloss=x['newly_affected_research_share']*x['within_environment_productivity_loss']*s['security_rollout_fraction_year']+x['migration_research_input_loss']
            z['us_labor_ratio']=const(1-usloss)
        if pid in ('weight-security','light-vetting','personnel-security','secure-dev-env'):
            if pid=='weight-security':cuts=np.stack([x['newly_changed_risk_weighted_share']*x[key] for key in ('remote_risk_cut_in_changed_exposures','insider_risk_cut_in_changed_exposures','other_risk_cut_in_changed_exposures')],axis=1)
            elif pid=='light-vetting':cuts=np.stack([np.zeros(n),x['insider_risk_cut_in_newly_screened_exposures']*x['newly_screened_risk_weighted_share'],np.zeros(n)],axis=1)
            elif pid=='personnel-security':cuts=np.stack([np.zeros(n),x['insider_risk_cut'],np.zeros(n)],axis=1)
            else:cuts=np.stack([x[key] for key in ('remote_risk_cut','insider_risk_cut','other_risk_cut')],axis=1)
            z['mature_route_hazard_cuts']=cuts
            z.update(security_paths(s,cuts,t,gt))
        # Resource-input ratios at t=0 are policy-on input choices, but direct level shocks start at zero.
        z['direct_us_logcompute'][:,t==0]=0;z['direct_cn_logcompute'][:,t==0]=0
        if pid in ('export-controls','kyc-compute'):
            z['us_compute_ratio']=np.exp(z['direct_us_logcompute'])
            z['cn_compute_ratio']=np.exp(z['direct_cn_logcompute'])
        policies[pid]=z
    return dict(times=t,year_days=Y,shared=dict(phi_T=pt,phi_A=pa,g_total=gt,g_algo=ga,security=s,diffusion=d),policies=policies,parameters=pp,
                extension_assumptions=['Positive exponential baseline compute and proportionately growing sales flow beyond year1, at fixed 2026 chip mix.', 'Constant first-year-equivalent labor ratio for longer-horizon sensitivity; not a measured steady-state policy burden.', 'Teacher knowledge loss accumulates after implementation under fixed marginal reliance.', 'Security uses most recent useful theft, bounding retained uplift by one current-gap transfer. First-event diagnostic also supplied.'])

def security_paths(s, mature_route_cuts, times, g_total):
    """Vectorized retained endpoint theft value; all external arrays shared.

    For bundle accounting call this once on combined_hazard_cuts(...).
    Cuts order is remote, insider, other. Returns direct CN log effect and
    diagnostic first-event effect; negative direct effect means China slower.
    """
    import numpy as np
    Y=365.25;t=np.asarray(times)[None,:]*Y;gt=np.asarray(g_total)
    if gt.ndim==0:gt=np.full(len(s['annual_useful_frontier_compromise_probability']),float(gt))
    ins=s['insider_hazard_share'];other=(1-ins)*s['other_nonremote_hazard_share']
    shares=np.stack([1-ins-other,ins,other],axis=1)
    r=(shares*mature_route_cuts).sum(axis=1)[:,None]
    lam=(-np.log1p(-s['annual_useful_frontier_compromise_probability'])/Y)[:,None]
    reduced=lam*(1-r);onset=(Y*(1-s['security_rollout_fraction_year']))[:,None]
    cutoff=np.maximum(t-s['compromise_absorption_days'][:,None],0)
    k=(np.log(2)/s['compromise_advantage_half_life_days'])[:,None]
    end=np.minimum(cutoff,onset);dur_after=np.maximum(cutoff-onset,0)
    def recent_segment(duration,hazard,age_at_end,survival_after):
        return hazard*survival_after*np.exp(-k*age_at_end)*(-np.expm1(-(hazard+k)*duration))/(hazard+k)
    baseline=recent_segment(cutoff,lam,np.zeros_like(cutoff),1)
    pre=recent_segment(end,lam,cutoff-end,np.exp(-reduced*dur_after))
    post=recent_segment(dur_after,reduced,np.zeros_like(cutoff),1)
    value=(s['relevant_asset_gap_days']/Y*gt*s['compromise_gap_fraction_recovered'])[:,None]
    monotone=(baseline-pre-post)*value
    def first_segment(start,duration,hazard,survival):
        v=k-hazard
        factor=np.where(np.abs(v)>1e-12,np.expm1(v*duration)/v,duration)
        return survival*hazard*np.exp(-k*(cutoff-start))*factor
    first_base=first_segment(0,cutoff,lam,1)
    first_pre=first_segment(0,end,lam,1)
    first_post=first_segment(onset,dur_after,reduced,np.exp(-lam*onset))
    first=(first_base-first_pre-first_post)*value
    return dict(direct_cn_logcompute=-monotone,security_avoided_expected_endpoint_log_uplift=monotone,
                security_first_event_diagnostic_log_uplift=first,
                annualized_baseline_hazard=lam[:,0]*Y,security_control_onset_day=onset[:,0])

def combined_hazard_cuts(policy_cut_arrays):
    """Overlap-aware N x 3 hazard reduction for selected security policies.

    Light is nested in clearance vetting. Weight controls are nested in secure
    environment by route. Technical and personnel controls act on different
    stages and multiply remaining insider hazard. Source correlation remains
    an analyst assumption; maximum-only is a useful conservative sensitivity.
    """
    import numpy as np
    vals=list(policy_cut_arrays.values())
    if not vals:raise ValueError('supply at least one N x 3 cuts array')
    zero=np.zeros_like(vals[0]);technical=zero.copy();personnel=zero.copy()
    for p in ('weight-security','secure-dev-env'):
        if p in policy_cut_arrays:technical=np.maximum(technical,policy_cut_arrays[p])
    for p in ('light-vetting','personnel-security'):
        if p in policy_cut_arrays:personnel=np.maximum(personnel,policy_cut_arrays[p])
    return 1-(1-technical)*(1-personnel)

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=10000);ap.add_argument('--seed',type=int,default=20260925);args=ap.parse_args()
    from statistics import mean
    draws=list(sample(args.n,args.seed));summary={}
    for pid in draws[0]['policies']:
        summary[pid]={key:mean(x['policies'][pid][key] for x in draws) for key in draws[0]['policies'][pid] if isinstance(draws[0]['policies'][pid][key],(int,float))}
    print(json.dumps(dict(n=args.n,seed=args.seed,mean_phi_T=mean(x['shared']['phi_T'] for x in draws),mean_phi_A=mean(x['shared']['phi_A'] for x in draws),mean_resource_outputs=summary),indent=2))
