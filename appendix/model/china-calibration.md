# Quantitative calibration: China access, diffusion and security

As of 25 September 2026. These are usable best-estimate inputs, not a claim that the causal effects are measured. The shared root model must turn them into the single headline day price for each policy. The core quantities below precede that conversion; no desired day result was inserted as an input. The locked estimand is the one-year (365.25-day) endpoint gap change on the fixed U.S. progress ruler. The callable module supplies endpoint compute and retained-compromise effects; average-year research inputs drive accumulated algorithmic innovation.

## Point choices and counterfactuals

| Policy | Mode-input resource/hazard implications (average-year resource illustration) |
|---|---|
| Advanced chip export controls | extra_china_average_compute_without_controls_million_h100e: 0.51656; cn_compute_loss_fraction: 0.088136; us_compute_gain_fraction: 0.006528; us_research_input_loss_fraction: 0.001 |
| Know-your-customer rules for compute providers | cn_compute_loss_fraction: 0.00525; us_compute_loss_fraction: 5.4795e-05 |
| Anti-distillation controls | cn_algorithmic_knowledge_flow_loss_fraction: 0.018; us_research_input_loss_fraction: 0.00074658 |
| Model-weight security standard | us_research_input_loss_fraction: 0.00099315; annual_useful_compromise_probability_reduction: 0.0053879; conditional_capability_gap_recovered_fraction: 0.6; compromise_absorption_days: 21 |
| Background checks for lab staff | us_research_input_loss_fraction: 0.00020274; annual_useful_compromise_probability_reduction: 0.00050355; conditional_capability_gap_recovered_fraction: 0.6; compromise_absorption_days: 21 |
| Clearance-level vetting for lab staff | us_research_input_loss_fraction: 0.021685; cn_research_input_gain_fraction: 0.0012825; annual_useful_compromise_probability_reduction: 0.00809; conditional_capability_gap_recovered_fraction: 0.6; compromise_absorption_days: 21 |
| Isolated secure development environment | us_research_input_loss_fraction: 0.08875; annual_useful_compromise_probability_reduction: 0.033758; conditional_capability_gap_recovered_fraction: 0.6; compromise_absorption_days: 21 |

These mode-input results are not posterior means. Broad skewed priors can shift the final expected price substantially; compute the expectation in the root engine and disclose the difference. For probabilities and fractions, multiply by 100 for percentages.

## Evidence and judgment

Numerical anchors come from primary research/operational reports: 2026 chip-production forecasts, observed teacher–student benchmark differences, government clearance timings, and vendor screening turnaround. None directly measures the marginal national effect. Theft probabilities, blocked-access shares, substitution rates, labor exposure and frontier relevance are explicitly analyst priors. Every distribution and rationale is in the accompanying JSON.

## Advanced chip export controls

**Counterfactual.** Maintain the frozen site’s advanced-accelerator and manufacturing-input restrictions for 12 months versus relaxing those covered restrictions at the start; current stock, voluntary practices, unrelated sanctions, and non-U.S. export decisions remain. China purchases and deployments ramp, not instant parity.

Price present restrictions relative to specified relaxation, not versus a historically never-restricted China. Nominal H100e is an imperfect common unit. The largest uncertainty is incremental purchases and frontier relevance, not the measured chip-generation gap.

