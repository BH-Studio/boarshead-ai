# Actual verification — recovered candidate 1.0.0

Executed 2026-10-04 in Linux, Python 3.13.5. The final suite is **125 tests passed, zero failures, zero errors, zero skips**, completed as six deterministic nonoverlapping partitions of the same discovered suite. Source-hash maps are identical across all six runs. Total reported test-run time is **47.857 seconds**, not a benchmark of Codex or Unity.

Commands: `python -B tools/run_tests.py --part N --parts 6 --output review/evidence/final-attempt-2`, N=0 through 5. Each JSON file lists exact test IDs, environment and source hashes; each adjacent log preserves actual unittest output. Partition counts: 21, 21, 21, 21, 21, 20. The test suite directly imports and executes the shipped runtime and installer. It does not reimplement their logic in a mock.

## Coverage actually exercised
84 recovered runtime/process tests; 20 actual installer cases; 21 added package/build/release/assembly cases. Coverage includes structured handoff/version/references/approval gates; scope and identity; real process failure, timeout, cancellation and result parsing; zero/missing/wrong/stale evidence; altered dirty inputs; required manual criteria; bounded recovery; safe paths/links; actual install previews, conflicts, idempotence and rollback; complete instruction budget; shared-copy equality; missing full-package refs; actual local-Git blob assembly; filename release scan; build-result failure and fresh-output parsing.

## Actual synthetic round trip
`python -B tools/export_examples.py --output <new directory>` executed actual Python fixture processes. Captured artifacts are in `examples/round-trip`.
- Positive URP-labelled synthetic counter: AC-01 PASS, AC-HUMAN HUMAN_PENDING, phase READY_FOR_HUMAN_REVIEW, human acceptance PENDING.
- Contrary HDRP-labelled synthetic counter: observed value99 vs approved1, AC-01 FAIL, human acceptance PENDING, phase FAILED.
- After an initially passing run, a source edit invalidated AC-01 to NOT_RUN.
- Missing design approval, unsupported version, dropped acceptance ID, missing invariant and manifest mismatch were rejected. Missing knowledge is a structural package failure; actual configured-GPT missing-resource behavior remains NOT_RUN.
These labels exercise project isolation and different observed outcomes, not real render pipelines. No synthetic approval is authority for any actual game.

## Preserved earlier evidence
`recovered-runtime.log` is an interrupted full-suite attempt, not a pass. `tests-part-1-of-4.log` contains the original build-result classification failure. `final-attempt-1/part-0-of-6.log` records three test-expectation errors caused by separate imported BHError class identities; tests were corrected to expect the actual module's exception without changing the rejection behavior. Final-attempt-2 supersedes those runs for the tested source. No historical103/115-pass checkpoint claim is reused.

## Package validation boundary
`tools/check_package.py --allow-unassembled` completed **60 static checks with zero problems**, but returns **PARTIAL_UNASSEMBLED**, exit3, because the local additions intentionally lack thirteen full-method/reference files already preserved on GitHub. A full package check without that flag correctly fails until assembly. The actual offline assembler was tested against a synthetic local Git object, not against a complete clone of the user's repo in this container. Therefore the complete assembled original-reference package check remains NOT_RUN here. Exact required Git blobs are in PRESERVED_REFERENCES.json.

## Integration status
Windows / PowerShell launcher: NOT_RUN. Actual Unity Editor compilation, EditMode, PlayMode, builds and optional BHBuild.cs compilation: NOT_RUN. VS Code/Codex native skill activation, existing SonarQube diagnostics bridge, Unity MCP and configured design-GPT/Project behavior: NOT_RUN. Human playtest, adoption, comparative cost/latency benchmarks and independent review: NOT_RUN. No integration or savings claim is inferred from offline tests.

## Final tested runtime/source hashes
| File | SHA-256 |
|---|---|
| `project-template/Tools/BH/bh.py` | `78f4d1555d8d55de4ec4b8dfe44d3087ea85eaa5c3108194694685ff8cc68be8` |
| `project-template/Tools/BH/check_release_profile.py` | `fcc3516fe87ea4209631cc0777cae5616329488f83d68d9355afd88840200ac5` |
| `installer/install.py` | `bdcc7ec6c11ecda3db415cbf781b84c567fbfe4d91bab1a2945eaaab69e3169f` |
| `contracts/schema.json` | `a781cccd0e652c73c0dff6809e0b3f72e7c292b39cc1ed1e1ae5f587703e438f` |
| `tests/test_runtime.py` | `f6e7ea0a48e65a0c36d7b7a03bfde772781f668ab51b8c4be542b7ed7e15824e` |
| `tests/test_installer.py` | `3caaf6a6abd445a5e797ae37448f08ad75564c36d62354f9e095de1c767431c9` |
| `tests/test_package.py` | `1f370bf166a77cbf2503cd67ab0c89e952d5d6ebe1f4d73025e4b7c747f6ab71` |
| `tests/support.py` | `87e06af520085c00dd64ee67f4ae2394f2ead92bf2c68520fcaeeaab65d2dd90` |
| `tests/fixture_driver.py` | `b14bbf022221bfea4100711bbbeb4b8a13ac591938400b3315f138571a0888d6` |

Documentation and exported evidence were finalized after execution. They do not change the tested runtime, installer, schema, fixtures or test code. Manifest/source tests validate the named scope, not every English claim in every guide. See ASSURANCE.md for remaining source-review and publication gaps.
