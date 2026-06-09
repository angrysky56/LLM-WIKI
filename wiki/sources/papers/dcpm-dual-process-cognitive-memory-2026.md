---
summary: "DCPM: Dual-process cognitive memory for self-evolving LLM agents — System 1 (daytime writer) + System 2 (nighttime inducer) on a cognitive hierarchy from raw facts to cross-domain schemas. Tencent."
tags: [agent-memory, dual-process, self-evolution, cognitive-architecture, arxiv-2026-06-09]
updated: 2026-06-09T15:06:37Z
created: 2026-06-09T15:06:37Z
---

# DCPM: Dual-Process Cognitive Memory for Self-Evolving LLM Agents

**arXiv:** 2606.09483 | **Authors:** Tianxiang Fei, Mingyang Song, Mao Zheng, Xiang Yu (Tencent)

## Problem

Current LLM agent memory systems treat long-term memory as a retrieval problem: vector stores, temporal knowledge graphs, and update-in-place layers are all engineered to surface relevant text chunks at query time. But this single-retrieval-surface approach **collapses belief revision, causal coupling, and cross-domain abstraction into one mechanism tuned for surface recall**. An agent that has spoken with the same user for weeks still confidently misanswers basic personalisation queries that a careful human assistant would not — because it cannot model *how* a stated belief was revised, *why* a preference shifted, or what latent patterns link behaviours across seemingly unrelated life domains.

## Method — DCPM

DCPM (Dual-Process Cognitive Memory) reorganises agent memory along a **cognitive capability hierarchy** ascending through six levels:

1. **Raw inputs & atomic facts** — the passive foundation
2. **Diachronic belief trajectories** — how beliefs change over time (supersedes chains)
3. **Identity** — stable characterisation of the user across interactions
4. **Domain schemas** — structured knowledge about specific domains
5. **Latent intentions** — inferred goals behind observed behaviour
6. **Cross-domain patterns / core schemas** — higher-order abstractions recurring across life domains

This hierarchy is driven by **two processes** inheriting the architectural split of dual-process theory:

- **System 1 (Synchronous Daytime Writer):** Records belief revisions as **doubly linked supersedes chains**. Each time the user expresses a new preference or corrects a prior statement, System 1 links the old belief to the new one bidirectionally, preserving the revision history. Operates synchronously during agent-user interaction.

- **System 2 (Asynchronous Nighttime Engine):** Runs as a background process during idle periods. Induces domain schemas, latent intentions from observed behaviour patterns, and sweeps for **cross-domain collisions** — patterns that recur across seemingly unrelated domains — abstracting them into higher-level core schemas. This is the system that turns episodic records into semantic knowledge.

The two-process split means the agent can simultaneously maintain a faithful interaction record (System 1) and progressively build deeper understanding through offline consolidation (System 2) — analogous to the wake/sleep cycle in biological cognition, with System 2 doing the "sleep consolidation" work.

## Results

Evaluated on LongMemEval, PersonaMem, and PersonaMem-v2 benchmarks:

| Metric | DCPM Full | DCPM (System 1 only) | Prior SOTA |
|--------|-----------|----------------------|------------|
| PersonaMem-v2 (implicit inference) | **+5.20** over S1-only | baseline | — |
| LongMemEval (span recall) | competitive | ~matched | previous best |
| PersonaMem (direct recall) | competitive | strongest | — |

Key pattern: **Enabling System 2 contributes most where the benchmark rewards implicit cross-session inference** (up to +5.20 on PersonaMem-v2) and least on span recall. This matches the architectural prediction — System 2 is designed for abstraction and inference, not verbatim retrieval.

## Limitations

- System 2 runs asynchronously — the consolidation latency means the agent operates with an outdated cognitive model until the next nighttime cycle
- The hierarchy levels are hand-designed; learned hierarchical representations could be more adaptive
- Evaluated only on personalisation benchmarks — generalisation to other agent domains (tool use, task planning) is unvalidated
- System 2's schema induction quality depends on sufficient interaction history; cold-start performance is unclear
- Single-agent context only — no multi-agent or delegation-scoped evaluation

## Connections

- [[sleep-self-modify-consolidate-2026]] — Sleep/cognition cycle is a direct antecedent: Sleep's wake/sleep paradigm for parameter-level consolidation and DCPM's daytime/nighttime memory hierarchy are complementary. Sleep consolidates into parameters; DCPM consolidates into schemas.
- [[autosci-memory-centric-research-lifecycle-2026]] — AutoSci's SciMem provides a schema-governed two-region memory with lifecycle states; DCPM provides the cognitive hierarchy that could govern the schema design.
- [[bounded-representation-capacity]] — The hierarchy is a direct response to bounded capacity: rather than trying to store everything, DCPM compresses interaction history into progressively abstract representations.
- [[continual-learning]] — DCPM is a continual learning architecture for agent memory, explicitly designed to handle evolving user beliefs.
- [[skillopt-self-evolving-2026]] — Self-evolving agents that update their skills based on interaction history; DCPM provides the memory substrate for those updates.
- [[reuserl-skill-reuse-compression-2026]] — MDL-grounded compression as an alternative lens: DCPM compresses through cognitive abstraction rather than skill-dictionary segmentation.

## Key Quote

> "An LLM agent that has spoken with the same user for weeks accumulates a long, evolving record of what the user said, did, and preferred, yet still confidently misanswers basic personalisation queries that a careful human assistant would not."

## Discussion

DCPM is significant for the wiki's **bounded-self-model** theme because it provides a concrete architecture for one of the four axes — **the introspection axis**. The model's inability to inspect its own evolving understanding of the user is precisely the gap that System 2's nighttime schema induction addresses. Combined with Sleep's wake/sleep paradigm and AutoSci's harnessed memory, the trio forms a complete picture: the agent needs episodic recording (System 1), periodic consolidation (System 2/Sleep), and harnessed runtime control (AutoSci SciFlow) to maintain a faithful self-model.
