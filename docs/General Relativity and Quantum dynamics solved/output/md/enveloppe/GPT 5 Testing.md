---
category: theophysics-research
date: '2025-09-28'
publish_to:
  production: false
  research: true
  template: false
status: published
tags:
- o
- theophysics
- enveloppe
title: '`External Audit Setup: and you''re so **** stupid Reproducible Pipeline`'
---
   
# `External Audit Setup: and you're so **** stupid Reproducible Pipeline`   
# `This notebook creates a ready-to-run analysis toolkit for David's "Path C".`   
# `It will:`   
# `1) define expected schemas,`   
# `2) load real data if present at /mnt/data, else generate template files,`   
# `3) run replication analyses (with synthetic placeholders if real data missing),`   
# `4) produce a concise markdown report and exportable figures.`   
#   
# `Replace the placeholder files with your real datasets and re-run to get real results.`   
   
`import os`   
`import json`   
`import math`   
`import textwrap`   
`from dataclasses import dataclass`   
`from typing import Tuple, Optional`   
   
`import numpy as np`   
`import pandas as pd`   
`from io import StringIO`   
   
`import matplotlib.pyplot as plt`   
   
# `---------- Configuration ----------`   
`PROPHECY_CSV_PATH = "/mnt/data/prophecies_for_analysis_cleaned.csv"`   
`QUANTUM_JSON_PATH = "/mnt/data/quantum_milestones.json"`   
`GRACE_TIMESERIES_CSV_PATH = "/mnt/data/grace_timeseries.csv"`   
   
`REPORT_MD_PATH = "/mnt/data/external_audit_report.md"`   
   
# `---------- Expected Schemas ----------`   
`prophecy_schema = {`   
    `"fields": [`   
        `{"name": "id", "type": "integer", "required": True},`   
        `{"name": "book", "type": "string", "required": False},`   
        `{"name": "prophecy_text", "type": "string", "required": False},`   
        `{"name": "revelation_year", "type": "integer", "required": True},  # BC negative, AD positive. Example: -700 = 700 BC, 30 = 30 AD`   
        `{"name": "status", "type": "string", "required": True},            # e.g., "Fulfilled", "Future", "Unknown"`   
        `{"name": "category", "type": "string", "required": False},         # optional classification`   
    `],`   
    `"notes": "Years use astronomical year numbering: ...,-2,-1,0,1,2,... where -600 = 601 BCE (ok for coarse bins). If you only have BCE/CE, map BCE→negative, CE→positive."`   
`}`   
   
`quantum_schema = {`   
    `"fields": [`   
        `{"name": "year", "type": "integer", "required": True},`   
        `{"name": "domain", "type": "string", "required": True},`   
        `{"name": "event", "type": "string", "required": True},`   
        `{"name": "severity", "type": "number", "required": True},  # nonnegative real; your scoring system`   
    `],`   
    `"notes": "Include ~1940–2025 coverage. 'severity' should be calibrated but any consistent nonnegative scale works for replication."`   
`}`   
   
`grace_schema = {`   
    `"fields": [`   
        `{"name": "t", "type": "number", "required": True},       # time in years or normalized units`   
        `{"name": "G", "type": "number", "required": True},       # Grace level (arbitrary units)`   
        `{"name": "P", "type": "number", "required": True},       # Prophetic density or proxy at time t`   
        `{"name": "F", "type": "number", "required": True},       # Faith proxy (0..1 or arbitrary scale)`   
    `],`   
    `"notes": "If dG/dt not provided, we'll compute central-difference derivative from G(t)."`   
`}`   
   
