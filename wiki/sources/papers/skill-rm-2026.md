---
created: 2026-06-03T00:00:00Z
updated: 2026-06-03T00:00:00Z
type: source
summary: "Skill-RM (Alibaba Qwen team) — reformulates reward modeling as the execution of a reusable Reward-Evaluation Skill. Resource bank (rubrics, verifiers, references, checklists) + procedural invocation protocol + structured judgment. Achieves 86.2 avg on RewardBench2/RM-Bench/JudgeBench, beats all scalar, generative, rubric, agentic, and LLM-as-Judge baselines at matched backbone."
tags: [arxiv-2026, reward-modeling, agent-skill, agentic-judge, evaluation, rubrics, verifiers, heterogeneous-criteria, paper-2606-03980]
sources: https://arxiv.org/abs/2606.03980
status: active
confidence: 0.90
---

# Skill-RM: Unifying Heterogeneous Evaluation Criteria via Agent Skill (Chen et al., Alibaba, 2026)

**arXiv:** 2606.03980
**Authors:** Tao Chen, Gangwei Jiang, Pengyu Cheng, Siyuan Huang, Yihao Liu, Jingwei Ni, Jiaqi Guo, Mengyu Zhou, Kai Tang, Junling Liu, Qinliang Su, Xiaoxi Jiang, Guanjun Jiang (Alibaba Qwen Team + Sun Yat-sen / CUHK / PKU / ETH Zürich / U Zurich)
**Date:** 2026-06-02

## The Problem

Reward models (RMs) are the supervisory signal for RFT, RLHF, and GRPO — but the *criteria* they need to apply have become increasingly heterogeneous:

- **Rule-based verifiers** for math / code (Lightman 2024)
- **Reference-based** factuality checks (Nakano 2021, Min 2023)
- **Procedural checklists** (Viswanathan 2025)
- **Rubrics** for open-ended generation (Kim 2024, Liu 2025)
- **Multi-step agentic trajectories** (Qin 2024, Lu 2026)
- **Constraint decomposition + policy vetoes** for safety (Bai 2022b, Jiang 2024)

Existing approaches each handle one resource modality:
- **Scalar RMs** — opaque, uninterpretable, can't route to tools
- **LLM-as-a-Judge** — flat-prompt everything into one context, no resource management
- **Rubric / verifier systems** — expose one resource at a time

There is no *unified, reusable abstraction* that can seamlessly synthesize heterogeneous resources, adaptively select evidence, and produce explicit, evidence-grounded reward computation.

## The Core Idea: Reward-Evaluation Skill

Skill-RM **reformulates reward modeling as the execution of a reusable Reward-Evaluation Skill**. A skill, in the agent sense (Anthropic 2025, Agent Skills Contributors 2025), is a filesystem-based package containing:

- A procedural document (analogous to `SKILL.md`) encoding the evaluation procedure
- A resource bank — modular, version-controlled, loadable-on-demand
- A structured schema for evidence collection and judgment

The skill is composed of two parts:

- **M_RM (procedural specification)** — the execution blueprint: which resources to invoke, in what order, with what preconditions
- **U_RM (resource bank)** — categorized into:
  - **Criteria** — declarative evaluative standards (rubrics, constraints, principles)
  - **Evidence-producing procedures** — code interpreters, retrieval tools, NL verifiers
  - **Aggregation / calibration rules** — score normalization, conflict resolution, priority

The judge model 𝜋_ϕ executes the skill via an **action-observation trace**:

```
τ = (a₁, o₁, ..., a_T, o_T, z) ~ 𝜋_ϕ(· | x, Y; S_RM)
```

where `z` is a structured judgment populated only after all mandatory evidence fields are satisfied. The action set includes: listing available resources, inspecting evidence, executing tools, finalizing the judgment.

The final reward is read out deterministically:

```
r_ϕ^Skill(x, Y; S_RM) = A(τ) ∈ ℝ (pointwise) or {1,...,K} (selection)
```

## Why This Matters

