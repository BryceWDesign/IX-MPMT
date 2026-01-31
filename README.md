# IX-MPMT — IX Multi-Physics Micro-Force Testbed

IX-MPMT is a modular, symmetry-driven **micro-force measurement and field-excitation testbed** designed to produce **audit-grade, repeatable evidence** when evaluating small force claims and non-contact actuation concepts (E-field/HV, magnetic gradients, acoustic fields, pulsed EM), while aggressively controlling common false-positive pathways (thermal drift, airflow/ionic wind, vibration rectification, EMI coupling, cable forces).

This repository is **evaluation-focused**: it provides the architecture, build guidance, BOM structure, null-test methodology, and analysis workflow required to distinguish real effects from artifacts. It does **not** claim “antigravity.” It is a falsification-first instrument platform.

## What IX-MPMT Does
- Builds a repeatable **micro-force measurement** fixture (bench testbed, not flight hardware).
- Provides a modular **core capsule** + swappable **pod modules** for controlled excitations or dummy loads.
- Enforces **symmetry + null testing** to surface artifacts quickly.
- Enables **phase-locked / coded excitation** so causality can be verified via correlation/lock-in analysis.
- Produces **traceable datasets** (time-synced channels, raw logs, plots, and test reports).

## Why It Matters
Micro-force experiments are extremely easy to fool. A professional-grade testbed is valuable because it:
- reduces wasted time on non-reproducible results,
- makes small effects reviewable by others,
- creates a credible pass/fail workflow for R&D claims.

## Repository Structure
- `docs/` — design docs, safety, test plans, null suite, analysis method.
- `hardware/` — mechanical layout, module specifications, and BOMs.
- `firmware/` — timing/phase/coherence control stubs and interfaces (when applicable).
- `software/` — acquisition + analysis (correlation/lock-in, plotting, reporting).
- `tests/` — structured test procedures and acceptance criteria.

## Principles (Non-Negotiables)
1. **Falsification-first:** null tests are mandatory, not optional.
2. **Symmetry matters:** geometry is used to cancel bias forces and reveal artifacts.
3. **Causality must be demonstrated:** effects must correlate with known excitation codes.
4. **Safety by design:** HV/pulsed power must include current limiting and dump paths.
5. **Audit-grade evidence:** raw logs + calibration notes + repeat run comparisons.

## Status
This repo is being built commit-by-commit into a complete proof-of-concept package:
BOM → assembly → instrumentation → null suite → reproducible dataset.

## License
See `LICENSE` for evaluation-only terms (no commercial use without a separate written agreement).

