#if UNITY_EDITOR
// Original BH implementation. Optional source only; not installed or enabled by the harness.
using System;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using UnityEditor;
using UnityEngine;
using MCPForUnity.Editor.Tools;

namespace BH.UnityHarness.Coplay
{
    [InitializeOnLoad]
    [McpForUnityTool("bh_asset_query", AutoRegister = false, RequiresPolling = false,
        Description = "Optional BH bounded AssetDatabase diagnostic; not an acceptance provider.")]
    public static class BHAssetQuery
    {
        private const int MaxBytes = 262144;
        private const string Provider = "unity-asset-database";
        // Unity initializes this class on the Editor thread. Changes at every domain reload.
        private static readonly int EditorThread = Thread.CurrentThread.ManagedThreadId;
        private static readonly string DomainId = Guid.NewGuid().ToString("N");
        private static readonly string[] IdentityKeys =
            { "project_root", "assets_root", "unity_version", "process_id", "editor_domain_id" };
        static BHAssetQuery() { }

        private sealed class Rejected : Exception
        {
            internal readonly string State;
            internal Rejected(string state, string reason) : base(reason) { State = state; }
        }
        private static void Require(bool condition, string reason, string state = "unavailable")
        {
            if (!condition) throw new Rejected(state, reason);
        }
        private static void Fields(JObject value, params string[] names)
        {
            Require(value != null && value.Properties().Select(p => p.Name).OrderBy(n => n, StringComparer.Ordinal)
                .SequenceEqual(names.OrderBy(n => n, StringComparer.Ordinal)), "invalid_fields");
        }
        private static string Text(JToken value, int max)
        {
            Require(value != null && value.Type == JTokenType.String, "expected_string");
            string text = (string)value;
            Require(text.Length > 0 && text.Length <= max && !text.Any(char.IsControl), "invalid_text");
            return text;
        }
        private static string Absolute(string path)
        {
            return Path.GetFullPath(path).Replace('\\', '/').TrimEnd('/');
        }
        private static JObject Observe()
        {
            string assets = Absolute(Application.dataPath);
            return new JObject {
                ["identity"] = new JObject {
                    ["project_root"] = Absolute(Path.GetDirectoryName(assets)),
                    ["assets_root"] = assets, ["unity_version"] = Application.unityVersion,
                    ["process_id"] = System.Diagnostics.Process.GetCurrentProcess().Id,
                    ["editor_domain_id"] = DomainId
                },
                ["observed_at_unix_ms"] = DateTimeOffset.UtcNow.ToUnixTimeMilliseconds(),
                ["is_compiling"] = EditorApplication.isCompiling,
                ["is_updating"] = EditorApplication.isUpdating,
                ["is_playing_or_changing"] = EditorApplication.isPlayingOrWillChangePlaymode,
                ["is_paused"] = EditorApplication.isPaused,
                ["native_coplay_session_id"] = JValue.CreateNull(),
                ["test_run_active"] = JValue.CreateNull(),
                ["domain_reload_pending"] = JValue.CreateNull(),
                ["disk_assetdatabase_coherence"] = "unknown",
                ["loaded_capability_schema_digest"] = JValue.CreateNull()
            };
        }
        private static void Idle(JObject observation)
        {
            foreach (string field in new[] { "is_compiling", "is_updating", "is_playing_or_changing", "is_paused" })
                Require(!(bool)observation[field], "editor_busy", "busy");
        }
        private static void Deadline(System.Diagnostics.Stopwatch clock)
        {
            Require(clock.ElapsedMilliseconds < 30000, "cooperative_deadline_exceeded", "over_budget");
        }
        private static void SafeDiskPath(string absolute)
        {
            // Reject symlinks/junctions in every existing ancestor, including the project root.
            string cursor = absolute;
            while (!string.IsNullOrEmpty(cursor))
            {
                Require((File.GetAttributes(cursor) & FileAttributes.ReparsePoint) == 0, "linked_path");
                cursor = Path.GetDirectoryName(cursor);
            }
        }
        private static void AssetPath(string path, string project)
        {
            Require(path.StartsWith("Assets/", StringComparison.Ordinal) && path.Length <= 1024,
                "invalid_assets_subpath");
            Require(!path.Contains("\\") && !path.Contains(":") && !path.Any(char.IsControl), "invalid_path");
            Require(path.Split('/').All(p => p.Length > 0 && p != "." && p != ".." && p.Trim() == p
                && !p.EndsWith(".", StringComparison.Ordinal)), "ambiguous_path");
            SafeDiskPath(Path.Combine(project, path));
        }
        private static string Folder(string path, string project)
        {
            AssetPath(path, project);
            Require(Directory.Exists(Path.Combine(project, path)) && AssetDatabase.IsValidFolder(path),
                "invalid_scope_no_fallback");
            string guid = AssetDatabase.AssetPathToGUID(path);
            Require(Regex.IsMatch(guid, "^[0-9a-f]{32}$"), "scope_identity_unknown");
            Require(AssetDatabase.GUIDToAssetPath(guid) == path, "scope_path_not_exact");
            return guid;
        }
        private static JObject Envelope(string state, string reason, JObject before, JObject after,
            JObject result, long elapsed)
        {
            return new JObject {
                ["format"] = "BH-COPLAY-ASSET-QUERY-1", ["state"] = state, ["reason"] = reason,
                ["provider_ready"] = false, ["enabled_capabilities"] = new JArray(),
                ["live_schema_digest"] = JValue.CreateNull(),
                ["before"] = before, ["after"] = after, ["result"] = result,
                ["elapsed_ms"] = elapsed, ["coverage_basis"] = "assetdatabase_only",
                ["unavailable_facts"] = new JArray("native_coplay_session_binding", "loaded_dependency_identity",
                    "loaded_capability_schema", "test_run_state", "domain_reload_pending", "disk_assetdatabase_coherence"),
                ["hard_interrupt_supported"] = false
            };
        }

