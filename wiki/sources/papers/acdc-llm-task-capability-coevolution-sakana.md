---
summary: Sakana AI arXiv 2604.14969 — AC/DC coevolves LLM populations (via evolutionary model merging) with synthetic task populations (via scientist LLM). Discovers a task force of small diverse models with broader Coverage on benchmarks than experts, larger models, or GPT-4o at N=8 — without explicit benchmark optimization.
tags: [source, llm-training, evolutionary-algorithms, model-merging, quality-diversity, open-endedness, coevolution, papers]
updated: 2026-06-04T12:42:02Z
created: 2026-06-04T12:42:02Z
---

---
created: 2026-06-04T00:00:00Z
updated: 2026-06-04T00:00:00Z
type: source
summary: "Dai, Meinardus, et al. (Sakana AI, arXiv 2604.14969) — AC/DC: Assessment Coevolving with Diverse Capabilities. Open-ended coevolution of LLM populations (via evolutionary model merging) and synthetic task populations (via scientist-LLM task generation). Discovers a diverse task force of small models that achieves broader Coverage on downstream benchmarks than hand-selected experts, control sampling, or a single larger model, including GPT-4o at N=8 in some configurations."
tags: [source, llm-training, evolutionary-algorithms, model-merging, quality-diversity, open-endedness, coevolution, papers]
sources: https://arxiv.org/html/2604.14969v1
status: active
confidence: 0.9
---

# Discovering Novel LLM Experts via Task-Capability Coevolution (AC/DC)

**Authors**: Andrew Dai, Boris Meinardus, Ciaran Regan, Yingtao Tian, Yujin Tang (Sakana AI)
**Source**: arXiv 2604.14969v1
**Project page**: https://acdc-llm.github.io/

## Core idea

A new model-development framework — **AC/DC (Assessment Coevolving with Diverse Capabilities)** — that coevolves a population of LLMs alongside a population of synthetic tasks, in a single training run, to discover a *task force* of small diverse models that collectively cover a wide range of capabilities. The headline claim: AC/DC's discovered collectives can outperform hand-selected expert models, repeated self-sampling, and even a single larger frontier model (e.g., GPT-4o) on Coverage — without explicit benchmark optimization.

## The three challenges AC/DC addresses

