# Codex efficiency review — findings and measured reproductions

Review baseline: `b002e3cc0b2134868c36ea93dadc83aaa7333739`.
Status: REVIEW COMPLETE; efficiency changes PROPOSED, NOT IMPLEMENTED.
Scope: the installed Codex consumer, handoff/return interface, recurring context, verification, and recovery. The original game-agnostic runtime, installer, contracts, design package and installation manifest are unchanged by this review. PR #1 remains draft. Prior functional-test success is not a credit-efficiency benchmark.

## Verdict

The candidate has useful cost controls, but is not yet demonstrably credit-efficient. Its most important avoidable costs are model-facing bookkeeping, unnecessary verification/reconciliation, and an over-restrictive ordinary failure loop. The five small skills are not the main problem. Local hashing and receipt work also have concrete scaling defects, but their CPU/I/O is not itself a model-token charge.

Prioritize compact views for the agent, incremental verification with preserved final gates, and a normal scoped repair path. Do not replace the harness, remove approval/evidence protections, or build another orchestration platform.

## Basis and measurement limits

The source review read AGENTS, all five SKILL.md files, operating guide, shared interface, configuration and the runtime's approval, snapshot, scope, plan, subprocess, verification, audit, recovery, return and CLI logic. Connector reads pinned the current code and source identities. The local 22-file installed template was reconciled byte-for-byte to Git tree `ce27c06dfeee268ca718b7fcf08eee160ab02af8`. The runtime is blob `5dff7bef67a6ee750918e190ce635ac1cddf2857`, 73,100 bytes; the test support and fixture driver match current blobs `f857e634e084fa2ae50af13e337a69f6ab26696b` and `d664cf352242a661ac02e2ca2173819aaaa0815b`. This is materialization of existing code, not a reimplementation.

`review/tools/measure_codex_overhead.py` was executed against that code in disposable, visibly synthetic Git projects on Linux/Python 3.13.5. Instrumentation wraps real methods without replacing their behavior. Real fixture subprocesses write observations; the real harness constructs and audits receipts. All probe assertions passed. Results: `review/evidence/codex-efficiency/MEASUREMENTS.json`.

These probes are separate from the historical 148-test suite. No native Codex session, Windows, Unity Editor, real game, billed-credit measurement, or before/after optimized runtime was tested. Timings are one local sample each, not production benchmarks. Output byte counts are not token counts. CLI stdout is generally compact; the large maps described below are stored records that may enter context when an agent follows the reading instructions, not automatic uploads of every asset.

Reproduce from a trusted checkout of the reviewed candidate, using a NEW output file outside the checkout:

```text
python -B BH-Unity-Harness/review/tools/measure_codex_overhead.py --package BH-Unity-Harness --output <new-disposable-output-path>/measurements.json
```

Do not use Python optimization flags that disable assertions. The script imports the repository fixture helper and checks the pinned runtime. Inspect it before execution. The measured platform is Linux; the fixture's Git setup is not a Windows compatibility claim. Counts can vary with environment; the stored outcomes are the observed run, not promised universal counts.

## Ranked findings

Priority denotes recommended remediation order, not an invented estimate of credits saved. All runtime line numbers below refer to `project-template/Tools/BH/bh.py` at the pinned baseline.

| ID | Priority | Finding | Main cost channel | Evidence |
|---|---|---|---|---|
| EF-01 | High | Agent-facing plan/return records contain complete source hash maps | Avoidable model context if read in full | Actual 1,031-file fixture payloads |
| EF-02 | High | Verification reruns already-valid checks and lacks focused selection | Redundant tools, results and model-led test handling | Unchanged fast-to-slice reproduction |
| EF-03 | High | Ordinary failures exhaust recovery before documented stuck thresholds | Extra interventions, re-planning and repeated context | Two-failure reproduction |
| EF-04 | High | Whole-input defaults and commit identity cause excessive invalidation | Rechecks/reconciliation without affected behavior changes | Default versus narrow and empty-commit probes |
| EF-05 | Medium | Consumer instructions include producer-only retrieval; schema access is broad | Unnecessary reference retrieval and manual schema work | Installed instructions/interface source review |
| EF-06 | Medium | Mutable pinned test helpers conflict with approved test edits | Binding changes can force reapproval during iteration | Authorized helper-edit reproduction |
| EF-07 | Medium | Routine status audits every superseded run and return lists all receipts | Growing local work; excess evidence retrieval if followed | Eight-run status/return reproduction |
| EF-08 | Medium | Repeated full snapshots and per-path directory scans scale poorly | Primarily local I/O/CPU; indirect wait/retry overhead | Call counts and dense-directory probes |

