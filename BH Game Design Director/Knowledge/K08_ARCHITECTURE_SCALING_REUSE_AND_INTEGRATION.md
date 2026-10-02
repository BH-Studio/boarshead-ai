# Architecture, Scaling, Reuse, Persistence, and Integration Reference

## 1. System boundary
For substantial systems identify:
- canonical owner;
- inputs/outputs;
- dependencies and dependency direction;
- public contracts/events/queries/commands;
- lifecycle/initialization/shutdown;
- failure behavior;
- neighboring systems that consume or mutate state.

Prefer stable contracts around volatile implementation details.

## 2. Separate meanings of state
When applicable distinguish:
- **definitions/configuration** — what can exist;
- **runtime state** — what is happening now;
- **player/discovery knowledge** — what a specific actor knows;
- **campaign/session state** — what this playthrough changed;
- **presentation/cache state** — derived/rebuildable data.

Do not merge these only because a single class or save file could technically hold them.

## 3. Data-driven design
Use data-driven policy where it improves tuning, content creation, variation, testing, or modding. Avoid moving behavior into data merely to claim flexibility.

Define:
- stable IDs/references;
- schema/validation;
- defaults/overrides;
- invalid-data behavior;
- authoring source vs runtime representation;
- canonicalization/determinism where required.

## 4. Persistence/versioning/migration
For save-dependent systems decide early:
- what persists;
- schema/version identifiers;
- backward-compatibility window;
- migration strategy;
- unknown/missing definition behavior;
- corruption/integrity handling;
- load failure/recovery;
- semantic vs byte-equivalence requirements;
- export/import/modding policy if relevant.

## 5. Scale is a vector, not a single number
Define scale axes relevant to the system, e.g.:
- entities/objects/systems/players;
- active vs dormant items;
- update/event rate;
- simultaneous queries;
- save size;
- content definitions;
- network replication volume;
- pathfinding/simulation jobs;
- lifetime accumulated records.

For each important axis define:
- **Nominal** — ordinary expected workload;
- **Target** — product requirement;
- **Stress** — deliberate margin/overload test;
- **Failure/guardrail** — where behavior degrades/rejects safely.

## 6. Resource envelope
Measure only resources that matter, such as:
- main-thread/frame time;
- worker CPU utilization;
- memory/allocations/GC;
- GPU if relevant;
- I/O and save/load duration;
- storage/artifact size;
- network bandwidth/packet rate;
- background processing budget.

Budgets must be project-specific. Do not copy a percentage or threshold from another system without re-deriving it.

## 7. Reuse test
Before calling a system reusable, name at least one realistic second consumer or extension case.
Then identify:
- reusable core;
- game-specific policy/adapters;
- public surface;
- extension points intentionally supported;
- unsupported internal surface;
- version compatibility;
- clean-consumer test.

Avoid speculative abstraction that increases indirection before a consumer exists.

## 8. Clean-consumer / conformance testing
For a declared reusable package/module, validate it from outside its home environment using only supported public contracts. This exposes hidden dependency/coupling.

## 9. Determinism and concurrency
Do not add determinism/threading/ECS automatically. Ask what claim requires them.
When required define:
- deterministic inputs/state/order;
- RNG seed/stream ownership;
- floating-point/platform tolerance;
- job/thread ownership;
- synchronization/atomicity;
- event ordering;
- replay/conformance expectations.

## 10. Error taxonomy and observability
Define actionable categories rather than generic failure:
- invalid configuration;
- missing dependency;
- recoverable runtime condition;
- persistence/version incompatibility;
- corrupted input;
- resource/scale guardrail exceeded;
- programmer invariant violation.

Provide logs/metrics/debug views appropriate to diagnose them.

## 11. Integration review
Periodically examine:
- dependency fan-out;
- duplicate abstractions;
- contract churn;
- hidden cross-system state mutation;
- event storms/order coupling;
- save/schema drift;
- resource accumulation;
- tooling/content burden;
- tests that no longer reflect contracts.

A milestone can pass locally while the overall system degrades; integration gates catch that.

## 12. Pragmatic software-design principles
Use SOLID, Clean Architecture, composition, dependency inversion, modularity, state machines, event-driven design, ECS/jobs, and data-driven techniques **where they solve a real constraint**. Prefer the simplest architecture that satisfies current requirements while preserving explicitly required future feasibility.
