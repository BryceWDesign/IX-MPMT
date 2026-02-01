# Safety & Interlocks (Non-Negotiable)

IX-MPMT may involve **high voltage**, **stored energy**, **strong magnetic fields**, **ultrasonics**, and **hot surfaces**. These hazards can injure or kill. This document defines the minimum safety controls required for any “serious” build and for producing data that professionals will trust.

> If a configuration cannot be operated safely and repeatably, it is not a valid configuration for IX-MPMT.

---

## 1) Primary Hazards (What can hurt you)
### High Voltage (HV)
- Shock/burn risk, arc flash risk at higher energies.
- HV can jump gaps, travel on contaminated surfaces, and couple into adjacent wiring.

### Stored Energy (Capacitors / Supercaps / Inductors)
- Even “low voltage” supercaps can deliver extreme currents.
- Inductors can generate dangerous voltage spikes during switching.

### Magnetic Fields
- Pinch hazards, projectile hazards, interference with medical implants.
- Magnetic forces can create *real* motion that looks like “thrust” if not controlled.

### Acoustic (Ultrasonic) Systems
- Some ultrasonic transducers/drivers can cause heating, discomfort, or equipment damage.
- High SPL or focused ultrasound requires strict exposure limits.

### Thermal
- Resistors, coils, drivers, and loads can exceed safe touch temperatures quickly.
- Thermal gradients are also a major **measurement artifact source**.

---

## 2) Safety Architecture (Minimum Required Controls)

### A) Master Power Control
**Required**
- Physical **master disconnect** (hard power cut).
- **E-stop** that removes power from all drivers (not just “software stop”).
- A **keyed enable** (or guarded switch) for “ARM.”

**Rationale**
- Professionals expect layered controls: disconnect → e-stop → arm.

### B) Current Limiting (HV and non-HV)
**Required**
- Explicit current limiting for HV stages (series resistor network and/or controlled source).
- Fusing sized to wiring and connectors (not to “what you hope happens”).
- Inrush limiting for any capacitor bank (precharge path).

**Rationale**
- Prevents catastrophic failures and keeps tests repeatable.

### C) Dump / Discharge Path (Energy Must Have Somewhere Safe to Go)
**Required**
- A defined **dump load** for stored energy (resistor bank or controlled load).
- A defined **bleeder path** that discharges capacitors when power is removed.
- A clear, measurable **“safe voltage” threshold** (example: < 30 V) before handling.

**Rationale**
- “I turned it off” is not a discharge strategy.

### D) Interlock Loop (Hardware, Not Just Firmware)
**Required**
- A simple hardware interlock loop that must be closed for “ARM.”
- Recommended interlock elements:
  - enclosure lid switch (if using a HV enclosure)
  - E-stop chain
  - “bleeders OK” / “dump connected” status
  - thermal over-limit switch on primary load elements

**Rationale**
- Hardware interlocks reduce single-point human error.

---

## 3) Required Operating States (State Machine)

### STATE 0 — SAFE / DISARMED
- Master power off OR drivers disabled.
- Dump/bleeder engaged by default.
- No HV enabled.

### STATE 1 — PRECHECK
- Visual + meter verification:
  - no exposed conductors
  - cable routing correct (strain relief, symmetry)
  - sensor wiring separated from power wiring where possible
  - dump/bleeder connected and measured functional

### STATE 2 — PRECHARGE (if capacitor bank present)
- Precharge path engaged (limited current).
- Voltage rises under control.
- Transition only when stable.

### STATE 3 — ARMED
- Keyed enable on.
- Interlock loop closed.
- Drivers allowed to operate, but only after “run start” command.

### STATE 4 — RUN
- Active excitation.
- Continuous monitoring for:
  - overcurrent
  - overtemperature
  - unexpected voltage rise
  - loss of interlock
  - sensor saturation (invalid data)

### STATE 5 — FAULT / E-STOP
- Drivers disabled immediately.
- Dump/bleeder engaged.
- Log the fault condition and mark the run invalid unless proven otherwise.

---

## 4) “Do Not Fool Yourself” Rules (Safety + Data Integrity)
These rules also prevent false thrust.

1. **No free-hanging wires near the measurement axis.**  
   Cable forces are real forces.

2. **No unmonitored heating.**  
   Thermal drift will produce apparent force on many stands.

3. **No ad hoc grounds.**  
   Ground loops can create forces (and bad data) via EMI coupling.

4. **No running without a dump path.**  
   Stored energy must always have a safe place to go.

5. **No “software-only” safety.**  
   Hardware must be able to shut it down.

---

## 5) Minimum PPE / Lab Discipline
- Eye protection for any HV or high-energy switching work.
- Keep one hand away from the system when probing HV (“one-hand rule”).
- Remove jewelry; secure loose clothing.
- Operate with a clear “hot zone” boundary; no bystanders near the rig.
- Never work alone if HV or high stored energy is present.

---

## 6) Required Verification Before Touching Hardware
**You must verify both conditions:**
- **Energy is removed** (master disconnect off), AND
- **Energy is discharged** (measure voltage at defined test points)

Define “touch-safe” thresholds and put them on labels near test points.

---

## 7) Labels & Physical Marking (Professional expectation)
Minimum labels:
- ARMED indicator
- HV present indicator
- Discharge status indicator (or “wait time + verify voltage” instruction)
- “Do not touch” on hot loads/coils
- Interlock diagram (simple: what must be closed)

---

## 8) What Makes a Build “Professional-Serious”
A professional reviewer will look for:
- documented state machine and interlocks,
- explicit dump/bleeder strategy,
- current limiting and fusing aligned to wiring/connectors,
- safe, repeatable procedures (not improvisation),
- evidence that safety and data integrity were considered together.

If any of those are missing, the rig will be treated as a hobby hazard—not an R&D instrument.

