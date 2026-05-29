---
created: 2026-05-29
updated: 2026-05-29
type: concept
summary: The ability of language models to learn tasks from examples in context without any parameter updates — the core mechanism behind few-shot prompting
tags: [llm, learning, prompting, in-context-learning, reasoning]
sources: https://arxiv.org/abs/2005.14165, https://arxiv.org/abs/2104.01286, https://arxiv.org/abs/2210.03629
status: active
confidence: 0.9
---



# In-Context Learning

**In-Context Learning (ICL)** is the capability of language models to perform new tasks given only a few examples in the input prompt — without any gradient updates or parameter changes. The model reads the examples, infers the pattern, and applies it to a test case.

This is distinct from traditional machine learning where a model is fine-tuned on examples. In ICL, the examples are part of the *context* — they shape the model's output within a single inference call.

## Definition

Formally: given a prompt containing K demonstration examples `{(x₁, y₁), ..., (x_k, y_k)}` and a query input `x_{k+1}`, the model predicts `y_{k+1}` by reasoning over the demonstration pairs. The model never updates its weights — the learning happens entirely in the forward pass.

The key mechanism is that transformers perform *in-context estimation*: the attention heads condition on the entire sequence of demonstrations simultaneously, learning to map input patterns to outputs.

## Why It Matters

ICL is the foundation of few-shot prompting and the reason large language models are general-purpose:

- **Zero adaptation cost**: No fine-tuning required. Every new task is just a different prompt.
- **Task composition**: A single model can handle translation, summarization, coding, and math — the same weights, different prompts.
- **Human-legible**: Demonstrations are plain text — non-technical users can teach models new behaviors by providing examples.

Without ICL, each task would require a specialized model or expensive fine-tuning. With ICL, one model serves as a platform.

## The Mechanism

### Early Views (2020–2022)

The original GPT-3 paper (Brown et al., 2020) introduced ICL as an empirical observation: models trained for next-token prediction naturally acquire the ability to condition on in-context examples. The explanation was that the model's pre-training on diverse text implicitly taught it to infer tasks from textual patterns.

Gpt-3's in-context learning showed that performance improves with more demonstrations (K) up to a ceiling, and that performance is sensitive to the format and ordering of examples.

### Attention-based Explanation

Follow-up work (Garg et al., 2022; von Oswald et al., 2023) proposed that the transformer's attention heads implement a form of *Bayesian regression* over the demonstration surface. Each attention head effectively computes a weighted average of the label vectors from the K examples, where the weights depend on the query's similarity to each example's input.

This means the model isn't "memorizing" the examples — it's computing a function of them at inference time. The function is determined by the weights that were trained during pre-training.

### What Enables ICL

Research has identified several pre-training factors that affect ICL quality:

| Factor | Effect |
|
--|
--|
| **Training data diversity** | More diverse pre-training data → stronger ICL |
| **Model scale** | ICL ability emerges roughly around 10B parameters |
| **Next-token prediction objective** | The standard pre-training objective is sufficient; no special loss needed |
| **Attention pattern** | The ability to selectively attend to relevant examples is critical |

### Relationship to Fine-Tuning

ICL and fine-tuning represent two ends of a spectrum:

| | In-Context Learning | Fine-Tuning |
|--|
|
-|
| **Updates** | Zero | Gradient-based weight changes |
| **Speed** | Instant (new prompt) | Hours to days |
| **Cost** | Cheap per-task | Expensive per-task |
| **Data needed** | Few examples (K) | Thousands of examples |
| **Catastrophic forgetting** | None | Risk during fine-tuning |
| **Task specificity** | High (prompt controls) | High (weights encode) |

The field has also explored *in-context fine-tuning* (ICT) — updating the weights using examples in context — which blends both properties.

## Key Results

| Finding | Paper | Result |
|
|
-|
--|
| ICL emerges at scale | GPT-3 (2020) | 175B model shows strong few-shot on 40+ tasks |
| Transformers implement Bayesian regression | von Oswald et al. (2023) | Attention heads compute linear regression over examples |
| ICL vs fine-tuning comparison | Singh et al. (2024) | Fine-tuning outperforms ICL on niche tasks; ICL better on diverse distributions |
| In-context learning of algorithms | Garg et al. (2022) | Transformers can learn simple algorithms (sorting, DFS) from examples |

## Connections
- [[concepts/emergence]]
- [[concepts/causal-reasoning]]
- [[wiki/index]]
- [[sources/articles/titans-test-time-memory]]
- [[log]]
- [[concepts/load-bearing-reasoning]]
- [[concepts/creativity]]
- [[concepts/in-context-learning]]
- [[concepts/inference-time-compute-scaling]]
- [[concepts/generative-ai]]
- [[sources/repositories/tabpfn]]
- [[concepts/chain-of-thought]]
- [[concepts/reward-modeling]]
- [[concepts/transformer-architecture]]
- [[scratchpad/jobs/reports/librarian/audit-2026-05-23]]
- [[concepts/scaling-laws]]
- [[concepts/llm-reasoning]]
- [[in-context-learning]]

- [[scaling-laws]] — ICL ability scales with model parameters; a power-law relationship between scale and ICL performance
- [[inference-time-compute-scaling]] — ICL examples are part of the input; longer context means more compute per token
- [[chain-of-thought]] — CoT is a form of ICL where the examples demonstrate reasoning steps
- [[reward-modeling]] — Reward models must learn from few examples via ICL to score new generations
- [[load-bearing-reasoning]] — ICL is the substrate for the "thinking" that happens in agentic loops
- Concept: [[causal-reasoning]]
- Concept: [[emergence]]
- Concept: [[titans-test-time-memory]]
- Concept: [[transformer-architecture]]


- [[llm-reasoning]]
- [[generative-ai]]
- [[creativity]]
## Open Questions

1. **Theoretical foundation**: Why does next-token prediction pre-training give rise to in-context learning? The connection is empirical, not theoretical.

2. **ICL reliability**: ICL is sensitive to example ordering, format, and the K-shots used. When does it fail systematically?

3. **Compositional generalization**: Can ICL handle compositions of concepts not seen together in demonstrations? Early evidence suggests it's limited — models struggle when the combination requires genuinely novel reasoning.

4. **Relation to in-memory learning**: Is ICL doing something functionally similar to episodic memory retrieval in the brain, or is it a different mechanism entirely?

## Limitations

- **Finite context**: The number of examples K is limited by context window size. Very K-shot learning (K > 1000) is infeasible.
- **Position sensitivity**: Examples near the start or end of the context are weighted differently; ordering affects performance non-monotonically.
- **No persistent task encoding**: Each prompt must include all examples. There's no way to "remember" a learned task across separate conversations except by re-including examples.
- **Scale requirement**: ICL emerges meaningfully only around 10B parameters for most tasks. Smaller models show weak or inconsistent ICL.
- **Brittle under distribution shift**: If the test input is very different from the demonstration examples, ICL breaks down even for large models.