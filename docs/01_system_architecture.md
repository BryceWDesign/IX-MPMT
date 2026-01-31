# File: docs/01_system_architecture.md

# IX-MPMT System Architecture (H6-C12)

## Purpose
IX-MPMT is a **micro-force measurement + controlled excitation** platform built to:
- generate repeatable multi-physics excitation conditions, and
- determine whether any observed force is **real** or an **artifact**.

This is achieved through **geometry (symmetry)**, **timing discipline (phase coherence)**, and **proof discipline (null tests + causality checks)**.

---

## Top-Level Configuration: H6-C12
**H6-C12** means:
- **H6**: six identical peripheral pods in a hex ring (60° spacing).
- **C12**: twelve sensor nodes (“skin”) distributed around the test volume.

At the center is a **Core Capsule** (shielded, mechanically stable) that provides a consistent reference volume and mounting interface.

### Physical layout (conceptual)
- Core Capsule at center
- 6 Pods around it (Pod 1..6), evenly spaced
- 12 Sensor Nodes around the test volume (not necessarily a perfect sphere; “even coverage” is the goal)

---

## System Blocks (What exists in hardware)
### 1) Core Capsule
**Job:** provide a stable, shielded reference environment and a standardized mount for:
- DUT (device under test) or emitter cartridge
- internal shielding/thermal control surfaces
- reference sensors (baseline temperature/field)

**Core rules**
- Mechanically stiff and symmetric
- Thermal gradients minimized and monitored
- Cable routing constrained and repeatable

### 2) Pod Modules (x6, identical mechanically)
Each pod can be configured as one of:
- **Emitter Pod** (active excitation)
- **Dummy Pod** (matched electrical load with no intended external field output)
- **Sensor Pod** (optional instrumentation-heavy variant)

**Why identical pods?**
- symmetry reduces bias forces,
- swap testing becomes meaningful,
- null tests become fast and decisive.

### 3) Sensor Skin (x12 nodes)
**Job:** measure the “usual liars” that can mimic thrust:
- temperature gradients (drift/expansion)
- airflow / ionic wind (in-air testing)
- vibration / acceleration (rectification into force)
- EMI / magnetic coupling (cable + chassis forces)
- stray light (photonic heating / sensor contamination)

**Key idea:** Force measurement without context is unreliable. The sensor skin provides context.

### 4) Power Spine (Buffer + Gating + Dump)
**Job:** deliver controlled power while preventing unsafe or misleading behavior:
- current limiting
- dump/load path for stored energy
- interlocks and arming sequence
- measured delivery (voltage/current logged)

This is the “honest power” layer: no guessing, no “scope theater.”

### 5) Timing / Coherence Controller
**Job:** keep all active channels referenced to a shared timing base so:
- phases are known (0°/120°/240° patterns are meaningful),
- modulation codes are deterministic,
- causality checks (correlation/lock-in) are valid.

---

## Measurement Chain (How force is measured)
IX-MPMT is designed to support multiple force sensing approaches, but all must be:
- repeatable,
- calibratable,
- resistant to vibration/thermal artifacts.

Force sensing options (implementation choices in later docs):
- torsion balance / torsion pendulum readout
- flexure beam with optical displacement readout
- high-resolution load cell (only with strict vibration/thermal controls)

**Non-negotiable:** force data must be time-synchronized with all context sensors and excitation commands.

---

## “Coded-Phase Causality” (Core upgrade)
### Concept
Each excitation channel can be driven with a unique **modulation code** (envelope pattern).
During analysis, measured force is correlated against these known codes.

### Why it matters
- Real effects should track the code.
- Artifacts (random drift, ambient vibration, cable creep) usually do not.
- If something *only* appears when a specific code is active and survives nulls, it becomes a credible lead.

---

## Null Test Philosophy (Built into the architecture)
Null tests are not “extra.” The geometry exists to make them easy:
- rotate the rig (force direction should rotate predictably if real)
- permute pod roles (swap emitter vs dummy positions)
- swap phase ordering (0/120/240 mapping)
- polarity flip (where applicable)
- matched dummy loads (same power/heat, no intended field)

If the “force” fails any of these, it is treated as an artifact until proven otherwise.

---

## Interfaces (What plugs into what)
### Mechanical
- Core Capsule mount plane (standard bolt pattern)
- Pod mount rails or indexed positions (repeatable angle/height)
- cable routing channels (fixed path, strain-relieved)

### Electrical
- standardized pod connector (power + control + sense)
- dedicated instrumentation harness separate from power harness where possible
- grounding strategy explicitly defined (star or controlled bus—no ad hoc grounds)

### Data
- single time base for all sampled channels
- raw logs stored with metadata:
  - configuration
  - calibration state
  - ambient conditions
  - null tests performed
  - run IDs and timestamps

---

## Success Criteria (What “works” means here)
IX-MPMT “works” when it can:
1) reproduce a known, explainable effect (baseline validation),
2) show that artifacts are detected and rejected by null tests,
3) produce a dataset that another engineer can audit and reproduce.

The goal is scientific credibility first, novelty second.

