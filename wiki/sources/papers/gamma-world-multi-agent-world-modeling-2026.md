---
summary: Gamma-World: Multi-agent video world model with permutation-symmetric agent encoding and linear cross-agent attention
tags: [world-models, multi-agent, video-generation, permutation-symmetry, nvidea]
updated: 2026-05-28T14:13:21Z
created: 2026-05-28T14:13:21Z
---

---
created: 2026-05-28T00:00:00Z
updated: 2026-05-28T00:00:00Z
type: source
summary: "Gamma-World: Multi-agent video world model using Simplex Rotary Agent Encoding (permutation-symmetric, parameter-free) + Sparse Hub Attention (linear cross-agent cost) — enables real-time 24-FPS multi-player simulation."
tags: [world-models, multi-agent, video-generation, permutation-symmetry, nvidea]
sources: https://arxiv.org/abs/2605.28816
status: active
confidence: high
---

# Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players

**arXiv**: [2605.28816](https://arxiv.org/abs/2605.28816) | May 27, 2026  
**Authors**: Fangfu Liu, Kai He, Tianchang Shen, Tianshi Cao, Sanja Fidler, Yueqi Duan, Jun Gao, Igor Gilitschenski, Zian Wang, Xuanchi Ren (NVIDIA + Tsinghua + U Toronto)

## Core Finding

**Gamma-World** — a generative multi-agent world model that handles arbitrary numbers of agents with permutation symmetry, linear cross-agent attention cost, and real-time 24-FPS rollout. Key innovation: Simplex Rotary Agent Encoding places agents at simplex vertices in rotary angle space, enabling parameter-free agent identity that generalizes from 2 to 4 players without retraining.

## Architecture

### Simplex Rotary Agent Encoding

Standard 3D RoPE extended with explicit agent axis. Agents are placed at vertices of a regular simplex in rotary angle space:
- All agents at equal pairwise distances → permutation-equivalent
- Each agent retains distinct rotary phase → individually controllable
- Parameter-free: no learned per-slot identities, no fixed ordering
- Generalizes from N to M agents without architecture change

### Sparse Hub Attention

Dense all-to-all cross-agent attention is quadratic. Hub attention:
- Learnable hub tokens mediate token interaction across agents
- Agent tokens attend to their own stream + hub tokens
- Cross-agent cost: O(agents) instead of O(agents²)
- Preserves shared communication pathway without dense pairwise interaction

### Real-Time Distillation

- Bidirectional teacher → block-causal student with KV caching
- Causal temporal blocks with autoregressive generation
- **24 FPS** interactive rollout responding to newly issued actions

## Problem with Prior Work (Solaris)

- Dense joint attention over all agent tokens: quadratic cost, restrictive for >2 players
- Learned per-slot ID embedding: violates permutation symmetry, ties model to fixed roster
- Cannot extend beyond trained agent count without retraining

## Results

Multiplayer virtual environments (2 and 4 players, movement/mining/combat/building):

| Metric | Gamma-World vs Slot-based | Gamma-World vs Dense-attention |
|--------|--------------------------|-------------------------------|
| Video fidelity | + | + |
| Action controllability | + | + |
| Inter-agent consistency | + | + |
| Generalization 2→4 players | No retraining needed | — |

## Related Concepts

- [[cognitive-world-models-for-llm-agents]] — world modeling thread in wiki
- [[permutation-symmetry]] — fundamental property of multi-agent systems
- [[sparse-attention]] — hub attention efficiency mechanism
- [[world-models]] — general research thread

## Connections

- Extends [[recuriosity-episodic-context-3d-exploration-2026]] — both address multi-agent simulation in shared environments
- Permutation symmetry connects to [[envfactory-2026]] — learned environments need to support multiple agents with consistent physics
- Real-time 24-FPS generation relates to interactive simulation needs in agent training
