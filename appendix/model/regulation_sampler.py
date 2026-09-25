"""Sample documented input priors and compose shared regulatory gates.

No network or writes on import. No national-lead calculation occurs here.
Input n/seed returns numpy arrays plus metadata. Values represent epistemic
parameter draws of conditional expected event losses; Bernoulli realizations
are not additionally sampled. Annual events are tagged, not multiplied by cadence.
"""
from pathlib import Path
import json
from itertools import product
import numpy as np

DEFAULT_CALIBRATION=Path(__file__).with_name('regulation-calibration.json')

def expected_maximum(gates):
    """Exact E[max(gates)] conditional on parameters and independent gate events.

    Each gate is [(outcome_probability, outcome_calendar_days), ...]. Outcomes
    inside a gate are mutually exclusive; gates are independent conditional on
    the shared parameter draws. Shared tasks must be supplied once, not repeated.
    This integrates event risk without turning parameter uncertainty into random
    realized policy histories. Max(E[X]) is generally not E[max(X)].
    """
    if not gates:
        return 0.0
    result=np.zeros_like(np.asarray(gates[0][0][1],dtype=float))
    for outcomes in product(*gates):
        probability=1.0
        maximum=0.0
        for p,d in outcomes:
            probability=probability*p
            maximum=np.maximum(maximum,d)
        result=result+probability*maximum
    return result

def training_chain_penalty(raw_wait_days, preserved_progress_fraction,
                           critical_stages_per_year=1.5, horizon_days=365.25,
                           year_days=365.25):
    """Continuous-progress first-year approximation for a serial training chain.

    Return equivalent lost progress days, capped at the horizon. Only stages on
    one serial critical chain count. Parallel qualifying runs scale labor but
    never multiply this delay. Preserved progress is applied exactly once.
    Inputs are epistemic conditional means; this is not an exact model-release
    hitting time, and assumes no later catch-up of foregone capability work.
    """
    w=np.asarray(raw_wait_days)
    f=np.asarray(preserved_progress_fraction)
    k=np.asarray(critical_stages_per_year)
    if np.any(w<0) or np.any((f<0)|(f>1)) or np.any(k<0):
        raise ValueError('Invalid training schedule input')
    # horizon_days is elapsed *eligible* exposure, after any parent-specified
    # inherited pipeline/grandfathering delay. No initial pipeline delay here.
    elapsed=np.maximum(0,np.asarray(horizon_days))
    return np.minimum(elapsed,w*k*elapsed/year_days)*(1-f)

def gate_release_dates(planned_release_days, holds):
    """Apply dated annual/setup holds to releases, without propagating a backlog.

    Each hold=(start,end). Mask is start <= currently_ready_date < end; dates at
    end are allowed. Iterate until no remaining hold contains a ready date.
    An annual audit that ends before a later release does not delay that release.
    Pass genuinely sequential production dependencies separately, not as holds.
    """
    actual=np.array(planned_release_days,dtype=float,copy=True)
    windows=sorted(holds)
    if any(start>end for start,end in windows):
        raise ValueError('Hold end precedes start')
    for start,end in windows:
        actual=np.where((actual>=start)&(actual<end),end,actual)
    return actual

