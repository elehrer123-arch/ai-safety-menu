# Human sign-off on automated AI research

**Best estimate: +3.8 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is +1.17 to +8.0 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

Labs may not let AI systems run AI research on their own from start to finish. A human researcher has to direct and approve the experiments AI agents run, and labs must report how much of their research AI is doing.

The intervention is incremental to the same 2026 voluntary practices, with initial models, knowledge and hardware held fixed. The clock starts when the obligation is operative.

## Research and calculation

Existing human oversight is already in the baseline. Incremental checkpoints create service and handoff delays, magnified when reviewers are busy. Only affected task chains are charged. Fully autonomous work rises under an explicit first-year scenario rather than being assumed ubiquitous today.

AI-leads and fully autonomous shares are kept disjoint by capping s4 at1-s5. Review queue is an illustrative adapted operation, not an empirically fitted queue. Required human approval is per meaningful experiment/chain, not every token or tool call. Worst-case near-overload is a sensitivity, not baseline.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +4.1 |
| U.S. response to Chinese changes | +0.005 |
| **Total U.S. capability loss** | **+4.1** |
| China direct compute/access/security effect | 0.000 |
| China accumulated research effect | +0.019 |
| China response to U.S. changes | +0.24 |
| **Total Chinese capability loss** | **+0.26** |
| **U.S. loss minus Chinese loss** | **+3.8** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
review=service/(1-utilization)+handoff [M/M/1]; h=review/(cycle+review); s4(t)=linear(start,end), s5(t)=t*end5; Lloss=s4*additional*h+s5*u_aut/(1+u_aut); resource_R=(1-ramp*Lloss)^labor_share.
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| current ai leads share | 0.15 / 0.26 / 0.4 | cognitive task share | calibrated | 26% at Anthropic, wide industry/sample transport interval. |
| endyear ai leads share | 0.3 / 0.55 / 0.8 | cognitive task share | analyst prior | Forward adoption judgment; current0.26 is not frozen through the year. |
| endyear fully autonomoU.S. share | 0 / 0.1 / 0.4 | cognitive task share | analyst prior | Starts zero; prospective uptake grows linearly. This is an adoption forecast, not a claim of existing full automation. |
| incremental checkpoint share | 0.1 / 0.4 / 0.8 | fraction eligible chains receiving an additional checkpoint | analyst prior | Many successful tasks already include human steering; only extra gates relative to voluntary practice count. |
| review service hours | 0.05 / 0.25 / 1 | hours/checkpoint | analyst prior | Three to60minutes substantive service; measured lab service times unavailable. |
| reviewer utilization | 0.3 / 0.65 / 0.9 | fraction capacity | analyst prior | Staffing and batching keep mean below overload; tail models congestion. |
| handoff hours | 0.05 / 0.2 / 1 | hours/checkpoint | analyst prior | Context restoration and handoff in addition to queue service. |
| autonomoU.S. cycle hours | 2 / 6 / 24 | hours/chain | calibrated | Observed reporting includes4-8hour tasks; broad range for experiments and agent chains. |
| autonomy uplift over supervised | 0.2 / 0.5 / 2 | productivity gain | analyst prior | Gain specifically attributable to removing human dependencies, not overallAI uplift. |
| implementation ramp days | 0 / 30 / 90 | days | analyst prior | Incremental controls phase in. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [Anthropic, Measurements for understanding the pace of AI development inside frontier labs](../sources.md#production-anthropic_allocation) — [original source](https://www.anthropic.com/institute/measuring-pace-of-ai-development).
- [Demirer et al., Chaining Tasks, Redefining Work](../sources.md#production-chaining2026) — [original source](https://arxiv.org/abs/2606.15960).
- [OpenAI, Research acceleration: The view inside OpenAI](../sources.md#production-openai_acceleration) — [original source](https://openai.com/index/research-acceleration-view-inside-openai/).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | +3.8 |
| No marginal U.S.-to-China research/teacher reliance | +4.1 |
| Half the marginal U.S.-to-China reliance | +4.0 |
| Twice the marginal U.S.-to-China reliance | +3.6 |
| No incremental AI-assisted research feedback | +3.5 |
| No China-to-U.S. research response | +3.8 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | +4.9 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | +1.30 |
| 12 months | +3.8 |
| 36 months | +11.4 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): endyear cognitive labor loss fraction (r=+0.77), endyear fully autonomoU.S. share (r=+0.54), affected chain throughput loss (r=+0.39).

Monte Carlo standard error of the numerical mean: 0.0250 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
