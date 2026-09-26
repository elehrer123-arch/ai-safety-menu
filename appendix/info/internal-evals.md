# Mandatory internal capability evaluations

**Best estimate: -0.032 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -0.15 to +0.026 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

Before release, the lab must test every frontier model for dangerous abilities, such as helping build a bioweapon or break into computer systems, and record the results.

The intervention is incremental to the same 2026 voluntary practices, with initial models, knowledge and hardware held fixed. The clock starts when the obligation is operative.

## Research and calculation

Published testing durations anchor possible workloads; only mandatory work beyond the voluntary suite is incremental. Most testing overlaps training, launch preparation and other safety work. Findings requiring new remediation belong to the separate triggered-remediation mechanism.

Existing evaluation effort stays in baseline; extra mandatory coverage is a prior. Evaluation-induced remediation modeled in triggered-redteam, not here.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +0.026 |
| U.S. response to Chinese changes | +0.002 |
| **Total U.S. capability loss** | **+0.028** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.008 |
| China response to U.S. changes | +0.052 |
| **Total Chinese capability loss** | **+0.060** |
| **U.S. loss minus Chinese loss** | **-0.032** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction
annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)
release_lag_excluding_training_days = incremental_test_probability*maximum(0,incremental_service_days-remaining_non_eval_buffer)
internal_use_lag_excluding_training_days = incremental_test_probability*maximum(0,incremental_service_days-remaining_non_eval_buffer)*internal_gate_fraction
training_lag_per_affected_run_days = 0
annual_investment_input_loss_fraction = 0
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| setup and annual staff days | 5 / 20 / 60 | person_workdays_per_lab_year | analyst prior | Incremental setup/maintenance work beyond voluntary practice; explicit workload prior. |
| per release staff days | 5 / 20 / 70 | person_workdays_per_model | analyst prior | Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program. |
| research counterfactual fraction | 0.1 / 0.35 / 0.7 | fraction_of_compliance_labor | analyst prior | Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers. |
| incremental test probability | 0.05 / 0.2 / 0.6 | probability_per_model | analyst prior | Mandatory suite causes extra final testing relative to actual voluntary suite. |
| incremental service days | 2 / 5 / 14 | calendar_days | calibrated | Additional final-checkpoint test/writeup workload; informed by AISI but incremental share is prior. |
| remaining non eval buffer | 0 / 2 / 7 | calendar_days | analyst prior | Time until other launch readiness after additional tests start. |
| internal gate fraction | 0 / 0.03 / 0.15 | fraction_of_holds | analyst prior | Optional holding of internal use absent statutory internal gate. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [AISI, Early lessons from evaluating frontier AI systems](../sources.md#production-aisi) — [original source](https://www.aisi.gov.uk/blog/early-lessons-from-evaluating-frontier-ai-systems).
- [GPT-5.5 System Card](../sources.md#regulation-card_gpt55) — [original source](https://deploymentsafety.openai.com/gpt-5-5).
- [METR evaluation of GPT-5](../sources.md#regulation-met_gpt5) — [original source](https://metr.org/evaluations/gpt-5-report/).
- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).
- [Trebbi, Zhang and Simkovic, Compliance costs](../sources.md#regulation-compliance26) — [original source](https://www.nber.org/papers/w30691).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | -0.032 |
| No marginal U.S.-to-China research/teacher reliance | +0.026 |
| Half the marginal U.S.-to-China reliance | -0.003 |
| Twice the marginal U.S.-to-China reliance | -0.090 |
| No incremental AI-assisted research feedback | -0.027 |
| No China-to-U.S. research response | -0.034 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | -0.041 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | -0.029 |
| 12 months | -0.032 |
| 36 months | -0.023 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): public release gate days (r=-0.64), teacher reliance (r=-0.52), incremental service days (r=-0.45).

Monte Carlo standard error of the numerical mean: 0.0007 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
