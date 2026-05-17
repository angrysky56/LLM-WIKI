---
summary: Waldis et al. (2026) — Instructions affect LLM production (output tokens) but not processing (input tokens); causal attention interventions confirm; asymmetry sharpens with scale and instruction-tuning; parallels human Broca's/Wernicke's dissociation.
tags: [llm, instruction-tuning, interpretability, probing, production, processing, cognition-analogy]
updated: 2026-05-17T20:30:00Z
created: 2026-05-17T20:30:00Z
type: source
sources: [https://arxiv.org/abs/2605.11206]
status: active
confidence: 0.85
---

# Instructions Shape Production of Language, not Processing

**Authors:** Andreas Waldis, Leshem Choshen, Yufang Hou, Yotam Perlitz (IBM Research / IIT / Cornell)
**arXiv:** [2605.11206](https://arxiv.org/abs/2605.11206) [cs.CL] · [v2](https://arxiv.org/abs/2605.11206v2)
**Submitted:** 11 May 2026 | **Revised:** 13 May 2026

---

## Core Finding

Instructions trigger a **production-centered mechanism** in LLMs — they change how models generate outputs, not how models comprehend inputs.

**The fundamental asymmetry:**

| | Sample tokens (input) | Output tokens |
|---|---|---|
| **Instruction sensitivity** | Stable across prompting variations | Substantially varies |
| **Behavioral correlation** | Weak | Strong |

## Method

1. **Five binary judgment tasks** probed layer-wise
2. **Separated token positions:** measured instruction influence on "sample tokens" (input under evaluation) vs. "output tokens" (model's generated response)
3. **Attention-based causal interventions:**
   - Block instruction flow to all subsequent tokens → behavior drops + production info degrades
   - Block instruction flow only to sample tokens → minimal effect on either

## Key Results

- **Generalizes across model families and tasks**
- **Scales with model size:** larger models show sharper production-only asymmetry
- **Scales with instruction-tuning:** instruction-tuned models disproportionately affect the production stage
- **Processing (sample) representations are nearly instruction-invariant** — they contain task info but it doesn't drive behavior
- **Production (output) representations are highly instruction-sensitive** — task info in output tokens strongly predicts behavior

## Cognitively Inspired Framing

The processing/production dissociation mirrors human neuroanatomy:

| | LLM stage | Human region |
|---|---|---|
| **Processing** | Input token comprehension | Wernicke's area (comprehension) |
| **Production** | Output token generation | Broca's area (speech production) |

The paper argues this dissociation is structural in LLMs — not metaphorical.

## Implications

### For interpretability
Probing input representations (the standard approach) underestimates capabilities. Task-specific information in output tokens is the more diagnostic signal.

### For prompting
Instruction effects operate at the **production** stage. "Output engineering" — controlling what the model generates — is the primary mechanism, not "input engineering."

### For alignment
If production and processing are dissociable, alignment techniques targeting outputs (e.g., RLHF, constitutional AI) may be more fundamental than those targeting input representations.

### For Chain-of-Thought
CoT generates intermediate **output** tokens, so it operates entirely within the production mechanism. This may explain why CoT effects are so instruction-sensitive — they're shaping production directly, not processing. See [[chain-of-thought]] and [[shorthand-for-thought]].

---

## Connections

- [[chain-of-thought]] — CoT operates entirely in the production stage; this may explain its instruction sensitivity
- [[shorthand-for-thought]] — compression of CoT traces; production-side manipulation
- [[hidden-states]] — probing internal representations; paper argues output-side probing is more diagnostic
- [[wernickes-area]] — human processing analog
- [[brocas-area]] — human production analog
- [[arcuate-fasciculus]] — connects Wernicke's and Broca's in humans; analogous to the instruction pathways connecting processing and production in LLMs