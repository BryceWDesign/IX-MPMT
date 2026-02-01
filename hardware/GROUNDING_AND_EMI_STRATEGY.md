# Grounding & EMI Strategy (So the Rig Doesn’t Push Itself)

## Purpose
Bad grounding and EMI create two problems:
1) corrupted measurements, and  
2) **real forces** from current loops interacting with magnetic fields and nearby conductors.

This document defines minimum grounding discipline for credible micro-force work.

---

## 1) Core Principles
### Principle A — One intentional return path
Every signal must have a defined return. “It returns through the chassis somewhere” is not acceptable.

### Principle B — Minimize loop area
Loop area is proportional to:
- radiated EMI,
- induced noise,
- and magnetic force coupling.

### Principle C — Separate domains, bond intentionally
Keep domains separate and bond at defined points:
- Power domain
- Sense/Data domain
- Shield/Chassis domain

If you bond them, do it once, on purpose, and document it.

---

## 2) Recommended Grounding Topologies (Choose One and Stick to It)
### Option 1 — Star Ground (Preferred early build)
- One defined “star point” near the power entry / measurement hub.
- Power returns and sense returns meet only at the star point.
- Shields bond at the star point (or at the DAQ end), per documented decision.

Pros: easy to reason about.  
Cons: can become messy at high frequencies.

### Option 2 — Controlled Bus Ground (Advanced)
- Short, low-impedance ground bus with defined tap points.
- Requires careful layout to avoid unintended current sharing.

Pros: better for higher frequency currents if done correctly.  
Cons: easier to do wrong.

---

## 3) Shielding Rules
- Sensor cable shields should be terminated consistently (document whether one-end or both-end).
- Do not “float” shields randomly per run.
- Faraday shields must have a defined connection to chassis/ground.

---

## 4) EMI Containment Rules (Practical)
- Twist power supply/return pairs.
- Twist signal/return pairs.
- Physically separate:
  - switching power wiring
  - sensor/DAQ wiring
- Avoid routing sensor wiring parallel to switching loops for long distances.
- Use ferrites only if documented (ferrites can change behavior; they are not invisible).

---

## 5) Force-Artifact Rule (The One Professionals Notice)
Any current loop near the force measurement axis can create a Lorentz-force bias.
To control this:
- keep loop areas small,
- keep wiring symmetric around the axis,
- lock cable routing using guides and strain relief.

If “force” changes when cable routing changes, your rig is lying.

---

## 6) Minimum EMI/Force Diagnostics
To make the system reviewable, log:
- magnetometer channel(s) near test volume (C12 M-nodes)
- accelerometer channels (C12 A-nodes)
- power traces (MP1–MP3)

If a force spike coincides with a magnetometer spike and a switching edge, assume coupling until ruled out by nulls.

---

## 7) Acceptance Criteria (Grounding/EMI “Good Enough” When)
- repeated runs show consistent noise floor and baseline stability,
- sensor channels do not saturate during switching events,
- permuting pod phases does not create unexplained “force” sign changes,
- cable re-route tests do not significantly change results (within expected uncertainty).

---

## 8) Documentation Requirement
For every “serious” dataset include:
- a wiring diagram (power + sense)
- grounding topology choice (star/bus)
- shield termination choice
- a photo of the harness routing

If a reviewer cannot reconstruct your wiring, they will not trust your conclusions.

