---
name: bh-review-handoff
description: Validate a design-to-Codex handoff or prepare an evidence-backed return to the design method. Do not approve or implement.
---

# bh-review-handoff

Read Docs/Harness/INTERFACE.md and the current handoff's exact read_order. Run `validate-handoff Handoff/handoff.json`; use `--draft` only for incomplete authoring review. Check genuine design approval externally, acceptance roster, project invariants, manifest hashes, required checks, and unresolved decisions. Valid means eligible for reconciliation, not approved execution.

For intake, `init Handoff/handoff.json` creates task state. Author a technical proposal with the schema's proposal fields, then `plan PATH`. Present its exact plan hash and discrepancies to the human. Do not write an approval on their behalf.

For return, run `return`. Upload/publish RETURN.json, the relevant approved artifacts, receipts, and requested raw result artifacts through an authorized path. Local paths are unavailable to the design GPT until retrieved. Keep logs out of the summary; distinguish claims, actual observations, NOT_RUN checks, deviations, and pending human playtest.

Inputs: version-matched contracts and actual retrieved artifacts. Outputs: validated intake or .bh/exports/TASK/RETURN.json and .md. Missing resources block the affected procedure. Example: a passing NUnit check plus pending game-feel criterion must return PENDING human acceptance, not Accepted.
