# Twenty business days of evaluator access

**Best estimate: -0.19 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -0.81 to +0.005 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

Outside testers get at least four weeks with a new model before the public can use it. Today they often get between three days and three weeks.

The intervention is incremental to the same 2026 voluntary practices, with initial models, knowledge and hardware held fixed. The clock starts when the obligation is operative.

## Research and calculation

Twenty business days is modeled as a 28-calendar-day convention. Existing access can satisfy much of that requirement. Earlier sharing is allowed; a material checkpoint reset can create an additional residual tail. Holidays and particular legal counting conventions are not separately forecast.

Eight cases demonstrate heterogeneous access clocks; baseline runway distribution is a coarse prior-informed calibration. Three-day testing window is not asserted to be three-day runway.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +0.044 |
| U.S. response to Chinese changes | +0.008 |
| **Total U.S. capability loss** | **+0.052** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.031 |
| China response to U.S. changes | +0.21 |
| **Total Chinese capability loss** | **+0.24** |
| **U.S. loss minus Chinese loss** | **-0.19** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction
annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)
release_lag_excluding_training_days = maximum(0,floor_calendar_days-baseline_access_runway-earlier_sharing_gain)+late_checkpoint_reset_probability*late_checkpoint_reset_days
internal_use_lag_excluding_training_days = (maximum(0,floor_calendar_days-baseline_access_runway-earlier_sharing_gain)+late_checkpoint_reset_probability*late_checkpoint_reset_days)*internal_gate_fraction
training_lag_per_affected_run_days = 0
annual_investment_input_loss_fraction = 0
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| setup and annual staff days | 3 / 10 / 30 | person_workdays_per_lab_year | analyst prior | Incremental setup/maintenance work beyond voluntary practice; explicit workload prior. |
| per release staff days | 3 / 10 / 40 | person_workdays_per_model | analyst prior | Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program. |
| research counterfactual fraction | 0.1 / 0.25 / 0.6 | fraction_of_compliance_labor | analyst prior | Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers. |
| floor calendar days | 28 / 28 / 28 | calendar_days | calibrated | 20business days modeled as4weeks ignoring holidays; explicit convention, not20calendar days. |
| internal gate fraction | 0 / 0.03 / 0.15 | fraction_of_release_holds | analyst prior | Optional internal hold beyond literal external-release-only gate. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [EU GPAI Code of Practice safety/security](../sources.md#regulation-eu_code) — [original source](https://ec.europa.eu/newsroom/dae/redirection/document/118119).
- [METR evaluation of GPT-5](../sources.md#regulation-met_gpt5) — [original source](https://metr.org/evaluations/gpt-5-report/).
- [METR predeployment evaluation of Claude Opus 5.5](../sources.md#regulation-met_opus55) — [original source](https://metr.org/blog/2026-09-22-claude-opus-5-5/).
- [GPT-6 Astra System Card](../sources.md#regulation-card_astra) — [original source](https://deploymentsafety.openai.com/gpt-6-astra).
- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).
- [Trebbi, Zhang and Simkovic, Compliance costs](../sources.md#regulation-compliance26) — [original source](https://www.nber.org/papers/w30691).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | -0.19 |
| No marginal U.S.-to-China research/teacher reliance | +0.043 |
| Half the marginal U.S.-to-China reliance | -0.072 |
| Twice the marginal U.S.-to-China reliance | -0.42 |
| No incremental AI-assisted research feedback | -0.16 |
| No China-to-U.S. research response | -0.20 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | -0.24 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | -0.15 |
| 12 months | -0.19 |
| 36 months | -0.21 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): public release gate days (r=-0.71), internal gate days (r=-0.52), teacher reliance (r=-0.44).

Monte Carlo standard error of the numerical mean: 0.0034 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
