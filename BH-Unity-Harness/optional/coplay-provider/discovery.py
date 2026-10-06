"""Optional, diagnostic-only Coplay discovery. No BH provider operations.

Python standard library only. Live route compatibility remains unverified.
The injected transport has request(endpoint, route, payload, timeout) -> bytes.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import http.client
import ipaddress
import json
import math
from pathlib import Path
import re
import subprocess
import sys
import time
from urllib.parse import urlsplit

MAX_BYTES = 262144
MAX_REQUEST = 4096
SOURCE_BASELINE = {
    "repository_commit": "4325d0e6a0eb39ffff219ded4629971d8467ce7a",
    "reference_tree": "b3ec16283d5ce88e7576fbe2eacf2d2eb9bdf1dc",
    "unity_package_tree": "ef358632ad5d0cecd84420eaeb7b0e0294ac4e49",
    "server_tree": "c8577d68137ce5c8bc80c52f1989b36bef4ecef5",
}


class DiscoveryError(ValueError):
    """Stable reason code, with no remote error text or payload interpolation."""


def require(condition, code):
    if not condition:
        raise DiscoveryError(code)


def token(value):
    return type(value) is str and re.fullmatch(r"[A-Za-z0-9_.-]{1,256}", value) is not None


def strict_json(raw, maximum=MAX_BYTES):
    require(type(raw) is bytes and 0 < len(raw) <= maximum, "json_size_or_type")

    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "duplicate_json_key")
            result[key] = value
        return result

    def invalid(_):
        raise DiscoveryError("nonfinite_json")

    def number(value):
        result = float(value)
        require(math.isfinite(result), "nonfinite_json")
        return result

    try:
        result = json.loads(raw.decode("utf-8"), object_pairs_hook=pairs,
                            parse_constant=invalid, parse_float=number)
    except (UnicodeError, ValueError, RecursionError) as exc:
        if isinstance(exc, DiscoveryError):
            raise
        raise DiscoveryError("invalid_json") from exc
    require(type(result) is dict, "json_object_required")
    return result


def endpoint_parts(endpoint):
    require(type(endpoint) is str and len(endpoint) <= 128
            and not any(ord(c) <= 32 for c in endpoint), "invalid_endpoint")
    try:
        parsed = urlsplit(endpoint)
        host, port = parsed.hostname, parsed.port
        address = ipaddress.ip_address(host)
    except (ValueError, TypeError) as exc:
        raise DiscoveryError("invalid_endpoint") from exc
    require(parsed.scheme == "http" and address.is_loopback and port is not None
            and 1 <= port <= 65535 and not parsed.username and not parsed.password
            and parsed.path in ("", "/") and not parsed.query and not parsed.fragment,
            "endpoint_not_explicit_loopback")
    return host, port


def wire_request(endpoint, route, payload, timeout, connection_factory=None):
    """One direct HTTP exchange: no proxy, redirect, retry or remote URL support."""
    host, port = endpoint_parts(endpoint)
    require(type(timeout) in (int, float) and 0 < timeout <= 5, "invalid_timeout")
    if route == "/api/instances":
        require(payload is None, "inventory_payload_forbidden")
        method, body = "GET", None
    else:
        require(route == "/api/command" and type(payload) is dict
                and set(payload) == {"type", "params", "unity_instance"}
                and payload["type"] in ("get_project_info", "get_editor_state")
                and payload["params"] == {} and token(payload["unity_instance"]),
                "command_not_allowed")
        method, body = "POST", json.dumps(payload, allow_nan=False).encode("utf-8")
        require(len(body) <= MAX_REQUEST, "request_too_large")
    factory = connection_factory or http.client.HTTPConnection
    connection = factory(host, port, timeout=timeout)
    try:
        connection.request(method, route, body=body,
                           headers={"Accept": "application/json", "Content-Type": "application/json"})
        response = connection.getresponse()
        require(response.status == 200, "http_status_rejected")
        require(response.getheader("Content-Type", "").split(";")[0].strip().lower()
                == "application/json", "http_content_type")
        require(response.getheader("Content-Encoding", "identity").lower() == "identity",
                "http_content_encoding")
        raw = response.read(MAX_BYTES + 1)
        require(0 < len(raw) <= MAX_BYTES, "http_body_size")
        return raw
    finally:
        connection.close()


class LoopbackTransport:
    def request(self, endpoint, route, payload, timeout):
        # A socket idle timeout does not bound slow-drip headers/bodies. The
        # isolated child gives each entire exchange a wall-clock limit and is
        # killed/reaped by subprocess.run on timeout. No background waiter.
        request = json.dumps({"endpoint": endpoint, "route": route, "payload": payload,
                              "timeout": timeout}, allow_nan=False).encode("utf-8")
        require(len(request) <= MAX_REQUEST, "request_too_large")
        try:
            result = subprocess.run([sys.executable, "-I", "-S", str(Path(__file__).resolve()),
                                     "--wire-worker"], input=request, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, timeout=timeout, check=False)
        except subprocess.TimeoutExpired as exc:
            raise DiscoveryError("transport_deadline") from exc
        require(result.returncode == 0, "transport_failure")
        require(len(result.stdout) <= MAX_BYTES, "http_body_size")
        return result.stdout


def canonical_directory(value):
    require(type(value) is str and value and "\x00" not in value, "invalid_project_path")
    path = Path(value)
    require(path.is_absolute(), "absolute_project_path_required")
    try:
        require(not any(p.is_symlink() for p in (path, *path.parents)), "linked_project_path")
        resolved = path.resolve(strict=True)
        require(resolved.is_dir(), "project_directory_required")
    except (OSError, RuntimeError) as exc:
        raise DiscoveryError("project_path_unavailable") from exc
    return str(resolved)


def validate_config(config):
    require(type(config) is dict and set(config) == {
        "endpoint", "project_root", "instance_hash", "session_id", "unity_version"}, "config_fields")
    endpoint_parts(config["endpoint"])
    require(token(config["instance_hash"]) and token(config["session_id"]), "explicit_target_required")
    require(type(config["unity_version"]) is str and 0 < len(config["unity_version"]) <= 80,
            "unity_version_required")
    root = canonical_directory(config["project_root"])
    assets = canonical_directory(str(Path(root) / "Assets"))
    return root, assets


def select_instance(response, config):
    require(response.get("success") is True and type(response.get("instances")) is list,
            "inventory_unavailable")
    instances = response["instances"]
    require(0 < len(instances) <= 32, "inventory_count")
    for item in instances:
        require(type(item) is dict and token(item.get("hash")) and token(item.get("session_id"))
                and type(item.get("project")) is str and 0 < len(item["project"]) <= 256
                and type(item.get("unity_version")) is str, "inventory_identity_missing")
    target = config["instance_hash"]
    # Coplay CLI routes match hash OR project name, so inspect both predicates.
    matches = [i for i in instances if i["hash"] == target or i["project"] == target]
    require(len(matches) == 1 and matches[0]["hash"] == target, "ambiguous_or_missing_target")
    item = matches[0]
    require(sum(i["project"] == item["project"] for i in instances) == 1, "duplicate_project_name")
    require(item["session_id"] == config["session_id"], "session_changed")
    require(item["unity_version"] == config["unity_version"], "unity_version_changed")
    return {key: item[key] for key in ("hash", "session_id", "project", "unity_version")}


def response_data(response):
    require(response.get("success") is True and type(response.get("data")) is dict,
            "native_response_failed")
    return response["data"]


def validate_state(state, selected, config, now_ms):
    require(state.get("schema_version") == "unity-mcp/editor_state@2", "unknown_state_schema")
    observed = state.get("observed_at_unix_ms")
    require(type(observed) is int and 0 <= now_ms - observed <= 2000, "stale_or_unknown_state")
    require(type(state.get("sequence")) is int and state["sequence"] >= 0, "state_sequence_missing")
    unity = state.get("unity")
    require(type(unity) is dict and unity.get("instance_id") in (
        selected["hash"], selected["project"] + "@" + selected["hash"]), "state_identity_unavailable")
    require(unity.get("unity_version") == config["unity_version"], "state_version_changed")
    for section, field in (("compilation", "is_compiling"), ("compilation", "is_domain_reload_pending"),
                           ("assets", "is_updating"), ("tests", "is_running")):
        value = state.get(section)
        require(type(value) is dict and type(value.get(field)) is bool, "readiness_unknown")
        require(value[field] is False, "editor_busy")
    assets = state["assets"]
    refresh = assets.get("refresh")
    require(type(refresh) is dict and refresh.get("is_refresh_in_progress") is False, "refresh_unknown_or_busy")
    # The raw vendor route currently supplies false/null defaults here. Those
    # defaults are not observed disk/import reconciliation.
    seen = assets.get("external_changes_last_seen_unix_ms")
    require(type(seen) is int and 0 <= now_ms - seen <= 2000
            and assets.get("external_changes_dirty") is False, "external_changes_unresolved")
    editor = state.get("editor")
    play = editor.get("play_mode") if type(editor) is dict else None
    require(type(play) is dict and all(play.get(k) is False for k in (
        "is_playing", "is_paused", "is_changing")), "play_state_unknown_or_active")


def discover(config, transport=None, monotonic=time.monotonic, wall_ms=None):
    """Return diagnostic evidence only, including failures and exact raw hashes."""
    report = {"format": "BH-COPLAY-DISCOVERY-1", "status": "unavailable",
              "provider_ready": False, "enabled_capabilities": [], "live_schema_digest": None,
              "source_baseline": dict(SOURCE_BASELINE), "records": [],
              "unavailable_facts": ["loaded_package_and_server_identity", "loaded_capability_schema",
                                    "atomic_response_target_session_provenance"],
              "readiness_checks": "NOT_CONFIRMED"}
    start = monotonic()
    wall = wall_ms or (lambda: int(time.time() * 1000))
    transport = transport or LoopbackTransport()

    def call(route, payload=None):
        remaining = 30 - (monotonic() - start)
        require(remaining > 0, "discovery_deadline")
        raw = transport.request(config["endpoint"], route, payload, min(5, remaining))
        require(type(raw) is bytes and 0 < len(raw) <= MAX_BYTES, "json_size_or_type")
        record = {"route": route, "request": payload, "response_sha256": hashlib.sha256(raw).hexdigest(),
                  "response_bytes": len(raw), "response_base64": base64.b64encode(raw).decode("ascii")}
        report["records"].append(record)
        require(monotonic() - start < 30, "discovery_deadline")
        value = strict_json(raw)
        record["response"] = value
        return value

    try:
        root, assets = validate_config(config)
        before = select_instance(call("/api/instances"), config)
        def command(name):
            return response_data(call("/api/command", {"type": name, "params": {},
                                                       "unity_instance": config["instance_hash"]}))
        project = command("get_project_info")
        require(canonical_directory(project.get("projectRoot")) == root
                and canonical_directory(project.get("assetsPath")) == assets, "project_root_mismatch")
        require(project.get("unityVersion") == config["unity_version"]
                and project.get("projectName") == before["project"], "project_identity_mismatch")
        state = command("get_editor_state")
        validate_state(state, before, config, wall())
        after = select_instance(call("/api/instances"), config)
        require(before == after, "inventory_changed")
        validate_state(state, after, config, wall())
        report.update(status="diagnostic_only", readiness_checks="PASS", observed_target=before)
    except (DiscoveryError, OSError, ValueError, TypeError) as exc:
        report["reason"] = str(exc) if isinstance(exc, DiscoveryError) else "discovery_io_or_shape_error"
    report["elapsed_seconds"] = round(max(0, monotonic() - start), 6)
    return report


def main():
    if sys.argv[1:] == ["--wire-worker"]:
        try:
            request = strict_json(sys.stdin.buffer.read(MAX_REQUEST + 1), MAX_REQUEST)
            require(set(request) == {"endpoint", "route", "payload", "timeout"}, "worker_fields")
            sys.stdout.buffer.write(wire_request(**request))
            return 0
        except Exception:
            return 2
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, type=Path)
    args = parser.parse_args()
    try:
        with args.config.open("rb") as stream:
            config = strict_json(stream.read(MAX_REQUEST + 1), MAX_REQUEST)
        report = discover(config)
    except (OSError, DiscoveryError) as exc:
        report = {"format": "BH-COPLAY-DISCOVERY-1", "status": "unavailable", "provider_ready": False,
                  "enabled_capabilities": [], "live_schema_digest": None,
                  "reason": str(exc) if isinstance(exc, DiscoveryError) else "config_unavailable"}
    print(json.dumps(report, allow_nan=False, ensure_ascii=True))
    return 0 if report["status"] == "diagnostic_only" else 2


if __name__ == "__main__":
    raise SystemExit(main())
