---
category: theophysics-research
date: 2025-08-26
status: published
tags:
- o
- theophysics
- biblical-prophecy-temporal-pattern-analysis
title: External Audit — Replication Notebook (Auto‑Generated)
---
   
# External Audit — Replication Notebook (Auto‑Generated)   
   
**Status:** This run used PLACEHOLDER/SYNTHETIC datasets.   
Replace the files below with your real data and re‑run this notebook for publishable results.   
   
## File Paths   
   
- Prophecies CSV: `/mnt/data/prophecies_for_analysis_cleaned.csv`   
- Quantum Milestones JSON: `/mnt/data/quantum_milestones.json`   
- Grace Time Series CSV: `/mnt/data/grace_timeseries.csv`   
   
## Expected Schemas (summary)   
   
- **Prophecies**: id:int, book:str, prophecy_text:str, revelation_year:int, status:str, category:str   
- **Quantum**: year:int, domain:str, event:str, severity:float   
- **Grace Time Series**: t:float, G:float, P:float, F:float   
   
   
---   
   
## Replication A — Prophecy Acceleration   
   
   
- Count (pre‑1000 BC): **3**   
- Count (600 BC → 0): **3**   
- Density A (per‑year): **0.00075**   
- Density B (per‑year): **0.005**   
- **Acceleration (B/A): 6.66667**   
   
**Future prophecy clustering in -600..0:** 2/7 = **28.57%**   
   
Bootstrap (1‑sided, years permuted across entries):     
   
- Observed ratio: **6.66667**     
- p‑value: **1**     
- Bootstrap mean ± sd: **6.67 ± 8.88e-16**   
   
   
---   
   
## Replication B — Quantum Acceleration   
   
   
- Sum severity (1940–1980): **6**   
- Sum severity (1980–2025): **41**   
- **Acceleration (B/A): 6.83333**   
   
Bootstrap (1‑sided, years permuted):     
   
- Observed ratio: **6.83333**     
- p‑value: **0.068**     
- Bootstrap mean ± sd: **4.29 ± 1.29**   
   
   
---   
   
## Combined Evidence (Fisher's method)   
   
   
- Statistic: **5.3765**, df=4     
- Combined p‑value: **0.251**   
   
> Note: Fisher’s assumes independence; interpret cautiously if datasets are not independent.   
   
   
---   
   
## Replication C — β‑fit for dG/dt = β·G·P·(1+F)   
   
   
- Estimated β: **0.344911**     
- R² (fit on central‑difference derivative): **-558.0180**   
   
**Instruction:** Provide a real `grace_timeseries.csv` with columns (t,G,P,F). If you also have a preferred smoother derivative (e.g., Savitzky–Golay), we can swap it in.   
   
   
---   
   
## Figures (saved)   
   
- Prophecy timeline histogram: `/mnt/data/prophecy_timeline_hist.png`   
- Quantum severity scatter: `/mnt/data/quantum_severity_scatter.png`   
- Grace fit scatter: `/mnt/data/grace_fit_scatter.png`   
   
   
---   
   
## Methods (concise)   
1. **Prophecy Acceleration:** Counts within fixed windows; density normalized by window duration; acceleration = density_B / density_A.     
   Significance via permutation of revelation_year across rows (N=1000).   
   
2. **Quantum Acceleration:** Sum of severities across two fixed windows; acceleration = sum_B / sum_A.     
   Significance via permutation of `year` labels (N=1000).   
   
3. **Joint Evidence:** Fisher’s combining function on the two one‑sided permutation p‑values.   
   
4. **Grace β‑fit:** Central-difference derivative of G; OLS fit of dG/dt against X=G·P·(1+F). Report β and R².   
   
   
---   
   
## What You Need To Do   
   
- Replace the template files with your real datasets at the same paths.     
- Re‑run to obtain real metrics.     
- If your period definitions differ (e.g., alternative pre‑exilic windows), update the constants near the top of the code.   
   
   
---   
   
## Integrity Notes   
   
- All calculations are deterministic given the random seeds specified.     
- Bootstraps use permutation of time labels to preserve marginal distributions.