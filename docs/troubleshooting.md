# Troubleshooting Guide - FDM Print Failure Analysis

This guide provides engineering diagnostics and corrective workflows for physical FDM printing failures, such as warp stresses and moisture absorption.

## 1. Physical Layer Warping ($S_{warp} >$ Adhesion Limit)

### Diagnostic Symptoms:
- Corners of printed ABS/Polycarbonate models lift from the build plate.
- Layer splitting or cracking along the Z-axis in mid-print height.

### Root-Cause Physics:
Residual thermal stress ($S_{warp} = E \times \alpha \times \Delta T$) exceeds the bed plate adhesive limits or layer bonding limits.

### Action Plan:
1. **Reduce $\Delta T$**: Ensure your chamber heater keeps the internal ambient temperature stable:
   - For Polycarbonate (PC): Target $80^\circ\text{C}$ chamber temperature.
   - For ABS/ASA: Target $50^\circ\text{C}$ chamber temperature.
2. **Increase Bed Temperature**: Run build plate at $100^\circ\text{C}$ (ABS) or $110^\circ\text{C}$ (PC) to expand the adhesion base.
3. **Use Draft Shields**: If your printer lacks an active chamber heater, enable "Draft Shield" in the slicer to trap hot air around the print.

---

## 2. Hygroscopic Moisture Bubbles (Micro-voiding)

### Diagnostic Symptoms:
- Hissing or popping sounds emanating from the nozzle during extrusion.
- Rough, porous surface finishes or stringing between columns.
- Extreme loss of Z-axis tensile strength (up to 60%).

### Root-Cause Physics:
Atmospheric moisture absorbed by hygroscopic filaments (such as PA6-GF, Nylon CF, or PETG) vaporizes instantly inside the $280^\circ\text{C}$ hotend, leaving micro-bubbles inside the extruded bead.

### Action Plan:
1. **Baking Protocol**: Prior to printing, bake the filament spool in a convection oven:
   - For Nylon/PA6: Bake at $80^\circ\text{C}$ for 12 hours.
   - For TPU/PETG: Bake at $65^\circ\text{C}$ for 6 hours.
2. **Active Dry Cabinet**: Transfer the baked filament directly into a dry box containing fresh silica gel or molecular sieve packs. Maintain relative humidity below $15\%\text{ RH}$ during the print process.
3. **Purge the Nozzle**: Extrude a small test length. If the purge is clear and silent, the filament is sufficiently dry.
