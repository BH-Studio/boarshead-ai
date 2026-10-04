---
name: bh-systematic-debug
description: Diagnose a failed or interrupted approved slice using bounded evidence-led recovery. Do not broaden scope or bypass approvals.
---

# bh-systematic-debug

Read checkpoint, the latest failed receipt and only the relevant raw output. Categorize deterministic defect, infrastructure/tool unavailability, refresh/domain reload, user interruption, or observed service limit. State a falsifiable hypothesis, one discriminating observation, and the smallest permitted repair. Repeated reads/rewrites alone do not prove a stuck loop.

The runtime counts completed verification rounds, identical result fingerprints, no acceptance progress, and infrastructure failures separately. Configured defaults are proposals, not research-proven constants. At a threshold it checkpoints and stops. `recover "Concrete diagnosis and one bounded next action"` consumes the recovery budget; a revised scope or exhausted budget requires human decisions. Never reset/clean/broad-restore or weaken tests.

For interruption, use `resume`; inspect process ownership before retrying. Stale locks are not automatically deleted. Do not kill a live owner, the user's Editor, or another session. For observed quota limits checkpoint and stop; no indefinite sleep/retry.

Inputs: current plan and retained failure evidence. Outputs: bounded diagnosis, preserved evidence and exact next action; no self-approved acceptance. Example: a missing Unity executable is an environment blocker, not a reason to mark compilation N/A.