| Input | Low / mode / high | Units | Evidence status | Rationale |
|---|---:|---|---|---|
| nvidia_annual_output_h100e | 18 / 23 / 30 | million rated H100e/year | calibrated | Mode equals published 2026 forecast; interval is our predictive uncertainty, not the paper’s confidence interval. Hold 2026 output pace for this exercise. |
| incremental_china_purchase_share | 0.02 / 0.1 / 0.2 | fraction of Nvidia annual output additional to purchases allowed in baseline | analyst_prior | Net incremental access after relaxing covered controls. One-tenth mode reflects strong demand but U.S. contracted allocation and Chinese budgets; deliberately below unconstrained parity. Existing permitted purchases are not recounted. |
| deployment_lag_days | 30 / 90 / 180 | calendar days | analyst_prior | Ordering, delivery, power and commissioning prevent immediate use. Includes supplying HBM/equipment pathway lag. |
| usable_fraction_of_added_rated_compute | 0.4 / 0.7 / 0.95 | fraction | analyst_prior | Allows for provisioning, interconnect, utilization and imperfect substitution into relevant training/inference workloads. |
| extra_domestic_output_after_relaxation | 0 / 0.3 / 1.0 | million rated H100e delivered in first year | analyst_prior | Additional domestic chip output from newly available manufacturing inputs. Small first-year mode because fabs cannot be rebuilt instantly; final-chip imports are faster. |
| baseline_china_average_usable_compute | 1.5 / 3.0 / 5.5 | million H100e during next 12 months | calibrated | End-2025 owned stock near 1m plus 2026 output, illicit imports, rentals and further build-out; 3m is an analyst extrapolation, not a reported current stock. Broad upper accommodates substantial unobserved access. |
| endpoint_to_average_compute_ratio | 1.05 / 1.4 / 1.8 | ratio of end-year stock to average stock over first year | analyst_prior | Growing baseline stock; use baseline_average times this factor for endpoint compute changes. Share draw across U.S. and China as a simple trend scenario. |
| share_relevant_to_frontier_progress | 0.25 / 0.6 / 1 | fraction of country-level marginal compute increase available to frontier production | analyst_prior | Not all additional chips serve frontier research or change a binding constraint. Avoids treating all national compute as a frontier cluster. |
| redirected_share_to_us_under_controls | 0 / 0.5 / 0.9 | fraction of prevented China sales deployed by U.S. users instead | analyst_prior | Current supply allocation could redirect rather than destroy sales. This is a small positive U.S. resource effect of maintaining controls. |
| baseline_us_average_usable_compute | 20 / 35 / 60 | million H100e during next 12 months | analyst_prior | Rough 2026 installed/allocated stock extrapolation. Wider than ownership evidence; only scales redirection term. |
| supplier_innovation_loss_us | 0 / 0.001 / 0.01 | fraction of U.S. research-equivalent input over first year | analyst_prior | Revenue constraints may reduce upstream innovation, but near-term supply-constrained sales and long R&D lags make a small first-year mode appropriate. Not imported from market capitalization loss. |

**Formulas**

- `AUTHORITATIVE PATH: solve k/(1-exp(-k))=endpoint_to_average_compute_ratio; C0=baseline_china_average_usable_compute*k/expm1(k)>0; Cbase(t)=C0*exp(k*t), with t in years`
- `delivery_factor(t)=expm1(k*max(t-deployment_lag_days/365.25,0))/expm1(k); extra_china_compute=(nvidia_annual_output_h100e*incremental_china_purchase_share+extra_domestic_output_after_relaxation)*usable_fraction_of_added_rated_compute*delivery_factor`
- `direct_cn_logcompute(t)=-share_relevant_to_frontier_progress*log1p(extra_china_compute/Cbase(t)); cn_compute_ratio=exp(direct_cn_logcompute)`
- `direct_us_logcompute(t)=log1p(redirected_share_to_us_under_controls*nvidia_annual_output_h100e*incremental_china_purchase_share*usable_fraction_of_added_rated_compute*delivery_factor/Ubase(t)); us_compute_ratio=exp(direct_us_logcompute)`
- `Compute ratios enter both the direct frontier training channel and the root research-compute production function, where the latter contributes only additional algorithmic progress.`
- `us_research_input_loss_fraction = supplier_innovation_loss_us`

## Know-your-customer rules for compute providers

**Counterfactual.** Additional identity, recordkeeping and intent checks above the covered scale versus existing cloud screening. Primary case includes enforcement of already-applicable restrictions when new identification reveals ineligible access; identity-only sensitivity sets denial_after_detection=0.

Reporting-only produces zero China resource loss. Export controls and KYC use a common covered-compute stock; combine denials as surviving access, never add the same blocked GPU-hours twice.