### EF-01 — Keep integrity records out of normal reasoning context

Source: `make_plan` lines 579-619 embeds `baseline: snap`; `verification` lines 801-876 embeds the full snapshot in each receipt; `return_report` lines 980-1029 embeds it again in `source_snapshot`. The implementation skill says to read the approved plan, while the handoff/return skill selects RETURN.json for transport. There is no dedicated compact plan/context projection in the CLI.

Actual fixture with 1,000 additional small files, 1,031 total snapshot files:

| Record | Actual bytes |
|---|---:|
| Approved plan JSON | 116,236 |
| Receipt JSON | 118,070 |
| RETURN.json | 116,009 |
| Existing RETURN.md | 580 |

Three copies of the path/hash map exist across these records. This is reasonable machine evidence but poor default model input. The Markdown result demonstrates an existing compact route, although a real task's complete acceptance summary may be larger. No exact token/credit conversion is justified.

**Proposed change:** keep immutable machine records and expose deterministic compact views containing the actual task, scope, constraints, approval subject, relevant file paths, acceptance criteria, current failures and next action. Exclude the full hash roster by default; expose it on explicit inspection. Content-address the full source manifest once and reference it where contract migration permits. Do not omit criteria or silently truncate approval meaning to hit a cosmetic size budget. Make the consumer skill prefer the view and read only needed machine fields programmatically. Preserve a complete, retrievable evidence path.

**Acceptance:** scaling irrelevant fixture files from hundreds to thousands should not expand the routine agent context by the whole roster; every acceptance criterion and actual blocker remains visible. Altering a manifest or required artifact still fails verification.

### EF-02 — Coverage profiles are not incremental execution

Source: `verification` lines 801-876 selects every handoff check with profile <= requested profile and executes it. Existing valid results are consulted by `audit_results` only after execution. The CLI lines 1151-1232 offers a profile, not check-ID/affected-check selection or a pre-execution reuse decision.

Actual probe: `fast` passed CHECK-01; with no input change, `slice` executed CHECK-01 again, plus the manual placeholder. This is confirmed redundant check execution, not merely inferred from prose. A second probe showed later checks still execute after an ordinary FAIL; the loop stops for mutation, timeout or cancellation, not assertion/compile failure. That fixture did not declare a dependency between checks, so running its second independent check is not itself a demonstrated bug. The missing capability is dependency-aware staging for expensive checks that cannot be useful after a prerequisite fails.

**Proposed change:** support approved check selection and stale/missing/failed selection; validate dependency and artifact freshness before reusing results. Preserve explicit final full/profile runs wherever the approved validation plan requires them. Allow declared prerequisites to block dependent builds/tests after compile failure, while still collecting useful independent diagnostics. Mark unexecuted required gates NOT_RUN/BLOCKED, never PASS. A reused receipt must retain its original run/time/source identity, not be relabeled as newly executed.

**Acceptance:** an unchanged fast-to-slice call reuses eligible CHECK-01 evidence unless an explicitly required fresh final run says otherwise; relevant code/config/fixture changes rerun it; dependent expensive checks do not launch after their prerequisite fails; final gate coverage is complete.

### EF-03 — Separate ordinary repair from exceptional recovery

Source: `verification` moves to FAILED after the first failing round, even below the stuck thresholds. `recovery` lines 967-978 is the documented return to EXECUTING and consumes `recovery_cycles` on each call. Default project configuration allows one recovery cycle but three failed/repeated/no-progress rounds.

Actual probe: first FAIL -> recover -> second FAIL -> second recover refused with `Recovery budget exhausted; human must revise scope/plan, not loop`. At refusal all three failure counters were 2, below their configured threshold of 3. This is a reproduced lifecycle/default mismatch that can escalate normal iterative development prematurely. It is not evidence that unlimited autonomous retries would be better.

**Proposed change:** a bounded, evidence-led ordinary repair transition within the approved scope should be distinct from the special recovery cycle used after stuck detection. Preserve failure counters, new-evidence requirements, cancellation, quota handling and escalation on material scope/authority changes. Raising all thresholds indiscriminately is not the fix.

**Acceptance:** ordinary authorized repairs can proceed until the approved stuck boundary; the exceptional cycle is consumed only there; repeated identical failures without new evidence still stop; no failure changes acceptance thresholds or claims human approval.

### EF-04 — Invalidate affected claims, not every harmless project event

