# AI Risk Evaluation Act (Hawley–Blumenthal)

**Best estimate: -0.40 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -1.50 to +0.022 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

A proposed federal law that would require every frontier model to go through a Department of Energy testing program before it can be sold across state lines.

Remove this bundle obligation while preserving otherwise-same2026 voluntary practice; not the estimated causal effect of historical enactment.

Constituent requirements: internal-evals, third-party-eval.

Union obligations; common evidence production charged once; shared release prerequisites combine by maximum, sequential review after evidence adds only its residual; no independent bundle-price prior.

## Research and calculation

The combined estimate reuses compliance evidence, integrates overlapping gate events, and keeps recurring, annual and setup clocks separate. Package-specific scope is frozen to the original menu, rather than silently treating its name as a later amended law.

Do not silently upgrade participation duty into a veto based on findings; separate agency-in-practice pressure scenario.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +0.14 |
| U.S. response to Chinese changes | +0.019 |
| **Total U.S. capability loss** | **+0.15** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.072 |
| China response to U.S. changes | +0.49 |
| **Total Chinese capability loss** | **+0.56** |
| **U.S. loss minus Chinese loss** | **-0.40** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| classified extra service days | 0 / 7 / 28 | calendar_days | analyst prior | Security/onboarding/specialized tests beyond normal qualifying evaluation. |
| government queue days | 0 / 7 / 45 | calendar_days | analyst prior | First-year DOE program congestion; analyst prior. |
| completion required probability | 0.25 / 0.75 / 1 | probability_per_model | analyst prior | Participation compliance interpreted to require completed testing/report before release; statute does not explicitly demand safety approval. |
| common compliance labor overlap | 0.1 / 0.3 / 0.5 | fraction_of_sum | analyst prior | Internal results reused by external program. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [AI Risk Evaluation Act S2938 introduced text](../sources.md#regulation-s2938) — [original source](https://www.govinfo.gov/content/pkg/BILLS-119s2938is/html/BILLS-119s2938is.htm).
- [AISI, Early lessons from evaluating frontier AI systems](../sources.md#production-aisi) — [original source](https://www.aisi.gov.uk/blog/early-lessons-from-evaluating-frontier-ai-systems).
- [Charnock et al., Expanding external access](../sources.md#regulation-access26) — [original source](https://arxiv.org/abs/2601.11916).
- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).

Component parameter priors are reused from the corresponding policy pages. The table above contains additional package-specific parameters only.

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | -0.40 |
| No marginal U.S.-to-China research/teacher reliance | +0.13 |
| Half the marginal U.S.-to-China reliance | -0.13 |
| Twice the marginal U.S.-to-China reliance | -0.94 |
| No incremental AI-assisted research feedback | -0.35 |
| No China-to-U.S. research response | -0.42 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | -0.52 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | -0.33 |
| 12 months | -0.40 |
| 36 months | -0.42 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): public release gate days (r=-0.62), teacher reliance (r=-0.57), internal gate days (r=-0.42).

Monte Carlo standard error of the numerical mean: 0.0061 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
