# Mechanical Layout — H6 Hex Ring + Core Capsule

## Purpose
This document defines the **mechanical geometry** and **repeatability constraints** for the IX-MPMT H6 configuration:
- 1x Core Capsule at center
- 6x identical Pods arranged in a hex ring (60° spacing)

The goal is not aesthetics. The goal is:
- symmetry (artifact cancellation),
- indexed repeatability (swap tests),
- controlled cable routing (eliminate hidden forces).

---

## 1) Coordinate System (Reference)
Define a right-handed coordinate system for the rig:
- **+Z**: “up” (opposite gravity)
- **+X**: reference axis (Pod 1 direction)
- **+Y**: completes right-handed frame

All pod positions and sensor placements reference this coordinate system.

---

## 2) Core Capsule Mount Plane
The Core Capsule mounts on a **rigid central plate** with:
- a defined bolt pattern (example: 4-hole square pattern)
- an indexed orientation feature (dowel pin or keyed edge) so “rotation” is measurable and repeatable

### Core mount requirements
- Stiffness: avoid flex under cable strain or thermal growth
- Materials: minimize ferromagnetic content near test volume if doing magnetic tests
- Thermal: provide mounting options for heat sinking or insulation (but document which one is used)

---

## 3) H6 Pod Ring Geometry
### Pod placement
Pods are placed at radius **R_pod** from the center, at angles:

- Pod 1: 0°
- Pod 2: 60°
- Pod 3: 120°
- Pod 4: 180°
- Pod 5: 240°
- Pod 6: 300°

Where angle is measured from +X toward +Y.

### Radius selection (engineering guidance)
Pick R_pod to satisfy:
- sufficient clearance from Core Capsule (no arcing, no mechanical contact)
- space for sensors and cable routing channels
- consistent field interaction distance for comparative tests

**Default guidance:** Start with a radius that leaves at least **2× Core radius** of clearance, then iterate.

---

## 4) Pod Module Mechanical Spec (Identical Cartridges)
Each pod should be physically identical in:
- mass (within a tight tolerance)
- external geometry
- mount interface (same bolt pattern / clamp)
- cable exit direction and strain relief

**Why:** If pods are not identical, “swap tests” become ambiguous.

### Pod mount requirements
- indexed location (stop features so the pod always sits at the same radius and angle)
- defined height reference (pod centerline height relative to base plate)

---

## 5) Cable Routing Rules (Mechanical)
Cable forces are real forces. Routing must be standardized.

### Required routing features
- fixed routing channels or guides from each pod to a common harness trunk
- strain relief at pod exit and at harness trunk
- no free-hanging loops near the measurement axis
- avoid cable contact with any moving/force-sensitive element

### Symmetry rule
As much as practical, each pod’s cable path length and curvature should be matched.

---

## 6) Vibration Isolation & Bench Interface
### Why it matters
Vibration rectification is a major false-positive pathway.

### Minimum requirement
- defined feet locations
- defined isolation approach:
  - either isolation feet, or
  - isolation platform under the entire base plate

Document which is used for each dataset.

---

## 7) Mechanical Repeatability Checks (Before Every Data Run)
- verify pod seating against stops
- verify core capsule orientation index
- verify cable routing matches the documented path
- verify all fasteners are torqued to the recorded spec (or at least marked)

---

## 8) Suggested Build Materials (Non-binding)
Choose materials based on test types:
- For magnetic tests: minimize steel near test volume.
- For HV tests: prioritize insulation, rounded edges, and controlled creepage distances.
- For acoustic tests: stiff mounts reduce spurious motion.

---

## 9) Deliverables in Later Docs
This document defines geometry. Later docs will provide:
- pod connector standard (electrical)
- sensor skin placement (C12)
- assembly steps and torque guidance
- null-test rotation schedule tied to the indexing features

