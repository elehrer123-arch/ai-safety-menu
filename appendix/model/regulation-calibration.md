# Quantitative regulatory calibration

Best estimate = prior predictive mean from explicitly labeled inputs. Triangular bounds are scenario supports, not confidence bounds. p10/p90 here summarize parameter priors; full event uncertainty not sampled. Observed policy constants represented as degenerate triangular distributions.

This file supplies numerical intermediate effects for14 policies. Country dynamics must translate them to one headline lead-closure estimate. The estimates are built from task loads, schedule prerequisites, event probabilities and investment responses, not desired months.

Public process dataset: 8 distinct models, 6 release clusters; shared campaigns are explicitly tagged. Missing dates stay empty.

## First-year intermediate best estimates

|Policy|Displaced R&D workdays/year|R&D input loss (%)|Release lag days/model|Internal lag days/model or annual event|Effective training lag days/run|Investment input loss (%)|
|---|---:|---:|---:|---:|---:|---:|
|incident-reporting|2.52|0.0008|0.00|0.00|0.00|0.000|
|safety-framework|8.55|0.0026|1.05|0.23|0.00|0.000|
|transparency-report|16.02|0.0049|0.53|0.00|0.00|0.000|
|whistleblower|1.47|0.0004|0.00|0.12|0.00|0.000|
|shutdown|27.22|0.0083|2.22|0.37|0.00|0.000|
|third-party-audit|18.99|0.0058|2.85|0.62|0.00|0.000|
|internal-evals|95.75|0.0292|1.16|0.07|0.00|0.000|
|third-party-eval|46.45|0.0142|1.24|0.10|0.00|0.000|
|evaluator-window|43.63|0.0133|4.72|0.28|0.00|0.000|
|triggered-redteam|123.06|0.0375|2.26|0.94|0.00|0.000|
|safety-case-deploy|226.10|0.0690|35.10|3.51|0.00|0.000|
|safety-case-train|85.48|0.0261|0.00|0.00|22.28|0.000|
|training-notice-30|6.75|0.0021|0.00|0.00|2.42|0.000|
|strict-liability|43.31|0.0132|5.27|0.53|0.00|0.499|

Internal/release lag means are conditional expected shifts across a model cycle. Whistleblower, shutdown and annual-audit events are tagged in JSON as annual events and must not be multiplied by release count. Training lag already nets assumed progress during waiting; do not charge it a second time as a release gate. R&D input is a fraction of annual effective researcher labor; it needs a research-production elasticity before becoming capability progress. Investment input requires a separate capital/research-production elasticity.

## Data findings

- GPT-5: initial access July10, final checkpoint July25, reasoning traces July26, preliminary report August1 and release August7. Four-week access window; three-week evaluation workload. The existing menu conflates these.
- GPT-5.5: SecureBio testing April2–9, product release April23, API April24. Testing could end two weeks before launch, demonstrating overlap without proving policy would create no delay.
- Astra: three-day testing period and two-day high-throughput reasoning access are known; access-to-release runway and exact endpoints are unknown.
- Opus5.5:10business days of API capability testing; do not relabel as observed14calendar days.
- o1-preview/o1-mini and o3/o4-mini share campaigns and should not be treated as four independent experiments.

## Policy assumptions and formulas

### incident-reporting

Setup and incident-contingent reporting; no pre-release statutory gate. No invented filing delay charged to capability. Harm response itself belongs to the baseline unless induced by reporting. Direct report-labor estimate excludes uncertain beneficial learning.

|Input|Units|Low / mode / high|Status|Rationale|
|---|---|---|---|---|
|setup_and_annual_staff_days|person_workdays_per_lab_year|2 / 5 / 15|analyst_prior|Incremental setup/maintenance work beyond voluntary practice; explicit workload prior.|
|per_release_staff_days|person_workdays_per_model|0 / 0 / 0|analyst_prior|Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program.|
|research_counterfactual_fraction|fraction_of_compliance_labor|0.05 / 0.15 / 0.4|analyst_prior|Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers.|
|incidents_per_year|incidents_per_lab_year|0 / 1 / 4|analyst_prior|Reportable incidents requiring incremental reports; frequency prior, not empirical incident rate.|
|report_staff_days|person_workdays_per_incident|0.5 / 2 / 7|analyst_prior|Fact-gathering/legal write-up beyond existing incident response.|

Formulas:
- `annual_displaced_rd_workdays = (setup_and_annual_staff_days+incidents_per_year*report_staff_days)*research_counterfactual_fraction`
- `annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)`
- `release_lag_excluding_training_days = 0`
- `internal_use_lag_excluding_training_days = 0`
- `training_lag_per_affected_run_days = 0`
- `annual_investment_input_loss_fraction = 0`

### safety-framework

Annual document and enforceability of previously discretionary commitment. Do not charge evaluation/remediation event again when bought with those policies. Framework obligations may weaken endogenously; prior reflects small but nonzero enforceability effect.

|Input|Units|Low / mode / high|Status|Rationale|
|---|---|---|---|---|
|setup_and_annual_staff_days|person_workdays_per_lab_year|10 / 30 / 100|analyst_prior|Incremental setup/maintenance work beyond voluntary practice; explicit workload prior.|
|per_release_staff_days|person_workdays_per_model|0 / 0 / 0|analyst_prior|Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program.|
|research_counterfactual_fraction|fraction_of_compliance_labor|0.05 / 0.15 / 0.35|analyst_prior|Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers.|
|binding_event_probability|probability_per_model|0 / 0.05 / 0.2|analyst_prior|Probability legal adherence adds a hold beyond the same voluntary framework.|
|binding_event_delay|calendar_days|1 / 7 / 30|analyst_prior|Incremental unresolved compliance/safeguard tail conditional on binding event.|
|internal_gate_fraction|fraction_of_binding_holds|0 / 0.15 / 0.5|analyst_prior|Share of legally induced holds affecting internal use, not only release.|

Formulas:
- `annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction`
- `annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)`
- `release_lag_excluding_training_days = binding_event_probability*binding_event_delay`
- `internal_use_lag_excluding_training_days = binding_event_probability*binding_event_delay*internal_gate_fraction`
- `training_lag_per_affected_run_days = 0`
- `annual_investment_input_loss_fraction = 0`

