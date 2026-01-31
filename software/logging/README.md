# File: software/logging/README.md

# Logging (Run Manifest + Channel Map)

## Purpose
This folder defines the minimum dataset structure required for IX-MPMT runs:
- a machine-validated `run_manifest.json`
- a consistent channel naming map
- raw data storage conventions

IX-MPMT treats datasets as first-class artifacts.

---

## Required Dataset Layout (Per Run)
A single run should be stored as:

- `runs/<run_id>/`
  - `run_manifest.json`
  - `raw/`
    - (one or more raw files; HDF5 preferred)
  - `plots/`
    - exported figures (png/pdf)
  - `notes/`
    - optional photos, setup notes

The `run_manifest.json` is mandatory even for exploratory runs.

---

## Manifest Validation
`run_manifest.schema.json` is provided so manifests can be validated automatically.

---

## Channel Map
A channel map template is provided to keep naming stable across DAQ configs.

