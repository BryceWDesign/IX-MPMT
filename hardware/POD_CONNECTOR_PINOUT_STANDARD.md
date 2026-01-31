# File: hardware/POD_CONNECTOR_PINOUT_STANDARD.md

# Pod Connector / Pinout Standard (Concept-Level)

## Purpose
Define a consistent pod wiring/pinout strategy to:
- keep wiring forces symmetric,
- reduce EMI coupling,
- support time-synced acquisition,
- make swaps repeatable.

This file is intentionally **connector-agnostic** (you can choose specific part numbers later),
but the signal grouping and discipline are mandatory.

---

## 1) Connector Classes (Recommended Minimum)
### S-Conn (Sense/Data)
Signals that must be low-noise and time-synced.

Recommended groups:
- S1: Sensor supply (if needed)
- S2: Sensor ground (paired, not shared with power ground unless specified)
- S3: I2C/SPI/UART (choose one per pod to avoid confusion)
- S4: Timing reference / trigger (optional but recommended)
- S5: Shield/drain (terminate per grounding strategy)

### P-Conn (Power, non-HV)
Recommended groups:
- P+: Pod driver supply +
- P-: Pod driver supply return
- P_sense+: Optional remote sense +
- P_sense-: Optional remote sense -

### HV-Conn (Only if HV used)
- HV+ and HV- only (keep it simple)
- Provide a documented discharge/bleed path external to the pod before disconnecting

---

## 2) Grounding Rule (Avoid “mystery return paths”)
- Sense ground is not automatically power ground.
- If you bond them, you must do it at a defined single point (documented).
- Avoid large loop areas: route signal and return as a pair.

---

## 3) Strain Relief + Routing
- Every connector must have strain relief.
- Cable exit direction is fixed per pod standard.
- Cable length and routing should be as matched across pods as practical.

---

## 4) Run Metadata Requirement
Every dataset must include:
- connector class used (S/P/HV)
- which signals were populated
- a photo or diagram of the harness routing

If a reviewer can’t reconstruct your wiring, they will not trust your force data.

