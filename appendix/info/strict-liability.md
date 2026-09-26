# Product liability for AI harms

**Best estimate: -0.040 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -0.54 to +0.46 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

AI systems are treated as products under the law. If one causes harm, the people hurt can sue the company that built it, the same way they could sue over a faulty car part.

The intervention is incremental to the same 2026 voluntary practices, with initial models, knowledge and hardware held fixed. The clock starts when the obligation is operative.

## Research and calculation

The financing channel multiplies exposed investment, an added risk premium, an investment response and productive redirection. A separate trust/demand offset allows net gains. Recent economics informs the channels; no medical-device coefficient is mechanically transplanted into frontier AI.

Numerical best estimate is analyst-prior expectation. Recent device evidence supports separating releases/research/safety but does not quantify AI investment loss. Capital response can be positive or negative after an explicit demand/trust offset. Neither downside nor upside coefficient is empirically identified; report gross and net sensitivity.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +0.24 |
| U.S. response to Chinese changes | +0.010 |
| **Total U.S. capability loss** | **+0.25** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.037 |
| China response to U.S. changes | +0.26 |
| **Total Chinese capability loss** | **+0.29** |
| **U.S. loss minus Chinese loss** | **-0.040** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction
annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)
release_lag_excluding_training_days = extra_review_probability*extra_review_days
internal_use_lag_excluding_training_days = extra_review_probability*extra_review_days*internal_gate_fraction
training_lag_per_affected_run_days = 0
annual_investment_input_loss_fraction = minimum(.5,financing_exposed_share*extra_risk_premium*investment_semielasticity*(1-innovation_redirection_offset))-trust_demand_investment_offset
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| setup and annual staff days | 20 / 60 / 200 | person_workdays_per_lab_year | analyst prior | Incremental setup/maintenance work beyond voluntary practice; explicit workload prior. |
| per release staff days | 3 / 10 / 40 | person_workdays_per_model | analyst prior | Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program. |
| research counterfactual fraction | 0.05 / 0.15 / 0.4 | fraction_of_compliance_labor | analyst prior | Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers. |
| extra review probability | 0.1 / 0.35 / 0.8 | probability_per_model | analyst prior | Incremental caution relative to existing tort exposure. |
| extra review days | 1 / 7 / 30 | calendar_days | analyst prior | Additional launch-risk review and remediation tail; not a legal minimum. |
| internal gate fraction | 0 / 0.05 / 0.25 | fraction_of_release_holds | analyst prior | Liability chiefly external harm; some internal research choices affected. |
| financing exposed share | 0.1 / 0.3 / 0.6 | fraction_of_annual_RnD_investment | analyst prior | Projects whose funding hurdle responds to extra liability; no universal capital freeze. |
| extra risk premium | 0 / 0.01 / 0.04 | annual_rate_fraction | analyst prior | Extra liability uncertainty/insurance-adjusted financing hurdle:0-100-400bps; entirely analyst prior. |
| trust demand investment offset | 0 / 0.001 / 0.005 | fraction_of_annual_RnD_investment | analyst prior | Possible credible safety commitment and demand/insurance benefit reallocated to R&D; wholly unmeasured analyst prior. Central0.1percent, support0to0.5percent annualR&D. Permits net investment gain rather than constraining sign. |
| investment semielasticity | 0 / 1 / 5 | fractional_investment_change_per_unit_annual_rate | analyst prior | Local response of exposed research investment to hurdle rate; not imported from medical-device coefficient. |
| innovation redirection offset | 0 / 0.3 / 0.8 | fraction_of_foregone_investment_redeployed_productively | analyst prior | Safer architectures/research substitutes can retain some capability progress. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [Galasso and Luo, Product Liability Litigation and Innovation](../sources.md#regulation-galasso26) — [original source](https://www.aeaweb.org/articles?id=10.1257/mic.20240255).
- [Gans, Regulating the Direction of Innovation](../sources.md#regulation-gans25) — [original source](https://www.nber.org/papers/w32741).
- [Gans, Staged Access and Liability for Dual-Use AI](../sources.md#regulation-gans26) — [original source](https://www.nber.org/papers/w35586).
- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).
- [Trebbi, Zhang and Simkovic, Compliance costs](../sources.md#regulation-compliance26) — [original source](https://www.nber.org/papers/w30691).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | -0.040 |
| No marginal U.S.-to-China research/teacher reliance | +0.24 |
| Half the marginal U.S.-to-China reliance | +0.10 |
| Twice the marginal U.S.-to-China reliance | -0.32 |
| No incremental AI-assisted research feedback | -0.031 |
| No China-to-U.S. research response | -0.050 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | -0.052 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | -0.071 |
| 12 months | -0.040 |
| 36 months | +0.11 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): annual investment input loss fraction (r=+0.62), teacher reliance (r=-0.46), public release gate days (r=-0.38).

Monte Carlo standard error of the numerical mean: 0.0036 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
