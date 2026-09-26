# EU AI Act, systemic-risk models

**Best estimate: -0.50 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -1.56 to +0.078 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

Europe's rules for the most powerful models, enforceable since August 2026. Labs must test for serious risks, give outside testers time with the model, report incidents, and file a report before release.

Remove this bundle obligation while preserving otherwise-same2026 voluntary practice; not the estimated causal effect of historical enactment.

Constituent requirements: safety-framework, internal-evals, third-party-eval, evaluator-window, transparency-report, incident-reporting, weight-security.

Union obligations; common evidence production charged once; shared release prerequisites combine by maximum, sequential review after evidence adds only its residual; no independent bundle-price prior.

## Research and calculation

The combined estimate reuses compliance evidence, integrates overlapping gate events, and keeps recurring, annual and setup clocks separate. Package-specific scope is frozen to the original menu, rather than silently treating its name as a later amended law.



The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +0.23 |
| U.S. response to Chinese changes | +0.018 |
| **Total U.S. capability loss** | **+0.25** |
| China direct compute/access/security effect | +0.55 |
| China accumulated research effect | +0.064 |
| China response to U.S. changes | +0.13 |
| **Total Chinese capability loss** | **+0.74** |
| **U.S. loss minus Chinese loss** | **-0.50** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| common compliance labor overlap | 0.2 / 0.4 / 0.65 | fraction_of_sum | analyst prior | Same test/evidence package supports internal/external evaluation and report. |
| access floor applies probability | 0.25 / 0.6 / 1 | probability_per_model | analyst prior | Code says appropriate for most methods, unlike standalone universal floor. |
| global release synchronization probability | 0 / 0.4 / 1 | probability_per_model | analyst prior | Otherwise EU-only release hold does not delay non-EU access; source gives regional examples, probability is prior. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [EU GPAI Code of Practice safety/security](../sources.md#regulation-eu_code) — [original source](https://ec.europa.eu/newsroom/dae/redirection/document/118119).
- [GovAI, Delays to Frontier AI in EU and UK](../sources.md#regulation-govai26) — [original source](https://www.governance.ai/research-paper/delays-to-frontier-ai-in-the-eu-and-uk).
- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).

Component parameter priors are reused from the corresponding policy pages. The table above contains additional package-specific parameters only.

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | -0.50 |
| No marginal U.S.-to-China research/teacher reliance | -0.36 |
| Half the marginal U.S.-to-China reliance | -0.43 |
| Twice the marginal U.S.-to-China reliance | -0.64 |
| No incremental AI-assisted research feedback | -0.46 |
| No China-to-U.S. research response | -0.52 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | -0.62 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | -0.12 |
| 12 months | -0.50 |
| 36 months | -0.91 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): weight-security.newly changed risk weighted share (r=-0.41), weight-security.remote risk cut in changed exposures (r=-0.21), teacher reliance (r=-0.13).

Monte Carlo standard error of the numerical mean: 0.0060 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
