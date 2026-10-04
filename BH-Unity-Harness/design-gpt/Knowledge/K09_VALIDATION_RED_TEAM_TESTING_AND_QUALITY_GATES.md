# Validation, Red Team, Testing, and Quality Gates Reference

## Three different validity questions
### Design validity
Does the design create the intended player behavior/experience?
Evidence may include playtests, prototypes, UX tests, telemetry, comparable evidence, economy models, expert review, or player studies.

### Architectural validity
Can the design integrate, scale, persist, perform, remain compatible, and support declared reuse?
Evidence may include spikes, benchmarks, schema prototypes, load/save fixtures, conformance tests, representative-scale data, dependency review, and clean-consumer tests.

### Implementation correctness
Did the implementation satisfy the approved milestone?
Evidence includes build/test output, diff/contract inspection, regression, performance/scale results, and player-facing verification.

Passing software tests does not automatically prove design validity.

## Hypothesis format
For meaningful claims:
```text
VAL-###
Claim:
Why it matters:
Method:
Falsification criterion:
Success threshold:
Evidence produced:
Status: UNVALIDATED / PARTIAL / SUPPORTED / FALSIFIED
```

## Red Team procedure
1. State the preferred design and strongest rationale.
2. Temporarily adopt the mandate: **prove this should not be approved**.
3. Search for concrete failure scenarios, not generic "risks."
4. Categorize:
   - CRITICAL — invalidates core design/architecture unless resolved;
   - MAJOR — material risk requiring mitigation/validation;
   - ACCEPTABLE RISK — understood and consciously accepted;
   - UNKNOWN / NEEDS VALIDATION;
   - NO ISSUE FOUND.
5. For serious findings, propose the smallest validation that could resolve uncertainty.
6. Revise candidate or record explicit risk acceptance.

### Red-team targets
- dominant/degenerate strategies;
- positive feedback runaway;
- hidden player information/fairness issues;
- cognitive overload/feedback ambiguity;
- exploit/cheese behavior;
- scale/performance cliffs;
- state explosion or unbounded growth;
- persistence/migration failure;
- deterministic/order coupling;
- cross-system dependency cycle;
- authoring/tooling explosion;
- speculative abstraction;
- untestable requirements;
- milestone scope too large to verify.

## Software validation ladder
Use only stages relevant to the claim, but make closure gates explicit:
1. static/build/sanity;
2. focused unit/property tests;
3. contract/schema/serialization tests;
4. integration/conformance;
5. save/load/migration/backward compatibility;
6. representative-scale/performance;
7. stress/failure/guardrail behavior;
8. affected regression;
9. exploratory/manual/playtest/UX;
10. clean-consumer/package validation where reuse is claimed.

## Representative scale
A scale requirement should be tested while architecture is still changeable. Tiny unit fixtures do not prove large-world architecture.
Always record workload, environment, units, threshold, actual result, and variance if meaningful.

## Evidence matrix
| Acceptance Criterion | Validation Type | Test/Method | Required Result | Actual Evidence | Status |
|---|---|---|---|---|---|

## Codex evidence quality
When Codex returns results distinguish:
- reported claim;
- exact command/test name;
- pass/fail/skipped counts;
- benchmark workload and units;
- warnings/errors;
- missing evidence.

Do not translate "tests pass" into stronger claims than the tests actually cover.

## Closure rules
A milestone should not close with:
- unmet acceptance criteria unless explicitly deferred/approved;
- unexplained contract drift;
- missing required scale/performance evidence;
- unreviewed schema/persistence changes;
- a claimed player-experience validation that was never performed.

## Final system acceptance
After milestones, re-evaluate the system against original requirements and design hypotheses. This catches local success with global failure.
