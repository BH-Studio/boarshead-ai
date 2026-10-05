# Unity Reference deep review — findings and adoption plan

Status: TARGETED REVIEW COMPLETE; recommendations NOT_IMPLEMENTED by this review.
Requested basis: `Reference/Unity` in `BH-Studio/boarshead-ai`.
Pinned source and candidate baseline: `1b62ae6e8e34e996c7f1c5e29dc7e5ae30db2485`.
Initial durable review checkpoint: `bfe9e1f83e58996dcd642d89f3670c1debbf6ff0`.
Coverage register: `UNITY_REFERENCE_INVENTORY.json`.

## Verdict

There is useful Unity engineering guidance here, but neither catalog should be imported wholesale. The highest-value additions are bounded Editor inspection, explicit asynchronous job/completion handling, stronger persisted-asset verification, and an optional Project Auditor integration. UI, localization, navigation, audio, text and rendering recipes belong behind project-specific applicability checks, not in the always-loaded core.

Several sources conflict with each other or with the BH evidence/approval model. Some contain technically questionable or demonstrably incorrect prescriptions. First-party provenance is useful provenance, not proof that every instruction is correct or compatible. Extract tested mechanisms; do not inherit vendor workflow authority.

## 1. Basis, exact coverage and limits

The immediate family inventories contain 34 skill folders in `skills-main/skills` and 33 in `unity-agent-plugin-main/skills`. Twenty-four common subtrees have identical Git identities; nine differ. `project-auditor-fixes` exists only in the skills snapshot. The plugin manifest describes version `0.1.8-beta`, requires a local executor, and points its skills entry at the entire `./skills/` directory.

This review fully read thirteen distinct skills-main SKILL bodies: `asset-transformer-toolkit`, `generate-editor-search-query`, `initialize-ai-navigation`, `localization`, `optimize-audio`, `optimize-text-mesh-pro`, `project-auditor-fixes`, `shader-graph-create-custom-node`, `ui`, `ui-ugui`, `ui-uitk`, `unity-package-management`, and `validate-urp-render-graph-renderer-feature`. It read portions of `unity-cli` and `physics-3d-collision`; their larger responses were truncated. Localization's initially truncated read was completed with an overlapping range through the end. Nineteen other families received directory/identity inventory only and are NOT approved by a content review.

Eleven additional complete path reads are recorded in the inventory: both licenses, the Codex plugin manifest, CLI security and play-mode guidance, Search query and opener references, the plugin Search body/opener, the uGUI ScrollView reference, and the frontmatter validator. Full SKILL-body coverage does not mean all linked recipes/security files or every differing catalog variant was read. No exhaustive audit of the vendor packages, binaries, dependencies or all nested files is claimed.

The preceding EXTERNAL_UNITY_REVIEW was checked to avoid duplicating its few-file coverage claim. The current compact `contracts/CODEX_CONSUMER.md` was read to map recommendations onto the actual efficiency revision. Earlier implementation/evidence records remain authoritative for their pinned revisions. This is not a fresh line-by-line runtime audit or a test execution.

Stored roots are `f4cf5bc9f7f41598f82237bd890159745727b481` and `e4f8d1f03a9da07c4112147bfd1c607a5534deed`. Source paths and hashes are in the inventory. These are stored snapshots, not claims that the folders match current upstream HEADs. Outside documentation checks below are separately labeled; they do not replace the requested local sources.

## 2. Prioritized incorporation matrix

Every row below is a recommendation. Suggested destinations are future candidate changes, not files or adapters newly installed by this review.