### transparency-report

Incremental document completion and occasional launch-critical signoff. Quarterly internal summaries folded into annual staff work. First trusted external access can trigger report; a launch-day document date is not measured causal delay.

|Input|Units|Low / mode / high|Status|Rationale|
|---|---|---|---|---|
|setup_and_annual_staff_days|person_workdays_per_lab_year|4 / 10 / 30|analyst_prior|Incremental setup/maintenance work beyond voluntary practice; explicit workload prior.|
|per_release_staff_days|person_workdays_per_model|2 / 6 / 20|analyst_prior|Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program.|
|research_counterfactual_fraction|fraction_of_compliance_labor|0.05 / 0.15 / 0.4|analyst_prior|Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers.|
|late_report_probability|probability_per_model|0 / 0.1 / 0.4|analyst_prior|Report not ready at otherwise planned external deployment despite existing system-card process.|
|report_tail_days|calendar_days|0.5 / 2 / 7|analyst_prior|Residual document/legal signoff tail after final evaluation, not total writing time.|

Formulas:
- `annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction`
- `annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)`
- `release_lag_excluding_training_days = late_report_probability*report_tail_days`
- `internal_use_lag_excluding_training_days = 0`
- `training_lag_per_affected_run_days = 0`
- `annual_investment_input_loss_fraction = 0`

### whistleblower

Reporting-channel operation and occasional incremental internal investigation. Internal delay is an annual localized hold expressed as equivalent complete-lab days; tag annual_event rather than multiply per release. Possible information/retention benefits set to zero in cost calibration, not established absent.

|Input|Units|Low / mode / high|Status|Rationale|
|---|---|---|---|---|
|setup_and_annual_staff_days|person_workdays_per_lab_year|3 / 10 / 40|analyst_prior|Incremental setup/maintenance work beyond voluntary practice; explicit workload prior.|
|per_release_staff_days|person_workdays_per_model|0 / 0 / 0|analyst_prior|Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program.|
|research_counterfactual_fraction|fraction_of_compliance_labor|0 / 0.05 / 0.2|analyst_prior|Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers.|
|extra_investigation_probability|probability_per_lab_year|0 / 0.03 / 0.15|analyst_prior|Incremental substantive concern producing a temporary hold due to legal protection, beyond voluntary channels.|
|investigation_hold_days|calendar_days|1 / 5 / 30|analyst_prior|Conditional annual hold; excludes ordinary responses that would happen anyway.|
|affected_research_fraction|fraction_of_lab_frontier_activity|0 / 0.1 / 0.4|analyst_prior|Share of frontier activity stopped during incremental investigation.|

Formulas:
- `annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction`
- `annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)`
- `release_lag_excluding_training_days = 0`
- `internal_use_lag_excluding_training_days = extra_investigation_probability*investigation_hold_days*affected_research_fraction`
- `training_lag_per_affected_run_days = 0`
- `annual_investment_input_loss_fraction = 0`

### shutdown

Documentation, testing and occasional incremental control-plane engineering. One-time engineering tail, not annual launch-rate multiplication. Avoided outage/theft not credited here.

|Input|Units|Low / mode / high|Status|Rationale|
|---|---|---|---|---|
|setup_and_annual_staff_days|person_workdays_per_lab_year|5 / 20 / 100|analyst_prior|Incremental setup/maintenance work beyond voluntary practice; explicit workload prior.|
|per_release_staff_days|person_workdays_per_model|1 / 3 / 10|analyst_prior|Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program.|
|research_counterfactual_fraction|fraction_of_compliance_labor|0.1 / 0.3 / 0.7|analyst_prior|Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers.|
|architecture_change_probability|probability_per_lab_first_year|0 / 0.05 / 0.3|analyst_prior|Frozen scope is developer-controlled models; expansive uncontrollable derivatives excluded.|
|architecture_change_days|calendar_days|2 / 10 / 45|analyst_prior|Engineering critical-path tail if current shutdown capability inadequate.|
|affected_research_fraction|fraction_of_frontier_activity|0 / 0.1 / 0.4|analyst_prior|Portion of ongoing frontier activity blocked by required engineering.|

Formulas:
- `annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction`
- `annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)`
- `release_lag_excluding_training_days = architecture_change_probability*architecture_change_days`
- `internal_use_lag_excluding_training_days = architecture_change_probability*architecture_change_days*affected_research_fraction`
- `training_lag_per_affected_run_days = 0`
- `annual_investment_input_loss_fraction = 0`

### third-party-audit

Independent annual audit plus residual findings. Audit finding uses same remediation node as evaluation findings; do not count duplicate remediation. Annual event affects releases nearby, not every release.

|Input|Units|Low / mode / high|Status|Rationale|
|---|---|---|---|---|
|setup_and_annual_staff_days|person_workdays_per_lab_year|25 / 60 / 200|analyst_prior|Incremental setup/maintenance work beyond voluntary practice; explicit workload prior.|
|per_release_staff_days|person_workdays_per_model|0 / 0 / 0|analyst_prior|Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program.|
|research_counterfactual_fraction|fraction_of_compliance_labor|0.05 / 0.15 / 0.4|analyst_prior|Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers.|
|blocking_finding_probability|probability_per_annual_audit|0 / 0.1 / 0.35|analyst_prior|Finding creates incremental hold relative to voluntary audit baseline.|
|finding_remediation_days|calendar_days|2 / 10 / 45|analyst_prior|Incremental unresolved remediation after audit finding.|
|internal_gate_fraction|fraction_of_holds|0 / 0.15 / 0.5|analyst_prior|Fraction of blocking remediation applicable to internal use.|

Formulas:
- `annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction`
- `annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)`
- `release_lag_excluding_training_days = blocking_finding_probability*finding_remediation_days`
- `internal_use_lag_excluding_training_days = blocking_finding_probability*finding_remediation_days*internal_gate_fraction`
- `training_lag_per_affected_run_days = 0`
- `annual_investment_input_loss_fraction = 0`

### internal-evals

Coverage of mandatory suite and residual final-checkpoint re-test. Existing evaluation effort stays in baseline; extra mandatory coverage is a prior. Evaluation-induced remediation modeled in triggered-redteam, not here.

