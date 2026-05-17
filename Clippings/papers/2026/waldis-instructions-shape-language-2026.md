---
source_url: https://arxiv.org/abs/2605.11206
ingested: 2026-05-17
sha256: 2a4e07a18d9ccd96cd7e7722397e3480bca1659d3a7a4b6450a6870d51ed0be7
---

# Instructions Shape Production of Language, not Processing

**Authors:** Andreas Waldis, Leshem Choshen, Yufang Hou, Yotam Perlitz (IBM Research / IIT / Cornell)

**Submitted:** 11 May 2026 | **Revised:** 13 May 2026 (v2)
**arXiv:** [2605.11206](https://arxiv.org/abs/2605.11206) [cs.CL]
**DOI:** https://doi.org/10.48550/arXiv.2605.11206

---

## Abstract

Instructions trigger a production-centered mechanism in language models. Through a cognitively inspired lens that separates language processing and production, we reveal this mechanism as an asymmetry between the two stages by probing task-specific information layer-wise across five binary judgment tasks.

Specifically, we measure how instruction tokens shape information both when sample tokens (the input under evaluation) are processed and when output tokens are produced.

**Key finding:** Task-specific information in sample tokens remains largely stable and correlates only weakly with behavior. The same information in output tokens varies substantially and correlates strongly with behavior.

### Causal confirmation via attention interventions

- Blocking instruction flow to **all subsequent tokens** → reduces both behavior and information in output tokens
- Blocking instruction flow **only to sample tokens** → minimal effect on either

The asymmetry generalizes across model families and tasks, and becomes sharper with model scale and instruction-tuning, both of which disproportionately affect the production stage.

---

## Methodology

- **Tasks:** Five binary judgment tasks
- **Probing:** Layer-wise probing of task-specific information
- **Token decomposition:** Separated sample tokens (input under evaluation) from output tokens (model generation)
- **Attention-based intervention:** Surgical ablation of instruction token flow

---

## Key Claims

1. **Production-centric mechanism:** Instructions affect how models produce outputs, not how they process inputs
2. **Processing is stable:** Sample token representations are largely unaffected by instruction variations
3. **Production varies:** Output token representations shift substantially based on instructions
4. **Scale amplifies the asymmetry:** Larger and instruction-tuned models show sharper production-only effect
5. **Implications for evaluation:** Probing only input representations misses the actual capability mechanism

---

## Cognitively Inspired Framing

The processing/production dissociation in LLMs parallels human psycholinguistics:
- **Processing** ≈ comprehension (Wernicke's area)
- **Production** ≈ language generation (Broca's area)

The paper argues these are partly dissociable mechanisms in LLMs as well.

---

## Implications

- **For interpretability:** Measuring task info in input representations underestimates model capabilities; output token internals are more diagnostic
- **For prompting:** Instruction effects operate at the production stage, suggesting that "output engineering" (controlling what the model generates) is the primary lever, not "input engineering" (shaping how the model interprets the prompt)
- **For alignment:** If production is distinct from processing, alignment techniques targeting outputs may be more effective than those targeting internal representations of inputs