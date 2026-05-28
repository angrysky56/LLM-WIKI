---
created: 2026-06-09
updated: 2026-06-27
type: report
summary: Researcher discovery report
tags: [researcher, report]
---

# Researcher Discovery Report — 2026-06-09

## Discovery Cycle
- Topics researched: 9
- New pages created: 9 (converted from stubs)
- Pages updated: 0
- Cross-links added: ~40+

## New Entries (Stub → Active Conversions)

### Transformer Infrastructure Cluster (3 pages) — Complete
- **[[attention-mechanism]]**: Scaled dot-product attention, multi-head attention, Flash Attention, GQA/MQA. Core mechanism formulation, variants, and why O(1) path length matters.
- **[[transformer-architecture]]**: Encoder-decoder vs decoder-only (GPT-style). Architecture components, scaling as primary strategy, RoPE/ALiBi/GQA extensions.
- **[[kv-cache]]**: Inference optimization for autoregressive models. PagedAttention, MQA/GQA memory reduction, prefix caching. Prevents O(n²) recomputation.

### Agent Architecture Cluster (2 pages) — Elevated
- **[[autonomous-research]]**: Six-stage pipeline (idea → hypothesis → experiment → evaluation → revision → paper). Six failure modes from Trehan/Chopra. SEG Scientist architecture addresses these.
- **[[agent-leak-benchmark]]**: Reconstruction attack benchmark for multi-agent KV sharing. ASR up to 0.900 on vanilla KV sharing (LCGuard paper).

### Reasoning/Search Cluster (3 pages) — Complete
- **[[causal-reasoning]]**: SCM framework, do-calculus, counterfactuals, causal discovery algorithms (PC, FCI, NOTEARS). ELHSR hidden-state causal signals. LLM integration open questions.
- **[[MCTS]]**: Monte Carlo Tree Search with UCB1. AlphaZero architecture. Game-playing impact (Go, Chess, Shogi, Poker). Connection to process reward models and SD-Search.
- **[[evolutionary-strategies]]**: CMA-ES, natural evolution strategies. NES as likelihood-ratio gradient estimation. ML evolution applications, connection to GRPO as simplified group-relative ES.

### Security Cluster (1 page)
- **[[adversarial-training]]**: PGD/BIM attacks, adversarial training for robustness. LLM applications: jailbreaks, prompt injection, LCGuard's adversarial training for KV-cache privacy.

## Gap Analysis

**Transformer infrastructure cluster is now complete** — attention-mechanism, transformer-architecture, and kv-cache all have substantive content. These connect to the broader scaling-laws → length-generalization research thread that runs through multiple cycles.

**MCTS + causal-reasoning + evolutionary-strategies** form a coherent reasoning/search cluster — all three are optimization/decision-making methods with distinct bias profiles. MCTS uses tree search with value estimation, ES uses population-based black-box optimization, causal reasoning provides the structural model for counterfactual planning.

**Agent leak benchmark** (agent-leak-benchmark) bridges the multi-agent systems work (from earlier cycles) with the security/privacy thread. The LCGuard paper (already in sources) is the source material; now there's a concept page connecting it to the agent-onboarding thread.

**Stub count**: 134 total stubs found (note: this count includes entities, not just concepts). Remaining high-value targets include llm-agent-architecture (very thin, MOP connections), code-generation (connects to swe-bench/code-agent chain), and video-llm (thin but connects to vision-language-alignment).

## Related
- [[scratchpad/jobs/reports/researcher/discovery-2026-06-09]]
- [[index]]

- [[discovery-2026-06-09]]

## Open Questions
- **MoE routing collapse under RLHF**: is it happening in practice? No empirical data. Worth monitoring.
- **Adaptive budget learning**: how to train the gating model. No clear paper yet.
- **Hybrid reward models**: combining ELHSR (hidden-state) with SD-Search (process-level). Emerging direction — no full treatment yet.
- **Reward hacking detectability**: Is there a reliable signal that reward hacking is occurring before it becomes severe? Current approaches are post-hoc.
- **Category theory for neural network verification**: Do attention mechanisms form a closed monoidal category? Enables categorical compositional verification.
- **Cognitive world models for LLM agents**: How do you represent "what the world looks like" for a text-based agent? Conversation state? Tool return history?
- **MOP training for transformers**: Can path entropy maximization be applied to next-token prediction training from scratch?