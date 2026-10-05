# Codex consumer — compact operating reference

This is execution guidance, not a game design. The canonical wire schema remains `.bh/schema.json`; `INTERFACE.md` is the complete paired contract. Producer-only framework/persona retrieval applies to the design host, not Codex. Read only this project's approved handoff inputs. No source game supplies defaults.

## Routine context
At task start use AGENTS, project configuration and the checkpoint. For an initialized task run `python Tools/BH/views.py --root . context`. This read-only projection validates the handoff, plan and current evidence and includes every criterion, invariant, risk, scope/action limit, approval subject, blocker and next action. The full file-hash roster stays in the referenced machine records. `recorded_phase` is historical state, not a new acceptance claim. A context command may return exit 2 with useful JSON because final evidence is missing. Fix the stated issue; do not retry the same read in a loop.

Read the handoff's `read_order` and relevant code. Do not dump complete plans, receipts, schema families or old logs into routine context. For an integrity question, retrieve the exact underlying record and run deterministic validation. Never infer human approval from the view.

## Intake and mechanical fields
Use `bh.py validate-handoff`, `init`, `plan`, `approve` and `begin` as documented. To inspect one complete schema family use `python Tools/BH/views.py --root . schema proposal` (or another definition). It includes transitive local references, not unrelated definitions.

`views.py --root . draft-proposal Handoff/handoff.json` prints a schema-valid but deliberately blocked draft. It supplies IDs and acceptance mapping; replace unresolved content with actual implementation decisions and repository evidence. It creates no approval and writes no file unless the operator explicitly redirects output. Do not erase a blocker without resolving it.

## Evidence return
After verification, `python Tools/BH/views.py --root . return` writes the existing full RETURN.json/RETURN.md and derived AGENT_RETURN.json/HISTORY_INDEX.json under `.bh/exports/<task>`, under the writer lock. This is not read-only. Prefer AGENT_RETURN.json for the design review: all criteria, deviations, human status and current evidence references remain. It references the hashed complete return and historical receipt index; it is not a replacement wire contract or independent attestation.

Transfer the compact view, pinned design, and supporting receipts/results through an authorized channel. Fetch historical failures when relevant; do not automatically load every old run. Local paths remain unavailable to a remote design host until transferred. Never count a compact projection as new execution, approval, or a passed human test.
