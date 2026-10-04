# Durable Artifacts, Decision Records, Context Continuity, and Traceability

## Why
Complex projects become brittle when approved decisions exist only in chat history. Custom GPT conversations begin fresh; durable artifacts are the continuity layer.

## Recommended artifacts
### PROJECT_CONTEXT
Stable facts: game pillars, platforms, engine, high-level architecture, terminology, constraints, global non-goals.

### CURRENT_STATE
Concise present-tense truth: current milestone, completed capabilities, blockers/limitations, next planned work.

### <System>_SYSTEM_DESIGN
Approved system intent, behavior, boundaries, contracts, scale/reuse/persistence, validation, risks.

### <System>_RESEARCH
Targeted comparable/evidence brief when research materially influenced design.

### <System>_VALIDATION_PLAN
Design/architecture hypotheses and methods when validation is substantial.

### ADR / decision record
Why a meaningful design/technical choice was made.

### M##_SPEC
Approved bounded milestone scope/acceptance contract.

### M##_WORK_STATE
Temporary resume point for long implementation work.

### M##_COMPLETION_REPORT
What was actually delivered and proven.

## Canon hierarchy default
1. explicit current human decision;
2. accepted ADR/change record;
3. approved system design;
4. approved active milestone spec;
5. current-state/project-context;
6. completion reports;
7. implementation/tests;
8. old chats/brainstorming.

If implementation contradicts approved design, flag it; code does not silently become design canon.

## Decision record template
```markdown
# ADR-### — <Decision>
Status: PROPOSED / ACCEPTED / SUPERSEDED
System:
Date:

## Context
## Decision
## Alternatives considered
## Rationale
## Consequences
## Risks
## Player/design impact
## Data/save/compatibility impact
## Scale/performance impact
## Validation implications
## Supersedes / Superseded by
```

## Change control after approval
Record:
```text
Previous decision:
New decision:
Reason:
Requested by:
Player/design impact:
Architecture impact:
Data/save/migration impact:
Scale/performance impact:
Milestones affected:
Tests invalidated/added:
Docs to update:
Rework/migration:
Human approval:
```

## Traceability
For complex systems use IDs only where useful:
- `REQ-###` requirement;
- `DEC-###` decision;
- `ADR-###` architecture/design record;
- `VAL-###` validation hypothesis;
- `RISK-###` risk;
- `AC-###` acceptance criterion.

A strong chain is:
`REQ → Design Decision/Contract → Milestone AC → Validation/Test → Completion Evidence`.

## Fresh-chat rehydration packet
Prefer:
- PROJECT_CONTEXT;
- CURRENT_STATE;
- approved SYSTEM_DESIGN;
- relevant ADRs;
- active M##_SPEC;
- active M##_WORK_STATE if implementation is mid-flight;
- previous completion report when it is a dependency.

Do not paste entire historical chat transcripts when canonical project artifacts can carry the state more accurately and cheaply.

## Historical integrity
Completion reports and accepted ADRs are historical records. Supersede or append correction; do not silently rewrite what was previously approved/completed.
