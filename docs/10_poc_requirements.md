# File: docs/10_poc_requirements.md

# Proof-of-Concept (PoC) Requirements — What “Works” Means

## Purpose
This document defines what IX-MPMT must include to be taken seriously by professionals:
- a build that is reproducible,
- a measurement chain that is calibratable,
- a null-test suite that is executed and reported,
- and datasets that are audit-grade (raw + metadata + repeatability).

**Important:** IX-MPMT does not accept fabricated or “illustrative” datasets.
Templates are allowed; claims require real measurements.

---

## 1) Minimum PoC Outcome (Baseline Credibility)
A PoC is considered credible only if you can show:

### A) Known-effect validation
Demonstrate at least one **known, explainable mechanism** (choose one):
- in-air EHD ionic wind (air-dependent by nature), OR
- a purely thermal dummy-control demonstration that proves your artifact detection works, OR
- a magnetic interaction test with polarity/rotation predictability (careful: easy to create bench coupling)

This is not about novelty. It is about proving the rig can produce *defensible* conclusions.

### B) Artifact rejection
Run the null suite in `docs/08_null_test_suite.md` and show:
- which nulls pass,
- which fail,
- and how you interpret the results using context channels.

### C) Repeatability
Provide at least **3 repeat runs** of the same profile and show:
- variability bounds,
- consistent timing alignment via `sync_out`,
- consistent correlation behavior (if coded excitation is used).

---

## 2) Required PoC Deliverables (What professionals expect)
For a PoC release, publish:

1) **Assembly evidence**
- photos (top, side, harness routing)
- wiring diagram (power + sense)
- configuration snapshot (pod IDs, roles, sensor node map)

2) **Calibration notes**
- force calibration method and constants
- pre-run and post-run checks
- what changed (if anything) between runs

3) **Raw data + manifest**
- raw logs (immutable)
- `run_manifest.json` per run (complete)
- channel map used

4) **Analysis artifacts**
- scripts/notebooks used to generate plots
- plots:
  - force raw + processed
  - overlays with temp/accel/mag (and airflow proxy if relevant)
  - CPFS correlation results (if used)

5) **Null suite outcomes**
- a table summarizing N1..N7 outcomes
- narrative: what was ruled out, what remains plausible

---

## 3) “No Cheating” Rule (How to avoid self-deception)
A PoC claim is invalid if:
- dummy-load controls were not run,
- rotation or phase permutations were skipped,
- cable routing changed without being a defined null test,
- time sync markers were not recorded,
- sensor saturation or dropouts occurred,
- or you only publish processed plots without raw logs.

---

## 4) PoC Readiness Checklist (Pass/Fail)
You are PoC-ready when:
- [ ] safety + interlocks are implemented and verified
- [ ] `sync_out` is captured and used for alignment
- [ ] force sensor is calibrated (documented)
- [ ] C12 minimum context sensors are logged
- [ ] power spine MP1/MP2 (and ideally MP3) is logged
- [ ] null suite is executed
- [ ] results are repeatable across ≥ 3 runs

If any box is unchecked, label work as “exploratory,” not “PoC.”

