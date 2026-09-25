"""Boundary, algebra, numerical convergence and scenario checks; no empirical fit claim."""
import json
from pathlib import Path
import numpy as np
from production_model import simulate, integrate_resource_effect, _data_loss, summarize, YEAR
BASE=Path(__file__).parent
checks={}
r=simulate(n=1500,seed=260925,horizon_years=3,steps_per_year=52)
s=r['shared'];t=r['times'];shape=r['baseline_log_effective_compute'].shape
assert shape==(1500,157)
for p in r['policies'].values():
    assert p['log_effective_compute'].shape==shape
    assert np.isfinite(p['log_effective_compute']).all()
    assert (p['resource_ratio']>0).all()
    assert np.allclose(p['log_effective_compute'],r['baseline_log_effective_compute']+p['direct_log_effect']+p['algorithmic_log_effect'])
checks['shapes_finiteness_positive_resources_decomposition']='passed'
r2=simulate(n=1500,seed=260925,horizon_years=3,steps_per_year=52)
assert all(np.array_equal(r['policies'][p]['log_effective_compute'],r2['policies'][p]['log_effective_compute']) for p in r['policies'])
checks['reproducible_seed']='passed'
zero=integrate_resource_effect(s,t,np.ones(shape))
assert np.max(abs(zero))==0
checks['zero_shock_zero_effect']='passed'
zlam=dict(s,lambda_R=np.zeros(1500),beta=np.zeros(1500))
assert np.max(abs(integrate_resource_effect(zlam,t,np.full(shape,.5),np.full(shape,-.5))))==0
checks['zero_research_elasticity_zero_algorithmic_effect']='passed'
no_feedback=dict(s,eta=np.zeros(1500))
no_fb={}
for pid,p in r['policies'].items():
    a=integrate_resource_effect(no_feedback,t,p['resource_ratio'],p['direct_log_effect'])
    j=52
    no_fb[pid]=float((-(a[:,j]+p['direct_log_effect'][:,j])/s['g_total']*YEAR).mean())
    if pid!='safety-compute-share':
        assert np.min(a[:,j]-p['algorithmic_log_effect'][:,j])>=-1e-12
checks['feedback_off_year1_mean_days']=no_fb
# A constant direct level shock has no algorithmic consequence when feedback is off
# and the effective research input flow is unchanged.
assert np.max(abs(integrate_resource_effect(no_feedback,t,np.ones(shape),np.full(shape,-.4))))==0
checks['constant_direct_level_not_repeated_annual_loss']='passed'
# N*/D* implied by the primary paper coefficients equals its U_N/U_D ratio.
ratio=(521/1488)**(1/.353)
assert abs(ratio-.051)<.001
checks['compute_optimal_parameter_data_ratio']=ratio
m=200
u=np.linspace(.05,1,m);rd=np.full(m,15.3878);rn=np.full(m,5.3097);alpha=np.full(m,.353)
l=_data_loss(u,rd,rn,alpha)
assert np.max(np.diff(l))<=1e-12
assert abs(_data_loss(np.ones(1),np.array([15.3878]),np.array([5.3097]),np.array([.353]))[0]-2)<1e-12
fine=_data_loss(u,rd,rn,alpha,grid_points=481)
checks['data_grid_121_vs_481_max_log_compute_error']=float(np.max(2/.353*abs(np.log(l/fine))))
assert checks['data_grid_121_vs_481_max_log_compute_error']<.001
checks['data_more_unique_monotone_and_no_constraint_boundary']='passed'
b=simulate(n=100,seed=1,horizon_years=1,overrides={'policies':{'data-licensing':{'data_needing_new_permission':0,'licensing_budget_share':0,'transition_critical_share':0}}})
assert np.max(abs(b['policies']['data-licensing']['log_effective_compute_effect']))==0
checks['data_no_loss_boundary']='passed'
# Simultaneous changes use the same pseudo-random numbers as the reference.
no_sub=simulate(n=1500,seed=260925,horizon_years=3,steps_per_year=52,overrides={'policies':{'compute-cap':{'scale_gap_recovered_other_channels':0,'blocked_compute_redeployed':0}}})
assert np.all(no_sub['policies']['compute-cap']['log_effective_compute_effect']<=r['policies']['compute-cap']['log_effective_compute_effect']+1e-12)
checks['cap_no_substitution_year1_mean_days']=summarize(no_sub)['compute-cap']['year1']['mean_days']
assert np.all(r['policies']['pause-6']['resource_ratio'][:,t>=.5]==1)
checks['pause_expires_at_half_year']='passed'
rfine=simulate(n=1500,seed=260925,horizon_years=3,steps_per_year=104)
conv={}
for pid,p in r['policies'].items():
    lag=-p['log_effective_compute_effect'][:,52]/s['g_total']*YEAR
    lagfine=-rfine['policies'][pid]['log_effective_compute_effect'][:,104]/s['g_total']*YEAR
    conv[pid]={'mean_abs_days':float(np.abs(lag-lagfine).mean()),'max_abs_days':float(np.abs(lag-lagfine).max())}
    assert conv[pid]['mean_abs_days']<.15
checks['weekly_vs_halfweekly_endpoint_convergence']=conv
modes=simulate(n=1,use_modes=True,horizon_years=3)
checks['all_parameter_modes_days']={k:{y:v['mean_days'] for y,v in x.items()} for k,x in summarize(modes).items()}
def scenario(pid,name,values):
    results=[]
    for value in values:
        z=simulate(n=1,use_modes=True,horizon_years=1,overrides={'policies':{pid:{name:value}}})
        results.append({'input_value':value,'local_year1_days':summarize(z)[pid]['year1']['mean_days']})
    return results
checks['modal_one_at_a_time_sensitivity']={
 'pause_catchup':scenario('pause-6','scale_gap_recovered_by_yearend',[0,.5,.9]),
 'cap_scale_substitution':scenario('compute-cap','scale_gap_recovered_other_channels',[0,.25,.6]),
 'internal_incremental_uplift':scenario('internal-deploy','new_model_incremental_uplift',[.05,.2,.6]),
 'approval_reviewer_utilization':scenario('ai-rnd-limits','reviewer_utilization',[.3,.65,.9]),
 'data_recovery':scenario('data-licensing','affected_data_recovered',[.2,.65,.95]),
 'safety_budget_expansion':scenario('safety-compute-share','budget_expansion',[0,.08,.25]),
}
p=modes['policies']['safety-compute-share']['parameters']
s0=p['baseline_safety_share'][0];s1=p['mandated_safety_share'][0];k=p['safety_capability_cobenefit'][0]
checks['safety_neutral_budget_expansion_at_other_modes']=(1-s0+k*s0)/(1-s1+k*s1)-1
(BASE/'production-validation.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
