# Production-side calibration for six AI Safety Menu policies

Prepared September 25, 2026. This supplies local frontier effects for the main country-comparison model. **The resulting numbers are conditional model estimates informed by public evidence and explicit priors, not measured causal policy effects.** No policy-day value from the menu was used as a target. Every numerical input, distribution, evidence classification and rationale is in `production-calibration.json`; the builder preserves provenance and can regenerate it.

## Contract and numerical output

The headline horizon is the first 12 months after implementation. A model year is 365.25 days; the pause lasts exactly half a year. The counterfactual includes the same voluntary testing, safety allocation, human review and existing restrictions without the additional hypothetical mandate. The policy effect is measured at the horizon, rather than charging every waiting period as an equal loss of frontier progress.

The module supplies the U.S. production effect before China spillovers or additional national coverage adjustments. With `x` denoting log effective compute and `g = g_C + g_A`, its local progress-equivalent deficit is

`local_days(T) = -365.25 * [x_policy(T)-x_baseline(T)] / g`.

The parent can map these paths into its 14.183 ECI/year descriptive baseline using `ECI_delta(t)=14.183*x_delta(t)/g`, then calculate the difference between the U.S. and Chinese effects on that same U.S. ruler. **The table below is not yet the amount by which the U.S.–China gap closes.** Nor is it an exact hitting-time delay, which differs when slopes change.

Results: 20,000 paired draws, seed 260925, weekly grid, midpoint integration with substeps no longer than half a week. The chosen best estimate is the arithmetic expectation of each draw's endpoint ratio. The displayed 10th–90th percentiles describe these specified priors, not a frequentist confidence interval or exhaustive structural uncertainty.

| Policy | Local first-year mean days | Median | 10th–90th percentile | Local year-three mean days |
|---|---:|---:|---:|---:|
| One-third safety budget | 35.49 | 35.12 | 15.92–55.39 | 55.34 |
| Safety checks before internal use | 1.22 | 0.95 | 0.30–2.50 | 2.61 |
| Human sign-off on automated research | 4.17 | 3.63 | 1.60–7.44 | 13.29 |
| Permanent training-compute cap | 127.52 | 126.27 | 87.16–169.35 | 458.88 |
| Six-month training pause | 50.57 | 49.02 | 29.88–73.29 | 18.21 |
| Training-data consent/licensing | 30.02 | 28.03 | 16.09–46.25 | 38.25 |

Three-year outputs are a sensitivity: all common growth parameters stay fixed, the cap remains fixed, autonomy adoption freezes at its year-one level, and the pause expires after six months. Its direct gap then continues recovering exponentially. A constant safety/data input-level penalty is not subtracted again each year; its separate research consequences accumulate dynamically.

## Shared production and research model

Baseline raw training compute grows at `g_C`, algorithmic efficiency at `g_A`, and effective research inputs at `g_R`. Let `c(t)` be a direct log compute-equivalent policy shock, `a(t)=log(A_policy/A_baseline)`, and `r(t)` the policy-to-baseline ratio of effective research effort. The policy path is

`x_policy(t) = (g_C+g_A)*t + c(t) + a(t)`

`da/dt = g_A * {exp[lambda_R*(log r(t)+eta*(a(t)+c(t))) - beta*a(t)] - 1}`

`beta = lambda_R*g_R/g_A`.

This is a normalized idea-production model with diminishing research returns and endogenous model assistance. The beta identity imposes a balanced-growth normalization; beta is derived, not independently measured. The feedback elasticity applies to deviations from the baseline, whose forecast already includes baseline AI assistance. This avoids adding an extra baseline feedback growth term. No instantaneous `1/(1-feedback)` multiplier is used.

The resource aggregate allocates a labor elasticity `l` and an experimental-compute elasticity `1-l`: a cognitive labor ratio `r_L` produces `r=r_L^l`, while experimental compute ratio `r_E` produces `r=r_E^(1-l)`. For proportional reallocations, the same fraction can affect both the final-training bundle and the distinct non-final-training research bundle. Those are separate production inputs, not a second subtraction of the same dollar cost. Their actual allocation is an important sensitivity.

