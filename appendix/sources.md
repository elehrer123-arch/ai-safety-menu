# Primary evidence and source boundaries

Published sources support the observations or mechanisms below. They do not estimate all policy-specific priors. Full input-to-source mappings are in the calibration JSON files.

<a id="production-rsi2026"></a>
## [Cunningham et al., The Economics of Recursive Self-Improvement](https://arxiv.org/abs/2609.15802)

Calibration uses algorithmic and research-input growth near ln(3)/year; approximately 6.5 ECI per log effective compute. Reported labor-task uplift implies a rough upper-ish 0.09 log productivity/ECI, explicitly uncertain; this is not aggregate R&D productivity.



Locator/date: PDF pp17-24,28-29.

<a id="production-slowdown2025"></a>
## [Whitfill, Snodin and Becker, Forecasting AI Time Horizon Under Compute Slowdowns](https://arxiv.org/abs/2511.19492)

Algorithmic log growth estimate 1.265/year, 95% interval .667-3.614. Appendix C cites labor exponent .67 and long-run research return .95; time-horizon/effective-compute exponent .454. Compute-bottleneck mechanism is assumed, not established by two model families.



Locator/date: Appendix C and G; Table1.

<a id="production-anthropic_allocation"></a>
## [Anthropic, Measurements for understanding the pace of AI development inside frontier labs](https://www.anthropic.com/institute/measuring-pace-of-ai-development)

July13-20: safety 6% of AI-R&D compute, 12% of AI-driven AI-R&D compute; conservative definition excludes equally dual-use work. August: AI leads26%, collaborates-or-higher>90%, measured fully autonomous0%. One-lab, one-week compute snapshot and model-assisted classification.



Locator/date: Sections1 and3; appendix.

<a id="production-openai_acceleration"></a>
## [OpenAI, Research acceleration: The view inside OpenAI](https://openai.com/index/research-acceleration-view-inside-openai/)

August7 model-specific restrictions: Astra-class GPU allocation fell59.2%; other classes rose17.2%, offsetting about85% of decline. July20 incident included two-week RL pause. Over half successful4-8h tasks already had human intervention. Redeployed compute does not measure recovered research value.



Locator/date: Sections1,3,4.

<a id="production-anthropic_uplift"></a>
## [Anthropic, When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement)

March survey of130 employees: median4x self-reported output with Mythos versus no AI; authors expect true uplift lower. Human review and research direction remain bottlenecks. This is not the incremental uplift of the newest versus previous model.



Locator/date: Evidence from within Anthropic; footnotes.

<a id="production-epoch_compute"></a>
## [Sevilla and Roldan, Training compute of frontier AI models grows by4-5x per year](https://epoch.ai/publications/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year)

Historical recommendation4-5x/year; frontier post2018 estimate4.2x,90%CI3.6-4.9; frontier language-model trend5x,90%CI3.1-7.3. Future range must allow structural breaks.



Locator/date: Introduction; frontier and leading-lab regressions.

<a id="production-epoch_software"></a>
## [Anson Ho, The least understood driver of AI progress](https://epoch.ai/gradient-updates/the-least-understood-driver-of-ai-progress)

Synthesizes mostly-pretraining estimates around3x,6x, and10x/year with very broad uncertainty; stresses data quality, distillation and scale dependence. Informal primary-author methodological discussion, not an additional independent sample.



Locator/date: Appendix table and scale-dependence discussion.

<a id="production-epoch_compute_share"></a>
## [Denain and Wu, Final training runs account for a minority of R&D compute spending](https://epoch.ai/gradient-updates/r-and-d-vs-training-compute)

OpenAI2024 estimate: about10% of R&D compute spend in final released-model training; remaining workloads include experiments and synthetic data. Final-run share is not the share of capability progress attributable to scale.



Locator/date: Main text and methods.

<a id="production-scale_dependence"></a>
## [Gundlach et al., On the Origin of Algorithmic Progress in AI](https://arxiv.org/abs/2511.21622)