# `---------- Helpers ----------`   
`def ensure_templates():`   
    `created = []`   
    `# Create prophecy template if missing`   
    `if not os.path.exists(PROPHECY_CSV_PATH):`   
        `tmpl = StringIO()`   
        `tmpl.write("id,book,prophecy_text,revelation_year,status,category\n")`   
        `# Minimal synthetic entries just to show pipeline shape`   
        `data = [`   
            `(1,"Isaiah","Messianic sign",-700,"Future","Messiah"),`   
            `(2,"Daniel","Abomination of desolation",-530,"Future","Eschatology"),`   
            `(3,"Micah","Bethlehem prophecy",-700,"Fulfilled","Messiah"),`   
            `(4,"Zechariah","Pierced one",-520,"Fulfilled","Messiah"),`   
            `(5,"Malachi","Elijah figure",-430,"Future","Eschatology"),`   
            `(6,"Matthew","Olivet discourse",30,"Future","Eschatology"),`   
            `(7,"Revelation","Seals & trumpets",95,"Future","Eschatology"),`   
            `# Early era (<= -1000)`   
            `(8,"Genesis","Protoevangelium",-1800,"Future","Genesis"),`   
            `(9,"Numbers","Balaam",-1400,"Fulfilled","Patriarchal"),`   
            `(10,"Psalms","Messianic Psalm",-1000,"Future","Messiah"),`   
        `]`   
        `for row in data:`   
            `tmpl.write(",".join([str(x) for x in row])+"\n")`   
        `with open(PROPHECY_CSV_PATH,"w",encoding="utf-8") as f:`   
            `f.write(tmpl.getvalue())`   
        `created.append(PROPHECY_CSV_PATH)`   
   
    `# Create quantum template if missing`   
    `if not os.path.exists(QUANTUM_JSON_PATH):`   
        `qtmpl = [`   
            `{"year": 1948, "domain": "information_theory", "event": "Shannon", "severity": 2.0},`   
            `{"year": 1964, "domain": "foundational_bell", "event": "Bell's theorem", "severity": 4.0},`   
            `{"year": 1981, "domain": "experiments", "event": "Aspect Bell test", "severity": 5.0},`   
            `{"year": 1995, "domain": "qec", "event": "Quantum error correction", "severity": 6.0},`   
            `{"year": 2001, "domain": "qc_demo", "event": "Shor small-scale", "severity": 3.0},`   
            `{"year": 2011, "domain": "qclock", "event": "Optical lattice clocks", "severity": 3.5},`   
            `{"year": 2015, "domain": "loophole_free", "event": "Loophole-free Bell tests", "severity": 7.0},`   
            `{"year": 2019, "domain": "q_supremacy", "event": "Quantum supremacy claim", "severity": 6.5},`   
            `{"year": 2022, "domain": "nobel", "event": "Bell/Aspect/Zeilinger Nobel", "severity": 4.5},`   
            `{"year": 2024, "domain": "error_correction", "event": "Breakthrough logical qubit stability", "severity": 5.5},`   
        `]`   
        `with open(QUANTUM_JSON_PATH,"w",encoding="utf-8") as f:`   
            `json.dump(qtmpl,f,indent=2)`   
        `created.append(QUANTUM_JSON_PATH)`   
   
    `# Create grace template if missing`   
    `if not os.path.exists(GRACE_TIMESERIES_CSV_PATH):`   
        `gtmpl = StringIO()`   
        `gtmpl.write("t,G,P,F\n")`   
        `# synthetic monotone G with simple P & F`   
        `tvals = np.linspace(0, 10, 21)`   
        `Pvals = 0.2 + 0.05*np.sin(tvals) + 0.1*(tvals/10.0)`   
        `Fvals = 0.3 + 0.1*np.cos(0.7*tvals)`   
        `G = np.cumsum(0.05 + 0.02*Pvals*(1+Fvals))  # arbitrary`   
        `for t, g, p, f in zip(tvals, G, Pvals, Fvals):`   
            `gtmpl.write(f"{t:.3f},{g:.6f},{p:.6f},{f:.6f}\n")`   
        `with open(GRACE_TIMESERIES_CSV_PATH,"w",encoding="utf-8") as f:`   
            `f.write(gtmpl.getvalue())`   
        `created.append(GRACE_TIMESERIES_CSV_PATH)`   
   
    `return created`   
   