| Shared input | Triangular low / mode / high | Status and interpretation |
|---|---|---|
| Raw compute log growth, yearly | ln 2 / ln 4.5 / ln 8 | Historical training trend calibrates mode; future bounds are judgment. |
| Algorithmic log growth, yearly | ln 1.5 / 1.265 / ln 10 | Recent compute-slowdown paper anchors mode; contains data and recipe improvement already. |
| Research input log growth, yearly | ln 2 / ln 3 / ln 5 | RSI calibration anchor, broadly transported to current conditions. |
| Research flow elasticity `lambda_R` | 0.30 / 0.70 / 1.00 | Analyst prior; not identified by the sources. |
| Research labor elasticity `l` | 0.35 / 0.67 / 0.90 | Weak published labor-exponent anchor, broad structural range. |
| Feedback elasticity `eta` | 0.05 / 0.25 / 0.60 | Analyst prior for whole research effort versus effective-compute capability. |

The feedback upper bound is informed by the RSI paper's rough labor-productivity/ECI slope (about 0.09) multiplied by its effective-compute/ECI conversion (about 6.5), yielding about 0.585. That calculation is an uncertain labor-task proxy, not an estimate of aggregate research feedback. The central value discounts self-report, bottlenecks and research-compute costs. The 6.5 conversion is used only as a weak prior anchor; the parent's fixed ECI ruler controls final normalization.

Common parameter draws are shared across policies. Marginal priors are otherwise independent; correlated adoption, compute and algorithmic-growth uncertainty is not fitted. This particularly limits strong claims from three-year tails.

## Six policy mechanisms and assumptions

Notation below: `Tri(low,mode,high)`. All omitted factual precision is supplied as an explicit prior in the JSON, never silently replaced by certainty.

### One-third of research budgets on safety

**Replacement for the menu's repeated annual compute charge:** a persistent input-level shift plus its evolving research effect. The effective ratio is `r=(1+b)*(1-s1+k*s1)/(1-s0+k*s0)`, where `s1=1/3`, `s0=Tri(.03,.06,.15)`, safety's capability co-benefit `k=Tri(0,.15,.4)`, and additional total budget `b=Tri(0,.08,.25)`. Implementation ramps over `Tri(0,90,180)` days. Set `c=ramp*log r` and research ratio `exp(c)`.

Anthropic now reports a roughly 6% AI-R&D compute safety share and roughly 12% within AI-driven AI R&D. The conservative labeling excludes equally dual-use work. That is useful evidence but is one lab and one week; it does not directly measure all compensation or the statutory budget definition. The menu's claim that no lab publishes a share is outdated. The proportional spending mix, budget response and safety-to-capability contribution remain analyst assumptions.

At all other parameter modes, complete capability-input offset requires **32.4%** budget expansion. Moving budget expansion from 0% to 8% to 25% produces local year-one effects of 63.55, 46.52 and 13.37 days at other modes. The joint expectation is different from evaluating all parameter modes. This model does not monetize reduced accident risk or the value of safety research itself.

### Safety checks before internal use

**Replacement for charging the full test duration per generation:** foregone incremental productivity while the preceding model remains available. With gate `d=Tri(0,7,21)` days, generation interval `G=Tri(30,60,120)`, exposed work `e=Tri(.4,.7,1)` and newest-versus-previous uplift `u=Tri(.05,.2,.6)`, cognitive labor loss is `f=min(1,d/G)*e*u/(1+u)`. Set `r=(1-ramp*f)^l`; there is no direct training or public-release stop. Ramp is `Tri(0,30,90)` days.

AISI's one-to-two-week evaluation tier informs elapsed duration. Existing safeguards, earlier checkpoints and overlapping tests justify an incremental range starting at zero. OpenAI's recent internal restriction also shows substantial compute redeployment; it cannot establish equivalent output recovery. Anthropic's reported roughly fourfold uplift versus no AI does not identify the needed newest-versus-previous uplift.

At other modes, raising that incremental uplift from .05 to .20 to .60 moves local first-year effect from 0.23 to 0.80 to 1.81 days. The small result is conditional on productive fallback, moderate model increments and gates measured against current voluntary practice. It would fail if only the newest model can execute a crucial research bottleneck; that requires a separate threshold model or a much larger incremental-uplift scenario.

### Human sign-off on automated AI research

