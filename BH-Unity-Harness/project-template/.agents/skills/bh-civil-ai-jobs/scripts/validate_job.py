#!/usr/bin/env python3
"""Read-only validation of proposed Ronin job JSON; NOT a Unity/CIVIL-AI importer."""
import json
import pathlib
import sys

REQUIRED = ("schema_version", "id", "name", "civil_ai_job", "workplace_type", "targeting", "steps", "economy", "prefab", "tests")
MODES = {"nearest_eligible", "assigned", "zone", "random_eligible", "explicit_order", "route"}

def validate(data):
    errors = []
    for key in REQUIRED:
        if key not in data:
            errors.append(f"Missing: {key}")
    if data.get("schema_version") != "0.1.0":
        errors.append("Unsupported schema_version (expected 0.1.0)")
    for key in ("id", "name", "civil_ai_job", "workplace_type"):
        if not isinstance(data.get(key), str) or not data.get(key, "").strip():
            errors.append(f"{key} must be nonempty string")
    targeting = data.get("targeting", {})
    if not isinstance(targeting, dict) or targeting.get("mode") not in MODES:
        errors.append("targeting.mode invalid")
    steps = data.get("steps")
    if not isinstance(steps, list) or not steps or any(not isinstance(s, str) or not s for s in steps):
        errors.append("steps must be a nonempty list of strings")
    economy = data.get("economy", {})
    if not isinstance(economy, dict):
        errors.append("economy must be object")
    else:
        if not isinstance(economy.get("units_per_trip"), int) or isinstance(economy.get("units_per_trip"), bool) or economy["units_per_trip"] <= 0:
            errors.append("economy.units_per_trip must be positive integer")
        if "confirm_delivery" in (steps or []) and economy.get("exactly_once_delivery") is not True:
            errors.append("deliveries must require exactly_once_delivery")
    prefab = data.get("prefab", {})
    if not isinstance(prefab, dict) or not isinstance(prefab.get("name"), str) or not prefab.get("name"):
        errors.append("prefab.name missing")
    if isinstance(prefab, dict) and prefab.get("resource_node") and prefab.get("persistent_instance_id") != "editor_or_spawn_assigned":
        errors.append("resource node identity must be editor_or_spawn_assigned")
    if not isinstance(data.get("tests"), list) or not data["tests"]:
        errors.append("tests must be a nonempty list")
    return errors

def main():
    if len(sys.argv) != 2:
        print("Usage: validate_job.py <job.json>", file=sys.stderr)
        return 2
    try:
        path = pathlib.Path(sys.argv[1]); data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("Root must be JSON object")
        errors = validate(data)
        print(json.dumps({"file": str(path), "valid": not errors, "errors": errors}, indent=2))
        return 1 if errors else 0
    except (OSError, ValueError, json.JSONDecodeError) as e:
        print(json.dumps({"valid": False, "errors": [str(e)]}, indent=2))
        return 1

if __name__ == "__main__":
    sys.exit(main())
