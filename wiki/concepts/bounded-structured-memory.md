---
created: 2026-05-28
updated: 2026-07-14
type: concept
summary: Bounded structured memory — layered memory architecture for agent continuity across sessions, implementing episodic/semantic/procedural separation
tags: [memory, agentic, bounded-memory, layered-memory, markovian-carryover]
sources: []
status: active
confidence: 0.8
---

# Bounded Structured Memory

## Definition

Bounded structured memory is a layered memory architecture pattern for LLM-based agents that divides memory into functionally distinct layers — episodic (session trace), semantic (compressed knowledge), and procedural (skills and methods) — each with bounded capacity, explicit retention policies, and differentiated access patterns. The "bounded" qualifier is critical: each layer has a defined capacity budget, and when the budget is exceeded, entries are evicted, compressed, or consolidated.

The pattern directly addresses the fundamental problem of agent continuity: without structured memory, agents either retain everything (context overflow, noise accumulation) or nothing (no continuity). Bounded structured memory provides a principled middle path.

## Layer Architecture

### Layer 1 — Episodic Memory (Session Trace)

The raw, high-fidelity record of the current session. This is the most detailed layer — every relevant event, decision, and tool result is recorded in essentially uncompressed form.

**Properties**:
- High bandwidth, high detail
- Session-scoped (or until budget exceeded)
- Format: timestamped event log
- Eviction: compressed to Layer 2 on budget exceeded or session end

**Example**: `Session trace: user asked about X → searched Y → found Z → confirmed W`

### Layer 2 — Semantic Memory (Compressed Knowledge)

Summarized, queryable knowledge derived from episodic memory. Raw events are compressed into structured facts, conclusions, and connections.

**Properties**:
- Persistent across sessions
- Lossy compression from Layer 1
- Format: key-value facts, entity relationships, claim records
- Eviction: least-recently-used when budget exceeded; never fully deleted (can be re-summarized from Layer 1 if needed)

**Example**: `Fact: user is interested in topic X; established: Y relates to Z via relationship R`

### Layer 3 — Procedural Memory (Skills and Methods)

How the agent does things — not what it knows but how it operates. Includes prompt templates, delegation patterns, tool use sequences, and learned workflows.

**Properties**:
- Most stable layer; changes only on skill acquisition
- Format: structured skill definitions, workflow templates
- Eviction: rarely, only when skills are replaced

## Boundedness and Budget Allocation

The bounded nature is the defining feature. Budget allocation is a critical design decision:

| Layer | Typical Budget | Retention Policy |
|-------|---------------|------------------|
| Episodic | 4–8 KB per session | Flush on budget exceeded |
| Semantic | 16–32 KB total | LRU eviction, priority boost for recent |
| Procedural | Unlimited (skill count) | Append-only for skills |

Boundedness forces the agent to *forget intelligently* — not randomly, but through principled compression that preserves the most useful information.

## Connection to Markovian Carryover

The [[markovian-carryover]] skill is the Hermes agent's implementation of bounded structured memory. Specifically:

- The `carryover.md` file is Layer 2 — semantic memory, compressed from the session trace
- The `vault.md` is Layer 1 working state — current session episodic context
- The skill definitions in the Hermes workspace are Layer 3 — procedural memory

The carryover pattern enforces the boundedness principle: carryover is hard-capped at ~512 tokens (~2000 characters), forcing ruthless compression of session knowledge into the most essential forward-state.

## Connection to MOP Architecture

Bounded structured memory is the *specific implementation* of the more general [[mop-architecture]] pattern in the Hermes agent context. MOP provides the theoretical framework; bounded structured memory provides the concrete instantiation.

The three-layer model here maps directly to MOP:
- Layer 1 (episodic) = MOP Layer 1 (session trace)
- Layer 2 (semantic) = MOP Layer 2 (compressed knowledge)
- Layer 3 (procedural) = MOP Layer 3 (skills and methods)

## Design Principles

1. **Boundedness is non-negotiable**: Unbounded memory always degrades. Design for eviction from the start.

2. **Compression is selective**: Not everything from Layer 1 makes it to Layer 2. The agent must learn what to compress.

3. **Procedural memory is most stable**: Skills change slowly. Don't rebuild them every session.

4. **Layer independence**: Each layer should be replaceable independently. The episodic store can be swapped for a different implementation without touching semantic or procedural layers.

## Connections

- [[markovian-carryover]]: the skill implementing this pattern in Hermes
- [[mop-architecture]]: the general pattern this implements
- [[hermes-agent]]: the agent using this memory architecture
- [[entities/projects/zettelkasten-engine]]: the pattern-detection engine that implements similar insight-generation principles; both systems use bounded-capacity models for knowledge synthesis
- [[cognitive-architecture]]: the cognitive science foundation (episodic/semantic/procedural memory division is well-established in psychology)
- [[autonomous-agents]]: autonomous agents depend on bounded structured memory for session-level continuity and cross-session persistence
- [[subagent-delegation]]
- [[agent-architectures]]
- [[markovian-dev-agency]]
- [[kanban]]
- [[continual-learning]]
- [[knowledge-management]]
- [[namm]]
- [[agentic-oversight]]
- [[knowledge-architecture-stub]]
- [[persistent-goals-hermes-agent]]
- [[betteti-baggio-bullo-zampieri-idp-hopfield-2025]]
- [[autonomous-ai-agents]]
- [[meta-cognitive-agents]]
- [[catastrophic-forgetting]]
- [[schema-competition]]
- [[agentic-hierarchy]]
- [[bounded-rationality]]
## Open Questions

1. **Optimal budget allocation**: How should total memory budget be distributed across layers? Is there a principled method for determining Layer 2 budget size?

2. **Compression quality measurement**: How do we measure whether Layer 2 compression is preserving the right information? Are there reliable compression fidelity metrics?

3. **Cross-layer consistency**: When Layer 1 is evicted to Layer 2, how do we ensure Layer 2 remains consistent? Can stale Layer 2 entries cause downstream errors?

4. **Procedural memory updates**: When should Layer 3 (procedural) be updated? Currently it's append-only for skills — but skills can become obsolete. Is there a skill depreciation mechanism?
- [[agents]]
- [[delegation]]