---
created: 2026-05-25
updated: 2026-06-30
type: concept
summary: LLM reasoning — the distinction between pattern matching and genuine multi-step logical inference; chain-of-thought, process reward models, search-augmented reasoning, and the emergent reasoning capabilities that appear at scale
tags: [reasoning, llm, chain-of-thought, process-reward-model, inference-time-compute, reasoning-language-models]
sources: https://arxiv.org/abs/2201.11903 (CoT, Wei 2022), https://arxiv.org/abs/2302.01326 (emergent abilities), https://arxiv.org/abs/2408.03324 (OpenAI o1), https://arxiv.org/abs/2410.01279 (ProcessBench), https://arxiv.org/abs/2505.04057 (o3)
status: active
confidence: 0.82
---

# LLM Reasoning

## Definition

LLM reasoning is the set of capabilities that allow a language model to perform multi-step logical inference — going beyond direct pattern matching to construct and evaluate intermediate representations that support conclusions which are not explicitly present in the input.

The core distinction is between **system-1** (fast, associative, pattern-matching) and **system-2** (slow, deliberate, multi-step inference) cognition. Early LLMs were strong system-1 systems — they could retrieve and interpolate but not truly chain steps. The reasoning capability is the emergence of system-2-like behavior.

## Why It Matters

Reasoning is the bridge from "sophisticated autocomplete" to "genuine problem-solver." The practical significance:

1. **Math and code require multi-step inference**: Neither can be solved by single-token prediction — each step depends on the previous one in ways that require holding intermediate results in context.

2. **Hallucination is system-1 failure**: When a model generates a false claim, it is often retrieving a plausible-sounding pattern rather than inferring from known facts. Reasoning chains create verifiable intermediate steps, making errors detectable.

3. **Test-time compute matters**: Scaling isn't just about training. o1/o3-class models show that inference-time compute — spending more tokens reasoning before answering — produces qualitative improvements that training alone cannot.

4. **Reasoning is the substrate for alignment**: A model that can reason about consequences can evaluate whether its own outputs are honest, safe, and useful. Without reasoning, the model can only pattern-match to "what sounds good."

## The Chain-of-Thought Revolution

### Chain-of-Thought Prompting (Wei et al., 2022)

The key discovery: asking models to produce a reasoning trace before answering significantly improves accuracy on multi-step tasks — even without examples.

```
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls.
   Each can has 3 tennis balls. How many tennis balls does he have now?

A: Roger started with 5 balls. 2 cans × 3 balls = 6 more balls.
   5 + 6 = 11 balls. The answer is 11.
```

The intermediate tokens (the "chain") serve two purposes:
- They force the model to construct intermediate representations that are verifiable
- They effectively allocate more inference-time compute to the problem

This was surprising because the model was not trained to reason explicitly — it emerged at scale. Smaller models (<10B parameters) do not show this improvement consistently.

### Why CoT Works: The Grokked Reasoning Hypothesis

Recent analysis (June 2025) suggests CoT works by "grokked reasoning" — the model learns to encode multi-step inference patterns in its weights during pre-training, but only generalizes these patterns correctly at sufficient scale. At smaller scales, the model memorizes CoT-shaped surface patterns without underlying logical structure.

## Reasoning Models vs Base Models

### The o1/o3 Class (OpenAI 2024–2025)

OpenAI's o1 (September 2024) introduced test-time compute scaling: the model produces an internal reasoning trace before answering, using substantially more inference compute than standard models. Key properties:

- **Reasoning as a learned skill**: Unlike CoT prompting (which is prompted), o1's reasoning behavior appears to be trained into the model via reinforcement learning on reasoning tasks
- **Process reward signals**: o1 was trained with process-level reward signals — not just outcome reward — which produces more coherent reasoning chains
- **Benchmark performance**: o1 achieved 83% on AIME (American Invitational Mathematics Examination), compared to ~44% for GPT-4o at the same time

o3 (early 2025) extended this substantially:
- 87.5% on ARC-AGI
- 25/25 on FrontierMath (a benchmark previously near 0%)
- o3-mini variants offered reasoning quality tradeoffs at lower compute cost

### The Broader Landscape

Google DeepMind's Gemini Thinking, Anthropic's Claude with extended thinking, and open-source models (DeepSeek-R1, QwQ-32B) followed. The common thread: reasoning chains that allocate test-time compute to hard problems, rather than treating all tokens equally.

## Process Reward Models and Search-Augmented Reasoning

### Process Reward Models vs Outcome Reward Models

Standard RLHF uses **outcome reward models (ORMs)** — the reward is assigned only at the final answer. This is insufficient for reasoning because:
- A wrong final answer gets the same reward as no answer at all
- The model cannot learn which intermediate steps were valuable
- Credit assignment across long reasoning chains is noisy

