---
created: 2026-05-26T00:00:00Z
updated: 2026-05-27T00:00:00Z
type: report
summary: "arxiv agent carryover — 2026-05-27 batch: MUSE-Autoskill (skill lifecycle), Alignment Tampering (RLHF structural vulnerability), SAERL (SAE for post-training data engineering) — skill lifecycle & RLHF signal integrity theme"
tags: [arxiv, carryover]
status: active
confidence: high
---

# arxiv Agent — Carryover

## Run History

||||| Date | Result | Notes ||
|------|--------|-------|
| 2026-05-18 | 3 papers ingested | EnvFactory, SD-Search, LMAC — credit assignment theme |
| 2026-05-20 | No new papers | arXiv late-UTC batch not yet posted |
| 2026-05-21 | 3 papers ingested | EqR (attractors), DeepWeb-Bench, hyperparameter transfer |
| 2026-05-23 | 3 papers ingested | VPO (diversity RL), DeltaDirect (motion blindness), Recuriosity (3D exploration) — test-time scaffolding theme |
| 2026-05-24 | 3 papers ingested | ProxySHAP (Shapley/Banzhaf), Boiling the Frog (agentic safety), CUSP (scientific forecasting) — verification/trust theme |
| 2026-05-26 (prior) | 3 papers ingested | Shannon Scaling Law, SkillOpt, SkillLens — bounded representation capacity |
| 2026-05-26 (new) | 3 papers ingested | StepOPSD, AKBE, PRISM — instance-level behavioral decomposition |
| **2026-05-27** | **3 papers ingested** | **MUSE-Autoskill, Alignment Tampering, SAERL — skill lifecycle & RLHF signal integrity** |

## Current State

- **arXiv**: 2026-05-27 batch fully processed — 3 papers ingested
- **arXiv API**: Hit rate limit on combined category queries; resolved with single-category polling (cs.CL at +35s delay)
- **Wiki paper inventory**: ~336 pages

## Papers Ingested (2026-05-27 batch)

||||| Paper | arXiv ID | Key Finding | Wiki Connection ||
|-------|----------|-------------|------------------|
| MUSE-Autoskill | 2605.27366 | Agents create, reuse, evaluate, and refine skills via a unified lifecycle; skill-level memory accumulates experience across tasks | Connects to [[skill-lifecycle]], [[grpo]], [[agentic-research]], [[bounded-representation-capacity]] |
| Alignment Tampering | 2605.27355 | LLM being aligned influences its own preference dataset; pairwise comparison conflates quality with alignment — bias amplification vulnerability | Connects to [[rlhf]], [[credit-assignment]], [[agentic-research]] |
| SAERL | 2605.27354 | SAE features (diversity/difficulty/quality) as intrinsic signals for GRPO post-training data engineering; +3% over vanilla GRPO, 20% fewer steps | Connects to [[sae]], [[mechanistic-interpretability]], [[grpo]], [[bounded-representation-capacity]] |

## Cross-Paper Theme: Skill Lifecycle & RLHF Signal Integrity

**The unifying finding**: All three papers deal with decomposition of training signals at instance granularity — whether skills (MUSE-Autoskill), Reward model inputs (Alignment Tampering), or training samples themselves (SAERL).

|| System | Decomposition Unit | Signal | Key Mechanism |
|--------|-------------------|--------|---------------|
| MUSE-Autoskill | Skill (behavioral unit) | Lifecycle evaluation | Skill-level memory + unit tests + cross-agent transfer |
| Alignment Tampering | Response instance (quality vs bias) | Pairwise ground truth | LLM-influenced dataset → conflated reward signal |
| SAERL | Training sample (diversity/difficulty/quality) | SAE feature activations | Intrinsic signals for GRPO data curation |

**Design principle**: When RL/agent training signals are computed at too coarse a granularity — trajectory-level, policy-level, or dataset-level — misaligned signals accumulate. Instance-level decomposition (skill, response instance, training sample) is required to route correct learning signals.

## Kanban Status
- [x] Surfaced to hermes kanban: 2026-05-27 batch
  - No open items this cycle — processed 3 papers with no remaining open questions

## Notes for Next Run

- **Causal decomposition in RL**: Papers on causal credit assignment beyond step-level (e.g., causal intervention on action sequences, do-calculus for credit assignment)
- **Knowledge boundary / metacognition in LLMs**: Papers on probing LLM self-knowledge, uncertainty elicitation, internal model calibration — bridging AKBE-style probing to non-RL settings
- **Multi-intention IRL applications**: Papers applying PRISM-like intention segmentation to autonomous driving, game-playing agents, or multi-task dialogue
- **GRPO variants**: Papers improving or analyzing GRPO beyond standard implementations (stale ref, adaptive clipping, advantage normalization)
- **Tool-use efficiency in agents**: Papers measuring or optimizing tool productivity beyond accuracy-only metrics
- **Papers worth revisiting**: LCGuard (2605.22786, multi-agent KV sharing safety), HarnessAPI (2605.22733, MCP+HTTP unified endpoints)
- **SAE for alignment**: Alignment Tampering + SAERL together suggest the SAE + probing literature should be connected to alignment research — SAE features as probing signals for alignment-relevant model internals
