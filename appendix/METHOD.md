# Policy estimates: measurement contract

The headline is the expected change in the U.S.–China capability lead **12 months after implementation**, in days of baseline U.S. frontier progress. Positive means the policy closes the U.S. lead; negative means it widens it. A single signed number is reported for every individual policy and every bundle.

Let q be a common capability scale, and let v be baseline annual U.S. progress on that scale. The endpoint effect is:

`closure_days = 365.25 × [(q_US,baseline − q_US,policy) − (q_CN,baseline − q_CN,policy)] / v`

This fixed-horizon capability-gap measure avoids mixing different capability targets or country-specific time rulers. It differs from an unconditional forecast of how soon China will catch up. The main estimand is technical capability possessed by leading domestic AI developers, including privately trained models; release restrictions affect it through research inputs, diffusion, feedback, and financing, rather than automatically moving technical capability one-for-one. Restricting routine internal use of a newly trained model affects research through the incremental productivity of that model over its still-usable predecessor.

## Counterfactual and implementation

All policies are evaluated at 2026 technical conditions against otherwise identical voluntary practices without the specified obligation. Existing hardware, trained weights and knowledge are held fixed at implementation. Thus export controls compare maintaining the specified restriction with relaxing it prospectively; they do not claim the entire historical effect of all controls. Bill simulations use the frozen specification recorded in the AI Safety Menu on September24, rather than silently substituting an amended law. These counterfactual policy comparisons are not estimates of an enactment's observed historical causal effect.

The one-year clock begins when the policy becomes operative. Operational adaptation, implementation costs and research consequences during that year enter the calculation. Future statutory commencement dates do not shorten the common exposure window. A universal pause and a unilateral pause are distinct interventions and are priced separately where specified.

## What a best estimate means here

The headline is the arithmetic mean over documented parameter and structural uncertainty. This minimizes expected squared error in days, and naturally includes low-probability large effects. The model is calibrated to published observations where available. Missing causal parameters receive explicit analyst priors; they are never relabeled as observed effects or fitted posteriors. The uncertainty range is a model-uncertainty interval, not a frequentist confidence interval or a claim that the model contains every possible future.

Parameters are selected from mechanisms and evidence before reading final policy rankings. Computation, simulation precision, empirical calibration, and causal identification are different checks. A large simulation cannot compensate for weak evidence. The info pages identify the assumptions that dominate each result while retaining the required point estimate.

## Shared models

1. Evaluation schedules and shared capacity determine incremental internal-use and public-release delays. Work overlaps; a release window is not multiplied by every annual release.
2. Compute and data affect production levels; human/AI research resources affect algorithmic progress dynamically. Feedback and diminishing returns are modeled explicitly.
3. Chinese capability responds to domestic inputs and lagged U.S. research/model access. One common diffusion model prevents independent full credits for overlapping access channels.
4. Security controls reduce conditional compromise hazards and asset usability; their benefits share the same underlying risk. Research friction and talent effects enter separately.
5. Bundles reuse tasks and impose gates jointly. Standalone prices are not additive package estimates.

The run produces a machine-readable input ledger, empirical reference tables, reusable code, point estimates, sensitivity results, and one replacement info page per policy. No interviews or training experiments are represented as having occurred.

## Production, feedback and the progress ruler

The computational capability coordinate is log effective compute. Let `g_C` be annual log growth of physical frontier-training compute and `g_A` annual algorithmic efficiency growth. The baseline technical frontier grows at `g = g_C + g_A`. A policy supplies a direct log-capability shock `c(t)` and an aggregate research-input ratio `r(t)`.

The algorithmic deviation `a(t)` obeys:

```
da/dt = g_A * { exp[lambda_R*log(r)
                   + lambda_R*eta*(a + c + incoming_spillover)
                   - beta*a] - 1 }
beta = lambda_R*g_R/g_A
r = labor_ratio^labor_share * experimental_compute_ratio^(1-labor_share)
```

