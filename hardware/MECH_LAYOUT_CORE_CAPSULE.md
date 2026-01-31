# File: hardware/MECH_LAYOUT_CORE_CAPSULE.md

# Mechanical Layout — Core Capsule (Shielded Center Module)

## Purpose
The Core Capsule provides a stable, repeatable central module for:
- DUT mounting
- internal shielding
- thermal control surfaces
- reference sensors

It exists to make the outer rig quiet and symmetric while allowing “busy” physics inside.

---

## 1) Core Capsule Functional Requirements
- mechanically stiff enclosure
- repeatable mount interface to the central plate
- controlled cable exit (strain-relieved, fixed direction)
- provisions for:
  - internal mounting rails / rings (nested stages)
  - shielding layers (Faraday / magnetic shielding where appropriate)
  - thermal sensors

---

## 2) Outer Shell Rules (Data Integrity)
- external symmetry favored (reduce asymmetric airflow/drag and electrostatic attraction)
- rounded edges if HV is used (reduce corona/arcing)
- define and document:
  - shell material
  - thickness
  - grounding/shielding scheme

---

## 3) Internal “Nested Stage” Mounting
The internal structure should allow:
- multiple rings/coils/plates to be mounted at defined spacings
- adjustable coupling (distance shims, removable ferrite, damping resistors)
- quick swap of internal cartridges without altering the external shell

---

## 4) Cable Exit & Strain Relief
- one defined exit path (do not “pick a convenient route” per run)
- strain relief anchored to the shell, not to the force-sensitive structure
- separate power and sensor bundles where possible

---

## 5) Assembly Repeatability Features
- orientation key (dowel or keyed flange)
- external labels for “front” and “pod 1 direction”
- repeatable gasket/clamp pressure if sealed

---

## 6) Notes
The Core Capsule is not where “truth” comes from.
Truth comes from:
- controlled geometry,
- time-synced sensing,
- null tests,
- and transparent datasets.

The capsule simply makes that easier by reducing uncontrolled coupling.