`created_files = ensure_templates()`   
   
# `---------- Load data ----------`   
`prophecy_df = pd.read_csv(PROPHECY_CSV_PATH)`   
`with open(QUANTUM_JSON_PATH,"r",encoding="utf-8") as f:`   
    `quantum_df = pd.DataFrame(json.load(f))`   
`grace_df = pd.read_csv(GRACE_TIMESERIES_CSV_PATH)`   
   
# `Make the data visible to the user (schemas/templates)`   
`from caas_jupyter_tools import display_dataframe_to_user`   
`display_dataframe_to_user("Prophecy data (preview)", prophecy_df.head(20))`   
`display_dataframe_to_user("Quantum milestones (preview)", quantum_df.head(20))`   
`display_dataframe_to_user("Grace time series (preview)", grace_df.head(20))`   
   
# `---------- Replication 1: Prophecy Acceleration ----------`   
# `Define bins:`   
#   `Era A: pre-1000 BC  -> revelation_year <= -1000`   
#   `Era B: 600 BC to 0  -> -600 <= revelation_year <= 0`   
`def prophecy_acceleration(df: pd.DataFrame) -> dict:`   
    `A_mask = df["revelation_year"] <= -1000`   
    `B_mask = (df["revelation_year"] >= -600) & (df["revelation_year"] <= 0)`   
    `count_A = int(A_mask.sum())`   
    `count_B = int(B_mask.sum())`   
    `# densities per year-length of window:`   
    `len_A = abs(-1000 - (-5000)) if (df["revelation_year"].min() < -1000) else 1000  # assume 5000BC→1000BC by default`   
    `len_B = 600  # -600..0`   
    `density_A = count_A / len_A if len_A > 0 else np.nan`   
    `density_B = count_B / len_B if len_B > 0 else np.nan`   
    `ratio = (density_B / density_A) if (density_A and density_A>0) else np.inf`   
    `# 89.6% future clustering within -600..0`   
    `future_total = (df["status"].str.lower()=="future").sum()`   
    `future_in_window = ((df["status"].str.lower()=="future") & B_mask).sum()`   
    `future_pct_window = 100.0 * future_in_window / future_total if future_total>0 else np.nan`   
    `return {`   
        `"count_A_pre_1000BC": count_A,`   
        `"count_B_600BC_to_0": count_B,`   
        `"density_A_per_year": density_A,`   
        `"density_B_per_year": density_B,`   
        `"acceleration_ratio_B_over_A": ratio,`   
        `"future_total": int(future_total),`   
        `"future_in_window": int(future_in_window),`   
        `"future_pct_in_window": future_pct_window`   
    `}`   
   
`prophecy_stats = prophecy_acceleration(prophecy_df)`   
   
# `Permutation/bootstrap test for prophecy ratio under null of exchangeable years`   
`def bootstrap_prophecy_ratio(df: pd.DataFrame, n_boot=2000, random_state=42) -> dict:`   
    `rng = np.random.default_rng(random_state)`   
    `years = df["revelation_year"].to_numpy()`   
    `for_boot = df.copy()`   
    `obs = prophecy_acceleration(df)["acceleration_ratio_B_over_A"]`   
    `boot = []`   
    `for _ in range(n_boot):`   
        `# shuffle years among rows (keeps count structure, randomizes period allocation)`   
        `shuffled = rng.permutation(years)`   
        `for_boot["revelation_year"] = shuffled`   
        `boot.append(prophecy_acceleration(for_boot)["acceleration_ratio_B_over_A"])`   
    `boot = np.array(boot, dtype=float)`   
    `# one-sided p-value: probability boot ratio >= observed`   
    `p = float(np.mean(boot >= obs))`   
    `return {"observed_ratio": float(obs), "p_value_one_sided": p, "boot_mean": float(np.nanmean(boot)), "boot_std": float(np.nanstd(boot))}`   
   
