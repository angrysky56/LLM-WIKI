---
summary: RiM — Reasoning in Memory, latent reasoning via fixed memory blocks in single forward pass
tags: [paper, arxiv, llm, reasoning, test-time-compute, working-memory]
updated: 2026-05-30T01:35:45Z
created: 2026-05-30T01:35:45Z
---

---
created: 2026-05-30T00:00:00Z
updated: 2026-05-30T00:00:00Z
type: source
summary: "RiM (Reasoning in Memory) — latent reasoning via fixed memory blocks in a single forward pass, decoupling internal computation from external autoregressive generation."
tags: [paper, arxiv, llm, reasoning, test-time-compute, working-memory, latent-reasoning]
sources: https://arxiv.org/abs/2605.30343
status: active
confidence: high
---

# Unlocking the Working Memory of Large Language Models for Latent Reasoning

**Paper**: Reasoning in Memory (RiM)  
**arXiv**: [2605.30343](https://arxiv.org/abs/2605.30343)  
**Authors**: Lukas Aichberger, Sepp Hochreiter — JKU Linz (ELLIS Unit Linz, LIT AI Lab); NXAI GmbH  
**Published**: 2026-05-28  
**Categories**: cs.CL, cs.AI

## Executive Summary

RiM replaces autoregressive generation of reasoning steps with **fixed memory blocks** — special token sequences that unlock LLM working-memory capacity. Since memory blocks are fixed (not generated), they can be processed in a single forward pass, enabling compute-efficient latent reasoning. A two-stage curriculum first grounds memory blocks by predicting explicit reasoning steps, then discards step-level supervision and iteratively refines the final answer after each block.

## Core Problem

Chain-of-thought reasoning couples internal computation to external text generation — forcing LLMs to "think out loud" in natural language, which allocates part of the computational budget to grammatical fluency rather than pure internal computation. Latent reasoning methods (continuous representations instead of discrete tokens) preserve the step-by-step generation paradigm — each intermediate computation must still be externalized before future computation can condition on it.

## Technical Approach: Reasoning in Memory (RiM)

### Memory Blocks

Fixed sequences of special tokens (`<b> <m><m> ... <\b>`) processed in parallel within a single forward pass. The LLM learns to use these as an internal workspace — holding and manipulating task-relevant representations without externalizing intermediate thoughts.

### Two-Stage Curriculum

**Stage 1 — Grounding**: Train the LLM to predict explicit reasoning steps after each memory block. This grounds the memory blocks in intermediate computation.

**Stage 2 — Refinement**: Remove step-level supervision; train the LLM to iteratively refine the final answer after each memory block. Memory blocks become vehicles for latent computation, not just scaffolding for generated text.

### Comparison to Prior Approaches

| Approach | Generation Mode | Coupling |
|----------|----------------|----------|
| Chain-of-Thought | Autoregressive tokens | Externalizes reasoning |
| Continuous latent | Step-by-step continuous | Still externalizes |
| RiM | Single forward pass | Internal only |

## Key Results

- Matches or exceeds existing latent reasoning methods across language models of different families and sizes
- Avoids autoregressive generation of thoughts
- Compute-efficient: single forward pass processing of memory blocks
- Validated on reasoning benchmarks

## Connections

- [[test-time-scaling]] — alternative to test-time compute scaling via generation
- [[reasoning-scaffolding]] — connects to Entropy-Cut MH (reasoning point identification)
- [[llm-architecture]] — working memory as architectural primitive
- [[evolutionary-search]] — both address escaping local optima in reasoning (BES via evolutionary operators)
- [[parallel-reasoning]] — parallel processing of memory blocks

## Key Quote

> "Human cognition can use working memory to hold and manipulate information internally without the need to externalize intermediate thoughts... part of the computational budget is allocated for generating grammatical and fluent intermediate text, rather than being devoted purely to internal computation."

## Relevance to Agentic AI

As agentic systems scale test-time compute, the inefficiency of autoregressive reasoning becomes a bottleneck. RiM demonstrates that latent reasoning without token generation is viable — potentially enabling faster, more compute-efficient agentic reasoning at test time. Connects to the broader theme of evaluation infrastructure for agentic AI: if we can make reasoning more efficient, we can evaluate it more thoroughly.

## Notes

- JKU = Johannes Kepler University Linz
- NXAI GmbH — Sepp Hochreiter is also co-founder; both work on recurrent memory architectures
- Sepp Hochreiter: known for LSTM (1997), Highway Networks, various recurrent architecture contributions
