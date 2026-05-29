---
created: 2026-05-21T08:00:00Z
updated: 2026-05-21T08:00:00Z
type: concept
summary: Neural memory architecture combining attention with a learnable long-term memory module that dynamically stores sequence-specific information at test time
tags: [llm, memory, architecture, neural-memory, titans]
sources: [https://arxiv.org/abs/2501.00663]
status: active
confidence: 1.0
---

# Titans (Architecture)

Titans is a neural network architecture family introduced by Google Research (Behrouz, Zhong, Mirrokni) that augments standard attention with a learnable neural long-term memory module. The core innovation is a three-tier memory system:

1. **Short-term Memory** — standard attention over local context windows
2. **Neural Long-Term Memory** — learnable parameters that dynamically update during inference to store sequence-specific information
3. **Persistent Memory** — data-independent parameters encoding static knowledge from pretraining

## Variants

- **MAC** (Memory as Context): Memory output concatenated with input sequence — best for long-range dependencies
- **MAL** (Memory as Layer): Memory acts as a hierarchical layer before attention
- **MAG** (Memory as Gate): Memory output combined with main branch via gating

## Key Mechanism: Surprise-Based Memorization

The neural long-term memory uses gradient-based "surprise" (∇θL) to identify which tokens are worth storing. Only tokens that produce a sufficiently large gradient update the memory parameters. This acts as an adaptive filter preventing parameter saturation on long sequences.

## Connections
- [[sources/papers/decoupling-perception-reasoning-vlm-post-training]]
- [[concepts/length-generalization]]
- [[concepts/titans]]
- [[entities/tools/mamba]]
- [[wiki/index]]
- [[agents/skills/librarian-agent/skill]]
- [[concepts/titans-test-time-memory]]
- [[log]]
- [[concepts/surprise-based-learning]]
- [[concepts/neural-long-term-memory]]

- Concept: [[neural-long-term-memory]] — the memory paradigm Titans implements
- Concept: [[surprise-based-learning]] — the memorization mechanism
- Concept: [[length-generalization]] — memory architectures as a solution to length generalization failures
- Source: [[titans-test-time-memory]] — the original paper summary
- Concept: [[mamba]]


## Note on Terminology

The abbreviation "Titans" in `[[titans]]` wikilinks refers to this architecture concept. The paper summary page is [[titans-test-time-memory]].
