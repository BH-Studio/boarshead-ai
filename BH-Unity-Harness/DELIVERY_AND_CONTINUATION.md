# Recovered delivery and exact continuation

## Status
This is an actual **recovered local candidate additions package**, not an empty skeleton and not a claim that the original assignment is fully finished. It includes the implemented runtime/installer, five skills, schemas, revised design instructions/K12, operating guides, manifests, 125 passing offline tests and actual synthetic round-trip records.

Normal file-level GitHub publication of these additions is **not complete**. The existing branch `harness/bh-standard-v1-20261004` in `BH-Studio/boarshead-ai` contains the thirteen preserved source references and construction/delivery records, not the full executable candidate. The original source baseline is `0cffc7e090eccb2d0b453c2c2c5a0db4631650c8`; the preserved-reference commit is `424698b1a6210638632fd163a32bfa9f889aec00`. This package does not authorize merging, live GPT updates, real-game installation or acceptance.

Two construction deliverables still need completion: (1) ordinary readable file-level publication and readback/diff review; (2) the remaining exhaustive nested legacy/reference review and current upstream/license comparison recorded in SOURCE_INVENTORY and EXTERNAL_SOURCES. Live Windows/Unity/Codex/design-host validation is a separate unperformed adoption gate, not a substitute for those construction items.

## Assemble the complete candidate without spending Codex coding tokens
Extract this ZIP to a separate non-game folder. From inside its BH-Unity-Harness directory, using a local clone of boarshead-ai that contains the pinned source objects:

```powershell
py -3 tools/assemble_candidate.py --clone 'C:\Repos\boarshead-ai' --output 'C:\Review\BH-Unity-Harness-v1-candidate'
Set-Location 'C:\Review\BH-Unity-Harness-v1-candidate'
py -3 tools/check_package.py
py -3 -m unittest discover -s tests -v
```

The output directory must not already exist and must not be inside the clone or additions directory. The assembler copies the real additions plus exactly thirteen preserved Git blobs; it performs no network fetch, source-repository edits, commits or installation. A shallow clone missing the blobs must first obtain the stated baseline using your normal authorized Git workflow. Never use a missing-knowledge workaround that invents its contents.

The game-installable template is already wholly contained in the additions. The full design GPT needs the thirteen preserved references; do not upload the additions alone as a supposedly complete knowledge set. Inspect PACKAGE_FILES.json and the knowledge manifest before adoption. Do not copy the synthetic example state/approvals into an actual game.

## Applying the additions patch to an isolated authoring branch
The companion patch contains additions under BH-Unity-Harness only and excludes the construction checkpoint/delivery record already published by this recovery. It does not modify the original Readme.md or original source directories. In a separate clean authoring checkout, inspect `git status`, the target branch/head and `git apply --stat <patch>`, then `git apply --check <patch>`. Only after reviewing conflicts, apply with `git apply <patch>`. This stages/commits/pushes nothing. Reconcile any occupied candidate paths instead of forcing overwrite. Run package validation on the combined candidate, inspect every changed path, then use normal authorized Git/GitKraken publishing. Do not install it into a game during publication.

## Exact continuation prompt for this ChatGPT/GitHub construction task

> Continue the existing BH Unity Harness 1.0.0 candidate in BH-Studio/boarshead-ai, branch harness/bh-standard-v1-20261004. Read the current review/BUILD_CHECKPOINT.md and RECOVERY_DELIVERY.md through GitHub, then read this actual additions package, PACKAGE_FILES.json, PRESERVED_REFERENCES.json, SOURCE_INVENTORY.json and VERIFICATION_REPORT.md. Recover the supplied implementation; do not rewrite or re-prompt Codex to rebuild it. The final offline suite recorded here passed125 tests in six partitions on identical tested sources; Windows/Unity/Codex/configured-GPT tests are NOT_RUN. Check current branch head and existing files before writes. Complete the remaining source coverage listed in the inventory, specifically legacy Docs/AI policies/templates/baselines and the unevaluated Reference repositories/current notices, and make only justified candidate-scope changes. Publish the actual missing readable files under BH-Unity-Harness via supported authorized GitHub writes; preserve original directories and existing Readme.md, never force-push, and keep the PR draft. Verify the resulting tree against all artifact manifests, inspect the complete diff, and report actual commit/PR IDs. Separate published/local files, tests, integration and human adoption. Do not claim work is complete merely because this checkpoint or a ZIP exists.

For the next **local integration** task and paired **design-method pilot**, use the ready-to-run prompts in review/LOCAL_INTEGRATION_TEST.md. Those prompts test the existing candidate; they do not ask Codex to design a new harness or spend tokens reimplementing it.
