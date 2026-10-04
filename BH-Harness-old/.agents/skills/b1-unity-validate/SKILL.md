---
name: b1-unity-validate
description: "Run or plan authorized Breach One validation across EditMode, PlayMode, built player and relevant integration gates. Discover real harnesses; never treat missing or zero-test runs as passes."
---

# b1-unity-validate

Package: B1-CODEX-OPS | Version: 0.1.0
Authority: use only within the adopted repository instructions and the current authorized task.

## Entry

Read `docs/AI/VALIDATION_AND_EVIDENCE.md`, the package test plan and repository command registry.
Confirm permission to launch Unity/run tests/build and the actual editor, test-framework and
package versions. Inspect harnesses and side effects; a review-only task may plan but not execute.

## Procedure

1. Map ACs to the cheapest falsifying tests and required final gates. Specify exact fixtures,
   category/filter, expected nonempty discovery and target platform. Use actual runner syntax.
2. Prepare a unique run ID and authorized evidence output location. Record implementation
   snapshot, config/fixtures and environment. Avoid a second Editor process using the same project.
3. Run approved focused checks first, then required integration/regression and representative
   gates at a stable candidate revision. Capture exit status and fresh result/log timestamps.
4. Verify that expected tests ran. Record discovered/executed/passed/failed/skipped/inconclusive
   counts and how the runner defines them. Zero discovered tests, stale XML or absent output is
   not a pass. Distinguish runner crash, compilation failure, assertion failure and blocked setup.
5. Triage with exact test names and first useful project stack/assertion. A failure is only
   "pre-existing" when comparable baseline evidence supports it. Do not delete assertions or
   widen thresholds. Keep raw evidence available and summarize it without dumping giant logs.
6. Check modified scenes/lifecycle in PlayMode and a built player when required; perform genuine
   multi-process scenarios for co-op. Pure unit tests do not prove those integrations.
7. Reassess evidence after every relevant late edit. Record which runs remain valid and which
   need repeating. Leave unavailable human/playtest checks NOT RUN.

## Return

Produce run ledger and AC matrix with exact commands/cwd, revisions, versions, target,
counts, duration if exposed, warnings, artifact references, limits and required next evidence.
Use PASSED/FAILED/SKIPPED/BLOCKED/NOT RUN accurately. Do not close the milestone.
