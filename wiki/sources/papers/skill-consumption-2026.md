---
created: 2026-05-26
updated: 2026-05-26
type: source
summary: "SkillLens: First systematic study of full model-generated skill lifecycle — non-trivial negative transfer is common, skill utility is independent of model scale, extraction guidance meta-skill reduces negative transfer."
tags: [paper, agent-skills, skill-lifecycle, skill-extraction, skill-consumption, negative-transfer, agentic-research]
sources: https://arxiv.org/abs/2605.23899
status: active
confidence: high
---

# SkillLens: From Raw Experience to Skill Consumption

**Paper:** [From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills](https://arxiv.org/abs/2605.23899)  
**arXiv:** `2605.23899` | **Published:** 2026-05-22 | **Authors:** Zisu Huang, Jingwen Xu, Yifan Yang, Ziyang Gong, Qihao Yang (Fudan, Microsoft Research, Shanghai Jiao Tong)

---

## Executive Summary

Despite proliferation of skill extraction methods for language agents, no comprehensive study spans the full skill lifecycle — experience generation, skill extraction, and skill consumption — to ask whether skills actually work, when they work, and what makes them succeed or fail. This paper provides the first utility-grounded evaluation framework covering all three stages across five agentic domains (embodied planning, productivity software, software engineering, web search, tool calling). Key findings: model-generated skills are beneficial on average but exhibit **non-trivial negative transfer**; neither extractors nor targets behave uniformly (a model can be a strong extractor but weak consumer, or vice versa); skill utility is **independent of model scale or baseline task strength**. A meta-skill that guides extraction toward features tied to actual utility consistently improves skill quality and substantially reduces negative transfer.

---

## Technical Approach

### Three-Stage Lifecycle Analysis

```
Stage 1: Experience Generation
  Target agent executes tasks → produces trajectory pool (experience)

Stage 2: Skill Extraction  
  Extractor model distills experience pool → single domain-level skill document

Stage 3: Skill Consumption
  Skill applied to target agent → evaluated on held-out test split → utility = Δ vs no-skill baseline
```

### Key Metrics Introduced

- **Extraction Efficacy (EE)**: How reliably a fixed extractor produces helpful skills across targets
- **Target Evolvability (TE)**: How much a fixed target benefits from skills extracted by different extractors from its own experience

### Domains Evaluated

1. ALFWorld (embodied planning)
2. SpreadsheetBench (productivity software)
3. SWE-bench (software engineering)
4. BFCL (tool calling)
5. Web search tasks

### Extractors Studied

Trace2Skill, one-shot LLM, human-authored, and variations

### Targets Studied

GPT family, Qwen family — ranging from small to frontier scale

---

## Key Findings

### Finding 1: Non-trivial Negative Transfer

Skills frequently **hurt** performance when transferred:
- Average positive transfer across domains, but **significant negative transfer cases**
- A model's skill can improve one target and degrade another
- Neither extractor quality nor target model scale predicts skill utility

### Finding 2: Extractor-Target Independence

> *"A model can be a strong extractor yet a weak consumer, or vice versa, with skill utility independent of model scale or baseline task strength."*

This means the skill lifecycle stages are **factorable** — extraction quality and consumption quality must be evaluated separately.

### Finding 3: Skill Quality Factors

Analysis across all three lifecycle stages reveals what drives skill utility:
- **Experience composition**: Diverse trajectory pools produce more robust skills
- **Extraction targeting**: Skills focused on recurring procedures transfer better than instance-specific learnings
- **Skill compactness**: Smaller, more procedural skills transfer better than verbose documentation

### Finding 4: Meta-Skill Improves Extraction

A meta-skill that **guides extraction toward utility-features** (rather than similarity or completeness metrics) consistently improves skill quality and reduces negative transfer. This is a skill about building skills — analogous to learning a learning algorithm.

---

## Relevance to EFHF/Wiki Research Threads

**[[efhf]]**: EFHF's bounded representation layer is challenged by the negative transfer finding. A skill document that encodes too much instance-specific detail will fail to transfer — it has exceeded its semantic capacity for the target agent's context. The meta-skill finding suggests that **structured compression** (guiding extraction toward transferable features) is essential for bounded representations to remain useful across contexts.

**[[agentic-research]]**: This paper directly addresses the agentic research thread's question about skill lifecycle. The finding that extraction and consumption are factorable means agent memory systems should separate:
1. Skill extraction quality (how well does this model distill experience?)
2. Skill consumption quality (how well does this model utilize transferred skills?)

**[[mop-explorer]]**: The negative transfer finding maps to MOP saturation — when a skill document becomes too dense or too specific, it saturates the available semantic capacity for the target agent, producing degradation rather than improvement. The meta-skill's compression guidance is precisely the MOP's bounded exploration strategy applied to skill construction.

> *"Model-generated skills are beneficial on average but exhibit non-trivial negative transfer, and that neither extractors nor targets behave uniformly."*

---

## Key Quotes

> *"No comprehensive study examines all three stages of the skill lifecycle and systematically asks whether domain-level, model-generated skills actually work, when they work, and what makes them work or fail."*

> *"A model can be a strong extractor yet a weak consumer, or vice versa, with skill utility independent of model scale or baseline task strength."*

> *"We translate these findings into a concrete meta-skill that guides skill extraction toward the features tied to actual utility, which consistently improves skill quality across domains and substantially reduces negative transfer."*

---

## Related
- [[index]]
- [[sources/papers/skill-consumption-2026]]

- [[skill-consumption-2026]]

## Structural Insights

1. **The three lifecycle stages are orthogonally optimizable**: This is a critical insight for agent architecture. EFHF's separation of verifier (skill evaluator) from agent (skill consumer) is validated by the finding that extraction quality and consumption quality are independent — they can be separately optimized without coupling.

2. **Negative transfer is the primary failure mode of bounded representations**: When the skill document exceeds the target's semantic capacity (or doesn't match the target's prior), degradation occurs. This is the bounded representation analog of the Shannon Scaling Law's SNR collapse — capacity saturation leads to performance degradation, not just sub-optimality.

3. **Meta-skill is a second-order representation**: A skill that guides skill extraction is a hyperparameter in representation space — it controls how other skills are constructed. This parallels the verifier-graph's meta-level verification: the meta-skill verifies that the skill extraction process targets transferable features, just as the verifier verifies that the agent's outputs target reliable patterns.