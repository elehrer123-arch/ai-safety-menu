# Triggered red-team and remediation

**Best estimate: +0.021 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -0.15 to +0.20 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

If testing shows a model crossing a danger line, such as giving real help with a bioweapon, the lab must have experts attack it hard and fix what they find before anyone uses it.

The intervention is incremental to the same 2026 voluntary practices, with initial models, knowledge and hardware held fixed. The clock starts when the obligation is operative.

## Research and calculation

The relevant probability is an incremental binding intervention, not merely a model crossing a risk threshold. Prepared mitigations reduce remaining work. Joint incidence and remedy difficulty could be more correlated than the base independent priors.

Threshold incidence is not legal increment. Preserve correlated tails when threshold crossing and remedial difficulty increase together; base numerical sampling treats them independent for inspectability.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +0.14 |
| U.S. response to Chinese changes | +0.004 |
| **Total U.S. capability loss** | **+0.15** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.016 |
| China response to U.S. changes | +0.11 |
| **Total Chinese capability loss** | **+0.13** |
| **U.S. loss minus Chinese loss** | **+0.021** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction
annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)
release_lag_excluding_training_days = danger_trigger_probability*incrementally_binding_fraction*remediation_service_days*(1-prepared_fraction)
internal_use_lag_excluding_training_days = danger_trigger_probability*incrementally_binding_fraction*remediation_service_days*(1-prepared_fraction)*internal_gate_fraction
training_lag_per_affected_run_days = 0
annual_investment_input_loss_fraction = 0
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| setup and annual staff days | 5 / 20 / 60 | person_workdays_per_lab_year | analyst prior | Incremental setup/maintenance work beyond voluntary practice; explicit workload prior. |
| per release staff days | 5 / 20 / 80 | person_workdays_per_model | analyst prior | Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program. |
| research counterfactual fraction | 0.15 / 0.4 / 0.8 | fraction_of_compliance_labor | analyst prior | Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers. |
| danger trigger probability | 0.5 / 0.8 / 1 | probability_per_frontier_model | calibrated | 2026 frontier systems often have High/ASL3 or Critical capability classifications; frequency chosen, not estimated from selective cases. |
| incrementally binding fraction | 0.05 / 0.2 / 0.5 | fraction_of_triggered_models | analyst prior | Fraction with additional hold relative to already voluntary safeguards, accounting for actual enforcement. |
| remediation service days | 7 / 21 / 60 | calendar_days | calibrated | Unprepared elevated testing/mitigation; AISI anchorsweeks but implementation tail is prior. |
| prepared fraction | 0.25 / 0.65 / 0.9 | fraction_of_remediation_completed_in_parallel | analyst prior | Proportion of remediation already prepared before it becomes critical; not a measured fact. |
| internal gate fraction | 0.1 / 0.35 / 0.8 | fraction_of_binding_holds | analyst prior | Some safeguards needed before internal inference as Astra demonstrates; extent remains prior. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [AISI, Early lessons from evaluating frontier AI systems](../sources.md#production-aisi) — [original source](https://www.aisi.gov.uk/blog/early-lessons-from-evaluating-frontier-ai-systems).
- [GPT-5.5 System Card](../sources.md#regulation-card_gpt55) — [original source](https://deploymentsafety.openai.com/gpt-5-5).
- [GPT-6 Astra System Card](../sources.md#regulation-card_astra) — [original source](https://deploymentsafety.openai.com/gpt-6-astra).
- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).
- [Trebbi, Zhang and Simkovic, Compliance costs](../sources.md#regulation-compliance26) — [original source](https://www.nber.org/papers/w30691).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | +0.021 |
| No marginal U.S.-to-China research/teacher reliance | +0.14 |
| Half the marginal U.S.-to-China reliance | +0.082 |
| Twice the marginal U.S.-to-China reliance | -0.10 |
| No incremental AI-assisted research feedback | +0.021 |
| No China-to-U.S. research response | +0.017 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | +0.027 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | -0.010 |
| 12 months | +0.021 |
| 36 months | +0.12 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): teacher reliance (r=-0.49), internal gate fraction (r=+0.31), internal gate days (r=+0.21).

Monte Carlo standard error of the numerical mean: 0.0014 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
