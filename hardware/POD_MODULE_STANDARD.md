# Pod Module Standard (H6 Pods)

## Purpose
The H6 ring only works if each pod is a **standardized, interchangeable cartridge**.
This document defines the minimum mechanical/electrical constraints so swap tests,
nulls, and comparisons remain meaningful.

> If pods are not functionally identical on the outside (mass, geometry, cable exit),
> your “force” results become ambiguous.

---

## 1) Pod Roles (Same Hardware, Different Internals)
Each pod position can be configured as:

### A) Emitter Pod (Active)
A pod containing an excitation element (examples: coil, electrode pair, ultrasonic head)
plus the required driver interface.

### B) Dummy Pod (Matched Load)
A pod containing a matched electrical load intended to:
- draw the same power profile as an emitter run, and
- produce similar heating,
without producing the intended external field output.

### C) Sensor Pod (Optional Variant)
A pod configured with extra context sensors (temperature, magnetic, etc.) while remaining
mass/geometry compatible with the standard pod envelope.

---

## 2) Mechanical Standard (Non-Negotiable)
### External geometry
- All pods share the same **outer envelope** (same dimensions, same mount points).
- All pods share the same **cable exit side/direction**.
- All pods use the same **strain relief method** at the cable exit.

### Mass balance
- Pod total mass must be matched across all pods within a tight tolerance.
- Pod center-of-mass should be approximately consistent across pods.
- If a pod is lighter/heavier (e.g., dummy load vs emitter), add internal ballast.

**Why:** asymmetry creates real forces (gravity torque, vibration response, cable tension).

### Mount interface
- Same bolt pattern / clamp interface for each pod.
- Pods seat against **hard stops** (indexed position) to ensure repeatable radius and angle.
- Pod vertical height must be repeatable (define a reference plane).

---

## 3) Electrical Interface Standard (Pod I/O)
Pod wiring must be standardized so swapping pods does not change:
- cable stiffness
- routing
- connector mass near the rig
- loop areas that create Lorentz forces

### Harness separation rule
Use separate bundles for:
- **Power** (high current / switching)
- **Sense/Data** (low-level sensors, timing)

Do not “share convenient ground returns” across bundles without documenting it.

---

## 4) Pod Connector Classes (Keep HV Separate)
To avoid dangerous and misleading coupling, define connector classes:

### Class P (Power, non-HV)
- Low-voltage, higher-current lines (example: driver supply)
- Must be keyed/locking
- Must have strain relief

### Class S (Sense/Data)
- Sensors, timing reference, control lines
- Shielded cable preferred
- Strain relief required
- Keep away from switching loops

### Class HV (High Voltage, if used)
- HV must be physically isolated from P and S
- Use a dedicated HV-rated connector and HV-rated cable
- Provide clear “touch-safe” test points and discharge strategy (see safety doc)

> If HV is used, treat it as its own subsystem. No exceptions.

---

## 5) Emitter Pod Requirements (If Active)
- Driver and excitation element must be mechanically secure (no rattling, no loose parts).
- Rounded edges / controlled creepage distances for HV elements.
- Document intended external field direction relative to the pod (for symmetry tests).
- Provide temperature sensing at:
  - the primary dissipative element (coil/resistor/driver heatsink), and
  - the pod shell (to track thermal drift).

---

## 6) Dummy Pod Requirements (Matched Load)
A valid dummy pod must match an emitter pod on:
- **power draw profile** (average + transient behavior where relevant),
- **heat dissipation location** (as close as feasible),
- **thermal time constant** (avoid “dummy heats instantly” vs “emitter heats slowly”).

If you cannot match transients, record that limitation and treat comparisons cautiously.

**Minimum dummy design:**
- resistive load bank sized for expected power
- thermal coupling to a similar mass/heat sink arrangement as the emitter pod
- temperature sensor at the load element

---

## 7) Pod ID + Role Map (Required)
Each run must record:
- which physical pod (serial/ID) is in each position (1..6),
- what role it is configured for (Emitter/Dummy/Sensor),
- what connector classes are active (P/S/HV),
- cable routing photo (or reference photo ID).

Without this, the dataset is not auditable.

---

## 8) Symmetry Discipline (How pods support “truth”)
The pod standard exists so you can do decisive tests:
- swap an emitter with a dummy in a different position without changing mechanics
- permute phase ordering across positions
- rotate the entire rig and compare outcomes

If the effect does not survive these symmetry-based nulls, it is treated as an artifact.

