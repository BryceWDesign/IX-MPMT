"""
IX-MPMT CPFS Correlation Tool
----------------------------

Compute normalized cross-correlation between measured force and a known excitation code.

This is intentionally minimal and auditable:
- numpy only (plus matplotlib if you choose to plot externally)
- explicit normalization
- explicit lag computation

Expected CSV format (early build):
- first column: time_s
- include columns: force_primary, sync_out (optional for alignment)
- optional context channels for overlay (temp/accel/mag)

For serious datasets, prefer HDF5 + run manifests; this tool can be adapted.
"""

from __future__ import annotations
import csv
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional

import numpy as np

from .prbs import CodeSpec, make_default_codes, bits_to_bipolar


@dataclass(frozen=True)
class CorrelationResult:
    code_id: str
    peak_corr: float
    peak_lag_s: float
    lags_s: np.ndarray
    corr: np.ndarray


def load_csv_columns(path: str) -> Dict[str, np.ndarray]:
    """
    Load a CSV where header row contains column names.
    Returns dict of numpy arrays keyed by column name.

    Minimal requirement: must include 'time_s' and 'force_primary'.
    """
    with open(path, "r", newline="") as f:
        reader = csv.DictReader(f)
        cols: Dict[str, List[float]] = {}
        for row in reader:
            for k, v in row.items():
                if k is None:
                    continue
                cols.setdefault(k, []).append(float(v))
    return {k: np.asarray(v, dtype=float) for k, v in cols.items()}


def build_code_waveform(
    time_s: np.ndarray,
    code_bits: List[int],
    chip_duration_s: float,
    start_time_s: float,
    bipolar: bool = True,
) -> np.ndarray:
    """
    Build a piecewise-constant code waveform aligned to time_s.
    - code repeats as needed to cover the time window.
    """
    if chip_duration_s <= 0:
        raise ValueError("chip_duration_s must be > 0")

    bits = bits_to_bipolar(code_bits) if bipolar else code_bits
    n = len(bits)
    y = np.zeros_like(time_s, dtype=float)

    # Determine chip index for each sample time
    t_rel = time_s - start_time_s
    chip_index = np.floor(t_rel / chip_duration_s).astype(int)

    # Assign values only where t >= start_time
    valid = chip_index >= 0
    idx = chip_index[valid] % n
    y[valid] = np.array([bits[i] for i in idx], dtype=float)
    return y


def normalized_xcorr(x: np.ndarray, y: np.ndarray, fs_hz: float, max_lag_s: float) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute normalized cross-correlation r_xy(lag) for lags in [-max_lag_s, +max_lag_s].

    Normalization: r = corr(x,y) / (std(x)*std(y)*N_eff)

    This produces correlation coefficients approximately in [-1, +1].
    """
    if x.shape != y.shape:
        raise ValueError("x and y must have the same shape")

    n = x.size
    if n < 10:
        raise ValueError("signals too short")

    x0 = x - np.mean(x)
    y0 = y - np.mean(y)
    sx = np.std(x0)
    sy = np.std(y0)
    if sx == 0 or sy == 0:
        raise ValueError("zero-variance signal encountered")

    max_lag = int(round(max_lag_s * fs_hz))
    lags = np.arange(-max_lag, max_lag + 1, dtype=int)

    corr = np.zeros_like(lags, dtype=float)
    for i, lag in enumerate(lags):
        if lag < 0:
            a = x0[:lag]
            b = y0[-lag:]
        elif lag > 0:
            a = x0[lag:]
            b = y0[:-lag]
        else:
            a = x0
            b = y0

        if a.size < 5:
            corr[i] = np.nan
            continue

        corr[i] = float(np.sum(a * b) / (a.size * sx * sy))

    lags_s = lags / fs_hz
    return lags_s, corr


def estimate_fs(time_s: np.ndarray) -> float:
    """
    Estimate sampling frequency from time vector.
    """
    dt = np.diff(time_s)
    dt_med = float(np.median(dt))
    if dt_med <= 0:
        raise ValueError("non-increasing time vector")
    return 1.0 / dt_med


def correlate_force_to_codes(
    time_s: np.ndarray,
    force: np.ndarray,
    codes: List[CodeSpec],
    chip_duration_s: float,
    start_time_s: float,
    max_lag_s: float = 5.0,
) -> List[CorrelationResult]:
    fs = estimate_fs(time_s)
    results: List[CorrelationResult] = []
    for c in codes:
        code_w = build_code_waveform(time_s, c.bits, chip_duration_s, start_time_s, bipolar=True)
        lags_s, corr = normalized_xcorr(force, code_w, fs_hz=fs, max_lag_s=max_lag_s)

        # Ignore NaNs when finding peak
        valid = np.isfinite(corr)
        if not np.any(valid):
            raise ValueError("correlation produced only NaNs")

        idx_peak = int(np.nanargmax(np.abs(corr)))
        peak_corr = float(corr[idx_peak])
        peak_lag_s = float(lags_s[idx_peak])

        results.append(
            CorrelationResult(
                code_id=c.code_id,
                peak_corr=peak_corr,
                peak_lag_s=peak_lag_s,
                lags_s=lags_s,
                corr=corr,
            )
        )
    return results


def main_example() -> None:
    """
    Example usage (edit paths and parameters for your run).

    This function prints correlation peaks for default codes.
    """
    path = "runs/example_run/raw/example.csv"  # update for your dataset
    chip_duration_s = 0.200  # example: 200 ms chips
    start_time_s = 0.0       # if you align start time from sync_out, set it here
    max_lag_s = 10.0         # search +/- 10 seconds

    cols = load_csv_columns(path)
    time_s = cols["time_s"]
    force = cols["force_primary"]

    codes = make_default_codes(n_bits=127)
    results = correlate_force_to_codes(time_s, force, codes, chip_duration_s, start_time_s, max_lag_s=max_lag_s)

    print("CPFS Correlation Summary")
    for r in results:
        print(f"{r.code_id}: peak_corr={r.peak_corr:+.3f} at lag={r.peak_lag_s:+.3f} s")


if __name__ == "__main__":
    main_example()
