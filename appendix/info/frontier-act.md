# FRONTIER Act (Obernolte–Trahan)

**Best estimate: +0.81 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is +0.089 to +2.1 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

A proposed federal law that sets California-style rules nationwide, adds outside audits, and stops states from writing their own versions.

Remove this bundle obligation while preserving otherwise-same2026 voluntary practice; not the estimated causal effect of historical enactment.

Constituent requirements: safety-framework, third-party-audit, transparency-report, incident-reporting.

Union obligations; common evidence production charged once; shared release prerequisites combine by maximum, sequential review after evidence adds only its residual; no independent bundle-price prior.

## Research and calculation

The combined estimate reuses compliance evidence, integrates overlapping gate events, and keeps recurring, annual and setup clocks separate. Package-specific scope is frozen to the original menu, rather than silently treating its name as a later amended law.

Emergency order is separate annual event, often overlapping a risk-triggered remediation; do not count both.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | +0.85 |
| U.S. accumulated research effect | +0.15 |
| U.S. response to Chinese changes | +0.006 |
| **Total U.S. capability loss** | **+1.00** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.021 |
| China response to U.S. changes | +0.17 |
| **Total Chinese capability loss** | **+0.19** |
| **U.S. loss minus Chinese loss** | **+0.81** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| audit frequency per year | 2 / 2 / 2 | audits_per_year | observed | Frozen very-large-developer six-month verification frequency. |
| second audit increment fraction | 0.3 / 0.5 / 0.8 | fraction_of_first_audit_work | analyst prior | Evidence reused between annual audit and six-month verification; do not double every fixed task. |
| second audit new finding fraction | 0.1 / 0.3 / 0.6 | fraction_of_annual_finding_probability | analyst prior | Additional six-month verification reuses evidence; incremental binding finding probability relative to first audit is explicitly a prior, distinct from labor reuse. |
| common compliance labor overlap | 0.15 / 0.3 / 0.5 | fraction_of_sum | analyst prior | Common reports and governance system. |
| preempted duplicate labor fraction | 0 / 0.1 / 0.3 | fraction_of_common_work | analyst prior | Marginal state duplication eliminated; no automatic frontier-day credit. |
| emergency order probability | 0 / 0.01 / 0.05 | probability_per_lab_year | analyst prior | Incremental emergency hold under frozen powers; analyst tail. |
| emergency order days | 7 / 30 / 90 | calendar_days | analyst prior | Resolution/replacement period for rare order. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).

Component parameter priors are reused from the corresponding policy pages. The table above contains additional package-specific parameters only.

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | +0.81 |
| No marginal U.S.-to-China research/teacher reliance | +1.00 |
| Half the marginal U.S.-to-China reliance | +0.90 |
| Twice the marginal U.S.-to-China reliance | +0.63 |
| No incremental AI-assisted research feedback | +0.74 |
| No China-to-U.S. research response | +0.81 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | +1.03 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | +0.37 |
| 12 months | +0.81 |
| 36 months | +2.8 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): emergency order probability (r=+0.74), internal gate days (r=+0.59), emergency order days (r=+0.58).

Monte Carlo standard error of the numerical mean: 0.0070 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
