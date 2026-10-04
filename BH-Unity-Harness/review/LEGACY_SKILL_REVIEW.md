# Legacy skills and VS Code review — 2026-10-04

All reads at source baseline 0cffc7e090eccb2d0b453c2c2c5a0db4631650c8. Full text read for all thirteen SKILL.md bodies and all thirteen agents/openai.yaml files under BH-Harness-old/.agents/skills/, and the three .vscode files. This extends the 31 complete file reads in LEGACY_SOURCE_REVIEW.md to 60. The original root AGENTS was already fully reviewed; the large narrative remains selectively covered, not fully reread.

| Skill | SKILL.md blob | agents/openai.yaml blob | Legacy implicit |
|---|---|---|---|
| b1-package-preflight | 582811ddfada51a61bb2456c455fdfae66277859 | dab58234e5bc001c00c6f2a02e0ff4c31ac0a5db | true |
| b1-package-compile | 017eb7197bc0f9df6d8117c1e74c4e846818e74e | f8a8ae24bda09f901a3abb6a0e728db4d7d26d6d | false |
| b1-milestone-implement | 02ca2f919f500b6fda3431557ac22e8ceba679a3 | b6bad8f3693d09daef2a0b14a96a5e959fb60670 | false |
| b1-unity-safety | 6ac2927ff46c42f1505785d22116201488dfd6f0 | 9ea371e88dbd82e9c76cd90b2591ebeff94434ab | true |
| b1-middleware-integration | 4c8145f5561c30ae3b7f142456d8c1a414daed46 | 0e6c17275daf9b52da06c69bf0d92bec30eefc4d | true |
| b1-gameplay-experiment | 1c62205b8c54963df63dee9cf187ea852c547faa | c30451737df8c3258d12208d2bc16b5dddd5c5f1 | true |
| b1-unity-validate | b8e4b08d9121c0cb76d6f7761aca7e541352ebc6 | f9f31348a6965a8b94d66bf7611d44b97a024bc5 | true |
| b1-performance-scale | 99c340bce7a783fee069a69bf36e9fe82bfd8e83 | eaca4c7c42ebacbb7ad165f5e1d4577cdb333152 | true |
| b1-state-persistence | 3a433a6fbe020c3c6a2f410c958342650844885c | 50a2ce9c64339a681affb3e21663fc56085a0fe9 | true |
| b1-coop-authority | 5d8bee6952e2505b3ecc3ef9b2a7d1e6f684461f | f76df71d1c93db75f306aae50a21cc53dc55e9a9 | true |
| b1-narrative-contracts | f5a18958a34c1acae064002f913f748f5b7cc648 | 307f3c138cd94a37e6952ed0b348cf9fe10d572f | true |
| b1-evidence-review | 3290c9557bb6f888ffe43fa941ecf813521f552a | 472f55a15988c5029faab76c72a1c02b318b0fe6 | true |
| b1-completion-report | d07b16c6413073da7bba81019f62e1c55d766141 | fa80c1eacbe3c6de02b725b66f13ddb4efd75fb5 | false |

The existing REQUIREMENTS_AND_MIGRATION skill-responsibility map is now supported by full body/metadata reads. Five new BH skills deliberately use explicit-only invocation; native discovery and actual triggering remain a host pilot, not a security boundary. No additional skills or middleware catalogs are installed.

## Justified corrections included in this batch

K12 section 11 adds on-demand semantic detail, reproducible authoring, controlled experiments, performance capture, persistence/co-op/narrative authority, and canonical shared-state delta checks. Sections 1-10 are byte-identical to the previous candidate (prior SHA-256 405e444b81a46f283409ae94d7cf8c769c89eab87dc8b3e5f87cc15ab0ff295b). The new K12 digest is f2a7c65fbfc6b4d5e3fb6c043667ded840ef14eb72bbadc4d75d700a20feed10 and KNOWLEDGE_MANIFEST is updated. No extra knowledge upload or root instruction growth: still fifteen knowledge files and 7713 official instruction characters.

The Breach One overlay now retains nine additional compact, source-located invariants: combat-first, bounded power/progression, route/economy/theater coupling, proof order, historical production envelope, rejected scope, six asset-acceptance gates, participant authority and conditional narrative reconciliation. All remain SOURCE_DERIVED_UNRECONCILED. Camera, revive, bot, friendly fire, exact progression, persistence/consent and future platforms/session features stay open or deferred. Source skill narrative interpretation is explicitly conditional on retrieving the actual adopted narrative ledger; it is not a new whole-narrative review or approval. Core implementation, installed game files and source directories are unchanged.

Six new static tests actually passed using PYTHONPATH=tests python -B -m unittest test_review_amendments -v (Linux/Python 3.13.5, 6 tests, 0 failures/errors/skips, 0.002s). They check schema, non-adoption, retained IDs, exact old K12 prefix, checklist presence and matching manifest digest. These test structure and retention, not model compliance or game behavior. Full suite rerun remains the next execution action; old 127-pass results must not be presented as including these new six tests.

## VS Code settings disposition

| File under BH-Harness-old/.vscode | Blob | Finding/disposition |
|---|---|---|
| extensions.json | ddb6ff85a307649b2e4b11175a6b4fa3ac3b20f9 | Recommends visualstudiotoolsforunity.vstuc; preserve existing user setup, no automatic install. |
| launch.json | da60e25ae2b5a8148bbe8f2c810b85bd395e8f59 | vstuc attach configuration; optional existing debug path, not evidence it works locally. |
| settings.json | f324a476a12909d06c8cdba01c8b66c22b4aebf3 | JSONC-style trailing comma, broad Explorer hiding of metadata/scenes/prefabs/ProjectSettings and a BreachOne-Proto1.slnx binding. Do not copy as universal settings or parse as strict runtime JSON. Inspect actual hidden assets through appropriate tooling; Explorer hiding is not an access boundary. |

These three files contain no actual diagnostics MCP binding. Preserve the documented sonarqube source expectation and discover the installed bridge; do not invent tool names or claim a missing connector configuration was migrated. No SonarQube/VS Code/Unity execution occurred here.

Remaining: original design reference coverage, seven Reference/current upstream notices review, current artifact/delta manifests, full suite evidence and final PR/tree/diff reconciliation. Existing installation runtime, official GPT field and shared schema stay unchanged in this batch.
