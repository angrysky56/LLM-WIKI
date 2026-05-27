---
summary: Statistical paired-comparison model for aggregating pairwise judgments into global rankings; core of OpenDeepThink's parallel reasoning selection (+405 Codeforces Elo)
tags: [bradley-terry, llm-evaluation, ranking, paired-comparison, test-time-compute, inference-time-scaling]
updated: 2026-05-27T07:26:14Z
created: 2026-05-27T07:26:14Z
---

# Bradley-Terry Model

## Definition

The **Bradley-Terry model** is a statistical model for analyzing paired comparison data — predicting the outcome of a contest between two items by assigning each item a latent strength parameter. Given items *i* and *j* with strengths *λᵢ* and *λⱼ*, the model estimates the probability that *i* beats *j* as:

```
P(i beats j) = λᵢ / (λᵢ + λⱼ) = sigmoid(log λᵢ - log λⱼ)
```

The strengths are estimated via maximum likelihood from a set of binary outcome observations (win/loss). The model originated in psychology (Bradley & Terry, 1952) and became foundational in chess rating (Elo) and sports ranking systems (TrueSkill). It is the canonical model for *pairwise ranking from noisy comparisons*.

## Relevance to LLM Evaluation

In LLM research, the Bradley-Terry model gained renewed attention as a mechanism for aggregating **pairwise judgments** — where an LLM judge is asked "which of these two outputs is better?" — into a globally consistent ranking across N candidates (without ground-truth labels). This solves the **selection bottleneck** in parallel reasoning:

- **The problem**: Generating N candidate reasoning traces produces N outputs, but selecting the best requires a judge. Pointwise judging (scoring each independently) is biased toward verbose outputs or self-consistent responses. Voting (majority win) suppresses minority correct answers.

- **Bradley-Terry advantage**: Pairwise comparison avoids the positional and verbosity biases of pointwise judging. Aggregating N×(N-1)/2 binary comparisons into a global ranking via maximum likelihood produces calibrated strength estimates (Elo-style ratings) that are transitive and comparable.

### OpenDeepThink Application

The [OpenDeepThink paper](https://arxiv.org/abs/2605.15177) (arXiv:2605.15177, May 2026) demonstrated Bradley-Terry aggregation as the core selection mechanism for parallel reasoning:

| Result | Details |
|--------|---------|
| +405 Codeforces Elo | Gemini 3.1 Pro with 8 rounds of Bradley-Terry ranking on CF-73 benchmark |
| Model-agnostic transfer | Ranking trained on one model transfers to others without retuning |
| 73 expert-rated problems | CF-73 dataset with International Grandmaster annotation |

The pipeline: generate N candidates → pairwise LLM judge comparisons → Bradley-Terry MLE to get global ratings → select top-ranked. Each "round" involves O(N) pairwise comparisons; the model runs for 8 rounds, progressively refining the ranking.

### Relationship to Reward Modeling

Bradley-Terry is a **reward-free alternative** to explicit reward models (RMs) for Best-of-N selection. Instead of training a scalar reward model:

- **Reward model approach**: Train a neural network to emit a scalar score for each output; use it to rank N candidates.
- **Bradley-Terry approach**: O(N) binary comparator calls — ask an LLM "which is better?" for each pair, aggregate win/loss counts into strength estimates via MLE.

Bradley-Terry avoids the overhead of training a separate RM (which can be as large as the generator itself), and the binary comparison signal is richer than a scalar score: "A beats B" encodes direction, not just magnitude. However, Bradley-Terry requires O(N²) comparisons for N candidates (vs. O(N) scoring for a reward model), making it expensive at scale unless rounds are used to reduce the comparison budget.

## Connections

- [[opendeepthink-parallel-reasoning]] — Primary empirical source; +405 Elo via Bradley-Terry aggregation on Codeforces
- [[reward-modeling]] — Bradley-Terry as a reward-free ranking alternative to scalar reward models for Best-of-N selection
- [[parallel-reasoning]] — Bradley-Terry solves the selection bottleneck in parallel reasoning
- [[inference-time-compute-scaling]] — Bradley-Terry aggregation is a core mechanism within the test-time compute scaling paradigm
- [[process-reward-model]] — PRM step-level scores could in principle serve as comparators for per-step Bradley-Terry ranking in multi-step reasoning
- [[llm-evaluation]] — Bradley-Terry ELO calibration is used to track model strengths in verifiable reasoning domains (Codeforces, MATH)

## Open Questions

1. **Round efficiency**: OpenDeepThink achieves +405 Elo in 8 rounds. What determines the optimal number of rounds? Is 8 rounds always sufficient or does it vary by problem difficulty?

2. **Bradley-Terry + PRM integration**: Can per-step Bradley-Terry ranking (comparing which sub-step leads closer to the goal) be combined with process reward model scores for multi-step reasoning problems?

3. **Comparator quality ceiling**: If the LLM judge cannot reliably distinguish subtle reasoning quality, Bradley-Terry rankings collapse to noise — the ceiling is the ceiling of the comparator model.

4. **Subjective domain extension**: Bradley-Terry requires a well-defined "wins/loses" outcome. In subjective domains (creative writing, nuanced analysis), the binary comparator may be inconsistent — what aggregation mechanism replaces it?

## Limitations

- **O(N²) comparisons**: Full Bradley-Terry requires all N×(N-1)/2 pairs. OpenDeepThink mitigates this with rounds (fewer comparisons per round, multiple rounds). Pure N² scaling is prohibitive for large candidate pools.
- **Verifiable-domain restriction**: The strongest results are on tasks with clear ground truth (code, math). Bradley-Terry requires the judge to reliably determine "which is better" — noisy or inconsistent judgments produce nonsense rankings.
- **No step-level credit**: The ranking is at the candidate level; it cannot identify which *step* within a multi-step reasoning trace is load-bearing. PRMs address this differently.