def sample_regulation(n=10000, seed=260925, calibration_path=None, overrides=None):
    data=json.loads(Path(calibration_path or DEFAULT_CALIBRATION).read_text())
    rng=np.random.default_rng(seed)
    overrides=overrides or {}
    def draw(items,scope):
        out={}
        for i in items:
            d=dict(i['distribution']);key=scope+'.'+i['name']
            if key in overrides:
                v=overrides[key]
                if isinstance(v,(float,int)):
                    out[i['name']]=np.full(n,v,dtype=float);continue
                d.update(v)
            lo,mo,hi=[d[k] for k in ('low','mode','high')]
            if not lo<=mo<=hi:raise ValueError(key)
            out[i['name']]=np.full(n,mo,dtype=float) if lo==hi else rng.triangular(lo,mo,hi,n)
        return out
    shared=draw(data['shared_inputs'],'shared')
    if 'shared.baseline_access_runway' not in overrides:
        # Four release clusters, not eight independent models. The last is a
        # conservative test-start proxy, not observed earliest possible access.
        historical=rng.choice([12.,21.,28.,21.],n)+shared['runway_transport_shift']
        short=rng.random(n)<shared['short_unobserved_runway_probability']
        shared['baseline_access_runway']=np.maximum(0,np.where(short,shared['short_unobserved_runway'],historical))
    out={};inputs={};meta={}
    for p in data['policies']:
        pid=p['policy_id'];v=draw(p['inputs'],pid);inputs[pid]=v
        env={**shared,**v,'maximum':np.maximum,'minimum':np.minimum};r={}
        for key,f in p['formula_suggestion'].items():
            val=np.asarray(eval(f,{'__builtins__':{}},env))
            if val.ndim==0:val=np.full(n,val,dtype=float)
            if not np.all(np.isfinite(val)):raise ValueError(pid+':'+key)
            r[key]=val;env[key]=val
        out[pid]=r
        meta[pid]={k:p[k] for k in ('annual_event_internal_delay','annual_event_release_delay','one_time_release_gate','first_year_setup_internal_delay','training_note') if k in p}
    zero=lambda:np.zeros(n)
    one=lambda:np.ones(n)
    def binary(probability,days):
        return [(1-probability,zero()),(probability,days)]
    def thin(gate,probability):
        # A shared applicability/internal-use gate precedes all outcomes.
        return [(1-probability,zero())]+[(p*probability,d) for p,d in gate]
    gates={}
    for pid,v in inputs.items():
        rel=[(one(),out[pid]['release_lag_excluding_training_days'])]
        internal=[(one(),out[pid]['internal_use_lag_excluding_training_days'])]
        if pid=='safety-framework':
            rel=binary(v['binding_event_probability'],v['binding_event_delay'])
            internal=binary(v['binding_event_probability']*v['internal_gate_fraction'],v['binding_event_delay'])
        elif pid=='transparency-report':
            rel=binary(v['late_report_probability'],v['report_tail_days'])
        elif pid=='whistleblower':
            internal=binary(v['extra_investigation_probability'],v['investigation_hold_days']*v['affected_research_fraction'])
        elif pid=='shutdown':
            rel=binary(v['architecture_change_probability'],v['architecture_change_days'])
            internal=binary(v['architecture_change_probability'],v['architecture_change_days']*v['affected_research_fraction'])
        elif pid=='third-party-audit':
            rel=binary(v['blocking_finding_probability'],v['finding_remediation_days'])
            internal=binary(v['blocking_finding_probability']*v['internal_gate_fraction'],v['finding_remediation_days'])
        elif pid=='internal-evals':
            days=np.maximum(0,v['incremental_service_days']-v['remaining_non_eval_buffer'])
            rel=binary(v['incremental_test_probability'],days)
            internal=binary(v['incremental_test_probability']*v['internal_gate_fraction'],days)
        elif pid=='third-party-eval':
            p=v['new_eval_probability'];q=v['late_report_probability']
            days=np.maximum(0,shared['standard_eval_service']+shared['external_queue']-shared['baseline_access_runway']-shared['earlier_sharing_gain'])
            rel=[(p,days),((1-p)*q,v['report_tail_days']),((1-p)*(1-q),zero())]
            internal=thin(rel,v['internal_gate_fraction'])
        elif pid=='evaluator-window':
            base=np.maximum(0,v['floor_calendar_days']-shared['baseline_access_runway']-shared['earlier_sharing_gain'])
            p=shared['late_checkpoint_reset_probability']
            rel=[(1-p,base),(p,base+shared['late_checkpoint_reset_days'])]
            internal=thin(rel,v['internal_gate_fraction'])
        elif pid=='triggered-redteam':
            p=v['danger_trigger_probability']*v['incrementally_binding_fraction']
            days=v['remediation_service_days']*(1-v['prepared_fraction'])
            rel=binary(p,days)
            internal=binary(p*v['internal_gate_fraction'],days)
        gates[pid]={'release':rel,'internal':internal}
    def maxgate(cs,key):return np.maximum.reduce([out[c][key] for c in cs]) if cs else zero()
    sums=lambda cs,key:sum((out[c][key] for c in cs),zero())
    def mean_gate(g):return sum((p*d for p,d in g),zero())
    def annual_union(days):
        # Independent uniformly timed interruptions: expected occupied days.
        # This is an exposure approximation; dated-window masks are preferable.
        active=one()
        for d in days:active*=1-np.minimum(1,d/365.25)
        return 365.25*(1-active)
    for pid,r in out.items():
        m=meta[pid]
        r['recurring_release_lag_days']=zero() if m.get('annual_event_release_delay') or m.get('one_time_release_gate') else r['release_lag_excluding_training_days']
        r['recurring_internal_use_lag_days']=zero() if m.get('annual_event_internal_delay') or m.get('first_year_setup_internal_delay') else r['internal_use_lag_excluding_training_days']
        r['annual_event_release_equivalent_days']=r['release_lag_excluding_training_days'] if m.get('annual_event_release_delay') else zero()
        r['annual_event_internal_equivalent_days']=r['internal_use_lag_excluding_training_days'] if m.get('annual_event_internal_delay') else zero()
        r['first_year_setup_release_equivalent_days']=r['release_lag_excluding_training_days'] if m.get('one_time_release_gate') else zero()
        r['first_year_setup_internal_equivalent_days']=r['internal_use_lag_excluding_training_days'] if m.get('first_year_setup_internal_delay') else zero()
    B={};BI={}
    for b in data['bundles']:
        pid=b['policy_id'];v=draw(b['inputs'],pid);BI[pid]=v
        cs=[c for c in b['components'] if c in out]
        r={k:zero() for k in ('annual_displaced_rd_workdays','annual_rd_input_loss_fraction','annual_investment_input_loss_fraction','release_lag_excluding_training_days','internal_use_lag_excluding_training_days','training_lag_per_affected_run_days','raw_training_wait_calendar_days')}
        overlap=v.get('common_compliance_labor_overlap',zero())
        r['annual_displaced_rd_workdays']=sums(cs,'annual_displaced_rd_workdays')*(1-overlap)
        # Keep original max-of-means as an explicit lower bound, not the estimate.
        r['release_max_of_means_lower_bound_days']=maxgate(cs,'release_lag_excluding_training_days')
        r['internal_max_of_means_lower_bound_days']=maxgate(cs,'internal_use_lag_excluding_training_days')
        release_gates=[gates[c]['release'] for c in cs]
        internal_gates=[gates[c]['internal'] for c in cs]
        r['release_lag_excluding_training_days']=expected_maximum(release_gates) if cs else zero()
        r['internal_use_lag_excluding_training_days']=expected_maximum(internal_gates) if cs else zero()
        if pid=='raise-act':
            # Legal/staff filing mostly specialists, reuses framework's counterfactual research share.
            r['annual_displaced_rd_workdays']+=v['extra_state_filing_staff_days']*inputs['safety-framework']['research_counterfactual_fraction']
        elif pid=='sb-1047':
            r['raw_training_wait_calendar_days']=v['pretraining_protocol_residual_probability']*v['pretraining_protocol_residual_days']
            r['training_lag_per_affected_run_days']=r['raw_training_wait_calendar_days']
        elif pid=='eu-ai-act':
            # Conditional appropriate window; all work/other rules retained regardless applicability.
            ordinary=[c for c in cs if c!='evaluator-window']
            local_release=expected_maximum([gates[c]['release'] for c in ordinary]+[thin(gates['evaluator-window']['release'],v['access_floor_applies_probability'])])
            r['regional_release_lag_days']=local_release
            r['release_lag_excluding_training_days']=local_release*v['global_release_synchronization_probability']
            r['internal_use_lag_excluding_training_days']=expected_maximum([gates[c]['internal'] for c in ordinary]+[thin(gates['evaluator-window']['internal'],v['access_floor_applies_probability'])])*v['global_release_synchronization_probability']
        elif pid=='ai-risk-evaluation-act':
            # Special government process replaces ordinary external process; no duplicate queue.
            govtail=np.maximum(0,shared['standard_eval_service']+v['classified_extra_service_days']+v['government_queue_days']-shared['baseline_access_runway']-shared['earlier_sharing_gain'])
            govgate=binary(v['completion_required_probability'],govtail)
            r['release_lag_excluding_training_days']=expected_maximum([govgate,gates['internal-evals']['release']])
            r['internal_use_lag_excluding_training_days']=expected_maximum([thin(govgate,inputs['third-party-eval']['internal_gate_fraction']),gates['internal-evals']['internal']])
        elif pid=='secure-ai-development-act':
            tail=np.maximum(0,v['required_calendar_access']+v['weights_handoff_extra_days']-shared['baseline_access_runway']-shared['earlier_sharing_gain'])
            tail+=shared['late_checkpoint_reset_probability']*shared['late_checkpoint_reset_days']
            r['release_lag_excluding_training_days']=tail
            r['internal_use_lag_excluding_training_days']=tail*inputs['evaluator-window']['internal_gate_fraction']
            r['annual_displaced_rd_workdays']+=shared['releases_per_year']*v['additional_staff_days']*inputs['evaluator-window']['research_counterfactual_fraction']
        elif pid=='frontier-act':
            r['annual_displaced_rd_workdays']+=out['third-party-audit']['annual_displaced_rd_workdays']*v['second_audit_increment_fraction']*(1-overlap)
            r['annual_displaced_rd_workdays']*=1-v['preempted_duplicate_labor_fraction']
            emergency=v['emergency_order_probability']*v['emergency_order_days']
            emergency_gate=binary(v['emergency_order_probability'],v['emergency_order_days'])
            av=inputs['third-party-audit']
            audit2=binary(av['blocking_finding_probability']*v['second_audit_new_finding_fraction'],av['finding_remediation_days'])
            r['release_lag_excluding_training_days']=expected_maximum(release_gates+[audit2,emergency_gate])
            r['internal_use_lag_excluding_training_days']=expected_maximum(internal_gates+[thin(audit2,av['internal_gate_fraction']),emergency_gate])
            r['annual_emergency_equivalent_delay_days']=emergency
        r['annual_rd_input_loss_fraction']=r['annual_displaced_rd_workdays']/(shared['rd_staff']*shared['workdays_per_FTE_year'])
        r['unowned_components']=[c for c in b['components'] if c not in out]
        r['composition_note']=b['overlap_rule']
        r['event_dependence_note']='Exact event integration conditional on shared parameters; distinct incremental binding events independent. Shared task prerequisites occur once. Maxima assume simultaneous readiness, not a fully dated release schedule. Annual/setup and per-model events must be assigned their recurrence masks below.'
        r['recurrence_masks']={c:dict(release=('annual_event' if meta[c].get('annual_event_release_delay') else 'first_year_setup' if meta[c].get('one_time_release_gate') else 'per_model'),internal=('annual_event' if meta[c].get('annual_event_internal_delay') else 'first_year_setup' if meta[c].get('first_year_setup_internal_delay') else 'per_model')) for c in cs}
        if pid=='frontier-act':
            r['recurrence_masks']['second_verification']={'release':'annual_event','internal':'annual_event'}
            r['recurrence_masks']['emergency_order']={'release':'annual_event','internal':'annual_event'}
        recurring_rel=[gates[c]['release'] for c in cs if r['recurrence_masks'][c]['release']=='per_model']
        recurring_int=[gates[c]['internal'] for c in cs if r['recurrence_masks'][c]['internal']=='per_model']
        annual_rel=[out[c]['annual_event_release_equivalent_days'] for c in cs]
        annual_int=[out[c]['annual_event_internal_equivalent_days'] for c in cs]
        setup_rel=[out[c]['first_year_setup_release_equivalent_days'] for c in cs]
        setup_int=[out[c]['first_year_setup_internal_equivalent_days'] for c in cs]
        if pid=='frontier-act':
            annual_rel.extend([mean_gate(audit2),emergency])
            annual_int.extend([mean_gate(audit2)*av['internal_gate_fraction'],emergency])
        r['recurring_release_lag_days']=expected_maximum(recurring_rel) if recurring_rel else zero()
        r['recurring_internal_use_lag_days']=expected_maximum(recurring_int) if recurring_int else zero()
        if pid in ('eu-ai-act','ai-risk-evaluation-act','secure-ai-development-act'):
            # All gates in these packages are per-model, after their specific
            # applicability, queue replacement, and shared window transformations.
            r['recurring_release_lag_days']=r['release_lag_excluding_training_days']
            r['recurring_internal_use_lag_days']=r['internal_use_lag_excluding_training_days']
        r['annual_event_release_equivalent_days']=annual_union(annual_rel)
        r['annual_event_internal_equivalent_days']=annual_union(annual_int)
        r['first_year_setup_release_equivalent_days']=annual_union(setup_rel)
        r['first_year_setup_internal_equivalent_days']=annual_union(setup_int)
        B[pid]=r
    return dict(shared=shared,policy_inputs=inputs,policies=out,policy_metadata=meta,bundle_inputs=BI,bundles=B,interpretation=data['interpretation'])

if __name__=='__main__':
    d=sample_regulation(n=50000)
    for pid,p in d['bundles'].items():
        print(pid, 'release',round(float(p['release_lag_excluding_training_days'].mean()),3),'internal',round(float(p['internal_use_lag_excluding_training_days'].mean()),3),'rd_pct',round(100*float(p['annual_rd_input_loss_fraction'].mean()),4),'unowned',p['unowned_components'])