| ID | Priority / disposition | Stored source | Useful mechanism | Proposed BH destination |
|---|---|---|---|---|
| UR-01 | High / adapt | generate-editor-search-query and two references | Asset-versus-scene semantic queries, type/path/reference narrowing, explicit query scope | Existing preflight/debug skills plus a small on-demand Editor-inspection reference and bounded result adapter |
| UR-02 | High / adapt | unity-cli playmode-verification-loop; project-auditor-fixes | Explicit project targeting, terminal job results, readiness and frame/state observation, file-backed captures | Existing preflight/verify procedures; optional configured live-Editor adapter; future prerequisite work |
| UR-03 | High / optional integration | project-auditor-fixes | Unity-specific diagnostics, grouped findings, before/after evidence | Optional `bh-unity-project-audit` procedure and deterministic report adapter, outside default discovery until tested |
| UR-04 | High / adapt | localization; ui, ui-ugui, ui-uitk | Persisted sub-asset/binding readback, declared UI-family routing, visible and interactive verification | Existing implement/verify skills with selected UI/asset-authoring references |
| UR-05 | Medium / adapt | unity-package-management; asset-transformer-toolkit; localization; shader-graph-create-custom-node | Resolved version and capability gates, batched approved package changes, no premature async completion | Existing preflight and project configuration; no universal package installer or automatic upgrade |
| UR-06 | Medium / optional references | optimize-audio, optimize-text-mesh-pro, initialize-ai-navigation, Render Graph validator | Symptom-specific diagnosis and narrowly applicable implementation checks | Project-selected reference leaves; optional renderer review only for an applicable project |
| UR-07 | Medium / authoring quality gate | frontmatter validator, plugin metadata, licenses/security, differing snapshots | Syntax/name validation, complete referenced-file selection, explicit applicability/provenance | Harness-authoring validation and capability register, not extra model work on every task |

### UR-01 — Bounded Editor inspection instead of broad repository exploration

Source support: the Search skill and `references/query-patterns.md` distinguish assets from scene objects and use simple type, directory, label and reference queries. They explicitly warn that broad keyword matches and missing-script searches are not exhaustive dependency audits. The opener encodes query text rather than interpolating raw user text into C# and shell strings.

Recommended adaptation: start from an actual asset path/object identity and the smallest useful query; return counts, stable references, requested properties and explicit scope. Return only a bounded page of results, with continuation when necessary. A missing provider, incomplete index, unloaded scene or unreachable Editor must not become an authoritative empty result. Use disk/code search for code questions and Editor-aware inspection for serialized objects.

The source opener opens a UI window; it does not implement a machine-readable enumerator. A bounded result adapter is proposed new work, not a discovered ready-made capability. Opening Search may help a human but should not be the automatic default for headless Codex. Reuse the active, explicitly targeted Editor route. Do not install the Pipeline package, create an ad hoc script, change selection, or mutate search results merely to answer an inspection question.

Cost rationale: fewer broad source scans and speculative edits; one selected property batch rather than one model tool round trip per property. Measure actual payload/call counts in the pilot. Do not claim savings from the source's prose alone.

### UR-02 — Treat long-running Editor work as a bounded job, not a chat polling loop

Source support: the play-mode reference distinguishes CLI timeouts from Editor command timeouts, CLI detached jobs from Pipeline asynchronous waits, and readiness from completed gameplay observations. It documents a synchronous wait occupying the execution queue, which matters when the condition requires another command. Project Auditor has `completed`, `failed`, `unavailable`, `interrupted`, and `busy` states; the source says that audit has no cancellation operation.

Recommended adaptation: discover the connected package's command schema once for the selected project/connection/version, then retrieve only the required command details. Persist the actual job identifier, owning project/session, terminal status, deadline and evidence paths. Let a local bounded operation wait or poll; do not spend model turns repeatedly asking the same status. Revalidate capability information after package changes, reconnection or domain reload where necessary. Never mistake no visible instance for permission to launch a second Editor.

Stopping polling is not cancelling a server job. On interruption/timeout, retain incomplete evidence and check ownership before launching again. No automatic repeated scan/restart loop. A package lacking the required terminal status or cancellation behavior needs an explicit supported fallback, not invented commands.

For smoke evidence, observe frames or the relevant domain state advancing, then check the approved condition and capture the correct view. Frame advancement alone does not prove the mechanic. Prefer a saved image plus bounded error summary to inline base64 or full console dumps. The source distinguishes screen captures, which include overlay UI, from camera-only captures. Discover the actual parameters; do not hard-code its changing defaults.

Record initial Play state, ticking/background settings and any temporary changes; restore only state changed by the harness under its approved scope. `set_autotick`, Play/Stop, import, and `eval` tuning are not read-only. The source's live-tuning step belongs to an approved experiment/execution phase, never inside an evidence-only audit. Persistent code/asset changes need reimport/reload and fresh checks.

