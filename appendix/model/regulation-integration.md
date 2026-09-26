# Regulatory model integration contract (2026-09-25)

This module supplies intermediate policy mechanisms, not the national lead-closure headline. All causal parameters without direct observations are labeled analyst priors. Eight model cases comprise six release campaigns; timestamps measure access and evaluation windows, never causal policy delays.

## Callable interface

`sample_regulation(n, seed, overrides={})` returns NumPy arrays in `shared`, `policies`, `bundles`, plus input dictionaries and recurrence metadata. Override names are `shared.baseline_access_runway`, `strict-liability.extra_risk_premium`, etc. Values can be constants or triangular dictionaries. There are no file writes or network requests on import.

The original `release_lag_excluding_training_days` and `internal_use_lag_excluding_training_days` bundle outputs are nominal simultaneous-gate envelopes. They combine event-clock families for comparison and MUST NOT be treated as permanent endpoint lags. Prefer these decomposed fields:

|Field|Clock and application|
|---|---|
|recurring_release_lag_days|Expected marginal lag for each affected release; do not add across independent releases.|
|recurring_internal_use_lag_days|Expected marginal lag in availability of each affected internally used model; do not add across independent releases.|
|annual_event_release_equivalent_days|Annual event exposure; not a per-release or permanent gate. Can use a clearly labeled cycle-average division by releases/year for a coarse teacher-access approximation.|
|annual_event_internal_equivalent_days|Equivalent annual interrupted frontier days; annual recurrence, not per-release multiplication.|
|first_year_setup_release_equivalent_days|One first-year setup event, no annual repetition. A dated release model should recover after a later unaffected release.|
|first_year_setup_internal_equivalent_days|One first-year interruption; cumulative approximation scales with min(years,1), not years indefinitely.|
|raw_training_wait_calendar_days|Physical elapsed administrative wait per qualifying critical-chain stage.|
|progress_preserved_during_wait_fraction|Research progress retained by useful parallel work; apply exactly once.|
|training_lag_per_affected_run_days|Already discounts preserved parallel work; do not apply preservation again.|
|annual_rd_input_loss_fraction|Annual effective research labor input displaced; map through research production, not directly through the calendar.|
|annual_investment_input_loss_fraction|Signed annual R&D investment/input change; loss positive, gain negative. Does not represent an immediate installed compute-stock loss.|

For bundles, `recurrence_masks` enumerates each component. Shutdown is first-year setup for both clocks. Whistleblower is an annual internal interruption. Audit is annual on both clocks. Framework, transparency, internal/external evaluations and access windows recur per affected model. FRONTIER's second verification and emergency orders are annual events. Labor reuse discounts labor, never arbitrary percentages of gate durations.

`gate_release_dates(planned_release_days, holds)` applies concrete dated hold windows using `start <= ready_date < end`, then permits all later unaffected releases. It does not accumulate a fictional permanent backlog. Exact onset dates are not known from public evidence; the parent's coarse calendar approximation should be labeled as such.

## Event-max correction

`expected_maximum(gates)` calculates E[max(X1,...,Xk)] exactly conditional on sampled parameters, using mutually exclusive outcomes within each gate and independent distinct incremental binding events across gates. For two independent 50% chances of a ten-day gate, the expectation is 7.5 days, whereas max of expected values is only 5 days. Shared evidence tasks and queues occur once. Within the external evaluation gate, new evaluation and late reporting are mutually exclusive outcomes. Within the access floor, the final-checkpoint re-test extends the same floor rather than creating a second independent release pipeline.

This independence assumption is transparent, not identified. Correlated risk findings remain a sensitivity: each marginal policy excludes baseline voluntary remediation; bundles use a maximum where holds overlap rather than adding all delays. Annual events at different dates use a uniform-exposure union approximation, H*(1-product(1-E[occupied_days_i]/H)), rather than a maximum. Neither approximation substitutes for private dated operations data.

## Training schedule

Qualifying training runs Tri(1,2,6) scale paperwork labor only. The separate `shared.critical_training_stages_per_year` prior Tri(1,1.5,2) represents genuinely sequential stages on the active frontier critical path. It is not derived from release counts or parallel training experiments. Widen this prior if the policy treats every major ongoing RL revision as a newly licensed run.

`training_chain_penalty(raw_wait, preserved, critical_stages_per_year, horizon_days=eligible_elapsed)` returns:

`min(eligible_elapsed, raw_wait * critical_stages_per_year * eligible_elapsed / 365.25) * (1-preserved)`

This is continuous-progress equivalent loss during the first year, with no later catch-up assumed. The function includes NO initial pipeline or grandfathering delay. If the parent applies its Tri(30,90,180) first-output delay, pass elapsed days after that delay. Do not apply a second initial pipeline offset. This formula is preferable to Kd/(365+Kd), which is a stationary renewal-throughput expression rather than the first-year loss accounting requested here. An exact milestone timing model would instead need run start times, dependencies, training durations and completion schedules.

## Evidence-linked runway update

The preferred sampler supersedes the fallback triangle with four equally weighted release-cluster values: 12, 21, 28 and 21 calendar days. The 12-day value averages the paired o1-preview/o1-mini campaign; the o3/o4 figure is a rounded reported three weeks. GPT-5 has exact 28-day first-checkpoint runway but only 13 days on the final launch checkpoint. GPT-5.5's 21 days use the start of the reported SecureBio test interval and are a conservative lower bound on possible earlier access.

The historical component receives an explicit Tri(-7,0,7)-day transport shift. It is mixed with an unobserved short-runway Tri(3,7,14) scenario at probability Tri(0,.15,.4). The short component is an analyst assumption about 2026 transport, not an invented observation from Astra's three days of testing. Missing Astra/Opus endpoints stay missing. This changes baseline expected runway from the previous 15-day hand triangle to about 18.2 days; an all-historical zero-transport scenario has exactly 20.5-day expectation. The public sample is selected, clustered, heterogeneous in checkpoint and scope, and too small for a credible population confidence interval.

METR's May 2026 process description now independently supports calendar service priors: around 1,000 test runs might fit within one theoretical compute day, but access setup, scaffolds, infrastructure, reruns and manual analysis typically require at least one to two calendar weeks.

## Signed liability response

Gross financing/input loss remains an explicit product of exposed share, added annual risk premium, investment semielasticity and productive substitution. New `trust_demand_investment_offset` Tri(0,.001,.005) allows credible safety commitment, insurance or demand to support R&D investment. Its mean is 0.20% of annual R&D investment, versus roughly 0.70% gross financing loss, leaving a 0.50% net loss prior mean and allowing negative net loss in some draws. The benefit has no identified empirical AI coefficient; neither side is presented as one. Report zero-benefit and upper-benefit sensitivities. Do not count this annual input both through the research input ratio and an immediate log compute-stock hit.

## Validation

`python -m unittest discover -s work/policy-pricing -p test_regulation_sampler.py -v`

Eight tests pass: exact event maxima, training units/exposure/cap, dated annual masks without backlog, date arithmetic and source IDs, deterministic reproducibility and recurrence, clustered runway sampling, signed liability gains, and separation of parallel-run paperwork from critical-chain scheduling. Missing dates are never imputed. Tests do not validate the truth of the analyst priors.

The `pause-letter` bundle deliberately has an unowned `pause-6` component; root must attach the production model rather than reporting the zero placeholder. SB1047 similarly needs KYC; EU needs weight security.