This is a relative-path version of an idea-production model with diminishing returns and AI-assisted research. It compares the policy path with a growing baseline. It does not apply an arbitrary `1/(1-feedback)` multiplier to every delay. The shared calibration is informed by [the economics of recursive self-improvement](https://arxiv.org/abs/2609.15802) and [research on compute slowdowns](https://arxiv.org/abs/2511.19492). The transport ranges remain analyst priors.

The main growth priors are triangular distributions on annual log growth: physical compute `log(2), log(4.5), log(8)`; algorithmic efficiency `log(1.5), log(3.5), log(10)`; research inputs `log(2), log(3), log(5)`. Research-flow elasticity is `0.3, 0.7, 1.0`; the response of research productivity to log effective compute is `0.05, 0.25, 0.60`. The exact ledger in `model/production-calibration.json` is authoritative. Both countries use this common technology and research-return calibration; a separate Chinese idea-production function has not been estimated. This is a transport assumption, not a claim of identical observed national growth rates.

A descriptive OLS fit to Epoch’s published 13-model reasoning-frontier table gives **14.1827 ECI points per year**, with seven expanding-window holdouts averaging **1.1300 ECI points absolute error**. This is a frozen September 1 publication whose table ends June 9, 2026, not a newly downloaded live frontier. [Epoch table](https://epoch.ai/data-insights/eci-frontier-trend).

The ECI fit is a **crosscheck and optional display normalization**. It does not identify the policy effects or fit the main growth priors. A linear conversion of both capability shocks and the progress ruler cancels in the headline ratio. At modal growth the implied conversion is 5.12 ECI per log effective compute. Imposing the separate RSI calibration of 6.5 and dividing by the observed ECI slope is a different measurement assumption; the sensitivity table reports it explicitly. We do not claim both mappings hold simultaneously.

## Internal use, release and training

A new model may exist before its routine internal use or public release is allowed. The headline counts its technical capability as part of the frontier. An internal-use gate therefore reduces research productivity by:

```
newest_model_labor_loss = min(1, gate_days/model_generation_days)
                         * research_work_exposure
                         * incremental_uplift/(1+incremental_uplift)
```

This same rule applies whether the gate appears alone or inside a broader obligation. Existing models remain usable. Actual suspended research activity and blocked future training are separate production losses. Public-release restrictions affect foreign model access; they do not automatically erase a trained U.S. model.

Evaluation windows use a clustered empirical mixture of access runways plus explicit transport uncertainty. Final-checkpoint resets and evaluator queues are separate inputs. Annual audit events are not multiplied by the number of releases. The main paths approximate an annual release hold’s effect on the stream of public models by its cycle-average delay; the supplied dated-window helper demonstrates the exact mask for an individual schedule. This is not a full discrete national launch simulator.

Only serial stages on a critical training chain accumulate training-gate losses. Qualifying parallel runs affect compliance workload. Existing outputs and already-running training pipelines are preserved with an explicit 30/90/180-day first-output-effect prior. Eligible exposure, raw waiting and work preserved during waiting enter once each. At long horizons this flow approximation assumes no separate catch-up unless the policy model specifies it.

## Country spillovers

Public research and frontier teachers have separate gross shares of Chinese algorithmic knowledge additions. Each is reduced by an explicit substitution-recovery fraction, then scaled by algorithmic progress’s share of total progress. For example:

```
phi_teacher = (g_A/g) * teacher_share * (1-substitution_recovery)
China_spillover_target(t) = (phi_research+phi_teacher)*US_shock(t-lag)
                           - phi_teacher*g*public_release_delay(t-lag)/365.25
```

A first-order absorption filter approaches this target. The disclosure lag represents time until a relevant private U.S. advance enters the accessible stream; absorption represents subsequent assimilation. The absorption constant is weighted from the research and teacher channels. A smaller reverse channel transmits Chinese losses or gains to U.S. research. These elasticities are assumptions, not a regression of national capabilities.

The same teacher-reliance draw prices anti-distillation. If that reliance is zero, the China-side benefit of withholding teachers is exactly zero. It is not assigned an independent full benefit elsewhere. Incoming spillovers feed research productivity in both countries. A fixed-point iteration solves this interaction to a maximum trajectory change below **0.001 progress-equivalent day**; failure to converge raises an error.

## Hardware, security, data and bundles

Export controls use a partial-equilibrium stock-and-flow counterfactual: the initial usable stock remains, additional purchases after relaxation arrive with deployment lag, and only the share relevant to frontier work affects capability. The model includes redirected supply and a supplier-innovation offset. It does not infer model delay directly from a chip-generation lag, and it is not a fitted global semiconductor general-equilibrium model. Beyond year one, a stated exponential stock/supply scenario replaces a falsely constant annual number of days.

Security controls thin remote, insider and other compromise hazards. Expected retained benefit integrates the timing of the most recent useful theft, absorption and the subsequent decay of a stolen asset’s advantage. This avoids an artifact in which preventing an early theft makes a later theft appear more valuable. Benefits are bounded by the recoverable frontier gap. Overlapping controls share the same underlying hazard; research friction and talent migration enter separately.

Data licensing changes quality-adjusted unique data, supports substitution and repeated epochs, and reoptimizes normalized parameter/data allocation at fixed training compute using a published data-constrained scaling function. Licensing-budget and transition effects are separate. The fitted small-model scaling constants are empirical; their applicability to the 2026 frontier is unvalidated.

Bundles take unions of work and expectations of the maximum of shared gates. `E[max(X,Y)]` is computed over explicit conditional event outcomes; it is not replaced by `max(E[X],E[Y])`. Distinct residual gate events are conditionally independent given shared parameters. Actual calendar correlation, regulator congestion across all labs, and national frontier replacement remain structural limitations.

## Interpretation of uncertainty and validation

The reported 5th–95th percentiles describe uncertainty over stated parameters in conditional expected outcomes. Rare-event probabilities, including compromise or a binding review, are integrated inside each draw. These percentiles are **not** the range of all realized future policy histories, a posterior fitted to policy outcomes, or a confidence interval.

The artifact validates zero-effect and sign limits, unchanged-input paths, declining marginal research returns, shared-teacher zero reliance, security overlap, positive compute stocks, bundle recurrence, reproducibility, feedback convergence, Monte Carlo precision and time-step refinement. Those tests verify implementation and internal consistency. They cannot establish the truth of the priors or rule out omitted mechanisms.
