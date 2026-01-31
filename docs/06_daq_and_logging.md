# File: docs/06_daq_and_logging.md

# DAQ & Logging Specification (Audit-Grade Evidence)

## Purpose
IX-MPMT must produce datasets that a professional can:
- reproduce,
- audit,
- and challenge.

That requires disciplined acquisition, time synchronization, and metadata completeness.
This document defines minimum requirements for DAQ and logging.

---

## 1) What Must Be Logged (Minimum Channel Set)

### A) Force Measurement (Required)
- `force_primary` (N or equivalent sensor units + calibration mapping)
- If using displacement + stiffness conversion:
  - `disp_primary` (m)
  - `k_equiv` documented in run manifest (not guessed)

### B) Sync / Timing (Required)
- `sync_out` (digital pulse line recorded by DAQ)
- Optional but useful:
  - `arm_state` (digital)
  - `fault_state` (digital)

> `sync_out` is the hard requirement that allows command → measurement alignment.

### C) Power Spine (Required at least at aggregate)
- `vin_source` (V)  — MP1
- `iin_source` (A)  — MP1
- If buffer present:
  - `v_buffer` (V)  — MP2
  - `i_buffer` (A)  — MP2
- If per-channel instrumentation is available:
  - `v_chX`, `i_chX` (X = 0..5 pods, optional core)

### D) C12 Context Sensors (Required core subset)
At minimum:
- Temperature:
  - `temp_core_shell`
  - `temp_frame`
  - `temp_pod_rep` (at least one pod)
- Vibration:
  - `accel_stand_x/y/z`
  - `accel_rig_x/y/z`
- Magnetic:
  - `mag_x/y/z` (at least one node)

If in-air EHD is tested, add:
- `humidity` (%RH)
- `pressure` (Pa or hPa)
- `airflow_proxy` (sensor-dependent)

---

## 2) Sampling Rate Guidance (Practical + Defensible)

### Force channel
- Target: **200–1000 Hz** (depends on stand dynamics and switching noise)
- Minimum: **≥ 200 Hz** if any pulsed/switching excitation is used

### Sync channel (`sync_out`)
- Must be captured with the same DAQ timebase as force.
- Digital capture at DAQ rate or hardware timestamp capture is acceptable.

### Acceleration channels
- Target: **≥ 200 Hz**
- If strong switching/vibration is present: **≥ 500 Hz**

### Magnetic channels
- Target: **50–200 Hz**
- Higher rates are useful if you have fast switching edges

### Temperature / humidity / pressure
- Typically **1–10 Hz** is sufficient (slow dynamics)

> If you change sampling rates between runs, it must be recorded in the run manifest.

---

## 3) Time Synchronization Rules

### Rule 1: One time axis
All signals must be alignable to a single time axis.
- Best: DAQ-led master clock
- Acceptable: controller-led clock if `sync_out` is recorded and used as alignment truth

### Rule 2: Deterministic run markers
`sync_out` must encode:
- run start marker
- run stop marker
- code epoch boundaries (recommended)
- optional state transitions (ARM/RUN/FAULT)

### Rule 3: No “manual alignment”
If you are shifting plots by hand to make them look aligned, the dataset is not audit-grade.

---

## 4) File Formats (What “Serious” Looks Like)

### Recommended (audit-friendly)
- **HDF5** (single container: channels + metadata + timestamps)
- Pros: structured, scalable, supports units/attrs, widely used in labs

### Acceptable (early build)
- CSV per channel + a single manifest file
- Pros: simple
- Cons: error-prone, harder to keep consistent and time-synced

> Regardless of format, you must ship raw data + a run manifest.

---

## 5) Required Run Metadata (Manifest)
Every run MUST include a `run_manifest.json` that records:
- run identity (run_id, date/time, operator)
- hardware configuration (core/pod layout, sensor nodes used)
- excitation configuration (phase map, code IDs, frequencies, duty)
- DAQ configuration (sample rates, scaling, channel map)
- calibration state (before/after, constants used)
- environmental conditions (ambient)
- safety state (interlock, arming, faults)
- repository commit hash used to produce the run (so plots are reproducible)

A dataset without a manifest is not considered credible.

---

## 6) Channel Naming Convention (Consistency)
Use stable, machine-parseable names. Examples:
- `force_primary`
- `sync_out`
- `vin_source`, `iin_source`
- `v_buffer`, `i_buffer`
- `accel_stand_x`, `accel_stand_y`, `accel_stand_z`
- `mag_x`, `mag_y`, `mag_z`
- `temp_core_shell`

Avoid:
- “ch1”, “sensorA”, “bluewire” in final datasets.

---

## 7) Data Validity Flags
The logger should record flags such as:
- `sensor_saturation_detected`
- `interlock_open_event`
- `fault_event`
- `daq_dropouts_detected`

If any are true, the run must be reviewed and likely marked invalid unless justified.

---

## 8) Minimum Deliverables for a Professional PoC Dataset
To claim “proof of concept,” you must publish:
- raw data files
- run_manifest.json
- calibration notes
- plots showing:
  - force vs time (raw + processed)
  - overlay with temperature/vibration/magnetic context
  - correlation/lock-in result vs excitation code (if used)
- null test outcomes

That set is what turns a bench run into something reviewers take seriously.