Ablations and scaling experiments find substantial compute-scale dependence of algorithmic gains. Supports a nonzero cap/experiment bottleneck prior, not its numerical mode.



Locator/date: Abstract and scaling experiments.

<a id="production-chaining2026"></a>
## [Demirer et al., Chaining Tasks, Redefining Work](https://arxiv.org/abs/2606.15960)

Models nonlinear gains from contiguous AI task chains and handoff costs. Supplies mechanism, no frontier-lab service-time estimate.



Locator/date: Task-chain model.

<a id="production-aisi"></a>
## [AISI, Early lessons from evaluating frontier AI systems](https://www.aisi.gov.uk/blog/early-lessons-from-evaluating-frontier-ai-systems)

Standard evaluation tier can complete in1-2weeks; light tier QA/reporting1-2weeks. Elevated investigations may take longer; proxy models/preparation can overlap. These are durations, not incremental research delays.



Locator/date: Section4.

<a id="production-data_scaling"></a>
## [Muennighoff et al., Scaling Data-Constrained Language Models](https://jmlr.org/papers/v26/24-1000.html)

182-run parametric fit: repeated-token saturation R_D=15.3878, excess-parameter R_N=5.3097, exponents≈.353, fittedR2=.781. Full project400runs up to9B parameters. Transport to2026 frontier is unvalidated.



Locator/date: AppendixB Table1 Eq18; AppendixC.

<a id="production-commonpile"></a>
## [Kandpal et al., The Common Pile v0.1](https://arxiv.org/abs/2506.05209)

Openly licensed8TB corpus;7B models trained on1T/2Ttokens competitive with similarly budgeted Llama1/2. Establishes credible substitutes, not frontier parity or the fraction of present data licensable.



Locator/date: Sections4.3-4.4.

<a id="production-menu"></a>
## [AI Safety Menu policy definitions](https://elehrer123-arch.github.io/ai-safety-menu/#/)

Defines the six hypothetical requirements; prior menu prices are not used as calibration targets.



Locator/date: Backing info pages and local work/policy-audit/data.js.

<a id="regulation-met_o1"></a>
## [METR preliminary evaluation of o1-preview](https://metr.org/evaluations/openai-o1-preview-report/)

o1-preview access September 3 and o1-mini August 28; testing ended September 9, 2024. Earlier related checkpoint August 26. API throughput constrained.



Locator/date: 2026-09-24.

<a id="regulation-rel_o1"></a>
## [OpenAI introducing o1-preview](https://openai.com/index/introducing-openai-o1-preview/)

o1-preview and o1-mini first public release September 12, 2024.



Locator/date: 2026-09-24.

<a id="regulation-met_o3"></a>
## [METR preliminary evaluation of o3 and o4-mini](https://metr.org/evaluations/openai-o3-report/)

Earlier checkpoints supplied three weeks before release; no specific access start date or full evaluation/report timeline published here.



Locator/date: 2026-09-24.

<a id="regulation-rel_o3"></a>
## [OpenAI introducing o3 and o4-mini](https://openai.com/index/introducing-o3-and-o4-mini/)

Public release April 16, 2025.



Locator/date: 2026-09-24.

<a id="regulation-met_gpt5"></a>
## [METR evaluation of GPT-5](https://metr.org/evaluations/gpt-5-report/)

First checkpoint July 10; final launch checkpoint July 25; reasoning traces July 26; checklist answers July 29; preliminary report August 1, 2025. Four weeks of pre-release access versus three weeks of evaluation work.



Locator/date: 2026-09-24.

<a id="regulation-rel_gpt5"></a>
## [OpenAI introducing GPT-5](https://openai.com/index/introducing-gpt-5/)

Public release August 7, 2025.



Locator/date: 2026-09-24.

<a id="regulation-card_gpt55"></a>
## [GPT-5.5 System Card](https://deploymentsafety.openai.com/gpt-5-5)

SecureBio assessed two pre-release checkpoints April 2 through April 9, 2026. They differed from deployed version; final-version rerun was planned. High cyber classification with safeguards.



