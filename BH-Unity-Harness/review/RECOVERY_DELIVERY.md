# Recovery delivery record — 2026-10-04

This branch is a preserved-reference and construction-checkpoint publication, **not the full installed/executable candidate**. The actual newly authored implementation is supplied as the recovery response's downloadable additions archive and patch. Do not mistake the existence of this record for code publication.

## Actual delivery files

- BH_Unity_Harness_v1.0.0_Recovery_Additions.zip — 339472 bytes; SHA-256 `be4fab9c97ad9661f4b8dfe06095ae946af2bce1abd6f7e8a766b783efb5fa42`.
- BH_Unity_Harness_v1.0.0_Recovery_Additions.patch — 1050531 bytes; SHA-256 `bbe6f1d9c8eb97903eeda311d17e31e180c256b9e03ca364ef4d629a7c759653`.
- BH_Unity_Harness_v1.0.0_Delivery_Manifest.json — external archive/patch metadata; the ZIP also contains DELIVERY_MANIFEST.json with file-level hashes.

The ZIP contains176 actual files, including complete game-installable consumer code, installer, five focused skills, shared schemas, revised official GPT instructions/K12, guides, assurance/coverage maps,125 passing offline tests, raw logs and synthetic round-trip examples. It intentionally excludes thirteen source references already preserved at commit424698b1a6210638632fd163a32bfa9f889aec00; the exact missing Git blobs are listed in PRESERVED_REFERENCES.json. The original source baseline is0cffc7e090eccb2d0b453c2c2c5a0db4631650c8.

The offline tools/assemble_candidate.py combines additions with those exact objects from a local clone into a new non-game directory. It performs no network fetch, source edits, commits or installation. tools/check_package.py rejects a missing full knowledge package; --allow-unassembled reports PARTIAL_UNASSEMBLED rather than PASS. The additions patch contains new files only under BH-Unity-Harness and excludes this delivery record and the already-published construction checkpoint. Use git apply --check first in a separate authoring checkout; do not force conflicts. Neither operation requires Codex to reimplement the harness.

## Evidence and boundaries

125 actual offline tests passed across six nonoverlapping completed partitions with identical source hashes (47.857seconds combined; zero failures/errors/skips). The original interrupted/failed attempts are retained. Actual synthetic subprocess results leave human acceptance PENDING after automatic success, reject behavior contrary to design, and invalidate changed-source evidence. This is not real Unity or design-host evidence.

Windows/PowerShell, Unity and optional C# build-producer compilation, Codex native skill activation, MCP/diagnostics bridges, configured design GPT/Project, human playtest, cost benchmarks and adoption are NOT_RUN. The local candidate's complete source/upstream comparison and ordinary file-level GitHub publication still need completion. See SOURCE_INVENTORY.json, EXTERNAL_SOURCES.md, ASSURANCE.md and DELIVERY_AND_CONTINUATION.md inside the archive for specific remaining items and the exact continuation prompt.

Keep any PR draft. No merge, live GPT change, game installation or acceptance is authorized by this delivery. Original BH-Game-Design-Director, BH-Harness-old, Reference and existing BH-Unity-Harness/Readme.md remain unchanged. Continue from the actual supplied implementation, not a reconstruction based solely on this prose.
