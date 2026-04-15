---
summary: Bae et al. (2025) — Mixture-of-Recursions: dynamic per-token recursion depth in shared-parameter transformers; expert-choice and token-choice routing; recursion-wise KV caching; 47% fewer params, 2x throughput; provides the adaptive-depth execution substrate for EML compiled transformers
tags: [transformers, recursive-transformers, adaptive-computation, parameter-sharing, KV-caching, routing, efficiency]
updated: 2026-04-15T06:20:13Z
created: 2026-04-15T06:20:13Z
---

# Mixture-of-Recursions (MoR)

**Authors:** Bae, Kim, Bayat et al. (KAIST AI, Google DeepMind, Mila)
**Source:** [arXiv:2507.10524v3](https://arxiv.org/html/2507.10524v3)
**Published:** 2025 (v3 updated 2026)

## Core Contribution

MoR unifies three efficiency axes in a single Recursive Transformer architecture:

1. **Parameter sharing** — a shared layer stack is reused across recursion steps (weight tying)
2. **Adaptive computation** — lightweight routers assign per-token recursion depth dynamically
3. **Memory-efficient KV caching** — selective caching only for tokens active at each depth

The key insight: not all tokens require equal compute depth. Mathematical tokens, rare words, and complex reasoning steps need more cycles through the shared block; common tokens can exit early. The router learns this allocation from scratch during pretraining.

## Architecture

**Recursion block:** A shared stack of transformer layers applied $N_r$ times (configurable: 2, 3, or 4 recursions). Each recursion uses identical parameters $\Phi'$.

**Routing strategies:**

- **Expert-choice:** Each recursion depth selects its top-$k$ tokens via learned router scores. Hierarchical filtering: only tokens selected at step $r$ are candidates at step $r+1$. Guarantees load balance but has causality leakage during training.
- **Token-choice:** Each token commits to a full recursion depth upfront via top-1 gating over a softmax. No causality leakage but requires balancing loss.

**KV caching strategies:**

- **Recursion-wise caching:** Cache KV pairs only for tokens active at each depth. Memory scales as $(N_r + 1) / 2N_r$ of vanilla. Attention FLOPs scale as $(k/N_{\text{ctx}})^2$ per layer.
- **Recursive sharing:** Cache KV only at first recursion, reuse across all depths. Memory scales as $1/N_r$. Higher KV I/O but maximal memory savings.

**Parameter sharing:** "Middle-Cycle" strategy — unique first and last layers, shared middle layers cycled across recursions — consistently outperforms alternatives.

## Results

At 360M scale with $N_r = 2$, expert-choice routing, recursion-wise caching:

- **Lower validation loss** than vanilla Transformer (2.7511 vs. 2.7824) with **47% fewer parameters** (167M vs. 315M)
- Processes **35% more training tokens** within same FLOP budget (27B vs. 20B)
- **2.06× inference throughput** via continuous depth-wise batching (at $N_r = 4$)
- Scales favorably: gap with vanilla closes at 360M+ parameters, MoR matches or exceeds vanilla at higher compute

## Connection to EML-Transformer Architecture

Gemini identified this as the critical architectural component for the [[eml-operator]] compiled transformer (see `eml_transformer_architecture.md`). The mapping:

| MoR Component | EML-Transformer Role |
|---|---|
| Shared recursion block | The EML ALU — one physical block computing $\exp(a) - \ln(b)$ |
| Router | Control flow — determines recursion depth per token based on EML tree depth |
| Recursion depth $N_r$ | EML tree depth $D$ — how many EML steps this token requires |
| Expert-choice hierarchical filtering | Natural fit: deeper EML nodes only execute if parent nodes completed |
| Recursion-wise KV caching | Matches register allocation — only cache slots for live variables at current depth |
| Continuous depth-wise batching | Tokens at different EML computation stages share the same ALU parameters |

**Key efficiency gain:** Instead of $\lceil D/2 \rceil$ physical layers for depth-$D$ trees, MoR requires **one physical EML block** that loops $D$ times. A single block handles exp(x) (1 cycle), ln(x) (3 cycles), and multiplication (10 cycles) — all sharing parameters.

**The router as MOP's α/β tradeoff:** The router's learned allocation of compute depth per token is structurally equivalent to [[maximum-occupancy-principle]]'s action selection: tokens requiring deep computation (high β — more state exploration) get more cycles; trivial tokens (low β) exit early. The balancing loss in token-choice routing prevents the MOP absorbing state of all tokens taking maximum depth (which would waste compute on trivial predictions).

## Connections

- [[eml-operator]] — MoR provides the dynamic-depth execution substrate for compiled EML programs
- [[maximum-occupancy-principle]] — router allocation = MOP α/β tradeoff; balancing loss = absorbing state avoidance
- [[transformer-vm-moran-2026]] — MoR extends the compiled-transformer paradigm from fixed-depth to adaptive-depth
- [[alphaevolve]] — could evolve optimal router configurations and recursion strategies
- [[minimal-generative-architectures]] — MoR adds dynamic depth to the MGA pattern: same primitive, variable recursion count
- [[llm-kernel-optimization]] — continuous depth-wise batching parallels GPU kernel optimization (maximizing hardware utilization)