Source: `dependency_hash` lines 461-466 selects every nonvolatile input when `dependency_paths` is empty and includes the Git commit. Reviewed narrow dependencies already exist. `scope` lines 455-459 separately requires HEAD to match the original plan; `approve` lines 621-633 requires the full original planning snapshot. Whole configuration/core changes also require replanning.

Actual probes: modifying `Source/unrelated.txt` made an unrelated passing criterion NOT_RUN under the default; the same edit preserved PASS with the existing reviewed narrow binding. An empty Git commit changed no input-file bytes but made resume fail with `Git revision changed; reconcile/replan explicitly` even with narrow test dependencies.

**Proposed change:** derive and review per-check dependency sets during design/reconciliation, including fixtures, configuration, assets and relevant shared contracts. Use conservative whole-input fallback only where dependency closure is genuinely unknown. Separate provenance commits from evidence validity by content, with an explicit authorized content-preserving checkpoint reconciliation route. This must not permit silent rebases, branch switching, concurrent-source changes or removal of the user's approval gate. Any approval-policy adjustment needs an explicit candidate compatibility decision and tests.

**Acceptance:** unrelated edits preserve unaffected results, relevant/shared changes invalidate them, and an explicitly permitted content-preserving checkpoint does not require regenerating an identical technical plan. Real changes outside approved scope remain blocked.

### EF-05 — The Codex consumer should not retrieve the design method

Source: the byte-identical shared `Docs/Harness/INTERFACE.md` contains `Required design resources` and instructions to retrieve the full method/K01 for full system work and K12/interface/schema for handoff work. Those resources are deliberately outside the installed game. The handoff skill reads that interface. AGENTS correctly says not to load the full design library, so this is an instruction-role ambiguity, not an observed native-model retrieval failure.

The operating guide also tells the reader to consult the exact schema. The schema is 56,715 bytes/2,414 lines; the proposal definition alone serializes to 2,426 bytes, excluding transitive references. Shared interface is 11,614 bytes and operating guide 15,544. These disk files are not automatically token charges, but an overly literal full-file read would be avoidable overhead.

**Proposed change:** explicitly label producer-only procedures and generate a concise consumer guide from the same owned contract. Keep one canonical machine schema, not divergent contracts. Add a deterministic command to show one schema definition plus required references and generate validated proposal/approval-record skeletons and hashes locally. The agent supplies substantive plan decisions; scripts handle boilerplate. Compose redundant nonmutating preparation operations behind a single entry point if useful; keep human approval separate. Multiple shell commands are not necessarily multiple model turns, so do not invent a fixed turn-saving figure.

**Acceptance:** a fresh installed Codex consumer can validate, plan, execute and return without asking for producer personas/frameworks; schema queries return complete relevant definitions rather than unrelated contract families; generated records never fabricate human decisions.

### EF-06 — Distinguish reviewed runners from changing test content

Source: `binding_ready` lines 468-513 checks every pinned `input_files` hash and requires a Python entry script to be pinned. That is an intentional execution safeguard. It becomes expensive when the same entry script is also approved mutable test content.

Actual probe explicitly allowed the Tests directory and then appended a harmless comment to the pinned fixture driver. Verification was BLOCKED before launching it: `Missing or changed artifact: Tests/fixture_driver.py`. This affects pinned helpers/inputs, not every Unity test file.

**Proposed change:** use stable reviewed runner adapters and separate task-owned tests/data tracked as current tested dependencies. Where the executable itself genuinely changes, keep the reviewed code-execution/approval boundary and provide a narrow rebind process. Do not bless arbitrary changed scripts just because their directory is writable.

**Acceptance:** an authorized edit to task-owned tests does not require repinning an unchanged runner; an unauthorized executable/helper change remains blocked; relevant evidence becomes stale correctly.

### EF-07 — Current evidence and full historical audit need different paths

Source: `audit_results` lines 878-939 iterates every retained run, validates snapshot/configuration/core identities, calculates dependencies repeatedly, hashes artifact files and reparses prior passing results. It is called by status, resume, return and verification. `return_report` additionally lists every retained receipt, even if the current acceptance mapping references only the latest one.

Actual status after eight successful superseding runs: one snapshot, five Git calls, 519 file-hash calls, 26 harness-hash and 26 configuration-hash calls, and eight NUnit reparses. Stdout was only 297 bytes: this particular burden is local computation, not a huge status response. The return listed eight receipts while the current automated criterion referenced one.

**Proposed change:** index the current supporting receipt per check; retain an immutable historical ledger. Validate current supporting evidence fully at trust boundaries, and make full-history audit explicit. Cache unchanged small core/configuration digests within a single operation; do not blindly trust stale cross-operation caches. Export the bounded current evidence set and a historical index; include earlier failures when relevant to the review rather than making every old run a mandatory default retrieval.

