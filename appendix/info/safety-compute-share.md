# One-third of AI research budgets on safety

**Best estimate: +32 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is +9.3 to +55 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

Frontier labs must spend at least a third of their AI research budget, including computing power, on safety work such as alignment, interpretability and testing, rather than on making models more capable.

The intervention is incremental to the same 2026 voluntary practices, with initial models, knowledge and hardware held fixed. The clock starts when the obligation is operative.

## Research and calculation

The one-third requirement covers R&D budgets. A one-week AI-R&D compute snapshot at one lab is informative but is not a measurement of industry-wide total-budget safety shares. Safety-capability overlap and a possible budget response reduce displacement. A permanent share change is a level/resource shock, not another identical annual delay.

Apply equal proportional input ratio to direct production training and the separate research-input bundle. Budget and safety overlap apply once. The direct compute term is a lasting level shift; algorithmic feedback is integrated separately. A one-third total-budget rule is interpreted as covering compute and staff with proportional effective reallocation; alternate allocation optimization should be a sensitivity.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | +20 |
| U.S. accumulated research effect | +14.9 |
| U.S. response to Chinese changes | +0.096 |
| **Total U.S. capability loss** | **+35** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.35 |
| China response to U.S. changes | +3.0 |
| **Total Chinese capability loss** | **+3.3** |
| **U.S. loss minus Chinese loss** | **+32** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
r=(1+b)*(1-s1+k*s1)/(1-s0+k*s0); c(t)=ramp(t)*ln(r); resource_R(t)=exp(c(t)).
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| baseline safety share | 0.03 / 0.06 / 0.15 | R&D budget share | calibrated | Observed6% compute anchors mode; wider range for other labs, salaries and less conservative definitions. |
| mandated safety share | 0.33333 / 0.33333 / 0.33333 | R&D budget share | observed | Specified policy. |
| safety capability cobenefit | 0 / 0.15 / 0.4 | relative capability productivity of safety dollar | analyst prior | Safety can improve reliability, tools and safe usable capabilities; not all spending contributes to measured frontier. |
| budget expansion | 0 / 0.08 / 0.25 | extra total R&D budget/baseline | analyst prior | Marginal capital response over one year; allows partial offset without assuming unlimited fundraising. |
| implementation ramp days | 0 / 90 / 180 | days | analyst prior | Organizational reallocation ramps linearly; not a legal grace-period assertion. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [Anthropic, Measurements for understanding the pace of AI development inside frontier labs](../sources.md#production-anthropic_allocation) — [original source](https://www.anthropic.com/institute/measuring-pace-of-ai-development).
- [AI Safety Menu policy definitions](../sources.md#production-menu) — [original source](https://elehrer123-arch.github.io/ai-safety-menu/#/).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | +32 |
| No marginal U.S.-to-China research/teacher reliance | +35 |
| Half the marginal U.S.-to-China reliance | +33 |
| Twice the marginal U.S.-to-China reliance | +28 |
| No incremental AI-assisted research feedback | +28 |
| No China-to-U.S. research response | +32 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | +39 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | +26 |
| 12 months | +32 |
| 36 months | +47 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): effective input ratio (r=-0.93), budget expansion (r=-0.73), safety capability cobenefit (r=-0.47).

Monte Carlo standard error of the numerical mean: 0.1544 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
