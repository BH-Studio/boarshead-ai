# Validation plan — <actual milestone/revision>

Status: TEMPLATE — NOT AUTHORIZED; all runs initially NOT RUN
Governing approval/package: <actual>
Implementation snapshot to test: <actual commit plus dirty-diff identity>

## Claims and coverage

| AC/VAL | Claim type: design/architecture/correctness | Method | Falsification/pass rule | Approved threshold | Required environment | Gate |
|---|---|---|---|---|---|---|
| <actual> | <actual> | <actual> | <precise> | <units/source> | <actual> | <blocking/approved deferred> |

## Commands and prerequisites

For each command: ID, inspected script/executable revision, exact arguments, cwd, shell/OS,
Unity/test-framework/packages, filters/expected discovery, input fixtures, authorized output root,
side effects, process-lock constraints, required permissions, timeout/cancellation and cleanup.
Unbound commands block their gates; never invent a guaranteed Unity CLI line from memory.

## Validation tiers

Specify relevant build/static, focused, contracts/schema, PlayMode, built-player, integration,
co-op, persistence/migration, scale/stress, affected regression and clean-consumer checks. Each
omitted tier needs a reason; each required tier needs a runnable binding or an explicit capability gap.

## Workloads and performance

Record nominal/target/stress/guardrail scenarios, units, hardware/settings, version, capture method,
warm-up, duration/repetitions, distribution/variance and comparison baseline. Separate Editor from
player results and automatic correctness from human perception. Identify instrumentation overhead.

## Manual and player protocols

For each check: setup/entry/reset, participant role/input/segment, actions, expected feedback,
observation method, failure/falsification, evidence capture, accessibility conditions and owner.
Identify informed/repeat participants and test-order effects. No invented percentages or consensus.

## Run ledger

| Run ID | Revision/config/fixture | Command/cwd/environment | Start/end/exit | Discovered/executed/pass/fail/skip/inconclusive | Artifact/freshness | Result/limit |
|---|---|---|---|---|---|---|
| <actual after execution> | <actual> | <actual> | <actual> | <runner counts> | <path/locator> | NOT RUN until observed |

## Evidence rules and revalidation

Verify fresh outputs and nonempty expected discovery; retain original artifacts at approved paths.
Keep failures/skips and define runner counts. Use a comparable baseline to claim pre-existing
failure or improvement. Name changes that invalidate results and rerun affected gates after edits.
Retain sanitized logs/XML/captures and specify retention; do not embed raw secrets or giant logs.

## Final disposition

Map each AC to actual evidence, remaining gap and status. Unexecuted gates remain NOT RUN/BLOCKED.
Only the human may accept deferrals or closure. Review can recommend but not approve.
