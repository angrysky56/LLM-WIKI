---
summary: Project page for Graph-RLM.
tags: [projects, ty-repo, recursive-reasoning]
updated: 2026-05-01T07:06:52Z
created: 2026-05-01T07:06:52Z
---

---
created: 2026-05-01T07:06:42Z
updated: 2026-05-01T07:06:42Z
type: entity
summary: Self-healing Recursive Language Model with persistent graph memory and sheaf-theoretic monitoring.
tags: [projects, ty-repo, angrysky56, rlm, sheaf-theory, recursive-reasoning, falkordb, self-healing]
status: active
confidence: 1.0
---

# Graph-RLM

**Graph-RLM** (Self-Healing Recursive Language Model) is a world-class implementation of the Recursive Language Model paradigm developed by [[tyler-hall|Ty]]. It replaces linear context windows with a persistent, recursive, and self-correcting **Graph of Thoughts (GoT)**.

## Architectural Pillars
- **Recursive Logic Machine (RLM)**: Decomposes complex tasks into sub-queries that maintain shared stateful memory.
- **Topological Sheaf Context**: Treats context as a sheaf to preserve high-fidelity reasoning across deep recursions, solving "context rot."
- **Constraint Augmented Generation (CAG)**: Ingests documents to mine logical invariants and codifies them into executable **Axioms** (Guardrails).
- **Sheaf-Theoretic Monitoring**: Measures **Consistency Energy** and detects **Holonomy** (logical loops) using the Sheaf Laplacian.
- **The Dreamer (Sleep Phase)**: Implements the **Ralph Protocol** (Wake -> Sleep -> Wake) to consolidate high-surprise events into permanent wisdom (Axioms).

## Tech Stack
- **Persistence**: FalkorDB (Graph + Vector Store).
- **Execution**: Python REPL with `uv` process isolation.
- **Metacognition**: online Metacognitive Control of Decisions (oMCD) for resource optimization.

## Connections
- [[efhf]] — Implements the "Sheaf Consistency" and "Verification" layers.
- [[agem]] — Provides the underlying recursive reasoning engine for multi-agent groups.
- [[tys-repos]] — Part of Ty's repository collection.
