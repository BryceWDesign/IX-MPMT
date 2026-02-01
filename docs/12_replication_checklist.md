# Replication Checklist (What a Reviewer Can Follow)

## Purpose
This checklist is designed so a third party can replicate your process and judge outcomes
without trusting narration. If you cannot provide the items below, label results
“exploratory,” not “proof.”

---

## A) What You Must Provide (Minimum Package)
### A1 — Build evidence
- [ ] 3 photos: top view, side view, harness trunk routing
- [ ] Mechanical notes:
  - [ ] core capsule indexed orientation method
  - [ ] pod seating/stop method (repeatable placement)
- [ ] Wiring diagram:
  - [ ] power spine (source → buffer → gating → dump)
  - [ ] sense/data harness routing and shield termination choice
- [ ] Safety proof:
  - [ ] interlock behavior demonstrated (what happens when opened)
  - [ ] dump/bleeder discharge time measured to touch-safe threshold

### A2 — Data evidence
- [ ] Raw data files (immutable) for every run
- [ ] run_manifest.json for every run (validated)
- [ ] Plots:
  - [ ] force raw + processed
  - [ ] overlays (force + temp + accel + mag; add airflow proxy if in-air)
  - [ ] CPFS correlation vs lag (if coded excitation used)
- [ ] Null suite outcomes table (N1..N7) with pass/fail per run

### A3 — Calibration evidence
- [ ] Force calibration method described
- [ ] Pre-run and post-run calibration checks documented
- [ ] Any drift flagged and handled

---

## B) What the Reviewer Does (Replication Steps)
### Step 1 — Confirm rig discipline
- [ ] Core capsule indexing exists and is used
- [ ] Pod modules are externally identical and swap-ready
- [ ] Cable routing is fixed and strain-relieved (no free-hanging loops)

### Step 2 — Confirm safety state machine is real
- [ ] Interlock prevents ARM
- [ ] Dump/bleeder discharges stored energy to touch-safe threshold
- [ ] E-stop / master disconnect behavior is clear

### Step 3 — Confirm time sync is not hand-waved
- [ ] sync_out is recorded
- [ ] run start/stop markers exist
- [ ] analysis aligns runs using sync_out (not “eyeballing”)

### Step 4 — Confirm baseline
- [ ] N1 baseline run (no excitation) shows quantified drift/noise floor

### Step 5 — Confirm a known-effect validation
- [ ] one known mechanism run is performed (document mechanism and expectation)
- [ ] context channels confirm plausible signatures

### Step 6 — Confirm dummy-load control
- [ ] N2 dummy-load match is performed
- [ ] power traces are similar (MP1/MP2 at least)
- [ ] outcome is interpreted honestly (if dummy matches “effect,” treat as artifact)

### Step 7 — Confirm null suite executed
- [ ] N3 phase permutation set executed (A/B/C maps)
- [ ] N4 polarity flip executed (where applicable)
- [ ] N5 position swap executed
- [ ] N6 rotation test executed (0/90/180/270 or documented angles)
- [ ] N7 cable sensitivity probe executed (controlled, documented alternate routing)

### Step 8 — Confirm CPFS causality (if used)
- [ ] correlation peaks repeat across runs with plausible lag
- [ ] correlation differs across codes/channels as expected
- [ ] context channels do not provide a simpler explanation (thermal/vibe/EM/airflow)

---

## C) Pass/Fail Rules (Reviewer Verdict)
A “credible effect lead” requires ALL:
- [ ] survives dummy-load match (or has a clearly justified reason it should not)
- [ ] behaves predictably under rotation and/or phase permutations
- [ ] shows causality via sync/correlation (if coded)
- [ ] repeatability across ≥ 3 runs (with quantified scatter)
- [ ] artifacts explicitly ruled out with context channels

If any is missing → label “artifact/inconclusive” until fixed.

---

## D) What Professionals Want To See
- disciplined geometry
- disciplined logging
- disciplined nulls
- raw data
- honest interpretation

That is what makes this a tool, not a story.