1. The current pre-/post-training paradigm requires hand-designing datasets/rewards per training run, producing one model at a time. This is expensive and produces brittle, single-model artifacts.
2. Collective intelligence (CI) outperforms any single member (the paper's broader thesis) but is hard to *discover* in the LLM setting.
3. Open-endedness (OE) — never-ending discovery — is the right paradigm but hasn't been extended to LLM populations.

## Key building blocks (Section 2)

### Evolutionary Model Merging
AC/DC builds on EvoMerge / CycleQD with two operators:
- **Crossover**: weighted linear interpolation of *task vectors* $\tau = \theta_{parent} - \theta_{base}$ for two sampled parents.
- **Mutation**: SVD-based — for each weight matrix $W = U\Sigma V^T$, perturb the top $k$ singular values of $\Sigma$. Modifies representational structure while preserving geometry.

### Coverage metric
The central evaluation metric. For $Q$ questions and $N$ LLMs:
$$\text{Coverage} = \frac{1}{Q}\sum_{q=1}^{Q} \left(\bigvee_{i=1}^{N}(x_{q,i}=y_q)\right)$$
The "at least one model gets it right" rate across the population. Captures *complementary* capability better than per-model accuracy.

### Skill vectors
Binary per-question pass/fail vectors serve as behavioral signatures. Distances between skill vectors measure population diversity. Inspired by MAP-Elites' niche scheme, but no predefined niches — DNS handles the partitioning.

### Quality-Diversity selection
**Dominated Novelty Search (DNS)** — for solution $i$, $\tilde{f}_i$ is the mean distance to the $k$ nearest better-performing solutions in the descriptor (skill-vector) space. Encourages diversity by rewarding solutions that are *distant from better neighbors*.

### Open-ended coevolution + minimal criteria
AC/DC uses *minimal criteria* (MC) for both models and tasks — coarse filters that weed out gibberish and impossible tasks while letting exploration flourish.

## The algorithm (Section 3)

Two archives: $\mathcal{A}_M$ (model archive) and $\mathcal{A}_Q$ (task archive).

**Model evolution phase (every generation $g$):**
1. Select $P$ parents from $\mathcal{A}_M$
2. Crossover + mutation → $N$ offspring
3. Evaluate offspring on $\mathcal{A}_Q$ to get skill vectors
4. Apply "gibberish filter" (judge LLM flags degenerate outputs)
5. DNS update on $\mathcal{A}_M$ — keep $M$ best by adjusted fitness

**Task evolution phase (every $G_{task}$ generations):**
1. **Task proposal**: scientist LLM takes a parent task + 3 reference tasks + an adaptation hint (harder / easier / novel) → generates a candidate task
2. **Novelty filtering**: cosine-similarity nearest-neighbor + judge LLM verdict
3. **Reflection & validation**: scientist LLM attempts its own task, runs the scoring function, fixes compilation/logic errors
4. **MC filter**: drop impossible tasks, replace with parent

Selection for downstream eval: pick $N_{tf}$ models from the historical archive that maximize correct-solves on the global task archive $\mathcal{A}_{Q_g}$ — independent of any downstream benchmark.

## Quantitative results (Section 4)

Coverage gains vs baselines (averaged across benchmarks):

| Base model | vs Experts N=3 | vs Control N=8 | vs Big Model N=8 | vs GPT-4o N=8 |
|------------|---------------:|---------------:|-----------------:|--------------:|
| Qwen2 7B | +2.06% | -1.04% | +8.83% | +2.05% |
| Qwen2.5 7B | +4.40% | +0.61% | +9.78% | +6.95% |
| Qwen3 14B | -0.21% | +1.54% | +9.48% | +10.71% |
| DeepSeek V1 7B | +9.69% | +7.04% | +12.69% | -7.72% |
| **Average** | **+3.99%** | **+2.04%** | **+10.19%** | **+2.99%** |

Headline: **Qwen2.5 7B achieves +3.85% over a 72B model using only 29% of the params (N=3)**, and **+9.78% (N=8)** — a 3.85x parameter efficiency win. With N=3 Qwen2.5 also beats GPT-4o (+1.02%).

Best-of-N single-answer selection (Tab. 2) — smaller but still positive gains, demonstrating practical value beyond Coverage.

Ablations (Sec D.1) — DNS selection and the gibberish filter are the most critical components (2.39% / 2.46% drops at N=3 when removed). Removing *all* evolutionary components: -2.36% at N=3, -7.02% at N=8.

Comparison to prior QD methods (DNS, CQD) on benchmark-specific optimization — AC/DC wins without any benchmark-specific optimization, demonstrating that the discovered models generalize OOD.

## Qualitative findings (Section 5)

- **Emergent specialization** (Fig 3): 8 discovered models have distinct per-benchmark performance profiles; "Model 4 may not be best overall but provides correct chemistry answers that no other model can."
- **Merged models unlock new capabilities** (Fig 4): cases where every baseline (math expert, code expert, 8x instruct sampling, 72B) fails but a merged AC/DC model succeeds. Includes a 512-token training cap that creates selection pressure for concise answers — addressing a real deployment constraint.
- **Response diversity** (Fig 5): on the same synthetic task, three merged models produce three different analogies (library nav / urban directions / maze solving) and three different correct algorithm implementations — genuine conceptual diversity, not surface variation.
- **Human study** (47 synthetic + 49 benchmark tasks, 3 reviewers): synthetic tasks are 97.8% correct, 68.9% OOD vs standard benchmarks, 37.8% creative. Benchmarks scored 10.2% OOD and 6.1% creative. Strong inter-rater agreement on objective metrics.

## Connection to prior work

- **EvoMerge** (Akiba et al.) — evolutionary merging with CMA-ES
- **CycleQD (CQD)** — task-vector crossover in QD setting
- **MAP-Elites / DNS** — quality-diversity algorithms
- **Quality-Diversity** (Pugh, Lehman) — collections of diverse, high-quality solutions
- **Open-ended coevolution + minimal criteria** (Brant & Stanley; Soros & Stanley)
- **Synthetic task generation** (e.g., FunSearch, prior work on LLM-generated benchmarks)

## Why this is useful for the vault

- **Concept of "Coverage"** is a clean, general metric for evaluating multi-model populations — could be applied to the multi-agent sheets in this vault (insights, news, arxiv all produce parallel agent runs).
- **Open-ended coevolution** pattern is directly relevant to the agent sheet / carryover architecture: coevolving tasks (e.g., research questions) alongside the agents that address them.
- **Task force selection** (independent of downstream benchmarks) maps onto Ty's pattern of letting the wiki's own structure decide which pages get linked/promoted, rather than externally imposing a hierarchy.
- **Skill vectors as behavioral signatures** — could be a formalization pattern for the agent sheets' per-page authority scores.

## Connections

- [[concepts/open-endedness]] — the OE framework AC/DC instantiates
- [[concepts/quality-diversity]] — the QD selection family (DNS, MAP-Elites)
- [[concepts/evolutionary-model-merging]] — EvoMerge / CQD lineage
- [[concepts/coevolution]] — the minimal-criteria open-ended variant
- [[concepts/coverage-metric]] — the central evaluation
- [[concepts/synthetic-task-generation]] — scientist-LLM pattern
- [[concepts/skill-vectors]] — behavioral signatures without predefined niches
- [[entities/projects/sakana-ai]] — the lab behind the paper
- [[concepts/model-merging]] — broader category
- [[concepts/llm-distillation]] — *not* a substitute, AC/DC uses merging, not distillation

## Caveats

- arXiv preprint, no peer review yet (and the date format 2604 is unusual — likely 2026-04 misformatted in source filename)
- "GPT-4o" baseline is the only frontier model compared; not tested against Claude, Gemini, or newer open-weights leaders
- DeepSeek V1 7B against GPT-4o is -18.46% at N=3 — the small-model collective doesn't always win
- Best-of-N is "rudimentary" per the authors; closing the gap to single-model inference is acknowledged as future work
- The 97.8% correctness of synthetic tasks is human-evaluated on 47 tasks — small sample
- "Out-of-distribution" is human-judged; strong inter-rater agreement on this metric was not established (creativity had weak agreement)
