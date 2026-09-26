# AI Safety Menu: 12-month lead estimates

This package supplies one signed estimate for each of the 27 policies and eight bundles in the September 24, 2026 menu, with replacement research pages and a reproducible model. Estimates measure how much a policy changes the U.S.–China capability gap **12 months after implementation**, expressed in days of baseline U.S. frontier progress.

**Positive closes the U.S. lead; negative widens it.** The point estimate is the arithmetic mean over disclosed parameter uncertainty. Zero is a numerical estimate, including rounding of negligible effects. These are calibrated structural estimates; none is presented as an experimentally identified causal policy effect.

Open **[the research pages](index.html)** to browse the results. The same numbers are in [CSV](policy-estimates.csv) and [JSON](policy-estimates.json). The [executed notebook](policy-model.ipynb) and its [HTML export](policy-model.html) show the empirical calibration, calculations, checks and sensitivity results. [METHOD.md](METHOD.md) defines the common estimand and the model equations.

## What was completed

- A consistent production-and-diffusion model translates compute, research resources, training gates, data constraints, release access and security into a common endpoint measure.
- An evaluation-process dataset records eight models in six release campaigns. Dates that were not published remain missing; testing duration, first access, final checkpoint access and release are distinct.
- A published 13-model reasoning-frontier series provides an empirical capability progress ruler. Expanding-window holdouts check the descriptive trend; they do not validate causal policy effects.
- Recent primary research and lab measurements inform the production model, including diminishing returns to research, AI-assisted research feedback, scale-dependent experiments, compute substitution and data-constrained scaling.
- Every policy has a numerical estimate, a decomposition, explicit priors, primary-source links and sensitivity results. Bundles share obligations and gates.

## What the evidence does and does not establish

The model replaces unsupported guesses about final numbers with specified mechanisms and inspectable assumptions. Most policy-specific causal elasticities remain judgment-based. Public release cases are selected completed launches; they do not contain the unobserved launch dates absent regulation. One-lab compute allocation or productivity measurements do not identify national averages. Theft rates, China’s marginal reliance on U.S. teachers, purchases after export-control relaxation, and the productivity cost of secure environments are especially consequential priors.

The national frontier is represented by a broadly covered leading-developer production path. This is not a fitted competition model taking the maximum across several labs. Heterogeneous compliance and substitution by a less-affected frontier lab remain structural uncertainty. The 36-month results extend the stated mechanisms and hold post-year-one inputs fixed where specified; they are sensitivity scenarios, not a separate long-run forecast.

Safety, welfare, catastrophic-risk reduction and the desirability of each policy are outside the headline measure. A policy can be worthwhile even if it closes the U.S. lead, or undesirable even if it widens it.

## Reproduce

Use Python 3 with NumPy, pandas, matplotlib, nbformat and nbclient. No paid API, private dataset or network call is needed to run the delivered model.

```sh
cd model
python unified_model.py --n 8192 --seed 260925 --steps 52
python validate_unified.py
python validate_production_model.py
```

Run the notebook from the package directory to regenerate the complete review. Input ledgers and model modules are under `model/`; primary publication links and locators are preserved in those ledgers. `source-snapshot.json` preserves the exact policy definitions used.

## Integration

Use the `lead_closure_days` field in `policy-estimates.json` as the new headline value, and the corresponding `info/<policy_id>.md` as its backing text. `lead_closure_days_unrounded` preserves the simulation mean; displayed precision is deliberately coarser than the calculation.

These estimates already include the modeled China response. Applying the old menu’s independent China-dependence multiplier or theft pool again would double-count it. Each bundle has its own combined estimate; do not sum its component headlines. Arbitrary baskets need the same joint model and an explicit overlap map. This package does not supply a validated price for every possible basket.

The existing website has not been published over. The research pages and integration payload are ready for review; adopting the new metric also requires replacing the old price formula and its assumption controls.
