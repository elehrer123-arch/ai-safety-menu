# New York RAISE Act

**Best estimate: -0.045 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -0.16 to +0.021 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

New York's version of California's law, starting January 2027. It has a faster 72-hour incident deadline and a state office that can write new rules.

Remove this bundle obligation while preserving otherwise-same2026 voluntary practice; not the estimated causal effect of historical enactment.

Constituent requirements: safety-framework, transparency-report, incident-reporting.

Union obligations; common evidence production charged once; shared release prerequisites combine by maximum, sequential review after evidence adds only its residual; no independent bundle-price prior.

## Research and calculation

The combined estimate reuses compliance evidence, integrates overlapping gate events, and keeps recurring, annual and setup clocks separate. Package-specific scope is frozen to the original menu, rather than silently treating its name as a later amended law.

If combined withSB53, replace reporting deadline by stricter requirement and charge only extra state filings, not duplicate framework work.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +0.033 |
| U.S. response to Chinese changes | +0.003 |
| **Total U.S. capability loss** | **+0.036** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.010 |
| China response to U.S. changes | +0.070 |
| **Total Chinese capability loss** | **+0.080** |
| **U.S. loss minus Chinese loss** | **-0.045** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| common compliance labor overlap | 0.1 / 0.25 / 0.45 | fraction_of_summed_compliance_work | analyst prior | Reusable framework/system-card processes. |
| extra state filing staff days | 2 / 5 / 15 | person_workdays_per_year | analyst prior | Separate regulator deadlines/forms beyond one common process. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).

Component parameter priors are reused from the corresponding policy pages. The table above contains additional package-specific parameters only.

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | -0.045 |
| No marginal U.S.-to-China research/teacher reliance | +0.033 |
| Half the marginal U.S.-to-China reliance | -0.006 |
| Twice the marginal U.S.-to-China reliance | -0.12 |
| No incremental AI-assisted research feedback | -0.038 |
| No China-to-U.S. research response | -0.047 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | -0.057 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | -0.040 |
| 12 months | -0.045 |
| 36 months | -0.034 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): teacher reliance (r=-0.71), public release gate days (r=-0.35), algorithmic growth (r=-0.17).

Monte Carlo standard error of the numerical mean: 0.0007 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
