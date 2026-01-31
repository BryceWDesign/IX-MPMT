# File: docs/04_data_integrity.md

# Data Integrity & Evidence Standards

## Required for every run
- Unique Run ID
- Configuration snapshot:
  - pod roles (emitter/dummy), positions, wiring variant
  - excitation parameters (frequency, duty, code ID, phase map)
  - ambient (temperature, humidity, pressure if available)
- Calibration state (before/after)
- Raw logs (unaltered)
- Processing scripts/notebooks (versioned)
- Plots:
  - force signal (raw + processed)
  - correlation/lock-in result (if used)
  - temperature / airflow / vibration overlays

## Storage rules
- Raw data is immutable once recorded.
- Any derived dataset must reference the raw file hash or run ID.
- Processing must be reproducible from repo scripts.

## What reviewers look for
- raw data availability,
- repeatability across runs,
- clear null-test outcomes,
- explicit artifact controls.

