# File: hardware/POWER_SPINE.md

# Power Spine — Buffer, Gating, Dump, and Measurement

## Purpose
The Power Spine exists to do two things **professionals care about**:
1) deliver repeatable power to pods/capsules without unsafe behavior, and  
2) make power delivery **measurable and auditable** so “force” claims can be tied to real electrical conditions.

IX-MPMT does not accept “it was about X watts” estimates. Power must be logged.

---

## 1) Top-Level Power Blocks
### A) Source Supply
- Bench PSU, battery pack, or isolated supply.
- Must be documented per run: model, settings, current limit, voltage.

### B) Buffer (Optional but strongly recommended)
A buffer smooths transients and makes repeat tests consistent.
- Capacitor bank / supercap bank
- Used with **precharge** and **bleeder** paths (see safety docs)

### C) Gating / Switching
- Controlled enable/disable for each active channel (pods / core).
- Must support deterministic timing (for phase coherence and coded excitation).

### D) Dump / Discharge
- A defined load path to safely absorb stored energy when stopping or faulting.
- “Power off” is not sufficient; dump must be real and verified.

### E) Measurement
- Voltage and current must be measured at meaningful points and time-synced with force data.

---

## 2) Required Measurement Points (Minimum)
### MP1 — Source Input
- Source voltage and source current (helps detect supply droop and hidden limits)

### MP2 — Buffer Node (if buffer used)
- Buffer voltage (state of charge)
- Buffer current (charge/discharge during events)

### MP3 — Channel Delivery (per active channel if feasible)
- Channel voltage delivered to pod/core
- Channel current delivered to pod/core

> If you can’t instrument every channel at first, instrument at least the aggregate and one representative channel.

---

## 3) Current Measurement Methods (Acceptable Options)
Use one (or more) and document it:

### Option A — Precision Shunt + Differential Amplifier
- Best for audit-grade current measurement.
- Place shunt in a known location (low-side or high-side) and do it consistently.

### Option B — Hall Effect Current Sensor
- Easier isolation, good bandwidth depending on sensor.
- Must document sensor bandwidth and calibration.

### Option C — Rogowski Coil (advanced)
- Useful for very fast pulsed currents.
- Requires integration and careful calibration; usually not the “first build” choice.

**Non-negotiable:** whatever you use must be time-synced to the data logger.

---

## 4) Buffer + Precharge Requirements (If Buffer Present)
### Precharge
- Must be current-limited.
- Must be observable (buffer voltage rises predictably; log it).

### Bleeders
- Must discharge to touch-safe within a defined, documented time.
- Verify with meter at labeled test points.

### Isolation
- Keep buffer physically close to the switching stage to reduce loop area.
- Keep buffer wiring short and symmetric where possible.

---

## 5) Gating Requirements (What makes it “serious”)
Gating must support:
- deterministic enable/disable timing,
- clean state transitions (avoid oscillation/ringing that confuses measurement),
- fault shutdown that is **hardware enforceable**.

Recommended structure:
- global ARM gate (hardware interlock)
- per-channel enable gate (timing control)

If a channel is “software stopped,” it must still fail safe to OFF if interlock opens.

---

## 6) Dump Path Requirements (Mandatory if Stored Energy Exists)
Dump must be:
- sized for worst-case energy
- thermally safe (won’t ignite or melt)
- connected by default in fault state

Minimum implementation:
- dump resistor bank with a controlled switch OR
- a permanent resistor path sized for safe bleed-down (slower, but simpler)

---

## 7) Wiring Discipline (Power Loop Geometry)
Power loops create:
- EMI (corrupts sensors),
- Lorentz forces (can look like thrust),
- heating (thermal drift).

Rules:
- minimize loop area (route supply and return together)
- avoid large loops near the force measurement axis
- keep each channel’s power loop geometry consistent
- document harness routing and strain relief

---

## 8) Time Sync Requirement (Power ↔ Force Correlation)
All power measurements must share a time base with:
- force measurement channel(s),
- C12 sensor channels,
- excitation command timestamps.

If time sync is missing, causality cannot be claimed.

---

## 9) Run Metadata (Required)
Every run must log:
- source type and settings
- buffer presence + capacity + starting voltage
- gating mode (global/per-channel)
- dump mode (resistor value / method)
- measurement method and sensor IDs
- sampling rates for each measurement point

---

## 10) Acceptance Criteria (Power Spine “Works” When)
- you can repeat the same excitation profile and observe similar MP2/MP3 power traces,
- shutdown reliably dumps/discharges to touch-safe,
- measured power correlates with commanded states and does not show unexplainable drift,
- no fuses/interlocks are bypassed “for convenience.”

The Power Spine is the difference between “cool demo” and “reviewable instrument.”

