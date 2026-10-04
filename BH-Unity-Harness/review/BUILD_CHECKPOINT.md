# BH Unity Harness construction checkpoint

Status: RESUMED — reconciliation and remaining source review in progress. Not adopted.
Repository: BH-Studio/boarshead-ai
Branch: harness/bh-standard-v1-20261004
PR: #1 (must remain draft and unmerged)
Pinned source baseline: 0cffc7e090eccb2d0b453c2c2c5a0db4631650c8
Observed branch head at this resume: dd61db6ebf829baa6c08824bc51e7a828b07584a
Preserved-reference commit: 424698b1a6210638632fd163a32bfa9f889aec00

## Confirmed this resume
- Read this branch's BUILD_CHECKPOINT.md and RECOVERY_DELIVERY.md through GitHub at the observed head.
- Recovered the actual supplied BH_Unity_Harness_v1.0.0_Recovery_Additions.zip: 339472 bytes, SHA-256 be4fab9c97ad9661f4b8dfe06095ae946af2bce1abd6f7e8a766b783efb5fa42; 176 archive entries. No runtime reconstruction.
- Read PACKAGE_FILES.json (22 game-installed entries), PRESERVED_REFERENCES.json (13 exact source blobs), and the delivered verification/continuation records. Finish full source-inventory reading before claiming coverage.
- The branch has intervening commits. Earlier statements that only reference files are published are historical, NOT current inventory evidence. Reconcile every path and hash before writes.

## Evidence retained, not rerun yet
Historical delivered suite: 125 tests in six nonoverlapping partitions, identical tested-source hashes, zero failures/errors/skips, 47.857 seconds combined. Do not apply this result to changed source without checking hashes and rerunning. Windows/PowerShell, Unity/C# build helper, Codex, MCP/diagnostics, configured GPT/Project, real cost comparisons and human adoption remain NOT_RUN.

## Durable work batches
1. Reconcile current branch tree against the actual archive and all manifests; preserve contributor changes, repair only justified omissions. Commit files plus findings.
2. Finish pinned legacy docs/AI policies, templates, baselines, skill and design references identified by SOURCE_INVENTORY; write exact read coverage and requirement dispositions. Commit the review and any justified candidate-only corrections.
3. Review the seven Reference repositories' relevant source and current upstream versions/notices; retain attribution, exclude uncertain redistribution, and record exact adoption decisions. Commit the register and corrections.
4. Run assembled-package checks and actual offline tests, publish evidence, verify resulting tree/manifests and complete diff, update draft PR. Keep platform tests and adoption separate.

## Exact next action
Read SOURCE_INVENTORY.json and VERIFICATION_REPORT.md fully from the supplied archive. Fetch the current candidate subtree and compare it to PACKAGE_FILES.json, PRESERVED_REFERENCES.json, DELIVERY_MANIFEST.json and the archive. Do not replace existing files with archive copies without inspecting their current changes. Continue the recovered implementation; never re-prompt Codex to rebuild it.

## Checkpoint discipline
Commit each completed, coherent work batch with its actual files and evidence before starting the next substantial batch. Refresh this checkpoint with completed items, missing paths, observed results and the exact next action. Use non-force updates and recheck the head. A future session must first read this file, the associated evidence and current branch state; local /mnt/data paths are temporary, not the durable source of truth.

All candidate edits remain under BH-Unity-Harness. Preserve original directories and existing Readme.md. No merge, release, game installation, live GPT edit or human acceptance. Never install this construction checkpoint as a game's task state.
