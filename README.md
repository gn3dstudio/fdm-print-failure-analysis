# FDM Print Failure Analysis & Troubleshooting Database

This repository houses empirical datasets and systematic engineering diagnostic guides mapping physical FDM (Fused Deposition Modeling) print failures to root-cause slicing, thermal, mechanical, and filament moisture variables.

By replacing standard subjective troubleshooting steps ("dry your filament") with quantitative physical parameters (mass absorption weights, crystallization velocities, input shaping profiles), operators can optimize part repeatability and maintain structural yield thresholds.

---

## 1. Directory Structure

```
├── README.md
└── datasets/
    ├── moisture_vs_tensile.csv (Empirical log of filament moisture vs. Z-axis strength)
    └── annealing_shrinkage_log.csv (Dimensional variance logs before/after thermal baking)
```

---

## 2. Core Failure Diagnosis Framework

### Warp and Thermal Stress ($S_{warp}$)
Warping occurs when residual thermal stress exceeds the layer adhesion limits. 
Thermal stress generated in a printed layer can be modeled using:

$$S_{warp} = E \times \alpha \times \Delta T$$

Where:
*   $E$ = Tensile Modulus of the polymer ($\text{GPa}$)
*   $\alpha$ = Linear Coefficient of Thermal Expansion ($\text{mm/mm/°C}$)
*   $\Delta T$ = Temperature delta ($T_{extrusion} - T_{chamber}$)

#### Warping Control Action:
To reduce $S_{warp}$ in high-shrinkage materials such as **ABS** and **Polycarbonate (PC)**:
1.  **Reduce $\Delta T$**: Raise the ambient chamber temperature ($T_{chamber}$) closer to the glass transition temperature ($T_g$) of the polymer. Cap chamber temperature at **$80\text{°C}$ for PC** and **$50\text{°C}$ for ABS**.
2.  **Ensure Bed Adhesion**: Utilize high-temp bed plates ($100\text{°C–}115\text{°C}$), thin layers of PVA glue, or pei build sheets to provide a mechanical counter-force that resists warping stress.

---

## 3. Empirical Datasets Analysis

### 3.1: Moisture Absorption vs. Z-Axis Tensile Strength
This dataset ([datasets/moisture_vs_tensile.csv](datasets/moisture_vs_tensile.csv)) records the mechanical tensile degradation of standard specimens printed under varying hygroscopic conditions.

*   **Hygroscopic Physics**: Semicrystalline polymers like Polyamide (PA6) readily absorb atmospheric water molecules. Under thermal extrusion ($280\text{°C–}290\text{°C}$), water boils inside the nozzle melt zone. This rapid vaporization creates microscopic steam bubbles, causing **micro-voiding** at the toolpath interface.
*   **The Mechanical Limit**: Our tensile tests show that when **Nylon-CF30** moisture content increases from **$0.03\%$ (bone-dry)** to **$1.10\%$ (humid)**, Z-axis tensile strength drops from **$35.1\text{ MPa}$ to $13.2\text{ MPa}$**—a catastrophic **$62.4\%$ reduction in load-bearing capacity**.

### 3.2: Annealing Thermal Shrinkage Log
This dataset ([datasets/annealing_shrinkage_log.csv](datasets/annealing_shrinkage_log.csv)) logs post-annealing shrinkage percentages and tensile modifications.

*   **Annealing Kinetics**: Heating printed parts to slightly above their glass transition temperature ($T_g$) but below their melting point ($T_m$) allows polymer chains to relax, re-crystallize, and increase molecular diffusion across layer boundaries.
*   **Dimensional Trade-off**: Annealing ABS at $80\text{°C}$ for 4 hours increases tensile strength by **$+15.2\%$**, but introduces an isotropic dimensional shrinkage rate of **$0.72\%$ along the XY-axis** while causing a minor expansion **($-0.15\%$) along the Z-axis**.

---

## 4. Hardware Calibration & Metrology

To guarantee structural tolerance repeatability within $\pm 0.1\text{ mm}$ on FDM platforms, operators must run dynamic calibration steps:

1.  **Active Input Shaping**: Calibrate dynamic resonant frequencies using an ADXL345 accelerometer to define Klipper input shaping parameters (recommended: $MZV$ or $EI$ shaper types) to eradicate surface ghosting/ringing under accelerations $> 5,000\text{ mm/s}^2$.
2.  **Pressure Advance ($k$-Factor)**: Calibrate the extrusion melt-zone pressure to eliminate corner swelling and under-extrusion at seam margins.

---

## 5. Structural Solutions & B2B Manufacturing

If your prototypes require absolute mechanical validation or if you struggle to maintain dimensional repeatability when printing advanced composite filaments in-house, you can leverage a fully calibrated industrial FDM fleet.

For high-precision industrial production, detailed diagnostic reviews, and certified materials testing, consult our B2B additive manufacturing guides:

👉 **[Quy trình chẩn đoán và khắc phục cong vênh nhựa ABS | GN3D Studio](https://gn3dstudio.com/kien-thuc-in-3d/abs-bi-cong-venh-chan-doan-va-khac-phuc-theo-quy-trinh-san-xuat)**

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
*Developed by [GN3D Studio](https://gn3dstudio.com).*
