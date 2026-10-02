# Milestones, Implementation Package Compiler, Codex Handoff, and Completion

## 1. Milestone design principles
After system approval, decompose into steps that leave a **coherent, reviewable frontier**.
Prefer:
- risk-first proof before dependent volume;
- contract-first boundaries for widely consumed systems;
- thin vertical slices when player/integration behavior must be proven;
- independent acceptance criteria;
- no giant batch whose failure source cannot be isolated;
- no micro-step with no durable/testable outcome.

## 2. Milestone spec template
```markdown
# M## — <Milestone Name>
Status: DRAFT / QUESTION GATE / READY FOR APPROVAL / APPROVED / IN PROGRESS / READY FOR REVIEW / COMPLETE
Parent system:
Dependencies:

## Purpose
## Why now / risk retired
## In scope
## Out of scope
## Locked decisions / contracts
## Required implementation behavior
## Data/schema/persistence impact
## Integration points
## Scale/performance target
## Reuse/extension impact
## Failure/recovery behavior
## Deliverables
## Acceptance criteria
- AC-001 ...
## Validation matrix
## Documentation/state updates
## Definition of done
## Deferred items
```

## 3. Milestone question gate
Before final approval, inspect unresolved behavior, contracts, compatibility, scale, tests, and scope.
Classify `BLOCKING / DESIGN-SHAPING / TUNING / DEFERRED`.
Do not re-ask settled system decisions.

## 4. Implementation Package Compiler
After human milestone approval, prompt generation becomes a **translation/compilation step**, not a design step.

Inputs:
- approved system design;
- approved milestone spec;
- relevant ADRs/contracts/schema;
- current state;
- repository instructions/AGENTS references;
- validation requirements.

Allowed:
- make instructions clearer;
- order implementation work;
- reference authoritative repo paths;
- turn acceptance criteria into a test checklist;
- identify an actual conflict.

Not allowed:
- change approved player behavior;
- alter architecture/contracts/schema;
- expand scope;
- weaken scale/performance targets;
- invent acceptance criteria that contradict design;
- silently resolve a design conflict.

If inputs conflict, stop and escalate.

## 5. Codex prompt template
```markdown
# Codex Implementation Request — M## <Name>

You are implementing an APPROVED milestone in an existing project.

## Authority / read first
1. Read applicable repository instructions / AGENTS.md, including nested instructions.
2. Read approved milestone spec: <path>
3. Read approved system design/current state/relevant ADRs/contracts: <paths>
4. Inspect existing implementation and tests before editing.
5. Treat approved scope and locked decisions as authoritative.

## Objective
<one precise result>

## In scope
...

## Out of scope
...

## Locked decisions / non-negotiables
...

## Architecture/contracts
- ownership/boundaries:
- APIs/events:
- data/schema/persistence:
- compatibility/migration:
- scale/performance:
- reuse/extension:

If implementation requires a design-level change to these, STOP and report the conflict/options rather than silently redesigning.

## Implementation guidance
<ordered phases; smallest coherent changes; preserve behavior outside scope>

## Acceptance criteria
- AC-...

## Required validation
1. build/static/sanity:
2. focused tests:
3. contract/schema/serialization:
4. integration/conformance:
5. regression:
6. performance/scale/stress:
7. manual/playtest/other:

Do not claim a gate passed without evidence.

## Documentation/state updates
...

## Completion response
Return:
1. implementation summary;
2. files changed;
3. acceptance-criteria mapping;
4. exact tests/commands and pass/fail/skipped results;
5. performance/scale workload + actual result;
6. warnings/errors;
7. deviations/conflicts;
8. unresolved risks/limitations;
9. docs/state updated;
10. recommended status: READY FOR REVIEW or BLOCKED.
```

## 6. Focused iteration template
```markdown
# Codex Iteration — M## <Name>
Milestone remains OPEN.

## Previous evidence / failure
## Unresolved acceptance criteria
## Required correction
## Locked constraints unchanged
## Explicitly out of scope
## Validation required to prove correction
## Required completion evidence
```

Do not regenerate unrelated original scope unless necessary.

## 7. Codex result review order
1. **Scope diff** — unexpected/missing/out-of-scope files or behavior.
2. **Contract review** — approved API/schema/persistence/behavior preserved.
3. **Build/static** — errors/warnings/analyzers.
4. **Focused correctness** — unit/property/contract tests.
5. **Integration/conformance/regression**.
6. **Performance/scale/stress** — compare workload and thresholds.
7. **Design behavior** — actual player/system validation where applicable.
8. **Durable state** — docs/current state/completion evidence.

Verdict vocabulary:
- READY TO CLOSE
- PASS WITH DEFERRED ITEMS
- ITERATION REQUIRED
- DESIGN CHANGE REQUIRED
- BLOCKED

Human decides closure.

## 8. Completion report template
```markdown
# M## — Completion Report
Status: READY FOR REVIEW / COMPLETE
Implementation reference:

## Scope delivered
## Files/components changed
## Acceptance criteria
| Criterion | Status | Evidence |
|---|---|---|

## Validation
### Build/static
### Focused
### Contracts/schema/persistence
### Integration/conformance
### Regression
### Performance/scale/stress
### Playtest/UX/telemetry

## Review findings
## Deviations
## Known limitations
## Decisions/ADRs created
## Documentation updated
## Deferred work
## Impact on next milestone
## Closure decision
```

## 9. Integration Gate record
For long systems periodically record:
- milestones included;
- architecture/dependency drift;
- API/schema stability;
- accumulated resource results;
- save/migration compatibility;
- regression status;
- duplication/technical debt;
- reuse/clean-consumer evidence;
- authoring/tooling burden;
- decisions/corrections before the next milestone group.
