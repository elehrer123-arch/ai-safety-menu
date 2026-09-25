# Published frontier safety framework

**Best estimate: -0.023 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -0.11 to +0.029 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

The lab publishes a document that says which dangerous abilities it tests its models for, what it does when a model crosses a line, and how it guards its models. Then it has to follow what it wrote.

The intervention is incremental to the same 2026 voluntary practices, with initial models, knowledge and hardware held fixed. The clock starts when the obligation is operative.

## Research and calculation

The estimate concerns legal adherence to a framework beyond voluntary practice. A public hold mostly affects foreign access. Internal holds matter through foregone productivity of the newest model; an already-trained model is not erased from the technical frontier.

Do not charge evaluation/remediation event again when bought with those policies. Framework obligations may weaken endogenously; prior reflects small but nonzero enforceability effect.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +0.031 |
| U.S. response to Chinese changes | +0.002 |
| **Total U.S. capability loss** | **+0.032** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.007 |
| China response to U.S. changes | +0.048 |
| **Total Chinese capability loss** | **+0.055** |
| **U.S. loss minus Chinese loss** | **-0.023** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction
annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)
release_lag_excluding_training_days = binding_event_probability*binding_event_delay
internal_use_lag_excluding_training_days = binding_event_probability*binding_event_delay*internal_gate_fraction
training_lag_per_affected_run_days = 0
annual_investment_input_loss_fraction = 0
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| setup and annual staff days | 10 / 30 / 100 | person_workdays_per_lab_year | analyst prior | Incremental setup/maintenance work beyond voluntary practice; explicit workload prior. |
| per release staff days | 0 / 0 / 0 | person_workdays_per_model | analyst prior | Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program. |
| research counterfactual fraction | 0.05 / 0.15 / 0.35 | fraction_of_compliance_labor | analyst prior | Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers. |
| binding event probability | 0 / 0.05 / 0.2 | probability_per_model | analyst prior | Probability legal adherence adds a hold beyond the same voluntary framework. |
| binding event delay | 1 / 7 / 30 | calendar_days | analyst prior | Incremental unresolved compliance/safeguard tail conditional on binding event. |
| internal gate fraction | 0 / 0.15 / 0.5 | fraction_of_binding_holds | analyst prior | Share of legally induced holds affecting internal use, not only release. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [California SB53 frozen text](../sources.md#regulation-sb53) — [original source](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53).
- [GPT-6 Astra System Card](../sources.md#regulation-card_astra) — [original source](https://deploymentsafety.openai.com/gpt-6-astra).
- [Breuer, Leuz and Vanhaverbeke, Reporting and innovation](../sources.md#regulation-breuer25) — [original source](https://www.nber.org/papers/w26291).
- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).
- [Trebbi, Zhang and Simkovic, Compliance costs](../sources.md#regulation-compliance26) — [original source](https://www.nber.org/papers/w30691).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | -0.023 |
| No marginal U.S.-to-China research/teacher reliance | +0.030 |
| Half the marginal U.S.-to-China reliance | +0.004 |
| Twice the marginal U.S.-to-China reliance | -0.076 |
| No incremental AI-assisted research feedback | -0.019 |
| No China-to-U.S. research response | -0.025 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | -0.029 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | -0.023 |
| 12 months | -0.023 |
| 36 months | -0.008 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): teacher reliance (r=-0.59), public release gate days (r=-0.36), internal gate fraction (r=+0.25).

Monte Carlo standard error of the numerical mean: 0.0005 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
