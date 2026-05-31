---
summary: Transfer learning — applying knowledge from source to target domain; pretrained model adaptation, three transfer regimes, hyperparameter transfer, μP
tags: [machine-learning, transfer-learning, fine-tuning, pretrained-models, domain-adaptation, ml-theory]
updated: 2026-05-31T05:03:53Z
---

---
created: 2026-09-08
updated: 2026-09-08
type: concept
summary: "Transfer learning — applying knowledge from a source domain to improve learning in a target domain; pretrained model adaptation, domain adaptation, and meta-learning"
tags: [machine-learning, transfer-learning, fine-tuning, pretrained-models, domain-adaptation, ml-theory]
status: active
confidence: 0.75
---

# Transfer Learning

## Definition

Transfer learning is the ML paradigm where knowledge acquired while solving one task is leveraged to improve performance on a related, but distinct, target task. Rather than training from scratch, a model initialized with weights learned on a source domain (often a large, general-purpose pretraining task) is adapted to the target domain through additional training.

The core motivation: general-purpose representations learned from abundant, cheap data (e.g., language modeling on web text) contain transferable structural knowledge about syntax, semantics, and world facts that can accelerate learning on specific downstream tasks where labeled data is scarce.

## Three Transfer Regimes

### 1. Domain Adaptation

The source and target tasks are the same (e.g., text classification) but the data distributions differ (e.g., legal documents → medical records). The model keeps its learned task structure but shifts its domain-specific statistics.

Key methods:
- **Full fine-tuning**: Update all parameters on target domain data
- **Feature extraction**: Freeze pretrained layers, train only an added task head
- **Domain-adversarial training**: Align source and target feature distributions

### 2. Task Transfer

Source and target tasks differ but share structural similarities (e.g., language modeling → text summarization). The model keeps its learned representations but must learn a new output structure.

Key methods:
- **Linear probing**: Evaluate frozen pretrained representations on the target task with a linear head (diagnostic of representation quality)
- **Adapter tuning**: Add task-specific modules that learn while keeping the base model frozen
- **Multitask fine-tuning**: Jointly fine-tune on source task + target task data

### 3. Zero/Few-Shot Transfer

The target task has minimal or no training data. The model's pretraining knowledge alone must generalize.

Key methods:
- **Prompt-based transfer**: Engineer prompts to convert target task into pretraining format
- **In-context learning**: Provide task examples in the context window
- **Meta-learning (MAML)**: Learn an initialization that fast-adapts to new tasks with few gradient steps

## The Transfer Learning Landscape in LLMs

### Pretraining → Fine-tuning Pipeline

Modern LLMs follow a two-stage transfer pattern:

```
Pretraining (large corpus, self-supervised) → General-purpose representations
     ↓
Fine-tuning (task-specific, labeled data) → Task-specific performance
```

This is transfer from the pretraining task (often next-token prediction on diverse text) to the target task (e.g., sentiment classification). The quality of transfer depends on:
- **Representation richness**: Did pretraining capture task-relevant structure?
- **Task alignment**: How similar is the target task structure to pretraining?
- **Transfer distance**: How far is the target domain from pretraining distribution?

### Hyperparameter Transfer

[[sources/papers/kalra-barkeshli-hyperparameter-transfer-2026]] provides a quantitative framework for transfer, identifying three metrics:
1. **Quality of scaling law fit**: How well do scaling laws extrapolate from source to target?
2. **Robability to extrapolation errors**: How sensitive is performance to hyperparameter choice in the target regime?
3. **Asymptotic loss penalty**: What is the irreducible loss difference between source and target?

Key finding: the embedding layer learning rate is the critical bottleneck for hyperparameter transfer in standard parameterization — maximizing it dramatically improves transfer quality and training stability.

### Minimal兀 Parameterization (μP)

μP (Maximal Update Parameterization) is a parameterization scheme that ensures hyperparameter transfer is stable across model scales. It normalizes weight updates so that the scale of gradients and updates is constant across layers and width dimensions, enabling the same learning rate to work at all scales. This is particularly important for frontier model training where architecture changes across generations.

## Transfer vs Continual Learning

Transfer learning and continual learning share the concern of avoiding interference between tasks, but differ in framing:

| Dimension | Transfer Learning | Continual Learning |
|-----------|-----------------|-------------------|
| Objective | Optimize target task performance | Maintain performance across all tasks |
| Source access | Source data available during adaptation | Source data may be unavailable |
| Forgetting | Acceptable if target improves | Fundamental problem to solve |
| Typical setting | One-shot or few-shot target adaptation | Sequential multi-task learning |

In LLM development, transfer learning (pretraining → fine-tuning) is the dominant paradigm; continual learning is relevant for ongoing model updates but less central to the standard pipeline.

## Connections

- [[fine-tuning]]: The primary mechanism for transfer in LLMs
- [[parameter-efficient-fine-tuning]]: Transfer via lightweight adapter modules
- [[ml-evolution]]: Transfer as the foundation for autonomous model evolution
- [[kalra-barkeshli-hyperparameter-transfer-2026]]: Quantitative framework for hyperparameter transfer
- [[continual-learning]]: Related but distinct; maintains performance across all tasks
- [[bounded-representation-capacity]]: Transfer efficiency constrained by what can be stored in pretrained weights
