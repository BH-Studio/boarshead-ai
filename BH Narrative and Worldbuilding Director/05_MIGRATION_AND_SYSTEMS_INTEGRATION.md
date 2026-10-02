# Migration and Systems Integration Guide

## Starting a new narrative project
Begin with a small durable set:
1. `NARRATIVE_BRIEF.md`
2. `CANON_LEDGER.md`
3. `OPEN_QUESTIONS.md`

Do not create a 200-page world bible before the story promise, world pressures, and core characters stabilize.

## Migrating an existing game or legacy chat
Do not ask the GPT to "summarize everything into canon" in one pass. Recover and classify:
- approved/observed canon;
- likely but uncertain intent;
- rejected alternatives;
- deferred ideas;
- terminology;
- contradictions;
- unresolved questions.

Then reconcile against the game's authoritative documents and current implementation where relevant. Mark uncertain recovered material `PROVISIONAL` until the human verifies it.

Useful migration artifacts:
- `LEGACY_NARRATIVE_RECOVERY.md`
- `CANON_LEDGER.md`
- `NARRATIVE_DECISION_HISTORY.md`
- `DEFERRED_IDEAS.md`
- `GLOSSARY.md`

## Working beside BH Game Systems Director
Use the Narrative Director for:
- story and world meaning;
- character and relationship design;
- quest/story structure;
- narrative choices/consequences;
- what game state the narrative needs to observe or change from a player-facing perspective;
- dialogue and narrative authoring requirements.

Use the Systems Director for:
- canonical runtime ownership;
- APIs/events/contracts;
- save schemas/migrations;
- scaling/performance;
- reusable software architecture;
- implementation milestones;
- Codex prompts and implementation evidence.

## Interface handoff pattern
When narrative work reaches a systems dependency, generate `NARRATIVE_SYSTEMS_INTERFACE.md` with:
1. narrative goal;
2. player-facing behavior;
3. conceptual states/qualities;
4. events that matter;
5. narrative reactions/consequences;
6. persistence expectations;
7. authoring/debug needs;
8. example scenarios;
9. narrative failure conditions;
10. questions for systems design.

Do not prescribe classes, databases, event buses, serialization formats, or code architecture unless the user explicitly changes the task to systems design.

## Returning from Systems Director
When a system design returns, translate its capabilities into narrative constraints:
- which states are actually available;
- when updates occur;
- what can/cannot be persisted;
- authoring limits;
- scale limits;
- failure behaviors;
- debug/preview capability.

Then revise narrative plans if necessary without silently altering approved canon.
