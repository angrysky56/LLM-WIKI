---
summary: Memory architecture for multi-agent LLM systems — pointers, Markovian carries, and externalized cognitive infrastructure. Synthesizes DCPM (2606.09483), skill economics (2606.09421), observability (2606.09692), and externalization review (2604.08224) into a practical design.
tags: [memory, agent-architecture, Markovian-carryover, externalization, cognitive-architecture, multi-agent, synthesis]
type: synthesis
status: active
confidence: 0.9
created: 2026-06-10
updated: 2026-06-10
---

# Externalized Memory Architecture for Multi-Agent LLM Systems

**System:** Hermes Agent + LLM-WIKI wiki + Neo4j/Synapse + Headroom compression
**Context:** 8-agent wiki system (overseer, researcher, arxiv, news, ingest, librarian, librarians-assistant, insights), 1,212-page knowledge vault, multi-session daily operation

## The Problem

LLM agents forget. Every session starts from near-zero: the context window is
empty, prior reasoning is gone, and last session's discoveries might as well
have been made by a stranger. The agent's built-in memory is a 2,200-char
key-value store — a sticky note, not a memory system.

Multi-agent architectures compound this: agent A discovers a bug, agent B
encounters it three sessions later with no way to know about A's fix. Agents
write reports that get compressed by cost-saving proxies (`<<ccr:...>>`
markers destroy the original content). Tools change their output format
between sessions. The system "knows" things but cannot access its own knowledge.

Current approaches fall into two failure modes:

1. **Retrieval-only** (RAG): dump everything into a vector DB, retrieve by
   surface similarity. Misses structured state, working intentions, and
   operational patterns.
2. **Parametric-only**: expect the model to remember within its context
   window. Fails at cross-session continuity and degrades as context grows.

We propose a **layered externalization architecture** grounded in four recent
papers and validated by our own production experience.

## Theoretical Foundation

### 1. Externalization as Cognitive Infrastructure (Zhou et al., 2026)

*"Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols
and Harness Engineering"* (arXiv 2604.08224) argues that agent capabilities are
increasingly **externalized** into runtime infrastructure rather than model
weights. Memory externalizes state across time, skills externalize procedural
expertise, protocols externalize interaction structure, and harness
engineering coordinates them.

Critically, the paper frames this as a **cognitive artifact** problem: external
infrastructure transforms hard cognitive burdens into forms the model can solve
more reliably. The quality of this infrastructure — not model capability — is
what determines system reliability.

**Implication:** Memory architecture is a first-class engineering concern, not
an afterthought. The structure of externalized state matters as much as the
retrieval mechanism.

### 2. Dual-Process Cognitive Memory (Fei et al., 2026)

*"Memory Beyond Recall: A Dual-Process Cognitive Memory System for
Self-Evolving LLM Agents"* (DCPM, arXiv 2606.09483) separates agent memory
into two processes:

- **System 1** (synchronous daytime): Records belief revisions as linked
  chains — what happened, what superseded what
- **System 2** (asynchronous nighttime): Induces schemas and intentions from
  accumulated records — pattern extraction, cross-domain abstraction

System 2's contribution is largest for **implicit cross-session inference**
(+5.20 on PersonaMem-v2) and smallest for surface recall — matching the
architectural prediction that consolidation, not storage, is the bottleneck.

**Implication:** Agent memory needs both a write-path (capture as it happens)
and a consolidation-path (distill patterns afterward). Running only System 1
gives you a diary; running both gives you a knowledge base.

### 3. Operational Anchors and Skill Economics (Xing et al., 2026)

*"What Should a Skill Remember? Quality-Cost Trade-offs in Cost-Aware Skill
Rewriting"* (arXiv 2606.09421) found that **~20% of skill content accounts
for ~80% of error-prevention value**. These "operational anchors" — validation
checks, recovery procedures, edge-case handling, domain rules — are the first
things removed by naive compression, and the most economically valuable parts of
the skill.

Naive compression reduced tokens 55% but *increased* total cost by 18%
through increased exploration and debugging. Cost-aware rewriting (25% reduction)
yielded **-12% total cost**.

**Implication:** Any memory or skill system that optimizes purely for token
reduction will systematically destroy the content that prevents the most
errors. Compression must be **operational-anchor-aware**.