| Input | Low / mode / high | Units | Evidence status | Rationale |
|---|---:|---|---|---|
| cn_covered_cloud_compute_share | 0.01 / 0.1 / 0.3 | fraction of China-relevant frontier compute rented through newly affected providers/resellers | analyst_prior | Unobserved; modest mode because domestic compute is substantial, upper allows material offshore frontier use. |
| incremental_detection | 0.05 / 0.35 / 0.7 | fraction of otherwise hidden ineligible compute access newly identified | analyst_prior | Mandate improves on current screening; high-volume use is observable but identity evasion persists. |
| denial_after_detection | 0 / 0.5 / 0.9 | probability that newly identified covered use is actually restricted | analyst_prior | Explicit action assumption. KYC itself creates no prohibition. Half-mode includes already-ineligible customers; not all identified foreign users are forbidden. |
| replacement_share | 0.25 / 0.6 / 0.95 | fraction of denied relevant compute replaced elsewhere within horizon | analyst_prior | Alternative providers, domestic capacity and evasion offset denials; complete substitution retained near upper bound. |
| rollout_fraction_year | 0.25 / 0.75 / 1 | fraction of first-year exposure after implementation | analyst_prior | Coverage phases in rather than full-year instantaneous denial. |
| us_new_contract_exposure | 0.05 / 0.2 / 0.5 | fraction of U.S. compute provisioning newly checked | analyst_prior | Large labs are already identified; burden mainly extensions/new contracts. |
| check_elapsed_days | 0.1 / 1 / 7 | calendar days per exposed provisioning | analyst_prior | Incremental documentation can complete quickly for known major customers, but tail accommodates exceptions. |
| blocking_fraction | 0 / 0.1 / 0.5 | fraction of elapsed check that blocks usable compute | analyst_prior | Most work asynchronous with provisioning. |

**Formulas**

- `cn_compute_loss_fraction=cn_covered_cloud_compute_share*incremental_detection*denial_after_detection*(1-replacement_share)*rollout_fraction_year`
- `us_compute_loss_fraction=us_new_contract_exposure*check_elapsed_days*blocking_fraction/365`

## Anti-distillation controls

**Counterfactual.** Mandated coordinated API vetting, restrictions on full traces and detection versus current voluntary enforcement and existing product choices; does not ban all open models or independent Chinese/self-distillation.

Multiply the China effect by the shared algorithmic-knowledge contribution to progress in the root engine, not full national progress. If foreign teacher dependence is zero, benefit is zero. Experimental score uplifts establish potential value but do not set the dependence prior mechanically.

| Input | Low / mode / high | Units | Evidence status | Rationale |
|---|---:|---|---|---|
| additional_blocked_teacher_access | 0.05 / 0.3 / 0.65 | fraction of remaining valuable U.S. teacher access prevented by mandate | analyst_prior | Incremental to existing restrictions; prior deliberately below total attack detection or account closure rate. |
| rollout_fraction_year | 0.25 / 0.75 / 1 | fraction of first year mature coordination operates | analyst_prior | Engineering, shared telemetry and enforcement require time. |
| us_research_staff_reassigned_share | 0 / 0.002 / 0.01 | fraction of U.S. frontier research-equivalent staff at full rollout | analyst_prior | Most costs fall on trust/safety/product staff; count only research-equivalent diversion. |
| implementation_work_days | 7 / 45 / 120 | calendar work duration during first year | analyst_prior | Temporary build-out; not the eventual national delay. |
| us_research_product_friction | 0 / 0.0005 / 0.005 | fraction of research-equivalent output lost across year from legitimate access limits | analyst_prior | Small central effect because laboratories retain access to their own internal models. Public developer welfare loss is outside frontier lead estimand. |

**Formulas**

- `cn_algorithmic_knowledge_flow_loss_fraction = shared.frontier_teacher_channel_share*additional_blocked_teacher_access*(1-shared.teacher_substitution_recovery)*rollout_fraction_year`
- `us_research_input_loss_fraction=us_research_staff_reassigned_share*implementation_work_days/365+us_research_product_friction`

## Model-weight security standard

**Counterfactual.** An SL3-like floor for unreleased frontier weights versus current voluntary security practices, with already compliant labs credited zero incremental burden/risk change.

Counts incremental technical hardening, not every voluntary security dollar. Staff days are divided by relevant total research capacity and year before root production-function conversion.

| Input | Low / mode / high | Units | Evidence status | Rationale |
|---|---:|---|---|---|
| newly_changed_risk_weighted_share | 0.05 / 0.25 / 0.6 | share of baseline compromise hazard located in exposures materially changed by mandate | analyst_prior | Leading labs already strengthen defenses voluntarily; uncovered exposures may be riskier than their headcount share. |
| remote_risk_cut_in_changed_exposures | 0.1 / 0.5 / 0.8 | fraction of remote compromise hazard prevented | analyst_prior | Access hardening, monitoring and outbound restrictions address remote exfiltration but are not foolproof. |
| insider_risk_cut_in_changed_exposures | 0.05 / 0.25 / 0.6 | fraction of insider compromise hazard prevented | analyst_prior | Access minimization and exfiltration controls reduce insider success; excludes clearance vetting. |
| other_risk_cut_in_changed_exposures | 0 / 0.1 / 0.4 | fraction of other compromise hazard prevented | analyst_prior | Limited effect on sophisticated supply-chain/physical paths. |
| us_research_staff_reassigned_share | 0.0002 / 0.003 / 0.015 | fraction of research-equivalent U.S. staff | analyst_prior | Marginal research burden only, below whole-company voluntary hardening campaign. |
| implementation_work_days | 14 / 60 / 180 | calendar duration | analyst_prior | One-time implementation counted only in first-year workload. |
| ongoing_research_friction | 0 / 0.0005 / 0.004 | fraction of U.S. effective research input across year | analyst_prior | SL3 floor should preserve ordinary tooling; friction remains nonzero where access changes. |

