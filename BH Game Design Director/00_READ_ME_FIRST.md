# BH Game Systems Director v3 — Read Me First

## What this rebuild changes
Version 3 replaces the earlier "large committee" mental model with a **Design Orchestrator + dynamic specialist panels** model.

A custom GPT is one model operating in one conversation context. The personas are therefore **professional lenses and responsibilities**, not independent AI processes. The Orchestrator invokes only the expertise needed for the decision, deliberately separates evidence gathering from design judgment, performs an adversarial red-team pass, and owns the approval/milestone lifecycle.

## Recommended use
Use this package to **update the existing Game Design Team GPT** if your account cannot create a new GPT. The architecture does not depend on the GPT having memory; durable project/repository artifacts carry approved state across chats.

## Package structure
### Paste into GPT configuration
- `01B_GPT_INSTRUCTIONS_COMPACT.md` — **recommended installed Instructions**; keeps the always-on controller concise and high-salience.
- `01_GPT_INSTRUCTIONS_FULL.md` — full controller specification/reference; use if your editor accepts it and Preview testing shows the extra detail improves behavior, or keep it as the design source of truth.
- `02_NAME_DESCRIPTION_STARTERS.md` — suggested name, description, conversation starters, and capabilities.

### Upload as GPT Knowledge
Upload **all 12 files in `Knowledge/`**. They are reference material; workflow rules live in GPT Instructions.

### Test before relying on it
- `03_GPT_ACCEPTANCE_TESTS.md` — Preview tests for routing, gates, research, validation, red-team behavior, milestone handling, and Codex review.

### Design rationale
- `04_ARCHITECTURE_RATIONALE.md` — why v3 uses one orchestrator with dynamic panels rather than several Custom GPTs.
- `05_MIGRATION_FROM_V2.md` — what changed from v2.
- `PACKAGE_MANIFEST.md` — file inventory.

## Core lifecycle
```text
YOU
 ↓
DESIGN ORCHESTRATOR
 ↓
Problem framing
 ↓
Targeted evidence/research
 ↓
Design Council
 ↓
Technical Review Board
 ↓
Red Team
 ↓
Validation / revised candidate
 ↓
Comprehensive Question Gate
 ↓
YOU APPROVE SYSTEM
 ↓
Milestone roadmap
 ↓
[for each milestone]
Milestone design → question gate → YOU approve
 → Implementation Package Compiler → Codex
 → evidence review → close or iterate
 ↓
Periodic Integration Gates
 ↓
Final System Acceptance
```

## Important behavioral principle
The system should **not** treat every request as a full studio meeting. The Orchestrator selects the lightest sufficient workflow:
- `LEVEL 0 — Consultation`
- `LEVEL 1 — Feature`
- `LEVEL 2 — System`
- `LEVEL 3 — Foundation / Framework`

The human designer can always override the level.
