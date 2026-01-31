# File: docs/08_null_test_suite.md

# Null-Test Suite (Required to Claim Anything)

## Purpose
Null tests are the core of IX-MPMT credibility. They are designed to:
- expose thermal / airflow / vibration / EMI / cable-force artifacts, and
- prove whether any measured force is tied to the intended excitation.

> If you skip null tests, you do not have a “result.” You have a story.

---

## 0) Baseline Requirements (Before Nulls)
Every null suite run must include:
- `force_primary` + `sync_out`
- minimum context channels:
  - `temp_core_shell`, `temp_frame`, `temp_pod_rep`
  - `accel_stand_*`, `accel_rig_*`
  - `mag_*`
- power logs:
  - `vin_source`, `iin_source` (+ buffer logs if present)
- a valid `run_manifest.json` per docs/06

---

## 1) Null Suite Overview (What You Must Run)
You will run the same “Experiment Profile” under multiple conditions:

### Experiment Profile (EP)
Define EP once and keep it fixed across nulls:
- duration
- which channels enabled (pods/core)
- phase map
- code IDs + chip duration
- power level / limits
- environment (open air / enclosure)

Then execute nulls below.

---

## 2) Null Tests (Required Set)

### N1 — No-Excitation Baseline (Noise Floor)
**Goal:** measure drift/noise with the same logging duration.

- Excitation OFF
- All logging ON
- Duration = EP duration

**Pass condition**
- force baseline remains within expected drift bounds
- no unexplained steps or saturations

---

### N2 — Dummy-Load Thermal Match (Heat-Only Control)
**Goal:** match power dissipation without intended external field output.

- Replace emitter pods with dummy pods in the same positions (or configure pods as dummy)
- Run EP with identical power profile and timing

**Pass condition**
- If “force” remains similar to active run, treat effect as thermal/cable/vibe artifact until proven otherwise.
- A credible field-driven effect should be significantly reduced or absent in the dummy match.

---

### N3 — Phase Permutation (Causality / Symmetry Check)
**Goal:** determine whether effect depends on phase mapping rather than bench quirks.

For a 3-channel phase pattern (0/120/240):
- Run EP with Phase Map A:
  - Pod1=0°, Pod3=120°, Pod5=240° (example)
- Run EP with Phase Map B (permute):
  - Pod1=120°, Pod3=240°, Pod5=0°
- Run EP with Phase Map C (permute):
  - Pod1=240°, Pod3=0°, Pod5=120°

(Keep physical pods fixed; only remap phases.)

**Pass condition**
- A real phase-dependent effect should follow predictable changes (document expected behavior).
- If the force stays identical across permutations while EM/mag channels spike similarly, suspect coupling artifacts.
- If correlation/lock-in shows code association shifting incorrectly, suspect time-sync or wiring issues.

---

### N4 — Polarity Flip (Where Applicable)
**Goal:** reveal electrostatic/magnetic coupling artifacts.

- Flip polarity of the relevant excitation (HV polarity, coil current direction, etc.)
- Keep EP timing identical

**Pass condition**
- Magnetic coupling effects often invert with polarity in predictable ways.
- Electrostatic attraction can change magnitude/direction depending on geometry.
- If “force” does not change at all while magnetometer indicates polarity flip occurred, suspect measurement insensitivity or incorrect wiring.

---

### N5 — Position Swap (Pod Role Swap)
**Goal:** determine whether a location-specific bias exists.

- Swap an active emitter pod with a dummy pod between two positions (e.g., Pod1 ↔ Pod4)
- Keep EP identical (same command profile; remap channels accordingly)

**Pass condition**
- A real emitter-driven effect should track the emitter location or the commanded channel, not the physical slot’s bias.
- If the “effect” stays with the same physical slot regardless of which pod is active, suspect mechanical bias, airflow bias, cable routing bias.

---

### N6 — Rotation Test (Directional Truth Check)
**Goal:** verify whether a vector-like force rotates with the rig or stays fixed relative to the room/bench.

**Method (preferred)**
- Rotate entire rig about vertical axis by a known angle (example: 0°, 90°, 180°, 270°)
- Use the indexed mount feature; do not “eyeball” angles
- Keep cabling routing discipline unchanged (same slack management, same guides)

**Pass condition**
- If a true thrust-like vector exists in the rig frame, the measured effect should rotate predictably with the rig (directionality must be defined).
- If the effect stays fixed in the room frame, suspect:
  - airflow gradients in the room
  - cable forces anchored to non-rotating supports
  - bench-level biases
  - magnetic interaction with nearby objects

---

### N7 — Cable Sensitivity Probe (Artifact Trigger)
**Goal:** deliberately test if cables are pushing the rig.

- Keep EP identical
- Perform a controlled, documented cable change:
  - Variant A: standard routing
  - Variant B: slightly different routing (predefined, repeatable alternate path)

**Pass condition**
- Credible results must not change dramatically with minor cable routing changes.
- If force changes strongly, cable forces are dominating. Fix routing before further work.

---

## 3) Required Reporting for Any “Positive” Outcome
If any run shows a meaningful force signature:
- Provide overlays:
  - force + temperature + accel + mag vs time
- Provide CPFS correlation plots vs lag for each channel/code (docs/07)
- Provide null suite table of outcomes in the report narrative:
  - which nulls passed/failed
  - interpretation and next mitigation steps

---

## 4) Stop Conditions (When to Halt and Fix the Rig)
Stop and fix the build if:
- accelerometer shows large vibration spikes aligned to switching edges AND force shows steps
- temperature drift matches force drift AND dummy matches “effect”
- cable routing changes produce large “force” changes
- sensor saturation occurs or time-sync markers are missing

A professional will not accept “we think it’s real” under these conditions.