**Formulas**

- `risk_cut[remote,insider,other]=newly_changed_risk_weighted_share*[remote_risk_cut_in_changed_exposures,insider_risk_cut_in_changed_exposures,other_risk_cut_in_changed_exposures]*shared.security_rollout_fraction_year`
- `us_research_input_loss_fraction=us_research_staff_reassigned_share*implementation_work_days/365+ongoing_research_friction`
- `security_benefit = shared competing-hazard module; output probability reduction and conditional gap-fraction recovery, with root time conversion`

## Background checks for lab staff

**Counterfactual.** Standard checks for all new staff and catch-up checks for previously unscreened incumbents, without citizenship exclusion, versus existing private screening.

No estimate of ordinary-screening exclusion is imported from ethnic composition. Catch-up checks can run during ongoing employment. Mode produces a very small U.S. labor-input effect; security effect remains prior-driven.

| Input | Low / mode / high | Units | Evidence status | Rationale |
|---|---:|---|---|---|
| annual_hires_relative_to_staff | 0.15 / 0.3 / 0.6 | hires per current researcher-equivalent staff per year | analyst_prior | Fast-growing labs with turnover; not an observed industry aggregate. |
| newly_screened_share | 0.05 / 0.2 / 0.5 | fraction of incoming staff not already equivalently screened | analyst_prior | Most established labs likely already screen; precise baseline unreported. |
| screening_calendar_days | 2 / 6 / 21 | calendar days | calibrated | Mode converts 3–5 business days to about 6 calendar days; broad upper for overseas/manual checks. Distribution is ours. |
| screening_blocks_start_fraction | 0 / 0.15 / 0.6 | fraction of turnaround that delays otherwise productive work | analyst_prior | Notice periods and provisioning absorb most checks. |
| newly_screened_incumbent_share | 0 / 0.1 / 0.35 | fraction of current staff receiving new check | analyst_prior | Existing employees often screened; unknown coverage. |
| incumbent_productive_days_lost | 0 / 0.2 / 2 | staff-days per newly checked incumbent | analyst_prior | Form filling and exceptional access interruption rather than whole check duration. |
| insider_risk_cut_in_newly_screened_exposures | 0 / 0.1 / 0.3 | fraction of insider hazard prevented | analyst_prior | Ordinary checks can detect some histories, not sophisticated clean-record infiltrators. |
| newly_screened_risk_weighted_share | 0.05 / 0.25 / 0.6 | fraction of insider hazard exposed to genuinely new screening | analyst_prior | May exceed staff share if unscreened roles disproportionately risky; prior not a measured relationship. |

**Formulas**

- `us_research_input_loss_fraction=annual_hires_relative_to_staff*newly_screened_share*screening_calendar_days*screening_blocks_start_fraction/365+newly_screened_incumbent_share*incumbent_productive_days_lost/365`
- `risk_cut[insider]=insider_risk_cut_in_newly_screened_exposures*newly_screened_risk_weighted_share*shared.security_rollout_fraction_year; other cuts=0`

## Clearance-level vetting for lab staff

**Counterfactual.** Near-clearance checks for sensitive weight/research-access roles, without automatic citizenship exclusion; transition allows most incumbents restricted/interim access. Versus voluntary baseline. Blanket citizenship rules are a separate stress case.

Use role-specific exposure and retained productivity, not China-origin researcher fraction. Use clearance turnover, waiting and departure terms jointly; alternative extreme citizenship-exclusion policy should not silently change the base definition.

