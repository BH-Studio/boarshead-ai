---
name: b1-state-persistence
description: "Handle approved Breach One state, stable IDs, saves, migrations and compatibility changes. Apply determinism only where required; do not import galaxy-world formats or policies."
---

# b1-state-persistence

Package: B1-CODEX-OPS | Version: 0.1.0
Authority: use only within the adopted repository instructions and the current authorized task.

## State inventory

Read the actual owner/contracts and affected save/definition fixtures. Distinguish configuration,
instance runtime state, campaign/session changes, participant knowledge and rebuildable presentation.
List which persists, resets, is replicated, is derived or remains out of scope. Do not store campaign
contributions or shared access resources in character inventory by convenience.

## Contract work

Define stable identity and units at actual persistence boundaries. Separate display names and
process-local handles from persistent IDs. Explicitly specify semantic versus byte equivalence,
ordering/numeric rules and RNG ownership only when the approved contract needs them. Do not
ban all Unity vectors or randomness because a different project required astronomical determinism.

Read exact schema/storage/content versions and compatibility window. Determine old-data handling,
unknown/missing definitions, migration order, integrity failures, partial writes, cancellation,
corruption, backup/recovery and source preservation. An unsupported format must follow the approved
failure policy, not be silently repaired, regenerated, downgraded or replaced with a blank save.
Do not introduce encryption, cloud saves or modding support without a requirement.

## Integration

Trace save/load and retry/checkpoint boundaries through character, operation, narrative and session
owners. For co-op, use the separately approved save-owner and participant rules; do not infer them
from network-host authority. Avoid mixed-revision state, duplicate rewards and accidental persistence
of prototype/debug flags. Never test destructive migration against a real player's only save.

## Validation/output

Use synthetic/versioned fixtures for round trip, old format, missing/unknown content, interrupted
write, invalid data and reset/lifecycle cases. Run consumer/regression checks as specified.
Return old/new versions, migration/recovery behavior, affected owners, fixture identities, observed
results and unresolved compatibility risks. Keep schema or persistence meaning changes behind
human-approved change control. A working serializer alone does not prove valid campaign state.
