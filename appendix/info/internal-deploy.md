# Safety checks before internal use

**Best estimate: +1.12 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is +0.18 to +2.9 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

Before a lab's own staff can use a new frontier model, for example to write code and run experiments, the lab must finish its dangerous-capability tests and put safeguards in place, the same way it would before a public launch.

The intervention is incremental to the same 2026 voluntary practices, with initial models, knowledge and hardware held fixed. The clock starts when the obligation is operative.

## Research and calculation

A newer model improves some research tasks over the predecessor already available. The model charges that incremental research productivity during the gate, using exposed task share and model cadence. It does not charge the same capability both as a calendar delay and as lost research output.

No direct training or public-release stop is imposed. Foregone incremental productivity feeds the shared R&D equation. Gate overlap is already in gate_days; do not discount overlap again. Generation-average exposure avoids mechanically adding the full gate once per model.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +1.21 |
| U.S. response to Chinese changes | +0.002 |
| **Total U.S. capability loss** | **+1.21** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.009 |
| China response to U.S. changes | +0.089 |
| **Total Chinese capability loss** | **+0.098** |
| **U.S. loss minus Chinese loss** | **+1.12** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
f=min(1,gate/cadence)*exposure*u/(1+u); rL(t)=1-ramp(t)*f; resource_R(t)=rL(t)^labor_share; c(t)=0.
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| incremental gate days | 0 / 7 / 21 | days/model-generation | calibrated | Standard tests1-2weeks; zero for existing/overlapped gates, upper adds safeguards. Increment over voluntary practice. |
| model generation days | 30 / 60 / 120 | days/generation | analyst prior | Effective internally useful upgrades; not count of every public API variant. |
| research work exposure | 0.4 / 0.7 / 1 | share of cognitive research labor | calibrated | >90%AI collaboration at one lab suggests broad usage; newest model affects less than all work. |
| new model incremental uplift | 0.05 / 0.2 / 0.6 | productivity gain vs previous available model | analyst prior | Much less than4x versus noAI; no direct randomized newest-versus-previous effect. |
| implementation ramp days | 0 / 30 / 90 | days | analyst prior | Rule and evaluator capacity phase in over first quarter. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [AISI, Early lessons from evaluating frontier AI systems](../sources.md#production-aisi) — [original source](https://www.aisi.gov.uk/blog/early-lessons-from-evaluating-frontier-ai-systems).
- [Anthropic, Measurements for understanding the pace of AI development inside frontier labs](../sources.md#production-anthropic_allocation) — [original source](https://www.anthropic.com/institute/measuring-pace-of-ai-development).
- [Anthropic, When AI builds itself](../sources.md#production-anthropic_uplift) — [original source](https://www.anthropic.com/institute/recursive-self-improvement).
- [OpenAI, Research acceleration: The view inside OpenAI](../sources.md#production-openai_acceleration) — [original source](https://openai.com/index/research-acceleration-view-inside-openai/).
- [Cunningham et al., The Economics of Recursive Self-Improvement](../sources.md#production-rsi2026) — [original source](https://arxiv.org/abs/2609.15802).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | +1.12 |
| No marginal U.S.-to-China research/teacher reliance | +1.21 |
| Half the marginal U.S.-to-China reliance | +1.16 |
| Twice the marginal U.S.-to-China reliance | +1.02 |
| No incremental AI-assisted research feedback | +0.99 |
| No China-to-U.S. research response | +1.11 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | +1.42 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | +0.61 |
| 12 months | +1.12 |
| 36 months | +2.2 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): cognitive labor loss fraction (r=+0.87), incremental gate days (r=+0.58), new model incremental uplift (r=+0.39).

Monte Carlo standard error of the numerical mean: 0.0099 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