| Input | Low / mode / high | Units | Evidence status | Rationale |
|---|---:|---|---|---|
| sensitive_research_role_share | 0.1 / 0.3 / 0.6 | fraction of researcher-equivalent staff subject to high vetting | analyst_prior | Not everyone requires direct sensitive access; broad site includes key research as well as weights. |
| already_equivalently_vetted_share | 0 / 0.05 / 0.2 | fraction of covered staff | analyst_prior | Private background checks rarely equal clearance-style investigation. |
| clearance_process_days | 60 / 160 / 300 | calendar days | calibrated | Mode lower than official 206-day analogue because near-clearance private scheme can omit government adjudication; wide high reflects complex cases. Not lab data. |
| annual_hires_relative_to_staff | 0.15 / 0.3 / 0.6 | hires per current researcher-equivalent staff per year | analyst_prior | Common hiring flow; correlate with light-vetting draw. |
| new_hire_productivity_blocked_fraction | 0.1 / 0.4 / 0.9 | fraction of new hire contribution unavailable while awaiting clearance | analyst_prior | Interim access and nonsensitive tasks preserve output; some sensitive roles cannot contribute fully. |
| incumbent_blocked_share | 0 / 0.15 / 0.5 | fraction of sensitive incumbents losing some productivity during review | analyst_prior | Most retain provisional access; no transition text specified, so explicit policy-design prior. |
| incumbent_productivity_blocked_fraction | 0.1 / 0.35 / 0.8 | fraction of affected incumbents’ output lost during review | analyst_prior | Measures unavailable tasks, not full headcount. |
| covered_staff_departure_or_foregone_hire_fraction | 0 / 0.04 / 0.15 | fraction of covered staff equivalents lost over year | analyst_prior | Central behavioral response is smaller than severe geopolitical-isolation analogues; could be much higher with blanket eligibility exclusions. |
| lost_capacity_unreplaced_fraction | 0.2 / 0.6 / 1 | fraction of departure-related capacity loss not replaced by another worker | analyst_prior | Compensation/recruiting and internal substitutes offset some loss. |
| departure_year_exposure_fraction | 0.25 / 0.5 / 0.9 | average fraction of first year departure loss operates | analyst_prior | Departures distributed over year rather than all at inception. |
| china_destination_share | 0.05 / 0.25 / 0.6 | share of lost personnel capacity joining Chinese frontier research | analyst_prior | Many move to third countries/other sectors; avoid treating all U.S. losses as China gains. |
| us_to_cn_research_capacity_ratio | 0.7 / 1.5 / 3 | ratio of effective U.S. to Chinese frontier research capacity | analyst_prior | Converts transferred worker equivalents into Chinese share; not an observed talent-headcount ratio. |
| china_first_year_transfer_productivity | 0.2 / 0.6 / 1 | fraction of departing workers’ former output realized in Chinese teams | analyst_prior | Onboarding, noncompetes and changed compute/tools limit immediate contribution. |
| insider_risk_cut | 0.1 / 0.4 / 0.7 | fraction of baseline insider compromise hazard prevented at mature implementation | analyst_prior | Deep vetting addresses additional insider threats beyond ordinary checks but cannot eliminate coercion or clean-record infiltrators. |

**Formulas**

- `affected=sensitive_research_role_share*(1-already_equivalently_vetted_share); w=min(clearance_process_days,365)/365`
- `new_hire_wait_loss=affected*annual_hires_relative_to_staff*new_hire_productivity_blocked_fraction*(w-w*w/2); integrates uniform arrival over first year`
- `incumbent_wait_loss=affected*incumbent_blocked_share*incumbent_productivity_blocked_fraction*w`
- `departing_capacity=affected*covered_staff_departure_or_foregone_hire_fraction*departure_year_exposure_fraction`
- `us_research_input_loss_fraction=min(0.95,new_hire_wait_loss+incumbent_wait_loss+departing_capacity*lost_capacity_unreplaced_fraction)`
- `cn_research_input_gain_fraction=departing_capacity*china_destination_share*us_to_cn_research_capacity_ratio*china_first_year_transfer_productivity`
- `risk_cut[insider]=insider_risk_cut*shared.security_rollout_fraction_year; other cuts=0`

## Isolated secure development environment

**Counterfactual.** Frontier research moved into isolated networks and physical access controls; existing voluntary cluster isolation remains baseline. First-year rollout includes modular migration, not assumed immediate construction of entirely new facilities.

Treat as reduced effective research inputs, not uniform national progress delay. The secure environment remains compatible with internal AI tools. If policy instead forbids those tools, that is an additional policy channel.