Locator/date: 2026-09-24.

<a id="regulation-rel_gpt55"></a>
## [OpenAI introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)

First product release April 23; API availability April 24, 2026.



Locator/date: 2026-09-24.

<a id="regulation-card_astra"></a>
## [GPT-6 Astra System Card](https://deploymentsafety.openai.com/gpt-6-astra)

Apollo had three days of testing, two with high-throughput reasoning-trace access, on a near-final representative model. Safeguards applied to internal tool-using inference. Published September 3, 2026.



Locator/date: 2026-09-24.

<a id="regulation-rel_astra"></a>
## [OpenAI introducing GPT-6 Astra](https://openai.com/index/gpt-6-astra/)

Initial release to limited organizations, broader rollout over following days. Do not code September 3 as established general API availability.



Locator/date: 2026-09-24.

<a id="regulation-rel_astra_notes"></a>
## [ChatGPT release notes September 3 2026](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

September 3 entry: Astra initially available to limited organizations, not general availability.



Locator/date: 2026-09-24.

<a id="regulation-metr_process26"></a>
## [METR time horizon evaluation process May 2026](https://metr.org/time-horizons/)

Typically at least1-2weeks calendar for access setup, scaffolds, around1000 test runs, restarts and manual review. One theoretical compute day is not complete evaluation service time.



Locator/date: 2026-09-24.

<a id="regulation-met_opus55"></a>
## [METR predeployment evaluation of Claude Opus 5.5](https://metr.org/blog/2026-09-22-claude-opus-5-5/)

10 business days of API capability testing; exact calendar endpoints not provided. Report published September 22, 2026.



Locator/date: 2026-09-24.

<a id="regulation-rel_opus55"></a>
## [Anthropic introducing Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5)

Model publicly released September 22, 2026.



Locator/date: 2026-09-24.

<a id="regulation-access26"></a>
## [Charnock et al., Expanding external access](https://arxiv.org/abs/2601.11916)

Access has model, information and timeframe dimensions. Extra access creates operational and security work; no causal delay coefficient.



Locator/date: 2026-09-24.

<a id="regulation-gans26"></a>
## [Gans, Staged Access and Liability for Dual-Use AI](https://www.nber.org/papers/w35586)

August 2026, revised September: release windows and liability interact through strategic defensive and adversarial effort; no US-China calibration.



Locator/date: 2026-09-24.

<a id="regulation-gans25"></a>
## [Gans, Regulating the Direction of Innovation](https://www.nber.org/papers/w32741)

JPubE 2025: regulation can change allocation between research paths; sign of innovation effect is not fixed.



Locator/date: 2026-09-24.

<a id="regulation-guerreiro26"></a>
## [Guerreiro, Rebelo and Teles, Regulating AI](https://www.nber.org/papers/w31921)

May 2026 revision: staged experimentation and release under uncertainty and heterogeneous beliefs. No service-time estimate.



Locator/date: 2026-09-24.

<a id="regulation-galasso26"></a>
## [Galasso and Luo, Product Liability Litigation and Innovation](https://www.aeaweb.org/articles?id=10.1257/mic.20240255)

AEJ Micro August 2026: medical-device introductions fall temporarily in litigated categories, with safer devices. Do not transport coefficients to AI.



Locator/date: 2026-09-24.

<a id="regulation-compliance26"></a>
## [Trebbi, Zhang and Simkovic, Compliance costs](https://www.nber.org/papers/w30691)

Occupation-task compliance costing motivates labor decomposition; no frontier-lab headcount or marginal research elasticity identified.



Locator/date: 2026-09-24.

<a id="regulation-breuer25"></a>
## [Breuer, Leuz and Vanhaverbeke, Reporting and innovation](https://www.nber.org/papers/w26291)

JAE 2025: firm-level innovation changes differ from industry aggregate after reporting requirements; no AI calibration.



Locator/date: 2026-09-24.

<a id="regulation-sb53_incident"></a>
## [California BPC 22757.13](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=22757.13)