**Acceptance:** repeated status on the same evidence does not reparse every superseded result; corrupt/missing current artifacts still invalidate the claim; historical failure evidence remains accessible and distinguishable.

### EF-08 — Snapshot cost is multiplied and dense paths approach quadratic work

Source: `safe` lines 119-130 enumerates children at each path component for each file. `snapshot` lines 231-259 calls it across tracked/untracked nonignored inputs. `make_plan` takes a snapshot and invokes a preflight that takes another; begin similarly repeats snapshots. Verification takes an authorization snapshot, a pre-run snapshot, one after every selected check including manual placeholders, and a final snapshot: N+3 snapshots for N executed check entries.

Actual one-automated-plus-manual slice: five full snapshots and 26 Git calls. Dense-directory probes with 100 versus 500 extra files visited 11,792 versus 256,992 directory entries. The repeated sibling enumeration explains the near-quadratic component; file payload sizes barely changed. Single-sample timings were 0.058223 and 0.794178 seconds, not a Windows/Unity prediction.

**Proposed change:** build a per-operation case/path index and share immutable snapshot/core metadata where no mutation boundary intervenes. Revalidate at actual process/write boundaries; keep link/junction/escape checks. Manual placeholders do not execute a workspace-mutating process. Do not eliminate required post-process mutation detection or hash only C# while ignoring affected serialized assets. Profile the real project before introducing a complex persistent cache or daemon.

**Acceptance:** dense sibling traversal is approximately linear in file count; safety regressions remain covered; duplicate reads within nonmutating preparation are removed; source-changing checks still fail.

## Conditional Unity concern, not a measured defect

`run_check` creates one process per bound check. A binding whose tool kind is Unity is currently batch-only and requires a closed project; an open Editor is intentionally blocked. Several independent Unity bindings could therefore repeat launch/import costs, while an unavailable Editor route could prompt repeated troubleshooting. No real Unity bindings were exercised in this review. During the pilot, preserve one working mutation route and evaluate grouping compatible tests or using a supported existing-Editor route without importing a new orchestration stack. Do not claim measured Editor startup or credit savings.

## Keep these strengths

AGENTS is 3,888 bytes; all five skill bodies together are 7,362 bytes and are explicitly selected. The installed package does not copy the authoring library. CLI stdout is already compact. Runtime does not call a model API or create worker fleets. Raw logs are separate, human-only criteria remain pending, and reviewed narrow dependencies already work. Keep these controls. A smaller safety paragraph is less valuable than fixing repeated planning or a hundred-kilobyte model-facing record.

## Outside verification, distinct from repository observations

Official OpenAI documentation was checked during this review, following these redirects:
- https://developers.openai.com/codex/pricing -> https://learn.chatgpt.com/docs/pricing
- https://developers.openai.com/codex/skills -> https://learn.chatgpt.com/docs/build-skills

The pricing documentation identifies context, reasoning, tool use, retrieval and caching as usage factors; files/history/tool results can become token input, and cached input is metered separately. Credit rates alone do not determine included subscription consumption. The skills documentation describes metadata-first progressive disclosure, with the full body loaded on selection. These points support compact relevant context, not a byte-to-credit estimate. No plan quota, pricing multiplier or model selection is inferred for the user's account.

## Bounded remediation sequence and validation

1. Agent interface: compact plan/context/return views, role-specific consumer guidance, focused schema extraction and locally generated mechanical fields. Preserve full machine evidence.
2. Execution loop: explicit affected-check selection/reuse, prerequisite gating, reviewed dependency maps and ordinary repair versus exceptional recovery. Keep mandatory final gates and human authority.
3. Local runtime: avoid duplicate snapshots and core hashes, index case-sensitive paths and current evidence; measure before adding persistence/daemons.

Before adoption compare baseline and proposed candidate on the same narrow task, unchanged resume, unrelated edit, relevant edit, two ordinary failures, content-preserving checkpoint and missing/tampered evidence. Record model/effort/speed/host, actual input/cached/output usage where available, tool-result bytes, useful versus repeated checks, interventions, task correctness and acceptance coverage. Warm/cold cache and differing task outcomes must not be conflated. No additional paid account or API purchases are needed for the proposed design.

The final finding is architectural: let deterministic code do the bookkeeping and let Codex see only the bounded decisions and evidence it needs. Efficiency fixes are still OPEN; the requested review and its synthetic reproductions are complete. Windows/Unity/native-Codex behavior and measured savings remain NOT_RUN.
