---
created: 2026-05-25
updated: 2026-07-14
type: concept
summary: Ramirez-Ruiz MOP research — foundational work on Memory-Oriented Programming for LLM agents, schema-based memory scaffolding
tags: [mop, research, llm-agents, memory, cognitive-architecture]
sources: []
status: active
confidence: 0.7
---

# Ramirez-Ruiz MOP Research (2024)

## Overview

The Ramirez-Ruiz MOP (Memory-Oriented Programming) research represents a foundational contribution to architectural memory design for LLM-based agents. The work treats memory not as an afterthought or external database, but as a first-class engineering concern with explicit structure,分层, and update policies. The research is particularly notable for connecting memory architecture to cognitive science concepts (schemas, episodic vs semantic memory) while grounding them in practical LLM agent engineering.

## Core Contributions

### Schema-Based Memory Scaffolding

The central innovation: memory is organized into *schemas* — structured knowledge frameworks that guide both storage and retrieval. Unlike simple key-value memory, schemas encode relationships between memory entries, enabling structured recall and analogical reasoning.

A schema in the MOP sense is not a database schema (rigid, enforced) but a cognitive schema (flexible, generative). Schemas can be incomplete, can overlap, and can be dynamically instantiated based on context.

### Three-Layer Memory Model

Ramirez-Ruiz proposed a three-layer memory hierarchy that maps to cognitive science categories:

1. **Working memory**: Current session context, maintained in the LLM context window
2. **Short-term memory**: Persistent within a project or task; compressed session summaries
3. **Long-term memory**: Cross-session knowledge that guides overall agent behavior

This maps to the broader MOP architecture layers, with the key insight that *the boundary between short-term and long-term memory is where most architectural failures occur* — either forgetting too much or retaining too much noise.

### Memory Update Policies

The research identified that naive memory (append-only) degrades quickly. The proposed solution: *selective consolidation* — episodic records are periodically compressed into semantic summaries using the LLM itself as the compressor. The consolidation policy determines what survives:

- **Recency-weighted**: Recent memories get priority (simple but suboptimal)
- **Relevance-weighted**: Memories relevant to current task get priority (better but requires relevance detection)
- **Diversity-weighted**: Ensures coverage across knowledge domains (prevents schema monopolization)

## Relationship to Cognitive Architecture

This work connects directly to the [[cognitive-architecture]] framework's MCM (Metacognitive Control Model):

- The **knowledge self-model** in MCM corresponds to the long-term memory layer in MOP
- The **meta-cognitive self-model** corresponds to the schema metadata — information about how the agent reasons, not just what it knows
- MOP provides the *substrate*; MCM provides the *control framework* for using that substrate

## Connection to MOP Architecture

The general [[mop-architecture]] pattern builds on this research, extending it into a broader design framework. Ramirez-Ruiz established the foundational principles; MOP architecture applies them as a general pattern for LLM agent design.

Specific MOP architecture decisions (layer count, update policies, retention budgets) can be seen as instantiations of the Ramirez-Ruiz framework with different engineering tradeoffs.

## Key Open Questions from This Research

1. **Schema competition**: When new information conflicts with existing schemas, how does the agent resolve the conflict? Is there a schema arbitration mechanism?

2. **Memory lifespan**: What determines when a memory entry should be promoted from short-term to long-term? Is there a threshold-based policy, or something more nuanced?

3. **Retrieval vs recognition**: The research notes that memory systems often conflate retrieval (actively recalling) with recognition (knowing something is in memory). Which does the agent actually do, and does it matter?

4. **Compression fidelity**: The LLM-as-compressor approach raises questions: does compression systematically bias memory in ways that accumulate over time? Are there "compression artifacts" analogous to JPEG artifacts in lossy image compression?

## Connections

- [[mop-architecture]]: general pattern this research established
- [[cognitive-architecture]]: cognitive science framework MOP connects to
- [[bounded-structured-memory]]: layered memory implementation in Hermes
- [[catastrophic-forgetting]]: the problem memory scaffolding addresses
- [[prd-ralph-loop-mop-gemini]]: experimental extension using Gemini

## See Also

- The [[PRD Ralph Loop MOP Gemini]] page for experimental implementation work
