---
summary: MOP (Memory-Oriented Programming) architecture integration plan — introducing vault.md as Layer 1 Episodic Working Memory and formalizing MOP compression cycle across all worker agent SKILL.md files
tags: [mop, agent-architecture, memory-management, vault, carryover, episodic-memory, semantic-state]
updated: 2026-06-03T14:49:59Z
---

---
created: 2026-06-03
updated: 2026-06-03T14:48:00Z
type: research
summary: MOP (Memory-Oriented Programming) architecture integration plan — introducing vault.md as Layer 1 Episodic Working Memory and formalizing MOP compression cycle across all worker agent SKILL.md files
tags: [mop, agent-architecture, memory-management, vault, carryover, episodic-memory, semantic-state]
sources: [wiki/concepts/mop-architecture.md, wiki/synthesis/bounded-structured-memory.md]
status: active
confidence: 0.85
---

# MOP Architecture Integration Plan

The MOP (Memory-Oriented Programming) architecture defines a layered approach to memory to enable continuity of cognition. Currently, the agents use `carryover.md` for passing state, but lack a formalized episodic trace (Layer 1) and explicit compression cycle (Layer 1 → Layer 2) as defined by the MOP principles.

## The Goal

Design the MOP architecture efficiently into the agent workflows by introducing `vault.md` as the Layer 1 Episodic Working Memory and formalizing the MOP compression cycle at the end of every agent's run.

## Implemented Changes

### MOP Workflow Integration across Agent `SKILL.md` files

I will update the core execution loop (Quick Start & Workflow) for the worker agents (`arxiv`, `ingest`, `insights`, `librarian`, `news`, `researcher`, `librarians-assistant`) to follow a strict MOP lifecycle:

1. **Layer 2 Load (Semantic State)**: Read `jobs/sheet.md` and `carryover.md` to load the compressed prior state and assignments.
2. **Layer 1 Initialization (Episodic Trace)**: Initialize or clear `vault.md` in the agent's directory to act as the working context/scratchpad for the current session.
3. **Execution**: The agent performs its tasks, explicitly logging its reasoning, intermediate findings, and raw data into `vault.md`. It will also use `synapse_remember` for significant events to build a permanent episodic record in the orchestrator memory.
4. **MOP Compression (Layer 1 → Layer 2)**: At the end of the session, the agent reads its `vault.md` (Episodic) and compresses the session trace into its `carryover.md` (Semantic), adhering to the strict ~512 token bound. This ensures that only established facts, open items, and headings survive to the next session, preventing context bloat.

### File Modifications

For each agent's `SKILL.md`:

- **Quick Start**: Add the initialization of `vault.md` and the final MOP compression step.
- **Workflow**: Add instructions to treat `vault.md` as the primary working memory during execution.
- **Final Step**: Rename the final step to "MOP Compression (Layer 1 → Layer 2)" and clarify that it involves reading the verbose `vault.md` and summarizing it into the strict `carryover.md` template.

How MOP is Now Implemented Efficiently
Instead of relying on a vague idea of carryovers, the agents now execute a very structured, layered memory lifecycle during every run:

Layer 2 Load: At the start of the session, the agent reads its compressed carryover.md (Semantic State) along with any assignments from the overseer.
Layer 1 Start: The agent initializes or clears a vault.md file in its directory. This acts as its volatile Episodic Working Memory for the current session.
Trace Logging: As the agent executes tasks (like running API queries, gap analysis, or reading RSS feeds), it logs its thoughts, reasoning, and intermediate outputs directly into vault.md.
MOP Compression: At the end of the session, the agent executes the crucial MOP compression step: it reads the bloated, verbose vault.md (Layer 1) and compresses the actual learnings, findings, and open items down into the strict ~512 token carryover.md template (Layer 2). The vault.md is then archived or cleared so the next session starts fresh.
This ensures your agents can reason deeply without hitting context limits, and strictly adheres to the architectural design from your mop-architecture.md concepts file.

## Connections

- [[mop-architecture]] — the foundational concept (Layer 0/1/2 memory model)
- [[bounded-structured-memory]] — architectural synthesis implementing MOP for agents
- [[markovian-carryover]] — the ~512-token forward-state pattern MOP compression produces
- [[librarians-assistant]] — example agent sheet implementing the MOP lifecycle
- [[librarian-agent]] — peer agent sheet using the same MOP compression protocol
- [[insights-agent]] — peer agent sheet running daily insight synthesis (Layer 1 → Layer 2)
- [[researcher-agent]] — peer agent sheet with MOP-integrated workflow
- [[news-agent]] — peer agent sheet with MOP-integrated workflow
- [[wiki/research]] — the parent index for research projects including this one

## See Also

- [[agent-native-design]] — agent architecture with persistence from the ground up
- [[synapse-llm-wiki-operating-guide]] — operating procedures that complement MOP
- [[llm-wiki-pattern]] — the broader wiki pattern MOP integrates into
