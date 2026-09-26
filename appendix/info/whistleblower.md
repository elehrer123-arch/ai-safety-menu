# Whistleblower protections

**Best estimate: +0.13 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is +0.011 to +0.39 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

Lab employees can tell regulators about serious safety risks without being fired or sued. Large labs also have to run an anonymous internal reporting line.

The intervention is incremental to the same 2026 voluntary practices, with initial models, knowledge and hardware held fixed. The clock starts when the obligation is operative.

## Research and calculation

Extra investigations are modeled as rare, localized interruptions of research. Benefits from better information, retention or avoided misconduct are not empirically quantified here. A near-zero result should not be interpreted as a judgment on those benefits.

Internal delay is an annual localized hold expressed as equivalent complete-lab days; tag annual_event rather than multiply per release. Possible information/retention benefits set to zero in cost calibration, not established absent.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | +0.12 |
| U.S. accumulated research effect | +0.014 |
| U.S. response to Chinese changes | 0.000 |
| **Total U.S. capability loss** | **+0.14** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.001 |
| China response to U.S. changes | +0.009 |
| **Total Chinese capability loss** | **+0.010** |
| **U.S. loss minus Chinese loss** | **+0.13** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction
annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)
release_lag_excluding_training_days = 0
internal_use_lag_excluding_training_days = extra_investigation_probability*investigation_hold_days*affected_research_fraction
training_lag_per_affected_run_days = 0
annual_investment_input_loss_fraction = 0
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| setup and annual staff days | 3 / 10 / 40 | person_workdays_per_lab_year | analyst prior | Incremental setup/maintenance work beyond voluntary practice; explicit workload prior. |
| per release staff days | 0 / 0 / 0 | person_workdays_per_model | analyst prior | Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program. |
| research counterfactual fraction | 0 / 0.05 / 0.2 | fraction_of_compliance_labor | analyst prior | Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers. |
| extra investigation probability | 0 / 0.03 / 0.15 | probability_per_lab_year | analyst prior | Incremental substantive concern producing a temporary hold due to legal protection, beyond voluntary channels. |
| investigation hold days | 1 / 5 / 30 | calendar_days | analyst prior | Conditional annual hold; excludes ordinary responses that would happen anyway. |
| affected research fraction | 0 / 0.1 / 0.4 | fraction_of_lab_frontier_activity | analyst prior | Share of frontier activity stopped during incremental investigation. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).
- [Gans, Regulating the Direction of Innovation](../sources.md#regulation-gans25) — [original source](https://www.nber.org/papers/w32741).
- [Trebbi, Zhang and Simkovic, Compliance costs](../sources.md#regulation-compliance26) — [original source](https://www.nber.org/papers/w30691).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | +0.13 |
| No marginal U.S.-to-China research/teacher reliance | +0.14 |
| Half the marginal U.S.-to-China reliance | +0.13 |
| Twice the marginal U.S.-to-China reliance | +0.12 |
| No incremental AI-assisted research feedback | +0.11 |
| No China-to-U.S. research response | +0.13 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | +0.16 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | +0.062 |
| 12 months | +0.13 |
| 36 months | +0.41 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): internal gate days (r=+1.00), extra investigation probability (r=+0.51), affected research fraction (r=+0.50).

Monte Carlo standard error of the numerical mean: 0.0015 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
