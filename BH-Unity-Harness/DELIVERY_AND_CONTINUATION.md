# Current delivery and continuation

The existing branch `harness/bh-standard-v1-20261004` in `BH-Studio/boarshead-ai` now contains the actual **game-agnostic** BH Unity Harness 1.0.0 candidate, paired design method 3.1.0 and interface 1.0.0. The functional revision is `72bf50263b39f9ccd236fb54ecae341c97f80125`; readable 148-case test and full-reference assembly evidence was published in `78f0c7527b884853a088d8c9a46e5e4813c0e054`.

## Use the current files, not the historical additions patch
Read review/BUILD_CHECKPOINT.md, CURRENT_REVIEW.md, CURRENT_ARTIFACT_STATE.json and VERIFICATION_REPORT.md, then inspect the current branch head. All required code and reference files are published; do not rebuild the harness or reapply the old additions ZIP/patch. DELIVERY_MANIFEST.json and RECOVERY_DELIVERY.md are immutable historical recovery receipts, not current distribution manifests. PACKAGE_FILES.json is the current 22-file game-installation manifest; design-gpt/KNOWLEDGE_MANIFEST.json selects the current 15 references; PRESERVED_REFERENCES.json identifies 13 exact originals, including one review-only lesson source.

Only project-template and the reviewed installer feed a game installation. Only the official Instructions file and the exact knowledge selection feed the design host. Do not copy the entire repository, authoring review, historical examples, source games or synthetic approvals into a game or live GPT. The old real-game overlay is removed; the current examples/profiles demonstrate synthetic discrete/continuous state contracts only.

## Optional offline assembly
A full branch checkout already contains every required reference. When assembling a separate review copy from the candidate and available Git objects, run from BH-Unity-Harness:

```powershell
py -3 tools/assemble_candidate.py --clone 'C:\Repos\boarshead-ai' --output 'C:\Review\BH-Unity-Harness-v1-candidate'
Set-Location 'C:\Review\BH-Unity-Harness-v1-candidate'
py -3 tools/check_package.py
py -3 -m unittest discover -s tests -v
```

The output must be new and outside the clone/candidate source. The assembler fetches no network data and modifies neither the clone nor a game. The original-object assembly and strict validation passed on Linux; Windows execution still needs the pilot. Do not lower missing-file or approval checks to complete a setup.

## Continuation after an interrupted authoring session
Read the current checkpoint and artifact-state record through GitHub, then compare actual branch contents before writing. Preserve contributor changes, use non-force updates, and commit each coherent new batch with actual results and the exact next action. Completed source review and runtime recovery must not restart just because older documents list historical gaps. Reopen only a concrete observed defect or changed requirement.

The next operational step is the separate controlled pilot in review/LOCAL_INTEGRATION_TEST.md, including its exact Codex prompt and paired design-host prompt. This is not permission to install into a live game, edit the live GPT, merge or release. Preview first; human approval precedes application. Windows/Unity/Codex/MCP/diagnostics/configured-GPT behavior and measured usage remain NOT_RUN until observed.