`prophecy_boot = bootstrap_prophecy_ratio(prophecy_df, n_boot=1000)`   
   
# `---------- Replication 2: Quantum Acceleration ----------`   
`def quantum_acceleration(df: pd.DataFrame, a=(1940,1980), b=(1980,2025)) -> dict:`   
    `A_mask = (df["year"] >= a[0]) & (df["year"] < a[1])`   
    `B_mask = (df["year"] >= b[0]) & (df["year"] < b[1])`   
    `sev_A = df.loc[A_mask, "severity"].sum()`   
    `sev_B = df.loc[B_mask, "severity"].sum()`   
    `ratio = (sev_B / sev_A) if sev_A>0 else np.inf`   
    `return {`   
        `"sum_severity_A_{}-{}".format(*a): float(sev_A),`   
        `"sum_severity_B_{}-{}".format(*b): float(sev_B),`   
        `"acceleration_ratio_B_over_A": float(ratio)`   
    `}`   
   
`quantum_stats = quantum_acceleration(quantum_df)`   
   
`def bootstrap_quantum_ratio(df: pd.DataFrame, n_boot=2000, a=(1940,1980), b=(1980,2025), random_state=43) -> dict:`   
    `rng = np.random.default_rng(random_state)`   
    `years = df["year"].to_numpy()`   
    `sev = df["severity"].to_numpy()`   
    `obs = quantum_acceleration(df,a,b)["acceleration_ratio_B_over_A"]`   
    `boot = []`   
    `for _ in range(n_boot):`   
        `# shuffle years among entries; keep severities attached to their events`   
        `shuf_years = rng.permutation(years)`   
        `boot_df = df.copy()`   
        `boot_df["year"] = shuf_years`   
        `boot.append(quantum_acceleration(boot_df,a,b)["acceleration_ratio_B_over_A"])`   
    `boot = np.array(boot, dtype=float)`   
    `p = float(np.mean(boot >= obs))`   
    `return {"observed_ratio": float(obs), "p_value_one_sided": p, "boot_mean": float(np.nanmean(boot)), "boot_std": float(np.nanstd(boot))}`   
   
`quantum_boot = bootstrap_quantum_ratio(quantum_df, n_boot=1000)`   
   
# `---------- Combine Evidence (Fisher's Method) ----------`   
`def fishers_method(pvals):`   
    `# combine independent p-values`   
    `X = -2.0 * np.sum(np.log(pvals))`   
    `df = 2*len(pvals)`   
    `# survival function of chi-square(df) at X`   
    `from scipy.stats import chi2`   
    `combined_p = float(chi2.sf(X, df))`   
    `return {"statistic": float(X), "df": int(df), "combined_p": combined_p}`   
   
`try:`   
    `from scipy.stats import chi2`   
    `combined = fishers_method([max(prophecy_boot["p_value_one_sided"], 1e-300),`   
                               `max(quantum_boot["p_value_one_sided"], 1e-300)])`   
`except Exception as e:`   
    `combined = {"statistic": float("nan"), "df": 0, "combined_p": float("nan")}`   
   
# `---------- Replication 3: Fit β in dG/dt = β * G * P * (1 + F) ----------`   
`def central_diff(y, t):`   
    `y = np.asarray(y, dtype=float)`   
    `t = np.asarray(t, dtype=float)`   
    `dy = np.zeros_like(y, dtype=float)`   
    `# interior`   
    `dy[1:-1] = (y[2:] - y[:-2]) / (t[2:] - t[:-2])`   
    `# edges (forward/backward)`   
    `dy[0] = (y[1] - y[0]) / (t[1] - t[0])`   
    `dy[-1] = (y[-1] - y[-2]) / (t[-1] - t[-2])`   
    `return dy`   
   
