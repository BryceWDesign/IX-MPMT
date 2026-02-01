# Artifact Kill-List (How Micro-Force Tests Lie)

Micro-force rigs are easy to fool. This document lists the most common false-positive
pathways and the required controls / tests to detect them.

> Rule: If an observed “force” can be explained by any item below and you have not
> explicitly ruled it out, the result is INVALID.

---

## 1) Thermal Drift (Most Common)
### What happens
- Heating causes expansion, warping, buoyancy changes, and sensor offset.
- Thermal gradients can create convection currents (in air) that push the rig.

### Signs
- Slow ramp over minutes.
- Correlates with temperature (even weakly).
- Changes when you add insulation or a fan.

### Required controls
- Log temperatures at multiple points (core + pods + stand).
- Use dummy-load runs that match power dissipation.
- Run “heater-only” trials with identical heat but no intended field output.

### Required null tests
- Same power, different configuration: effect should vanish if field-driven.
- Reverse on/off timing: thermal effects lag; real field effects should be immediate.

---

## 2) Airflow / Ionic Wind (EHD) and Convection
### What happens
- HV in air can generate ionic wind (real thrust in air).
- Heating creates convection currents (also real airflow forces).

### Signs
- Large changes with airflow blockage, enclosure changes, humidity, or distance to surfaces.
- Effect disappears or changes strongly in still-air vs enclosed volume.

### Required controls
- Flow sensor(s) or hot-wire anemometer near test volume (if in-air).
- Humidity and pressure logs (at least basic ambient logs).
- Physical airflow baffles for repeatability.

### Required null tests
- Same run in a sealed enclosure vs open air.
- If possible, reduced pressure / vacuum trial:
  - If the effect collapses with pressure, it’s almost certainly air-driven.

---

## 3) Cable Forces (Hidden “Thrusters”)
### What happens
- Stiff wires act like springs.
- Cable heating changes stiffness and routing.
- EMI induces currents that create Lorentz forces on cable loops.

### Signs
- Force depends on cable position or strain relief.
- Force changes when you reroute cables or change connector orientation.
- Force is asymmetric in certain rig orientations.

### Required controls
- Fixed cable routing channels and strain relief.
- Symmetric harness design.
- Separate power harness from sensor harness where possible.
- No free-hanging cable loops near the measurement axis.

### Required null tests
- Replace active pod with dummy load and keep cable identical.
- Rotate rig: cable-based forces often rotate incorrectly or change magnitude.

---

## 4) Vibration Rectification (Shaker → Net Force)
### What happens
- Vibration couples into nonlinear elements (friction, loose joints, flexures),
  producing a DC bias that looks like thrust.

### Signs
- Force depends strongly on bench, feet placement, or nearby equipment.
- High accelerometer readings during “thrust” events.
- Effect changes with added mass or damping.

### Required controls
- 3-axis accelerometer on the stand and on the rig body.
- Mechanical tightness checks and torque markings.
- Isolation feet or vibration isolation stage.

### Required null tests
- Run the same excitation with the rig mechanically constrained:
  - If “force” changes dramatically, it’s likely rectification.
- Add a controlled vibration source and verify the rig rejects it.

---

## 5) EMI Coupling / Magnetic Interaction
### What happens
- Current loops interact with Earth’s field, nearby steel, magnets, or sensor housings.
- EMI can corrupt sensors and create apparent shifts in force readouts.

### Signs
- Effect changes with nearby metal objects or tool placement.
- Magnetometer spikes coincide with “force.”
- Different behavior at different bench locations.

### Required controls
- Magnetometer logs (at least one near test volume).
- Keep ferromagnetic materials away from field regions.
- Controlled grounding strategy; minimize loop areas.

### Required null tests
- Polarity flip: true magnetic coupling should invert predictably.
- Rotate apparatus: EMI/magnetic artifacts often change with orientation.

---

## 6) Electrostatic Attraction
### What happens
- HV can attract nearby surfaces (plates, enclosures) producing net force.

### Signs
- Effect depends strongly on distance to nearby conductive surfaces.
- Large changes with added grounded shield plates.

### Required controls
- Known, repeatable distances to nearby surfaces.
- Use Faraday shielding where required.
- Explicit grounding of shields (documented).

### Required null tests
- Move a grounded plate closer/farther:
  - If effect scales with distance, suspect electrostatics.

---

## 7) Sensor Saturation / Offset / Drift
### What happens
- Load cells and amplifiers drift.
- ADCs clip.
- Thermal changes shift sensor offsets.

### Signs
- Flat-topped signals, sudden steps, or slow baseline wander.
- Different results after power cycling.

### Required controls
- Calibrate before/after runs with known masses/forces.
- Log sensor supply rails and temperature.
- Use redundant sensing where feasible (e.g., optical displacement + load cell).

### Required null tests
- Zero-load baseline runs (no excitation) at same duration.
- Known input step response check (calibrator pulse).

---

## 8) “Too Clean” Data (Suspicious Smoothness)
### What happens
- Over-filtering hides dynamics.
- Plotting a processed signal as “raw” misleads review.

### Signs
- Perfect ramps with no noise floor.
- Identical curves run-to-run with no scatter.

### Required controls
- Always store raw logs.
- Provide both raw and processed plots.
- Document filtering parameters.

---

## 9) Data Validity Rules (Pass/Fail)
A run is **VALID** only if:
- all sensors stayed within range,
- all required context channels are logged,
- the configured null tests were performed,
- the effect correlates with commanded excitation (coded-phase / lock-in),
- repeat runs show consistent magnitude and timing,
- at least one artifact pathway is explicitly ruled out.

A run is **INVALID** if:
- you changed cable routing mid-run,
- temperature was unlogged or uncontrolled,
- any required null test was skipped,
- the effect disappears or flips unpredictably with simple configuration changes.

---

## 10) Bottom Line
IX-MPMT is valuable because it **forces truth**:
it either produces an effect that survives these tests, or it documents exactly
why the effect is an artifact.

That is what professionals pay for.

