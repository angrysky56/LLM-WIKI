---
created: 2026-05-21T08:30:00Z
updated: 2026-05-21T08:30:00Z
type: concept
summary: Allocating inference-time compute to improve reasoning quality — the frontier of scaling laws beyond training
tags: [llm-architecture, inference, reasoning, test-time-compute, scaling-law]
status: active
confidence: 0.85
sources: https://arxiv.org/abs/2504.02495, https://arxiv.org/abs/2505.12225v1, https://arxiv.org/abs/2605.15177
---



# Inference-Time Compute Scaling

The practice of allocating variable amounts of computational resources at inference time to improve reasoning quality — representing a second axis of scaling beyond the training compute that dominated LLM development from 2020–2024.

## Definition

Inference-time compute scaling (also called **test-time compute scaling** or **thinking budget allocation**) refers to techniques that increase the computational effort expended when processing a single input, rather than increasing model size or training data. Where traditional scaling laws focused on "how much training compute?", inference-time scaling asks "how much inference compute per token?"

The canonical implementation is **Best-of-N (BoN) sampling**: generate N candidate responses, score each with a reward model, return the highest-scoring. The cost scales linearly with N, but the quality gain follows a sublinear curve — the 8th response is likely better than the 1st, but the 1000th yields diminishing returns.

## Why It Matters Now

The field shifted around 2024–2025 for several converging reasons:

1. **Training scaling plateaus**: GPT-4 class performance was reached with 7B–13B models (e.g., Llama 3, Mistral) on compute-optimal training. Further gains required something beyond raw training compute.

2. **Benchmark saturation**: On math (MATH, GSM8K), coding (HumanEval, Codeforces), and science (GPQA), frontier models achieved 85–95% accuracy. Marginal gains in training translated to large capability gaps on hard tasks — making inference-time optimization more valuable.

3. **Reward model efficiency**: ELHSR and similar approaches reduced the cost of scoring from a 7B-parameter model to a ~270K-parameter linear projection over hidden states, making BoN economically viable at scale.

4. **Verified reasoning demands**: As LLMs were deployed for code generation, mathematical proof, and scientific discovery, the cost of a wrong answer became high enough to justify multiple generative attempts.

## Approaches

### Best-of-N (Rejection Sampling)

The simplest form. Generate N completions, rank by reward model, return best. Gains are monotonic but concave — diminishing returns after N=16–64 depending on task difficulty.

**Key papers:**
- ELHSR (2025): Hidden-state reward model achieves 57.5% on MATH with BoN vs 52.9% baseline
- OpenDeepThink (2026): Bradley-Terry pairwise aggregation adds +405 Codeforces Elo in 8 rounds

### Process Reward Models vs Outcome Reward Models

The distinction matters enormously for inference-time scaling:

| Type | What it scores | Precision | Cost |
|
|
|
--|
|
| **Outcome Reward Model (ORM)** | Final answer only | Binary correct/incorrect | Lower — fewer decisions |
| **Process Reward Model (PRM)** | Each reasoning step | Token-level credit | Higher — per-token scoring |

PRMs enable smarter search: instead of generating N full responses and ranking them, an agent canprune reasoning paths at intermediate steps (beam search over reasoning steps rather than completion ranking). This is the insight behind systems like StepSearch and SD-Search.

**SD-Search** (arXiv:2605.18299, May 2026) provides the most compelling demonstration: matching 72B-teacher process supervision with a 3B model using no external teacher. The process-level signal comes from the policy's own token distributions under a "hindsight block" — aggregating sibling rollouts and their CORRECT/INCORRECT outcomes. The JSD between student and teacher distributions functions as an implicit PRM.

### Beam Search over Reasoning Steps

More sophisticated than BoN: maintain multiple active reasoning paths (beams), score each at each step, prune the lowest-scoring. The branching factor at each step determines the compute budget. Key challenge: ensuring the reward signal at intermediate steps is reliable enough to not prune the eventual correct path.

### Inference-Time Compute Allocation Strategies

Research from 2025–2026 has identified several allocation strategies:

1. **Fixed预算 (Fixed budget)**: Allocate N tokens regardless of problem difficulty. Wasteful on easy problems, insufficient on hard ones.

2. **Adaptive budget**: Use a small model or hidden-state signal to estimate problem difficulty first, then allocate compute proportionally. ELHSR's gating mechanism is a lightweight version of this.

3. **Verifier-guided search**: Train a separate verifier (often smaller than generator) to assess partial solutions, guiding the allocation decision at each step.

4. **Self-reflection based**: Have the model assess its own confidence at intermediate steps and decide whether to continue, backtrack, or try an alternative approach.

### Economics of Inference-Time Compute

The decision to spend inference-time compute is fundamentally an economic trade-off between four variables:

| Variable | Description | Typical Range |
|
|
-|
|
| **Error cost** | Cost of delivering a wrong answer | Domain-dependent: low for闲聊, extremely high for medical/coding |
| **Compute cost** | $ per token of inference | GPU cost / throughput; ~$0.001–0.01 per 1K tokens |
| **Accuracy gain** | Delta in task accuracy from BoN vs single-pass | Task-dependent; 0–15% for math/code |
| **Latency budget** | How much latency the application can tolerate | Hard real-time: none; batch: unlimited |

**The decision rule:** Inference-time compute is worth it when `error_cost × accuracy_gain > compute_cost`. This is why the economics shift dramatically by domain:

