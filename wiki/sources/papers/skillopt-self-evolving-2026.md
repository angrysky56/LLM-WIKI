---
created: 2026-05-26
updated: 2026-05-26
type: source
summary: "SkillOpt: First systematic text-space optimizer for agent skills — trains skill documents as external state via add/delete/replace edits, validation gating, and epoch-wise meta updates."
tags: [paper, agent-skills, skill-optimization, text-space-optimization, domain-adaptation, efhf, agentic-research]
sources: https://arxiv.org/abs/2605.23904
status: active
confidence: high
---

# SkillOpt: Executive Strategy for Self-Evolving Agent Skills

**Paper:** [SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/abs/2605.23904)  
**arXiv:** `2605.23904` | **Published:** 2026-05-22 | **Authors:** Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou (Microsoft, Shanghai Jiao Tong, Tongji, Fudan)

---

## Executive Summary

Agent skills today are hand-crafted, one-shot generated, or evolved through loosely controlled self-revision — none of which reliably improves over the starting point under feedback. SkillOpt proposes treating the **skill document as external trainable state** of a frozen agent, applying the same discipline as weight-space optimization: rollout batches, gradient-derived edit directions, learning rate budgets, held-out validation gates, and epoch-wise momentum. A separate frontier optimizer model converts scored rollouts into bounded add/delete/replace edits on the skill document; edits are accepted only when they strictly improve held-out validation score. SkillOpt is best or tied-best on all 52 evaluated (model, benchmark, harness) cells across six benchmarks, seven target models, and three execution harnesses (direct chat, Codex, Claude Code). On GPT-5.5 it lifts average no-skill accuracy by +23.5 points in direct chat, +24.8 in Codex, +19.1 in Claude Code. Exported skills transfer across model scales and execution environments.

---

## Technical Approach

### Core Formulation: Skill as External State

The key insight is that skill adaptation should be decoupled from model weight updates. A **skill document** (~300–2,000 tokens) is:
- Portable: works with any frozen agent
- Inspectable: human-readable procedures
- Trainable: can be optimized via feedback
- Transferable: retains value across model scales/harnesses

### SkillOpt Loop

```
rollout batch → trajectory analysis → optimizer model proposes edits →
textual learning rate budget → rank/filter edits → apply bounded update →
held-out validation gate → accept/reject → rejected-edit buffer (negative feedback)
```

Key components analogous to deep learning:

| Deep Learning | SkillOpt |
|--------------|----------|
| Weight parameters | Skill document |
| Gradient | Trajectory-derived edit direction |
| Learning rate | Textual edit budget |
| Minibatch | Reflection minibatch |
| Validation set | Held-out selection gate |
| Momentum | Epoch-wise slow/meta update |

### Edit Types

The optimizer model generates **add/delete/replace** operations on the skill document — these are the "gradients" in text space. An edit is only accepted if validation performance strictly improves. Rejected edits are retained as **negative examples** for the optimizer model.

### Key Design Decisions

1. **Bounded edits** vs. full rewrites: Prevents large semantic jumps and instability
2. **Held-out gating**: Prevents harmful edits from accumulating (critical for stability)
3. **Rejected-edit buffer**: Converts failures into learning signal
4. **Slow/meta update**: Preserves long-horizon regularities across epochs; acts like momentum

---

## Key Results

### Main Results (GPT-5.5)
- **Direct chat**: +23.5 avg points (SearchQA: 77.7→87.3, SpreadsheetBench: 41.8→80.7, DocVQA: 78.8→91.2, LiveMathematicianBench: 37.6→66.9, ALFWorld: 83.6→95.5)
- **Codex harness**: +24.8 avg points over no-skill
- **Claude Code harness**: +19.1 avg points over no-skill
- **52/52 cells**: Best or tied-best across all (model, benchmark, harness) combinations

### Transfer Results
- SpreadsheetBench skill trained on GPT-5.4 improves all smaller GPT variants
- Codex-trained spreadsheet skill transfers to Claude Code (+59.7 points)
- OlympiadBench skill yields positive gains on Omni-MATH without further optimization

---

## Relevance to EFHF/Wiki Research Threads

**[[efhf]]**: EFHF's principle of **bounded representation layers** aligns with SkillOpt's architecture: instead of modifying weights (unbounded parameter space), the agent operates on a bounded natural-language skill document. The "textual learning rate" constrains how far the skill can drift per update — analogous to EFHF's bounded state transitions. A skill document that tries to encode too much (exceeding its capacity) will experience the same SNR collapse predicted by the Shannon Scaling Law.

**[[agentic-research]]**: SkillOpt is a concrete realization of trainable procedural memory. The skill document is the **agent's external cortex** — encoding recurring procedures, domain heuristics, tool policies, and failure modes in a form that can be optimized without touching model weights. This directly addresses the agentic research thread's question: how do agents accumulate and refine experience?

**[[mop-explorer]]**: The MOP explorer's bounded exploration in semantic space parallels SkillOpt's bounded skill edits. Both systems use conservative step sizes with validation-gated acceptance to avoid catastrophic semantic drift.

> *"If the recurring object of adaptation is the agent's procedure, the skill document itself should be trainable. Yet weight adaptation is often unavailable for closed frontier models and expensive for open ones."*

---

## Key Quotes

> *"SkillOpt is, to our knowledge, the first systematic controllable text-space optimizer for agent skills: a separate optimizer model turns scored rollouts into bounded add/delete/replace edits on a single skill document, and an edit is accepted only when it strictly improves a held-out validation score."*

> *"The deep-learning analogy is operational rather than decorative. Rollout and reflection batch sizes control the noise in the evidence used for each edit; the textual learning rate and schedule control how far one skill version is allowed to move from the previous one."*

> *"A textual learning-rate budget, rejected-edit buffer, and epoch-wise slow/meta update make skill training stable while adding zero inference-time model calls at deployment."*

---

## Related
- [[sources/papers/skillopt-self-evolving-2026]]
- [[index]]

- [[skillopt-self-evolving-2026]]

## Structural Insights

1. **Skill documents are a practical externalization of EFHF's bounded representation layer**: Rather than encoding everything in weights (which faces SNR collapse at scale), SkillOpt uses bounded text documents as the adaptation substrate. The capacity of a 300-2000 token skill document is much smaller than model weights, but it's trainable, inspectable, and doesn't require access to closed model weights.

2. **The optimizer model pattern (frontier model optimizes frozen agent's skill) mirrors verifier-agent separation**: SkillOpt's architecture separates the "optimizer" (frontier model proposing edits) from the "actor" (frozen target model executing tasks). This is structurally identical to the verifier-agent separation in EFHF, where the verifier (frontier model) provides structured feedback to the agent (target model).

3. **Negative transfer is the failure mode corresponding to MOP saturation**: When skills don't transfer (e.g., a skill that helped one model hurts another), it's because the skill document exceeded its capacity for the target's semantic space — analogous to the SNR collapse in the Shannon Scaling Law. The meta-skill finding (guiding extraction toward utility features) is essentially a capacity-aware skill construction strategy.