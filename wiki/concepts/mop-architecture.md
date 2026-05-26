---
created: 2026-05-25
updated: 2026-07-14
type: concept
summary: MOP architecture — Memory-Oriented Programming design pattern for LLM agents with persistent, layered memory schemas
tags: [mop, memory, architecture, agent-design, continual-learning]
sources: []
status: active
confidence: 0.75
---

# MOP Architecture

## Definition

MOP (Memory-Oriented Programming) is an architectural design pattern for LLM-based agents that treats memory as a first-class engineering concern — organizing the agent's information storage into layered, purpose-differentiated schemas that persist across sessions and guide reasoning. Unlike traditional software where memory is undifferentiated (RAM is RAM), MOP divides memory into functionally distinct layers with different retention policies, access patterns, and update mechanisms.

The core insight: an agent that cannot remember what it learned last session cannot exhibit genuine continuity of cognition. MOP provides the architectural substrate for that continuity.

## Architectural Layers

MOP architecture typically implements three to four layers, each with distinct properties:

### Layer 1 — Episodic Memory (Session Trace)

The raw record of what happened in the current session. This is the most volatile layer — high fidelity, low persistence. Think of it as the agent's "working memory" of events.

**Properties**: High bandwidth, low latency, session-scoped retention, discarded at session end (or compressed into Layer 2).

### Layer 2 — Semantic Memory (Compressed Knowledge)

Compressed summaries of past sessions and ingested information — the "gist" of what the agent has learned. This layer converts episodic records into stable knowledge representations that can guide future reasoning.

**Properties**: Persistent, queryable, updatable. Lossy compression — not everything survives from Layer 1.

### Layer 3 — Procedural Memory (Skill & Method)

How the agent does things — skill repertoires, prompt templates, delegation patterns, workflow templates. This layer encodes *capability* rather than *knowledge*.

**Properties**: Most stable layer, changes only when skills are added/modified, guides agent behavior without requiring explicit recall.

### Layer 4 — Identity/Self-Model (Optional)

The agent's model of itself — its competencies, limitations, values, and operating principles. This is the MCM (Metacognitive Control Model) layer.

**Properties**: Updated slowly, foundational for self-awareness and calibration.

## Key Design Decisions

### What Goes in Each Layer?

The boundary between episodic and semantic is the critical design decision. MOP原则: *episodic records are exhaustively complete; semantic summaries are selectively compressed*. You cannot reconstruct everything from Layer 2 — that is a feature, not a bug. Compression forces generalization.

### Update Policy

When does Layer 2 get updated? Options:
- **On session end**: Compress the session trace into semantic memory before shutdown
- **On threshold**: When episodic memory exceeds a size budget, compress the oldest entries
- **On query**: Lazy compression — only compress when needed for a specific retrieval
- **Hybrid**: Continuous background compression with priority queue

### Retention Budget

Each layer has an implicit or explicit size budget. When budget is exceeded, older entries are evicted or further compressed. The budget allocation across layers reflects the agent's priorities — an agent that prioritizes knowledge continuity might budget heavily for Layer 2; an agent that prioritizes skill acquisition might budget for Layer 3.

## Connection to MCM Framework

MOP is the *architectural instantiation* of the Metacognitive Control Model (MCM). MCM specifies what must be modeled (knowledge self-model, meta-cognitive self-model); MOP specifies how that information is stored and accessed across time.

The identity/self-model layer (Layer 4) is where MCM lives architecturally:
- The **knowledge self-model** lives in Layer 2 (what the agent knows)
- The **meta-cognitive self-model** lives in Layer 4 (how the agent reasons)

## Connections

- [[cognitive-architecture]]: MOP implements the memory layer of a cognitive architecture
- [[memory-mechanisms]]: broader category; MOP is a specific design pattern within it
- [[bounded-structured-memory]]: Hermes agent's implementation of layered memory
- [[markovian-carryover]]: the forward-state skill that implements MOP-style Layer 1→Layer 2 compression
- [[ramirez-ruiz-mop-2024]]: original MOP research by Ramirez-Ruiz
- [[catastrophic-forgetting]]: the problem MOP mitigates via layered memory architecture

## Open Questions

1. **Compression fidelity**: How much episodic detail must survive compression to Layer 2 to be useful? Is there a minimum fidelity threshold below which compression destroys the signal?

2. **Layer priority under budget pressure**: When memory is constrained, which layer should be protected? Is it task-dependent?

3. **Cross-session schema drift**: As the agent's knowledge evolves, do Layer 2 schemas need to be periodically reorganized? Is there a "schema consolidation" process analogous to memory consolidation in sleep?

4. **MOP vs fine-tuning**: When should the agent compress session experience into memory (MOP) vs incorporate it into weights (fine-tuning)? What determines which path is appropriate?
