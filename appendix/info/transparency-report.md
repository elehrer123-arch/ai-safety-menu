# Transparency report at launch

**Best estimate: -0.023 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -0.075 to 0.000 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

When a lab releases a new frontier model, it publishes a short report on what the model is for, which risks it was tested for, and what the tests found.

The intervention is incremental to the same 2026 voluntary practices, with initial models, knowledge and hardware held fixed. The clock starts when the obligation is operative.

## Research and calculation

A late document can defer public launch without delaying technical development. The small modeled widening comes from less access to U.S. teachers, offset by incremental compliance labor. Its sign is sensitive to the marginal teacher-dependence assumption.

Quarterly internal summaries folded into annual staff work. First trusted external access can trigger report; a launch-day document date is not measured causal delay.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +0.003 |
| U.S. response to Chinese changes | +0.001 |
| **Total U.S. capability loss** | **+0.004** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.004 |
| China response to U.S. changes | +0.024 |
| **Total Chinese capability loss** | **+0.027** |
| **U.S. loss minus Chinese loss** | **-0.023** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction
annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)
release_lag_excluding_training_days = late_report_probability*report_tail_days
internal_use_lag_excluding_training_days = 0
training_lag_per_affected_run_days = 0
annual_investment_input_loss_fraction = 0
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| setup and annual staff days | 4 / 10 / 30 | person_workdays_per_lab_year | analyst prior | Incremental setup/maintenance work beyond voluntary practice; explicit workload prior. |
| per release staff days | 2 / 6 / 20 | person_workdays_per_model | analyst prior | Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program. |
| research counterfactual fraction | 0.05 / 0.15 / 0.4 | fraction_of_compliance_labor | analyst prior | Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers. |
| late report probability | 0 / 0.1 / 0.4 | probability_per_model | analyst prior | Report not ready at otherwise planned external deployment despite existing system-card process. |
| report tail days | 0.5 / 2 / 7 | calendar_days | analyst prior | Residual document/legal signoff tail after final evaluation, not total writing time. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [California SB53 frozen text](../sources.md#regulation-sb53) — [original source](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53).
- [METR evaluation of GPT-5](../sources.md#regulation-met_gpt5) — [original source](https://metr.org/evaluations/gpt-5-report/).
- [GovAI, Delays to Frontier AI in EU and UK](../sources.md#regulation-govai26) — [original source](https://www.governance.ai/research-paper/delays-to-frontier-ai-in-the-eu-and-uk).
- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).
- [Trebbi, Zhang and Simkovic, Compliance costs](../sources.md#regulation-compliance26) — [original source](https://www.nber.org/papers/w30691).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | -0.023 |
| No marginal U.S.-to-China research/teacher reliance | +0.003 |
| Half the marginal U.S.-to-China reliance | -0.010 |
| Twice the marginal U.S.-to-China reliance | -0.050 |
| No incremental AI-assisted research feedback | -0.020 |
| No China-to-U.S. research response | -0.024 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | -0.030 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | -0.018 |
| 12 months | -0.023 |
| 36 months | -0.027 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): public release gate days (r=-0.68), teacher reliance (r=-0.59), late report probability (r=-0.49).

Monte Carlo standard error of the numerical mean: 0.0003 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