|Input|Units|Low / mode / high|Status|Rationale|
|---|---|---|---|---|
|setup_and_annual_staff_days|person_workdays_per_lab_year|5 / 20 / 60|analyst_prior|Incremental setup/maintenance work beyond voluntary practice; explicit workload prior.|
|per_release_staff_days|person_workdays_per_model|5 / 20 / 70|analyst_prior|Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program.|
|research_counterfactual_fraction|fraction_of_compliance_labor|0.1 / 0.35 / 0.7|analyst_prior|Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers.|
|incremental_test_probability|probability_per_model|0.05 / 0.2 / 0.6|analyst_prior|Mandatory suite causes extra final testing relative to actual voluntary suite.|
|incremental_service_days|calendar_days|2 / 5 / 14|calibrated|Additional final-checkpoint test/writeup workload; informed by AISI but incremental share is prior.|
|remaining_non_eval_buffer|calendar_days|0 / 2 / 7|analyst_prior|Time until other launch readiness after additional tests start.|
|internal_gate_fraction|fraction_of_holds|0 / 0.03 / 0.15|analyst_prior|Optional holding of internal use absent statutory internal gate.|

Formulas:
- `annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction`
- `annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)`
- `release_lag_excluding_training_days = incremental_test_probability*maximum(0,incremental_service_days-remaining_non_eval_buffer)`
- `internal_use_lag_excluding_training_days = incremental_test_probability*maximum(0,incremental_service_days-remaining_non_eval_buffer)*internal_gate_fraction`
- `training_lag_per_affected_run_days = 0`
- `annual_investment_input_loss_fraction = 0`

### third-party-eval

Evaluation access and report-completion requirement with queue. A qualifying existing evaluator is reused. Reports and mandatory minimum access windows are shared nodes, not two independent waits. Need dedicated queues only if evaluator not substitutable.

|Input|Units|Low / mode / high|Status|Rationale|
|---|---|---|---|---|
|setup_and_annual_staff_days|person_workdays_per_lab_year|5 / 15 / 50|analyst_prior|Incremental setup/maintenance work beyond voluntary practice; explicit workload prior.|
|per_release_staff_days|person_workdays_per_model|3 / 10 / 40|analyst_prior|Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program.|
|research_counterfactual_fraction|fraction_of_compliance_labor|0.1 / 0.25 / 0.6|analyst_prior|Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers.|
|new_eval_probability|probability_per_model|0 / 0.15 / 0.4|analyst_prior|Fraction that would lack qualifying external assessment in same voluntary practice.|
|late_report_probability|probability_per_model|0 / 0.25 / 0.6|analyst_prior|Already-evaluated release that would proceed before formal report finalization.|
|report_tail_days|calendar_days|1 / 3 / 10|analyst_prior|Added formal report turnaround where release would previously proceed.|
|internal_gate_fraction|fraction_of_release_holds|0 / 0.05 / 0.2|analyst_prior|Voluntary internal hold induced by external report regime.|

Formulas:
- `annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction`
- `annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)`
- `release_lag_excluding_training_days = new_eval_probability*maximum(0,standard_eval_service+external_queue-baseline_access_runway-earlier_sharing_gain)+(1-new_eval_probability)*late_report_probability*report_tail_days`
- `internal_use_lag_excluding_training_days = (new_eval_probability*maximum(0,standard_eval_service+external_queue-baseline_access_runway-earlier_sharing_gain)+(1-new_eval_probability)*late_report_probability*report_tail_days)*internal_gate_fraction`
- `training_lag_per_affected_run_days = 0`
- `annual_investment_input_loss_fraction = 0`

### evaluator-window

Twenty-business-day qualifying access floor. Eight cases demonstrate heterogeneous access clocks; baseline runway distribution is a coarse prior-informed calibration. Three-day testing window is not asserted to be three-day runway.

|Input|Units|Low / mode / high|Status|Rationale|
|---|---|---|---|---|
|setup_and_annual_staff_days|person_workdays_per_lab_year|3 / 10 / 30|analyst_prior|Incremental setup/maintenance work beyond voluntary practice; explicit workload prior.|
|per_release_staff_days|person_workdays_per_model|3 / 10 / 40|analyst_prior|Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program.|
|research_counterfactual_fraction|fraction_of_compliance_labor|0.1 / 0.25 / 0.6|analyst_prior|Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers.|
|floor_calendar_days|calendar_days|28 / 28 / 28|calibrated|20business days modeled as4weeks ignoring holidays; explicit convention, not20calendar days.|
|internal_gate_fraction|fraction_of_release_holds|0 / 0.03 / 0.15|analyst_prior|Optional internal hold beyond literal external-release-only gate.|

Formulas:
- `annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction`
- `annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)`
- `release_lag_excluding_training_days = maximum(0,floor_calendar_days-baseline_access_runway-earlier_sharing_gain)+late_checkpoint_reset_probability*late_checkpoint_reset_days`
- `internal_use_lag_excluding_training_days = (maximum(0,floor_calendar_days-baseline_access_runway-earlier_sharing_gain)+late_checkpoint_reset_probability*late_checkpoint_reset_days)*internal_gate_fraction`
- `training_lag_per_affected_run_days = 0`
- `annual_investment_input_loss_fraction = 0`

### triggered-redteam

Danger threshold and incremental binding remediation. Threshold incidence is not legal increment. Preserve correlated tails when threshold crossing and remedial difficulty increase together; base numerical sampling treats them independent for inspectability.