- **High error cost + verifiable domains** (code generation, math, legal reasoning): BoN-64 with PRM-guidance is almost always justified. A wrong function call in production can cost hours of debugging.
- **Low error cost + subjective domains** (chat, creative writing, summarization): Single-pass generation dominates. The "right" answer is not verifiable and errors don't compound.
- **Medium error cost + verifiable** (fact QA, classification): ELHSR-style adaptive allocation with a lightweight gating model is the sweet spot — spend compute only on questions that are genuinely hard.

**Compute-optimal inference budget** (when to stop scaling N):

For a task with baseline accuracy `A₀` and per-attempt accuracy `p`, BoN with N attempts yields final accuracy:

`A_N = 1 - (1-p)ⁿ`

The marginal accuracy gain from adding attempt N is:

`ΔA = (1-p)ⁿ⁻¹ × p`

The marginal compute cost is constant. Diminishing returns set in when the marginal gain falls below the cost-per-attempt in accuracy units. Empirically, for math reasoning (p ≈ 0.5 per attempt), the curve flattens around N = 16–64 depending on model quality and problem difficulty.

**Implications for Hermes deployment:**

For a personal AI agent handling a mix of tasks:
- **Tool calls and code generation**: Run BoN-16 to BoN-32 with hidden-state gating. Error recovery cost is high enough to justify the compute.
- **Research and synthesis tasks**: PRM-guided beam search with wider branching on hard sub-problems; single-pass on straightforward queries.
- **Casual conversation**: No inference-time scaling — single-pass is fine.
- **Long-context reasoning** (multi-document synthesis): Nested BoN where the verifier scores both individual retrieved documents and final synthesis.

## Key Results

| Method | Model Scale | Benchmark | Result | External Teacher |
|
--|
-|
--|
--|
--|
| ELHSR + BoN | 3B | MATH | 57.5% | None |
| SD-Search | 3B | Multi-hop avg | 0.428 EM | None (self-distilled) |
| SD-Search | 7B | Multi-hop avg | 0.476 EM | None |
| OpenDeepThink | Gemini 3.1 Pro | Codeforces Elo | +405 pts | None |
| Thinker | 72B | Multi-hop avg | 0.430 EM | 72B teacher |

## Connections
- [[concepts/kv-cache]]
- [[concepts/in-context-learning]]
- [[concepts/group-relative-policy-optimization]]
- [[concepts/hidden-states]]
- [[concepts/chain-of-thought]]
- [[concepts/llm-inference]]
- [[concepts/reward-modeling]]
- [[concepts/taylors-law]]
- [[concepts/load-bearing-reasoning]]
- [[concepts/reward-hacking]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-05-21]]
- [[concepts/mop-and-rlhf-interaction]]
- [[concepts/inference-time-compute-scaling]]
- [[concepts/mixture-of-experts]]
- [[concepts/process-reward-model]]
- [[index]]
- [[concepts/hybrid-reward-models]]
- [[concepts/model-serving]]
- [[concepts/bradley-terry]]
- [[log]]
- [[scratchpad/agent-sheets/librarian/carryover]]
- [[concepts/parallel-reasoning]]
- [[concepts/scaling-laws]]
- [[inference-time-compute-scaling]]

- [[reward-modeling]] — BoN is the primary application; ORM vs PRM distinction is central
- [[hidden-states]] — ELHSR extracts reward signals from hidden states
- [[chain-of-thought]] — reasoning traces are what get scored; longer chains benefit more from compute allocation
- [[load-bearing-reasoning]] — identifying which tokens in a reasoning trace are load-bearing vs scaffolding
- Concept: [[group-relative-policy-optimization]]
- Concept: [[hybrid-reward-models]]
- Concept: [[in-context-learning]]
- Concept: [[kv-cache]]
- Concept: [[llm-inference]]
- Concept: [[mixture-of-experts]]
- Concept: [[mop-and-rlhf-interaction]]
- Concept: [[process-reward-model]]
- Concept: [[reward-hacking]]
- Concept: [[scaling-laws]]
- Concept: [[taylors-law]]


- [[model-serving]]
- [[parallel-reasoning]]
- [[bradley-terry]]
## Open Questions

1. **Optimal budget allocation**: What is the right compute budget for a given problem difficulty? Current approaches are heuristic — adaptive gating models show promise but no unified theory exists.

2. **PRM reliability**: Process reward models are expensive to train and easy to overfit. How do we get reliable step-level signals without human annotation?

3. **Diminishing returns curve**: At what N does BoN stop being worth the compute? It varies by task and model. No unified theory — empirical curves suggest N=16–64 depending on difficulty and model quality.

4. **Combining BoN with architectural improvements**: Most research treats inference-time scaling as orthogonal to model architecture. Can we design architectures that are more efficient to scale at inference time?

## Limitations

- **Not universally applicable**: On creative writing, opinion tasks, or other subjective domains, reward signals are weak and inference-time scaling provides little benefit.

- **Latency tradeoff**: BoN with N=64 means 64x latency. For real-time applications, this is often prohibitive.

- **Reward model quality ceiling**: If the reward model scores incorrectly, BoN selects the worst response. The ceiling is the ceiling of your reward model.

- **Diminishing returns**: The sublinear gain curve means exponential inference budget yields only polynomial quality gains — a fundamental constraint.