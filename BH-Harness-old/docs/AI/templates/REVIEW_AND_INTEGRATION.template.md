# Verification / integration review — <actual ID/revision>

Status: TEMPLATE — NOT EXECUTED
Mode: focused milestone / cumulative integration / final system acceptance
Reviewer lens/owner: <actual>; human acceptance authority unchanged
Inputs: <approved source revisions, diff/snapshot, reports and raw evidence actually available>

## Inspection limits

State what was directly inspected, reported only, inaccessible or not run. Name duplicate reports
of the same evidence. Do not invent independent agents or corroboration.

## Ordered findings

Review scope → contract → build/static → focused correctness → integration/regression → scale →
player behavior → durable records. For each finding: severity, exact file/line/test or source,
claim affected, concrete counterexample, confidence and smallest useful resolving validation.

## Acceptance matrix

| Requirement/AC | Actual evidence and revision | Supported claim | Unsupported portion | Required correction/evidence |
|---|---|---|---|---|
| <actual> | <actual> | <bounded> | <actual> | <actual> |

## Cumulative integration (when applicable)

Milestones included; dependency fan-out and cycles; duplicate ownership/abstractions; API/schema
stability; save/migration; resource accumulation; process/scene/network regressions; authoring
burden; suite health; actual clean-consumer evidence; debt threatening next work. Compare with
original requirements and hypotheses, not only the final local milestone.

## Verdict and next bounded action

Select READY TO CLOSE / PASS WITH DEFERRED ITEMS / ITERATION REQUIRED / DESIGN CHANGE REQUIRED /
BLOCKED based on evidence. Record unmet criteria and whether their deferral is actually approved.
Give a focused iteration or missing-evidence request. Human closure/acceptance remains PENDING
until explicitly recorded; no self-approval or source edits under this review.
