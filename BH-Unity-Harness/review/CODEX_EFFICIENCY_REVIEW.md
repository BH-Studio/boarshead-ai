# Codex efficiency review — in progress

Review baseline: `b002e3cc0b2134868c36ea93dadc83aaa7333739`.
Scope: the game-installed Codex consumer, its handoff/return interface, and recurring operating cost. This is a requested review, not authorization to activate a new runtime. No installed/runtime/design behavior is being changed during this audit. Preserve the game-agnostic boundary and draft PR #1.

## Source inspection completed
Read the current construction checkpoint, project-template/AGENTS.md, all five core SKILL.md files, the operating guide, and the runtime's snapshot, approval, planning, verification, receipt audit, recovery, return and CLI dispatch implementations through GitHub. Runtime blob: `5dff7bef67a6ee750918e190ce635ac1cddf2857` (73,100 bytes). The local recovered archive runtime was reconciled against the connector content and its resulting Git blob matches exactly; it is not a rewritten implementation.

## Preliminary findings to reproduce and rank
- `verification()` always executes every check at or below the requested profile; existing valid evidence is consulted after execution, not used to avoid redundant execution.
- Default empty `dependency_paths` ties each check to all nonvolatile project inputs. `scope()` also requires the original HEAD, and approval requires the full original input snapshot. Examine unrelated-edit and content-preserving-commit rework.
- `snapshot()` runs repeatedly at lifecycle boundaries and after every selected check, including manual checks. Path validation enumerates parent-directory entries for each path; investigate dense-directory cost without weakening path safety.
- `audit_results()` traverses every retained run and reparses/hash-checks prior passing artifacts during status/resume/return, not only the current relevant evidence.
- Approved plan/receipt/RETURN JSON records embed the complete input path/hash map, although stdout summaries are compact. Assess the model-reading burden of the instructed plan/return reads rather than falsely claiming asset bytes are automatically sent to a model.
- Recovery defaults allow one recovery cycle; examine whether ordinary failed verification prematurely consumes that budget even before three-failure thresholds.

## Exact next action
Read the shared interface, current configuration/budgets and remaining runtime range boundaries. Run small disposable synthetic probes against the exact runtime blob, distinguishing actual call/output-size counts from billed-credit estimates. Record all probes and limitations. Finish a ranked report with concrete changes and preserved safeguards; do not rebuild the runtime or alter approval semantics during this review.

Current official pricing/skills guidance is being checked separately to explain consumption mechanics, not to estimate this user's remaining allowance. Local CPU/I/O work alone is not a model token charge. Live Codex credit measurements, Windows/Unity integration and before/after savings remain NOT_RUN.
