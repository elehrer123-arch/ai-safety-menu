# Six-month training pause

**Best estimate: +44 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is +20 to +74 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

No one may train an AI system more powerful than today's best for at least six months. This is what the 2023 open letter asked for.

The intervention is incremental to the same 2026 voluntary practices, with initial models, knowledge and hardware held fixed. The clock starts when the obligation is operative.

## Research and calculation

This is a six-month U.S.-only pause, with China continuing, as in the menu’s original pricing convention. Below-threshold research and permitted methods continue. Restarting partially recovers the scaling gap before month 12. The maximum loss during the pause differs from the endpoint loss.

No China pause assumed here; parent handles foreign response. Includes only incremental statutory interruption relative to same voluntary baseline. Endpoint 12-month displacement differs from maximum displacement during the pause. After year 1 the direct residual continues to recover exponentially at the same fitted recovery rate; it is not charged again yearly. That continuation is a sensitivity assumption, not evidence about three-year recovery.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | +38 |
| U.S. accumulated research effect | +13.0 |
| U.S. response to Chinese changes | +0.22 |
| **Total U.S. capability loss** | **+51** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.76 |
| China response to U.S. changes | +6.1 |
| **Total Chinese capability loss** | **+6.9** |
| **U.S. loss minus Chinese loss** | **+44** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
P=pause_days/365.25; k=-ln(1-catchup)/(1-P). While paused: c(t)=-gC*t*(1-offset), R=[1-blocked_share*(1-redeploy*value)]^(1-labor_share). After pause: c(t)=-gC*P*(1-offset)*exp(-k*(t-P)), R=1. Recovery continues exponentially beyond year 1.
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| pause days | 182.62 / 182.62 / 182.62 | days | observed | Exactly half of a 365.25-day model year; no indefinite extension. |
| permitted progress offset | 0.05 / 0.25 / 0.5 | fraction blocked direct scaling replaced | analyst prior | Post-training/inference and below-threshold methods remain permitted as described on menu. |
| scale gap recovered by yearend | 0 / 0.5 / 0.9 | fraction accumulated scaling shortfall recovered | analyst prior | Hardware and recipes accumulate; restarting permits partial catch-up. Six-month recovery evidence is absent. |
| blocked research compute share | 0.2 / 0.5 / 0.8 | fraction experimental compute | analyst prior | Training ban affects scale-validation more than all below-threshold experiments. |
| blocked compute redeployed | 0.5 / 0.85 / 0.98 | fraction blocked experimental compute | calibrated | Short-run observed85% offset anchors uncertain transfer. |
| substitute experiment value | 0.2 / 0.6 / 0.95 | relative research productivity | analyst prior | Permitted work does not necessarily produce equivalent frontier-relevant discoveries. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [Denain and Wu, Final training runs account for a minority of R&D compute spending](../sources.md#production-epoch_compute_share) — [original source](https://epoch.ai/gradient-updates/r-and-d-vs-training-compute).
- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).
- [OpenAI, Research acceleration: The view inside OpenAI](../sources.md#production-openai_acceleration) — [original source](https://openai.com/index/research-acceleration-view-inside-openai/).
- [Gundlach et al., On the Origin of Algorithmic Progress in AI](../sources.md#production-scale_dependence) — [original source](https://arxiv.org/abs/2511.21622).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | +44 |
| No marginal U.S.-to-China research/teacher reliance | +51 |
| Half the marginal U.S.-to-China reliance | +47 |
| Twice the marginal U.S.-to-China reliance | +37 |
| No incremental AI-assisted research feedback | +36 |
| No China-to-U.S. research response | +44 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | +55 |
| Universal pause with uncertain relative country exposure | -4.0 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | +77 |
| 12 months | +44 |
| 36 months | +14.6 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): scale gap recovered by yearend (r=-0.81), permitted progress offset (r=-0.32), compute growth (r=+0.25).

Monte Carlo standard error of the numerical mean: 0.1803 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