BH already has one-writer, evidence freshness, selective checks and fail-fast. This recommendation adds Unity-specific completion/state semantics; it does not claim those live bindings already exist or that sequential fail-fast is a dependency scheduler. The earlier machine-prerequisite implementation item remains open.

### UR-03 — Optional Project Auditor as a complement to existing diagnostics

Source support: `project-auditor-fixes` describes CSV columns `Category, Severity, Areas, Description, RelativePath, Line, DescriptorId, Recommendation`, categories including code/project settings, grouped fixes, one scan at a time, and explicit unavailability when the package or rules are missing. It asks for the same test scenario before and after fixes.

Recommended adaptation: retain the existing SonarQube bridge and introduce a separately named Unity diagnostics source only when the project actually provides it. Parse real completed output, preserve category and descriptor identity, compare against an approved baseline, and return grouped deltas and high-value examples instead of every row. Preserve the raw CSV by hash/reference. Non-file project-setting findings must have a documented mapping; do not fabricate source paths simply to fit the current file-diagnostics schema.

Separate `audit/triage` from `repair`: findings do not authorize fixing every row. Select a bounded approved batch by issue type/affected files and verify unchanged baseline failures remain visible. An empty completed result is usable only after proving the intended rules and coverage ran; unavailable/interrupted output is not a clean scan. The source recommends automatic reruns, package installation, starting from clean commits, and treating all rows as fixes. Those policies are not adopted.

Implement the deterministic CSV/status adapter and synthetic negative tests first; then test the existing Editor integration on the actual Windows project. An optional skill may be useful if this becomes recurring, but it must not become a sixth always-enabled core skill merely to expose a vendor catalog.

### UR-04 — Verify serialized artifacts and approved behavior, not just in-memory objects

Source support: localization distinguishes requested package entries from resolved lockfile entries and from assemblies actually loaded. Its font recipe checks persisted material sub-assets instead of trusting an in-memory property. Its listener recipe separately checks target, method, call state and actual text change. Its completeness check distinguishes zero examined entries from success and enumerates gaps rather than silently filling them. Its extraction guidance distinguishes authored scene/prefab text from strings composed in code, acknowledging that one scan cannot cover both.

The UI router differentiates `.uxml/.uss` and `UIDocument`, Canvas/RectTransform, and IMGUI patterns. uGUI guidance favors inspecting and repairing existing hierarchy properties rather than destroying/rebuilding. UI Toolkit recommends completing a coherent file batch before import rather than repeated half-written imports.

Recommended adaptation: include an asset-authoring completion checklist for relevant work: intended object and owner, serialized references, saved sub-assets, applicable reload/reopen proof, actual callback behavior, idempotent rerun, and protection of hand-authored data. Check only affected assets/scenes and the approved shared dependencies. Reloading or switching scenes can mutate Editor state; it requires ownership and restoration rather than being described as a pure read.

For UI, select the framework used by the affected component, not whichever framework appears somewhere in a mixed repository. Load only that reference. Approved functional UI criteria require real input/binding behavior, not only rendered layout. Preserve controller/keyboard/accessibility requirements when they are in the task. For localization, use the approved locale/key roster and report missing/empty entries, runtime-composed text and glyph/layout gaps without inventing translations or copying fonts without rights.

Do not import the source's unconditional destroy-old-Canvas instruction, blanket fallback-font prohibition, hard-coded language/font choices, or project-wide all-scene modification recipe. Its stated sample measurements are source claims, not measurements performed here. Do not treat the ScrollView example's Mask/Image and ContentSizeFitter recipe as the only valid implementation; alternate masking, explicit sizing, pooling or virtualization may be intentional.

### UR-05 — One applicability gate for package, version, entitlement and command shape

Source support: Asset Transformer Toolkit explicitly checks resolved version, stops when entitlement/package is absent and does not automatically reimport when importer settings change. The Shader Graph custom-node body declares `com.unity.shadergraph >=17.5.0`. Package-management guidance explains asynchronous `Client.AddAndRemove` and one resolution pass; localization notes that resolved files and loaded types are different readiness claims.

