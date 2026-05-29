---
summary: Combines ELHSR hidden-state scoring (outcome-level, lightweight) with SD-Search process signals (step-level, self-distilled) for BoN guidance
tags: [reward-modeling, inference-time-compute, hidden-states, process-reward, best-of-n]
updated: 2026-05-25T20:22:04Z
created: 2026-05-25T20:22:04Z
---

# Hybrid Reward Models: Combining Hidden-State and Process-Level Signals

An emerging design pattern that combines lightweight hidden-state reward scoring (ELHSR-style) with process-level signals (SD-Search-style) to guide Best-of-N sampling. The goal is to get step-level pruning efficiency from process signals and outcome-level reranking quality from hidden-state scoring — in a single unified pipeline.

## Definition

A **hybrid reward model** combines two complementary reward signal sources:

1. **Hidden-state outcome scoring** (ELHSR-style): A lightweight linear probe over concatenated LLM hidden states that produces a single trajectory-level reward $R_{HS}$ — the same architecture as ELHSR, applied at trajectory-completion. Computational cost: ~270K parameters, <0.005% of a 7B reward model.

2. **Process-level step signals** (SD-Search-style): Self-distilled implicit process supervision from the policy's own token distributions under a hindsight-conditioned teacher. Yields per-step JSD-based signals $\{r_1^{proc}, r_2^{proc}, ..., r_T^{proc}\}$ that enable intelligent pruning of reasoning branches before trajectory completion.

The combination enables **adaptive BoN with process-guarded beam search**:
- SD-Search process signals: prune bad reasoning paths early (cheap, saves inference compute)
- ELHSR hidden-state score: rerank surviving complete trajectories (outcome-level quality signal)

## Motivation

ELHSR and SD-Search each solve half of the BoN problem:

| Signal Type | What it provides | Limitation |
|---|---|---|
| ELHSR hidden-state (outcome) | Cheap trajectory-level score for reranking | Scores only at completion — no early pruning |
| SD-Search process (step-level) | Per-step quality signal for beam pruning | Implicit signal; no final outcome confidence score |

Neither alone is sufficient for efficient inference-time scaling:
- Pure BoN with ELHSR: generates N complete trajectories, scores each, picks best. Wasteful when most candidates fail early.
- SD-Search alone: gives step-level pruning but lacks a final outcome confidence score — it knows *which steps were good* but not *how confident the model is that the trajectory will land correctly*.

A hybrid closes the loop: SD-Search prunes to top-k paths at each step using process signals; ELHSR scores each completed trajectory for reranking.

## Architecture: Two-Stage Hybrid

```
Input problem
    ↓
[SD-Search Process Stage]
    ├─ Generate N candidate paths with beam width b
    ├─ At each step i: compute JSD process signal rᵢproc between student/teacher
    ├─ Prune beams where rᵢproc < threshold τ → keep top-b surviving paths
    └─ Continue until all remaining beams reach terminal state or pruning kills them
    ↓
[ELHSR Outcome Stage — parallel scoring of remaining candidates]
    ├─ For each surviving trajectory: extract hidden states at token level
    ├─ Apply lightweight linear projection → R_HS trajectory score
    └─ Select trajectory with highest R_HS
    ↓
Output best trajectory
```

### Design Alternatives

**Option A — Sequential (prune-then-score)**: SD-Search prunes to a small candidate set (e.g., top-4 of 16 beams), ELHSR scores remaining for final selection. Most compute-efficient; risks pruning the correct path if process signals misjudge a step.

**Option B — Parallel scoring**: Generate N trajectories without early pruning, compute both ELHSR outcome scores and SD-Search process signals, use process signals for weighted aggregation in BoN selection. More robust but eliminates early pruning savings.

**Option C — Unified linear probe**: A single linear layer over hidden states that outputs both a step-level process score $r_t^{proc}$ and a gated outcome score $R_{HS}$. In this design ELHSR's gating mechanism (which identifies high-signal tokens) doubles as a process signal — tokens with high gating values $g_t$ indicate confidence at that reasoning step. This would be a direct extension of ELHSR's architecture rather than a two-stage system.

## Implementation Notes

### Deriving Process Signals from Hidden States (Option C)

ELHSR's gating mechanism is already step-aware: the per-token gating weights $\{g_t\}$ reflect the model's confidence in token-level reward estimation. In the original ELHSR paper, these are used to weight token-level rewards when aggregating to a trajectory score. 

