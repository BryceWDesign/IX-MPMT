# File: hardware/SENSOR_SKIN_C12.md

# Sensor Skin — C12 (12-Node Context Instrumentation)

## Purpose
C12 is a 12-node sensor “skin” that surrounds the test volume to measure the main
false-positive pathways in micro-force experiments. Force data without context is
not trusted; C12 provides the context needed to validate or reject a result.

C12 is not about adding complexity. It is about **making artifacts visible**.

---

## What C12 Measures (The “Usual Liars”)
Each run should include time-synced measurements of:

1) **Thermal gradients**
- Core shell temperature
- Pod temperatures (at least a representative subset)
- Stand/frame temperature near the force sensor

2) **Vibration / acceleration**
- Stand acceleration (3-axis)
- Rig-body acceleration (3-axis)
- Optional: additional nodes to localize vibration sources

3) **Magnetic / EMI context**
- 3-axis magnetic field near test volume (at minimum)

4) **Airflow / pressure / humidity (for in-air testing)**
- airflow proxy (hot-wire, differential pressure, or flow sensor)
- ambient pressure and humidity (helps interpret EHD and convection sensitivity)

5) **Stray light / radiative heating**
- photodiode to detect sudden changes in illumination that can heat surfaces
  or bias optical readouts

---

## C12 Geometry (Node Placement)
### Goal: even coverage, repeatable placement
The exact mechanical embodiment can vary, but node placement must be:
- repeatable (indexed),
- documented (photos + distances),
- time-synced across channels.

### Recommended conceptual layout (12 nodes total)
- **Ring A (upper)**: 6 nodes at 60° spacing, radius R_skin, height +Z
- **Ring B (lower)**: 6 nodes at 60° spacing, radius R_skin, height -Z
- Ring B is rotationally offset by 30° relative to Ring A (optional but recommended)
  to avoid blind directions.

This yields good angular coverage without requiring a perfect sphere.

> If you change R_skin or Z offsets, record it as a configuration change.

---

## Node Types (Standardized Roles)
To keep the system serious and interpretable, each node should have a defined role.

### Node role set (recommended)
- **T-node (Temperature):** precision RTD/thermistor + local board temp
- **A-node (Acceleration):** low-noise 3-axis accelerometer (or IMU accel)
- **M-node (Magnetic):** 3-axis magnetometer
- **P-node (Pressure/Humidity):** ambient P/RH (in-air testing)
- **L-node (Light):** photodiode + amplifier (stray light)

You do NOT need every node to carry every sensor.
You DO need enough redundancy that you can:
- detect gradients,
- detect vibration rectification,
- detect magnetic coupling,
- detect airflow/EHD sensitivity.

### Practical C12 composition (example that stays sane)
- 4 × T-nodes (distributed: two upper, two lower)
- 2 × A-nodes (one on stand, one on rig body — these can count as two of the 12)
- 2 × M-nodes (opposed locations for gradient detection)
- 2 × P-nodes (upper/lower or upstream/downstream in enclosure)
- 2 × L-nodes (opposed locations)

Total = 12 instrument points (nodes). Some nodes may be “stand-mounted” rather than ring-mounted;
that is acceptable if documented as part of the C12 map.

---

## Sensor Performance Targets (What “serious” looks like)
These are targets, not mandates, but they define the intent.

### Temperature (T)
- Resolution: ≤ 0.05 °C preferred
- Stability: predictable drift, known self-heating
- Sampling: 1–10 Hz is typically sufficient (thermal is slow)

### Acceleration (A)
- Low noise density preferred (vibration artifacts can be subtle)
- Sampling: ≥ 200 Hz recommended (higher if strong switching/vibration present)
- Mount: rigid, repeatable, no foam tape “for convenience”

### Magnetic (M)
- Sampling: 50–200 Hz recommended (capture switching and coupling)
- Placement: keep away from high-current loops but close enough to measure context

### Pressure/Humidity (P)
- Sampling: 1–10 Hz sufficient
- Use for documenting ambient sensitivity and EHD repeatability

### Light (L)
- Sampling: 50–200 Hz optional
- Use for detecting sudden illumination changes that can heat or corrupt optical readouts

---

## Electrical / Data Requirements
### Time synchronization
All C12 channels must be time-synced to the same clock used for:
- excitation commands,
- phase/coherence reference,
- force measurement channels.

### Wiring discipline
- C12 harness routing must be fixed and documented.
- Avoid large loop areas near high-current paths.
- Keep sensor wiring separated from power wiring where feasible.

### Calibration metadata
Each run must record:
- sensor IDs / serials
- calibration date/state (if applicable)
- placement map (Node ID → location)

---

## Node ID Convention (Required)
Use a consistent ID scheme:
- Ring A: A1..A6 (clockwise from Pod 1 direction)
- Ring B: B1..B6 (clockwise, offset if used)
- Stand accel: S-A
- Rig-body accel: R-A

If you substitute S-A or R-A into the 12 total nodes, document it clearly.

---

## Minimum Acceptance Checks (Before Any “Claim”)
A dataset is not considered credible unless:
- temperatures show no uncontrolled drift OR drift is matched by dummy-load controls
- accelerometers show vibration is either low or accounted for
- magnetometers show coupling events are identified and compared to polarity/phase swaps
- pressure/humidity is logged for in-air EHD work
- sensor saturation is absent (no clipping)

---

## Bottom Line
C12 is what lets IX-MPMT answer the only question that matters:
“Did we measure a real effect, or did the rig lie?”

Without C12-class context data, professionals will assume the latter.

