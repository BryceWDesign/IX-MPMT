# File: tests/TEST_PLAN.md

# IX-MPMT Test Plan (Proof-of-Concept Path)

## Goal
Produce a defensible proof-of-concept dataset showing:
1) the rig measures known effects and rejects artifacts, and
2) the methodology is reproducible (audit-grade logging + null suite).

This plan intentionally prioritizes credibility over novelty.

---

## Phase 1 — Bring-Up (No Claims)
### T1.1 Mechanical repeatability
- Verify pod seating stops and core indexing.
- Photograph routing and confirm it matches docs.

**Exit criteria**
- pods seat consistently
- cable routing is fixed and strain-relieved
- no loose parts / rattles

### T1.2 Timing sanity
- Record `sync_out` with no excitation and verify it is captured cleanly.
- Run a “toggle test” where all channels pulse simultaneously into dummy loads.

**Exit criteria**
- `sync_out` markers align with logged events
- channel edges are captured (skew documented)

### T1.3 Sensor health
- Confirm no sensor saturation in typical operating ranges.
- Confirm temperature sensors respond to mild warming.
- Confirm accelerometers and magnetometers show plausible baselines.

**Exit criteria**
- sensor baselines stable
- no clipping / dropouts

---

## Phase 2 — Baseline Validation (Known, Explainable Effect)
Pick ONE known effect for the first PoC dataset (recommended: in-air EHD or a purely resistive thermal step with matched dummy controls).

### T2.1 Baseline run (N1)
- Run no-excitation baseline for EP duration.

**Exit criteria**
- drift quantified and repeatable

### T2.2 Known-effect run
- Run EP with a known mechanism enabled (document mechanism and expectation).

**Exit criteria**
- measured response appears and is time-aligned to commands

### T2.3 Dummy-load match (N2)
- Run EP using dummy-load configuration intended to match heat/power.

**Exit criteria**
- demonstrates whether observed “force” is thermal/artifact vs mechanism-driven

---

## Phase 3 — Null Suite (Mandatory for Credibility)
Run the required null tests from docs/08 using the same EP:

- N1 No-excitation baseline
- N2 Dummy-load thermal match
- N3 Phase permutation set (A/B/C)
- N4 Polarity flip (if applicable)
- N5 Position swap
- N6 Rotation test (0/90/180/270)
- N7 Cable sensitivity probe

**Exit criteria**
- you can clearly label the effect as:
  - “artifact rejected” (most likely early),
  - or “mechanism-confirmed” (e.g., EHD in air),
  - or “requires redesign” (if coupling dominates)

---

## Phase 4 — CPFS Analysis (Causality Proof)
Use docs/07 pipeline.

### T4.1 Correlation extraction
- Compute correlation of force vs each code/channel
- Identify peak correlation and lag

### T4.2 Context overlays
- Overlay force with temperature, accel, mag, airflow proxy (if used)

**Exit criteria**
- causality narrative matches data:
  - if thermal dominates, lag and dummy match should agree
  - if vibration dominates, accel alignment should reveal it
  - if EM dominates, mag spikes align and polarity/rotation tests expose it

---

## Phase 5 — PoC Package (What You Publish)
A “serious” PoC release includes:
- raw data files
- run manifests
- calibration notes (before/after)
- plots (raw + processed)
- null suite outcomes
- CPFS correlation figures
- short report: “what was tested, what passed, what failed, what it means”

This is the package professionals respect.

