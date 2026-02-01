# Assembly Instructions (IX-MPMT H6-C12)

## Goal
Assemble IX-MPMT in a way that is:
- repeatable (pods/sensors return to the same geometry every time),
- safe (interlocks/dump paths are real),
- measurement-clean (cables and thermal behavior do not “push” the rig).

> If you change routing/geometry during a run, you invalidate the dataset.

---

## 0) Tools & Materials (Minimum)
- Torque driver or torque wrench appropriate for your fasteners
- Threadlocker (only where appropriate) + torque stripe/paint marker
- Calipers / ruler for verifying repeatable distances
- Label maker or permanent labels (Pod IDs, Node IDs, Harness IDs)
- Multimeter (required), insulated probes if HV is present
- Zip ties + cable clamps + strain relief hardware (not “dangling wires”)

---

## 1) Mechanical Assembly (Base → Core → Pods)
### Step 1 — Build the base plate / frame
1. Mount the base plate on the bench or isolation platform.
2. Install isolation feet (if used) in the documented locations.
3. Mark the coordinate frame on the base:
   - +X direction (Pod 1 direction)
   - +Z “up” reference

**Data integrity rule:** The base plate orientation becomes part of your dataset. Document it.

### Step 2 — Install the Core Capsule mount
1. Install the core mount plate/bracket at the center.
2. Install an **orientation index** (dowel pin, key, or hard stop).
3. Verify the core mount does not rock or flex under light hand pressure.

**Torque rule:** Use manufacturer torque specs for your fasteners/materials. Record them in notes.
Apply torque stripe so loosening is visible during inspection.

### Step 3 — Install Pod position stops / indexing features
1. Install six pod mounts at 60° spacing (Pod 1..6).
2. Install hard stops so each pod sits at the same radius and angle every time.
3. Verify each mount has the same height reference (pod centerline height).

**Repeatability check:** Seat a pod in each location and verify radius and angle match within your tolerance.

### Step 4 — Mount the Core Capsule
1. Mount the core capsule using the indexed orientation feature.
2. Confirm the “front” of the core points to Pod 1 direction (or document deviation).
3. Confirm the cable exit direction matches your standard.

---

## 2) Sensor Skin (C12) Installation
### Step 5 — Install C12 nodes (Ring A + Ring B or equivalent)
1. Install C12 node mounts in the documented geometry.
2. Apply Node IDs (A1..A6, B1..B6) physically on the mounts.
3. Install sensors and route node wiring to the harness trunk.

**Rule:** Node placement changes are configuration changes. Update the run manifest.

### Step 6 — Install stand and rig-body accelerometers
1. Install stand accelerometer rigidly (no foam tape).
2. Install rig-body accelerometer on the same rigid reference location every time.
3. Label them `S-A` and `R-A`.

---

## 3) Electrical Assembly (Power Spine + Harness Discipline)
### Step 7 — Install Power Spine module
1. Mount source input, buffer (if used), gating, measurement shunts/sensors, and dump path.
2. Verify the dump/bleeder path is physically connected and cannot be “forgotten.”
3. Label touch-safe test points and “verify voltage before touch” points.

**Safety rule:** If you cannot verify discharge with a meter at known points, do not proceed.

### Step 8 — Build the harness trunk (fixed routing)
1. Define one routing path from pods/sensors to the DAQ/power spine.
2. Install cable clamps along that path (repeatable, strain-relieved).
3. Keep power harness and sensor harness physically separated where possible.

**Force rule:** Cables must not pull on force-sensitive elements. Strain relief is mandatory.

### Step 9 — Connect pods using the pod connector standard
1. Install pods with identical cable exit direction.
2. Connect S-Conn (sense/data) first, then P-Conn (power), then HV-Conn (only if used).
3. Verify connector locking and strain relief at pod exit and trunk.

**Artifact rule:** No cable loops near the measurement axis. No free-hanging bundles.

---

## 4) Pre-Run Validation (You must pass these before any “claim”)
### Step 10 — Mechanical preflight
- Verify all torque stripes intact and aligned
- Verify pods seated against stops
- Verify core indexed correctly
- Verify cable routing matches the documented path (photo recommended)

### Step 11 — Electrical preflight
- Interlock loop test: opening any interlock prevents ARM
- Dump/bleeder test: measure discharge time to touch-safe threshold
- Continuity check: no shorts to chassis where not intended
- Sensor readback: plausible baselines, no saturation

### Step 12 — Timing preflight
- Record `sync_out` and confirm capture
- Toggle test into dummy loads to confirm DAQ alignment and edge capture

---

## 5) “Do Not Contaminate the Measurement” Rules (Hard Rules)
- Do not touch the rig during logging (not even lightly).
- Do not re-route cables between runs unless it is a documented null test (N7).
- Do not change pod seating, clamp pressure, or isolation feet mid-campaign.
- Do not add/remove nearby metal tools or magnets near the test volume mid-run.
- Do not filter away the noise and pretend it’s raw.

If any of these are violated, mark the run INVALID in the manifest.

---

## 6) Minimum Assembly Evidence (What professionals expect)
For every PoC campaign, keep:
- 3 photos: top view, side view, harness trunk routing
- a wiring diagram (power + sense)
- run manifests with configuration snapshots
- calibration notes

That is what turns “a build” into an instrument.

