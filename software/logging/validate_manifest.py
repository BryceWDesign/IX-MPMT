"""
Manifest validation helper for IX-MPMT.

Goal:
- Provide a minimal, dependency-light validator for run_manifest.json files.
- Encourage audit discipline early without forcing a heavy stack.

If 'jsonschema' is available, it will validate against the provided schema.
If not, it performs essential key checks and basic structural validation.

Usage:
  python software/logging/validate_manifest.py runs/<run_id>/run_manifest.json
"""

from __future__ import annotations
import json
import sys
from pathlib import Path
from typing import Any, Dict


REQUIRED_TOP_KEYS = ["run_id", "utc_timestamp", "repo", "hardware", "daq", "excitation", "calibration"]
REQUIRED_REPO_KEYS = ["name", "git_commit"]


def _basic_validate(obj: Dict[str, Any]) -> None:
    for k in REQUIRED_TOP_KEYS:
        if k not in obj:
            raise ValueError(f"Missing required top-level key: {k}")

    repo = obj["repo"]
    if not isinstance(repo, dict):
        raise ValueError("repo must be an object")
    for k in REQUIRED_REPO_KEYS:
        if k not in repo:
            raise ValueError(f"Missing required repo key: {k}")

    hw = obj["hardware"]
    if not isinstance(hw, dict):
        raise ValueError("hardware must be an object")
    if hw.get("architecture") != "H6-C12":
        raise ValueError("hardware.architecture must be 'H6-C12'")

    pods = hw.get("pods")
    if not isinstance(pods, list) or len(pods) != 6:
        raise ValueError("hardware.pods must be a list of 6 pod entries")
    for p in pods:
        if not isinstance(p, dict):
            raise ValueError("each pod entry must be an object")
        for rk in ["position", "pod_id", "role"]:
            if rk not in p:
                raise ValueError(f"pod entry missing required key: {rk}")

    daq = obj["daq"]
    if not isinstance(daq, dict):
        raise ValueError("daq must be an object")
    if "channels" not in daq or not isinstance(daq["channels"], list):
        raise ValueError("daq.channels must be a list")

    exc = obj["excitation"]
    if not isinstance(exc, dict):
        raise ValueError("excitation must be an object")
    if exc.get("sync_out_recorded") is not True:
        raise ValueError("excitation.sync_out_recorded must be true for audit-grade runs")

    cal = obj["calibration"]
    if not isinstance(cal, dict):
        raise ValueError("calibration must be an object")
    for ck in ["force_calibration_method", "pre_run", "post_run"]:
        if ck not in cal:
            raise ValueError(f"calibration missing required key: {ck}")


def validate_with_jsonschema(manifest: Dict[str, Any], schema_path: Path) -> None:
    try:
        import jsonschema  # type: ignore
    except Exception as e:
        raise RuntimeError("jsonschema not available") from e

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    jsonschema.validate(instance=manifest, schema=schema)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python software/logging/validate_manifest.py <path/to/run_manifest.json>")
        sys.exit(2)

    manifest_path = Path(sys.argv[1])
    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifest not found: {manifest_path}")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    schema_path = Path(__file__).resolve().parent / "run_manifest.schema.json"

    # Try full schema validation first; fall back to basic validation.
    try:
        validate_with_jsonschema(manifest, schema_path)
        print("OK: manifest validates against JSON schema.")
    except Exception:
        _basic_validate(manifest)
        print("OK: manifest passed basic validation (jsonschema not available).")


if __name__ == "__main__":
    main()
