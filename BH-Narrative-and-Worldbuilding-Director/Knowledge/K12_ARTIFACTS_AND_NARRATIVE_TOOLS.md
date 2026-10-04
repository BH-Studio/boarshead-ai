# Narrative Artifacts and Authoring Tools

## Artifact philosophy
Create only enough documentation to preserve canon, support iteration, and let future sessions rehydrate the project. Prefer text-forward files with stable headings, IDs, and cross-references. A tool database may become authoritative later, but keep a clear exportable canon layer.

## Core artifacts
### NARRATIVE_BRIEF.md
- game/player fantasy;
- premise;
- dramatic question;
- emotional promise;
- themes;
- tone;
- protagonist model;
- agency target;
- narrative delivery;
- anti-goals/non-negotiables.

### STORY_ARCHITECTURE.md
- whole-game transformation;
- Hero's Journey functional map;
- act/phase structure;
- major anchors/turning points;
- reveals/reversals;
- fixed vs flexible content;
- endings;
- setup/payoff index.

### WORLD_BIBLE.md
- foundational premises;
- world rules/pressures;
- history;
- factions/institutions;
- cultures/everyday life;
- locations;
- speculative systems;
- mysteries;
- glossary/naming.

### CHARACTER_BIBLE.md
Per major character:
- role/function;
- want/need/fear/belief/contradiction;
- history/secret;
- relationships;
- voice;
- pressure behavior;
- arc;
- player agency boundary;
- knowledge state.

### RELATIONSHIP_MAP.md
- relationship pair/group;
- starting assumptions;
- trust/power/dependency;
- turning points;
- rupture/recovery;
- branch-dependent states;
- final states.

### QUEST_AND_ARC_INDEX.md
- ID;
- type;
- narrative purpose;
- characters/factions;
- dramatic question;
- prerequisites;
- major beats/choices;
- consequences;
- larger-arc connections;
- status.

### CHOICE_CONSEQUENCE_MAP.md
- choice ID;
- player intention;
- choice type;
- immediate response;
- state change;
- delayed/cumulative consequence;
- acknowledgment;
- payoff;
- rejoin/convergence behavior.

### NARRATIVE_STATE_MODEL.md
Creative-level definitions of qualities/state the story needs, who/what they apply to, visibility, persistence expectation, and narrative use. Avoid implementation architecture.

### DIALOGUE_STYLE_GUIDE.md
- global prose/dialogue tone;
- character voiceprints;
- formatting conventions;
- choice-label conventions;
- profanity/content boundaries;
- exposition rules;
- barks/banter rules;
- localization-friendly guidance.

### CANON_LEDGER.md
Hard canon / soft canon / open items, source/approval, knowledge boundaries, change history.

### OPEN_QUESTIONS.md
Unresolved creative decisions with impact and next revisit trigger.

### NARRATIVE_CHANGE_LOG.md
Approved canon changes and ripple effects.

### NARRATIVE_SYSTEMS_INTERFACE.md
Optional cross-discipline handoff: narrative purpose, conceptual states, events, consequences, persistence expectations, authoring/debug needs, examples, failure conditions, systems questions.

---

# Authoring tools

## articy:draft X — narrative CMS / visual planning hub
### Strong fit for
- interconnected story/world/character databases;
- branching dialogue and flowcharts;
- quest/narrative planning;
- keeping context linked to characters/locations/items;
- simulating interactive narrative logic before game integration;
- structured data handoff to engines.

### Workflow recommendation
Use articy as the **structured narrative source of truth** when the project benefits from visual flow and linked canon. Keep stable IDs and exportable summaries so critical canon is not trapped in screenshots.

Official narrative-design overview: https://www.articy.com/en/pillars/writing/

## Ink / Inky — prose-first interactive flow
Ink is a text scripting language built around branching and recombining flow, state, and redrafting.

### Strong fit for
- prose-heavy interactive scenes;
- choice narratives with frequent rejoining;
- state-dependent variants;
- rapid writer-centric iteration;
- testing branching "by eye" and through playthroughs.

Official writing documentation: https://github.com/inkle/ink/blob/master/Documentation/WritingWithInk.md

## Yarn Spinner — dialogue-centric interactive narrative
Yarn Spinner provides a human-readable dialogue scripting language with nodes, lines, options, variables, flow control, commands/functions, and current advanced documentation for storylets/saliency/node groups. Its current docs also expose preview/testing workflows and Story Solver verification.

### Strong fit for
- dialogue-heavy games;
- NPC conversations;
- quest dialogue;
- reactive/conditional dialogue;
- storylets and contextual conversation;
- writer/programmer shared text workflow.

Official docs: https://www.yarnspinner.dev/docs/

## Twine — rapid nonlinear prototype
Twine is an open-source tool for interactive nonlinear stories and can use variables/conditional logic when needed.

### Strong fit for
- fast browser-playable narrative prototypes;
- testing choice wording and flow with users;
- visualizing simple branches;
- pitching/proving a narrative experience before production tooling.

### Caution
A visible link graph can encourage tree-shaped thinking even when a storylet/salience/state model would scale better. Use the prototype that matches the narrative architecture.

Official site: https://twinery.org/

---

# Tool selection matrix
| Need | Best first consideration |
|---|---|
| Master narrative database + visual flow | articy:draft X |
| Prose-heavy branching/recombination | Ink |
| Dialogue-centric runtime authoring | Yarn Spinner |
| Fast user-testable branch prototype | Twine |
| Dynamic storylet/salience planning | articy / Yarn / Ink depending runtime needs |

The Narrative Director should choose a **narrative architecture first**, then select the tool. Do not distort story design merely because one tool makes a certain graph easy to draw.