| Input | Low / mode / high | Units | Evidence status | Rationale |
|---|---:|---|---|---|
| newly_affected_research_share | 0.3 / 0.7 / 1 | fraction of U.S. research-equivalent activity facing tighter environment | analyst_prior | Some workloads already isolated; broad proposed requirement changes collaboration and access across many research activities. |
| within_environment_productivity_loss | 0.03 / 0.15 / 0.35 | fraction of affected research output at mature deployment | analyst_prior | No direct published measurement identified. Mode reflects material network/tool/collaboration friction, offset by local tooling and adaptation; high accommodates severe isolation. |
| migration_research_input_loss | 0.001 / 0.01 / 0.05 | fraction of total U.S. annual research-equivalent input consumed by one-time migration | analyst_prior | Separate transition burden; engineering build-out may overlap research. Not equal to facility construction duration. |
| remote_risk_cut | 0.3 / 0.8 / 0.97 | fraction of baseline remote compromise hazard prevented at mature implementation | analyst_prior | Isolation sharply reduces many remote paths but does not guarantee complete prevention. |
| insider_risk_cut | 0.05 / 0.3 / 0.7 | fraction of baseline insider compromise hazard prevented at mature implementation | analyst_prior | Physical/exfiltration controls help, but network isolation is not personnel clearance. |
| other_risk_cut | 0.05 / 0.3 / 0.7 | fraction of other compromise hazard prevented at mature implementation | analyst_prior | Physical security helps some paths while hardware/supply-chain vulnerabilities remain. |

**Formulas**

- `us_research_input_loss_fraction=newly_affected_research_share*within_environment_productivity_loss*shared.security_rollout_fraction_year+migration_research_input_loss`
- `risk_cut[remote,insider,other]=[remote_risk_cut,insider_risk_cut,other_risk_cut]*shared.security_rollout_fraction_year`

## Shared security and diffusion priors

### Security

| Input | Low / mode / high | Units |
|---|---:|---|
| relevant_asset_gap_days | 120 / 180 / 300 | days on root fixed U.S. capability ruler |
| annual_useful_frontier_compromise_probability | 0.01 / 0.08 / 0.3 | probability across covered U.S. frontier assets in one year |
| insider_hazard_share | 0.15 / 0.35 / 0.6 | fraction of baseline successful-compromise hazard |
| other_nonremote_hazard_share | 0.05 / 0.15 / 0.35 | fraction of hazard remaining after insiders |
| compromise_gap_fraction_recovered | 0.1 / 0.6 / 0.95 | fraction of current relevant U.S.–China capability gap recovered conditional on usable theft |
| compromise_absorption_days | 3 / 21 / 90 | calendar days from compromise to useful deployment |
| compromise_advantage_half_life_days | 30 / 120 / 365 | calendar days |
| security_rollout_fraction_year | 0.25 / 0.75 / 1 | share of first year during which mature controls operate |

### Diffusion

| Input | Low / mode / high | Units |
|---|---:|---|
| public_research_substitution_recovery | 0.1 / 0.4 / 0.85 | fraction of unavailable U.S. research value recovered independently or elsewhere |
| teacher_substitution_recovery | 0.2 / 0.6 / 0.95 | fraction of unavailable frontier-teacher value recovered from other teachers/data/self-training |
| public_research_channel_share | 0.05 / 0.2 / 0.4 | fraction of annual Chinese algorithmic knowledge additions before substitution |
| frontier_teacher_channel_share | 0.03 / 0.2 / 0.45 | fraction of annual Chinese algorithmic knowledge additions before substitution |
| released_weights_channel_share | 0.01 / 0.08 / 0.2 | fraction of annual Chinese algorithmic knowledge additions before substitution |
| researcher_transfer_channel_share | 0.0 / 0.05 / 0.15 | fraction of annual Chinese algorithmic knowledge additions before substitution |
| public_research_absorption_days | 7 / 45 / 180 | calendar days |
| teacher_data_absorption_days | 7 / 30 / 120 | calendar days |
| released_weights_absorption_days | 1 / 7 / 45 | calendar days |

Security hazard reductions are route-specific and act on residual hazards. The annual probability is shared across policies, not reintroduced once per item. Light and clearance vetting are nested. Weight hardening and secure-environment technical controls overlap. Do not add their standalone credits.

The researcher-origin share is deliberately absent from the estimator: it does not establish exposure, eligibility, threat, or marginal productivity. Near-clearance processing uses a government analogue with a downward-adjusted mode; actual government clearance and blanket citizenship exclusion require separate policy definitions.