**Replacement for assuming one-third of a generic AI uplift disappears:** an incremental approval queue plus prospective fully autonomous task chains. Anthropic's August AI-leads share anchors `Tri(.15,.26,.4)` initially; the end-year prior is `Tri(.3,.55,.8)`. Measured fully autonomous research starts at zero and grows to `Tri(0,.1,.4)` at year end. Shares are disjoint. These task shares proxy cognitive effort shares, an unverified mapping.

For AI-led chains, only `Tri(.1,.4,.8)` receive an additional checkpoint beyond voluntary practice. Queue-plus-service time is `review=service/(1-utilization)+handoff`, with service hours `Tri(.05,.25,1)`, utilization `Tri(.3,.65,.9)` and handoff hours `Tri(.05,.2,1)`. Throughput loss is `review/(cycle+review)`, with cycle hours `Tri(2,6,24)`. Fully autonomous chains lose an incremental autonomy uplift `Tri(.2,.5,2)/(1+uplift)`. Apply the shared labor elasticity and a `Tri(0,30,90)`-day ramp.

OpenAI reports human intervention in more than half of successful four-to-eight-hour tasks. This makes existing human oversight material to the counterfactual. The M/M/1 expression is a transparent congestion approximation, not a fitted lab queue; approval means meaningful experiments/chains, not every tool invocation. At other modes, utilization .30/.65/.90 gives 1.96/2.44/4.28 local days. Adoption, checkpoint granularity and the value of uninterrupted task chains remain the dominant priors.

### Fixed training-compute cap

**Replacement for an historical compute-plus-data attribution percentage:** a binding per-run constraint, explicit substitution and remaining experimental bottlenecks. Set `gap=max(0,g_C*t-headroom)*compliance`, with log headroom `Tri(0,0,.4)` and compliance `Tri(.85,.97,1)`. Direct shock is `c=-(1-recovery)*gap`, with other-channel recovery `Tri(.05,.25,.6)`. Experimental resource ratio is `1-share*(1-exp(-gap))*(1-redeploy*value)`, raised to `1-l`; frontier-scale-dependent experiment share is `Tri(.1,.35,.7)`, redeployment `Tri(.5,.85,.98)` and relative substitute value `Tri(.2,.6,.95)`.

Epoch's estimate that final training consumed only about 10% of OpenAI's 2024 R&D compute prevents equating a per-run cap with freezing all research. Algorithmic scale dependence prevents assuming all remaining research is unaffected. OpenAI's roughly 85% short-run compute redeployment is an anchor for quantity, explicitly not equivalent research value.

At other modes, direct-gap recovery 0/.25/.60 gives 211.71/159.65/86.55 local first-year days. With both direct substitution and experimental redeployment removed, the 1,500-draw paired validation mean rises to 183.12 days. The policy is a fixed ceiling on run compute, not an inference prohibition or a national compute-stock freeze.

### Six-month pause

**Replacement for charging six months at the year-one endpoint:** accumulate a scaling deficit during the pause and allow post-expiry catch-up. Permitted work replaces `Tri(.05,.25,.5)` of raw scaling progress. While paused, research-compute share `Tri(.2,.5,.8)` is affected, with redeployment and value priors as above. That research resource shock expires at six months.

Let `P=.5` years and catch-up fraction `h=Tri(0,.5,.9)`. The direct shock is `-g_C*min(t,P)*(1-offset)*exp[-k*max(0,t-P)]`, with `k=-log(1-h)/(1-P)`. Thus the stipulated fraction of the six-month direct gap has been recovered by year one. Research lost during the pause is integrated separately; algorithmic recovery need not equal direct catch-up. Three-year exponential recovery is a conditional extrapolation.

At other modes, 0%/50%/90% catch-up gives 87.55/48.35/16.19 local year-one days. No empirical six-month-pause study identifies this catch-up fraction. Hardware accumulation, saved recipes and permitted research motivate a broad prior. The menu's pricing explicitly assumes China does not pause, despite the letter advocating universal participation. The parent handles unilateral pricing and universal-compliance sensitivity; equal raw interruptions need not imply equal effects when baseline growth and spillovers differ.

### Consent/licensing for training data

