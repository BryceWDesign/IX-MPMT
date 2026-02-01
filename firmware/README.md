# Firmware (Timing / Coherence Control)

## Purpose
Firmware in IX-MPMT exists to generate **deterministic control signals**:
- phase maps (0/120/240, 0/180, permutations)
- coded excitation envelopes (Code A/B/C)
- SYNC OUT markers captured by DAQ

This repo intentionally starts firmware as a **spec-driven placeholder**.
Hardware choices (MCU/FPGA/DAQ-clock-led) will determine implementation.

## Minimum Outputs (Interface Contract)
- CH0..CH5: pod gate/drive reference outputs (implementation-specific voltage level)
- CH6: core capsule gate/drive reference output (optional)
- SYNC_OUT: digital marker line captured by DAQ
- ARM_IN: interlock/arming input (hardware enforced where possible)
- FAULT_OUT: fault indicator line (optional)

## Required Behaviors
- deterministic run start/stop with SYNC_OUT markers
- configurable phase map per run
- code ID assignment per channel per run
- metadata emission (at minimum: a run config file stored by the host)

## Safety Note
Firmware must never be the only safety layer.
Hardware interlocks, current limiting, and dump paths are mandatory regardless of firmware.

