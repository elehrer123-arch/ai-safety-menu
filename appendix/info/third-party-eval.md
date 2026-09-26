# Independent pre-deployment evaluation

**Best estimate: -0.041 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -0.15 to +0.010 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

An approved outside group, such as a government AI safety institute, tests the model before the public can use it and reports what it found.

The intervention is incremental to the same 2026 voluntary practices, with initial models, knowledge and hardware held fixed. The clock starts when the obligation is operative.

## Research and calculation

Qualifying evaluations already conducted voluntarily are reused. External evaluator service, queueing, existing access runway and final-report tails are distinct. This is not a claim that every observed evaluation caused its entire elapsed duration as delay.

A qualifying existing evaluator is reused. Reports and mandatory minimum access windows are shared nodes, not two independent waits. Need dedicated queues only if evaluator not substitutable.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +0.022 |
| U.S. response to Chinese changes | +0.002 |
| **Total U.S. capability loss** | **+0.024** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.008 |
| China response to U.S. changes | +0.056 |
| **Total Chinese capability loss** | **+0.064** |
| **U.S. loss minus Chinese loss** | **-0.041** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction
annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)
release_lag_excluding_training_days = new_eval_probability*maximum(0,standard_eval_service+external_queue-baseline_access_runway-earlier_sharing_gain)+(1-new_eval_probability)*late_report_probability*report_tail_days
internal_use_lag_excluding_training_days = (new_eval_probability*maximum(0,standard_eval_service+external_queue-baseline_access_runway-earlier_sharing_gain)+(1-new_eval_probability)*late_report_probability*report_tail_days)*internal_gate_fraction
training_lag_per_affected_run_days = 0
annual_investment_input_loss_fraction = 0
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| setup and annual staff days | 5 / 15 / 50 | person_workdays_per_lab_year | analyst prior | Incremental setup/maintenance work beyond voluntary practice; explicit workload prior. |
| per release staff days | 3 / 10 / 40 | person_workdays_per_model | analyst prior | Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program. |
| research counterfactual fraction | 0.1 / 0.25 / 0.6 | fraction_of_compliance_labor | analyst prior | Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers. |
| new eval probability | 0 / 0.15 / 0.4 | probability_per_model | analyst prior | Fraction that would lack qualifying external assessment in same voluntary practice. |
| late report probability | 0 / 0.25 / 0.6 | probability_per_model | analyst prior | Already-evaluated release that would proceed before formal report finalization. |
| report tail days | 1 / 3 / 10 | calendar_days | analyst prior | Added formal report turnaround where release would previously proceed. |
| internal gate fraction | 0 / 0.05 / 0.2 | fraction_of_release_holds | analyst prior | Voluntary internal hold induced by external report regime. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [AISI, Early lessons from evaluating frontier AI systems](../sources.md#production-aisi) — [original source](https://www.aisi.gov.uk/blog/early-lessons-from-evaluating-frontier-ai-systems).
- [METR evaluation of GPT-5](../sources.md#regulation-met_gpt5) — [original source](https://metr.org/evaluations/gpt-5-report/).
- [METR preliminary evaluation of o3 and o4-mini](../sources.md#regulation-met_o3) — [original source](https://metr.org/evaluations/openai-o3-report/).
- [Charnock et al., Expanding external access](../sources.md#regulation-access26) — [original source](https://arxiv.org/abs/2601.11916).
- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).
- [Trebbi, Zhang and Simkovic, Compliance costs](../sources.md#regulation-compliance26) — [original source](https://www.nber.org/papers/w30691).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | -0.041 |
| No marginal U.S.-to-China research/teacher reliance | +0.021 |
| Half the marginal U.S.-to-China reliance | -0.010 |
| Twice the marginal U.S.-to-China reliance | -0.10 |
| No incremental AI-assisted research feedback | -0.035 |
| No China-to-U.S. research response | -0.043 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | -0.052 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | -0.034 |
| 12 months | -0.041 |
| 36 months | -0.037 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): teacher reliance (r=-0.65), public release gate days (r=-0.57), internal gate days (r=-0.33).

Monte Carlo standard error of the numerical mean: 0.0006 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