1. **Interpretability** — every reward decision is grounded in an explicit evidence trace; no opaque scalar collapse
2. **Adaptability** — the judge invokes *only* the resources relevant to the input; no monolithic context pollution
3. **Modularity** — adding a new evaluation modality = adding a new resource to U_RM and a clause to M_RM. No retraining
4. **Reusability** — the same skill is reused across best-of-N, RFT, judge benchmarking, and downstream alignment
5. **Consistency** — pointwise scoring and multi-candidate selection become *two projections of the same evidence-bearing process*

## Results

### Reward Model Benchmarks (Qwen3.5-27B backbone)

| Method | RewardBench2 | RM-Bench | JudgeBench | Avg |
|---|---|---|---|---|
| INF-ORM-Llama3.1-70B | 76.5 | 75.4 | 70.2 | 74.0 |
| Skywork-Reward-V2-Qwen3-8B | 78.2 | 82.6 | 73.4 | 78.1 |
| Skywork-Reward-V2-Llama-3.1-8B | 84.1 | 92.8 | 80.0 | 85.6 |
| RM-R1-DeepSeek-Distill-Qwen-32B | 71.0 | 83.9 | 56.1 | 70.4 |
| RationaleRM-Qwen3-30B-A3B | — | 87.1 | 82.0 | — |
| Auto-Rubric-Qwen3-32B | 82.3 | 88.1 | 80.9 | 83.8 |
| RewardAgent (Qwen3.5-27B) | 82.0 | 80.5 | 66.3 | 76.3 |
| TIR-Judge-Zero (Qwen3-8B) | 73.4 | 83.7 | 72.0 | 76.4 |
| GPT-4o Judge | 64.9 | 73.1 | 59.8 | 65.9 |
| Qwen3.5-27B (raw) | 81.1 | 89.8 | 80.8 | 83.9 |
| **Skill-RM (Qwen3.5-27B)** | **85.0** | **91.5** | **82.1** | **86.2** |

**At matched backbone (Qwen3.5-27B), Skill-RM beats the raw LLM-as-a-Judge by 2.3 points on average and beats the strongest agentic judge (RewardAgent) by 9.9 points.** The 122B variant (Qwen3.5-122B-A10B) shows even stronger gap on JudgeBench (85.2 vs 67.1 raw).

The paper's ablation confirms the gains come from the *skill-mediated orchestration* itself, not just from additional context or tool availability.

## Methodological Significance

Skill-RM contributes to a wider shift in evaluation research from **prompt-level flat judges** to **protocol-governed executable procedures**. Notable parallel design choices:
- The procedural M_RM is essentially a *typed plan* in the agentic sense
- The resource bank is a *bounded representation capacity* mechanism — only relevant resources are loaded
- The action-observation trace is exactly the *evaluation trajectory* the agent traverses, not just the final score

The work also bridges two lines the wiki has tracked separately:
- **Skill research** (SkillOpt, SkillLens, MUSE-Autoskill, ReuseRL, SkillHarm) — agent skills as the operational unit
- **Reward model research** (Rubrics, RRM, GenerativeRMs, Auto-Rubric) — the supervisor for RL training

By treating the reward model as *itself* an agent executing a skill, Skill-RM shows that *the skill abstraction generalises beyond task execution into evaluation*.

## Limitations

- Resource bank construction is LLM-assisted and currently curated by the authors; no automated discovery of new resources at evaluation time
- The procedural M_RM is hand-engineered; learning it end-to-end remains open
- Pointwise scoring depends on the calibration / aggregation rule being well-designed; poor rules degrade performance below flat-prompt baselines
- Latency cost — multi-step agentic judge is slower than one-shot RM

## Connections to Wiki

### Wiki concepts
- [[bounded-representation-capacity]] — the resource bank is the *capacity allocation unit*; the procedural spec is what loads the right subset
- [[agent-skills]] — Skill-RM operationalises the agent-skill abstraction in the reward modeling domain
- [[reward-models]] — Skill-RM is the *unified* reward model: procedural, resource-aware, agentic
- [[rubric-evaluators]] — Skill-RM subsumes rubric-only judges via the U_RM resource type
- [[verifier-graphs]] — Skill-RM's evidence-bearing trace is a verifier graph realised as an action-observation sequence
- [[agentic-evaluation]] — Skill-RM is a canonical example of evaluation *as agentic action*

