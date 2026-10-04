# Architecture Rationale

## Why this is not a single giant "writer persona"
Video-game narrative combines several different crafts: dramatic structure, character psychology, worldbuilding, dialogue, quest design, interactive agency, continuity, research, and player experience. One generic writer voice tends to over-index on fluent prose and underweight structure, state, player control, and canon discipline.

The package therefore uses one **Narrative Orchestrator** with dynamic specialist lenses. The model remains one model; personas are deliberately treated as review perspectives rather than fictional independent agents.

## Why this is not the Systems Director workflow with the names changed
Narrative development benefits from **divergence and repeated human steering**. A systems design can often converge toward a specification and then lock it. Story development needs room to discover the story through character, world, theme, and user reaction.

Accordingly:
- the user is a co-author throughout;
- `CREATIVE CHOICE POINTS` happen frequently;
- major alternatives are preserved until the user chooses;
- Blue-Sky ideas are kept separate from canon;
- the workflow can move backward deliberately when a stronger story appears;
- no Codex/implementation compiler exists.

## Why Hero's Journey is core but not sovereign
Hero's Journey is exceptionally useful as a language of transformation: leaving a stable identity/world, undergoing trials that force change, and integrating/returning with a changed self or world. For games, however, a strict linear template can conflict with open-world ordering, player-authored identity, ensemble casts, repeated quest loops, or branching endings.

The controller therefore treats Hero's Journey as the **primary transformation lens** while allowing its dramatic functions to be omitted, inverted, nested, split among characters, or expressed through world/player change.

## Why multiple structural frameworks are retained
No single framework answers every narrative question.
- Three-Act asks whether macro escalation and climax work.
- Story Circle is compact enough for quests and episodes.
- Save the Cat is useful for diagnosing pacing pressure.
- Pixar Story Spine exposes weak causality very quickly.
- Dramatica can expose perspective/theme gaps in complex stories.
- interactive narrative structures answer a different question entirely: how does the story survive player control?

The controller explicitly forbids "framework compliance" as a goal. A framework must reveal or solve a narrative problem to be worth using.

## Why research happens after creative framing
Researching "how other games did it" too early causes anchoring and accidental imitation. The GPT first defines the narrative problem and desired player experience; then the Research Cell looks for relevant evidence and counterexamples.

## Why worldbuilding is causal
Large lore encyclopedias create the illusion of depth but often fail to produce drama. The worldbuilding model instead follows rules and pressures into institutions, everyday life, characters, conflicts, and story/gameplay hooks. This also makes the world easier to remember and maintain.

## Why there is a Narrative–Systems Interface instead of a Codex handoff
Narrative design often needs game state and events: relationship trust, faction reputation, discovery state, quest outcomes, who is alive/present, what the player knows, and world reactions. Those are legitimate narrative requirements, but their software architecture belongs elsewhere.

The optional interface brief preserves the boundary:
**Narrative Director says what the story must be able to perceive/express. Systems Director decides how the game implements it.**

## Why tool-aware but tool-agnostic
articy:draft X, Ink, Yarn Spinner, and Twine solve overlapping but different problems. Locking creative structure to one tool too early can distort the story. The GPT creates clean, structured narrative artifacts first, then adapts them to the selected authoring tool.
