# Background checks for lab staff

**Best estimate: -0.030 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -0.20 to +0.076 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

Everyone who works at a frontier lab passes a standard background check, like the checks many banks and hospitals run. Nobody needs a security clearance.

Standard checks for all new staff and catch-up checks for previously unscreened incumbents, without citizenship exclusion, versus existing private screening.

## Research and calculation

This is ordinary background screening with work continuing where possible. It does not assume citizenship exclusion. Both the affected insider risk and productive days blocked are marginal to checks already conducted.

No estimate of ordinary-screening exclusion is imported from ethnic composition. Catch-up checks can run during ongoing employment. Mode produces a very small U.S. labor-input effect; security effect remains prior-driven.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +0.051 |
| U.S. response to Chinese changes | +0.002 |
| **Total U.S. capability loss** | **+0.053** |
| China direct compute/access/security effect | +0.073 |
| China accumulated research effect | +0.007 |
| China response to U.S. changes | +0.004 |
| **Total Chinese capability loss** | **+0.083** |
| **U.S. loss minus Chinese loss** | **-0.030** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
us_research_input_loss_fraction=annual_hires_relative_to_staff*newly_screened_share*screening_calendar_days*screening_blocks_start_fraction/365+newly_screened_incumbent_share*incumbent_productive_days_lost/365
risk_cut[insider]=insider_risk_cut_in_newly_screened_exposures*newly_screened_risk_weighted_share*shared.security_rollout_fraction_year; other cuts=0
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| annual hires relative to staff | 0.15 / 0.3 / 0.6 | hires per current researcher-equivalent staff per year | analyst prior | Fast-growing labs with turnover; not an observed industry aggregate. |
| newly screened share | 0.05 / 0.2 / 0.5 | fraction of incoming staff not already equivalently screened | analyst prior | Most established labs likely already screen; precise baseline unreported. |
| screening calendar days | 2 / 6 / 21 | calendar days | calibrated | Mode converts 3–5 business days to about 6 calendar days; broad upper for overseas/manual checks. Distribution is ours. |
| screening blocks start fraction | 0 / 0.15 / 0.6 | fraction of turnaround that delays otherwise productive work | analyst prior | Notice periods and provisioning absorb most checks. |
| newly screened incumbent share | 0 / 0.1 / 0.35 | fraction of current staff receiving new check | analyst prior | Existing employees often screened; unknown coverage. |
| incumbent productive days lost | 0 / 0.2 / 2 | staff-days per newly checked incumbent | analyst prior | Form filling and exceptional access interruption rather than whole check duration. |
| insider risk cut in newly screened exposures | 0 / 0.1 / 0.3 | fraction of insider hazard prevented | analyst prior | Ordinary checks can detect some histories, not sophisticated clean-record infiltrators. |
| newly screened risk weighted share | 0.05 / 0.25 / 0.6 | fraction of insider hazard exposed to genuinely new screening | analyst prior | May exceed staff share if unscreened roles disproportionately risky; prior not a measured relationship. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [Securing AI Model Weights: Preventing Theft and Misuse of Frontier Models](../sources.md#china-rand_weights_2024) — [original source](https://www.rand.org/pubs/research_reports/RRA2849-1.html).
- [Checkr's background check process](../sources.md#china-checkr_turnaround) — [original source](https://help.checkr.com/helpcenter/s/article/216102167-Checkr-s-background-check-process).
- [CAISI’s Assessment of Z.ai’s GLM-5.3 Cyber Capabilities](../sources.md#china-nist_caisi_2026) — [original source](https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities).
- [Improving our alignment and security practices](../sources.md#china-anthropic_security_2026) — [original source](https://www.anthropic.com/news/improving-alignment-security-efforts).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | -0.030 |
| No marginal U.S.-to-China research/teacher reliance | -0.026 |
| Half the marginal U.S.-to-China reliance | -0.028 |
| Twice the marginal U.S.-to-China reliance | -0.034 |
| No incremental AI-assisted research feedback | -0.029 |
| No China-to-U.S. research response | -0.032 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | -0.037 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | +0.008 |
| 12 months | -0.030 |
| 36 months | -0.059 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): insider risk cut in newly screened exposures (r=-0.40), newly screened risk weighted share (r=-0.32), screening blocks start fraction (r=+0.18).

Monte Carlo standard error of the numerical mean: 0.0010 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
