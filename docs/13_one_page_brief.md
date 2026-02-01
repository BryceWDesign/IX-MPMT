# IX-MPMT — One-Page Brief (For Professional Review)

## What it is
IX-MPMT (IX Multi-Physics Micro-Force Testbed) is a **symmetry-driven micro-force measurement and field-excitation platform** built to produce **audit-grade, repeatable evidence** when evaluating small-force and non-contact actuation concepts.

It is designed to answer one question reliably:
**“Is the observed force real, and what caused it?”**

## What it is NOT
- Not “antigravity.”
- Not a propulsion claim.
- Not a finished commercial instrument.

It is a **falsification-first testbed**.

## Why it exists
Micro-force experiments are extremely prone to false positives from:
- thermal drift and convection,
- ionic wind (in air),
- vibration rectification,
- EMI coupling and cable forces,
- electrostatic attraction to nearby surfaces.

IX-MPMT is built to expose these quickly and decisively.

## Core architecture (H6-C12)
- **H6:** 6 identical pods in a hex ring (swappable emitter/dummy roles)
- **C12:** a 12-node sensor “skin” measuring context (temp/accel/mag/airflow/light)
- **Core capsule:** shielded central module with standardized mounting and routing

## Key differentiator (what makes it higher value)
**Coded-phase causality (CPFS):**
- each channel can be driven with a deterministic modulation code and phase map
- force measurements are correlated/lock-in analyzed against codes
- effects must survive null tests (rotation, permutations, dummy-load matching)

This shifts evaluation from “looks like thrust” to **provable causality**.

## What you get from this repo
- safety + interlocks + dump path requirements
- mechanical symmetry specs (pods/core)
- sensor skin requirements (C12)
- DAQ + audit logging standards (manifests, channel naming, validation)
- null test suite and structured test plan
- analysis tooling for correlation-based causality checking
- PoC reporting template and replication checklist

## Typical applications (realistic)
- rapid triage of small-force / exotic-force claims (artifact vs mechanism)
- development bench for real non-contact actuators (EHD-in-air, magnetic gradients, acoustic nodes)
- pulsed-power + EMI/thermal/vibration characterization with synchronized sensing

## Evidence standard (how “proof” is defined here)
A credible effect lead must:
- survive dummy-load matched-heat controls,
- behave predictably under rotation/phase permutations,
- be time-synced (sync_out recorded),
- show repeatability across ≥ 3 runs,
- include raw logs + manifests + null suite outcomes.

## License
Evaluation-only license (no commercial use). See `LICENSE`.

## Contact / commercial licensing
Commercial use, deployment, or redistribution requires a separate written agreement with the Licensor (repo owner).

