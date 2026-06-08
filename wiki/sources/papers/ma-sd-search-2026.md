---
created: 2026-05-19
updated: 2026-05-20
type: source
paper_id: 2605.18299
summary: On-policy hindsight self-distillation for step-level credit assignment in search-augmented reasoning — matches 72B external-teacher baselines using only the policy's own predictions.
tags: [paper, arxiv, search-augmented-rag, step-level-credit-assignment, self-distillation, reinforcement-learning, grpo]
sources: [arXiv:2605.18299, Ma et al. 2026]
status: active
confidence: 1.0
research_threads: [search-augmented-reasoning, credit-assignment, reward-modeling, graphrag]

---

# SD-Search: On-Policy Hindsight Self-Distillation for Search-Augmented Reasoning

**Paper**: [arXiv:2605.18299](https://arxiv.org/abs/2605.18299) | Authors: Yufei Ma, Zihan Liang, Ben Chen et al. (Kuaishou Technology) | Date: 2026-05-18

## Metadata

| Field | Value |
|-------|-------|
| arXiv ID | 2605.18299v1 |
| Category | cs.AI |
| Models | Qwen2.5-3B, Qwen2.5-7B (base + instruct) |
| Benchmarks | NQ, TriviaQA, PopQA (single-hop); HotpotQA, 2Wiki, MuSiQue, Bamboogle (multi-hop) |
| Training | GRPO + on-policy hindsight self-distillation |
| External Teacher | **None** — signal derived entirely from policy itself |

## Executive Summary

SD-Search solves the **step-level credit assignment problem** in search-augmented reasoning agents. Under standard outcome-reward RL (GRPO), every token in a rollout receives the same trajectory-level advantage — individual search queries get no specific credit. SD-Search addresses this by having the **same policy serve as both student and teacher**: the student sees only the standard inference-time context; the teacher additionally sees a **hindsight block** aggregating the search trajectories and binary outcome labels (CORRECT/INCORRECT) of sibling rollouts from the same question. The teacher’s distribution over search-query tokens implicitly encodes which queries were worth making; the student is aligned via token-level Jensen-Shannon divergence at those positions.

The key result: **SD-Search-3B reaches 0.428 average EM, matching the leading process-supervision baseline Thinker (which requires a 72B external teacher) without any external resources.** At 7B, SD-Search reaches 0.476, surpassing Thinker by 2.4 points and all outcome-reward baselines. The method requires only question-answer pairs (no sub-question annotations, no distillation data from larger models) and adds ~15.5% wall-clock training overhead entirely within the standard RL loop.

## Problem: The Step-Level Credit Assignment Gap

Search-augmented reasoning agents interleave internal reasoning (THINK spans) with calls to an external retriever (SEARCH spans), using GRPO to optimize for final-answer correctness. This outcome-reward formulation leaves individual search decisions without step-specific credit:

- Every token in τᵢ receives the same advantage ˆAᵢ, regardless of whether the query was well-formed or redundant
- Trajectories with multiple hops have **within-trajectory variance in query quality** — some queries route correctly, others retrieve irrelevant passages — but the trajectory-level reward averages over this variance
- Process-supervision methods (Thinker, StepSearch) close this gap using external resources: a 72B teacher for trajectory synthesis (Thinker), or GPT-4o-generated sub-question annotations (StepSearch)

## Technical Approach

### Core Insight

> "The policy itself, once given access to how its rollouts actually unfolded and which ones succeeded, is in a much better position to judge which earlier decisions were worth making than the same policy at decision time."

The step-level signal that external methods import from a teacher can be **recovered from the policy's own predictions under an appropriately constructed hindsight context**.

### Student-Teacher Architecture

The same policy πθ operates under two conditioning views that differ only in context:

**Student View** (standard inference-time conditioning):
```
P_stu_p = πθ(· | τ<p)
```
where τ<p is the trajectory prefix available at inference time.

**Teacher View** (additionally conditioned on hindsight block h(G)):
```
P_tch_p = sg[πθ(· | h(G), τi,<p)]
```
where `sg[·]` indicates stop-gradient (teacher is a fixed target, not updated by the loss).

### Hindsight Block Construction

The hindsight block `h(G)` aggregates all G rollouts GRPO already samples for the question:
```
h(G) = {M(τj), y(τj)} for j ∈ [1..G]
```
- `M(τj)` = **future masking** — retains only SEARCH spans, discards THINK, DOCUMENTS, ANSWER spans. Prevents answer leakage: if the teacher saw downstream THINK/DOCUMENTS/ANSWER tokens, the gold answer would become extractable from the prefix and the distribution would collapse onto retrieval-skipping continuations.
- `y(τj)` = binary CORRECT/INCORRECT label, derived by thresholding F1 score at ρ=0 (any non-empty overlap counts as CORRECT). The label provides **contrast**: conditioned on CORRECT, the teacher reaffirms the query tokens that led to success; conditioned on INCORRECT, it redistributes mass away from failed queries toward patterns shared with successful siblings.

**Key design**: the teacher sees the **full group of sibling rollouts**, not just the single trajectory being supervised. This cross-rollout contrast (not label conditioning alone) is what makes the signal informative. Ablation shows:
- Removing outcome labels: −1.4 points
- Shuffling labels randomly: −2.3 points (worse than removing — random labels actively mislead)
- Correct rollouts only (no contrast): −0.7 points
- Removing multi-rollout group: −1.0 points
- Leave-one-out (excluding τi from h(G)): only −0.5 points — τi's own search spans contribute less than the cross-rollout contrast

### Token-Level Jensen-Shannon Objective

The self-distillation loss for trajectory τ:
```
L_SD(τ) = (1/|Qτ|) * Σ_{p∈Qτ} JSD(P_tch_p || P_stu_p)
```
where Qτ ⊆ Aτ are the search-query token positions (strictly between `<search>` and `</search>` tags).

JSD is the symmetric form:
```
JSD(P||Q) = 0.5 * KL(P || (P+Q)/2) + 0.5 * KL(Q || (P+Q)/2)
```

**Why JSD over KL variants or MSE:**
- **Forward KL**: mode-covering — requires student to place mass on every teacher-supported token, preventing sharp commitment even when teacher is highly concentrated → slight entropy blunting
- **Reverse KL**: mode-seeking — collapses student onto teacher's single highest-probability token, foreclosing exploration → worse on multi-hop where multiple near-equivalent query reformulations are viable
- **MSE**: treats every logit coordinate equally, ignoring probability-simplex structure; small shifts on irrelevant tokens penalized as heavily as shifts on high-probability query tokens
- **JSD**: symmetric (avoids bias toward mode-seeking or mode-covering), bounded by log 2 (empirically improves training stability when distributions diverge sharply in early training)

The distillation loss is added to GRPO without modifying its advantage estimator:
```
L_total = L_GRPO + α_SD * L_SD
```
α_SD = 10⁻³, Twarm = 50 steps, top-k = 50 for distribution truncation.

**Warmup**: At training start, the policy hasn't learned the structured format — rollouts contain few well-formed queries. Distilling from these noisy trajectories injects signal rather than noise. α_SD is held at zero for Twarm = 50 steps.

**Scope restriction to Qτ**: Ablation shows broadening to all policy-generated positions Aτ costs −0.7 points. At think/answer positions, the teacher's distribution is shaped by outcome labels in h(G), pushing it toward overly confident continuations that short-circuit reasoning chains.

### Training Dynamics

SD-Search's gain comes from **query quality**, not search volume. After Twarm:
- Validation EM and search quality (fraction of retrieved documents containing gold answer) diverge upward from AutoRefine
- Search frequency (average search calls per rollout) remains nearly identical between SD-Search and AutoRefine
- Teacher-student entropy gap drops from ~0.25 (pre-warmup) to ~0.065 by step 200 — expected steady state since teacher has information student cannot recover

## Key Results

### 3B Scale

| Method | External Teacher | Avg EM |
|--------|-----------------|--------|
| AutoRefine-Base | — | 0.405 |
| MR-Search-Base | — | 0.414 |
| Thinker-Instruct | Qwen2.5-72B | 0.430 |
| **SD-Search-Base** | **None** | **0.428** |
| SD-Search-Instruct | None | 0.427 |

SD-Search matches Thinker without any external teacher, surpassing AutoRefine by +2.3 points.

### 7B Scale

| Method | External Teacher | Avg EM |
|--------|-----------------|--------|
| AutoRefine-Base | — | 0.455 |
| Thinker-Instruct | Qwen2.5-72B | 0.452 |
| **SD-Search-Instruct** | **None** | **0.476** |
| SD-Search-Base | None | 0.471 |

SD-Search surpasses every baseline at 7B. Gains concentrated on multi-hop benchmarks: HotpotQA +2.0, MuSiQue +3.5 over AutoRefine-Base.

### Scaling Behavior (1.5B → 14B)

Thinker's gain over AutoRefine shrinks monotonically: +3.7 (1.5B) → +2.4 (3B) → −0.3 (7B) → −0.5 (14B). As the student approaches the 72B teacher, distillation from a fixed external reference becomes a ceiling.

SD-Search's gain stays positive at every scale: +2.5 (1.5B) → +2.3 (3B) → +2.1 (7B) → +0.9 (14B). Because the teacher is produced by the student itself, it scales with the student's in-context reading capacity rather than against a fixed reference.

## Connection to EFHF/AGEM/MOP

### Step-Level Credit Assignment → Reward Modeling

SD-Search addresses the same credit assignment problem as [[concepts/reward-modeling]] but does so **without a separate reward model**. Where traditional reward modeling trains a secondary model (often 7B-13B parameters) to score outputs, SD-Search extracts step-level reward signal from the generator's own token distributions under hindsight conditioning. The token-level JSD functions as an implicit process reward model (PRM), identifying which search-query tokens within a trajectory were worth making — without the overhead of a separate RM.

The binary CORRECT/INCORRECT outcome labels attached to each rollout in the hindsight block function similarly to outcome reward models (ORMs), but derived from gold-answer F1 scores rather than a learned model.

### Hindsight Self-Distillation → On-Policy Distillation

The student-teacher asymmetry mirrors on-policy distillation: the policy generates the data it learns from, but the conditioning asymmetry (student sees only prefix, teacher additionally sees hindsight block) prevents the degenerate self-copying that would occur if the teacher saw the exact same context as the student. The stop-gradient on P_tch_p ensures the teacher is a fixed target; only the student is updated.

### Future Masking → GraphRAG Edge Pruning

The future masking operator M (retaining only SEARCH spans, discarding THINK/DOCUMENTS/ANSWER) functions analogously to GraphRAG's edge pruning: both strip downstream/derivational content to preserve only the structural relation between query and outcome. In GraphRAG, this prevents the graph from being dominated by transitive paths; in SD-Search, it prevents the teacher from conditioning on answer-extractable content.

The multi-rollout hindsight block, which aggregates search spans across G rollouts with outcome labels, has structural parallels to a graph where nodes are search queries and edges are annotated with success/failure signals — the teacher traverses this graph to assess query quality, analogous to how GraphRAG traverses entity-relation graphs to ground answers.

### Contrastive Signal → Multi-Agent Credit Distribution

The CORRECT/INCORRECT contrast across sibling rollouts is conceptually analogous to AGEM's multi-agent credit assignment: both distribute reward signals across a population (AGEM across molecular agents, SD-Search across rollouts from the same question) to distinguish productive from unproductive behavioral patterns.

## Key Quotes

> "The policy itself, once given access to how its rollouts actually unfolded and which ones succeeded, is in a much better position to judge which earlier decisions were worth making than the same policy at decision time."

> "The hindsight block aggregates all rollouts that GRPO already samples for the question. For each τj, it contains a masked view M(τj) that retains only the search spans of τj, together with a binary outcome label y(τj) ∈ {CORRECT, INCORRECT}."

> "We choose JSD over forward or reverse KL for two reasons. It is symmetric, thus avoiding biasing the student toward either mode-seeking or mode-covering behavior, and it is bounded by log 2, which empirically improves training stability."

> "The multi-rollout group is designed to keep the hindsight signal informative when the current rollout τi fails. The outcome contrast in the hindsight block degenerates whenever the group becomes label-homogeneous in either direction."

## Limitations

1. **Gold-answer dependency**: The hindsight contrast relies on binary outcome labels derived from gold answers (inherited from GRPO), restricting SD-Search to tasks with reliably scorable references. Open-ended generation requires a substitute — e.g., learned preference score or majority-vote proxy.

2. **Group-homogeneous degeneracy**: When all G rollouts end CORRECT (all-succeed regime, more frequent at 14B where base success rates are higher), the CORRECT/INCORRECT contrast narrows and SD-Search's gain shrinks. When all rollouts end INCORRECT (all-fail regime), GRPO's trajectory-level advantages also collapse. Designing a hindsight construction that remains informative under both scenarios is open.

## Computational Cost

- End-to-end wall-clock: 11.9h (SD-Search) vs 10.3h (AutoRefine) on 8×H800, 3B — **+15.5% overhead**
- Per-step breakdown: ~94% of overhead from SD-Search compute (+22.0%) and SD-Search backward (+17.5%); rollout, reward, PPO stages unchanged
- Inference cost: **unchanged** — teacher forward pass is training-only; at inference time, the two roles collapse back into a single policy

Compared to process-supervision baselines:
- **Thinker**: Runs Qwen2.5-72B inference over the full training set (generating sub-question decompositions), then performs supervised fine-tuning on the resulting trajectories before RL. 72B forward pass alone is ~24× per-token cost of SD-Search's 3B teacher pass.
- **StepSearch**: Relies on GPT-4o API calls for sub-question annotations on ~100k-example training set — wall-clock and monetary costs scale directly with dataset size.

SD-Search trades these multi-stage external pipelines for a single in-loop overhead.

## Related Methods

- **Search-R1** [Jin et al. 2025]: Search-during-think paradigm with GRPO; SD-Search inherits trajectory format and GRPO outer loop
- **AutoRefine** [Shi et al. 2025]: Outcome-reward RL with stronger reward shaping; SD-Search's primary baseline
- **Thinker** [Xu et al. 2025]: 72B teacher for sub-question decomposition; SD-Search matches without external teacher
- **StepSearch** [Wang et al. 2025]: GPT-4o sub-question annotations; SD-Search surpasses on every multi-hop benchmark
- **GiGPO** [Feng et al. 2025]: Exploits repeated environment states for step-level advantage groups; structural rather than self-distillation based

## Connections
- [[concepts/sd-search]]
- [[wiki/index]]
- [[sources/papers/ma-sd-search-2026]]
- [[ma-sd-search-2026]]

- Concept: [[concepts/reward-modeling]] — step-level vs trajectory-level reward
- Concept: [[rag]] — search-augmented reasoning context
- Concept: [[graphrag]] — structural parallel to hindsight block aggregation
- Concept: [[chain-of-thought]] — reasoning trace structure
- EFHF: Step-level credit assignment relevant to multi-agent credit distribution
- AGEM: Rollout-group contrast analogous to population-level credit assignment
