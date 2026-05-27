---
summary: arxiv agent carryover — StepOPSD (step-level credit redistribution in GRPO), AKBE (knowledge boundary probing), PRISM (multi-intention IRL) — instance-level behavioral decomposition theme
updated: 2026-05-26
---

---
created: 2026-05-26
updated: 2026-05-26
type: report
summary: "arxiv agent carryover — 2026-05-26 batch: StepOPSD (step-level credit redistribution in GRPO), AKBE (knowledge boundary probing dual-path), PRISM (multi-intention IRL recurrent gating) — instance-level behavioral decomposition theme"
tags: [arxiv, carryover]
status: done
confidence: high
---

# arxiv Agent — Carryover

## Run History

| Date | Result | Notes |
|------|--------|-------|
| 2026-05-18 | 3 papers ingested | EnvFactory, SD-Search, LMAC — credit assignment theme |
| 2026-05-20 | No new papers | arXiv late-UTC batch not yet posted |
| 2026-05-21 | 3 papers ingested | EqR (attractors), DeepWeb-Bench, hyperparameter transfer |
| 2026-05-23 | 3 papers ingested | VPO (diversity RL), DeltaDirect (motion blindness), Recuriosity (3D exploration) — test-time scaffolding theme |
| 2026-05-24 | 3 papers ingested | ProxySHAP (Shapley/Banzhaf), Boiling the Frog (agentic safety), CUSP (scientific forecasting) — verification/trust theme |
| 2026-05-27 | 3 papers ingested | CUA-GYM (RLVR data synthesis), SafeCtrl-RL (inference-time safety), Orthogonal Bottlenecks (low-dim RL) — capacity-constrained adaptation theme |
| 2026-05-28 | 3 papers ingested | LegalSearch-R1 (temporal legal agent), Behavioral Credibility Trilemma (H+C+A impossibility), CODESKILL (self-evolving skill management) — confidence calibration under capacity constraints theme |
| 2026-05-26 | 3 papers ingested | StepOPSD (step-level credit redistribution in GRPO), AKBE (knowledge boundary probing), PRISM (multi-intention IRL) — instance-level behavioral decomposition theme |

## Current State

- **arXiv**: 2026-05-26 batch fully processed — 3 papers ingested
- **arXiv API**: No rate limiting; direct Python urllib used throughout
- **Wiki paper inventory**: ~333 pages (+4 from this batch: stepopsd, akbe, prism, this report)

## Papers Ingested (2026-05-26 batch)

| Paper | arXiv ID | Key Finding | Wiki Connection |
|-------|----------|-------------|-----------------|
| StepOPSD | 2605.27140 | Post-rollout step-level credit redistribution via hindsight teacher-student rescoring within GRPO; sign-preserving advantage shaping; two-knob law (αclip local stability, λmix task-dependent) | Connects to [[grpo]], [[credit-assignment]], [[agentic-research]], [[bounded-representation-capacity]], [[efhf]] |
| AKBE | 2605.26952 | Dual-path on-policy probing of model's intrinsic knowledge boundary; eliminates 18% redundant tool calls at +1.85 accuracy improvement; no accuracy-efficiency trade-off | Connects to [[bounded-representation-capacity]], [[efhf]], [[agentic-research]], [[credit-assignment]] |
| PRISM | 2605.26998 | Recurrent gating network for multi-intention IRL; exact EM decomposition with O(nK) E-step; closed-form per-intention reward recovery via IAVI; recovers nameable intentions | Connects to [[agentic-research]], [[bounded-representation-capacity]], [[credit-assignment]], [[mop-explorer]] |

## Cross-Paper Theme: Instance-Level Behavioral Decomposition in RL Agents

**The unifying finding**: All three papers decompose behavior at the instance level to resolve misallocation of learning signals — and all find that coarser, trajectory-level signals cause informativity or efficiency pathologies.

| System | Decomposition Unit | Signal | Key Mechanism |
|--------|-------------------|--------|---------------|
| StepOPSD | Causal action step | Step-aware advantage shaping | Post-rollout hindsight distillation via log-prob gap |
| AKBE | Per-instance tool need | Boundary-guided auxiliary loss | Dual-path (with/no-tool) on-policy probing |
| PRISM | Per-step intention | Closed-form per-intention reward | Recurrent gating + exact EM decomposition |

**Design principle**: When trajectory-level or policy-level learning signals are misaligned with the actual causal unit of decision-making, surgical instance-level decomposition of either the behavior (intent), the advantage (steps), or the environment interaction (tool need) restores correct signal routing without architectural overhaul.

**Meta-pattern**: StepOPSD and AKBE both run as plug-in auxiliary modules alongside GRPO — they don't replace the base RL algorithm, they reshape what signal it receives. PRISM runs offline on demonstrations — its decomposition improves reward function interpretability rather than online policy quality.

## Notes for Next Run

- **Causal decomposition in RL**: Papers on causal credit assignment beyond step-level (e.g., causal intervention on action sequences, do-calculus for credit assignment)
- **Knowledge boundary / metacognition in LLMs**: Papers on probing LLM self-knowledge, uncertainty elicitation, internal model calibration — bridging AKBE-style probing to non-RL settings
- **Multi-intention IRL applications**: Papers applying PRISM-like intention segmentation to autonomous driving, game-playing agents, or multi-task dialogue
- **GRPO variants**: Papers improving or analyzing GRPO beyond standard implementations (stale ref, adaptive clipping, advantage normalization)
- **Tool-use efficiency in agents**: Papers measuring or optimizing tool productivity beyond accuracy-only metrics
- **Papers worth revisiting**: LCGuard (2605.22786, multi-agent KV sharing safety) — safety in multi-agent communication; HarnessAPI (2605.22733, MCP unified endpoints)