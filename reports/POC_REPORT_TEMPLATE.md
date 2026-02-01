# File: reports/POC_REPORT_TEMPLATE.md

# IX-MPMT Proof-of-Concept Report (Template)

> TEMPLATE ONLY — this file is a reporting structure.  
> Do not insert fabricated measurements. Populate only with real run IDs and real plots.

## 1) Summary
- What was tested:
- Why:
- High-level outcome:
  - Mechanism confirmed / artifact rejected / inconclusive

## 2) Build Configuration
- Architecture: H6-C12
- Core capsule version:
- Pod map (position → pod_id → role):
- Sensor nodes used:
- Cable routing reference photo IDs:

## 3) Safety and Interlocks
- Interlock loop verified? (yes/no)
- Dump/bleeder verified? (yes/no)
- Any faults during campaign? (describe)

## 4) Measurement Chain
- Force sensor type:
- Calibration method:
- Calibration constants:
- DAQ timebase:
- Sample rates:

## 5) Experiment Profile (EP)
- Duration:
- Channels enabled:
- Phase map:
- Code IDs + chip duration:
- Environment (open air / enclosure / pressure):

## 6) Runs Executed (Table)
| Run ID | Condition | Notes | Valid/Invalid |
|---|---|---|---|
| | N1 Baseline | | |
| | Known-effect | | |
| | N2 Dummy match | | |
| | N3 Phase perm A/B/C | | |
| | N4 Polarity flip | | |
| | N5 Position swap | | |
| | N6 Rotation 0/90/180/270 | | |
| | N7 Cable probe | | |

## 7) Results (Include Plots)
- Force vs time (raw + processed)
- Overlays:
  - force + temp + accel + mag (and airflow proxy if used)
- CPFS correlation vs lag for each code/channel (if used)

## 8) Null Suite Outcomes
- Which nulls passed:
- Which failed:
- What artifact pathways were ruled out:

## 9) Interpretation
- Most plausible mechanism:
- Remaining uncertainties:
- Next modifications (if needed):

## 10) Appendices
- Raw data file list (with hashes if available)
- Manifests
- Wiring diagrams
- Photos