For export controls the 2026 chip mix is frozen, and purchases ramp after relaxation. The authoritative vector path grows positive baseline stock exponentially, deriving its rate from the endpoint/average stock ratio; deliveries grow at that same rate and preserve the calibrated first-year purchase amount. The table above is a simpler average-year illustration, not the authoritative endpoint path. The calculation includes the possibility that maintaining controls redirects chips toward U.S. users. Export restrictions and cloud KYC draw on the same accessible-compute stock, so an integrated portfolio must condition the second intervention on resources that remain.

For teacher controls, channel share × incremental blocking × unrecovered value gives algorithmic knowledge-flow loss. That flow is only one input to overall frontier progress. It cannot be deducted one-for-one from national calendar time. Self-distillation evidence supplies a real substitute, not proof that foreign teachers are irrelevant.

## Callable integration

`china_model.py` exposes the authoritative vector API `china_paths(n, seed, times, g_total, g_algo)`, where times are years and shared growth inputs are scalars or length-N arrays. It returns N×T arrays `direct_us_logcompute`, `direct_cn_logcompute`, `us_labor_ratio`, `cn_labor_ratio`, `us_compute_ratio`, and `cn_compute_ratio` for each policy, plus shared phi_A/phi_T. Labor ratios are research labor inputs, not aggregate research output. Compute ratios apply only to export/KYC physical-resource channels and equal one for security and teachers; direct log effects include those knowledge/security channels in the shared units. Root can map physical compute ratios through the research capital elasticity in addition to the direct training effect. The scalar `sample` and `evaluate_draw` APIs remain illustrative legacy diagnostics; use the vector API for final pricing.

The vector security default is upgraded to most-recent useful theft: integrate hazard × probability of no later useful theft × retained value, before/after the control onset. This caps expected retained uplift at one current-gap transfer and preserves monotonicity under a hazard reduction. Theft within the final absorption delay contributes zero by the endpoint; an explicit half-life depreciates earlier advantage. `direct_cn_logcompute` already includes this expected avoided value with a negative sign. Do not multiply again by theft risk, gap or duration. `security_first_event_diagnostic_log_uplift` is a diagnostic only: combining first-event selection and depreciation can otherwise give spurious long-horizon sign reversals. `security_paths` accepts shared priors and mature route cuts, while `combined_hazard_cuts` provides nested-control overlap accounting; run the hazard model once for a bundle.

Common marginal teacher reliance is `phi_T=(g_algo/g_total)*teacher_channel_share*(1-teacher_substitution_recovery)`. Public withholding uses `phi_T*(-g_total*release_delay_days/365.25)` as its diffusion target; anti-distillation uses `-g_total*phi_T*blocked_fraction*rollout_fraction`. The same sampled substitute recovery is used once. Zero teacher reliance makes both teacher-access effects zero. Research-knowledge reliance is `phi_A=(g_algo/g_total)*public_research_channel_share*(1-public_research_substitution_recovery)`.

## Source ledger

