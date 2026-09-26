# Isolated secure development environment

**Best estimate: +2.7 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -2.4 to +9.3 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

Frontier research moves onto isolated computer networks with tight physical security, much like classified government work.

Frontier research moved into isolated networks and physical access controls; existing voluntary cluster isolation remains baseline. First-year rollout includes modular migration, not assumed immediate construction of entirely new facilities.

## Research and calculation

The model allows internal AI tools inside isolated environments. Research friction applies only to newly affected work; migration is additional. A policy that prohibited such tools or required immediate construction of an entirely new facility would have a different scope.

Treat as reduced effective research inputs, not uniform national progress delay. The secure environment remains compatible with internal AI tools. If policy instead forbids those tools, that is an additional policy channel.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +6.0 |
| U.S. response to Chinese changes | +0.077 |
| **Total U.S. capability loss** | **+6.1** |
| China direct compute/access/security effect | +2.7 |
| China accumulated research effect | +0.27 |
| China response to U.S. changes | +0.46 |
| **Total Chinese capability loss** | **+3.4** |
| **U.S. loss minus Chinese loss** | **+2.7** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
us_research_input_loss_fraction=newly_affected_research_share*within_environment_productivity_loss*shared.security_rollout_fraction_year+migration_research_input_loss
risk_cut[remote,insider,other]=[remote_risk_cut,insider_risk_cut,other_risk_cut]*shared.security_rollout_fraction_year
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| newly affected research share | 0.3 / 0.7 / 1 | fraction of U.S. research-equivalent activity facing tighter environment | analyst prior | Some workloads already isolated; broad proposed requirement changes collaboration and access across many research activities. |
| within environment productivity loss | 0.03 / 0.15 / 0.35 | fraction of affected research output at mature deployment | analyst prior | No direct published measurement identified. Mode reflects material network/tool/collaboration friction, offset by local tooling and adaptation; high accommodates severe isolation. |
| migration research input loss | 0.001 / 0.01 / 0.05 | fraction of total U.S. annual research-equivalent input consumed by one-time migration | analyst prior | Separate transition burden; engineering build-out may overlap research. Not equal to facility construction duration. |
| remote risk cut | 0.3 / 0.8 / 0.97 | fraction of baseline remote compromise hazard prevented at mature implementation | analyst prior | Isolation sharply reduces many remote paths but does not guarantee complete prevention. |
| insider risk cut | 0.05 / 0.3 / 0.7 | fraction of baseline insider compromise hazard prevented at mature implementation | analyst prior | Physical/exfiltration controls help, but network isolation is not personnel clearance. |
| other risk cut | 0.05 / 0.3 / 0.7 | fraction of other compromise hazard prevented at mature implementation | analyst prior | Physical security helps some paths while hardware/supply-chain vulnerabilities remain. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [Improving our alignment and security practices](../sources.md#china-anthropic_security_2026) — [original source](https://www.anthropic.com/news/improving-alignment-security-efforts).
- [SL5 Standard for AI Security](../sources.md#china-sl5_2026) — [original source](https://arxiv.org/abs/2605.08449).
- [Securing AI Model Weights: Preventing Theft and Misuse of Frontier Models](../sources.md#china-rand_weights_2024) — [original source](https://www.rand.org/pubs/research_reports/RRA2849-1.html).
- [CAISI’s Assessment of Z.ai’s GLM-5.3 Cyber Capabilities](../sources.md#china-nist_caisi_2026) — [original source](https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | +2.7 |
| No marginal U.S.-to-China research/teacher reliance | +3.2 |
| Half the marginal U.S.-to-China reliance | +3.0 |
| Twice the marginal U.S.-to-China reliance | +2.2 |
| No incremental AI-assisted research feedback | +2.3 |
| No China-to-U.S. research response | +2.7 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | +3.6 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | +2.5 |
| 12 months | +2.7 |
| 36 months | +5.2 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): within environment productivity loss (r=+0.48), newly affected research share (r=+0.27), algorithmic growth (r=+0.27).

Monte Carlo standard error of the numerical mean: 0.0393 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
