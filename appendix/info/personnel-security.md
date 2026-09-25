# Clearance-level vetting for lab staff

**Best estimate: +1.44 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -0.55 to +4.3 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

Anyone with access to a lab's model weights or key research must pass vetting close to a government security clearance, with regular re-checks. This is the strict version; background checks alone are a separate item.

Near-clearance checks for sensitive weight/research-access roles, without automatic citizenship exclusion; transition allows most incumbents restricted/interim access. Versus voluntary baseline. Blanket citizenship rules are a separate stress case.

## Research and calculation

Sensitive roles, interim access, hiring flow, productive work retained during waiting and departures are modeled separately. A portion of lost U.S. capacity may join Chinese research. Government clearance processing time is a context anchor, not an observed private-lab delay.

Use role-specific exposure and retained productivity, not China-origin researcher fraction. Use clearance turnover, waiting and departure terms jointly; alternative extreme citizenship-exclusion policy should not silently change the base definition.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | 0.000 |
| U.S. accumulated research effect | +2.2 |
| U.S. response to Chinese changes | +0.017 |
| **Total U.S. capability loss** | **+2.2** |
| China direct compute/access/security effect | +0.73 |
| China accumulated research effect | -0.12 |
| China response to U.S. changes | +0.17 |
| **Total Chinese capability loss** | **+0.78** |
| **U.S. loss minus Chinese loss** | **+1.44** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
affected=sensitive_research_role_share*(1-already_equivalently_vetted_share); w=min(clearance_process_days,365)/365
new_hire_wait_loss=affected*annual_hires_relative_to_staff*new_hire_productivity_blocked_fraction*(w-w*w/2); integrates uniform arrival over first year
incumbent_wait_loss=affected*incumbent_blocked_share*incumbent_productivity_blocked_fraction*w
departing_capacity=affected*covered_staff_departure_or_foregone_hire_fraction*departure_year_exposure_fraction
us_research_input_loss_fraction=min(0.95,new_hire_wait_loss+incumbent_wait_loss+departing_capacity*lost_capacity_unreplaced_fraction)
cn_research_input_gain_fraction=departing_capacity*china_destination_share*us_to_cn_research_capacity_ratio*china_first_year_transfer_productivity
risk_cut[insider]=insider_risk_cut*shared.security_rollout_fraction_year; other cuts=0
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| sensitive research role share | 0.1 / 0.3 / 0.6 | fraction of researcher-equivalent staff subject to high vetting | analyst prior | Not everyone requires direct sensitive access; broad site includes key research as well as weights. |
| already equivalently vetted share | 0 / 0.05 / 0.2 | fraction of covered staff | analyst prior | Private background checks rarely equal clearance-style investigation. |
| clearance process days | 60 / 160 / 300 | calendar days | calibrated | Mode lower than official 206-day analogue because near-clearance private scheme can omit government adjudication; wide high reflects complex cases. Not lab data. |
| annual hires relative to staff | 0.15 / 0.3 / 0.6 | hires per current researcher-equivalent staff per year | analyst prior | Common hiring flow; correlate with light-vetting draw. |
| new hire productivity blocked fraction | 0.1 / 0.4 / 0.9 | fraction of new hire contribution unavailable while awaiting clearance | analyst prior | Interim access and nonsensitive tasks preserve output; some sensitive roles cannot contribute fully. |
| incumbent blocked share | 0 / 0.15 / 0.5 | fraction of sensitive incumbents losing some productivity during review | analyst prior | Most retain provisional access; no transition text specified, so explicit policy-design prior. |
| incumbent productivity blocked fraction | 0.1 / 0.35 / 0.8 | fraction of affected incumbents’ output lost during review | analyst prior | Measures unavailable tasks, not full headcount. |
| covered staff departure or foregone hire fraction | 0 / 0.04 / 0.15 | fraction of covered staff equivalents lost over year | analyst prior | Central behavioral response is smaller than severe geopolitical-isolation analogues; could be much higher with blanket eligibility exclusions. |
| lost capacity unreplaced fraction | 0.2 / 0.6 / 1 | fraction of departure-related capacity loss not replaced by another worker | analyst prior | Compensation/recruiting and internal substitutes offset some loss. |
| departure year exposure fraction | 0.25 / 0.5 / 0.9 | average fraction of first year departure loss operates | analyst prior | Departures distributed over year rather than all at inception. |
| china destination share | 0.05 / 0.25 / 0.6 | share of lost personnel capacity joining Chinese frontier research | analyst prior | Many move to third countries/other sectors; avoid treating all U.S. losses as China gains. |
| U.S. to China research capacity ratio | 0.7 / 1.5 / 3 | ratio of effective U.S. to Chinese frontier research capacity | analyst prior | Converts transferred worker equivalents into Chinese share; not an observed talent-headcount ratio. |
| china first year transfer productivity | 0.2 / 0.6 / 1 | fraction of departing workers’ former output realized in Chinese teams | analyst prior | Onboarding, noncompetes and changed compute/tools limit immediate contribution. |
| insider risk cut | 0.1 / 0.4 / 0.7 | fraction of baseline insider compromise hazard prevented at mature implementation | analyst prior | Deep vetting addresses additional insider threats beyond ordinary checks but cannot eliminate coercion or clean-record infiltrators. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [Personnel Vetting: Leadership Attention Needed to Prioritize System Development and Achieve Reforms, GAO-26-108838](../sources.md#china-gao_vetting_2026) — [original source](https://files.gao.gov/reports/GAO-26-108838/index.html).
- [Building a Wall Around Science: The Effect of U.S.-China Tensions on International Scientific Research](../sources.md#china-flynn_2024) — [original source](https://appam.confex.com/appam/2024/mediafile/ExtendedAbstract/Paper51756/Building_a_Wall.pdf).
- [Securing AI Model Weights: Preventing Theft and Misuse of Frontier Models](../sources.md#china-rand_weights_2024) — [original source](https://www.rand.org/pubs/research_reports/RRA2849-1.html).
- [CAISI’s Assessment of Z.ai’s GLM-5.3 Cyber Capabilities](../sources.md#china-nist_caisi_2026) — [original source](https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities).
- [Improving our alignment and security practices](../sources.md#china-anthropic_security_2026) — [original source](https://www.anthropic.com/news/improving-alignment-security-efforts).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | +1.44 |
| No marginal U.S.-to-China research/teacher reliance | +1.62 |
| Half the marginal U.S.-to-China reliance | +1.53 |
| Twice the marginal U.S.-to-China reliance | +1.26 |
| No incremental AI-assisted research feedback | +1.25 |
| No China-to-U.S. research response | +1.43 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | +1.86 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | +1.09 |
| 12 months | +1.44 |
| 36 months | +2.8 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): sensitive research role share (r=+0.43), clearance process days (r=+0.26), algorithmic growth (r=+0.24).

Monte Carlo standard error of the numerical mean: 0.0169 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