Recommended adaptation: record engine, resolved package versions, selected integration route and exact needed API/tool capabilities. Missing or mismatched capabilities block only the dependent work. No automatic latest upgrade, replacement navigation backend, render-pipeline conversion or package purchase. A metadata field such as `required_packages` is a useful source declaration, not proof the host enforces it.

For an explicitly approved dependency change, deduplicate the requested changes, use the supported current route, wait for real resolution/compilation completion and inspect requested/resolved changes. Batch compatible approved changes rather than launch one Editor/resolution per package. Never use a version copied from an unrelated neighboring package. Keep package writes separate from read-only discovery and ordinary game edits.

No generic headless installer is copied from this source. A direct Editor batch operation without `-quit` may be appropriate for an async bootstrap, but it must not be launched against an already-owned open project. Existing verified package APIs and a current command catalog take precedence over conflicting snapshot recipes.

### UR-06 — Small feature-specific references, not more global policy

| Source | Retain after applicable verification | Reject as an unconditional rule |
|---|---|---|
| optimize-audio | Symptom triage; importer/mixer readback; device versus Editor evidence; comparable before/after workload | Universal bus-count/depth/clip-duration thresholds, automatic force-to-mono, all-source dumps and repeated approval pauses inside one approved plan |
| optimize-text-mesh-pro | Atlas/fallback/material ownership, dirty-canvas/AutoSize diagnosis, glyph coverage, device captures | Always changing text implementation, universal atlas/sample sizes, speculative Dynamic OS adoption or importing examples as a default fix |
| initialize-ai-navigation | Existing movement owner, agent/surface type match, valid path, masks, links, carving and representative behavior | Installing NavMesh for any pathfinding request, copying adjacent package versions or introducing a second movement authority |
| localization | Approved key/locale coverage, saved bindings, runtime versus authoring behavior, explicit unconverted sites | Silently replacing the project's font strategy, deleting/recreating UI or localizing an unapproved whole project |
| validate-urp-render-graph-renderer-feature | Confirmed versus likely findings; pass/resource/material wiring; fresh pooled PassData; required inputs; unnecessary global exposure/copies | Applying URP guidance to HDRP/Built-in, automatic pipeline upgrades, or treating sample snippets as compiled proof |
| shader-graph-create-custom-node | Explicit package/API gate and reuse of a suitable existing HLSL asset | Upgrading Shader Graph to make a sample fit or assuming reflection-node support on every Unity 6 project |
| asset-transformer-toolkit | Check installed version/entitlement; changing settings need not immediately trigger expensive reimport | Requiring an entitled industry package in a general game harness |

A URP Render Graph review is a particularly useful optional code-review leaf because its output separates confirmed errors from missing context. However, its descriptor example needs correction for the verified SRP Core 17.0 API; see the outside check below. No C# or HLSL examples from these files were compiled here.

### UR-07 — Validate skills as authored artifacts

The stored Node validator uses `js-yaml` and checks a YAML mapping, a nonempty name matching its directory, and a nonempty description. This is useful authoring QA, but not a guarantee of security, correct Unity APIs, native activation or complete references. Retain the principle, not necessarily its runtime dependencies.

BH should validate supported metadata, activation exclusions, unique names, required reference paths, version/provenance selection and scenario behavior when adding a skill. Use a standards-compliant YAML check in authoring validation where available, or clearly restrict the supported generated frontmatter grammar; a regex-only name check must not be described as full YAML validation. There is no need to install Node/js-yaml into every game or reparse the entire vendor catalog in each Codex task.

## 3. Concrete source conflicts and unsafe prescriptions

### F-01 — Physics diagnosis is overconfident and anti-verification (high)
The visible `physics-3d-collision` body requires no verification for some diagnoses, forbids consulting documentation, sets a five-tool-call hard stop followed by a likely diagnosis, and mandates particular fixes while ignoring competing details. Those are instructions under review, not authority for BH. A budget should end with an explicit unresolved diagnosis when evidence is insufficient, not convert a hypothesis into certainty.

Two targeted official-documentation checks contradict blanket advice in those visible sections: Raycast defaults to `QueryTriggerInteraction.UseGlobal`, not invariably ignoring triggers, and AddForce normally wakes the body when a nonzero force is applied. Preserve API-family/layer/body/callback checklists only after rewriting them as evidence-led diagnosis. Do not install this skill unchanged. The rest of its body is not represented as fully read or comprehensively fact-checked.