### Related papers (wiki)
- [[reuserl-skill-reuse-compression]] — ReuseRL uses skill compression as a structural regulariser; Skill-RM uses skills as the *evaluation procedure* itself. Both are MDL-adjacent: the *evaluation protocol* must be reusable, not bespoke per example
- [[skillopt-self-evolving-2026]] — SkillOpt optimises skill *content*; Skill-RM optimises skill *usage in evaluation*
- [[skillharm-lifecycle-skill-attacks-2026]] — SkillHarm showed poisoned skills mutate persistently and cause harm. **The obvious security question: can a poisoned skill be a poisoned *reward-evaluation* skill?** A reward skill that systematically rates a particular response style as 5/5 would corrupt the entire post-training pipeline. This is a high-leverage attack surface
- [[muse-autoskill]] — MUSE-Autoskill's 5-phase skill lifecycle (create → memory → manage → evaluate → refine) maps directly onto the Skill-RM M_RM execution; the *evaluate* phase of MUSE is exactly what Skill-RM operationalises
- [[codeskill]] — CodeSkill manages skills as a capacity bank; Skill-RM manages *evaluation resources* as a capacity bank
- [[ctx2skill]] — Ctx2Skill discovers skills from context; Skill-RM prescribes the procedural form
- [[muse-autoskill]] / [[skill-consumption-2026]] / [[stepopsd-2026]] — same skill-as-bounded-representation lineage

### Skill-Theme Cross-Link
This is the **8th paper** in the wiki's skill theme (after SkillOpt, SkillLens, ReuseRL, MUSE-Autoskill, CODESKILL, SkillHarm, Ctx2Skill). It confirms a wider pattern:
- skills as the *operational unit* of agents
- skills as the *compression unit* of trajectories
- skills as the *evaluation unit* of reward models
- skills as the *attack surface* of supply chains

## Key Quote

> "Scalar RMs compress complex, resource-grounded evidence into opaque scores, rendering the evaluation process fundamentally uninterpretable and inflexible. ... we can map this principle directly onto heterogeneous evaluation criteria: rubrics, references, constraints, and verifiers are modular and loadable resources, while a 'reward skill' governs their invocation and synthesis."

## What To Watch
- **Adversarial reward skills** — a poisoned M_RM or a malicious resource in U_RM would silently corrupt every downstream policy trained against it. This is the SkillHarm attack surface applied to evaluation.
- **Skill-compiled RMs** — a "skill compiler" that turns a natural-language evaluation spec into a portable, versioned reward skill is a natural follow-up.
- **Integration with agentic RL frameworks** — if Skill-RM becomes a standard reward interface, frameworks like verl / TRL would need to support agentic judges, not just scalar ones.

### Cross-cycle (2026-06-04 batch)
- **Skill-RM ↔ [[arxiv-2605-30335-locally-coherent-globally-incoherent]]:** Skill-RM is a *single-model* procedural evaluator. Kotawala's compositional residual ε★ is what happens when you stack many such evaluators into a system: each is locally coherent, the composition is not. The Skill-RM idea scales to systems; the ε★ analysis is what tells you when that scaling breaks.
- **Skill-RM ↔ [[arxiv-2605-30348-llmsurgeon-data-mixture-surgery]]:** Both are post-hoc audits of model internals. Skill-RM audits the *evaluation procedure*; LLMSurgeon audits the *training data*. LLMSurgeon's calibrated-confusion-matrix inverse problem is mathematically the same class of technique that would be needed to audit *which reward skills* an LLM has internalized — a natural follow-up.
- **Skill-RM ↔ [[arxiv-2605-30343-reasoning-in-memory-rim]]:** RiM is a *latent* reasoning method (no externalised chain-of-thought). Skill-RM is an *externalised* evaluation method (a multi-step evidence trace). Two polar answers to the same question: do you compute in the residual stream, or in the action space?
