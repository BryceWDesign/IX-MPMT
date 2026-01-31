# File: docs/checklists/arming_discharge_checklist.md

# Arming + Discharge Checklist (Print This)

## A) Before ARMED
- [ ] Master disconnect OFF while inspecting
- [ ] Visual: no exposed conductors, no loose fasteners, no damaged insulation
- [ ] Cable routing: strain-relieved, symmetric, no contact with moving/force-sensitive parts
- [ ] Dump load connected (physically verified)
- [ ] Bleeders connected (physically verified)
- [ ] Meter check: all defined “touch points” at safe voltage
- [ ] Sensors connected and reading plausible values (no saturation)
- [ ] Interlock loop closed and verified (toggle test: opening interlock prevents arm)

## B) Transition to ARMED
- [ ] Clear hot zone (no hands/tools inside rig volume)
- [ ] Keyed enable ON (or guarded ARM switch)
- [ ] ARMED indicator ON
- [ ] Start logging BEFORE enabling excitation

## C) During RUN
- [ ] Monitor: current, voltage, temperature, vibration
- [ ] If anything abnormal occurs: STOP → FAULT → dump/bleed → log

## D) After RUN (Discharge / Safe)
- [ ] Excitation OFF (commanded)
- [ ] Keyed enable OFF
- [ ] Master disconnect OFF
- [ ] Dump engaged
- [ ] Wait required time (if specified), THEN meter verify
- [ ] Meter verify: all defined test points at safe voltage
- [ ] Only then: touch/adjust/swap modules

