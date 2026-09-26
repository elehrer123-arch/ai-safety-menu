# Consent to train on copyrighted work

**Best estimate: +26 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is +12.3 to +47 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

AI companies must get clear permission, usually a paid license, before training on copyrighted books, articles, art or personal data. Anyone whose work is used without consent can sue.

The intervention is incremental to the same 2026 voluntary practices, with initial models, knowledge and hardware held fixed. The clock starts when the obligation is operative.

## Research and calculation

Quality-adjusted unique data can be licensed, replaced, repeated or traded against parameters. The model reoptimizes the training recipe. Published saturation coefficients come from smaller models, so frontier transport and legally available substitutions remain important assumptions.

Data ratio changes quality-adjusted unique tokens; repeated tokens and excess parameters follow fitted saturation functions. Equal-budget minimization captures recipe adaptation. The data penalty is a level term and already includes existing repetition; do not impose an extra raw-token penalty. Recurring budget loss applies once to direct training and once to distinct research inputs. No retroactive destruction/retraining required.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | +22 |
| U.S. accumulated research effect | +7.9 |
| U.S. response to Chinese changes | +0.12 |
| **Total U.S. capability loss** | **+30** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.46 |
| China response to U.S. changes | +3.1 |
| **Total Chinese capability loss** | **+3.5** |
| **U.S. loss minus Chinese loss** | **+26** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
uData=1-m+m*recovered*quality. Optimize N,D with N*D=1 at U=uData/baseline_epochs using effective-token/parameter saturation. logC_data=-(2/alpha)*log(L_policy/L_base)*dependency. Let h(t)=min(1,t*365.25/transition), z(t)=min(1,max(0,(t-transition/365.25)/(1-transition/365.25))). delay(t)=transition*critical*h(t)*(1-(1-remaining)*z(t)); c(t)=h(t)*(logC_data+ln(1-budget))-gTotal*delay(t)/365.25; R(t)=1-h(t)*budget.
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| data needing new permission | 0.3 / 0.6 / 0.9 | share baseline unique corpus | analyst prior | Unknown proprietary mixtures; copyright and personal-data scope potentially broad. |
| affected data recovered | 0.2 / 0.65 / 0.95 | fraction retained or licensed/replaced | analyst prior | Allowed corpora and contracts offer substitutes; frontier/domain coverage uncertain. |
| replacement quality | 0.75 / 0.95 / 1.1 | effective tokens/replaced token | analyst prior | Allows slightly better curated replacements; not equating token count to useful information. |
| baseline epochs | 1 / 2 / 4 | total passes through unique data | analyst prior | Public recipes vary; repeat-data response conditions on baseline usage. |
| repeat data saturation | 5 / 15.388 / 30 | R_D constant | calibrated | Published fitted mode, deliberately broadened for transport; not published confidence interval. |
| parameter saturation | 2 / 5.3097 / 12 | R_N constant | calibrated | Published fitted mode with structural transport uncertainty. |
| loss exponent | 0.28 / 0.353 / 0.42 | scaling exponent | calibrated | Equalized parameter/data exponents around studyfit for normalized toy model; task transport uncertain. |
| pretraining dependency | 0.4 / 0.7 / 1 | share effective-compute penalty that carries to target frontier | analyst prior | Downstream/post-training substitution may absorb part of pretraining-loss penalty. |
| licensing budget share | 0 / 0.02 / 0.08 | shareR&Dbudget unavailable for other inputs | analyst prior | Incremental recurring licensing and provenance costs; genericbudgetprior, not a measured licensingprice. |
| transition days | 7 / 30 / 90 | calendar daysdata preparation | analyst prior | A bounded one-time licensing/filtering/pipeline transition; not automatic retraining of existing models. |
| transition critical share | 0.1 / 0.35 / 0.8 | fraction transition duration on criticalpath | analyst prior | Most bargaining and preparation can overlap; no one-for-one elapsed-days assumption. |
| transition gap remaining | 0.1 / 0.5 / 1 | fractiondelayremainingatyear1 | analyst prior | Allows recovery of a one-time schedule disturbance. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [Kandpal et al., The Common Pile v0.1](../sources.md#production-commonpile) — [original source](https://arxiv.org/abs/2506.05209).
- [Muennighoff et al., Scaling Data-Constrained Language Models](../sources.md#production-data_scaling) — [original source](https://jmlr.org/papers/v26/24-1000.html).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | +26 |
| No marginal U.S.-to-China research/teacher reliance | +30 |
| Half the marginal U.S.-to-China reliance | +28 |
| Twice the marginal U.S.-to-China reliance | +23 |
| No incremental AI-assisted research feedback | +22 |
| No China-to-U.S. research response | +26 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | +33 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | +29 |
| 12 months | +26 |
| 36 months | +33 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): data log effective compute effect (r=-0.61), quality adjusted unique data ratio (r=-0.45), transition days (r=+0.39).

Monte Carlo standard error of the numerical mean: 0.1193 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
