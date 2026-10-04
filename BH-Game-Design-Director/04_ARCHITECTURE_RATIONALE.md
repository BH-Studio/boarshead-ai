# Architecture Rationale — Why v3 Uses One Orchestrator + Dynamic Panels

## Decision
Use **one Custom GPT** with a Design Orchestrator and dynamically routed specialist panels rather than several independent Custom GPTs.

## Why
### 1. A Custom GPT is one configured model/context
Persona labels inside one GPT are best treated as disciplined professional lenses. Calling them "independent agents" overstates what the no-code GPT is doing and encourages repetitive committee simulation.

### 2. The workflow needs a single design authority path
The system needs continuity from problem definition through human approval, milestone decomposition, Codex review, and final acceptance. A manager/orchestrator pattern preserves that ownership.

### 3. Multiple Custom GPTs would make the human the integration bus
Separate Design, Architecture, QA, and Production GPTs would require repeated context handoff and canon synchronization. Because GPT conversations begin fresh, the workflow would become more dependent on manual copy/paste and duplicated knowledge.

### 4. Dynamic routing reduces cost and noise
A UI-only question should not trigger narrative, marketing, audio, production, and architecture monologues. Specialist panels are invoked only when their discipline can change the answer.

### 5. The architecture maps cleanly to future true multi-agent implementation
If this workflow later moves to the OpenAI API/Agents SDK, the Research Cell, Technical Board, Validation agent, etc. can become truly separate context-isolated agents while the same Orchestrator/lifecycle remains.

## Internal panels
### Design Council
Defines player experience, mechanics, systems, tradeoffs, and game-facing behavior.

### Evidence & Research Cell
Retrieves and synthesizes external precedent/current player evidence. It does not choose the design.

### Technical Review Board
Challenges architecture, persistence, scale, performance, reuse, integration, testability, and production feasibility.

### Red Team
A temporary adversarial mode whose job is to falsify the preferred design and expose risks before approval.

### Delivery Board
Turns approved design into milestones and implementation-ready acceptance criteria.

### Verification Review
Maps Codex evidence back to approved acceptance criteria and system design.

## Why not fixed teams in every turn
Fixed teams create unnecessary context and tend to manufacture opinions simply because a persona exists. The Orchestrator instead uses **responsibility-based routing**.

## Why research follows problem framing
Researching comparables before defining the problem can anchor the team on familiar solutions. v3 first states what needs to be solved and which unknowns matter, then asks Rhea to research those targeted questions.

## Why approval happens after the question gate
The team can ask much better questions after it has a candidate design, technical review, red-team findings, and validation results. Early intake asks only blockers that would otherwise waste work.

## Why Codex packaging is a compiler step
Once a milestone is approved, prompt writing should not become another design session. The Implementation Package Compiler translates approved decisions into a precise execution contract. If a design-level conflict is discovered, it escalates rather than silently changing the design.
