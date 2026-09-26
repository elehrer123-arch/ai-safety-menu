# Critical safety incident reporting

**Best estimate: 0.000 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is 0.000 to +0.001 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

When something goes badly wrong, such as stolen model weights or a model helping to cause serious harm, the lab reports it to the state within 15 days. If lives are at immediate risk, it has 24 hours.

The intervention is incremental to the same 2026 voluntary practices, with initial models, knowledge and hardware held fixed. The clock starts when the obligation is operative.

## Research and calculation

There is no pre-release gate in this scope. Incremental reporting hours compete with research only to the extent that specialized staff or extra hiring fail to absorb them. The result is economically negligible on this metric; rounding does not imply that reporting requires literally no work.

No invented filing delay charged to capability. Harm response itself belongs to the baseline unless induced by reporting. Direct report-labor estimate excludes uncertain beneficial learning.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | 0.000 |
| U.S. response to Chinese changes | 0.000 |
| **Total U.S. capability loss** | **0.000** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | 0.000 |
| China response to U.S. changes | 0.000 |
| **Total Chinese capability loss** | **0.000** |
| **U.S. loss minus Chinese loss** | **0.000** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
annual_displaced_rd_workdays = (setup_and_annual_staff_days+incidents_per_year*report_staff_days)*research_counterfactual_fraction
annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)
release_lag_excluding_training_days = 0
internal_use_lag_excluding_training_days = 0
training_lag_per_affected_run_days = 0
annual_investment_input_loss_fraction = 0
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| setup and annual staff days | 2 / 5 / 15 | person_workdays_per_lab_year | analyst prior | Incremental setup/maintenance work beyond voluntary practice; explicit workload prior. |
| per release staff days | 0 / 0 / 0 | person_workdays_per_model | analyst prior | Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program. |
| research counterfactual fraction | 0.05 / 0.15 / 0.4 | fraction_of_compliance_labor | analyst prior | Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers. |
| incidents per year | 0 / 1 / 4 | incidents_per_lab_year | analyst prior | Reportable incidents requiring incremental reports; frequency prior, not empirical incident rate. |
| report staff days | 0.5 / 2 / 7 | person_workdays_per_incident | analyst prior | Fact-gathering/legal write-up beyond existing incident response. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [California BPC 22757.13](../sources.md#regulation-sb53_incident) — [original source](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=22757.13).
- [Trebbi, Zhang and Simkovic, Compliance costs](../sources.md#regulation-compliance26) — [original source](https://www.nber.org/papers/w30691).
- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | 0.000 |
| No marginal U.S.-to-China research/teacher reliance | 0.000 |
| Half the marginal U.S.-to-China reliance | 0.000 |
| Twice the marginal U.S.-to-China reliance | 0.000 |
| No incremental AI-assisted research feedback | 0.000 |
| No China-to-U.S. research response | 0.000 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | +0.001 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | 0.000 |
| 12 months | 0.000 |
| 36 months | +0.001 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): annual rd input loss fraction (r=+0.87), research counterfactual fraction (r=+0.47), setup and annual staff days (r=+0.28).

Monte Carlo standard error of the numerical mean: 0.0000 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