### F-02 — Package recipes disagree (high)
`unity-package-management` says the CLI has no package-management command and prohibits direct manifest edits. `initialize-ai-navigation` instructs a direct manifest addition and permits copying an adjacent package version. `project-auditor-fixes` uses `unity command package_add`. The latter is an Editor-exposed command, which is distinct from a CLI root command; that distinction must replace the ambiguous blanket limitation. Determine actual capabilities, approved versions and ownership instead of following whichever skill loaded last.

### F-03 — UI completion and mutation policies conflict (high)
The UI skills explicitly interpret working UI/menu requests as rendered layout without behavior. That is incompatible with any approved interaction/binding criterion. UI Toolkit's manual ask-user-to-focus/read-console loop also should not be mandatory when a verified Editor route can return the actual import results. Conversely, do not claim offline parsing proves Unity rendering.

uGUI says never destroy a hierarchy to fix it; localization tells the agent to destroy an old named Canvas before creation. TMP optimization favors dynamic CJK fallbacks while localization categorically rejects them. These are conflicting source prescriptions, not decisions the shared harness should silently make. The project owns the design; use conditional recipes and measured evidence.

### F-04 — Useful render checklist contains a questionable snippet (medium)
The Render Graph skill assigns `GetDescriptor(renderGraph)` to `RenderTextureDescriptor` and then sets `name`. The verified SRP Core 17.0.4 documentation declares `TextureHandle.GetDescriptor` as returning `TextureDesc`. Treat this as an API/type mismatch requiring correction and actual target-version compilation, not as validated source code. This does not invalidate the checklist's separate resource-lifetime and binding questions.

### F-05 — Full CLI and plugin bring too much unrelated behavior (medium)
The stored CLI skill body is 50,411 bytes and covers installs, updates, identity/cloud, licensing, multiple clients and other operations. This byte count is not a token charge and does not mean all references are always loaded. It does make the complete body a poor default for a narrow Editor check. The plugin points at the whole catalog, rather than being only a small Editor adapter.

Do not import automatic latest-version instructions, pipe-to-shell installation, vendor-accepted trust decisions, global client setup, cloud/monetization workflows, or a competing commit policy. Neither `enabled`, `modes`, `allowed-tools` nor declared packages should be assumed to map to the actual Codex host's enforcement. Keep native host capability testing separate.

### F-06 — Duplicate names do not imply equivalent packages (medium)
The two Search SKILL bodies are byte-identical, as is their query-pattern reference, but the opener differs: the plugin adds `--caller plugin --skill generate-editor-search-query`. This is a concrete support-file difference, not merely different README metadata. It does not prove every other differing subtree has the same kind of change. Preserve the exact selected tree and required referenced files; never mix folders based on name or assume either stored copy is newest.

## 4. Outside verification register

The following checks supplement, rather than replace, the stored-source review. Accessed during this October 4, 2026 Pacific review (repository commits may use October 5 UTC). They establish narrow documented behavior, not local executable compatibility.

| Subject | Primary URL / version | Supported conclusion |
|---|---|---|
| Rigidbody.AddForce | https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddForce.html | Nonzero force normally wakes the Rigidbody; source's mandatory sleeping-only diagnosis is not justified |
| Physics.Raycast | https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html | Default trigger policy is UseGlobal; actual global/argument settings matter |
| TextureHandle.GetDescriptor | https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/api/UnityEngine.Rendering.RenderGraphModule.TextureHandle.html (page identifies 17.0.4) | Returns TextureDesc; do not promote the source's mismatched example as verified C# |
| Unity Companion License | https://unity.com/legal/licenses/unity-companion-license (1.4, dated 2024-10-29) | Unity-dependent use conditions and required copyright/license/third-party notices must be considered before substantial copying/adaptation |

Both stored roots name Unity Companion License, not MIT or Apache. No vendor code, substantial skill text, trademark assets, fonts or packages were copied into the harness by this review. Any subsequent redistribution/adaptation must retain applicable notices and meet the license conditions; this report does not grant redistribution rights or change the repository's license. A maintainer's SECURITY accepted-risk declaration is not this user's authorization and not independent security certification.

