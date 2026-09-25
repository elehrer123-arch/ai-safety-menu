# Anti-distillation controls

**Best estimate: -3.7 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -9.8 to -0.54 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

Labs must verify large API customers, hide models' full reasoning, and watch for accounts that copy model outputs to train competing models.

Mandated coordinated API vetting, restrictions on full traces and detection versus current voluntary enforcement and existing product choices; does not ban all open models or independent Chinese/self-distillation.

## Research and calculation

The same marginal teacher-reliance parameter is used here and for public-release delays. Measured benefits from distillation establish that teachers can help; they do not establish how much China needs U.S. teachers after domestic alternatives and self-training.

Multiply the China effect by the shared algorithmic-knowledge contribution to progress in the root engine, not full national progress. If foreign teacher dependence is zero, benefit is zero. Experimental score uplifts establish potential value but do not set the dependence prior mechanically.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +0.15 |
| U.S. response to Chinese changes | +0.086 |
| **Total U.S. capability loss** | **+0.24** |
| China direct compute/access/security effect | +3.6 |
| China accumulated research effect | +0.32 |
| China response to U.S. changes | +0.015 |
| **Total Chinese capability loss** | **+4.0** |
| **U.S. loss minus Chinese loss** | **-3.7** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
cn_algorithmic_knowledge_flow_loss_fraction = shared.frontier_teacher_channel_share*additional_blocked_teacher_access*(1-shared.teacher_substitution_recovery)*rollout_fraction_year
us_research_input_loss_fraction=us_research_staff_reassigned_share*implementation_work_days/365+us_research_product_friction
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| additional blocked teacher access | 0.05 / 0.3 / 0.65 | fraction of remaining valuable U.S. teacher access prevented by mandate | analyst prior | Incremental to existing restrictions; prior deliberately below total attack detection or account closure rate. |
| rollout fraction year | 0.25 / 0.75 / 1 | fraction of first year mature coordination operates | analyst prior | Engineering, shared telemetry and enforcement require time. |
| U.S. research staff reassigned share | 0 / 0.002 / 0.01 | fraction of U.S. frontier research-equivalent staff at full rollout | analyst prior | Most costs fall on trust/safety/product staff; count only research-equivalent diversion. |
| implementation work days | 7 / 45 / 120 | calendar work duration during first year | analyst prior | Temporary build-out; not the eventual national delay. |
| U.S. research product friction | 0 / 0.0005 / 0.005 | fraction of research-equivalent output lost across year from legitimate access limits | analyst prior | Small central effect because laboratories retain access to their own internal models. Public developer welfare loss is outside frontier lead estimand. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [Detecting and preventing distillation attacks](../sources.md#china-anthropic_distill_2026) — [original source](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | -3.7 |
| No marginal U.S.-to-China research/teacher reliance | +0.14 |
| Half the marginal U.S.-to-China reliance | -1.79 |
| Twice the marginal U.S.-to-China reliance | -7.6 |
| No incremental AI-assisted research feedback | -3.4 |
| No China-to-U.S. research response | -3.8 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | -4.8 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | -0.93 |
| 12 months | -3.7 |
| 36 months | -17.4 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): teacher reliance (r=-0.75), additional blocked teacher access (r=-0.46), rollout fraction year (r=-0.30).

Monte Carlo standard error of the numerical mean: 0.0340 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