|Input|Units|Low / mode / high|Status|Rationale|
|---|---|---|---|---|
|setup_and_annual_staff_days|person_workdays_per_lab_year|5 / 20 / 60|analyst_prior|Incremental setup/maintenance work beyond voluntary practice; explicit workload prior.|
|per_release_staff_days|person_workdays_per_model|5 / 20 / 80|analyst_prior|Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program.|
|research_counterfactual_fraction|fraction_of_compliance_labor|0.15 / 0.4 / 0.8|analyst_prior|Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers.|
|danger_trigger_probability|probability_per_frontier_model|0.5 / 0.8 / 1|calibrated|2026 frontier systems often have High/ASL3 or Critical capability classifications; frequency chosen, not estimated from selective cases.|
|incrementally_binding_fraction|fraction_of_triggered_models|0.05 / 0.2 / 0.5|analyst_prior|Fraction with additional hold relative to already voluntary safeguards, accounting for actual enforcement.|
|remediation_service_days|calendar_days|7 / 21 / 60|calibrated|Unprepared elevated testing/mitigation; AISI anchorsweeks but implementation tail is prior.|
|prepared_fraction|fraction_of_remediation_completed_in_parallel|0.25 / 0.65 / 0.9|analyst_prior|Proportion of remediation already prepared before it becomes critical; not a measured fact.|
|internal_gate_fraction|fraction_of_binding_holds|0.1 / 0.35 / 0.8|analyst_prior|Some safeguards needed before internal inference as Astra demonstrates; extent remains prior.|

Formulas:
- `annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction`
- `annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)`
- `release_lag_excluding_training_days = danger_trigger_probability*incrementally_binding_fraction*remediation_service_days*(1-prepared_fraction)`
- `internal_use_lag_excluding_training_days = danger_trigger_probability*incrementally_binding_fraction*remediation_service_days*(1-prepared_fraction)*internal_gate_fraction`
- `training_lag_per_affected_run_days = 0`
- `annual_investment_input_loss_fraction = 0`

### safety-case-deploy

Independent affirmative signoff; service, queue, re-review and non-approval. No direct published approval-time series exists. Numeric best estimate is therefore prior-weighted, with explicit nonapproval tail and shared evidence nodes. Independent signoff distinct from comments on a public report.

|Input|Units|Low / mode / high|Status|Rationale|
|---|---|---|---|---|
|setup_and_annual_staff_days|person_workdays_per_lab_year|20 / 60 / 200|analyst_prior|Incremental setup/maintenance work beyond voluntary practice; explicit workload prior.|
|per_release_staff_days|person_workdays_per_model|15 / 40 / 120|analyst_prior|Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program.|
|research_counterfactual_fraction|fraction_of_compliance_labor|0.15 / 0.4 / 0.8|analyst_prior|Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers.|
|review_service_days|calendar_days|7 / 21 / 60|analyst_prior|Novel affirmative review; planned parallel document preparation. No measured frontier certification duration.|
|parallel_review_fraction|fraction_of_service_before_other_readiness|0.25 / 0.5 / 0.8|analyst_prior|Rolling review before final checkpoint; full prior.|
|review_queue_days|calendar_days|0 / 5 / 30|analyst_prior|Dedicated signoff capacity; first-year program may queue.|
|rereview_probability|probability_per_case|0.1 / 0.25 / 0.5|analyst_prior|Evidence deficiencies prompt another round.|
|rereview_days|calendar_days|7 / 14 / 45|analyst_prior|Residual second-review service.|
|nonapproval_probability|probability_per_case|0 / 0.01 / 0.08|analyst_prior|Cannot substantiate case, absent in voluntary baseline.|
|nonapproval_wait_days|calendar_days|30 / 90 / 180|analyst_prior|Time to acceptable substitute/reworked release within first-year horizon; not permanent prohibition.|
|internal_gate_fraction|fraction_of_release_holds|0 / 0.05 / 0.25|analyst_prior|Policy legally covers external deployment; internal delay is optional spillover.|

Formulas:
- `annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction`
- `annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)`
- `release_lag_excluding_training_days = review_service_days*(1-parallel_review_fraction)+review_queue_days+rereview_probability*rereview_days+nonapproval_probability*nonapproval_wait_days`
- `internal_use_lag_excluding_training_days = (review_service_days*(1-parallel_review_fraction)+review_queue_days+rereview_probability*rereview_days+nonapproval_probability*nonapproval_wait_days)*internal_gate_fraction`
- `training_lag_per_affected_run_days = 0`
- `annual_investment_input_loss_fraction = 0`

### safety-case-train

Pre-training licensing with early filing, revision and refusal. Training output is effective run-level lag after usable parallel research; raw calendar wait also supplied. Do not count release/internal wait again; downstream propagation handled by root. Investment uncertainty treated separately in sensitivity, to avoid hidden duplicate denial costs.

|Input|Units|Low / mode / high|Status|Rationale|
|---|---|---|---|---|
|setup_and_annual_staff_days|person_workdays_per_lab_year|20 / 60 / 200|analyst_prior|Incremental setup/maintenance work beyond voluntary practice; explicit workload prior.|
|per_run_staff_days|person_workdays_per_qualifying_run|10 / 30 / 100|analyst_prior|Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program.|
|research_counterfactual_fraction|fraction_of_compliance_labor|0.1 / 0.3 / 0.7|analyst_prior|Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers.|
|approval_service_days|calendar_days|14 / 30 / 90|analyst_prior|Novel regulator review rather than brief notice; prior.|
|approval_queue_days|calendar_days|0 / 10 / 45|analyst_prior|First-year authorization queue; no measured system.|
|filing_advance_days|calendar_days|7 / 30 / 90|analyst_prior|How far application can precede compute/data readiness; no unobserved actual dates invented.|
|rereview_probability|probability_per_run|0.1 / 0.25 / 0.5|analyst_prior|Conditions or revisions require additional review.|
|rereview_days|calendar_days|7 / 21 / 60|analyst_prior|Residual approval re-review duration.|
|refusal_probability|probability_per_run|0 / 0.02 / 0.1|analyst_prior|Refused or withdrawn run replaced by smaller/different run.|
|refusal_substitute_days|calendar_days|30 / 90 / 180|analyst_prior|Time until acceptable replacement research path within first year.|
|parallel_work_fraction|fraction_of_frontier_progress_preserved_while_waiting|0.1 / 0.35 / 0.7|analyst_prior|Algorithmic/data/other runs continue during administrative pause.|

Formulas:
- `annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_run_staff_days*qualifying_training_runs)*research_counterfactual_fraction`
- `annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)`
- `release_lag_excluding_training_days = 0`
- `internal_use_lag_excluding_training_days = 0`
- `training_lag_per_affected_run_days = (maximum(0,approval_service_days+approval_queue_days-filing_advance_days)+rereview_probability*rereview_days+refusal_probability*refusal_substitute_days)*(1-parallel_work_fraction)`
- `annual_investment_input_loss_fraction = 0`
- `raw_training_wait_calendar_days = (maximum(0,approval_service_days+approval_queue_days-filing_advance_days)+rereview_probability*rereview_days+refusal_probability*refusal_substitute_days)`
- `progress_preserved_during_wait_fraction = parallel_work_fraction`