- **nist_caisi_2026** — [CAISI’s Assessment of Z.ai’s GLM-5.3 Cyber Capabilities](https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities) (2026-09-17). About four months behind the U.S. frontier on a composite cyber evaluation. Limit: Public and trusted-access models only; explicitly excludes unreleased internal models. General/private gap prior is an extrapolation, not this observation.
- **epoch_huawei_2026** — [Will Huawei catch up to Nvidia by 2030?](https://epoch.ai/publications/huaweis-roadmap-to-2031) (2026-09-04; updated 2026-09-24). 2026 forecast: Nvidia 23 million H100-equivalents; Huawei 0.88 million. Huawei chip-count forecast 1.5 million; Nvidia 5.9 million. Limit: Forecast and hardware-rated throughput, not deployed frontier compute or causal effect of removing controls.
- **epoch_owners_2026** — [Introducing the AI Chip Owners Explorer](https://epoch.ai/latest/introducing-the-ai-chip-owners-explorer) (2026-04-06). End-2025 Chinese ownership just over 5% of global rated compute. Google about 5 million H100e and 25% of world total, implying world about 20 million and China about 1 million H100e. Limit: Rounded derivation. Excludes smuggling and offshore rentals. Does not establish September 2026 stock.
- **epoch_malaysia_2026** — [Trade data is consistent with more than $3 billion of chips smuggled into China via Malaysia](https://epoch.ai/data-insights/malaysia-china-chip-smuggling) (2026-09-17). April 2024–June 2025: China records $3.8bn server imports against Malaysia $0.6bn exports. Rough compute equivalent 150,000 H100e; alternative chip mix can reduce this to 50,000. Limit: Consistent with diversion, not proof or an exhaustive smuggling estimate.
- **deepseek_r1_2025** — [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/html/2501.12948v1) (2025-01-22, v1). Table 6: Qwen-32B distilled versus RL-only: AIME 72.6 vs 47.0; GPQA 62.1 vs 55.0; LiveCodeBench 57.2 vs 40.2. Teacher-generated training set: 800,000 samples. Limit: Domestic DeepSeek teacher and small students, not foreign-model dependence. No equal-total-cost causal conversion to national progress.
- **busbridge_2025** — [Distillation Scaling Laws](https://proceedings.mlr.press/v267/busbridge25a.html) (2025-07-13 to 2025-07-19, ICML 2025).  Limit: Provides teacher/student scaling method, not a Chinese dependence fraction or intervention efficacy.
- **anthropic_distill_2026** — [Detecting and preventing distillation attacks](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks) (2026-02-23). Over 16 million exchanges through approximately 24,000 fraudulent accounts attributed to three labs. Limit: Detected use is not causal capability uplift; selective detection and interested provider.
- **rand_weights_2024** — [Securing AI Model Weights: Preventing Theft and Misuse of Frontier Models](https://www.rand.org/pubs/research_reports/RRA2849-1.html) (2024-05-30). 38 attack vectors and five security levels. Limit: No empirically identified annual frontier theft hazard or risk-reduction fraction.
- **anthropic_security_2026** — [Improving our alignment and security practices](https://www.anthropic.com/news/improving-alignment-security-efforts) (2026-09 (date as retrieved)). About 150 product engineers temporarily reassigned; researchers also rotated; most teams finished by early summer. A separate production RL-environment freeze lasted roughly one month. Limit: Voluntary baseline; whole-company security/reliability/privacy campaign, not the marginal mandate cost or whole-frontier slowdown.
- **gao_vetting_2026** — [Personnel Vetting: Leadership Attention Needed to Prioritize System Development and Achieve Reforms, GAO-26-108838](https://files.gao.gov/reports/GAO-26-108838/index.html) (2026-02). FY2025 Q2 fastest 90% of initial Top Secret cases averaged 206 days; goal 114 days. Limit: Government processing is an analogue for near-clearance vetting, not lab-specific delay. GAO also reports significant underlying timeliness-data reliability issues.
- **flynn_2024** — [Building a Wall Around Science: The Effect of U.S.-China Tensions on International Scientific Research](https://appam.confex.com/appam/2024/mediafile/ExtendedAbstract/Paper51756/Building_a_Wall.pdf) (2024 conference version; NBER June 2024 revised October 2024). Version inspected: ethnic-Chinese entrants 15% less likely to attend U.S. PhD; graduates 4% less likely to remain; U.S.-based researcher productivity 2–6% lower. Limit: Different population, treatment and horizon; later revisions differ. Context for priors, not a clearance-policy causal coefficient.
- **checkr_turnaround** — [Checkr's background check process](https://help.checkr.com/helpcenter/s/article/216102167-Checkr-s-background-check-process) (retrieved 2026-09-25). Typical check turnaround 3–5 business days. Limit: Commercial service claim; actual start-date delay can be zero due to overlap and existing checks.
- **sl5_2026** — [SL5 Standard for AI Security](https://arxiv.org/abs/2605.08449) (2026-05-08, v0.1). 45 pages, ten control families. Limit: Long-lead security design, no measured productivity penalty or proven theft elimination.
- **egan_heim_2023** — [Oversight for Frontier AI through a Know-Your-Customer Scheme for Compute Providers](https://arxiv.org/abs/2310.13625) (2023-10-20).  Limit: KYC enables oversight and enforcement; does not estimate denial rate or offshore Chinese frontier share.
- **crosignani_2025** — [Securing Technological Leadership? The Cost of Export Controls on Firms](https://www.newyorkfed.org/research/staff_reports/sr1096) (2024-04; revised 2025-02). Reports $130bn decline in affected U.S. suppliers’ market capitalization and weaker firm outcomes. Limit: Not a current AI-accelerator R&D or frontier-speed elasticity.
