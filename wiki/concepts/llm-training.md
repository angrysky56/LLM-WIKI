---
created: 2026-06-17
updated: 2026-05-26
type: concept
summary: LLM training — pre-training, fine-tuning, continual learning, and catastrophic forgetting mitigation for large language models
tags: [llm, training, fine-tuning, continual-learning, rlhf, grpo]
sources: []
status: active
confidence: 0.75
---

# LLM Training

## Definition

LLM training encompasses all stages of developing a large language model — from initial pre-training through instruction tuning and alignment, to ongoing continual learning. Each stage has distinct objectives, data requirements, and optimization strategies. The training pipeline shapes what the model can do and how it behaves.

## Pre-Training

### Unsupervised Language Modeling

Pre-training trains the model to predict the next token given a large corpus of unlabeled text. The objective is simple: minimize perplexity on the training distribution. What emerges is a rich representations of language — syntactic structure, semantic relationships, world knowledge encoded in the weights.

The scaling laws governing pre-training (Kaplan et al., Chinchilla) determine the optimal allocation of compute among model size, training tokens, and architecture choices.

### Emergent Capabilities

Pre-training produces emergent capabilities — abilities that appear suddenly at scale rather than developing gradually. The relationship between model size, training tokens, and capability emergence is not smooth; certain thresholds trigger qualitatively new behaviors.

## Fine-Tuning

### Instruction Tuning

After pre-training, models are fine-tuned on instruction-response pairs to learn to follow instructions. This transforms a raw language model (which just completes text) into an instruction follower. The key challenge is maintaining the general capabilities from pre-training while adding instruction-following behavior.

### Catastrophic Forgetting

Fine-tuning risks catastrophic forgetting — updating the model on a new task degrades performance on previously learned tasks. The model "overwrites" relevant weights. Mitigation strategies include:

- **Regularization**: Constrain weight changes to minimize deviation from the pre-trained model
- **Rehearsal**: Interleave old task examples during new training
- **Elastic weight consolidation (EWC)**: Identify and protect weights that are important for old tasks
- **Mixture of Experts (MoE)**: Modular architecture where different experts handle different tasks, reducing interference

### RLHF and GRPO

**Reinforcement Learning from Human Feedback** (RLHF) fine-tunes a pre-trained model using a reward model trained on human preference data. The standard pipeline:

1. Collect comparison data (given X, prefer response A over B)
2. Train a reward model on the comparisons
3. Fine-tune the base model using the reward model as signal (typically via PPO)

**Group Relative Policy Optimization** (GRPO) is a simplified variant that replaces the reference model with group-relative advantage estimation — no reference model needed, reducing memory and compute requirements. GRPO is structurally compatible with MoE because it doesn't require the KL penalty against a reference model (which would double the memory footprint in MoE).

## Continual Learning

The goal of continual learning is to update a model with new information without forgetting old information — the core challenge of lifelong learning in LLMs.

### Key Approaches

- **Regularization-based**: Protect important weights (EWC, SI, Rwalk)
- **Replay-based**: Replay samples from old tasks while learning new ones
- **Knowledge distillation**: Use the old model as a teacher for the new model
- **Modular approaches**: Add new modules for new knowledge without modifying existing weights

### The Scaffolding Problem

A key tension in continual learning: do we learn by adding new weights (scaffolding), or by compressing existing representations? The brain appears to use both — adding new neurons over the lifespan while also forming new synaptic connections. LLMs lack this biological flexibility, making catastrophic forgetting a more severe problem.

## Connections
- [[concepts/continual-learning]]
- [[concepts/lora]]
- [[concepts/quantization]]
- [[concepts/instruction-tuning]]
- [[concepts/reinforcement-learning-from-human-feedback]]
- [[concepts/group-relative-policy-optimization]]
- [[concepts/qes]]
- [[concepts/control-llm]]
- [[wiki/index]]
- [[concepts/catastrophic-forgetting]]
- [[concepts/llm-training]]
- [[concepts/parameter-efficient-fine-tuning]]
- [[log]]
- [[concepts/llm-training]]

- [[catastrophic-forgetting]]: the core problem of continual learning
- [[control-llm]]: controlling LLM behavior during and after training
- [[group-relative-policy-optimization]]: simplified RLHF variant
- [[reinforcement-learning-from-human-feedback]]: standard alignment pipeline
- [[mixture-of-experts]]: architectural approach to mitigating interference
- [[agent-onboarding]]: the applied problem of integrating new capabilities into an agent

- [[continual-learning]]
- [[parameter-efficient-fine-tuning]]
- [[quantization]]
- [[lora]]
- [[instruction-tuning]]
- [[qes]]
## Open Questions

1. **Catastrophic forgetting mechanisms**: Is the degradation in old tasks due to weight interference, or due to the optimization objective not valuing those tasks? Can we selectively protect task-critical representations?

2. **Scaffolding vs compression**: Is the brain's dual strategy (new neurons + synaptic plasticity) the right model, or can we achieve continual learning through weight consolidation alone?

3. **GRPO + MoE interaction**: GRPO's compatibility with MoE is structural, but does GRPO training cause routing collapse (experts becoming unused) in MoE architectures? This is an active empirical question.

4. **Measuring forgetting before it happens**: Can we predict which weights will be disrupted by a new fine-tuning run? Probing methods might detect vulnerable representations before catastrophic forgetting occurs.