## 5. Proposed validation cases — authored, NOT_RUN

| ID | Scenario | Required outcome |
|---|---|---|
| UR-T01 | Two Editor instances, or stale project identity | Target exact approved project; wrong/ambiguous target blocks without launching another Editor |
| UR-T02 | Ready response but frozen frame/state | No gameplay PASS from screenshot/Play entry; bounded observation reports failure/incomplete evidence |
| UR-T03 | Job accepted, then busy/interrupted/unavailable/timeout | No false completion, model polling loop, duplicate scan or inferred cancellation |
| UR-T04 | Wait depends on a later command | Avoid queue deadlock; use supported async scheduling with deadline and retained identifiers |
| UR-T05 | Capture of overlay UI | Correct explicit capture source; original saved file and bounded preview/summary, not inline bulk data by default |
| UR-T06 | Search query contains quotes; provider/index incomplete | No code interpolation; bounded results and explicit coverage limitations, not false absence |
| UR-T07 | Auditor has no rules or empty/incomplete CSV | Distinguish unavailable/zero coverage from a completed clean analysis |
| UR-T08 | Existing Auditor findings plus one new issue | Report baseline delta; preserve prior findings; do not authorize whole-project cleanup |
| UR-T09 | New asset exists in memory but required sub-asset/listener is not persisted | Save/reload/readback and behavior checks expose incomplete authoring |
| UR-T10 | Rendered UI lacks approved interaction or input support | Acceptance stays unmet; no visual-only reinterpretation or framework rewrite |
| UR-T11 | Localization has zero entries, empty required locale value, or runtime-composed text | Report scope/count/gaps; do not silently fill English or claim complete conversion |
| UR-T12 | Missing/unsupported package or API | No automatic install/upgrade, adjacent-version guessing or substitute backend |
| UR-T13 | Physics symptom matches confident source fast-path but evidence conflicts | Keep hypothesis unconfirmed and investigate relevant evidence; no forced diagnosis |
| UR-T14 | Source recipe uses mismatched Render Graph API type | Reject or fix against actual package and compile; static review is not runtime proof |
| UR-T15 | Same skill name, different referenced-file versions | Pin one coherent variant; missing/mismatched references and malformed metadata fail validation |
| UR-T16 | Approved bounded repair already exists | No repeated permission gate for ordinary covered edits; extra scope and destructive changes still stop |

Run deterministic fixture tests for parsers, payload bounds, job-state mapping and negative outcomes before the Windows/Unity pilot. Then test actual commands, persistence and UI behavior in a disposable approved project. Compare task correctness, interventions, repeated calls and actual usage when telemetry exists; do not infer billed-credit savings from fewer files or a vendor claim.

## 6. Implementation boundary and recommended sequence

Keep the five existing core skills. Add small procedure references only when they answer an observed recurring need. The default game package must not contain either complete Unity catalog. Select applicable references using the approved task and observed project capabilities, not a new layer of autonomous agent planning.

First finish the already-open efficiency validation and prerequisite decisions. Then implement a small Unity inspection/job adapter with explicit supported capabilities and synthetic negatives; follow with the optional Project Auditor report adapter. Add the asset/UI completeness checks to existing verify/implementation procedures. Feature-specific performance/navigation/rendering references follow only for affected projects. Expensive rebuilds/imports and human player judgments remain separately scoped.

This review wrote only review artifacts. It did not modify the runtime, install manifest, design GPT, original Reference collection or live projects; it ran no Unity/Codex processes and no harness test suite. The previous 44 unrerun package/design/static tests and two unimplemented efficiency mechanisms remain open. Nothing here changes draft PR #1 into approval to merge, release or adopt.

## Durable continuation

Use this report and UNITY_REFERENCE_INVENTORY.json for the next scoped incorporation work. Do not repeat the completed thirteen-body review, claim the nineteen metadata-only families were audited, or activate source instructions on the strength of this report. Before copying any additional leaf, read its complete needed references, validate rights/version/API applicability, and add focused positive/negative tests. Keep unavailable integrations NOT_RUN, preserve originals, recheck the branch head and commit each coherent implementation/evidence batch without force-push.