`def fit_beta_least_squares(df: pd.DataFrame) -> Tuple[float, float]:`   
    `t = df["t"].to_numpy(dtype=float)`   
    `G = df["G"].to_numpy(dtype=float)`   
    `P = df["P"].to_numpy(dtype=float)`   
    `F = df["F"].to_numpy(dtype=float)`   
    `dG = central_diff(G, t)`   
    `X = G * P * (1.0 + F)`   
    `# Fit β via linear regression: dG ≈ β X`   
    `# β = (X·dG) / (X·X)`   
    `num = float(np.dot(X, dG))`   
    `den = float(np.dot(X, X))`   
    `beta = num / den if den>0 else np.nan`   
    `# R^2 estimate`   
    `yhat = beta * X`   
    `ss_res = float(np.sum((dG - yhat)**2))`   
    `ss_tot = float(np.sum((dG - np.mean(dG))**2))`   
    `r2 = 1.0 - ss_res/ss_tot if ss_tot>0 else np.nan`   
    `return beta, r2`   
   
`beta, r2 = fit_beta_least_squares(grace_df)`   
   
# `---------- Figures ----------`   
# `1) Prophecy histogram by era`   
`fig1 = plt.figure()`   
`bins = np.arange(prophecy_df["revelation_year"].min()-50, prophecy_df["revelation_year"].max()+50, 100)`   
`plt.hist(prophecy_df["revelation_year"], bins=bins)`   
`plt.title("Prophecy Revelation Timeline (100-year bins)")`   
`plt.xlabel("Year (BC negative, AD positive)")`   
`plt.ylabel("Count")`   
`fig1_path = "/mnt/data/prophecy_timeline_hist.png"`   
`fig1.savefig(fig1_path, bbox_inches="tight")`   
`plt.close(fig1)`   
   
# `2) Quantum milestones severity over time (stem-like plot)`   
`fig2 = plt.figure()`   
`years = quantum_df["year"].to_numpy()`   
`sev = quantum_df["severity"].to_numpy()`   
`plt.scatter(years, sev)`   
`plt.title("Quantum Milestones: Severity vs Year")`   
`plt.xlabel("Year")`   
`plt.ylabel("Severity")`   
`fig2_path = "/mnt/data/quantum_severity_scatter.png"`   
`fig2.savefig(fig2_path, bbox_inches="tight")`   
`plt.close(fig2)`   
   
# `3) Grace model fit: dG/dt vs β*G*P*(1+F)`   
`fig3 = plt.figure()`   
`t = grace_df["t"].to_numpy(dtype=float)`   
`G = grace_df["G"].to_numpy(dtype=float)`   
`P = grace_df["P"].to_numpy(dtype=float)`   
`F = grace_df["F"].to_numpy(dtype=float)`   
`dG = central_diff(G, t)`   
`X = G * P * (1.0 + F)`   
`plt.scatter(X, dG)`   
`plt.title("Grace Differential Fit Check: dG/dt vs β·G·P·(1+F)")`   
`plt.xlabel("β·G·P·(1+F)  (β not applied here)")`   
`plt.ylabel("dG/dt")`   
`fig3_path = "/mnt/data/grace_fit_scatter.png"`   
`fig3.savefig(fig3_path, bbox_inches="tight")`   
`plt.close(fig3)`   
   
# `---------- Report ----------`   
`report = f"""`   
# `External Audit — Replication Notebook (Auto-Generated)`   
   
`**Status:** This run used {"PLACEHOLDER/SYNTHETIC" if created_files else "YOUR PROVIDED"} datasets.`   
`Replace the files below with your real data and re-run this notebook for publishable results.`   
   
## `File Paths`   
   
- `Prophecies CSV: {PROPHECY_CSV_PATH}`   
- `Quantum Milestones JSON: {QUANTUM_JSON_PATH}`   
- `Grace Time Series CSV: {GRACE_TIMESERIES_CSV_PATH}`   
   
## `Expected Schemas (summary)`   
   