**Process reward models (PRMs)** assign rewards at each step of the reasoning chain, enabling:
- Learning from partial progress (a wrong step followed by recovery is less penalized than a wrong final answer)
- Better credit assignment in search
- Human-interpretable reasoning traces

### SD-Search (MA et al., 2026)

SD-Search is an on-policy hindsight self-distillation approach for step-level credit assignment in search-augmented reasoning:

- The model searches multiple reasoning paths for a given problem
- A PRM scores each step in each path
- On-policy updates refine the model's reasoning process, not just its outcome
- This closes the loop between search (exploration) and learning (credit assignment)

### ProcessBench (2024)

ProcessBench evaluates process reward models by asking: "Can we detect which specific step in a reasoning chain caused an incorrect final answer?" It found that:

- Most PRMs struggle to pinpoint the exact failing step
- The hardest cases are those where a reasoning chain looks locally correct but contains a subtle error 3-4 steps before the conclusion
- Current PRMs have ~60% accuracy at step-level error detection

## Limitations of LLM Reasoning

### Hallucination in Intermediate Steps

Chain-of-thought reasoning generates intermediate tokens that can themselves be hallucinated. The model may construct a reasoning chain where each step individually looks plausible, but the chain leads to a false conclusion because one intermediate step was false. This is harder to detect than a flat hallucination because the false step is embedded in valid-looking reasoning.

### brittleness under distribution shift

LLM reasoning is brittle to superficial changes in problem framing. The same logical problem presented with different surface features (different names, different irrelevant details) can produce dramatically different success rates. This suggests the reasoning is not fully abstract — it is entangled with surface pattern matching.

### Halliday's Mathematical Reasoning Gap

Thomas Halliday's research (2025) demonstrates that even frontier models fail systematically on mathematical reasoning tasks that require:
- Tracking multiple interdependent variables across long chains
- Backtracking when a hypothesis is disproved
- Recognizing when a problem is underdetermined

These are tasks humans handle routinely. The failure mode is not inability to perform individual steps, but inability to manage the search process over reasoning space.

### Lack of Metacognitive Monitoring

Most current reasoning models do not monitor their own confidence at the step level. They generate reasoning chains as if all steps have equal epistemic weight, rather than flagging uncertainty. ProcessBench and similar work is beginning to address this.

## Connections
- [[log]]
- [[concepts/parallel-reasoning]]
- [[concepts/why-llms-arent-scientists-yet]]
- [[concepts/creativity]]
- [[concepts/llm-reasoning]]
- [[concepts/adaptive-computation]]
- [[concepts/chain-of-thought]]
- [[concepts/agentic-reasoning]]
- [[concepts/multi-agent-reasoning]]
- [[concepts/latent-reasoning]]
- [[concepts/shorthand-for-thought]]
- [[wiki/index]]
- [[concepts/generative-ai]]
- [[concepts/imagination]]
- [[concepts/llm-reasoning]]

- [[mixture-of-experts]] — architectural substrate for scaling parameter count; route collapse under RLHF affects reasoning model fine-tuning
- [[process-reward-model]] — the reward mechanism needed for coherent reasoning chain learning
- [[reinforcement-learning-from-human-feedback]] — training paradigm that enables reasoning model training
- [[scaling-laws]] — emergent reasoning abilities appear non-linearly at scale; test-time compute adds a second scaling axis
- [[in-context-learning]] — the broader in-context capability from which CoT emerges
- [[adaptive-computation]] — reasoning models are a form of adaptive computation: more tokens for harder problems
- [[self-correction]] — the related capability of detecting and repairing reasoning errors mid-chain
- [[latent-reasoning]] — the distinction between explicit CoT and implicit reasoning encoded in hidden states
- [[world-model]] — reasoning requires a world model to avoid generating logically inconsistent chains

- [[parallel-reasoning]]
- [[imagination]]
- [[multi-agent-reasoning]]
- [[generative-ai]]
- [[creativity]]
- [[chain-of-thought]]
- [[agentic-reasoning]]
## Open Questions

1. **Abstraction**: Can reasoning be disentangled from surface pattern matching, or is it always entangled? Current evidence suggests partial disentanglement at scale.

2. **Metacognition**: How do you give a model accurate confidence estimates about its own reasoning steps, not just its final answer?

3. **Test-time compute scaling laws**: What is the functional form of reasoning improvement as inference-time compute increases? Is there a ceiling?

4. **Reasoning about code**: Code execution provides natural step-level feedback. Does this make code a superior training domain for reasoning compared to math?
