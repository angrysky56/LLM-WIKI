---
created: 2026-05-29
updated: 2026-07-21
type: concept
summary: Continual learning — ML paradigm where models learn continuously without catastrophic forgetting; regularization, architectural, and memory-based approaches
tags: [machine-learning, llm-training, continual-learning, catastrophic-forgetting, regularization, modular-learning]
sources: []
status: active
confidence: 0.75
---

# Continual Learning

## Definition

Continual learning (also called lifelong learning or incremental learning) is the machine learning paradigm where a model learns from a stream of tasks or experiences over time, without forgetting what it learned on previous tasks. The goal is to achieve *positive forward transfer* (learning new things helps performance on old things) while avoiding *negative backward transfer* (learning new things harms performance on old things).

The fundamental tension: standard gradient-based optimization has no mechanism to protect previously acquired knowledge. When a model trains on new data, weight updates optimize for the new objective with no inherent pressure to preserve old task performance. This is the **catastrophic forgetting** problem.

## The Three Paradigms

### Weight-Level Approaches (Regularization)

Add an explicit penalty to the loss function that discourages weight changes important for prior tasks.

| Method | Mechanism | Key Property |
|--------|-----------|--------------|
| **EWC** (Elastic Weight Consolidation) | Fisher information–based regularization | Rigorous per-weight importance |
| **SI** (Synaptic Intelligence) | Path-integral–based importance along learning trajectory | Online-compatible |
| **Rwalk** (Riemann Walk) | Combines Fisher and path integral | Better theoretical grounding |
| **KL-regularization** | Penalizes divergence from old policy (used in RLHF) | Soft constraint on old knowledge |

### Architectural Approaches

Modify the model architecture to allocate separate resources for different tasks.

| Method | Mechanism | Key Property |
|--------|-----------|--------------|
| **Progressive Networks** | Add new columns for new tasks, freeze old columns | No forgetting by construction; unbounded growth |
| **Control LLM** | Split layers into frozen (prior) and trainable (new) branches | Structural separation of knowledge |
| **Modular architectures (MoE)** | Different experts for different tasks | Experts don't interfere if routing is stable |
| **Low-rank adaptation (LoRA)** | Inject trainable low-rank matrices per task | Compact task-specific parameters |

### Memory-Based Approaches

Store representatives of old data and replay them during new training.

| Method | Mechanism | Key Property |
|--------|-----------|--------------|
| **Experience replay** | Store raw examples from old tasks | Simple but storage scales |
| **Generative replay** | Use a generative model to produce synthetic old-task examples | No raw storage |
| **Knowledge distillation** | Use old model's predictions as soft labels for new training | Preserves old model's behavior |
| **Memory-Oriented Programming (MOP)** | Offload old knowledge to external schema memory | Separates storage from computation entirely |

## The Forgetting Spectrum

Not all forgetting is catastrophic. There's a spectrum:

1. **Catastrophic forgetting**: Complete loss of prior task performance after training on new task
2. **Benign forgetting**: Prior performance degrades but remains acceptable
3. **Selective forgetting**: Agent intentionally removes outdated/harmful knowledge
4. **No forgetting**: Perfect preservation of all prior knowledge (the goal)

The boundary between "benign" and "catastrophic" depends on the deployment requirements. For safety-critical applications, even marginal degradation may be unacceptable.

## Connection to MOP

Memory-Oriented Programming (MOP) offers a fundamentally different approach to the forgetting problem: instead of trying to preserve old knowledge in weights, MOP **offloads knowledge to external memory**. The agent's schema layer replaces weight consolidation with structured retrieval.

The MOP perspective reframes the question: rather than "how do we prevent weights from forgetting?", ask "should weights remember everything, or should they delegate long-term knowledge to external memory?" The RAM-cache analogy — a bounded cache cannot hold all information; explicit eviction and retrieval policies are needed.

## Relationship to LLM Training

For large language models specifically, continual learning manifests in several scenarios:

- **Instruction tuning**: Adding new capabilities without degrading existing ones
- **Alignment training**: Improving safety/helpfulness tradeoffs without regression
- **Domain adaptation**: Specializing for medical/legal/code domains without losing general capabilities
- **Personalization**: Adapting to individual user preferences over time

All of these face the same fundamental tension: optimizing for new behavior while preserving old behavior that may share representational structures in the model.

## Open Questions

1. **Task boundary detection**: Real-world data doesn't come with task labels. How does a continual learning system detect when it's dealing with a "new task" vs. a continuation of an old one?

2. **Compositional generalization**: Can continual learning systems learn to compose knowledge from different tasks in ways not seen during training?

3. **When to compress vs. when to freeze**: MOP raises a deep question — when should an agent compress experience into memory vs. consolidate it into weights? The right answer depends on expected reuse frequency and generalization required.

4. **The interference-structure relationship**: Some architectures are more robust to catastrophic forgetting than others. Is there a fundamental structural property that predicts susceptibility?

5. **Selective forgetting as feature**: In some cases, removing harmful or outdated knowledge is desirable. How do we make forgetting targeted rather than catastrophic?

## Connections
- [[concepts/control-llm]]
- [[concepts/continual-learning]]
- [[scratchpad/agent-sheets/researcher/carryover]]
- [[wiki/index]]
- [[concepts/maximum-occupancy-principle]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-07-20]]
- [[concepts/parameter-efficient-fine-tuning]]
- [[log]]
- [[sources/papers/betteti-baggio-bullo-zampieri-idp-hopfield-2025]]
- [[concepts/lora]]
- [[continual-learning]]

- [[catastrophic-forgetting]]: the central problem continual learning tries to solve
- [[control-llm]]: architectural mitigation for forgetting during weight updates
- [[namm]]: learned cache management as contextual-level continual learning
- [[llm-training]]: the primary application context where forgetting matters for LLMs
- [[mop-architecture]]: Memory-Oriented Programming as a non-weight-based alternative to forgetting
- [[ramirez-ruiz-mop-2024]]: schema-based memory offloading as an alternative to weight regularization
- [[bounded-structured-memory]]: bounded memory design that avoids overwrite through capacity management
- [[mixture-of-experts]]: modular architecture that naturally reduces interference between knowledge domains
- [[parameter-efficient-fine-tuning]]: parameter-efficient methods as a practical approach to task-specific adaptation without full model fine-tuning
- [[betteti-baggio-bullo-zampieri-idp-hopfield-2025]]
- [[concepts/maximum-occupancy-principle]]
- [[lora]]