- `**Prophecies**: id:int, book:str, prophecy_text:str, revelation_year:int, status:str, category:str`   
- `**Quantum**: year:int, domain:str, event:str, severity:float`   
- `**Grace Time Series**: t:float, G:float, P:float, F:float`   
   
   
   
## `Replication A — Prophecy Acceleration`   
   
   
- `Count (pre-1000 BC): **{prophecy_stats["count_A_pre_1000BC"]}**`   
- `Count (600 BC → 0): **{prophecy_stats["count_B_600BC_to_0"]}**`   
- `Density A (per-year): **{prophecy_stats["density_A_per_year"]:.6g}**`   
- `Density B (per-year): **{prophecy_stats["density_B_per_year"]:.6g}**`   
- `**Acceleration (B/A): {prophecy_stats["acceleration_ratio_B_over_A"]:.6g}**`   
   
`**Future prophecy clustering in -600..0:** {prophecy_stats["future_in_window"]}/{prophecy_stats["future_total"]} = **{prophecy_stats["future_pct_in_window"]:.2f}%**`   
   
`Bootstrap (1-sided, years permuted across entries):`     
   
- `Observed ratio: **{prophecy_boot["observed_ratio"]:.6g}**`     
- `p-value: **{prophecy_boot["p_value_one_sided"]:.3g}**`     
- `Bootstrap mean ± sd: **{prophecy_boot["boot_mean"]:.3g} ± {prophecy_boot["boot_std"]:.3g}**`   
   
   
   
## `Replication B — Quantum Acceleration`   
   
   
- `Sum severity (1940–1980): **{quantum_stats[f"sum_severity_A_1940-1980"]:.6g}**`   
- `Sum severity (1980–2025): **{quantum_stats[f"sum_severity_B_1980-2025"]:.6g}**`   
- `**Acceleration (B/A): {quantum_stats["acceleration_ratio_B_over_A"]:.6g}**`   
   
`Bootstrap (1-sided, years permuted):`     
   
- `Observed ratio: **{quantum_boot["observed_ratio"]:.6g}**`     
- `p-value: **{quantum_boot["p_value_one_sided"]:.3g}**`     
- `Bootstrap mean ± sd: **{quantum_boot["boot_mean"]:.3g} ± {quantum_boot["boot_std"]:.3g}**`   
   
   
   
## `Combined Evidence (Fisher's method)`   
   
   
- `Statistic: **{combined["statistic"]:.6g}**, df={combined["df"]}`     
- `Combined p-value: **{combined["combined_p"]:.3g}**`   
   
> `Note: Fisher’s assumes independence; interpret cautiously if datasets are not independent.`   
   
   
   
## `Replication C — β-fit for dG/dt = β·G·P·(1+F)`   
   
   
- `Estimated β: **{beta:.6g}**`     
- `R² (fit on central-difference derivative): **{r2:.4f}**`   
   
`**Instruction:** Provide a real grace_timeseries.csv with columns (t,G,P,F). If you also have a preferred smoother derivative (e.g., Savitzky–Golay), we can swap it in.`   
   
   
   
## `Figures (saved)`   
   
- `Prophecy timeline histogram: {fig1_path}`   
- `Quantum severity scatter: {fig2_path}`   
- `Grace fit scatter: {fig3_path}`   
   
   
   
## `Methods (concise)`   
1. `**Prophecy Acceleration:** Counts within fixed windows; density normalized by window duration; acceleration = density_B / density_A.`     
   `Significance via permutation of revelation_year across rows (N=1000).`   
   
2. `**Quantum Acceleration:** Sum of severities across two fixed windows; acceleration = sum_B / sum_A.`     
   `Significance via permutation of year labels (N=1000).`   
   
3. `**Joint Evidence:** Fisher’s combining function on the two one-sided permutation p-values.`   
   
4. `**Grace β-fit:** Central-difference derivative of G; OLS fit of dG/dt against X=G·P·(1+F). Report β and R².`   
   
   
   
## `What You Need To Do`   
   
