# Contract — <actual ID/name/revision>

Status: TEMPLATE — NOT AUTHORIZED
Owner / approval / supersedes: <actual records>
Affected milestone/system/consumers: <actual>

## Purpose, scope and non-goals

State why a stable contract is necessary. Name the actual consumer(s); a possible future consumer
is not reuse already proven. Prefer a simple boundary over a universal abstraction.

## Canonical state and dependency direction

| State/data | Definition/runtime/campaign/knowledge/presentation | Owner | Permitted writers | Readers | Reset/persistence |
|---|---|---|---|---|---|
| <actual> | <actual> | <actual> | <actual> | <actual> | <actual> |

## Public operations/events

For each, specify exact approved signature or explicitly approved new deliverable; preconditions;
actor/authority; input units/ranges/IDs; validation; transition; outputs/feedback; ordering/time
source; concurrency/reentrancy; duplicate/stale/canceled behavior; error category and observability.
Distinguish command, query and semantic notification. Do not prescribe a mandatory global event bus.

## Lifecycle and failure

Initialization/dependencies, activation, interruption, disable, pool/reuse, scene unload, retry,
disconnect and shutdown as relevant. State safe behavior for missing dependencies, bad data,
invariants and overload. No silent repair or novel fallback that changes player behavior.

## Persistence/network/compatibility

Schema/content versions; identity and numeric representation; semantic versus byte equality;
compatibility window and migrations; unknown content/corruption; atomicity and recovery; authority,
replicated state and request idempotency as applicable. Mark intentionally unchanged categories.

## Scale, budgets and diagnostics

Approved workload axes/bounds, resource envelope, measurement method, limits, counters/logs and
failure classification. Avoid exposing secret/player data or narrative spoilers in player-facing diagnostics.

## Examples, fixtures and conformance

Supply valid, boundary and invalid examples; exact invariant assertions; consumer test setup and
approved result requirements. Keep fixtures synthetic and labeled as data, not agent instructions.

## Decision trace and change control

Source decision/ADR, alternatives/rationale, consequences, validation obligations and actual human
approval. Any semantic change needs explicit versioned review, migration/rework and affected test map.
