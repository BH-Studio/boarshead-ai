# Efficiency implementation publication — first two batches

Functional revision: 84d6976eef0e0fb9ffb0537cbdfad8d36abe5636.
Review baseline: 4ed5b1fccf25cf7f45e1cf933df162f3b79161d2.
This record/evidence batch does not alter the tested implementation.

## Readback observed
The actual GitHub root and candidate tree were read after publication. The installed project-template tree is 21fc13d1f02872fd6530265c3b79467730b95cba, and the contracts tree is 55f65b3f2d5070e930241a318d749b4fb0b191d9. Both match complete recomputed local Git tree identities. PACKAGE_FILES.json is blob 88f1d50ecfabff61a05950117eea4aef59da3635, containing exactly 24 installable files. Runtime blob 136f1b7e7a736e169227849cea953b0531b03833 matches the bytes executed in the focused runs. The shared interface has one owned definition and identical producer/consumer copies; the canonical wire schema is unchanged.

Original directory trees retain their identities: BH-Game-Design-Director 47c94bedc12c6d77149885c7b15879acb34c8f57; BH-Harness-old 62fb863b98357fc6227783cdea861a7aeb61ba47; Reference fdd5f817aeb4a47d40f4a3a275732bc0fa3940f9. Other root entries are unchanged. Existing BH-Unity-Harness/Readme.md remains df10f4364219edd7ae4edcf8652215c868ee9da3.

## Evidence now readable in the repository
review/evidence/efficiency-2 contains AFTER.json, BATCH.json and four original final test logs. These cover 136 distinct cases across four completed modules on identical 32-file source maps, with no failures/errors/skips. The actual reproduction script is review/tools/measure_efficiency_revision.py. Individual repeated-map JSON receipts and earlier attempts remain in the supplemental archive rather than being reconstructed from summaries. That archive is 9,946 bytes, SHA-256 f4698bd4a651959f5b61477e29becd4a8d158bef9d2093caf46e6203229a7e50, and contains 20 files. It is not itself a runtime distribution or a claim of GitHub publication.

## Remaining construction and validation
This is not a complete efficiency closure. The 44 existing package/design/static tests outside the four focused modules still need a run against an exact complete revised candidate. Content-preserving checkpoint-commit continuation and a machine-declared prerequisite graph are not implemented. Strict HEAD reconciliation therefore remains; fail-fast provides explicit sequential staging, not automatic prerequisite scheduling. Stable runner versus mutable task-data separation is a reviewed configuration pattern, not a newly authorized arbitrary-code loader.

Windows/PowerShell, Unity, native Codex, optional MCP/diagnostics, configured design host and actual billed-credit comparisons are NOT_RUN. Human adoption PENDING. Keep PR #1 draft/unmerged and existing live packages unchanged. EFFICIENCY_IMPLEMENTATION.md and BUILD_CHECKPOINT.md are the continuation authority; old full-suite/assembly reports remain pinned historical evidence.
