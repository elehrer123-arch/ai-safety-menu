"""Produce estimates, structural sensitivities and numerical checks."""
from pathlib import Path
import json,time
import numpy as np
from unified_model import make_inputs,evaluate
BASE=Path(__file__).parent

def clean(out):
    return {k:v for k,v in out.items() if k!='draws'}

def main(n=8192,seed=260925):
    start=time.time();print('Drawing shared inputs',flush=True)
    inputs=make_inputs(n,seed)
    print('Running all 35 headline estimates',flush=True);base=evaluate(inputs)
    np.savez_compressed(BASE/'policy-draws.npz',**base['draws'])
    result=clean(base);result['run']=dict(n=n,seed=seed,steps_per_year=52,year_days=365.25)
    (BASE/'model-results.json').write_text(json.dumps(result,indent=2)+'\n')
    scenarios={}
    for label,kwargs in [('no_forward_diffusion',dict(diffusion_scale=0.)),('half_forward_diffusion',dict(diffusion_scale=.5)),('double_forward_diffusion',dict(diffusion_scale=2.)),('no_ai_research_feedback',dict(feedback=False)),('no_reverse_diffusion',dict(reverse=False))]:
        print('Sensitivity: '+label,flush=True)
        out=evaluate(inputs,**kwargs)
        scenarios[label]={p:{h:v['mean_days'] for h,v in hs.items() if h!='convergence'} for p,hs in out['estimates'].items()}
    print('Sensitivity: universal pause and alternative capability ruler',flush=True)
    out=evaluate(inputs,policy_ids=['pause-6','pause-letter'],universal_pause=True)
    scenarios['universal_pause']={p:{h:v['mean_days'] for h,v in hs.items() if h!='convergence'} for p,hs in out['estimates'].items()}
    fit=json.loads((BASE/'baseline_fit.json').read_text());print('Fit fields',list(fit),flush=True)
    slope=14.1826945717092
    mult=6.5*inputs['production']['shared']['g_total']/slope
    scenarios['fixed_6_5_eci_per_log_compute_observed_ruler']={p:{'1':float(np.mean(d*mult))} for p,d in base['draws'].items()}
    print('Numerical checks: alternate seed, time-step refinement',flush=True)
    small=make_inputs(2048,seed+71,steps=52);a=evaluate(small)
    fine=make_inputs(2048,seed+71,steps=104);b=evaluate(fine)
    convergence={p:dict(coarse_mean_days=a['estimates'][p]['1']['mean_days'],fine_mean_days=b['estimates'][p]['1']['mean_days'],absolute_step_difference_days=abs(a['estimates'][p]['1']['mean_days']-b['estimates'][p]['1']['mean_days']),alternate_seed_mean_days=a['estimates'][p]['1']['mean_days'],main_mean_days=base['estimates'][p]['1']['mean_days'],main_mc_se_days=base['estimates'][p]['1']['mc_standard_error_days']) for p in base['estimates']}
    for p,v in convergence.items():
        if v['absolute_step_difference_days']>.2:raise AssertionError('Time-step sensitivity '+p+str(v))
    (BASE/'sensitivity-results.json').write_text(json.dumps(scenarios,indent=2)+'\n')
    (BASE/'numerical-validation.json').write_text(json.dumps(dict(comparisons=convergence,max_time_step_difference_days=max(v['absolute_step_difference_days'] for v in convergence.values()),elapsed_seconds=time.time()-start),indent=2)+'\n')
    for p,h in base['estimates'].items():
        r=h['1'];print(f"{p:28s} {r['mean_days']:9.3f} [{r['p05_days']:8.3f},{r['p95_days']:8.3f}]",flush=True)
    print('Complete',round(time.time()-start,1),'seconds',flush=True)
if __name__=='__main__':main()
