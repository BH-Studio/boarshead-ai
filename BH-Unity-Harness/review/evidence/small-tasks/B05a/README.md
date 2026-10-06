# B05a actual source and dependency inventory

Input: BH-Studio/boarshead-ai, branch harness/bh-standard-v1-20261004, head d1865991ca624a9c63eaecb1054989059ea02b64.

Exactly three requested test sources were retrieved and byte-reconciled: tests/test_package.py, tests/test_game_agnostic.py and tests/test_review_amendments.py. All three UTF-8 byte encodings matched pinned Git blob SHA, current tree size and recorded SHA-256. SOURCES.json records exact identities; FETCH_METADATA.json projects actual retrieval metadata. RAW.log is actual stdout/stderr captured from the reconciliation helper, and COMMANDS.json records its actual command and shell exit status 0.

Static AST parsing (no test import or execution) found 23/15/6 declared methods, total 44, matching the historical total. An initial conversational manual estimate of 45 was corrected by this actual AST result. SOURCE_FACTS.json contains exact method candidates, imports and source expressions/line numbers for file/tool calls. These are not runtime-discovered cases or test passes. RESULT.json explicitly records zero tests and runtime discovery NOT_RUN.

DEPENDENCIES.json records direct files, manifest-driven rosters, active recursive scan rules and unresolved tool/support dependencies. Its current Git-tree rosters are metadata only, not byte verification. B05b names eight shared support/tool sources as the next bounded task; B05c (seven manifests/direct policy inputs) and B05d (three lesson/reference inputs) are provisional follow-ups to refine after tool/manifest inspection. Remaining manifest-selected and active-scan byte closure must use small explicit child batches. Current imported package checker behavior is unresolved until B05b, so no complete input-closure claim is made.

B05b and later file reconciliation, all tests, B06/B07, native Unity/Windows/Codex, design-host/player checks and billed-credit comparisons were NOT_RUN. No implementation or game defaults changed; source-game names in scan counterexamples remain test data. PR #1 must remain draft and unmerged; full candidate validation and human adoption remain open.

The executed b05a_reconcile.py expects the original b05a-input.json GitHub export and writes b05a-work/. It hashes and parses those three fetched files without importing them. To reproduce, retrieve the exact three sources and current Git-tree metadata at the pinned input head, construct that export and run the recorded command. Do not use unittest discovery until the required byte closure has been reconciled.
