# Model-weight security standard

**Best estimate: -0.43 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -1.46 to +0.10 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

Labs must protect unreleased models from theft by skilled attackers, including foreign spies, with strict access controls and monitoring.

An SL3-like floor for unreleased frontier weights versus current voluntary security practices, with already compliant labs credited zero incremental burden/risk change.

## Research and calculation

An SL3-like floor is incremental to existing voluntary hardening. Hazard reduction, current asset value, assimilation and decay determine the benefit. Research effort and ongoing friction determine the U.S. cost. The compromise rate and effectiveness are explicit priors.

Counts incremental technical hardening, not every voluntary security dollar. Staff days are divided by relevant total research capacity and year before root production-function conversion.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +0.17 |
| U.S. response to Chinese changes | +0.014 |
| **Total U.S. capability loss** | **+0.19** |
| China direct compute/access/security effect | +0.55 |
| China accumulated research effect | +0.047 |
| China response to U.S. changes | +0.013 |
| **Total Chinese capability loss** | **+0.61** |
| **U.S. loss minus Chinese loss** | **-0.43** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
risk_cut[remote,insider,other]=newly_changed_risk_weighted_share*[remote_risk_cut_in_changed_exposures,insider_risk_cut_in_changed_exposures,other_risk_cut_in_changed_exposures]*shared.security_rollout_fraction_year
us_research_input_loss_fraction=us_research_staff_reassigned_share*implementation_work_days/365+ongoing_research_friction
security_benefit = shared competing-hazard module; output probability reduction and conditional gap-fraction recovery, with root time conversion
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| newly changed risk weighted share | 0.05 / 0.25 / 0.6 | share of baseline compromise hazard located in exposures materially changed by mandate | analyst prior | Leading labs already strengthen defenses voluntarily; uncovered exposures may be riskier than their headcount share. |
| remote risk cut in changed exposures | 0.1 / 0.5 / 0.8 | fraction of remote compromise hazard prevented | analyst prior | Access hardening, monitoring and outbound restrictions address remote exfiltration but are not foolproof. |
| insider risk cut in changed exposures | 0.05 / 0.25 / 0.6 | fraction of insider compromise hazard prevented | analyst prior | Access minimization and exfiltration controls reduce insider success; excludes clearance vetting. |
| other risk cut in changed exposures | 0 / 0.1 / 0.4 | fraction of other compromise hazard prevented | analyst prior | Limited effect on sophisticated supply-chain/physical paths. |
| U.S. research staff reassigned share | 0.0002 / 0.003 / 0.015 | fraction of research-equivalent U.S. staff | analyst prior | Marginal research burden only, below whole-company voluntary hardening campaign. |
| implementation work days | 14 / 60 / 180 | calendar duration | analyst prior | One-time implementation counted only in first-year workload. |
| ongoing research friction | 0 / 0.0005 / 0.004 | fraction of U.S. effective research input across year | analyst prior | SL3 floor should preserve ordinary tooling; friction remains nonzero where access changes. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [Securing AI Model Weights: Preventing Theft and Misuse of Frontier Models](../sources.md#china-rand_weights_2024) — [original source](https://www.rand.org/pubs/research_reports/RRA2849-1.html).
- [Improving our alignment and security practices](../sources.md#china-anthropic_security_2026) — [original source](https://www.anthropic.com/news/improving-alignment-security-efforts).
- [CAISI’s Assessment of Z.ai’s GLM-5.3 Cyber Capabilities](../sources.md#china-nist_caisi_2026) — [original source](https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | -0.43 |
| No marginal U.S.-to-China research/teacher reliance | -0.41 |
| Half the marginal U.S.-to-China reliance | -0.42 |
| Twice the marginal U.S.-to-China reliance | -0.44 |
| No incremental AI-assisted research feedback | -0.40 |
| No China-to-U.S. research response | -0.44 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | -0.54 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | -0.056 |
| 12 months | -0.43 |
| 36 months | -0.86 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): newly changed risk weighted share (r=-0.43), remote risk cut in changed exposures (r=-0.21), insider risk cut in changed exposures (r=-0.13).

Monte Carlo standard error of the numerical mean: 0.0059 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