### training-notice-30

Thirty-day notice with unplanned changes and substitute research. No fresh reset for trivial changes; reset scope explicitly part of frozen scenario. A notice rule is not a30day universal lost-output block.

|Input|Units|Low / mode / high|Status|Rationale|
|---|---|---|---|---|
|setup_and_annual_staff_days|person_workdays_per_lab_year|2 / 5 / 15|analyst_prior|Incremental setup/maintenance work beyond voluntary practice; explicit workload prior.|
|per_run_staff_days|person_workdays_per_qualifying_run|1 / 3 / 10|analyst_prior|Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program.|
|research_counterfactual_fraction|fraction_of_compliance_labor|0.1 / 0.25 / 0.6|analyst_prior|Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers.|
|notice_days|calendar_days|30 / 30 / 30|observed|Exact frozen policy waiting period.|
|ordinary_notice_advance_days|calendar_days|14 / 45 / 90|analyst_prior|Planned run notice leadtime before otherwise ready; explicit unmeasured prior.|
|reset_probability|probability_per_run|0 / 0.15 / 0.4|analyst_prior|Run/recipe changes requiring a fresh notice, assuming material changes reset clock.|
|reset_notice_advance_days|calendar_days|0 / 7 / 21|analyst_prior|Leadtime remaining for material run changes.|
|parallel_work_fraction|fraction_of_frontier_progress_preserved_while_waiting|0.1 / 0.4 / 0.8|analyst_prior|Alternative research and smaller runs while notice clock runs.|

Formulas:
- `annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_run_staff_days*qualifying_training_runs)*research_counterfactual_fraction`
- `annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)`
- `release_lag_excluding_training_days = 0`
- `internal_use_lag_excluding_training_days = 0`
- `training_lag_per_affected_run_days = ((1-reset_probability)*maximum(0,notice_days-ordinary_notice_advance_days)+reset_probability*maximum(0,notice_days-reset_notice_advance_days))*(1-parallel_work_fraction)`
- `annual_investment_input_loss_fraction = 0`
- `raw_training_wait_calendar_days = ((1-reset_probability)*maximum(0,notice_days-ordinary_notice_advance_days)+reset_probability*maximum(0,notice_days-reset_notice_advance_days))`
- `progress_preserved_during_wait_fraction = parallel_work_fraction`

### strict-liability

Product-liability risk changes releases, investment and legal labor. Numerical best estimate is analyst-prior expectation. Recent device evidence supports separating releases/research/safety but does not quantify AI investment loss. Capital response can be positive or negative after an explicit demand/trust offset. Neither downside nor upside coefficient is empirically identified; report gross and net sensitivity.

|Input|Units|Low / mode / high|Status|Rationale|
|---|---|---|---|---|
|setup_and_annual_staff_days|person_workdays_per_lab_year|20 / 60 / 200|analyst_prior|Incremental setup/maintenance work beyond voluntary practice; explicit workload prior.|
|per_release_staff_days|person_workdays_per_model|3 / 10 / 40|analyst_prior|Incremental preparation/support/signoff workload beyond voluntary practice; not total existing safety program.|
|research_counterfactual_fraction|fraction_of_compliance_labor|0.05 / 0.15 / 0.4|analyst_prior|Share of incremental task hours that actually displaces capability R&D after specialist staffing and substitution; not all safety/legal work competes1for1 with researchers.|
|extra_review_probability|probability_per_model|0.1 / 0.35 / 0.8|analyst_prior|Incremental caution relative to existing tort exposure.|
|extra_review_days|calendar_days|1 / 7 / 30|analyst_prior|Additional launch-risk review and remediation tail; not a legal minimum.|
|internal_gate_fraction|fraction_of_release_holds|0 / 0.05 / 0.25|analyst_prior|Liability chiefly external harm; some internal research choices affected.|
|financing_exposed_share|fraction_of_annual_RnD_investment|0.1 / 0.3 / 0.6|analyst_prior|Projects whose funding hurdle responds to extra liability; no universal capital freeze.|
|extra_risk_premium|annual_rate_fraction|0 / 0.01 / 0.04|analyst_prior|Extra liability uncertainty/insurance-adjusted financing hurdle:0-100-400bps; entirely analyst prior.|
|trust_demand_investment_offset|fraction_of_annual_RnD_investment|0 / 0.001 / 0.005|analyst_prior|Possible credible safety commitment and demand/insurance benefit reallocated to R&D; wholly unmeasured analyst prior. Central0.1percent, support0to0.5percent annualR&D. Permits net investment gain rather than constraining sign.|
|investment_semielasticity|fractional_investment_change_per_unit_annual_rate|0 / 1 / 5|analyst_prior|Local response of exposed research investment to hurdle rate; not imported from medical-device coefficient.|
|innovation_redirection_offset|fraction_of_foregone_investment_redeployed_productively|0 / 0.3 / 0.8|analyst_prior|Safer architectures/research substitutes can retain some capability progress.|

Formulas:
- `annual_displaced_rd_workdays = (setup_and_annual_staff_days+per_release_staff_days*releases_per_year)*research_counterfactual_fraction`
- `annual_rd_input_loss_fraction = annual_displaced_rd_workdays/(rd_staff*workdays_per_FTE_year)`
- `release_lag_excluding_training_days = extra_review_probability*extra_review_days`
- `internal_use_lag_excluding_training_days = extra_review_probability*extra_review_days*internal_gate_fraction`
- `training_lag_per_affected_run_days = 0`
- `annual_investment_input_loss_fraction = minimum(.5,financing_exposed_share*extra_risk_premium*investment_semielasticity*(1-innovation_redirection_offset))-trust_demand_investment_offset`

## Shared inputs