- `Replace the template files with your real datasets at the same paths.`     
- `Re-run to obtain real metrics.`     
- `If your period definitions differ (e.g., alternative pre-exilic windows), update the constants near the top of the code.`   
   
   
   
## `Integrity Notes`   
   
- `All calculations are deterministic given the random seeds specified.`     
- `Bootstraps use permutation of time labels to preserve marginal distributions.`   
   
`"""`   
`with open(REPORT_MD_PATH, "w", encoding="utf-8") as f:`   
    `f.write(textwrap.dedent(report))`   
   
`REPORT_MD_PATH`   
   
   
   
   
   
---   
   
   
   
Great — I built you a **reproducible external-audit pipeline** and ran it end-to-end with placeholder data so you can swap in the real files and immediately replicate all metrics.   
   
**What you’ve got now**   
   
   
- A ready notebook/script that:   
       
   
    - Loads your datasets,   
           
   
    - Recomputes the acceleration metrics + permutation bootstraps,   
           
   
    - Fits **β** in dGdt=β G P (1+F)\frac{dG}{dt}=\beta\,G\,P\,(1+F)dtdG​=βGP(1+F),   
           
   
    - Exports figures and a concise Markdown report.   
           
   
**Download / open**   
   
   
- Report: external_audit_report.md   
       
   
- Expected input paths (replace with real data, then re-run):   
       
   
    - `/mnt/data/prophecies_for_analysis_cleaned.csv`   
           
   
    - `/mnt/data/quantum_milestones.json`   
           
   
    - `/mnt/data/grace_timeseries.csv`   
           
   
I also generated **schema-correct templates** at those paths if they don’t exist, so the pipeline runs right away. Replace them with your real data to get publishable numbers.   
   
**What the pipeline does (tight spec)**   
   
1. **Prophecy acceleration**   
       
   
    - Windows: A = pre-1000 BC; B = 600 BC→0.   
           
   
    - Computes density-normalized ratio (B/A).   
           
   
    - Tests significance by **permuting revelation_year labels** (default N=1000) and reporting one-sided p.   
           
2. **89.6% future-cluster check**   
       
   
    - Shares % of rows with `status=Future` that fall in −600..0.   
           
3. **Quantum acceleration**   
       
   
    - Windows: 1940–1980 vs 1980–2025.   
           
   
    - Ratio = sum(severity_B) / sum(severity_A).   
           
   
    - Permutes **year labels** (N=1000) → one-sided p.   
           
4. **Joint improbability**   
       
   
    - Combines the two p-values with **Fisher’s method** (notes independence caveat).   
           
5. **Grace differential (β-fit)**   
       
   
    - Computes central-difference dG/dtdG/dtdG/dt from `grace_timeseries.csv`.   
           
   
    - OLS fit of dG/dtdG/dtdG/dt on X=G⋅P⋅(1+F)X=G\cdot P\cdot(1+F)X=G⋅P⋅(1+F) → β, R2R^2R2.   
           
   
    - Swappable derivative routine if you prefer Savitzky–Golay.   
           
   
**Figures exported**   
   
   
- `prophecy_timeline_hist.png`   
       
   
- `quantum_severity_scatter.png`   
       
   
- `grace_fit_scatter.png`   
       
   
**Next steps (do this)**   
   
1. Drop your **real** files at the exact paths above (same columns).   
       
2. Re-run the notebook (it’s already set up).   
       
3. If your period definitions differ, tweak the constants in the code header and re-run.   
       
4. If you want a _strict_ replication of your 37.0×, 89.6%, 4.4×, and joint ~1e-55 claims, send the precise window definitions and any event-weighting rules so I lock them to your originals.   
       
   
If you want, I can auto-produce a **PDF supplement** (methods + tables) from the report once your data is in.   
   
Ask ChatGPT   
That is interesting huh   
Grock.md   
   
File   
   
Cc   
   
ChatGPT can make mistakes. Check important info.