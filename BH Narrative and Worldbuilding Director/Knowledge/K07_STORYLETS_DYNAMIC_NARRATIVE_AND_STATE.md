# Storylets, Dynamic Narrative, Salience, and Narrative State

## Why this matters
"Branching narrative" is only one way to create player-responsive stories. Open-world, systemic, replayable, or long-running games often benefit from modular content selected by state rather than a giant tree.

Emily Short's "Beyond Branching" is a key practical reference for quality-based, salience-based, and waypoint structures.
Source: https://emshort.blog/2016/04/12/beyond-branching-quality-based-and-salience-based-narrative-structures/

## Storylets
A **storylet** is a relatively self-contained narrative unit that becomes eligible under defined conditions and can update state afterward.
A useful storylet specification:
- ID/title;
- dramatic purpose;
- entry/preconditions;
- exclusion conditions;
- priority/salience;
- participants/location;
- content/choices;
- outcomes;
- state changes;
- cooldown/repeat policy;
- follow-up hooks;
- continuity assumptions;
- fallback behavior.

## Quality-based narrative
Content becomes available based on **qualities/state variables**: skills, relationships, inventory, discoveries, progress, reputation, location, faction state, etc.

### Strengths
- modular content can be added without rewriting a whole tree;
- handles "collect these three facts in any order" elegantly;
- supports many intersecting short arcs;
- good for live/episodic/open-world structures.

### Risks
- bookkeeping/state sprawl;
- players may lose causal understanding;
- narrative arcs can feel like disconnected cards without strong spine/waypoints;
- state names may become implementation leakage rather than author-friendly meaning.

## Salience-based narrative
When multiple content pieces are eligible, choose the **most contextually relevant** based on location, recent events, relationships, world state, topic, emotional state, recency, or dramatic need.

### Strong uses
- contextual companion dialogue;
- reactive barks;
- ambient NPC commentary;
- situational cut-ins;
- selecting among possible scenes after variable play.

### Authoring rule
Always provide broad safe defaults before highly specific lines. Specific content should override or outrank general content when its conditions are met.

## Waypoint narrative
The narrative has important authored destinations, while the route between them can flex or "heal" around player input. This is useful when player freedom matters but the story still needs to reach critical revelations/decisions.

## Narrative state design — creative layer
The Narrative Director may define **conceptual** state without dictating code architecture.
Common narrative dimensions:
- relationship trust/respect/intimacy/rivalry;
- faction standing/obligation;
- discoveries/knowledge;
- promises/debts;
- moral/value pattern;
- secrets revealed;
- quest progress;
- world-event aftermath;
- companion availability;
- time/season/story phase;
- trauma/stress/mood only when narratively justified;
- topic history / repeated conversation;
- player reputation/identity labels.

Use human-meaningful names. Do not reduce every emotional relationship to one scalar if multiple dimensions matter.

## Narrative-state ownership questions
From a creative standpoint, ask:
- Is this state about **what happened**, **what someone believes happened**, or **what the player knows**?
- Is it global, character-specific, relationship-specific, location-specific, or route-specific?
- Must it persist across sessions?
- Can it decay or be reversed?
- Does the player need to see it?
- Does the narrative need exact values or only bands/conditions?

If implementation detail becomes necessary, generate a Narrative–Systems Interface for Systems Director.

## Storylet selection design
A robust dynamic narrative normally needs several controls:
- eligibility;
- priority/salience;
- novelty/recency suppression;
- arc phase;
- pacing cooldown;
- thematic/emotional compatibility;
- required/forbidden participants;
- fallback content;
- mandatory waypoint override.

## Dynamic narrative failure modes
- endless low-value chatter;
- repeating a "first-time" line;
- character knows something they never learned;
- emotional whiplash from incompatible scenes;
- important storylet never becomes eligible;
- over-specific condition creates unreachable content;
- random selection beats a dramatically urgent event;
- player cannot tell why events happen;
- every variable combination requires bespoke writing.

## Validation
- enumerate representative state combinations;
- randomized/simulated walkthroughs if a tool supports them;
- check unreachable/overused storylets;
- verify first-time/repeat variants;
- test out-of-order knowledge;
- test missing participant/location;
- test fallbacks;
- inspect dramatic pacing across long runs;
- verify waypoint convergence.

## Tool connections
- **Yarn Spinner** currently documents advanced storylets, saliency, node groups, variables, flow control, and a Story Solver verification tool: https://www.yarnspinner.dev/docs/
- **Ink** is designed for branching with recombination and state while remaining text-centric: https://github.com/inkle/ink/blob/master/Documentation/WritingWithInk.md
- **articy:draft X** can visually connect narrative content and simulate interactive story flows: https://www.articy.com/en/pillars/writing/