- **releases_per_year** (frontier_models_per_lab_year): {'type': 'triangular', 'low': 3, 'mode': 6, 'high': 12}; analyst_prior. Working current-technology range for material frontier releases, excluding mere effort/price variants; not fitted to these selected eight cases.
- **rd_staff** (effective_capability_research_FTE_per_lab): {'type': 'triangular', 'low': 500, 'mode': 1000, 'high': 3000}; analyst_prior. Explicit denominator prior; no public primary source identifies effective frontier research staffing. Sensitivity must include this denominator.
- **workdays_per_FTE_year** (workdays_per_FTE_year): {'type': 'triangular', 'low': 250, 'mode': 250, 'high': 250}; analyst_prior. Accounting convention; labor days remain distinct from calendar days.
- **baseline_access_runway** (calendar_days_before_planned_release): {'type': 'triangular', 'low': 9, 'mode': 21, 'high': 35}; calibrated. Fallback triangle only. Preferred sampling_override uses equally weighted release-cluster runways12/21/28/21days plus transport jitter and a separately labeled short-unobserved-runway mixture. GPT5.5 test-start runway is a lower bound on first access. Astra3testdays is not a measured runway.
- **runway_transport_shift** (calendar_days): {'type': 'triangular', 'low': -7, 'mode': 0, 'high': 7}; analyst_prior. Unidentified current2026 transport adjustment around historical observed release-cluster runways; analyst prior.
- **short_unobserved_runway_probability** (probability): {'type': 'triangular', 'low': 0, 'mode': 0.15, 'high': 0.4}; analyst_prior. Mixing probability for current short access runway absent observed endpoints; not fit from Astra testing duration.
- **short_unobserved_runway** (calendar_days): {'type': 'triangular', 'low': 3, 'mode': 7, 'high': 14}; analyst_prior. Explicit short-runway sensitivity component; no case coded as observing these endpoints.
- **earlier_sharing_gain** (calendar_days): {'type': 'triangular', 'low': 0, 'mode': 7, 'high': 21}; analyst_prior. Feasible early sharing induced by mandate; earlier checkpoints demonstrably possible, amount policy can advance access unknown.
- **standard_eval_service** (calendar_days): {'type': 'triangular', 'low': 7, 'mode': 10, 'high': 21}; calibrated. AISI standard1-2weeks with upper allowance for2026 broader coverage; not a measured mandate effect.
- **external_queue** (calendar_days): {'type': 'triangular', 'low': 0, 'mode': 2, 'high': 14}; analyst_prior. Funded current-scale evaluator program queue prior; no queue measurements public. High-capacity stress should change upper bound to60.
- **late_checkpoint_reset_probability** (probability_per_model): {'type': 'triangular', 'low': 0, 'mode': 0.15, 'high': 0.4}; analyst_prior. Final checkpoint may change after early access. GPT5 final checkpoint came15days after first. Frequency requiring legally fresh evaluation unknown.
- **late_checkpoint_reset_days** (calendar_days): {'type': 'triangular', 'low': 1, 'mode': 3, 'high': 10}; analyst_prior. Incremental re-test tail after a material final-checkpoint change; analyst prior, not observed GPT5 delay.
- **critical_training_stages_per_year** (sequential_stages_per_critical_chain_year): {'type': 'triangular', 'low': 1, 'mode': 1.5, 'high': 2}; analyst_prior. Separate schedule prior: only1-2 genuinely dependent qualifying stages on the frontier critical path, not every parallel experiment. Scenario support must be widened if continuous RL updates legally require fresh approvals.
- **qualifying_training_runs** (runs_per_lab_year): {'type': 'triangular', 'low': 1, 'mode': 2, 'high': 6}; analyst_prior. Qualifying new above-threshold training runs; material release count does not identify this. Explicit prior.

## Bundle gate logic

### sb-53

Union framework/report/incident/channel tasks; release=max(framework-induced hold, transparency-report gate). No mandatory external evaluation or training approval. 

Union obligations; common evidence production charged once; shared release prerequisites combine by maximum, sequential review after evidence adds only its residual; no independent bundle-price prior.

- **common_compliance_labor_overlap** (fraction_of_summed_compliance_work): {'type': 'triangular', 'low': 0.1, 'mode': 0.25, 'high': 0.45}. Common legal review/control infrastructure reused; not25percent of gates.
### raise-act

Same obligation families asSB53 with72hour reporting and separate filings; evaluate as standalone bundle-removal counterfactual, not six extra days on top ofSB53. If combined withSB53, replace reporting deadline by stricter requirement and charge only extra state filings, not duplicate framework work.

Union obligations; common evidence production charged once; shared release prerequisites combine by maximum, sequential review after evidence adds only its residual; no independent bundle-price prior.

- **common_compliance_labor_overlap** (fraction_of_summed_compliance_work): {'type': 'triangular', 'low': 0.1, 'mode': 0.25, 'high': 0.45}. Reusable framework/system-card processes.
- **extra_state_filing_staff_days** (person_workdays_per_year): {'type': 'triangular', 'low': 2, 'mode': 5, 'high': 15}. Separate regulator deadlines/forms beyond one common process.
### sb-1047

Add self-certified pre-training protocol plus unreasonable-risk release standard. Training starts when existing protections/protocol ready, without regulator approval; release remediation shares triggered-redteam node. 2026 counterfactual for frozen vetoed bill. KYC China effect from diffusion agent; do not add a free-standing liability policy as if statutory regimes identical.

Union obligations; common evidence production charged once; shared release prerequisites combine by maximum, sequential review after evidence adds only its residual; no independent bundle-price prior.

- **common_compliance_labor_overlap** (fraction_of_sum): {'type': 'triangular', 'low': 0.1, 'mode': 0.25, 'high': 0.45}. Cross-document and audit reuse.
- **pretraining_protocol_residual_probability** (probability_per_run): {'type': 'triangular', 'low': 0, 'mode': 0.05, 'high': 0.2}. Self-certification unusually not ready by planned run.
- **pretraining_protocol_residual_days** (calendar_days): {'type': 'triangular', 'low': 0.5, 'mode': 2, 'high': 7}. Protocol/security documentation tail; no formal licensing queue.
### eu-ai-act

One shared evaluation program plus Model Report; release=max(internal eval tail, external report tail, appropriate access-floor tail, transparency tail). Risk remediation remains shared. EU-only restrictions affect Chinese access only with synchronized global launch. 

