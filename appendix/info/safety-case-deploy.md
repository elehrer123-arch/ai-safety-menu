# Safety case before deployment

**Best estimate: -1.27 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -3.6 to +0.14 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

Before release, the lab writes a structured argument, backed by evidence, that the model is safe enough to launch. A reviewer has to approve it.

The intervention is incremental to the same 2026 voluntary practices, with initial models, knowledge and hardware held fixed. The clock starts when the obligation is operative.

## Research and calculation

The long-tail approval model can materially defer external availability while having a much smaller effect on technical progress. Internal-use restrictions enter research productivity separately. On a publicly deployable-model metric, this policy would have a substantially larger positive delay.

No direct published approval-time series exists. Numeric best estimate is therefore prior-weighted, with explicit nonapproval tail and shared evidence nodes. Independent signoff distinct from comments on a public report.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +0.49 |
| U.S. response to Chinese changes | +0.062 |
| **Total U.S. capability loss** | **+0.56** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.24 |
| China response to U.S. changes | +1.59 |
| **Total Chinese capability loss** | **+1.83** |
| **U.S. loss minus Chinese loss** | **-1.27** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction
annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)
release_lag_excluding_training_days = review_service_days*(1-parallel_review_fraction)+review_queue_days+rereview_probability*rereview_days+nonapproval_probability*nonapproval_wait_days
internal_use_lag_excluding_training_days = (review_service_days*(1-parallel_review_fraction)+review_queue_days+rereview_probability*rereview_days+nonapproval_probability*nonapproval_wait_days)*internal_gate_fraction
training_lag_per_affected_run_days = 0
annual_investment_input_loss_fraction = 0
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| setup and annual staff days | 20 / 60 / 200 | person_workdays_per_lab_year | analyst prior | Incremental setup/maintenance work beyond voluntary practice; explicit workload prior. |
| per release staff days | 15 / 40 / 120 | person_workdays_per_model | analyst prior | Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program. |
| research counterfactual fraction | 0.15 / 0.4 / 0.8 | fraction_of_compliance_labor | analyst prior | Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers. |
| review service days | 7 / 21 / 60 | calendar_days | analyst prior | Novel affirmative review; planned parallel document preparation. No measured frontier certification duration. |
| parallel review fraction | 0.25 / 0.5 / 0.8 | fraction_of_service_before_other_readiness | analyst prior | Rolling review before final checkpoint; full prior. |
| review queue days | 0 / 5 / 30 | calendar_days | analyst prior | Dedicated signoff capacity; first-year program may queue. |
| rereview probability | 0.1 / 0.25 / 0.5 | probability_per_case | analyst prior | Evidence deficiencies prompt another round. |
| rereview days | 7 / 14 / 45 | calendar_days | analyst prior | Residual second-review service. |
| nonapproval probability | 0 / 0.01 / 0.08 | probability_per_case | analyst prior | Cannot substantiate case, absent in voluntary baseline. |
| nonapproval wait days | 30 / 90 / 180 | calendar_days | analyst prior | Time to acceptable substitute/reworked release within first-year horizon; not permanent prohibition. |
| internal gate fraction | 0 / 0.05 / 0.25 | fraction_of_release_holds | analyst prior | Policy legally covers external deployment; internal delay is optional spillover. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [Guerreiro, Rebelo and Teles, Regulating AI](../sources.md#regulation-guerreiro26) — [original source](https://www.nber.org/papers/w31921).
- [Charnock et al., Expanding external access](../sources.md#regulation-access26) — [original source](https://arxiv.org/abs/2601.11916).
- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).
- [Trebbi, Zhang and Simkovic, Compliance costs](../sources.md#regulation-compliance26) — [original source](https://www.nber.org/papers/w30691).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | -1.27 |
| No marginal U.S.-to-China research/teacher reliance | +0.49 |
| Half the marginal U.S.-to-China reliance | -0.39 |
| Twice the marginal U.S.-to-China reliance | -3.0 |
| No incremental AI-assisted research feedback | -1.10 |
| No China-to-U.S. research response | -1.33 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | -1.63 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | -1.05 |
| 12 months | -1.27 |
| 36 months | -1.27 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): teacher reliance (r=-0.86), public release gate days (r=-0.32), algorithmic growth (r=-0.23).

Monte Carlo standard error of the numerical mean: 0.0134 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
