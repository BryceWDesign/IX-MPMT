# File: docs/07_coded_phase_analysis.md

# Coded-Phase Analysis (CPFS) — Correlation / Lock-In for Causality

## Purpose
IX-MPMT uses **coded excitation** so you can prove causality:
- If an observed force is real and driven by a channel,
  it should **correlate with that channel’s code** (with a physically plausible delay).
- If it does not correlate, it is likely drift/artifact/noise.

This is how you avoid “looks like thrust” traps.

---

## 1) Inputs Required (Per Run)
To run CPFS analysis, you need time-synced logs of:
- `force_primary` (or `disp_primary` + stiffness conversion documented)
- `sync_out` (recorded)
- excitation metadata:
  - code IDs per channel (e.g., CH0=CodeA, CH1=CodeB)
  - chip duration (seconds)
  - code start time (from sync_out markers)
  - any carrier frequency (if applicable)

And context channels for sanity:
- temperatures, vibration, magnetometer (at least the minimum C12 subset)

---

## 2) What CPFS Produces (Outputs)
For each channel/code, CPFS produces:
- **correlation score** vs lag (seconds)
- **peak correlation** and the lag where it occurs
- **sign and consistency** across repeat runs
- optional: coherence estimate vs frequency (if using lock-in at a carrier)

---

## 3) Correlation vs Lock-In (When to Use Which)
### A) Correlation (Envelope coding)
Use correlation when your excitation is encoded as:
- on/off bursts
- amplitude steps
- PRBS-like envelope patterns

This is the default IX-MPMT approach.

### B) Lock-In (Carrier-based)
Use lock-in when you drive a known carrier frequency (e.g., sinusoid) and modulate it.
Lock-in extracts the in-phase and quadrature response at that carrier.

If you aren’t explicitly measuring a carrier response, do not overcomplicate early builds.
Start with envelope correlation first.

---

## 4) Interpretation Rules (Avoid Fooling Yourself)
### Rule 1: Correlation must beat the nulls
A correlation peak is not enough.
It must also survive:
- phase permutations (where meaningful),
- dummy-load matched-heat trials,
- rotation/null suite outcomes.

### Rule 2: Check for “artifact correlation”
Some artifacts will correlate with code (because the code controls power/heat).
That’s why you must cross-check:
- temperature channels (thermal lag signatures),
- accelerometer channels (vibration signatures),
- magnetometer channels (EM coupling signatures),
- airflow proxy (EHD/convection signatures).

If force correlates with code AND temperature correlates strongly with the same code,
treat the effect as thermal until proven otherwise.

### Rule 3: Lag must be physically plausible
- EHD/airflow effects: can be near-immediate to short delay
- magnetic coupling forces: near-immediate
- thermal drift: typically slower (seconds to minutes), smoother
- mechanical vibration rectification: correlated with switching edges + accel spikes

If your best correlation appears at an implausible lag, it’s likely coincidence or misalignment.

---

## 5) Minimal CPFS Workflow (Per Run)
1) Align time using `sync_out` markers (run start, code epochs).
2) Build the expected code waveform in time (chip duration, code bits).
3) Compute normalized cross-correlation:
   - force vs codeA, force vs codeB, etc.
4) Report peak correlation and lag.
5) Overlay force with:
   - temperature, acceleration, magnetic channels
   to identify likely artifact pathways.
6) Repeat across runs and compare:
   - peak correlation consistency
   - lag consistency
   - magnitude consistency

---

## 6) Acceptance Criteria (What “credible” looks like)
A channel is a credible causal driver only if:
- force correlation is strong and repeatable,
- the effect survives dummy-load trials (matched heat),
- the effect behaves predictably under rotation/phase permutations,
- context channels do not show a simpler artifact explanation.

---

## 7) Deliverables Required in a “Serious” Report
For each claim, include:
- raw data
- run manifest
- correlation plots vs lag for each channel
- overlays (force + temp + accel + mag)
- null test results and conclusions

If any are missing, professionals will treat the conclusion as unproven.

