# Advanced chip export controls

**Best estimate: -27 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -54 to -9.0 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

The U.S. bans sales of advanced AI chips and chipmaking tools to China.

Maintain the frozen site’s advanced-accelerator and manufacturing-input restrictions for 12 months versus relaxing those covered restrictions at the start; current stock, voluntary practices, unrelated sanctions, and non-U.S. export decisions remain. China purchases and deployments ramp, not instant parity.

## Research and calculation

This maintains the specified controls versus prospective relaxation today. It preserves existing stocks, allows deployment lags, and models the extra hardware China would actually buy and use. It does not convert a four-year chip-generation lag directly into a national capability lag.

Price present restrictions relative to specified relaxation, not versus a historically never-restricted China. Nominal H100e is an imperfect common unit. The largest uncertainty is incremental purchases and frontier relevance, not the measured chip-generation gap.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | -1.40 |
| U.S. accumulated research effect | -0.024 |
| U.S. response to Chinese changes | +0.65 |
| **Total U.S. capability loss** | **-0.78** |
| China direct compute/access/security effect | +22 |
| China accumulated research effect | +4.3 |
| China response to U.S. changes | -0.053 |
| **Total Chinese capability loss** | **+26** |
| **U.S. loss minus Chinese loss** | **-27** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
AUTHORITATIVE PATH: solve k/(1-exp(-k))=endpoint_to_average_compute_ratio; C0=baseline_china_average_usable_compute*k/expm1(k)>0; Cbase(t)=C0*exp(k*t), with t in years
delivery_factor(t)=expm1(k*max(t-deployment_lag_days/365.25,0))/expm1(k); extra_china_compute=(nvidia_annual_output_h100e*incremental_china_purchase_share+extra_domestic_output_after_relaxation)*usable_fraction_of_added_rated_compute*delivery_factor
direct_cn_logcompute(t)=-share_relevant_to_frontier_progress*log1p(extra_china_compute/Cbase(t)); cn_compute_ratio=exp(direct_cn_logcompute)
direct_us_logcompute(t)=log1p(redirected_share_to_us_under_controls*nvidia_annual_output_h100e*incremental_china_purchase_share*usable_fraction_of_added_rated_compute*delivery_factor/Ubase(t)); us_compute_ratio=exp(direct_us_logcompute)
Compute ratios enter both the direct frontier training channel and the root research-compute production function, where the latter contributes only additional algorithmic progress.
us_research_input_loss_fraction = supplier_innovation_loss_us
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| nvidia annual output h100e | 18 / 23 / 30 | million rated H100e/year | calibrated | Mode equals published 2026 forecast; interval is our predictive uncertainty, not the paper’s confidence interval. Hold 2026 output pace for this exercise. |
| incremental china purchase share | 0.02 / 0.1 / 0.2 | fraction of Nvidia annual output additional to purchases allowed in baseline | analyst prior | Net incremental access after relaxing covered controls. One-tenth mode reflects strong demand but U.S. contracted allocation and Chinese budgets; deliberately below unconstrained parity. Existing permitted purchases are not recounted. |
| deployment lag days | 30 / 90 / 180 | calendar days | analyst prior | Ordering, delivery, power and commissioning prevent immediate use. Includes supplying HBM/equipment pathway lag. |
| usable fraction of added rated compute | 0.4 / 0.7 / 0.95 | fraction | analyst prior | Allows for provisioning, interconnect, utilization and imperfect substitution into relevant training/inference workloads. |
| extra domestic output after relaxation | 0 / 0.3 / 1 | million rated H100e delivered in first year | analyst prior | Additional domestic chip output from newly available manufacturing inputs. Small first-year mode because fabs cannot be rebuilt instantly; final-chip imports are faster. |
| baseline china average usable compute | 1.5 / 3 / 5.5 | million H100e during next 12 months | calibrated | End-2025 owned stock near 1m plus 2026 output, illicit imports, rentals and further build-out; 3m is an analyst extrapolation, not a reported current stock. Broad upper accommodates substantial unobserved access. |
| endpoint to average compute ratio | 1.05 / 1.4 / 1.8 | ratio of end-year stock to average stock over first year | analyst prior | Growing baseline stock; use baseline_average times this factor for endpoint compute changes. Share draw across U.S. and China as a simple trend scenario. |
| share relevant to frontier progress | 0.25 / 0.6 / 1 | fraction of country-level marginal compute increase available to frontier production | analyst prior | Not all additional chips serve frontier research or change a binding constraint. Avoids treating all national compute as a frontier cluster. |
| redirected share to U.S. under controls | 0 / 0.5 / 0.9 | fraction of prevented China sales deployed by U.S. users instead | analyst prior | Current supply allocation could redirect rather than destroy sales. This is a small positive U.S. resource effect of maintaining controls. |
| baseline U.S. average usable compute | 20 / 35 / 60 | million H100e during next 12 months | analyst prior | Rough 2026 installed/allocated stock extrapolation. Wider than ownership evidence; only scales redirection term. |
| supplier innovation loss us | 0 / 0.001 / 0.01 | fraction of U.S. research-equivalent input over first year | analyst prior | Revenue constraints may reduce upstream innovation, but near-term supply-constrained sales and long R&D lags make a small first-year mode appropriate. Not imported from market capitalization loss. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [Will Huawei catch up to Nvidia by 2030?](../sources.md#china-epoch_huawei_2026) — [original source](https://epoch.ai/publications/huaweis-roadmap-to-2031).
- [Introducing the AI Chip Owners Explorer](../sources.md#china-epoch_owners_2026) — [original source](https://epoch.ai/latest/introducing-the-ai-chip-owners-explorer).
- [Trade data is consistent with more than $3 billion of chips smuggled into China via Malaysia](../sources.md#china-epoch_malaysia_2026) — [original source](https://epoch.ai/data-insights/malaysia-china-chip-smuggling).
- [Securing Technological Leadership? The Cost of Export Controls on Firms](../sources.md#china-crosignani_2025) — [original source](https://www.newyorkfed.org/research/staff_reports/sr1096).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | -27 |
| No marginal U.S.-to-China research/teacher reliance | -27 |
| Half the marginal U.S.-to-China reliance | -27 |
| Twice the marginal U.S.-to-China reliance | -27 |
| No incremental AI-assisted research feedback | -25 |
| No China-to-U.S. research response | -27 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | -33 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | -9.7 |
| 12 months | -27 |
| 36 months | -69 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): incremental china purchase share (r=-0.49), share relevant to frontier progress (r=-0.43), baseline china average usable compute (r=+0.38).

Monte Carlo standard error of the numerical mean: 0.1617 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
