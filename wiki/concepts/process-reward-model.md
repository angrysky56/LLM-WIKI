---
created: 2026-05-21T08:30:00Z
updated: 2026-05-21T08:30:00Z
type: concept
summary: Reward models that evaluate individual reasoning steps rather than final outcomes — enabling precise credit assignment and intelligent path pruning
tags: [reward-modeling, reasoning, credit-assignment, process-reward, llm-training]
status: active
confidence: 0.88
sources: https://arxiv.org/abs/2605.18299, https://arxiv.org/abs/2605.15177
---



# Process Reward Models

A specialized form of reward modeling that evaluates each individual step within a reasoning trace, rather than scoring only the final outcome. Enables precise credit assignment and intelligent search pruning — the critical enabler for test-time compute scaling beyond Best-of-N.

## Definition

**Process Reward Models (PRMs)** assign scalar scores to intermediate reasoning steps, not just final answers. Where an **Outcome Reward Model (ORM)** produces a single score at trajectory completion, a PRM produces a sequence of step-level scores:

```
Trajectory: [Step_1 → Step_2 → Step_3 → ... → Step_n → Answer]
PRM:       [r_1,   r_2,   r_3,   ...,   r_n]  (step scores)
ORM:       [
--R]  (single final score)
```

This step-level granularity enables:

1. **Intelligent path pruning**: If Step_3 scores poorly, the search can terminate that branch early rather than completing N full trajectories
2. **Focused credit assignment**: Learning signals can be directed precisely to the steps that caused success or failure
3. **Coarse-to-fine reasoning**: Easy steps get low compute; hard steps get more search depth

## The Credit Assignment Problem

The fundamental challenge PRMs solve is **credit assignment** — determining which decisions in a reasoning chain actually caused the final outcome.

Consider a 20-step mathematical proof. The final outcome reward is binary (correct/incorrect). But:
- Steps 1–15 might be solid
- Step 16 introduced a faulty algebraic manipulation
- Steps 17–20 then built on the error

A trajectory-level ORM says "the proof is wrong" but provides no signal about *where* the error occurred. A PRM says "Step 16 is the problem" — enabling targeted correction.

**SD-Search** (arXiv:2605.18299) provides the most compelling recent demonstration: it sidesteps the need for a separate PRM by using the policy's own token distributions under a "hindsight block" as an implicit step-level signal. The JSD between student and teacher distributions at search-query token positions functions as a process reward without any external PRM.

## Technical Implementation

### Training Data for PRMs

PRMs require step-level annotations, which are expensive to produce:

1. **Human annotation**: Expert labelers mark each step as correct/incorrect. Expensive, slow, bottlenecks every model version.

2. **Synthetic annotation via larger teacher**: Thinker (Xu et al., 2025) uses a 72B model to generate step-level labels, then trains a smaller PRM. But this requires a 72B teacher and the distillation ceiling problem: as the student approaches the teacher, distillation gains shrink.

3. **Self-distillation without external teacher**: SD-Search recovers step-level signal from the policy's own predictions under a hindsight context — no external teacher required, no distillation ceiling.

4. **Automated step extraction**: Use heuristic boundaries (sentence breaks, line numbers in code, explicit "→" connectors) to auto-extract steps, then apply binary correctness labels via gold-answer F1 scoring.

### PRM vs ORM: When Each Matters

| Scenario | ORM | PRM |
|
-|
--|
--|
| Simple factual QA | ✓ Sufficient | Overkill |
| Multi-step math proof | PRM critical | PRM needed |
| Code generation (compilable check) | ORM can work | PRM helps on long files |
| Open-ended writing | Weak signal for both | Both weak |
| Verifiable reasoning (science, math) | Weak — trajectory is binary | Strong — step-level guidance |

## Key Results

| Method | Approach | Model | Result |
|
--|
|
-|
--|
| Thinker (2025) | 72B teacher PRM | 3B student | 0.430 multi-hop EM |
| SD-Search (2026) | Self-distilled implicit PRM | 3B | 0.428 multi-hop EM (matches Thinker, no teacher) |
| SD-Search (2026) | Self-distilled implicit PRM | 7B | 0.476 multi-hop EM (surpasses Thinker by +2.4pts) |

The SD-Search result is notable: self-distillation without external teacher matches the 72B-teacher approach at 3B and surpasses it at 7B. The "distillation ceiling" that makes Thinker's gains shrink as the student approaches the teacher doesn't apply when the teacher is the student's own future state.

## Connection to Inference-Time Compute

PRMs are the reason inference-time compute can be allocated *intelligently* rather than uniformly:

- **Best-of-N (no PRM)**: Generate 64 complete solutions, score each with an ORM, pick best. Uniform compute across all candidates.
- **PRM-guided beam search**: Maintain 8 active beams, score each at each step, prune to 4, continue. Compute concentrates on paths that show promise.

The intelligence is in the pruning: a PRM with 85% accuracy on step-level correctness can eliminate half the search space early with minimal quality loss, effectively doubling the effective inference budget.

## Open Questions

1. **PRM reliability at scale**: PRM training is noisy; a PRM that misjudges a critical step can cause the entire search to collapse on the wrong path. How do we validate PRM quality without expensive human annotation?

2. **Implicit PRM superiority**: SD-Search shows that implicit step-level signals (from hindsight-conditioned distributions) can match explicit PRMs at lower cost. Is explicit PRM training ever the right choice?

3. **Domain transfer**: PRMs trained on mathematical reasoning may not transfer to code generation or scientific reasoning. The step-level structure differs. Can we have domain-general PRMs or must each domain train its own?

4. **Combining with BoN**: If we have a reliable PRM, do we still need Best-of-N at the outcome level? PRM-guided search + final ORM scoring may be more efficient than uniform BoN.

5. **Alignment tax**: PRMs require additional training compute and introduce a new failure mode (bad PRM → wrong search path). Is the accuracy gain worth the complexity?

## Connections

- [[reward-modeling]] — PRM is a subclass of reward modeling with step-level granularity
- [[inference-time-compute-scaling]] — PRMs enable intelligent path pruning, the key to efficient test-time compute
- [[chain-of-thought]] — CoT traces are the "steps" that PRMs score
- [[load-bearing-reasoning]] — Identifying which tokens in a trace are load-bearing is the goal PRMs serve
- [[hidden-states]] — ELHSR's hidden-state reward approach could be extended to step-level signals