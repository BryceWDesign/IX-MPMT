# Calibration (Force / Displacement / Sensor Integrity)

## Purpose
Calibration is what makes IX-MPMT believable.
This document defines minimum calibration procedures and what must be recorded.

---

## 1) Force Calibration (Required)
You must be able to map your primary measurement channel to force units
(or clearly state the measured proxy and how it relates to force).

### Accepted approaches
A) **Known mass method (static)**
- Apply a known small mass through a known geometry to create a known force:
  - F = m * g (in Newtons)
- Record sensor response vs applied force.
- Use multiple points across the expected operating range.

B) **Known spring method (static)**
- Use a calibrated spring and known displacement to apply force:
  - F = k * x
- Document k and how it was obtained (manufacturer spec alone is not ideal).

C) **Optical displacement + stiffness mapping (if using flexure/pendulum)**
- Calibrate displacement to force by determining the effective stiffness k_equiv.
- Document the method and uncertainty.

### Required records (per calibration)
- date/time
- applied force points (with units)
- sensor output values
- fitted mapping (slope/offset or curve)
- uncertainty notes

---

## 2) Pre-Run / Post-Run Calibration Checks (Required)
Before a run:
- confirm baseline zero (or record offset)
- apply a small known check point (if feasible) to confirm response has not drifted

After a run:
- repeat baseline zero check
- repeat the same small check point
- if drift is significant, flag the run for review

---

## 3) Temperature Calibration (Recommended)
- Confirm sensors respond plausibly to a known temperature change.
- Record sensor IDs and placement.
- Avoid self-heating: document excitation current (if using RTDs) and sampling rate.

---

## 4) Accelerometer / Magnetometer Sanity
- Accelerometers:
  - verify gravity vector magnitude and orientation at rest
- Magnetometers:
  - record baseline and verify polarity flips produce consistent direction changes
  - keep away from saturating fields unless you can document range limits

If sensors saturate during a run, the run is not audit-grade.

---

## 5) Calibration Metadata in the Run Manifest (Required)
Every run must include:
- `force_calibration_method`
- `pre_run` calibration note reference
- `post_run` calibration note reference
- `constants` used (k_equiv, slope, offset, etc.)

If you change calibration constants between runs, treat that as a configuration change.

