# File: docs/05_timing_and_coherence.md

# Timing, Phase Coherence, and Coded Excitation (What “Coherent” Means)

## Purpose
IX-MPMT requires **deterministic timing** so that:
- phase relationships are known and repeatable,
- modulation codes can be correlated against measured force,
- null tests (phase permutations, polarity flips, rotation) are meaningful.

“Coherent” here means **time-locked to a shared reference clock** with controlled phase.

---

## 1) Definitions (Plain Language)
### Shared Reference Clock
A single timing source used by:
- excitation generation (pods/core),
- DAQ sampling timebase (or at minimum a synced trigger),
- event timestamps (start/stop, phase map, code ID).

### Phase Coherence
The ability to command and maintain known phase offsets between channels
(e.g., Pod A = 0°, Pod B = 120°, Pod C = 240°) at a selected frequency.

### Coded Excitation (Envelope Coding)
A deterministic on/off or amplitude envelope pattern (a “code”) applied to a channel,
so you can later test whether measured force correlates with that channel’s code.

---

## 2) Why This Matters (Professional Reason)
Micro-force signals are typically near the noise floor. Without coherent timing:
- drift and artifacts can masquerade as “effects,”
- run-to-run comparisons degrade,
- and causality becomes guesswork.

With coherent timing:
- you can do correlation/lock-in style extraction,
- you can prove whether an observed signal is synchronized to a command pattern,
- and you can separate “physics response” from “bench nonsense.”

---

## 3) Minimum Timing Architecture (Buildable, Not Exotic)
IX-MPMT supports multiple implementation choices. Pick one and document it.

### Option A — DAQ-Clock-Led (Preferred for serious measurement)
- DAQ provides a master sample clock and a hardware trigger out.
- Excitation controller receives trigger/clock reference.
- All logs reference the DAQ timebase.

Pros: tight sync between measurement and command.  
Cons: depends on DAQ features.

### Option B — Controller-Clock-Led (Practical early build)
- A dedicated controller generates:
  - excitation waveforms (or gate signals),
  - a sync pulse (“SYNC OUT”) to mark code boundaries,
  - timestamps for run state transitions.
- DAQ records SYNC OUT alongside force and C12 signals.

Pros: simple; still auditable if SYNC is captured.  
Cons: phase accuracy depends on controller and wiring.

### Option C — FPGA/Timing Module (Highest performance, more work)
- FPGA generates multi-channel phase-locked outputs and codes.
- Hardware timestamping built-in.
- DAQ uses shared ref clock or sync capture.

Pros: best determinism.  
Cons: more complexity.

---

## 4) Practical Phase-Coherent Channel Model
Define channels as:
- CH0..CH5 (Pods 1..6)
- CH6 (Core Capsule driver / internal stage gate)

For each channel define:
- carrier frequency `f0` (if applicable)
- phase offset `phi` (degrees)
- envelope code ID `Ck`
- duty/amplitude profile
- enable window (start/stop times)

### Minimum required phase features
- ability to set at least:
  - 0° / 120° / 240° on any 3 selected channels, and/or
  - symmetric pairs (0°/180°) for inversion tests
- ability to permute phase-to-position maps:
  - example: (Pod1=0, Pod3=120, Pod5=240) then swap mapping next run

---

## 5) Coded Excitation: What Code Must Look Like
A “code” must be:
- deterministic (same every time for a given ID)
- time-bounded (defined symbol length / chip length)
- recorded in metadata and in the controller output (SYNC markers)

### Minimum viable code set
- Code A: pseudo-random binary sequence (PRBS) or fixed pattern
- Code B: different PRBS/pattern (low cross-correlation with A)
- Code C: third pattern

You do not need dozens of codes. You need **2–3** that are distinguishable.

### Required logging
Every run must log:
- code IDs used per channel
- code chip duration
- code start time marker (SYNC OUT)
- carrier frequency (if used)

---

## 6) Sync Signal (“SYNC OUT”) Requirement
Regardless of timing architecture, you must provide a recorded sync channel:
- SYNC OUT is a digital pulse marking:
  - start of run
  - code epoch boundaries (optional but recommended)
  - state transitions (ARM/RUN/STOP)

The DAQ must record SYNC OUT so analysis can align command ↔ measurement even if clocks drift.

---

## 7) Timing Error Budget (Don’t Overpromise)
You must document expected timing uncertainty sources:
- controller clock tolerance (ppm)
- jitter on output edges
- propagation delay differences between channels (wiring length)
- DAQ sampling alignment error

If you do not know the numbers yet, state that they are TBD and treat early results as exploratory.

---

## 8) Acceptance Tests (Prove Timing is Real)
Before interpreting “force,” prove your timing chain:

1) **Edge alignment test**
- drive all channels with identical toggles
- record with DAQ
- verify relative timing skew is within your stated tolerance

2) **Phase verification test**
- generate a known sine/phase pattern (or square-wave phase pattern)
- record with DAQ
- confirm commanded phase ordering matches measured ordering

3) **Code detectability test**
- run Code A on one channel into a dummy load
- confirm analysis detects Code A strongly on that channel and not on others

If these fail, do not interpret micro-force data as meaningful.

---

## 9) Bottom Line
Coherence is not a buzzword here.
It is the mechanism that makes IX-MPMT:
- repeatable,
- auditable,
- and capable of proving causality.

Without it, you can still build a rig, but professionals will treat results as ambiguous.

