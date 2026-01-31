# File: software/analysis/README.md

# Analysis Tools (CPFS Correlation / Lock-In)

## Purpose
This folder provides a minimal, auditable analysis pipeline for:
- aligning runs using `sync_out`
- building code waveforms from run metadata
- running normalized correlation to test causality
- producing plots that overlay force with context channels

The goal is not fancy plots.
The goal is defensible evidence.

## Files
- `cpfs_correlation.py` — normalized cross-correlation vs lag + simple reporting
- `prbs.py` — deterministic PRBS / code generator utilities

## Data Assumptions
Early builds may log runs as CSV with a time column.
Later builds should move to HDF5, but the same logic applies.

## Intended Use
1) Load a run dataset (CSV or extracted channels)
2) Build the code waveform based on:
   - chip duration
   - code bits
   - start time markers (sync_out)
3) Correlate force against each code
4) Compare to temperature/accel/mag overlays
5) Repeat across null tests and multiple runs