Union obligations; common evidence production charged once; shared release prerequisites combine by maximum, sequential review after evidence adds only its residual; no independent bundle-price prior.

- **common_compliance_labor_overlap** (fraction_of_sum): {'type': 'triangular', 'low': 0.2, 'mode': 0.4, 'high': 0.65}. Same test/evidence package supports internal/external evaluation and report.
- **access_floor_applies_probability** (probability_per_model): {'type': 'triangular', 'low': 0.25, 'mode': 0.6, 'high': 1}. Code says appropriate for most methods, unlike standalone universal floor.
- **global_release_synchronization_probability** (probability_per_model): {'type': 'triangular', 'low': 0, 'mode': 0.4, 'high': 1}. Otherwise EU-only release hold does not delay non-EU access; source gives regional examples, probability is prior.
### ai-risk-evaluation-act

DOE compliance/participation, not statutory affirmative safety certification. Reuse ordinary eval where accepted; additional classified onboarding/service/report can determine external-release date. Do not silently upgrade participation duty into a veto based on findings; separate agency-in-practice pressure scenario.

Union obligations; common evidence production charged once; shared release prerequisites combine by maximum, sequential review after evidence adds only its residual; no independent bundle-price prior.

- **classified_extra_service_days** (calendar_days): {'type': 'triangular', 'low': 0, 'mode': 7, 'high': 28}. Security/onboarding/specialized tests beyond normal qualifying evaluation.
- **government_queue_days** (calendar_days): {'type': 'triangular', 'low': 0, 'mode': 7, 'high': 45}. First-year DOE program congestion; analyst prior.
- **completion_required_probability** (probability_per_model): {'type': 'triangular', 'low': 0.25, 'mode': 0.75, 'high': 1}. Participation compliance interpreted to require completed testing/report before release; statute does not explicitly demand safety approval.
- **common_compliance_labor_overlap** (fraction_of_sum): {'type': 'triangular', 'low': 0.1, 'mode': 0.3, 'high': 0.5}. Internal results reused by external program.
### secure-ai-development-act

Replace28day converted floor with21calendar days; model weights/runtime delivery and readiness rather than API-only access. No mandatory safety approval added. 

Union obligations; common evidence production charged once; shared release prerequisites combine by maximum, sequential review after evidence adds only its residual; no independent bundle-price prior.

- **required_calendar_access** (calendar_days): {'type': 'triangular', 'low': 21, 'mode': 21, 'high': 21}. Verified Section3(c).
- **weights_handoff_extra_days** (calendar_days): {'type': 'triangular', 'low': 0, 'mode': 2, 'high': 10}. Incremental secure handoff relative to existing API evaluator access; prior.
- **additional_staff_days** (person_workdays_per_model): {'type': 'triangular', 'low': 2, 'mode': 5, 'high': 20}. Secure packaging/liaison work beyond access-window overhead.
### frontier-act

Shared evidence; annual audits plus six-month independent verifications for very large developers; state-preemption removes duplicate obligations. No routine pre-training approval. Emergency order is separate annual event, often overlapping a risk-triggered remediation; do not count both.

Union obligations; common evidence production charged once; shared release prerequisites combine by maximum, sequential review after evidence adds only its residual; no independent bundle-price prior.

- **audit_frequency_per_year** (audits_per_year): {'type': 'triangular', 'low': 2, 'mode': 2, 'high': 2}. Frozen very-large-developer six-month verification frequency.
- **second_audit_increment_fraction** (fraction_of_first_audit_work): {'type': 'triangular', 'low': 0.3, 'mode': 0.5, 'high': 0.8}. Evidence reused between annual audit and six-month verification; do not double every fixed task.
- **second_audit_new_finding_fraction** (fraction_of_annual_finding_probability): {'type': 'triangular', 'low': 0.1, 'mode': 0.3, 'high': 0.6}. Additional six-month verification reuses evidence; incremental binding finding probability relative to first audit is explicitly a prior, distinct from labor reuse.
- **common_compliance_labor_overlap** (fraction_of_sum): {'type': 'triangular', 'low': 0.15, 'mode': 0.3, 'high': 0.5}. Common reports and governance system.
- **preempted_duplicate_labor_fraction** (fraction_of_common_work): {'type': 'triangular', 'low': 0, 'mode': 0.1, 'high': 0.3}. Marginal state duplication eliminated; no automatic frontier-day credit.
- **emergency_order_probability** (probability_per_lab_year): {'type': 'triangular', 'low': 0, 'mode': 0.01, 'high': 0.05}. Incremental emergency hold under frozen powers; analyst tail.
- **emergency_order_days** (calendar_days): {'type': 'triangular', 'low': 7, 'mode': 30, 'high': 90}. Resolution/replacement period for rare order.
### pause-letter

Use pause-6 upstream-production model with explicit country scope. No independent bundle estimate. The text requests global compliance. If headline preserves site unilateral-US scenario, label it unambiguously; provide universal coordinated scenario separately.

Union obligations; common evidence production charged once; shared release prerequisites combine by maximum, sequential review after evidence adds only its residual; no independent bundle-price prior.


## Limits and sensitivity

- Public timestamps constrain available service/runway durations but do not identify policy-caused delays. Most causal parameters are explicitly analyst priors.
- Baseline staff denominator is a prior, not verified lab headcount. Rerun with500 and3000 effective FTE; do not present fractional-day outputs as precise observations.
- Queue priors assume funded current-scale implementation. Stress queues at0/14/60calendar days and allow common delays across all labs.
- Existing voluntary practices may already satisfy the new rule, so threshold incidence and legally incremental binding incidence are distinct.
- Liability financing premium and semielasticity are sensitivity inputs, not empirical extrapolations from medical devices.
- National frontier=max across labs; repeated parallel release shifts do not simply add. Root estimator must handle replacement/serial chains/diffusion.
- Safety benefits beyond measured security/diffusion are not priced here; zero credited benefit is not evidence of zero benefit.

## Sources

