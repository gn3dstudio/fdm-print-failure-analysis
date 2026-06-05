# Shareable Promotional Content - FDM Print Failure Analysis

This file contains pre-written drafts for community engagement, focusing on quantitative material degradation and physical FDM print failure diagnostics.

---

## 1. LinkedIn Post Draft

**Hook**: Does wet filament actually weaken your functional 3D prints? 💦🏋️‍♂️

We've all heard the advice to "dry your filament." But as engineers, we wanted quantitative, empirical proof. How does moisture absorption affect Z-axis interlayer weld density and tensile strength?

We printed standard test specimens under controlled humidity levels using **Nylon-CF30 (Carbon-Fiber Nylon)** and performed mechanical pull tests.

**The Findings**:
- Increasing filament moisture from **0.03% (bone-dry)** to **1.10% (humid)** caused Z-axis tensile strength to drop from **35.1 MPa to 13.2 MPa**—a massive **62.4% strength reduction**.
- Under thermal extrusion (280C), trapped moisture boils instantly, creating micro-voids inside the toolpath margins.

We have open-sourced the empirical datasets and shrinkage matrices here: https://github.com/gn3dstudio/fdm-print-failure-analysis

#3DPrinting #MaterialsScience #AdditiveManufacturing #MechanicalEngineering #HardwareEngineering #NylonCF #GN3DStudio

---

## 2. Dev.to Article Draft

**Title**: Quantifying Additive Failure: The Physics of Moisture and Annealing Shrinkage in FDM Polymers

**Body**:
Subjective guidelines dominate 3D printing forums. However, producing functional end-use brackets requires physical and chemical calibrations.

In this technical breakdown, we look at the physics of two common failure points:
1. **Hygroscopic Micro-voiding**: Using CSV logs, we map how water molecules boil in the nozzle and reduce the weld density of Carbon-Fiber Nylon by up to 62.4%.
2. **Thermal Stress and Warping**: We map layer stresses ($S_{warp} = E \times \alpha \times \Delta T$) to ambient chamber limits.
3. **Annealing Shrinkage Rates**: While thermal post-baking ABS at 80C increases tensile strength by +15.2%, it introduces anisotropic dimensional shrinkage (0.72% along XY, while causing minor expansion along Z).

Explore the experimental datasets and parsing utilities:
👉 https://github.com/gn3dstudio/fdm-print-failure-analysis

---

## 3. Reddit Post Draft

**Subreddit**: r/3Dprinting or r/materials

**Title**: Empirical Datasets: How filament moisture degrades Z-axis tensile strength by up to 62% (With CSV logs)

**Body**:
Hi all,

Instead of relying on visual "stringing" checks to determine if filament is wet, our team conducted pull tests on specimens printed with various humidity ratings of Nylon-CF30.

We measured the absolute moisture weight percentage and corresponding Z-axis tensile strength in MPa. 

The dataset logs are open-sourced in CSV format along with a Python script to calculate degradation thresholds. We also compiled an annealing log tracking isotropic dimensional shrinkage of ABS and PETG post-bake.

Data and code link:
https://github.com/gn3dstudio/fdm-print-failure-analysis

Hope this helps anyone seeking quantitative data for their functional assemblies!

---

## 4. Hacker News Submission Draft

**Title**: Show HN: Empirical data on how filament moisture degrades 3D print strength

**Link**: `https://github.com/gn3dstudio/fdm-print-failure-analysis`

**Text/Description**:
Trapped water inside hygroscopic filaments (like Nylon) vaporizes during 3D printing extrusion. We ran mechanical pull tests on Carbon-Fiber Nylon specimens printed at moisture levels ranging from 0.03% to 1.10% and open-sourced the data. The results show a 62.4% loss of inter-layer tensile strength due to steam-induced micro-voiding.
