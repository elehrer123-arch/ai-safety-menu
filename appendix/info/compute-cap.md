# Hard cap on training compute

**Best estimate: +119 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is +71 to +173 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

No training run may use more computing power than today's largest runs, and the limit never rises.

The intervention is incremental to the same 2026 voluntary practices, with initial models, knowledge and hardware held fixed. The clock starts when the obligation is operative.

## Research and calculation

A permanent ceiling progressively binds as baseline training compute grows. Reallocation to other experiments, algorithmic work and permitted inference/post-training recover part of the lost scale. The result is an endpoint shortfall, not a fixed annual bill to add forever.

Ceiling applies to training-run compute, not all national compute, inference or every small experiment. Cap-driven direct scaling loss and remaining experimental-research losses are separate. The algorithmic baseline already includes historical scale-dependent progress: the resource penalty is only its marginal response to the cap, not another entire attribution share.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | +114 |
| U.S. accumulated research effect | +13.5 |
| U.S. response to Chinese changes | +0.17 |
| **Total U.S. capability loss** | **+128** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.60 |
| China response to U.S. changes | +7.8 |
| **Total Chinese capability loss** | **+8.4** |
| **U.S. loss minus Chinese loss** | **+119** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
gap(t)=max(0,gC*t-headroom)*compliance; c(t)=-(1-recovery)*gap(t); resource_R=[1-share*(1-exp(-gap))*(1-redeploy*value)]^(1-labor_share).
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| cap headroom log | 0 / 0 / 0.4 | log compute above current frontier | analyst prior | Ceiling about current largest run, with measurement/implementation headroom. |
| binding compliance | 0.85 / 0.97 / 1 | share targeted scaling actually prevented | analyst prior | High-enforcement domestic policy; not global coverage. |
| scale gap recovered other channels | 0.05 / 0.25 / 0.6 | fraction direct scaling gap | analyst prior | Post-training/inference/ensembles offset some capability loss; compute redeployment85% is not reused as capability recovery. |
| frontier scale dependent experiments | 0.1 / 0.35 / 0.7 | research-compute share | analyst prior | Most experiments are not final frontier training; a material share nevertheless needs frontier-relevant scale. |
| blocked compute redeployed | 0.5 / 0.85 / 0.98 | fraction blocked experimental compute | calibrated | 85% measured short-run offset anchors mode; transport from one restriction is uncertain. |
| substitute experiment value | 0.2 / 0.6 / 0.95 | productivity relative to blocked experiment | analyst prior | Quantity of reused compute is not value of the research it enables. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [Denain and Wu, Final training runs account for a minority of R&D compute spending](../sources.md#production-epoch_compute_share) — [original source](https://epoch.ai/gradient-updates/r-and-d-vs-training-compute).
- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).
- [OpenAI, Research acceleration: The view inside OpenAI](../sources.md#production-openai_acceleration) — [original source](https://openai.com/index/research-acceleration-view-inside-openai/).
- [Gundlach et al., On the Origin of Algorithmic Progress in AI](../sources.md#production-scale_dependence) — [original source](https://arxiv.org/abs/2511.21622).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | +119 |
| No marginal U.S.-to-China research/teacher reliance | +127 |
| Half the marginal U.S.-to-China reliance | +123 |
| Twice the marginal U.S.-to-China reliance | +111 |
| No incremental AI-assisted research feedback | +110 |
| No China-to-U.S. research response | +119 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | +149 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | +52 |
| 12 months | +119 |
| 36 months | +410 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): scale gap recovered other channels (r=-0.63), compute growth (r=+0.48), algorithmic growth (r=-0.47).

Monte Carlo standard error of the numerical mean: 0.3431 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