        // Synchronous: no queued continuation, refresh, polling, installation or file writes.
        public static object HandleCommand(JObject request)
        {
            var clock = System.Diagnostics.Stopwatch.StartNew();
            JObject before = null, after = null, result = null;
            string state = "unavailable", reason = "unknown";
            try
            {
                Require(Thread.CurrentThread.ManagedThreadId == EditorThread, "not_editor_thread");
                before = Observe();
                Require(request != null && Encoding.UTF8.GetByteCount(request.ToString(Formatting.None)) <= 8192,
                    "request_too_large", "over_budget");
                string action = Text(request["action"], 16);
                if (action == "describe")
                {
                    Fields(request, "action");
                    after = Observe();
                    state = "diagnostic_only"; reason = "identity_observation_only";
                }
                else
                {
                    Require(action == "search", "unsupported_action");
                    Fields(request, "action", "expected_identity", "spec");
                    var expected = request["expected_identity"] as JObject;
                    Fields(expected, IdentityKeys);
                    Require(JToken.DeepEquals(expected, before["identity"]), "target_or_domain_changed");
                    Idle(before);
                    var spec = request["spec"] as JObject;
                    Fields(spec, "query", "provider", "scope_paths", "properties", "max_items");
                    string query = Text(spec["query"], 128);
                    // Deliberately narrow: one literal type filter, optionally one plain name term.
                    Require(Regex.IsMatch(query, @"\At:[A-Za-z][A-Za-z0-9_.]*( [A-Za-z0-9_-]+)?\z"), "unsupported_query");
                    Require(Text(spec["provider"], 64) == Provider, "unsupported_provider");
                    var scopes = spec["scope_paths"] as JArray;
                    Require(scopes != null && scopes.Count == 1, "one_scope_required");
                    string scope = Text(scopes[0], 1024);
                    var properties = spec["properties"] as JArray;
                    Require(properties != null && properties.Count >= 1 && properties.Count <= 3, "invalid_properties");
                    string[] props = properties.Select(p => Text(p, 16)).ToArray();
                    Require(props.Distinct(StringComparer.Ordinal).Count() == props.Length
                        && props.All(p => p == "name" || p == "fileName" || p == "isFolder"), "unsupported_properties");
                    Require(spec["max_items"].Type == JTokenType.Integer, "invalid_max_items");
                    long requestedMax = (long)spec["max_items"];
                    Require(requestedMax >= 1 && requestedMax <= 25, "invalid_max_items");
                    string project = (string)before["identity"]["project_root"];
                    // Validation and query occur in the same main-thread invocation; never pass null folders.
                    string scopeGuid = Folder(scope, project);
                    Deadline(clock);
                    string[] guids = AssetDatabase.FindAssets(query, new[] { scope });
                    Require(guids != null, "candidate_list_unknown");
                    // Count BEFORE loading any asset record or resolving candidate paths/types.
                    Require(guids.Length <= requestedMax, "too_many_candidates", "over_budget");
                    Require(guids.All(g => g != null && Regex.IsMatch(g, "^[0-9a-f]{32}$"))
                        && guids.Distinct(StringComparer.Ordinal).Count() == guids.Length, "invalid_or_duplicate_guid");
                    Array.Sort(guids, StringComparer.Ordinal);
                    var items = new JArray();
                    foreach (string guid in guids)
                    {
                        Deadline(clock);
                        string path = AssetDatabase.GUIDToAssetPath(guid);
                        Require(path != null && path.StartsWith(scope + "/", StringComparison.Ordinal), "out_of_scope_result");
                        AssetPath(path, project);
                        Require(AssetDatabase.AssetPathToGUID(path) == guid, "asset_identity_changed");
                        Type kind = AssetDatabase.GetMainAssetTypeAtPath(path);
                        Require(kind != null && !string.IsNullOrEmpty(kind.FullName), "asset_type_unknown");
                        var values = new JObject();
                        foreach (string prop in props.OrderBy(p => p, StringComparer.Ordinal))
                        {
                            if (prop == "name")
                            {
                                UnityEngine.Object asset = AssetDatabase.LoadMainAssetAtPath(path);
                                Require(asset != null, "asset_unavailable");
                                values[prop] = Text(new JValue(asset.name), 1024);
                            }
                            else if (prop == "fileName") values[prop] = Path.GetFileName(path);
                            else values[prop] = AssetDatabase.IsValidFolder(path);
                        }
                        items.Add(new JObject { ["id"] = guid, ["kind"] = Text(new JValue(kind.FullName), 1024),
                            ["path"] = path, ["properties"] = values });
                    }
                    Require(Folder(scope, project) == scopeGuid, "scope_changed");
                    foreach (JObject item in items)
                    {
                        string path = (string)item["path"];
                        AssetPath(path, project);
                        Require(AssetDatabase.GUIDToAssetPath((string)item["id"]) == path
                            && AssetDatabase.AssetPathToGUID(path) == (string)item["id"], "asset_identity_changed");
                    }
                    after = Observe();
                    Idle(after);
                    Require(JToken.DeepEquals(before["identity"], after["identity"]), "target_or_domain_changed");
                    Deadline(clock);
                    result = new JObject { ["query"] = query, ["provider"] = Provider,
                        ["scope_paths"] = new JArray(scope), ["complete"] = true,
                        ["total_count"] = guids.Length, ["items"] = items };
                    state = "diagnostic_only"; reason = "bounded_assetdatabase_result_not_acceptance";
                }
            }
            catch (Rejected ex) { state = ex.State; reason = ex.Message; result = null; }
            catch (Exception) { state = "unavailable"; reason = "observation_exception"; result = null; }
            // No exception details or user-controlled error strings can grow the error response.
            var response = Envelope(state, reason, before, after, result, clock.ElapsedMilliseconds);
            if (Encoding.UTF8.GetByteCount(response.ToString(Formatting.None)) > MaxBytes)
                return Envelope("over_budget", "response_too_large", null, null, null, clock.ElapsedMilliseconds);
            if (clock.ElapsedMilliseconds >= 30000)
                return Envelope("over_budget", "cooperative_deadline_exceeded", before, after, null, clock.ElapsedMilliseconds);
            return response;
        }
    }
}
#endif
