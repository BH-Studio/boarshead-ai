# Validation gates and evidence quality

Package: B1-CODEX-OPS | Version: 0.1.0 | Prepared: 2026-09-08
Status: CANDIDATE workflow; effective only after human adoption.

## Three claims, three evidence needs

Design validity asks whether players exhibit the intended behavior and experience. Architectural
validity asks whether owners/contracts integrate, scale, persist and remain compatible.
Implementation correctness asks whether the approved milestone is implemented. Passing software
tests does not prove enjoyment, accessibility, fairness or the intended A/B result. [B1-K09]

## Risk-selected ladder

| Gate | Typical claim | Required evidence when applicable |
|---|---|---|
| Static/build | Affected code and assemblies compile | Bound command, warnings/errors, target, output and revision |
| Focused correctness | Rules/invariants meet ACs | Discovered tests, test names/filter, counts, assertions and fresh results |
| Contracts/persistence | IDs, schemas and old data retain meaning | Versioned fixtures, round trips/migration/failure evidence |
| PlayMode/integration | Lifecycle, input, AI, physics and scene behavior work together | Actual scene/fixture, installed versions, test result and cleanup/reset |
| Built player | The built target works beyond the Editor | Build profile/backend/platform, launch, runtime smoke and logs |
| Co-op | Named authority and interaction cases work across participants | Separate processes/roles, scenario/network conditions and convergent state evidence |
| Representative/performance | Target budget under stated workload | Hardware/settings, warm-up/capture, units, thresholds, distribution and limits |
| Stress/failure | Guardrails fail/recover as specified | Overload/corruption/interruption scenario and resulting state |
| Regression/integration gate | The cumulative system remains compatible | Named suite/scope, baseline, impacted consumers and missing coverage |
| Human playtest/UX/audio | Player-facing hypothesis is supported | Protocol, participants/segment, observations, accessibility conditions and uncertainty |

Unity documentation distinguishes EditMode, Editor PlayMode and player-platform test execution.
They must not be reported interchangeably. Installed Test Framework version and actual harness
must be inspected before binding command syntax. [EXT-UNITY-TEST]

## Gate planning

Use the smallest falsifying tests during development; run the package's authoritative final
gates at a stable candidate revision. A final suite need not mean every repository test for every
small change. The approved package specifies coverage and rationale. Missing required gates stay
open; no local exemption may be invented to obtain closure. A late fix invalidates relevant prior
evidence, including broad regression if the change could affect it.

Test states: PLANNED / NOT RUN / RUNNING / PASSED / FAILED / SKIPPED / BLOCKED.
Use NOT APPLICABLE only with explicit rationale. Hypothesis states: UNVALIDATED / PARTIAL /
SUPPORTED / FALSIFIED. A planned or skipped test is never evidence that a claim is supported.

## Freshness and completeness

Each run records unique run ID, implementation reference (commit plus dirty-diff fingerprint or
another unambiguous snapshot), exact command/cwd/shell, input revisions, environment, start/end,
exit status, discovered/executed/passed/failed/skipped/inconclusive counts, warnings and artifact
paths. Record how counts are defined when a runner differs. Confirm selected tests were actually
discovered and fresh output was written for this run. Zero tests cannot pass a nonempty gate.
Never fabricate a duration, file path or count that the runner did not expose.

Output files alone are not enough: bind them to the run and code revision. Keep raw logs/XML,
profiler captures, videos and synthetic-save fixtures at approved artifact paths, not automatically
in Git or the main chat. Retain enough evidence for review. Cite small diagnostic excerpts and
make source artifacts available through the authorized handoff. Redact secrets/PII.

## Diagnosis and review

Review scope → contracts → build → focused correctness → integration/regression → scale →
player behavior → durable records. Label reported claims separately from directly examined
outputs. Compare before/after under equivalent conditions before labeling a failure pre-existing
or claiming an improvement. Do not remove assertions, widen thresholds or suppress warnings to
hide failures. Flaky checks need diagnosis, repeat evidence and explicit disposition.

For serious risks state claim, importance, method, falsification, proposed/approved threshold,
evidence and status. Report CRITICAL / MAJOR / ACCEPTABLE RISK / UNKNOWN / NEEDS VALIDATION /
NO ISSUE FOUND accurately; absence of detected defects is not proof of absence.

## Final packet

Map every AC to evidence and remaining gap. Distinguish automated checks, manually observed
behavior and human playtests. Return review readiness, not acceptance. Human-deferred criteria
need an explicit scope/risk/revisit record. Whole-system acceptance compares original requirements
with cumulative evidence, not just the last milestone's test count. [B1-K09; B1-K12]