### 4. Observability for Delegation (Mishra & Sharad, 2026)

*"Observability for Delegated Execution in Agentic AI Systems"* (arXiv
2606.09692) proves that delegation-scoped execution is **structurally
underdetermined** from standard observables — audit logs can be identical under
multiple incompatible delegation assignments. A separate observability
infrastructure (gateway-based, polynomial-time reconstruction) is required to
make multi-agent delegation debuggable.

**Implication:** Multi-agent memory isn't just about storing facts — it's about
storing **provable chains of attribution**: who decided what, when, and why.

## The Architecture

```
┌─────────────────────────────────────────────────────┐
│                  MEMORY STACK                       │
│                                                     │
│  L1: Pointer Layer (≤2,200 chars)                   │
│    Hermes built-in memory tool                      │
│    "See skills/headroom/SKILL.md"                  │
│    "Carryover: wiki/scratchpad/agent-sheets/*"     │
│    Ultra-short — bootstrap context only             │
│                                                     │
│  L2: Markovian Carryover (≤512 tokens each)        │
│    wiki/scratchpad/agent-sheets/{agent}/carryover  │
│    Established / Open / Heading sections            │
│    Written at session boundary — survives context   │
│    compression because it's read, not cached        │
│                                                     │
│  L3: Operational Anchors (skills + references)      │
│    ~/.hermes/skills/{agent}/SKILL.md                │
│    references/ — pitfalls, patterns, edge cases     │
│    20% of content prevents 80% of errors            │
│    Must NEVER be naively compressed                 │
│                                                     │
│  L4: Deep Store (Neo4j + ChromaDB + Wiki)          │
│    synapse_remember() → Neo4j graph DB              │
│    wiki-*/ MCP tools → 1,212-page wiki vault       │
│    Vector-indexed via ChromaDB embeddings           │
│    LCM session summaries SQLite                     │
│                                                     │
│  L5: External Context (Hermes scratchpad)           │
│    wiki/scratchpad/YYYY-MM-DD.md                    │
│    Daily operational notes + carryover blocks       │
│    Ephemeral — pruned after 30-90 days              │
└─────────────────────────────────────────────────────┘
```

### Design Principles

1. **Pointers, not copies.** L1–L2 contain summaries and pointers to where
   full context lives (L3–L5), not the content itself. This prevents the 2,200-char
   pointer layer from bloating.

2. **Markovian state is write-once.** Each agent's carryover is overwritten
   at session boundary, never appended. Only the latest matters — prior state
   is preserved via L3 (skills) and L4 (Neo4j timeline).

3. **Operational anchors are sacred.** The pitfalls, known issues, and
   pattern sections in skills (L3) are the highest-value content per
   Xing et al. They must be cost-aware compressed or not compressed at all.

4. **System 2 consolidation is explicit.** A periodic process (librarian
   audit, overseer synthesis, or manual review) distills L5 (scratchpad
   notes) into L3 (skills) and L4 (Neo4j). Don't rely on the model to
   consolidate implicitly — headroom compression will destroy the raw
   material before the model sees it.

5. **Attribution chains for delegation.** Following Mishra & Sharad, every
   agent decision that affects another agent's work is recorded with
   provenance (who/when/why) in the carryover, not just the conclusion.

### The DCPM Mapping

| DCPM Component | Our Equivalent | Purpose |
|---|---|---|
| System 1 (daytime writer) | scratchpad + carryover writes | Record what happened during session |
| System 2 (nighttime engine) | librarian audit + overseer synthesis | Distill patterns, update skills |
| Cognitive hierarchy (facts → beliefs → identity → schemas) | L5 → L4 → L3 | Layered abstraction |
| Belief revision chains | git history + Neo4j timeline | Traceable supersedure |
| Cross-domain patterns | wiki/synthesis/ | Original cross-domain thinking |

### Compression Awareness

Headroom compression destroys ~53% of tokens in tool output. Without
operational anchors preserved to disk, the agent loses:

- Error messages that explain *why* a fix was needed
- The actual data from a prior run (lint output, HITS scores)
- Validation results that prevent re-exploration

**Rule:** Any fact, pattern, or lesson that would prevent a future error
must be written to disk (L3 or L4) immediately — never held only in
conversation context, which gets compressed.