**Replacement for a flat month of presumed retraining:** quality-adjusted corpus substitution, a data-constrained optimized recipe, recurring licensing costs, and a distinct temporary transition. Unique data ratio is `v=1-m+m*r*q`, with newly permissioned share `m=Tri(.3,.6,.9)`, retained/licensed/replaced share `r=Tri(.2,.65,.95)` and replacement quality `q=Tri(.75,.95,1.1)`. Baseline passes through unique data are `Tri(1,2,4)`.

Muennighoff et al.'s fitted saturation functions are used for both repeated data and excess parameters. Their `R_D=15.3878`, `R_N=5.3097` and exponent approximately .353 anchor broadened priors `Tri(5,15.3878,30)`, `Tri(2,5.3097,12)` and `Tri(.28,.353,.42)`. Optimize normalized `N*D=1`; convert the reducible loss ratio to log compute equivalent using `-(2/alpha)*log(L_policy/L_base)`. Only `Tri(.4,.7,1)` of this penalty reaches the target downstream frontier.

The code uses the same normalized unique bound for parameter and data saturation **by construction, not by equating their physical units**. Under equal exponents, the paper's coefficients imply `N*/D*=(521/1488)^(1/.353)=.051154`, close to its `U_N=.051 U_D`. Normalize `N` by `N*` and `D` by `D*`; then `U_N/N*≈U_D/D*`. Equal coefficients in normalized reducible loss follow from the compute-optimal first-order condition. This abstraction omits unequal exponents and the irreducible 1.87 loss term; that term cancels when matching reducible-loss compute equivalents, but cannot simply be included in their ratio.

The paper fits 182 runs from a broader 400-run project, up to 9B parameters; transport to a 2026 frontier model is uncertain. Common Pile's licensed 8TB corpus and budget-matched 7B results establish credible substitutes, not frontier parity. Proprietary present-day corpus composition is unavailable.

Incremental licensing/provenance cost is `Tri(0,.02,.08)` of budget. Preparation takes `Tri(7,30,90)` days, of which `Tri(.1,.35,.8)` lies on the critical path; `Tri(.1,.5,1)` of that one-time gap remains at year one. The code ramps the data/budget effect, adds the temporary scheduling gap, and then holds its year-one residual for the three-year sensitivity. It assumes no retroactive destruction or retraining requirement. At other modes, affected-data recovery .20/.65/.95 gives 31.09/17.24/12.53 local first-year days. Corpus access, transition overlap and downstream dependence remain judgment inputs.

## National exposure and model boundary

These equations model a representative frontier-producing laboratory. Applying them to the U.S. national frontier assumes the marginal leading lab and its plausible replacements face similar effective requirements. That assumption is plausible for a uniform domestic compute ceiling but less automatic for heterogeneous safety baselines, licensing exposure and evaluation procedures. `binding_compliance` for the cap is a within-policy effective constraint parameter, not an empirically fitted max-of-labs correction.

A true national model would calculate `q_US(t)=max_l q_l(t)` with lab-specific baseline capability, policy exposure, schedules and substitution. A runner-up that is nearly as strong and less exposed can replace the constrained leader; national losses can therefore be smaller than the representative-lab estimate. Conversely, common inputs, synchronized release cycles or scarce reviewers can make losses correlated. Neither an unestimated linear coverage haircut nor a national portfolio effect is hidden in this module. The parent should identify any applied coverage prior explicitly. Relocation, international policy response, security benefits and accident risk are outside this local production module.

The six policies are standalone counterfactuals. Adding their log losses without applying them jointly would overcount overlapping resource constraints, repeated evaluation work or the same compute prohibition. This module also does not claim a point estimate for welfare, safety value or the probability of an intelligence explosion.

## Primary evidence and source limits

Exact page/section locators and extracted facts are included in the JSON. Locally inspected PDFs/text are in `sources/`.

