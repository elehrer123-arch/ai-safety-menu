# Know-your-customer rules for compute providers

**Best estimate: -1.58 days of U.S. lead closed, 12 months after implementation.**

Positive closes the U.S. lead; negative widens it. The 90% parameter-uncertainty range is -4.5 to -0.12 days. This is a calibrated model estimate, not an identified causal effect.

## Intervention and counterfactual

Cloud companies must check the identity of any customer renting enough computing power to train a frontier model.

Additional identity, recordkeeping and intent checks above the covered scale versus existing cloud screening. Primary case includes enforcement of already-applicable restrictions when new identification reveals ineligible access; identity-only sensitivity sets denial_after_detection=0.

## Research and calculation

The base case allows new identity checks to uncover access prohibited by existing rules. Identity verification alone does not deny compute: the zero-denial boundary has zero China hardware benefit. This scope is narrower than a new blanket compute embargo.

Reporting-only produces zero China resource loss. Export controls and KYC use a common covered-compute stock; combine denials as surviving access, never add the same blocked GPU-hours twice.

The common country model uses technical capability, including nonpublic trained models. The calculation below expresses capability changes in days on the same baseline U.S. progress ruler.

| Channel at month 12 | Equivalent days |
|---|---:|
| U.S. direct production restriction or gain | +0.052 |
| U.S. accumulated research effect | +0.021 |
| U.S. response to Chinese changes | +0.059 |
| **Total U.S. capability loss** | **+0.13** |
| China direct compute/access/security effect | +1.30 |
| China accumulated research effect | +0.41 |
| China response to U.S. changes | +0.009 |
| **Total Chinese capability loss** | **+1.72** |
| **U.S. loss minus Chinese loss** | **-1.58** |

Negative country losses mean a capability gain. Components are expectations from the same draws; rounding can prevent exact visible summation.

### Policy mechanism

```
cn_compute_loss_fraction=cn_covered_cloud_compute_share*incremental_detection*denial_after_detection*(1-replacement_share)*rollout_fraction_year
us_compute_loss_fraction=us_new_contract_exposure*check_elapsed_days*blocking_fraction/365
```

The executable model is authoritative where these intermediate formulas use an average-year approximation. In particular, export controls use the positive stock trajectories in `china_paths`, and security uses the most-recent-compromise calculation. See the [common equations](../METHOD.md).

## Evidence and priors

The following input ranges are triangular scenario supports, not published confidence bounds. “Calibrated” means a published observation anchors part of the choice; it does not make the transported policy effect empirical. A policy constant is fixed. Shared growth, research, diffusion and security inputs are documented in the [model ledgers](../model/) and [method](../METHOD.md).

| Input | Low / mode / high | Units | Evidence status | Why it enters |
|---|---|---|---|---|
| China covered cloud compute share | 0.01 / 0.1 / 0.3 | fraction of China-relevant frontier compute rented through newly affected providers/resellers | analyst prior | Unobserved; modest mode because domestic compute is substantial, upper allows material offshore frontier use. |
| incremental detection | 0.05 / 0.35 / 0.7 | fraction of otherwise hidden ineligible compute access newly identified | analyst prior | Mandate improves on current screening; high-volume use is observable but identity evasion persists. |
| denial after detection | 0 / 0.5 / 0.9 | probability that newly identified covered use is actually restricted | analyst prior | Explicit action assumption. KYC itself creates no prohibition. Half-mode includes already-ineligible customers; not all identified foreign users are forbidden. |
| replacement share | 0.25 / 0.6 / 0.95 | fraction of denied relevant compute replaced elsewhere within horizon | analyst prior | Alternative providers, domestic capacity and evasion offset denials; complete substitution retained near upper bound. |
| rollout fraction year | 0.25 / 0.75 / 1 | fraction of first-year exposure after implementation | analyst prior | Coverage phases in rather than full-year instantaneous denial. |
| U.S. new contract exposure | 0.05 / 0.2 / 0.5 | fraction of U.S. compute provisioning newly checked | analyst prior | Large labs are already identified; burden mainly extensions/new contracts. |
| check elapsed days | 0.1 / 1 / 7 | calendar days per exposed provisioning | analyst prior | Incremental documentation can complete quickly for known major customers, but tail accommodates exceptions. |
| blocking fraction | 0 / 0.1 / 0.5 | fraction of elapsed check that blocks usable compute | analyst prior | Most work asynchronous with provisioning. |

Relevant primary evidence (the linked evidence register records the finding and its limits):

- [Oversight for Frontier AI through a Know-Your-Customer Scheme for Compute Providers](../sources.md#china-egan_heim_2023) — [original source](https://arxiv.org/abs/2310.13625).
- [Introducing the AI Chip Owners Explorer](../sources.md#china-epoch_owners_2026) — [original source](https://epoch.ai/latest/introducing-the-ai-chip-owners-explorer).

## Sensitivity and interpretation

| Scenario | Lead closed at month 12, days |
|---|---:|
| Main estimate | -1.58 |
| No marginal U.S.-to-China research/teacher reliance | -1.57 |
| Half the marginal U.S.-to-China reliance | -1.58 |
| Twice the marginal U.S.-to-China reliance | -1.59 |
| No incremental AI-assisted research feedback | -1.40 |
| No China-to-U.S. research response | -1.64 |
| Alternative fixed 6.5 ECI/log-compute and observed ruler | -1.95 |

| Endpoint | Lead closed, days |
|---|---:|
| 6 months | -1.15 |
| 12 months | -1.58 |
| 36 months | -2.2 |

The 36-month column extends stated assumptions; it is not another independently calibrated forecast. Effects need not grow linearly. The alternative ECI ruler changes the measurement assumption and is not the headline metric.

Largest sampled associations with the result (diagnostic correlations, not causal importance estimates): China covered cloud compute share (r=-0.50), denial after detection (r=-0.45), incremental detection (r=-0.40).

Monte Carlo standard error of the numerical mean: 0.0166 days. This is simulation error, not substantive uncertainty. Run: 8,192 shared parameter draws, seed 260925, weekly paths with finer-step verification.

[Back to estimates](../index.html) · [Full method](../METHOD.md) · [Reproducible notebook](../policy-model.ipynb)
