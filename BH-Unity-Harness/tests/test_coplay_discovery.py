"""CP-B1 offline tests. All Unity replies are explicit synthetic fixtures."""
import copy
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

MODULE = Path(__file__).resolve().parents[1] / "optional/coplay-provider/discovery.py"
spec = importlib.util.spec_from_file_location("bh_coplay_discovery", MODULE)
discovery = importlib.util.module_from_spec(spec)
spec.loader.exec_module(discovery)
NOW = 1800000000000


class FakeTransport:
    def __init__(self, replies, clock=None):
        self.replies = copy.deepcopy(replies)
        self.calls = []
        self.clock = clock

    def request(self, endpoint, route, payload, timeout):
        self.calls.append((endpoint, route, payload, timeout))
        if self.clock is not None:
            self.clock[0] += 31
        reply = self.replies.pop(0)
        return reply if isinstance(reply, bytes) else json.dumps(reply).encode()


class FakeResponse:
    def __init__(self, body=b'{}', status=200, headers=None):
        self.body, self.status = body, status
        self.headers = headers or {"Content-Type": "application/json"}
        self.read_sizes = []

    def getheader(self, key, default=None):
        return self.headers.get(key, default)

    def read(self, size):
        self.read_sizes.append(size)
        return self.body[:size]


class FakeConnection:
    def __init__(self, response):
        self.response, self.requests, self.closed = response, [], False

    def request(self, *args, **kwargs):
        self.requests.append((args, kwargs))

    def getresponse(self):
        return self.response

    def close(self):
        self.closed = True


class CoplayDiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        (self.root / "Assets").mkdir()
        self.config = {"endpoint": "http://127.0.0.1:8765", "project_root": str(self.root),
                       "instance_hash": "fixture-full-hash", "session_id": "fixture-session",
                       "unity_version": "fixture-editor-version"}
        self.instance = {"hash": "fixture-full-hash", "session_id": "fixture-session",
                         "project": "SYNTHETIC-PROJECT", "unity_version": "fixture-editor-version"}
        self.inventory = {"success": True, "instances": [self.instance]}
        self.project = {"success": True, "data": {"projectRoot": str(self.root),
            "assetsPath": str(self.root / "Assets"), "projectName": "SYNTHETIC-PROJECT",
            "unityVersion": "fixture-editor-version"}}
        self.state = {"success": True, "data": {"schema_version": "unity-mcp/editor_state@2",
            "observed_at_unix_ms": NOW, "sequence": 1,
            "unity": {"instance_id": "fixture-full-hash", "unity_version": "fixture-editor-version"},
            "compilation": {"is_compiling": False, "is_domain_reload_pending": False},
            "assets": {"is_updating": False, "external_changes_dirty": False,
                       "external_changes_last_seen_unix_ms": NOW,
                       "refresh": {"is_refresh_in_progress": False}},
            "tests": {"is_running": False},
            "editor": {"play_mode": {"is_playing": False, "is_paused": False, "is_changing": False}}}}

    def run_discovery(self, replies=None, config=None):
        transport = FakeTransport(replies if replies is not None else [
            self.inventory, self.project, self.state, self.inventory])
        report = discovery.discover(self.config if config is None else config, transport,
                                    wall_ms=lambda: NOW)
        self.assertFalse(report["provider_ready"])
        self.assertEqual(report["enabled_capabilities"], [])
        self.assertIsNone(report["live_schema_digest"])
        return report, transport

    def test_01_diagnostic_success_never_enables_provider(self):
        report, transport = self.run_discovery()
        self.assertEqual(report["status"], "diagnostic_only")
        self.assertEqual(report["readiness_checks"], "PASS")
        self.assertEqual(len(report["records"]), 4)
        self.assertEqual(len(report["records"][0]["response_sha256"]), 64)
        commands = [c[2] for c in transport.calls if c[2]]
        self.assertEqual([c["type"] for c in commands], ["get_project_info", "get_editor_state"])
        self.assertTrue(all(c["unity_instance"] == self.config["instance_hash"] and c["params"] == {}
                            for c in commands))
        self.assertIn("loaded_capability_schema", report["unavailable_facts"])

    def test_02_configuration_requires_explicit_identity(self):
        for key in self.config:
            config = dict(self.config)
            del config[key]
            report, transport = self.run_discovery(config=config)
            self.assertEqual(report["status"], "unavailable")
            self.assertEqual(transport.calls, [])
        for key in ("instance_hash", "session_id", "unity_version"):
            config = dict(self.config, **{key: ""})
            report, transport = self.run_discovery(config=config)
            self.assertEqual(report["status"], "unavailable")
            self.assertEqual(transport.calls, [])

    def test_03_only_explicit_literal_loopback_endpoints(self):
        for endpoint in ("http://example.com:80", "http://localhost:8765", "http://0.0.0.0:8765",
                         "https://127.0.0.1:8765", "http://127.0.0.1", "http://u:p@127.0.0.1:8765",
                         "http://127.0.0.1:8765/api", "http://127.0.0.1:8765/?x=1",
                         "http://127.0.0.1:8765/#x", "http://127.0.0.1:8765\n"):
            with self.subTest(endpoint=endpoint), self.assertRaises(discovery.DiscoveryError):
                discovery.endpoint_parts(endpoint)
        self.assertEqual(discovery.endpoint_parts("http://[::1]:8765"), ("::1", 8765))

    def test_04_strict_json_rejects_duplicates_nonfinite_and_bad_shape(self):
        for raw in (b'{"x":1,"x":2}', b'{"x":{"a":1,"a":2}}', b'{"x":NaN}',
                    b'{"x":Infinity}', b'{"x":1e400}', b'[]', b'{} {}', b'\xff', b''):
            with self.subTest(raw=raw), self.assertRaises(discovery.DiscoveryError):
                discovery.strict_json(raw)

    def test_05_inventory_rejects_ambiguous_missing_and_colliding_targets(self):
        variants = [[], [dict(self.instance, hash="other")], [self.instance, self.instance],
                    [self.instance, dict(self.instance, hash="other", session_id="other-session")],
                    [self.instance, dict(self.instance, hash="other", project="fixture-full-hash")]]
        for items in variants:
            report, transport = self.run_discovery([{"success": True, "instances": items}])
            self.assertEqual(report["status"], "unavailable")
            self.assertEqual(len(transport.calls), 1)

    def test_06_project_root_assets_name_and_version_must_match(self):
        for key, value in (("projectRoot", str(self.root / "Assets")), ("assetsPath", str(self.root)),
                           ("projectName", "wrong"), ("unityVersion", "wrong")):
            project = copy.deepcopy(self.project)
            project["data"][key] = value
            report, transport = self.run_discovery([self.inventory, project])
            self.assertEqual(report["status"], "unavailable")
            self.assertEqual(len(transport.calls), 2)

    def test_07_changed_session_blocks_without_replay(self):
        changed = {"success": True, "instances": [dict(self.instance, session_id="new-session")]}
        report, transport = self.run_discovery([self.inventory, self.project, self.state, changed])
        self.assertEqual(report["reason"], "session_changed")
        self.assertEqual(len(transport.calls), 4)

    def test_08_missing_or_wrong_native_state_identity_is_unavailable(self):
        for value in (None, "", "wrong-hash"):
            state = copy.deepcopy(self.state)
            state["data"]["unity"]["instance_id"] = value
            report, _ = self.run_discovery([self.inventory, self.project, state])
            self.assertEqual(report["reason"], "state_identity_unavailable")

    def test_09_state_timestamps_must_be_fresh_real_integers(self):
        for value in (NOW - 2001, NOW + 1, None, True, str(NOW)):
            state = copy.deepcopy(self.state)
            state["data"]["observed_at_unix_ms"] = value
            report, _ = self.run_discovery([self.inventory, self.project, state])
            self.assertEqual(report["reason"], "stale_or_unknown_state")

    def test_10_busy_or_missing_readiness_flags_block(self):
        for section, field in (("compilation", "is_compiling"), ("compilation", "is_domain_reload_pending"),
                               ("assets", "is_updating"), ("tests", "is_running")):
            for value in (True, None, 0):
                state = copy.deepcopy(self.state)
                state["data"][section][field] = value
                report, _ = self.run_discovery([self.inventory, self.project, state])
                self.assertEqual(report["status"], "unavailable")

    def test_11_dirty_or_unobserved_disk_state_blocks(self):
        for key, value in (("external_changes_dirty", True), ("external_changes_dirty", None),
                           ("external_changes_last_seen_unix_ms", None),
                           ("external_changes_last_seen_unix_ms", NOW - 2001)):
            state = copy.deepcopy(self.state)
            state["data"]["assets"][key] = value
            report, _ = self.run_discovery([self.inventory, self.project, state])
            self.assertEqual(report["reason"], "external_changes_unresolved")

    def test_12_total_deadline_rejects_late_transport_reply(self):
        clock = [0]
        transport = FakeTransport([self.inventory], clock)
        report = discovery.discover(self.config, transport, monotonic=lambda: clock[0], wall_ms=lambda: NOW)
        self.assertEqual(report["reason"], "discovery_deadline")
        self.assertEqual(len(transport.calls), 1)
        self.assertLessEqual(transport.calls[0][3], 5)

    def test_13_oversized_native_json_is_rejected(self):
        report, transport = self.run_discovery([b' ' * (discovery.MAX_BYTES + 1)])
        self.assertEqual(report["reason"], "json_size_or_type")
        self.assertEqual(len(transport.calls), 1)

    def test_14_redirect_status_and_encoding_are_not_followed(self):
        for response in (FakeResponse(status=302), FakeResponse(status=500),
                         FakeResponse(headers={"Content-Type": "text/html"}),
                         FakeResponse(headers={"Content-Type": "application/json", "Content-Encoding": "gzip"})):
            connection = FakeConnection(response)
            factory = mock.Mock(return_value=connection)
            with self.assertRaises(discovery.DiscoveryError):
                discovery.wire_request(self.config["endpoint"], "/api/instances", None, 1, factory)
            self.assertEqual(factory.call_count, 1)
            self.assertEqual(len(connection.requests), 1)
            self.assertTrue(connection.closed)

    def test_15_wire_size_limit_and_direct_connection_ignore_proxy_environment(self):
        response = FakeResponse(b'x' * (discovery.MAX_BYTES + 1))
        connection = FakeConnection(response)
        factory = mock.Mock(return_value=connection)
        with mock.patch.dict(os.environ, {"http_proxy": "http://remote.invalid:8080"}), self.assertRaises(discovery.DiscoveryError):
            discovery.wire_request(self.config["endpoint"], "/api/instances", None, 1, factory)
        factory.assert_called_once_with("127.0.0.1", 8765, timeout=1)
        self.assertEqual(response.read_sizes, [discovery.MAX_BYTES + 1])
        self.assertTrue(connection.closed)

    def test_16_exchange_uses_isolated_child_and_hard_timeout(self):
        with mock.patch.object(discovery.subprocess, "run", side_effect=subprocess.TimeoutExpired("worker", 0.2)) as run:
            with self.assertRaisesRegex(discovery.DiscoveryError, "transport_deadline"):
                discovery.LoopbackTransport().request(self.config["endpoint"], "/api/instances", None, 0.2)
        args, kwargs = run.call_args
        self.assertEqual(args[0][1:3], ["-I", "-S"])
        self.assertEqual(kwargs["timeout"], 0.2)
        self.assertNotIn("shell", kwargs)

    def test_17_mutating_commands_and_arbitrary_routes_never_dispatch(self):
        factory = mock.Mock()
        for route, payload in (("/api/command", {"type": "refresh_unity", "params": {}, "unity_instance": "x"}),
                               ("/api/command", {"type": "get_editor_state", "params": {"refresh": True}, "unity_instance": "x"}),
                               ("http://remote.invalid", None)):
            with self.assertRaises(discovery.DiscoveryError):
                discovery.wire_request(self.config["endpoint"], route, payload, 1, factory)
        factory.assert_not_called()

    def test_18_native_failure_unknown_schema_and_play_state_block(self):
        report, _ = self.run_discovery([self.inventory, {"success": False, "data": {}}])
        self.assertEqual(report["reason"], "native_response_failed")
        for mode in ("schema", "version", "play", "refresh"):
            state = copy.deepcopy(self.state)
            if mode == "schema": state["data"]["schema_version"] = "unknown"
            if mode == "version": state["data"]["unity"]["unity_version"] = "other"
            if mode == "play": state["data"]["editor"]["play_mode"]["is_playing"] = True
            if mode == "refresh": state["data"]["assets"]["refresh"] = {}
            report, _ = self.run_discovery([self.inventory, self.project, state])
            self.assertEqual(report["status"], "unavailable")

    def test_19_real_worker_rejects_mutation_before_network(self):
        request = {"endpoint": self.config["endpoint"], "route": "/api/command", "timeout": 1,
                   "payload": {"type": "delete_script", "params": {}, "unity_instance": "x"}}
        result = subprocess.run([sys.executable, "-I", "-S", str(MODULE), "--wire-worker"],
                                input=json.dumps(request).encode(), capture_output=True, timeout=5)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, b'')
        self.assertEqual(result.stderr, b'')

    def test_20_cli_reports_unavailable_without_inventing_capabilities(self):
        path = self.root / "invalid-config.json"
        path.write_text('{"endpoint":"http://remote.invalid:80"}')
        result = subprocess.run([sys.executable, "-I", "-S", str(MODULE), "--config", str(path)],
                                capture_output=True, timeout=5)
        report = json.loads(result.stdout)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(report["status"], "unavailable")
        self.assertFalse(report["provider_ready"])
        self.assertEqual(report["enabled_capabilities"], [])
        self.assertIsNone(report["live_schema_digest"])


if __name__ == "__main__":
    unittest.main()
