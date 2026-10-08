# Codex consumer — compact operating reference

This is execution guidance, not a game design. The canonical wire schema remains `.bh/schema.json`; `INTERFACE.md` is the complete paired contract. Producer-only framework/persona retrieval applies to the design host, not Codex. Read only this project's approved handoff inputs. No source game supplies defaults.

## Routine context
At task start use AGENTS, project configuration and the checkpoint. For an initialized task run `python Tools/BH/views.py --root . context`. This read-only projection validates the handoff, plan and current evidence and includes every criterion, invariant, risk, scope/action limit, approval subject, blocker and next action. The full file-hash roster stays in the referenced machine records. `recorded_phase` is historical state, not a new acceptance claim. A context command may return exit 2 with useful JSON because final evidence is missing. Fix the stated issue; do not retry the same read in a loop.

Read the handoff's `read_order` and relevant code. Do not dump complete plans, receipts, schema families or old logs into routine context. For an integrity question, retrieve the exact underlying record and run deterministic validation. Never infer human approval from the view.

## Intake and mechanical fields
Use `bh.py validate-handoff`, `init`, `plan`, `approve` and `begin` as documented. After the human approves the current reviewed plan, record the actual decision with `approve --by NAME --source REFERENCE`. The harness creates its internally bound record; do not ask the human to paste a plan hash or author approval JSON. Do not invent consent. To inspect one complete schema family use `python Tools/BH/views.py --root . schema proposal` (or another definition). It includes transitive local references, not unrelated definitions.

`views.py --root . draft-proposal Handoff/handoff.json` prints a schema-valid but deliberately blocked draft. It supplies IDs and acceptance mapping; replace unresolved content with actual implementation decisions and repository evidence. It creates no approval and writes no file unless the operator explicitly redirects output. Do not erase a blocker without resolving it.

## Evidence return
After verification, `python Tools/BH/views.py --root . return` writes the existing full RETURN.json/RETURN.md and derived AGENT_RETURN.json/HISTORY_INDEX.json under `.bh/exports/<task>`, under the writer lock. This is not read-only. Prefer AGENT_RETURN.json for the design review: all criteria, deviations, human status and current evidence references remain. It references the hashed complete return and historical receipt index; it is not a replacement wire contract or independent attestation.

Transfer the compact view, pinned design, and supporting receipts/results through an authorized channel. Fetch historical failures when relevant; do not automatically load every old run. Local paths remain unavailable to a remote design host until transferred. Never count a compact projection as new execution, approval, or a passed human test.

## Efficient verification and repair
Use `bh.py --root . verify --profile slice --reuse` for intermediate work, optionally selecting reviewed IDs with repeated `--check ID`. Missing/stale/failed checks run; a validated reusable PASS points to its original receipt and time. An all-reuse operation executes nothing and creates no new receipt. A changed executable still blocks reuse. Empty/unknown/out-of-profile selections fail.

Final completion uses `bh.py --root . verify --profile <required-profile>` WITHOUT `--reuse` or a partial selection. All required checks must have current support from one complete fresh profile run; human checks remain pending. Mixed partial runs and a high profile label alone cannot manufacture this gate. `--fail-fast` stops the ordered sequence after the first FAIL/ERROR/BLOCKED, leaving later checks unrun. Put prerequisite checks first in the approved handoff and use separate selected calls for independent diagnostics. This is conservative sequential staging, not an automatic dependency-graph scheduler.

For a normal FAILED result below configured thresholds use `bh.py --root . repair "Observed evidence, falsifiable hypothesis and bounded correction"`. It does not consume exceptional recovery or reset failure counters. PAUSED/BLOCKED/stuck work still requires explicit recovery and authority. The one exceptional cycle stays bounded. Neither route changes scope, test thresholds or acceptance.

Routine status/resume/context audit newest supporting results; `bh.py --root . status --history` explicitly validates superseded raw artifacts too. Failed history is retained, not deleted. Current corrupt/missing evidence blocks; it is never silently replaced with an earlier green result. Full records and the history index remain available for investigation.

## Dependency and runner preparation
Review each check's dependency_paths during reconciliation. Include affected code, tests/data, serialized assets, configuration and shared contracts; record dependency_review_ref. Empty paths deliberately retain whole-input fallback. Never guess a narrow set only to avoid a rerun. Use stable reviewed runner entry points and task-owned tests/data as dependencies; do not pin editable tests as the executable helper. Changes to the actual executable or pinned helper still require reviewed binding changes. Test-directory write permission is not arbitrary execution approval.

Git is optional. Without usable Git at the project root, snapshots use nonvolatile filesystem content and `commit=null`; no initial commit is needed. Filesystem mode does not interpret `.gitignore`. When Git provides the source roster, commit identity remains strict, including content-identical commits. Finish the slice or perform explicit reconciliation before changing HEAD or switching snapshot modes. A content-preserving checkpoint continuation protocol and machine-declared prerequisite graph remain open implementation items; neither is silently enabled here.
