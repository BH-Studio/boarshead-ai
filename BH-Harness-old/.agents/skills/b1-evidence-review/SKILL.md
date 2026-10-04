---
name: b1-evidence-review
description: "Review Breach One Codex evidence or cumulative integration against approved criteria. Read-only by default; report gaps and closure recommendations without accepting the milestone."
---

# b1-evidence-review

Package: B1-CODEX-OPS | Version: 0.1.0
Authority: use only within the adopted repository instructions and the current authorized task.

## Entry

Read governing package/revision, approval scope, relevant original requirements, final diff,
completion report and accessible raw evidence. Load `docs/AI/VALIDATION_AND_EVIDENCE.md`.
A report is a claim until supporting artifacts are examined. In Design Chat without code/raw
outputs, distinguish what can be checked from what remains reported; never imply repository access.

## Ordered review

1. Scope: unexpected/missing files, assets, behavior, dependencies or unrelated cleanup.
2. Contracts: ownership, public/serialized semantics, migration, lifecycle and compatibility.
3. Build/static: actual target and warnings, not just a "build passed" statement.
4. Focused correctness: exact assertions/coverage, discovery counts, skips and failure evidence.
5. Integration/regression: affected consumers and state handoffs, actual process/scene coverage.
6. Performance/scale: equivalent environment/workload, approved thresholds, actual units and limits.
7. Player behavior: actual protocol/observations versus predicted experience or automated proxies.
8. Durable records: truthful completion/work state and separately authorized shared-state changes.

Check evidence freshness against the final revision, commands, outputs and test discovery. Detect
zero-test passes, stale XML, suppressed failures, invented pre-existing regressions and metrics
presented without a baseline. Deduplicate repeated reports of the same underlying test/source.

## Cumulative integration mode

When a foundation contract spreads, shared state/schema changes, drift appears, or system
acceptance approaches, also inspect dependency fan-out, resource accumulation, duplicate owners,
contract churn, authoring burden, regression health and actual second-consumer conformance.
Do not require arbitrary integration ceremonies for a small isolated task. A named candidate
consumer is not a clean-consumer test already passed.

## Return

Give AC/requirement evidence matrix; actionable findings with file/line/test locators and severity;
missing evidence; smallest useful validation for serious unknowns; and one review verdict:
READY TO CLOSE / PASS WITH DEFERRED ITEMS / ITERATION REQUIRED / DESIGN CHANGE REQUIRED / BLOCKED.
Any deferred acceptance criterion requires human disposition. Suggest only the focused unresolved
iteration. Do not edit, approve, archive or close anything unless separately authorized.
