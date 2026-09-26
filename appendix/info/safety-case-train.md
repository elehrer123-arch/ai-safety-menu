# Authorization before frontier training

**Best estimate: +25 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is +4.9 to +59 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

Before starting a very large training run, the lab submits a safety plan to a regulator and waits for approval. The regulator can say no.

The intervention is incremental to the same 2026 voluntary practices, with initial models, knowledge and hardware held fixed. The clock starts when the obligation is operative.

## Research and calculation

The model distinguishes raw authorization waiting from research preserved during waiting. Only serial stages count toward frontier delay; parallel training runs increase workload. The first affected checkpoint arrives after a pipeline delay, preserving existing models and ongoing runs.

Training output is effective run-level lag after usable parallel research; raw calendar wait also supplied. Do not count release/internal wait again; downstream propagation handled by root. Investment uncertainty treated separately in sensitivity, to avoid hidden duplicate denial costs.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | +25 |
| U.S. accumulated research effect | +2.1 |
| U.S. response to Chinese changes | +0.025 |
| **Total U.S. capability loss** | **+27** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.092 |
| China response to U.S. changes | +1.48 |
| **Total Chinese capability loss** | **+1.57** |
| **U.S. loss minus Chinese loss** | **+25** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_run_staff_days*qualifying_training_runs)*research_counterfactual_fraction
annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)
release_lag_excluding_training_days = 0
internal_use_lag_excluding_training_days = 0
training_lag_per_affected_run_days = (maximum(0,approval_service_days+approval_queue_days-filing_advance_days)+rereview_probability*rereview_days+refusal_probability*refusal_substitute_days)*(1-parallel_work_fraction)
annual_investment_input_loss_fraction = 0
raw_training_wait_calendar_days = (maximum(0,approval_service_days+approval_queue_days-filing_advance_days)+rereview_probability*rereview_days+refusal_probability*refusal_substitute_days)
progress_preserved_during_wait_fraction = parallel_work_fraction
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| setup and annual staff days | 20 / 60 / 200 | person_workdays_per_lab_year | analyst prior | Incremental setup/maintenance work beyond voluntary practice; explicit workload prior. |
| per run staff days | 10 / 30 / 100 | person_workdays_per_qualifying_run | analyst prior | Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program. |
| research counterfactual fraction | 0.1 / 0.3 / 0.7 | fraction_of_compliance_labor | analyst prior | Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers. |
| approval service days | 14 / 30 / 90 | calendar_days | analyst prior | Novel regulator review rather than brief notice; prior. |
| approval queue days | 0 / 10 / 45 | calendar_days | analyst prior | First-year authorization queue; no measured system. |
| filing advance days | 7 / 30 / 90 | calendar_days | analyst prior | How far application can precede compute/data readiness; no unobserved actual dates invented. |
| rereview probability | 0.1 / 0.25 / 0.5 | probability_per_run | analyst prior | Conditions or revisions require additional review. |
| rereview days | 7 / 21 / 60 | calendar_days | analyst prior | Residual approval re-review duration. |
| refusal probability | 0 / 0.02 / 0.1 | probability_per_run | analyst prior | Refused or withdrawn run replaced by smaller/different run. |
| refusal substitute days | 30 / 90 / 180 | calendar_days | analyst prior | Time until acceptable replacement research path within first year. |
| parallel work fraction | 0.1 / 0.35 / 0.7 | fraction_of_frontier_progress_preserved_while_waiting | analyst prior | Algorithmic/data/other runs continue during administrative pause. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).
- [Guerreiro, Rebelo and Teles, Regulating AI](../sources.md#regulation-guerreiro26) — [original source](https://www.nber.org/papers/w31921).
- [Gans, Regulating the Direction of Innovation](../sources.md#regulation-gans25) — [original source](https://www.nber.org/papers/w32741).
- [Trebbi, Zhang and Simkovic, Compliance costs](../sources.md#regulation-compliance26) — [original source](https://www.nber.org/papers/w30691).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | +25 |
| No marginal U.S.-to-China research/teacher reliance | +27 |
| Half the marginal U.S.-to-China reliance | +26 |
| Twice the marginal U.S.-to-China reliance | +24 |
| No incremental AI-assisted research feedback | +23 |
| No China-to-U.S. research response | +25 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | +32 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | +7.8 |
| 12 months | +25 |
| 36 months | +102 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): effective training wait per run days (r=+0.94), approval service days (r=+0.56), filing advance days (r=-0.54).

Monte Carlo standard error of the numerical mean: 0.1929 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
