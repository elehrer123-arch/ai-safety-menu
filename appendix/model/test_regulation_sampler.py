"""Meaningful unit/data invariants for the regulatory calibration (standardlib unittest)."""
import csv
import importlib.util
import json
from datetime import date
from pathlib import Path
import unittest
import numpy as np
from regulation_sampler import expected_maximum,gate_release_dates,training_chain_penalty,sample_regulation
P=Path(__file__).parent

class RegulationTests(unittest.TestCase):
    def test_max_integrates_binding_events(self):
        # Two independent half-probability 10-day gates: 75% chance any binds.
        g=[(.5,np.array([0.])),(.5,np.array([10.]))]
        self.assertEqual(float(expected_maximum([g,g])[0]),7.5)
        # Different severities: .5*20 + .5*.5*10 = 12.5.
        h=[(.5,np.array([0.])),(.5,np.array([20.]))]
        self.assertEqual(float(expected_maximum([g,h])[0]),12.5)
    def test_training_clock(self):
        self.assertAlmostEqual(float(training_chain_penalty(20,.25,1.5)),22.5)
        self.assertAlmostEqual(float(training_chain_penalty(20,.25,1.5,365.25/2)),11.25)
        self.assertEqual(float(training_chain_penalty(1000,0,2)),365.25)
        self.assertEqual(float(training_chain_penalty(20,1,2)),0)
    def test_annual_masks_no_backlog(self):
        actual=gate_release_dates([10,20,25,30,60],[(15,25),(24,29)])
        np.testing.assert_array_equal(actual,[10,29,29,30,60])
        self.assertEqual(gate_release_dates([25],[(15,25)])[0],25)
    def test_data_dates_and_sources(self):
        d=json.loads((P/'regulation-calibration.json').read_text())
        ids={s['source_id'] for s in d['sources']}
        self.assertEqual(len(d['policies']),14)
        self.assertEqual(len(d['bundles']),8)
        with (P/'public-release-cases.csv').open() as f: cases=list(csv.DictReader(f))
        self.assertEqual(len(cases),8)
        self.assertEqual(len({c['release_cluster'] for c in cases}),6)
        for c in cases:
            self.assertTrue(set(c['source_ids'].split(';'))<=ids)
            if c['access_start_date']:
                actual=(date.fromisoformat(c['public_release_date'])-date.fromisoformat(c['access_start_date'])).days
                self.assertEqual(actual,int(c['calendar_access_to_release_days']))
            if c['access_start_date'] and c['evaluation_end_date']:
                actual=(date.fromisoformat(c['evaluation_end_date'])-date.fromisoformat(c['access_start_date'])).days
                self.assertEqual(actual,int(c['evaluation_elapsed_days']))
        astra=next(c for c in cases if c['case_id']=='astra_apollo')
        self.assertEqual(astra['calendar_access_to_release_days'],'')
        opus=next(c for c in cases if c['case_id']=='opus55_metr')
        self.assertEqual(opus['observed_access_window_unit'],'business_days')
        self.assertEqual(opus['access_start_date'],'')
    def test_reproducible_and_masks(self):
        a=sample_regulation(1000,7);b=sample_regulation(1000,7)
        np.testing.assert_array_equal(a['shared']['baseline_access_runway'],b['shared']['baseline_access_runway'])
        self.assertTrue(np.all(a['policies']['third-party-audit']['recurring_release_lag_days']==0))
        self.assertTrue(np.all(a['policies']['shutdown']['recurring_internal_use_lag_days']==0))
        self.assertTrue(np.all(a['bundles']['sb-53']['recurring_release_lag_days']>=a['bundles']['sb-53']['release_max_of_means_lower_bound_days']-1e-12))
        self.assertEqual(a['bundles']['sb-1047']['recurrence_masks']['third-party-audit']['release'],'annual_event')
        for block in ('policies','bundles'):
            for p in a[block].values():
                for k,v in p.items():
                    if isinstance(v,np.ndarray):
                        self.assertTrue(np.isfinite(v).all(),k)
                        if k!='annual_investment_input_loss_fraction':self.assertTrue((v>=-1e-12).all(),k)
    def test_empirical_runway_mixture(self):
        a=sample_regulation(20000,1,overrides={'shared.runway_transport_shift':0,'shared.short_unobserved_runway_probability':0})
        self.assertTrue(set(a['shared']['baseline_access_runway'])<={12,21,28})
        self.assertAlmostEqual(float(a['shared']['baseline_access_runway'].mean()),20.5,delta=.15)
        b=sample_regulation(100,1,overrides={'shared.baseline_access_runway':100})
        self.assertTrue(np.all(b['shared']['baseline_access_runway']==100))
    def test_liability_can_improve_investment(self):
        a=sample_regulation(100,5,overrides={'strict-liability.extra_risk_premium':0,'strict-liability.trust_demand_investment_offset':.005})
        np.testing.assert_allclose(a['policies']['strict-liability']['annual_investment_input_loss_fraction'],-.005)
    def test_parallel_runs_do_not_change_training_schedule(self):
        a=sample_regulation(100,5,overrides={'shared.qualifying_training_runs':1})
        b=sample_regulation(100,5,overrides={'shared.qualifying_training_runs':6})
        np.testing.assert_array_equal(a['policies']['safety-case-train']['training_lag_per_affected_run_days'],b['policies']['safety-case-train']['training_lag_per_affected_run_days'])
        self.assertTrue(np.all(b['policies']['safety-case-train']['annual_displaced_rd_workdays']>a['policies']['safety-case-train']['annual_displaced_rd_workdays']))

if __name__=='__main__':unittest.main()
