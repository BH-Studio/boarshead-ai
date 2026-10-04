---
name: b1-completion-report
description: "Produce evidence-backed Breach One completion/work records and proposed shared-state deltas at authorized paths. Does not mark human acceptance, approve deferrals or rewrite canon."
---

# b1-completion-report

Package: B1-CODEX-OPS | Version: 0.1.0
Authority: use only within the adopted repository instructions and the current authorized task.

## Inputs

Read the approved package, actual final revision/diff, run ledger and accessible result artifacts,
review findings, version/schema changes and remaining manual checks. Use
`docs/AI/templates/COMPLETION_REPORT.template.md` and the state-delta template as appropriate.
Do not manufacture a completion report for unimplemented work; a blocked report is legitimate.

## Procedure

1. State delivered and undelivered scope, status READY FOR REVIEW or BLOCKED, and implementation
   identity. Separate reported capabilities from directly inspected evidence and manual results.
2. List meaningful files/components/assets and approved contract/version changes. Identify
   deviations, incidental generated changes and omissions explicitly.
3. Map every AC to method, run/artifact/locator, actual result, limitation and status. Include
   commands/cwd/environment, discovered/passed/failed/skipped/inconclusive counts, warnings and
   unavailable metrics. Never infer a count or duration from "all green".
4. Report workload, units, threshold and measured result for scale claims; preserve comparison
   baseline and environment. Leave gameplay/UX claims UNVALIDATED where no player test occurred.
5. Record diagnostics, known defects, accepted versus proposed risks, required manual actions,
   follow-on effects and focused remaining work. Do not relabel skipped tests as passed.
6. Update authorized work-state paths for resumption. Propose `CURRENT_STATE`, decision and roadmap
   deltas with prior/new text, evidence and limits. Only edit shared files if this exact task
   delegates their paths and fields. Keep historical records intact.

## Closure boundary

The implementation agent recommends review readiness. Verification Review recommends a closure
verdict. The human accepts or declines closure and any deferrals. Record the actual human decision
only after it occurs; until then leave closure PENDING and do not mark COMPLETE or delete/archive
the work state. Avoid a documentation worker racing source/tests or another writer in one checkout.

## Output

Return the report path or complete report text, evidence references, authorized docs changed,
proposed shared-record changes and unresolved gates. Keep raw logs retained at approved locations
without pasting them wholesale into chat. A concise summary must not hide missing evidence.
