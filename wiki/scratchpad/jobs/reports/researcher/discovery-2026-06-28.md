---
created: 2026-06-28
updated: 2026-06-28
type: report
summary: Discovery cycle — power law scaling, Taylor's law, allometric scaling, LLM inference; 4 stubs upgraded to active
tags: [researcher, discovery, report]
---

# Researcher Discovery Report — 2026-06-28

## Discovery Cycle
- Topics researched: 4 (power law scaling, Taylor's law, allometric scaling, LLM inference)
- New pages created: 0
- Pages updated: 4 (power-law-scaling, taylors-law, allometric-scaling, llm-inference — all upgraded from stub → active)
- Cross-links added: ~20 (wikilinks across scaling cluster and inference stack)
- Stubs remaining: 174 (Jun 28 count after 3 upgrades)

## New Entries

### power-law-scaling (UPGRADED: stub → active)
Upgraded from stub with substantive content:
- Mathematical form: f(x) = ax^k, scale-invariance, exponent-driven classification
- Neural scaling law form with Kaplan/Chinchilla coefficients
- Allometric scaling connection (Kleiber's law as biological analog)
- Taylor's law connection (ecological variance-mean relationship)
- Neural network applications: loss landscape variance, feature scaling in SAEs
- 4 open questions, limitations section

### taylors-law (UPGRADED: stub → active)
Upgraded from stub to full concept:
- Ecological origin: Taylor 1961, variance-mean power law for population densities
- Exponent interpretation table: k≈1 (random), k≈1.5 (intermediate clustering), k≈2 (contagious)
- Neural network connection: loss variance across random initializations follows Taylor's law (k≈1.5–2)
- Practical applications: seed count estimation, generalization variance prediction, phase transition detection
- 4 open questions

### allometric-scaling (UPGRADED: stub → active)
Upgraded from stub to full concept:
- Definition: biological trait scaling with body mass (T ∝ M^k)
- Kleiber's law: B ∝ M^0.75, West-Brown-Enquist fractal network theory
- Allometric table: heart rate, lifespan, brain mass, running speed exponents
- Neural network analogies: width-depth scaling, attention head scaling, circuit complexity
- Fractal network hypothesis as unifying mechanism
- 4 open questions

### llm-inference (UPGRADED: stub → active)
Upgraded from stub with substantial content:
- 5-layer inference stack (autoregressive generation → KV cache → batching → serving)
- NAMM (Neural Attention Memory Models): learned KV cache management replacing heuristic rules
- Speculative decoding: draft model + verification, 2-4× speedup typical
- Batching strategies: static, continuous, chunked prefill
- Quantization: AWQ, GPTQ, KV cache FP8
- Economics table: error cost vs compute strategy mapping
- 4 open questions

## Updated Entries
N/A — all 4 were upgrades from existing stubs

## Gap Analysis
**Cluster filled this cycle: power law / scaling cluster**
- power-law-scaling: upgraded (hub connecting scaling-laws, power-law, taylor/allometric)
- taylors-law: upgraded (connects to power-law-scaling and scaling-laws)
- allometric-scaling: upgraded (connects to taylors-law and power-law-scaling)
- llm-inference: upgraded (connects to kv-cache, namm, inference-time-compute-scaling)

**Remaining priority stubs** (from carryover Heading):
- llm-reasoning: stub with chain-of-thought and large-language-models links — evaluate for upgrade
- llm-training: mentioned in carryover but file doesn't exist — likely need to create
- model-serving: listed in stub list — evaluate for upgrade vs deletion
- Coordination stubs: coordination.md, multi-agent-coordination.md — check for duplicate content

**Stub count: 174** (down from 175 after this cycle's 3 upgrades + 0 deletions)

## Related
- [[index]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-06-28]]

- [[discovery-2026-06-28]]

## Open Questions
- **MoE routing collapse under RLHF**: Resolved — Empirically confirmed via SafeMoE (Kim 2025)
- **Adaptive budget learning**: No clear paper yet — open
- **Hybrid reward models (ELHSR + SD-Search)**: Emerging direction, no full treatment — open
- **Reward hacking detectability**: No reliable early-warning signal — open
- **Cognitive world models for LLM agents**: Filled this cycle (Jun 26 report)
- **MOP training for transformers**: Stub exists (mop-next-token-prediction.md) — open research direction
- **Category theory + neural network verification**: Filled (attention-monoidal-closure, Jun 27) — resolved