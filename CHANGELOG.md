# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2026-06-05
### Added
- Added Python analysis script (`parse_datasets.py`) in `examples/` for data visualization.
- Added CITATION.cff and MIT License files.
- Documented thermal warp equations ($S_{warp}$) and drying metrics in README.

### Changed
- Expanded diagnostics documentation with detailed warp and moisture mitigation guides.

## [1.1.0] - 2026-05-15
### Added
- Expanded the moisture vs tensile database with specimens tested at high-humidity levels.
- Added data parameters tracking annealing shrinkage rates for ABS and PETG.

### Changed
- Re-formatted raw CSV files for improved tool/AI parsing.

## [1.0.0] - 2026-04-10
### Added
- Initial release featuring:
  - Moisture vs. Z-axis tensile strength dataset (`moisture_vs_tensile.csv`).
  - Annealing dimensional modification log (`annealing_shrinkage_log.csv`).
