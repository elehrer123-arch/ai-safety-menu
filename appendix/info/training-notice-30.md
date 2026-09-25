# Thirty-day pre-training notice

**Best estimate: +2.7 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is +0.58 to +6.2 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

The lab tells the government 30 days before starting a very large training run. No approval is needed; the run can start when the 30 days are up.

The intervention is incremental to the same 2026 voluntary practices, with initial models, knowledge and hardware held fixed. The clock starts when the obligation is operative.

## Research and calculation

The statutory notice duration is not treated as 30 lost days for every training run. Planning lead time, material changes and work conducted in parallel determine the residual. Additional qualifying runs do not automatically become serial frontier delays.

No fresh reset for trivial changes; reset scope explicitly part of frozen scenario. A notice rule is not a30day universal lost-output block.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | +2.6 |
| U.S. accumulated research effect | +0.23 |
| U.S. response to Chinese changes | +0.003 |
| **Total U.S. capability loss** | **+2.9** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.010 |
| China response to U.S. changes | +0.16 |
| **Total Chinese capability loss** | **+0.17** |
| **U.S. loss minus Chinese loss** | **+2.7** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_run_staff_days*qualifying_training_runs)*research_counterfactual_fraction
annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)
release_lag_excluding_training_days = 0
internal_use_lag_excluding_training_days = 0
training_lag_per_affected_run_days = ((1-reset_probability)*maximum(0,notice_days-ordinary_notice_advance_days)+reset_probability*maximum(0,notice_days-reset_notice_advance_days))*(1-parallel_work_fraction)
annual_investment_input_loss_fraction = 0
raw_training_wait_calendar_days = ((1-reset_probability)*maximum(0,notice_days-ordinary_notice_advance_days)+reset_probability*maximum(0,notice_days-reset_notice_advance_days))
progress_preserved_during_wait_fraction = parallel_work_fraction
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| setup and annual staff days | 2 / 5 / 15 | person_workdays_per_lab_year | analyst prior | Incremental setup/maintenance work beyond voluntary practice; explicit workload prior. |
| per run staff days | 1 / 3 / 10 | person_workdays_per_qualifying_run | analyst prior | Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program. |
| research counterfactual fraction | 0.1 / 0.25 / 0.6 | fraction_of_compliance_labor | analyst prior | Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers. |
| notice days | 30 / 30 / 30 | calendar_days | observed | Exact frozen policy waiting period. |
| ordinary notice advance days | 14 / 45 / 90 | calendar_days | analyst prior | Planned run notice leadtime before otherwise ready; explicit unmeasured prior. |
| reset probability | 0 / 0.15 / 0.4 | probability_per_run | analyst prior | Run/recipe changes requiring a fresh notice, assuming material changes reset clock. |
| reset notice advance days | 0 / 7 / 21 | calendar_days | analyst prior | Leadtime remaining for material run changes. |
| parallel work fraction | 0.1 / 0.4 / 0.8 | fraction_of_frontier_progress_preserved_while_waiting | analyst prior | Alternative research and smaller runs while notice clock runs. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).
- [Trebbi, Zhang and Simkovic, Compliance costs](../sources.md#regulation-compliance26) — [original source](https://www.nber.org/papers/w30691).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | +2.7 |
| No marginal U.S.-to-China research/teacher reliance | +2.9 |
| Half the marginal U.S.-to-China reliance | +2.8 |
| Twice the marginal U.S.-to-China reliance | +2.5 |
| No incremental AI-assisted research feedback | +2.5 |
| No China-to-U.S. research response | +2.7 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | +3.4 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | +0.83 |
| 12 months | +2.7 |
| 36 months | +11.1 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): effective training wait per run days (r=+0.95), reset probability (r=+0.56), parallel work fraction (r=-0.35).

Monte Carlo standard error of the numerical mean: 0.0209 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
