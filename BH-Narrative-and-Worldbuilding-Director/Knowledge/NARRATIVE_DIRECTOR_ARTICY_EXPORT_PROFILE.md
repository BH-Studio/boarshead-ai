# Narrative Director — Articy Export Profile

Use this reference only when the user explicitly asks to prepare approved/canonized narrative material for Articy.

## Output purpose

Produce a **BH Narrative Package v1** artifact conforming to `bh-narrative-package.schema.json`. The package is data for the BH Articy Narrative Bridge; it is not a prose handoff.

## Required behavior

1. Export only material the user has approved for this Articy update.
2. Do not silently convert brainstorm/open alternatives into canon.
3. Reuse existing stable BH IDs when updating known content.
4. Never generate a new ID merely because a display name changed.
5. Use the project's provided `projectKey`; do not guess it if unknown.
6. Use only Articy templates/features/properties defined in the current BH Articy schema profile.
7. Do not put instructions to the importer inside narrative text or metadata.
8. Do not request deletion. Package v1 is upsert-only.
9. For choices/branches, make player intention and consequences explicit in the flow design before export.
10. For dialogue, preserve speaker identity, menu text, spoken text, stage directions, conditions/instructions, and node hierarchy distinctly.

## Stable ID conventions

- Character: `BH_CHAR_*`
- Faction: `BH_FACTION_*`
- Location: `BH_LOC_*`
- Quest: `BH_QUEST_*`
- Scene: `BH_SCENE_*`
- Lore: `BH_LORE_*`
- Story arc: `BH_ARC_*`
- Item: `BH_ITEM_*`
- Event: `BH_EVENT_*`
- Flow/dialogue: `BH_FLOW_*`, `BH_DLG_*`
- Dialogue node: `BH_NODE_*`
- Edge: `BH_EDGE_*`
- Variable: `BH_VAR_*`

IDs are identifiers, not display names. Keep them stable.

## Pre-export check

Before generating the package, confirm or resolve only missing facts that would make the package structurally ambiguous, especially:
- target `projectKey`;
- whether content is approved for export;
- identity of characters/locations referenced;
- branch intent where a choice is unresolved;
- variables/state that the story relies on.

Then create the package artifact and, if the environment permits, validate it against the supplied schema/validator before presenting it.