- [Cunningham et al., The Economics of Recursive Self-Improvement, September 14, 2026](https://arxiv.org/abs/2609.15802): production framework and rough growth/productivity calibration; does not estimate these policy effects.
- [Whitfill, Snodin and Becker, Forecasting AI Time Horizon Under Compute Slowdowns, November 23, 2025](https://arxiv.org/abs/2511.19492): algorithmic log-growth estimate 1.265/year and broad interval .667–3.614; explicitly compute-bottleneck structure, not proof against software-driven acceleration.
- [Anthropic, Measurements for understanding the pace of AI development inside frontier labs, September 2026](https://www.anthropic.com/institute/measuring-pace-of-ai-development): compute allocation and classified autonomy measurements; one-lab transport limitations.
- [OpenAI, Research acceleration: The view inside OpenAI, September 6, 2026](https://openai.com/index/research-acceleration-view-inside-openai/): revealed response to internal restrictions and existing oversight; redeployment is not measured causal productivity recovery.
- [Anthropic, When AI builds itself, June 2026; updated September 18](https://www.anthropic.com/institute/recursive-self-improvement): self-reported productivity and human bottlenecks; not a randomized lab-output study.
- [Epoch, Training compute of frontier AI models grows by 4–5x per year, May 28, 2024](https://epoch.ai/publications/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year), [algorithmic progress discussion, February 25, 2026](https://epoch.ai/gradient-updates/the-least-understood-driver-of-ai-progress), and [R&D versus final-run compute, March 23, 2026](https://epoch.ai/gradient-updates/r-and-d-vs-training-compute): distinct historical inputs and structural context, not independent experimental policy elasticities.
- [Gundlach et al., On the Origin of Algorithmic Progress in AI, November 26, 2025](https://arxiv.org/abs/2511.21622): compute-scale dependence; no numerical current cap penalty supplied.
- [Demirer et al., Chaining Tasks, Redefining Work, June 14, 2026](https://arxiv.org/abs/2606.15960): task-chain mechanism; no measured frontier-lab queue parameters.
- [AISI, Early lessons from evaluating frontier AI systems, 2024](https://www.aisi.gov.uk/blog/early-lessons-from-evaluating-frontier-ai-systems): evaluation duration and overlap; not an incremental frontier delay.
- [Muennighoff et al., Scaling Data-Constrained Language Models, JMLR, February 2025](https://jmlr.org/papers/v26/24-1000.html): repeated-data/parameter saturation fit, PDF Appendix B Table 1 and Equation 18.
- [Kandpal et al., The Common Pile v0.1, June 5, 2025](https://arxiv.org/abs/2506.05209): controlled evidence for licensed-corpus substitutes at smaller scale.

## Reproduction and verification

```python
from production_model import simulate, integrate_resource_effect, summarize
r = simulate(n=20000, seed=260925, horizon_years=3, steps_per_year=52)
# r['times']: T years; r['shared']: N-vectors, including g_C, g_A, g_total,
# g_R, lambda_R, beta, eta, labor_share.
# Each r['policies'][id] includes N×T absolute log_effective_compute,
# log_effective_compute_effect, direct_log_effect, algorithmic_log_effect,
# resource_ratio, N-vector release_delay_days (zero here), parameters, diagnostics.
# Other policies can reuse exactly these common draws with:
a = integrate_resource_effect(r['shared'], r['times'], resource_ratio, direct_log_shock)
# Optional deterministic/scenario overrides:
z = simulate(n=1, use_modes=True, overrides={
    'shared': {'feedback_to_research': 0},
    'policies': {'pause-6': {'scale_gap_recovered_by_yearend': .9}}
})
```

Run `python3 build_production_calibration.py`, `python3 production_model.py --n 20000 --years 3 --steps 52`, and `python3 validate_production_model.py` from this directory. The last writes `production-validation.json`.

Validation passed for seeded reproducibility, shapes, finite trajectories, positive resources, component sums, zero-shock identity, zero research elasticity, no-loss data boundary, monotonic gains from more unique data, expired pause resource restrictions, cap without substitution, and feedback disabled. Weekly versus half-weekly first-year endpoint changes average below 0.045 day for every policy; the pause discontinuity has the largest maximum difference, 0.192 day. Refining the data optimization grid from 121 to 481 points changes implied log compute by at most .000282 on the checked range. These checks validate the implementation, not causal identification.

In 1,500 paired draws, switching feedback off gives local first-year means of 30.59 safety-budget days, 1.07 internal-gate days, 3.75 human-approval days, 117.54 compute-cap days, 41.58 pause days, and 25.01 data-licensing days. The full-model headline table uses 20,000 draws; differences should be compared using paired draws rather than treating these smaller-sample means as an exact decomposition.