- **met_o1** [METR preliminary evaluation of o1-preview](https://metr.org/evaluations/openai-o1-preview-report/): o1-preview access September 3 and o1-mini August 28; testing ended September 9, 2024. Earlier related checkpoint August 26. API throughput constrained.
- **rel_o1** [OpenAI introducing o1-preview](https://openai.com/index/introducing-openai-o1-preview/): o1-preview and o1-mini first public release September 12, 2024.
- **met_o3** [METR preliminary evaluation of o3 and o4-mini](https://metr.org/evaluations/openai-o3-report/): Earlier checkpoints supplied three weeks before release; no specific access start date or full evaluation/report timeline published here.
- **rel_o3** [OpenAI introducing o3 and o4-mini](https://openai.com/index/introducing-o3-and-o4-mini/): Public release April 16, 2025.
- **met_gpt5** [METR evaluation of GPT-5](https://metr.org/evaluations/gpt-5-report/): First checkpoint July 10; final launch checkpoint July 25; reasoning traces July 26; checklist answers July 29; preliminary report August 1, 2025. Four weeks of pre-release access versus three weeks of evaluation work.
- **rel_gpt5** [OpenAI introducing GPT-5](https://openai.com/index/introducing-gpt-5/): Public release August 7, 2025.
- **card_gpt55** [GPT-5.5 System Card](https://deploymentsafety.openai.com/gpt-5-5): SecureBio assessed two pre-release checkpoints April 2 through April 9, 2026. They differed from deployed version; final-version rerun was planned. High cyber classification with safeguards.
- **rel_gpt55** [OpenAI introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/): First product release April 23; API availability April 24, 2026.
- **card_astra** [GPT-6 Astra System Card](https://deploymentsafety.openai.com/gpt-6-astra): Apollo had three days of testing, two with high-throughput reasoning-trace access, on a near-final representative model. Safeguards applied to internal tool-using inference. Published September 3, 2026.
- **rel_astra** [OpenAI introducing GPT-6 Astra](https://openai.com/index/gpt-6-astra/): Initial release to limited organizations, broader rollout over following days. Do not code September 3 as established general API availability.
- **rel_astra_notes** [ChatGPT release notes September 3 2026](https://help.openai.com/en/articles/6825453-chatgpt-release-notes): September 3 entry: Astra initially available to limited organizations, not general availability.
- **metr_process26** [METR time horizon evaluation process May 2026](https://metr.org/time-horizons/): Typically at least1-2weeks calendar for access setup, scaffolds, around1000 test runs, restarts and manual review. One theoretical compute day is not complete evaluation service time.
- **met_opus55** [METR predeployment evaluation of Claude Opus 5.5](https://metr.org/blog/2026-09-22-claude-opus-5-5/): 10 business days of API capability testing; exact calendar endpoints not provided. Report published September 22, 2026.
- **rel_opus55** [Anthropic introducing Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5): Model publicly released September 22, 2026.
- **aisi_tiers** [AISI Early lessons from evaluating frontier AI systems](https://www.aisi.gov.uk/blog/early-lessons-from-evaluating-frontier-ai-systems): Light testing a few days and 1-2 weeks including QA/reporting; standard 1-2 weeks; elevated several weeks. Developing ideal-state tiers, not observed incremental legal delays.
- **access26** [Charnock et al., Expanding external access](https://arxiv.org/abs/2601.11916): Access has model, information and timeframe dimensions. Extra access creates operational and security work; no causal delay coefficient.
- **gans26** [Gans, Staged Access and Liability for Dual-Use AI](https://www.nber.org/papers/w35586): August 2026, revised September: release windows and liability interact through strategic defensive and adversarial effort; no US-China calibration.
- **gans25** [Gans, Regulating the Direction of Innovation](https://www.nber.org/papers/w32741): JPubE 2025: regulation can change allocation between research paths; sign of innovation effect is not fixed.
- **guerreiro26** [Guerreiro, Rebelo and Teles, Regulating AI](https://www.nber.org/papers/w31921): May 2026 revision: staged experimentation and release under uncertainty and heterogeneous beliefs. No service-time estimate.
- **galasso26** [Galasso and Luo, Product Liability Litigation and Innovation](https://www.aeaweb.org/articles?id=10.1257/mic.20240255): AEJ Micro August 2026: medical-device introductions fall temporarily in litigated categories, with safer devices. Do not transport coefficients to AI.
- **compliance26** [Trebbi, Zhang and Simkovic, Compliance costs](https://www.nber.org/papers/w30691): Occupation-task compliance costing motivates labor decomposition; no frontier-lab headcount or marginal research elasticity identified.
- **breuer25** [Breuer, Leuz and Vanhaverbeke, Reporting and innovation](https://www.nber.org/papers/w26291): JAE 2025: firm-level innovation changes differ from industry aggregate after reporting requirements; no AI calibration.
- **sb53_incident** [California BPC 22757.13](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=22757.13): 15-day incident report; 24-hour disclosure for imminent harm. No pre-release wait in this section.
- **sb53** [California SB53 frozen text](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53): Site definition used for framework/report/whistleblower package. Full statutory re-audit not performed in this calibration.
- **eu_code** [EU GPAI Code of Practice safety/security](https://ec.europa.eu/newsroom/dae/redirection/document/118119): 20 business days appropriate for most evaluation methods, not an unconditional statutory fixed waiting period. Frozen evaluator-window item explicitly imposes a floor.
- **s2938** [AI Risk Evaluation Act S2938 introduced text](https://www.govinfo.gov/content/pkg/BILLS-119s2938is/html/BILLS-119s2938is.htm): Deployment outside developer custody prohibited absent participation/compliance; testing and formal reports; no explicit statutory safety sign-off or fixed wait.
- **s5061** [Secure AI Development Act S5061 introduced text](https://www.govinfo.gov/content/pkg/BILLS-119s5061is/html/BILLS-119s5061is.htm): Section3(c): make model including weights/runtime available to NSA at least21 calendar days before commerce; no explicit approval gate in this clause.
- **govai26** [GovAI, Delays to Frontier AI in EU and UK](https://www.governance.ai/research-paper/delays-to-frontier-ai-in-the-eu-and-uk): 375 releases through May2026; regional API versus app distinction; enforcement period after August2026 absent.
- **site** [AI Safety Menu data.js snapshot 2026-09-24](https://elehrer123-arch.github.io/ai-safety-menu/#/): Frozen policy definitions are the modeled intervention; analyst priors are not inherited site prices.
