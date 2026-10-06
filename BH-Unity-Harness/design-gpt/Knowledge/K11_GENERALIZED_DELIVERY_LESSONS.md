# Generalized Design and Delivery Lessons

## Purpose
This game-agnostic reference retains fifteen process and architecture lessons from reviewed source material. Examples are explanatory only. No source project name, mechanic, genre, player count, middleware choice, rendering pipeline or numerical budget is a default. The provenance is recorded in the authoring review, outside deployed knowledge.

---

# 1. Durable repository state beats chat-only memory
A complex multi-milestone system became easier to manage once durable artifacts existed for:
- project context;
- current state;
- roadmap;
- approved milestone scope;
- work state;
- completion reports;
- decisions/contracts.

### General rule
Design chat can reason; repository/project artifacts should carry approved canon across fresh chats and implementation tools.

---

# 2. Explicit approval before implementation prevents design drift
Milestone specs were more reliable when they had an explicit approved status before Codex worked on them.

### General rule
Separate:
- candidate design;
- approved design;
- implementation.

Do not make Codex infer which brainstorming statement became canonical.

---

# 3. Contract-first work pays off in highly integrated systems
Prior implementation work benefited from explicit contracts/registries/error semantics/fixtures rather than allowing behavior to emerge from implementation details.

### General rule
For systems with many consumers, persistent data, exports/imports, or future extension:
- define identity;
- fields/schema;
- error behavior;
- versioning;
- examples/fixtures;
- invariants;
before large implementation volume.

---

# 4. Separate different meanings of "state"
Prior implementation work highlighted the importance of separating conceptually different domains such as:
- static definitions;
- runtime/generated state;
- knowledge/discovery;
- campaign-specific state.

### General rule
Do not conflate "what exists," "what is happening," "what the player knows," and "what this campaign changed."

This improves persistence, multiplayer authority, modding, testing, and reuse.

---

# 5. Semantic equivalence can matter more than byte identity
For some exports/representations, the real requirement is equivalent meaning rather than identical storage.

### General rule
When multiple formats/platforms/paths exist, explicitly define:
- exact equality;
- semantic equivalence;
- tolerated ordering/encoding differences.

Then build conformance tests around the correct definition.

---

# 6. Corruption/integrity and secrecy are different problems
The reviewed design separated corruption detection/integrity from encryption and recognized that modding can be a legitimate product goal.

### General rule
Choose:
- validation;
- fingerprints/checksums;
- signatures;
- encryption;
- obfuscation;
based on threat model and product policy. Do not use security features reflexively when they undermine supported modding or add cost without a requirement.

---

# 7. Resource envelopes must be explicit and project-specific
The reviewed project used a host-resource envelope and representative scale targets.

### General rule
Every scale-sensitive subsystem should define:
- what it may consume;
- under what workload;
- how the host can constrain it;
- what happens when the envelope is exceeded.

Do **not** copy another project's CPU percentage into other projects without re-deriving it.

---

# 8. Representative-scale tests change architectural confidence
Small fixtures cannot prove a target-scale system. Representative workloads, artifact-size measurements and stress/conformance runs provide evidence for the stated requirement; derive all counts and budgets from the current project.

### General rule
If the word "scale" appears in the requirement, test the scale during the milestone where architecture is still changeable.

---

# 9. Conformance/clean-consumer validation exposes hidden coupling
Standalone/consumer validation is valuable when a subsystem is intended to function as a reusable or independently consumable component.

### General rule
Test the supported public surface from outside the implementation's comfortable home environment.

---

# 10. Validation should be staged
A useful workflow was:
- compile/local sanity;
- focused tests;
- integration;
- stress/scale where needed;
- authoritative regression;
- review;
- completion evidence.

### General rule
Do not run the most expensive suite after every tiny edit by reflex, but do not close a milestone without the agreed authoritative gates.

---

# 11. Completion reports are part of engineering
A completion report made it possible to compare claimed scope, tests, performance, and remaining issues to the milestone spec.

### General rule
Implementation output should include evidence and state transition, not merely "done."

---

# 12. Current-state docs reduce context cost
A concise current-state file and milestone/work-state record reduced the need to carry enormous chat context.

### General rule
Optimize continuity by improving durable summaries, not by growing a permanent mega-chat.

---

# 13. Design authority and implementation authority should remain distinct
The design conversation decides what and why. Codex decides low-level how within approved constraints.

### General rule
When implementation discovers a design-level conflict, escalate it instead of allowing code to quietly redefine the design.

---

# 14. "Done" requires both correctness and conformance
For complex systems, unit tests alone were insufficient. Compilation, integration, conformance, stress, and broader regression each answered different questions.

### General rule
Choose a validation matrix based on claims:
- functional correctness;
- architecture contract;
- scale;
- performance;
- compatibility;
- integration;
- player experience.

---

# 15. Milestones should preserve a coherent frontier
A milestone should leave the project in a state that can be understood, tested, reviewed, and resumed.

### General rule
Prefer durable boundaries and phase/work-state records over a long sequence of half-integrated changes.
