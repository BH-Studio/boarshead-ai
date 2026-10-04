# Verification — game-agnostic candidate 1.0.0

Tested functional commit: `72bf50263b39f9ccd236fb54ecae341c97f80125`. Readable evidence published at `78f0c7527b884853a088d8c9a46e5e4813c0e054`. This report records actual offline execution, not live-host validation or human adoption.

## Current observed result
**148 tests passed**, six complete nonoverlapping partitions on identical 175-file source maps; zero failures, errors or skips. Combined recorded duration: **33.271 seconds**. Counts: 25, 25, 25, 25, 24, 24. Environment: Linux 6.18.44 x86_64/glibc 2.41; Python 3.13.5. No Codex token or game-performance benchmark is inferred.

The actual runner was invoked as `python tools/run_tests.py --part N --parts 6 --output review/evidence/game-agnostic-suite-2` for N=0…5, using absolute script/output paths in the execution environment. The script resolves its own package root. `evidence/game-agnostic-publication/PARTITIONS.json` records timestamps, counts and environment. `RESULTS.md` contains the exact concatenated raw logs, including all 148 case identities/outcomes. `SUMMARY.json` binds the tested functional tree identities and input-map digest. Individual original JSON receipts with repeated full source maps and earlier red/green logs are in the supplemental `RAW_EVIDENCE.tar.gz` download; that binary archive is not claimed committed as normal repository files.

Input-map SHA-256: `cda944d1afc0f0ae454eb6debcf6dde1df69d98606288b0220feee8b216ef381`.
Supplemental archive SHA-256: `e2e8dab87371a81c0d0654d3659bd9a1053a8158b9d86e0f3d0fe0c3088f346b`.

## Full package and assembly
Strict `tools/check_package.py`: **PASS_STATIC_PACKAGE, 85 checks**, zero problems or missing preserved files; 22 game-installable files, 15 knowledge selections, five explicit skills, 7,798 instruction characters and 202 characters of headroom.

The actual offline assembler was executed against an isolated local Git object store populated with all thirteen exact connector-read original blobs, into a new non-game output directory. Both assembly and strict validation exited 0; all copied bytes matched; all original identities matched. See `evidence/game-agnostic-publication/ASSEMBLY.json` for actual commands, paths, timestamp and results. This is not a real game checkout or a Windows test. The older PARTIAL_UNASSEMBLED limitation is resolved for this candidate.

## Newly tested corrections
Fifteen new automated cases cover source-name leakage in active content, two contrasting synthetic profiles, unconfigured real-project defaults, original-reference isolation, fifteen retained generic lessons, blocked unreconciled examples, cross-project invariant rejection, safe review-only assembly, Markdown input hashing, generic unreviewed-skill detection, preserved explicitly reviewed extras, malformed registry rejection and missing non-preserved knowledge rejection. Six existing source-retention cases were generalized without losing their responsibilities. Other runtime, installer, process, freshness, approval and parsing tests remain in the suite.

Three preflight tests failed against the earlier game-prefix-specific implementation before its narrow correction; four focused cases then passed. A missing-knowledge negative exposed an incorrect static PASS and then passed after the validator fix. An earlier 148-case suite passed before a duplicate evaluation label was corrected; the final suite above was rerun after that correction. Earlier attempts remain evidence, not erased or combined into the final total.

## Historical evidence and live boundary
The original 125-case report is preserved at `evidence/recovery-stage-VERIFICATION_REPORT.md`; historical 125/127/133 results and receipts are not relabeled as the new candidate. The archived synthetic round trips remain unchanged historical snapshots. Current tests exercise real fixture subprocesses and actual runtime/installer code, including a passing automatic result with human acceptance pending, behavior contrary to approved expectations, and invalidation after tested inputs change.

Windows/PowerShell, actual Unity Editor/PlayMode/build/C# helper, VS Code/Codex discovery, MCP/diagnostics, configured design GPT/Project, player validation, comparative usage and independent external review: **NOT_RUN**. Human adoption: **PENDING**. Static name scanning is bounded lexical evidence, not proof of semantic neutrality or model obedience. Documentation consolidation after the functional commit does not silently become part of that earlier tested source map; current manifests and subsequent static readback identify those documentation-only changes.
