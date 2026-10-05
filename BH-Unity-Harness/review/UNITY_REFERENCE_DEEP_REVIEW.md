# Unity Reference deep review — in progress

Requested basis: Reference/Unity in BH-Studio/boarshead-ai.
Pinned source and candidate baseline: 1b62ae6e8e34e996c7f1c5e29dc7e5ae30db2485.
Stored roots: skills-main tree f4cf5bc9f7f41598f82237bd890159745727b481; unity-agent-plugin-main tree e4f8d1f03a9da07c4112147bfd1c607a5534deed.

## Boundary
This is an additional source-grounded review for useful skills and improvements, not whole-catalog adoption, runtime installation or an instruction to repeat the prior efficiency build. Preserve the game-agnostic pipeline, five focused core skills, human gates and cost constraints. Original Reference files and existing candidate implementation remain unchanged. Recommendations and any external checks must be labeled separately from stored-source facts.

## Completed discovery
- Read both complete immediate skills-directory listings (API truncated=false; larger recursive displays were truncated, so no exhaustive nested-file claim).
- The plugin catalog overlaps the skills catalog but differs in several directory identities; project-auditor-fixes appears only in skills-main. Do not deduplicate by name alone.
- Read prior EXTERNAL_UNITY_REVIEW.md: its full content review covered a few files, not the whole catalog.
- Full new reads: skills-main/skills/generate-editor-search-query/SKILL.md (24626f518681b056cbb2a35e958e03de36e2754c), skills-main/skills/project-auditor-fixes/SKILL.md (24cd6b6c2381470320260e7bde95cd0ef6b4b4b4).
- unity-cli/SKILL.md opening read is partial due to response truncation; no full-read claim.

## Initial findings, not adopted
Bounded semantic Editor search could reduce broad repository scans. Project Auditor adds Unity-specific issue categories and explicit asynchronous terminal states, but its repeated polling, automatic package-install/repair suggestions and commit cadence must not become the BH policy. An interrupted audit needs explicit incomplete evidence, not an automatic success or indefinite restart loop.

## Exact continuation
Read the highest-value Unity skill bodies and their necessary references: CLI integration/play verification, Editor search, package management, UI selection, collision/navigation, audio/text performance and pipeline-specific validation. Compare actual candidate consumer/verification interfaces, inspect differing duplicate catalog variants and license/security guidance. Produce an explicit adopt/adapt/optional/exclude matrix with exact read scope, implementation targets and negative acceptance tests. Commit completed source/review batches. Do not execute vendor scripts, change live projects, install catalogs or assume advertised commands exist locally.

Prior efficiency remediation and its remaining full-package tests remain open per BUILD_CHECKPOINT.md; this source review does not close them. Unity/Windows/native-Codex/configured-GPT execution and billed-credit savings are NOT_RUN.
