# Migration from v2 to v3

## Keep
v3 retains:
- all original ten game-development disciplines;
- Rhea Research and Perry Production;
- the five system-design framework knowledge packs;
- human approval before final system and milestone implementation;
- scale/reuse/persistence/testing requirements;
- Galaxy Generator continuity/contract/validation lessons;
- durable system specs, ADRs, current state, milestone specs, work state, completion reports;
- Codex evidence review and focused iteration.

## Replace
### Committee Chair → Design Orchestrator
The controller is now explicitly process-only and routes temporary panels.

### "Independent personas" → expert lenses
The package no longer implies that a single Custom GPT is running true context-isolated agents.

### Fixed committee sequence → dynamic routing
Only relevant roles participate.

### Research first → problem framing first
External precedent is now targeted to known design questions.

### One heavy lifecycle → adaptive depth
L0 Consultation, L1 Feature, L2 System, L3 Foundation.

### General challenge → formal Red Team
The preferred design receives an explicit adversarial falsification pass.

### Prompt writing → Implementation Package Compiler
After milestone approval the GPT stops designing and compiles the Codex package from approved artifacts.

### Milestone-only QA → periodic System Integration Gates
v3 catches architecture drift that can accumulate across individually passing milestones.

### 18 Knowledge files → 12 Knowledge files
Behavior moves into Instructions; Knowledge is reference material. This leaves upload headroom and improves retrieval clarity.

## Migration procedure
1. Preserve your existing GPT so it remains a rollback point.
2. Replace its Instructions with `01B_GPT_INSTRUCTIONS_COMPACT.md` as the recommended starting controller. Keep the full Instructions file as the controller specification/reference; switch to it only if your editor accepts it and Preview tests show a benefit.
3. Remove the v2 Knowledge files.
4. Upload all 12 v3 Knowledge files.
5. Update Name/Description/Conversation Starters if desired.
6. Ensure Web Search and Code Interpreter/Data Analysis are enabled if available.
7. Run `03_GPT_ACCEPTANCE_TESTS.md` in Preview.
8. Do not rely on old GPT conversations as canonical project memory; begin a project conversation by providing/project-linking current durable artifacts.
