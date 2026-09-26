# Secure AI Development Act (Warner)

**Best estimate: -0.13 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -0.61 to +0.011 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

A proposed federal law that would require labs to give the NSA's AI Security Center access to new models 21 days before release.

Remove this bundle obligation while preserving otherwise-same2026 voluntary practice; not the estimated causal effect of historical enactment.

Constituent requirements: evaluator-window.

Union obligations; common evidence production charged once; shared release prerequisites combine by maximum, sequential review after evidence adds only its residual; no independent bundle-price prior.

## Research and calculation

The combined estimate reuses compliance evidence, integrates overlapping gate events, and keeps recurring, annual and setup clocks separate. Package-specific scope is frozen to the original menu, rather than silently treating its name as a later amended law.



The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +0.038 |
| U.S. response to Chinese changes | +0.006 |
| **Total U.S. capability loss** | **+0.044** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.023 |
| China response to U.S. changes | +0.15 |
| **Total Chinese capability loss** | **+0.17** |
| **U.S. loss minus Chinese loss** | **-0.13** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| required calendar access | 21 / 21 / 21 | calendar_days | observed | Verified Section3(c). |
| weights handoff extra days | 0 / 2 / 10 | calendar_days | analyst prior | Incremental secure handoff relative to existing API evaluator access; prior. |
| additional staff days | 2 / 5 / 20 | person_workdays_per_model | analyst prior | Secure packaging/liaison work beyond access-window overhead. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [Secure AI Development Act S5061 introduced text](../sources.md#regulation-s5061) — [original source](https://www.govinfo.gov/content/pkg/BILLS-119s5061is/html/BILLS-119s5061is.htm).
- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).

Component parameter priors are reused from the corresponding policy pages. The table above contains additional package-specific parameters only.

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | -0.13 |
| No marginal U.S.-to-China research/teacher reliance | +0.038 |
| Half the marginal U.S.-to-China reliance | -0.047 |
| Twice the marginal U.S.-to-China reliance | -0.30 |
| No incremental AI-assisted research feedback | -0.11 |
| No China-to-U.S. research response | -0.14 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | -0.17 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | -0.11 |
| 12 months | -0.13 |
| 36 months | -0.14 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): public release gate days (r=-0.73), internal gate days (r=-0.55), teacher reliance (r=-0.40).

Monte Carlo standard error of the numerical mean: 0.0027 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
