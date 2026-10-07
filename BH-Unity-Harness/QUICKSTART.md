# BH Unity Harness 1.0.0 candidate — start here

The paired deliverables are `design-gpt` (BH Game Systems Design Team v3 method 3.1.0 candidate), `contracts` (interface 1.0.0), and `project-template` plus `installer` (game-side harness). This is a candidate, not approval to merge, install into a game, replace a live GPT or accept a design.

The standard is game agnostic and Unity-first. It supplies no game design, genre, narrative, player count, middleware, render pipeline or numerical resource budget. All such facts come from the current approved project. Current examples are visibly synthetic; historical sources are review references only.

## Review without changing the current pipeline
Read `review/VERIFICATION_REPORT.md`, `review/ASSURANCE.md`, `review/REQUIREMENTS_AND_MIGRATION.md` and `design-gpt/REVIEW_AND_SETUP.md`. The original `BH-Harness-old`, `BH-Game-Design-Director`, Reference content and preexisting `BH-Unity-Harness/Readme.md` are preserved. Only candidate files belong in this branch's diff.

The complete current branch includes every required file. Thirteen exact original references are retained, twelve within the design/evaluation package and one under review/reference-only. The deployed K11 is generic. Use the current branch rather than reapplying the superseded recovery patch. A download explicitly named “Additions” is not a standalone full-GPT archive: assemble it with the exact preserved Git blobs using `tools/assemble_candidate.py` and a local clone. The resulting complete directory is the artifact to review or package, not the entire source repository. Never upload an incomplete knowledge package and assume missing resources will be inferred.

## Pilot the design method separately
Current OpenAI documentation (checked 2026-10-04) says personal plans cannot create new custom GPTs, while eligible owners can still edit existing ones. Do not replace your live GPT just to test this candidate. Use a separate ordinary ChatGPT Project for the pilot, or a separate already-existing test GPT where available and explicitly approved. `design-gpt/REVIEW_AND_SETUP.md` specifies the exact Instructions file, fifteen knowledge files and Project adaptation. Live-host behavior remains NOT_RUN until you perform that pilot. New paid accounts are not required.

## Validate and preview a game pilot
In a separate clone/worktree containing the complete candidate:
```powershell
py -3 tools/check_package.py
py -3 -m unittest discover -s tests -v
py -3 tools/export_examples.py --output '<new empty disposable directory>'
py -3 installer/install.py preview --target 'C:\Games\Your Existing Game'
```
The example exporter uses visibly synthetic temporary Git projects and real local subprocess output; it is not a Unity test. Do not copy synthetic approvals or state into a game. Review a game preview and source migration map before allowing installation. Existing AGENTS.md or unregistered/competing active skills require reconciliation, not silent replacement. Finish/cancel and archive any current slice before adopting a different harness.

Only after human approval of the installation preview, apply it, reconcile project/local/binding configuration and run the local integration protocol in `review/LOCAL_INTEGRATION_TEST.md`. Unity CLI is the preferred execution route. Missing required Unity CLI/diagnostics bindings must block; a native Unity CLI mapping is not shipped by this candidate. An alternative needs a demonstrated CLI capability gap, strong supporting evidence and explicit human approval; do not install a third-party provider or select MCP automatically. Use the first-run and paired design prompts in that protocol; do not ask Codex to implement the entire harness again.

## Two decisions remain separate
Decide whether to adopt the candidate design-method changes after a pilot. Separately decide whether to adopt the execution harness after Windows/Unity/Codex validation. A draft PR is neither decision, and a passing offline fixture suite is neither live integration nor game acceptance.
