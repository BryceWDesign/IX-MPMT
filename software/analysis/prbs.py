# File: software/analysis/prbs.py

"""
Deterministic code utilities for IX-MPMT coded excitation.

Goal: produce simple, repeatable binary codes with low cross-correlation.

This module intentionally avoids exotic dependencies.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class CodeSpec:
    code_id: str
    bits: List[int]  # must be 0/1


def _lfsr_bits(seed: int, taps: List[int], length: int) -> List[int]:
    """
    Simple LFSR-based PRBS generator.
    - seed: non-zero integer (state)
    - taps: bit positions to XOR (0 = LSB)
    - length: number of output bits

    Note: This is not meant for cryptography.
    It is meant for deterministic, repeatable lab modulation codes.
    """
    if seed == 0:
        raise ValueError("seed must be non-zero")

    state = seed
    out: List[int] = []
    for _ in range(length):
        lsb = state & 1
        out.append(lsb)
        xor = 0
        for t in taps:
            xor ^= (state >> t) & 1
        state = (state >> 1) | (xor << 31)  # keep a 32-bit style register
        state &= 0xFFFFFFFF
    return out


def make_default_codes(n_bits: int = 127) -> List[CodeSpec]:
    """
    Provide a minimal set of distinct codes (A/B/C) for early IX-MPMT work.
    These are stable across runs and repo versions unless explicitly changed.

    n_bits default 127: long enough to reduce accidental correlation but still practical.
    """
    # Distinct seeds and taps yield different sequences.
    bits_a = _lfsr_bits(seed=0xACE1, taps=[0, 2, 3, 5], length=n_bits)
    bits_b = _lfsr_bits(seed=0x1D2C3B4A, taps=[0, 1, 5, 7], length=n_bits)
    bits_c = _lfsr_bits(seed=0xBEEF1234, taps=[0, 3, 4, 6], length=n_bits)

    return [
        CodeSpec(code_id="CodeA", bits=bits_a),
        CodeSpec(code_id="CodeB", bits=bits_b),
        CodeSpec(code_id="CodeC", bits=bits_c),
    ]


def bits_to_bipolar(bits: List[int]) -> List[int]:
    """
    Convert 0/1 bits to -1/+1 for correlation-friendly coding.
    """
    return [1 if b else -1 for b in bits]
