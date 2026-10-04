# Resume reconciliation — 2026-10-04

## Scope and authoritative evidence
Compared the supplied 176-entry recovery archive (SHA-256 be4fab9c97ad9661f4b8dfe06095ae946af2bce1abd6f7e8a766b783efb5fa42) against GitHub commit f0b602ac8aa4472765dc7f99f8ea0d166600ef70, candidate tree 8dea032f74683f2dfe3db7fd95fa9f7619d8af5c. The immutable source baseline remains 0cffc7e090eccb2d0b453c2c2c5a0db4631650c8. Public connector reads supplied the actual tree entries; local code recomputed Git blob/tree object hashes from the archive and the thirteen exact identities in PRESERVED_REFERENCES.json. SHA identity is a byte-correlation check, not independent attestation.

## Publication finding: the implementation is already present
The archive's root CHANGELOG.md, DELIVERY_AND_CONTINUATION.md, DELIVERY_MANIFEST.json, PACKAGE_FILES.json, PRESERVED_REFERENCES.json and QUICKSTART.md have exact matching Git blob identities. The following entire directories match recursively (design-gpt includes the thirteen preserved source blobs):

| Directory | Exact Git tree SHA |
|---|---|
| contracts | 4dac938d7b7c768dab512773023d40462006c26b |
| design-gpt | 7ebb60e9e086d21c6c2f03f3560568acd827dd6d |
| examples | 42dde97942871fb7c3e19362c1f148c473cc1187 |
| installer | 4db995d7fce4428bcbea1f67508aec33c411cbf3 |
| optional | 374b290338b88eec887d53449f3fb8c945174e79 |
| project-template | 857a71570e56362252f4c1cf681730263e970233 |
| review/evidence (historical runs) | 7390373ee4d240452f2dd656baeef09e82bdf60f |

Every other archive review document matched its observed blob, except the deliberately updated BUILD_CHECKPOINT.md. Additional existing files are Readme.md, review/RECOVERY_ARTIFACTS.json and review/RECOVERY_DELIVERY.md. Readme.md retains original blob df10f4364219edd7ae4edcf8652215c868ee9da3. No archive implementation file is missing. Do not reapply the additions patch or overwrite the contributor changes below.

## Intervening changes retained
Two files differ from the original delivered archive. Both were read through GitHub in full, reproduced in the local test copy and checked against the actual Git blob SHA before tests:

| File | Current blob | Disposition |
|---|---|---|
| tools/assemble_candidate.py | 4d71817e0d313ef87130384dc80331864171b228 | Preserve matches_preserved_blob: accepts exact or CRLF checkout representation, then writes canonical blob bytes. |
| tests/test_package.py | 93cd672ba878db7da76b31628efcc2b55bc4ffc3 | Preserve two added cases: CRLF checkout accepted; substantive reference conflict rejected. |

All other files in tools and tests match the archive. These changes increase the discovered offline suite from 125 to 127. The existing DELIVERY_MANIFEST.json describes the original archive, not these later changes or future review files. Do not interpret its historical hashes as a current full-tree manifest; the current delta is recorded here and must be reconciled in final manifest work.

## Actual fresh execution
Command: python -B tools/run_tests.py --part N --parts 6 --output review/evidence/resume-20261004, N=0..5. Working directory: a temporary recovered BH-Unity-Harness package; no real game. Actual runtime, installer, tests and tools were executed, not rewritten or simulated.

All 127 discovered tests passed across six nonoverlapping completed partitions (22,21,21,21,21,21), zero failures/errors/skips, 32.239 seconds combined. All six source-hash maps were identical; canonical sorted compact-JSON SHA-256 of that map: cd15e870adb03d290edf41a5d6e95b2368bf9f11afd2315450dcd1f6fa998ebf. This is test execution time, not a performance or token-savings benchmark.

The actual full-method reference bytes are present in the repository, verified by exact tree identity, but absent from this temporary local additions test copy. Accordingly the suite exercises its documented PARTIAL_UNASSEMBLED path for package checks. This is not a claim of executing tools/check_package.py on the complete original-reference assembly. Historical 125-pass evidence remains unchanged, and these 127 results are separate.

## Remaining work
Finish pinned source-policy/template/baseline coverage and external source/notices review; make only justified candidate changes, reconcile current artifact manifests, publish fresh evidence, inspect final diff and update the draft PR. Full original-reference local assembly/static execution, Windows/PowerShell, actual Unity/C# compilation, Codex native skill activation, MCP/diagnostics, configured GPT/Project, human playtest and comparative usage measurements are NOT_RUN. No adoption, merge, install or live-GPT update occurred.

Original root tree entries outside BH-Unity-Harness remain identical to the pinned baseline, including BH-Harness-old, BH-Game-Design-Director, Reference, LICENSE and README.md. Recovery prose that says only references were published is superseded by this reconciliation, not evidence of missing code.