15-day incident report; 24-hour disclosure for imminent harm. No pre-release wait in this section.



Locator/date: 2026-09-24.

<a id="regulation-sb53"></a>
## [California SB53 frozen text](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53)

Site definition used for framework/report/whistleblower package. Full statutory re-audit not performed in this calibration.



Locator/date: 2026-09-24.

<a id="regulation-eu_code"></a>
## [EU GPAI Code of Practice safety/security](https://ec.europa.eu/newsroom/dae/redirection/document/118119)

20 business days appropriate for most evaluation methods, not an unconditional statutory fixed waiting period. Frozen evaluator-window item explicitly imposes a floor.



Locator/date: 2026-09-24.

<a id="regulation-s2938"></a>
## [AI Risk Evaluation Act S2938 introduced text](https://www.govinfo.gov/content/pkg/BILLS-119s2938is/html/BILLS-119s2938is.htm)

Deployment outside developer custody prohibited absent participation/compliance; testing and formal reports; no explicit statutory safety sign-off or fixed wait.



Locator/date: 2026-09-24.

<a id="regulation-s5061"></a>
## [Secure AI Development Act S5061 introduced text](https://www.govinfo.gov/content/pkg/BILLS-119s5061is/html/BILLS-119s5061is.htm)

Section3(c): make model including weights/runtime available to NSA at least21 calendar days before commerce; no explicit approval gate in this clause.



Locator/date: 2026-09-24.

<a id="regulation-govai26"></a>
## [GovAI, Delays to Frontier AI in EU and UK](https://www.governance.ai/research-paper/delays-to-frontier-ai-in-the-eu-and-uk)

375 releases through May2026; regional API versus app distinction; enforcement period after August2026 absent.



Locator/date: 2026-09-24.

<a id="china-nist_caisi_2026"></a>
## [CAISI’s Assessment of Z.ai’s GLM-5.3 Cyber Capabilities](https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities)

About four months behind the U.S. frontier on a composite cyber evaluation.

Public and trusted-access models only; explicitly excludes unreleased internal models. General/private gap prior is an extrapolation, not this observation.

Locator/date: 2026-09-17.

<a id="china-epoch_huawei_2026"></a>
## [Will Huawei catch up to Nvidia by 2030?](https://epoch.ai/publications/huaweis-roadmap-to-2031)

2026 forecast: Nvidia 23 million H100-equivalents; Huawei 0.88 million. Huawei chip-count forecast 1.5 million; Nvidia 5.9 million.

Forecast and hardware-rated throughput, not deployed frontier compute or causal effect of removing controls.

Locator/date: 2026-09-04; updated 2026-09-24.

<a id="china-epoch_owners_2026"></a>
## [Introducing the AI Chip Owners Explorer](https://epoch.ai/latest/introducing-the-ai-chip-owners-explorer)

End-2025 Chinese ownership just over 5% of global rated compute. Google about 5 million H100e and 25% of world total, implying world about 20 million and China about 1 million H100e.

Rounded derivation. Excludes smuggling and offshore rentals. Does not establish September 2026 stock.

Locator/date: 2026-04-06.

<a id="china-epoch_malaysia_2026"></a>
## [Trade data is consistent with more than $3 billion of chips smuggled into China via Malaysia](https://epoch.ai/data-insights/malaysia-china-chip-smuggling)

April 2024–June 2025: China records $3.8bn server imports against Malaysia $0.6bn exports. Rough compute equivalent 150,000 H100e; alternative chip mix can reduce this to 50,000.

Consistent with diversion, not proof or an exhaustive smuggling estimate.

Locator/date: 2026-09-17.

<a id="china-deepseek_r1_2025"></a>
## [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/html/2501.12948v1)

Table 6: Qwen-32B distilled versus RL-only: AIME 72.6 vs 47.0; GPQA 62.1 vs 55.0; LiveCodeBench 57.2 vs 40.2. Teacher-generated training set: 800,000 samples.