The extension to process-level is straightforward: treat $g_t \cdot r_t$ as an implicit per-step confidence signal. High $g_t$ means the hidden states at token $t$ strongly endorse the current reasoning direction; this can serve as a process signal analogous to SD-Search's JSD, but without the hindsight-distillation overhead.

Formally, for a trajectory composed of hidden states $h_1, ..., h_T$ and ELHSR gates $g_1, ..., g_T$:
- Process signal at step $t$: $s_t^{proc} = g_t \cdot r_t$ (or just $g_t$ if normalized)
- This requires no additional teacher rollouts — it comes from the same forward pass as outcome scoring.

### Hindsight Block Construction (SD-Search Component)

SD-Search constructs a hindsight block by conditioning a "teacher" variant of the model on the final outcomes of sibling rollouts. The JSD between student and teacher distributions at search-query token positions is the process reward.

For a hybrid, the key question is whether SD-Search's hindsight block is needed separately, or whether the ELHSR hidden states already encode equivalent step-level information. The empirical question is open:
- SD-Search's JSD captures *which decisions were correct given the final outcome* — a counterfactual step-level signal
- ELHSR's gating captures *which internal representations are being trusted for the current token prediction* — an epistemic confidence signal

These are related but not identical. No published paper yet compares them directly.

## Key Research Questions

1. **Correlation between $g_t$ and correctness**: Does ELHSR's per-token gating actually track step-level correctness, or does it just weight information density for outcome prediction? Probing studies on mathematical reasoning traces would validate this.

2. **Process signal reliability at scale**: The fundamental PRM reliability problem applies to hidden-state process signals too — a bad step-level confidence estimate can cause the search to prune the correct path. Can we validate hidden-state process signal quality without expensive human annotation?

3. **Hybrid vs weighted ensemble**: Instead of sequential prune-then-score, a weighted ensemble that combines SD-Search's JSD signal and ELHSR's gating signal into a single per-step score may outperform either alone. The combination could be $r_t^{hybrid} = \alpha \cdot JSD_t + (1-\alpha) \cdot g_t$, with $\alpha$ learned.

4. **Domain transfer**: Both ELHSR and SD-Search are evaluated primarily on mathematical reasoning. Does the hybrid approach transfer to code generation, scientific reasoning, or multi-hop QA?

5. **Self-distillation vs probe**: The SD-Search process signal requires running multiple rollouts to construct the hindsight block. Is there a way to derive equivalent signals from a single forward pass using hidden states, bypassing the rollout overhead?

## Relationship to Existing Concepts

- [[process-reward-model]]: PRM is the broader concept — hybrid is a specific architecture instantiating a PRM using hidden states
- [[ELHSR]]: Hidden-state scoring component — provides outcome-level reranking signal
- [[SD-Search]]: Process-level signal source via self-distillation; hybrid could adopt SD-Search's hindsight block construction rather than using hidden-state gating
- [[inference-time-compute-scaling]]: Hybrid is an inference-time scaling architecture; BoN guidance is the primary application
- [[reward-hacking]]: Combined signals provide defense-in-depth against reward hacking — process signals catch step-level gaming, outcome signals catch trajectory-level gaming

## Open Questions

1. Can ELHSR's gating mechanism serve as a valid proxy for SD-Search's JSD process signal without additional rollout overhead?
2. What is the optimal balance between prune aggressiveness (SD-Search) and reranking confidence (ELHSR)?
3. Is there a training regime that jointly optimizes the hybrid, rather than training components separately?
4. Does the hybrid reduce the "distillation ceiling" problem that affects explicit PRM approaches?

## Related
- [[concepts/process-reward-model]]
- [[wiki/index]]
- [[concepts/hybrid-reward-models]]
- [[concepts/reward-hacking]]
- [[log]]
- [[concepts/inference-time-compute-scaling]]

- [[hybrid-reward-models]]

## Sources

- ELHSR: arXiv:2505.12225v1 — Efficient Linear Hidden State Reward
- SD-Search: arXiv:2605.18299v1 — On-Policy Hindsight Self-Distillation for Search-Augmented Reasoning
- SWIFT (concurrent work): arXiv:2505.12225v3 — related hidden-state reward approach
- Process Reward Models: arXiv:2605.18299, arXiv:2605.15177
