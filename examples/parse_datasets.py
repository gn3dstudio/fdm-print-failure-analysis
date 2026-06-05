#!/usr/bin/env python3
"""
GN3D FDM Print Failure Analysis dataset parsing script.
Loads experimental logs from the datasets directory, calculates
tensile strength degradation rates and dimensional shrinkage percentages.
"""

import os
import csv

def analyze_moisture_dataset(csv_path):
    print(f"\n--- Loading Moisture vs Tensile Dataset: {csv_path} ---")
    if not os.path.exists(csv_path):
        print(f"[Error] File not found: {csv_path}")
        return

    with open(csv_path, mode='r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
    print(f"Loaded {len(rows)} experimental measurements.")
    
    # Calculate baseline and worst-case
    strengths = [float(row['z_tensile_strength_mpa']) for row in rows]
    moistures = [float(row['moisture_content_percent']) for row in rows]
    
    max_strength = max(strengths)
    min_strength = min(strengths)
    max_moisture = max(moistures)
    
    degradation = ((max_strength - min_strength) / max_strength) * 100
    
    print(f"Optimal Tensile Strength (Dry): {max_strength:.2f} MPa")
    print(f"Humid Tensile Strength ({max_moisture:.2f}% moisture): {min_strength:.2f} MPa")
    print(f"Calculated Z-Axis Tensile Strength Loss: -{degradation:.1f}%")

def analyze_shrinkage_dataset(csv_path):
    print(f"\n--- Loading Annealing Shrinkage Log: {csv_path} ---")
    if not os.path.exists(csv_path):
        print(f"[Error] File not found: {csv_path}")
        return

    with open(csv_path, mode='r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
    print(f"Loaded {len(rows)} material records.")
    for row in rows:
        material = row['material']
        temp = row['annealing_temp_c']
        xy_shrink = float(row['xy_shrinkage_percent'])
        z_shrink = float(row['z_shrinkage_percent'])
        strength_gain = float(row['tensile_strength_diff_percent'])
        
        print(f"- {material} @ {temp}C: XY Shrinkage: {xy_shrink:+.2f}%, Z Expansion: {z_shrink:+.2f}%, Strength Gain: {strength_gain:+.1f}%")

def main():
    # Paths relative to the root directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    moisture_path = os.path.join(base_dir, "datasets", "moisture_vs_tensile.csv")
    shrinkage_path = os.path.join(base_dir, "datasets", "annealing_shrinkage_log.csv")
    
    analyze_moisture_dataset(moisture_path)
    analyze_shrinkage_dataset(shrinkage_path)

if __name__ == "__main__":
    main()