Domestic DeepSeek teacher and small students, not foreign-model dependence. No equal-total-cost causal conversion to national progress.

Locator/date: 2025-01-22, v1.

<a id="china-busbridge_2025"></a>
## [Distillation Scaling Laws](https://proceedings.mlr.press/v267/busbridge25a.html)



Provides teacher/student scaling method, not a Chinese dependence fraction or intervention efficacy.

Locator/date: 2025-07-13 to 2025-07-19, ICML 2025.

<a id="china-anthropic_distill_2026"></a>
## [Detecting and preventing distillation attacks](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks)

Over 16 million exchanges through approximately 24,000 fraudulent accounts attributed to three labs.

Detected use is not causal capability uplift; selective detection and interested provider.

Locator/date: 2026-02-23.

<a id="china-rand_weights_2024"></a>
## [Securing AI Model Weights: Preventing Theft and Misuse of Frontier Models](https://www.rand.org/pubs/research_reports/RRA2849-1.html)

38 attack vectors and five security levels.

No empirically identified annual frontier theft hazard or risk-reduction fraction.

Locator/date: 2024-05-30.

<a id="china-anthropic_security_2026"></a>
## [Improving our alignment and security practices](https://www.anthropic.com/news/improving-alignment-security-efforts)

About 150 product engineers temporarily reassigned; researchers also rotated; most teams finished by early summer. A separate production RL-environment freeze lasted roughly one month.

Voluntary baseline; whole-company security/reliability/privacy campaign, not the marginal mandate cost or whole-frontier slowdown.

Locator/date: 2026-09 (date as retrieved).

<a id="china-gao_vetting_2026"></a>
## [Personnel Vetting: Leadership Attention Needed to Prioritize System Development and Achieve Reforms, GAO-26-108838](https://files.gao.gov/reports/GAO-26-108838/index.html)

FY2025 Q2 fastest 90% of initial Top Secret cases averaged 206 days; goal 114 days.

Government processing is an analogue for near-clearance vetting, not lab-specific delay. GAO also reports significant underlying timeliness-data reliability issues.

Locator/date: 2026-02.

<a id="china-flynn_2024"></a>
## [Building a Wall Around Science: The Effect of U.S.-China Tensions on International Scientific Research](https://appam.confex.com/appam/2024/mediafile/ExtendedAbstract/Paper51756/Building_a_Wall.pdf)

Version inspected: ethnic-Chinese entrants 15% less likely to attend U.S. PhD; graduates 4% less likely to remain; U.S.-based researcher productivity 2–6% lower.

Different population, treatment and horizon; later revisions differ. Context for priors, not a clearance-policy causal coefficient.

Locator/date: 2024 conference version; NBER June 2024 revised October 2024.

<a id="china-checkr_turnaround"></a>
## [Checkr's background check process](https://help.checkr.com/helpcenter/s/article/216102167-Checkr-s-background-check-process)

Typical check turnaround 3–5 business days.

Commercial service claim; actual start-date delay can be zero due to overlap and existing checks.

Locator/date: retrieved 2026-09-25.

<a id="china-sl5_2026"></a>
## [SL5 Standard for AI Security](https://arxiv.org/abs/2605.08449)

45 pages, ten control families.

Long-lead security design, no measured productivity penalty or proven theft elimination.

Locator/date: 2026-05-08, v0.1.

<a id="china-egan_heim_2023"></a>
## [Oversight for Frontier AI through a Know-Your-Customer Scheme for Compute Providers](https://arxiv.org/abs/2310.13625)



KYC enables oversight and enforcement; does not estimate denial rate or offshore Chinese frontier share.

Locator/date: 2023-10-20.

<a id="china-crosignani_2025"></a>
## [Securing Technological Leadership? The Cost of Export Controls on Firms](https://www.newyorkfed.org/research/staff_reports/sr1096)

Reports $130bn decline in affected U.S. suppliers’ market capitalization and weaker firm outcomes.

Not a current AI-accelerator R&D or frontier-speed elasticity.

Locator/date: 2024-04; revised 2025-02.
