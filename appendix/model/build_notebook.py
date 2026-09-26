from pathlib import Path
import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter
OUT=Path(__file__).resolve().parents[1]
ROOT=OUT
nb=nbformat.v4.new_notebook();cells=[]
def md(s):cells.append(nbformat.v4.new_markdown_cell(s))
def code(s):cells.append(nbformat.v4.new_code_cell(s))
md('''# AI Safety Menu: the 12-month model

**35 numerical estimates, with executable calculations and evidence boundaries.** Positive days close the U.S. technical capability lead; negative days widen it. Existing nonpublic models count as technical capability. Launch restrictions affect the production of future capability and foreign access rather than erasing a trained model.

This notebook recomputes the headline model locally. The more expensive structural sensitivity runs are supplied as saved results from `model/run_all.py`. They can be regenerated with that script. No private data, paid API or network request is needed.

Most policy-specific causal parameters are explicit analyst priors. This is a structural estimate under those priors, **not an empirically identified policy effect**. See [METHOD](METHOD.html), [all 35 info pages](index.html), and the [evidence register](sources.html).''')
code('''from pathlib import Path
import sys, json, hashlib
sys.dont_write_bytecode = True
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
ROOT = Path.cwd()
MODEL = ROOT / "model"
sys.path.insert(0, str(MODEL))
from unified_model import make_inputs, evaluate
N, SEED = 8192, 260925
plt.rcParams.update({"figure.dpi": 110, "savefig.dpi": 160, "font.size": 10,
                     "axes.spines.top": False, "axes.spines.right": False})
records = json.loads((ROOT / "policy-estimates.json").read_text())["policies"]
names = {p["policy_id"]: p["name"] for p in records}
print(f"Run: {N:,} shared parameter draws, seed {SEED}, weekly paths, three-year sensitivity horizon.")''')
md('''## 1. Observations used for calibration

The release table has eight models but only six release campaigns. Some campaign members share evaluations, so they are not independent evidence. Only four campaigns supply a usable access-to-release measure; the GPT-5.5 testing start is a conservative proxy for earliest access. Missing planned-release dates prevent causal measurement of evaluation-induced delay.''')
code('''release = pd.read_csv(MODEL / "public-release-cases.csv")
assert release.case_id.is_unique and len(release) == 8
assert release.release_cluster.nunique() == 6
assert release.causal_policy_delay_days.isna().all()
display(release[["model", "release_cluster", "public_release_date", "access_start_date",
                 "calendar_access_to_release_days", "observed_access_window_value",
                 "observed_access_window_unit"]].fillna("Not published"))
print("No observed access interval is relabeled as a causal policy delay.")''')
md('''The ECI trend is a descriptive crosscheck. It is not used to identify the policy effects. The frozen source table ends in June 2026; it is not the live September frontier. A linear scale conversion cancels when applied to both capability shocks and the progress ruler. The separate fixed-6.5-ECI/log-compute sensitivity deliberately changes that mapping.''')
code('''eci = pd.read_csv(MODEL / "eci_reasoning_frontier.csv")
print(eci.columns.tolist())
display(eci.head(3))
fit = json.loads((MODEL / "baseline_fit.json").read_text())
print(json.dumps({k:fit[k] for k in ["n", "ols_eci_per_year", "rmse_eci", "expanding_window_n", "expanding_window_mae_eci"]}, indent=2))''')
code('''date_col = next(c for c in eci if "date" in c or c == "release")
score_col = next(c for c in eci if "eci" in c.lower() or c.lower() == "score")
dates = pd.to_datetime(eci[date_col])
x = (dates-dates.min()).dt.days.to_numpy()/365.25
y = eci[score_col].to_numpy(dtype=float)
slope, intercept = np.polyfit(x,y,1)
assert abs(slope-fit["ols_eci_per_year"]) < 1e-8
fig,ax=plt.subplots(figsize=(9,4))
ax.scatter(dates,y,color="#1e6d72",s=45,label="Published reasoning-frontier entries")
ax.plot(dates,intercept+slope*x,color="#af6b35",label=f"Descriptive fit: {slope:.2f} ECI/year")
ax.set(ylabel="Epoch Capabilities Index",title="An observed progress crosscheck, not causal policy evidence")
ax.legend(frameon=False);ax.grid(axis="y",alpha=.18)
fig.autofmt_xdate();fig.tight_layout()
fig.savefig(ROOT/"eci-crosscheck.png")
plt.show()''')
md('''## 2. Recompute all 35 estimates

The production equation has diminishing returns to research and incremental feedback from AI capability. Both countries receive direct input effects and lagged spillovers. A fixed-point iteration includes incoming knowledge changes in research productivity. All comparisons share growth and dependence draws. Bundle gates and workloads are combined before national effects are calculated.''')
code('''inputs = make_inputs(n=N, seed=SEED, steps=52, years=3)
calculated = evaluate(inputs)
saved = json.loads((MODEL/"model-results.json").read_text())
assert set(calculated["estimates"]) == set(names)
for pid in names:
    r=calculated["estimates"][pid]["1"]
    assert abs(r["mean_days"]-saved["estimates"][pid]["1"]["mean_days"]) < 1e-10
    assert abs(r["us_delay_days"]-r["china_delay_days"]-r["mean_days"]) < 1e-9
    assert abs(r["us_direct_days"]+r["us_research_days"]+r["us_reverse_spillover_days"]-r["us_delay_days"]) < 1e-9
    assert abs(r["china_direct_days"]+r["china_research_days"]+r["china_spillover_days"]-r["china_delay_days"]) < 1e-9
    assert calculated["estimates"][pid]["convergence"]["converged"]
rows=[]
for record in records:
    pid=record["policy_id"];r=calculated["estimates"][pid]["1"]
    rows.append({"Policy":names[pid],"Best estimate, days":r["mean_days"],
                 "5th percentile":r["p05_days"],"95th percentile":r["p95_days"],
                 "US loss":r["us_delay_days"],"China loss":r["china_delay_days"],
                 "MC standard error":r["mc_standard_error_days"]})
prices=pd.DataFrame(rows)
display(prices.style.format(precision=3))
print("All 35 recomputed means match the frozen output; country decompositions reconstruct exactly.")''')
md('''The intervals below describe uncertainty in conditional expected effects under the input priors. They do not describe every realized history, and are not confidence intervals. Most fine rankings among near-zero measures are not robust.''')
code('''ordered=prices.sort_values("Best estimate, days")
y=np.arange(len(ordered));mid=ordered["Best estimate, days"].to_numpy()
fig,ax=plt.subplots(figsize=(12,12))
ax.hlines(y,ordered["5th percentile"],ordered["95th percentile"],color="#9aada8",lw=2)
ax.scatter(mid,y,c=np.where(mid<0,"#1c7165","#a16437"),s=34,zorder=3)
ax.set_yticks(y,ordered["Policy"])
ax.set_xscale("symlog",linthresh=1,linscale=1)
ax.set_xticks([-100,-10,-1,0,1,10,100],labels=["−100","−10","−1","0","1","10","100"])
ax.axvline(0,color="#53625e",lw=.8);ax.grid(axis="x",alpha=.2)
ax.set(xlabel="Lead closed, days — symmetric log scale, linear between −1 and +1 day",
       title="12-month technical capability gap: mean and 90% parameter range")
ax.text(.01,-.075,"Negative widens the U.S. lead; positive closes it. Most precise-looking small numbers are highly assumption-sensitive.",transform=ax.transAxes,fontsize=9)
fig.tight_layout();fig.savefig(ROOT/"policy-estimates.png",bbox_inches="tight")
plt.show()''')
md('''## 3. Horizon and structural sensitivity

A fixed input share can create a persistent level gap, a permanent compute ceiling can increasingly bind, and a temporary pause can partly unwind. This is why the 12-month endpoint cannot be replaced by an additive annual delay. The 36-month columns are scenario extensions, with post-year-one inputs held fixed where documented.''')
code('''selected=["compute-cap","pause-6","safety-compute-share","safety-case-train","data-licensing","export-controls"]
fig,ax=plt.subplots(figsize=(10,5))
x=np.arange(len(selected));width=.25
for k,(h,label,color) in enumerate([("0.5","6 months","#9bb7a8"),("1","12 months","#287271"),("3","36 months","#b4773d")]):
    vals=[calculated["estimates"][p][h]["mean_days"] for p in selected]
    ax.bar(x+(k-1)*width,vals,width,label=label,color=color)
ax.axhline(0,color="#44514b",lw=.8);ax.grid(axis="y",alpha=.18)
ax.set_xticks(x,["Compute cap","6-month pause","Safety budget","Training approval","Data licensing","Export controls"])
ax.set(ylabel="Lead closed, days",title="Endpoint effects can grow, level off or unwind")
ax.legend(frameon=False);fig.tight_layout();fig.savefig(ROOT/"horizon-sensitivity.png")
plt.show()''')
code('''sensitivity=json.loads((MODEL/"sensitivity-results.json").read_text())
cols={"Main":None,"No forward reliance":"no_forward_diffusion","Half reliance":"half_forward_diffusion",
      "Double reliance":"double_forward_diffusion","No AI feedback":"no_ai_research_feedback",
      "Alternative ECI ruler":"fixed_6_5_eci_per_log_compute_observed_ruler"}
rows=[]
for pid in names:
    row={"Policy":names[pid]}
    for label,key in cols.items():row[label]=calculated["estimates"][pid]["1"]["mean_days"] if key is None else sensitivity[key][pid]["1"]
    rows.append(row)
display(pd.DataFrame(rows).style.format(precision=2))
print("Universal-pause sensitivity at month12:",sensitivity["universal_pause"]["pause-6"]["1"])
print("It is a separate scenario. Both menu pause headlines retain the menu's unilateral implementation convention.")''')
md('''## 4. Numerical and methodological checks

Implementation checks do not validate the true policy effects. The source evidence, the model structure and the numerical solution are separate layers. The saved validation files describe boundary conditions, an alternative seed and a half-weekly time grid.''')
code('''validation=json.loads((MODEL/"numerical-validation.json").read_text())
print("Maximum weekly vs half-weekly difference:",validation["max_time_step_difference_days"],"days")
assert validation["max_time_step_difference_days"] < .2
checks=[]
for filename in ["unified-validation.json","production-validation.json","china-path-validation.json","regulation-sampler-validation.json"]:
    data=json.loads((MODEL/filename).read_text())
    print(filename)
    print(str(data)[:1000])
print("Largest MC standard error:",prices["MC standard error"].max(),"days")
print("Largest fixed-point iteration count:",max(x["convergence"]["iterations"] for x in calculated["estimates"].values()))
assert np.isfinite(prices.select_dtypes("number").to_numpy()).all()
assert calculated["estimates"]["pause-6"]["1"]["mean_days"] == calculated["estimates"]["pause-letter"]["1"]["mean_days"]
print("No missing numeric estimates. All bundle and policy identifiers covered.")''')
md('''## Reading the result correctly

The strongest numerical changes concern the meaning of a delay. An external launch gate can withhold useful teachers from China while leaving the U.S. technical frontier largely intact. Ordinary paperwork displaces only a small share of a frontier lab's research resources. Training prohibitions directly block new capability production and are much larger under these assumptions.

The model does not establish that the small negative estimates are empirically proven strategic benefits. Their signs depend on marginal foreign reliance and on the technical-frontier definition. The security estimates depend heavily on useful-compromise hazards and retained stolen-model value. Export controls depend on additional purchases after relaxation and the relevance of that compute. These are quantified assumptions, exposed in each info page.

To regenerate the full sensitivity suite: `python model/run_all.py`. To inspect a parameter, open the appropriate calibration JSON and its cited primary source. A complete manifest records file hashes. No changes have been published to the live website.''')
nb.cells=cells;nb.metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python','version':'3.12'}}
p=OUT/'policy-model.ipynb';nbformat.write(nb,p)
print('Executing notebook',flush=True)
client=NotebookClient(nb,timeout=900,kernel_name='python3',resources={'metadata':{'path':str(OUT)}})
client.execute();nbformat.write(nb,p)
exporter=HTMLExporter();body,_=exporter.from_notebook_node(nb);(OUT/'policy-model.html').write_text(body)
print('Notebook executed and HTML exported',flush=True)
