---
created: 2026-05-23
updated: 2026-07-15
type: concept
summary: Neural Architecture Search — automated methods for discovering optimal neural network architectures; covers CoLLM-NAS, RZ-NAS, LLaMA-NAS, and CMA-ES-driven search
tags: [neural-architecture-search, architecture-discovery, automated-ml, ml-evolution, evolutionary-algorithms]
sources: wiki/sources/articles/ml-evolution-benchmarking-protocol.md
status: active
confidence: 0.75
---

# Neural Architecture Search (NAS)

**Also known as:** NAS, Automated Architecture Design, Architecture Discovery

## What It Is

Neural Architecture Search (NAS) is the automated process of discovering high-performing neural network architectures — replacing manual design with search over a parameterized architecture space. Modern NAS methods span evolutionary algorithms, gradient-based architecture optimization, and reinforcement learning approaches.

Within the [[ml-evolution]] paradigm, NAS is a core use case: evolve architecture subsets within a pretrained model's parameter space, or discover entirely new layer compositions. The key challenge is evaluating architecture candidates without full training — requiring proxy metrics (zero-cost proxies) or weight sharing schemes.

## Core Methods in the ML Evolution Cluster

### CoLLM-NAS (Collaborative LLM NAS)

**CoLLM-NAS** uses a dual-LLM mechanism that separates strategic exploration from tactical generation:
- **Navigator LLM**: Given a task description and current architecture state, proposes architectural modifications
- **Generator LLM**: Takes the Navigator's proposals and generates concrete architecture candidates (valid layer configurations)

The separation prevents semantic drift and ensures generated candidates are syntactically valid. The Navigator provides strategic guidance ("reduce attention heads in layer 3 to improve compression"); the Generator translates this into a specific sub-network configuration.

This is the same LLM-driven operator principle seen in Guided ML Evolution — LLMs as intelligent mutation generators.

### RZ-NAS (Zero-Cost NAS)

**RZ-NAS** improves search efficiency using zero-cost proxies and a reflection module:
- **Zero-cost proxies**: Metrics that predict architecture quality without training (e.g., score from activation sparsity, gradient covariance, or thermal properties)
- **Reflection module**: A meta-learner that evaluates proxy quality and adjusts proxy weighting across search iterations

Standard NAS requires training each candidate or inheriting weights from a supernetwork — both expensive. Zero-cost proxies evaluate architecture quality in a single forward pass. RZ-NAS adds a reflection mechanism to handle proxy unreliability without abandoning the proxy speed advantage.

### LLaMA-NAS

**LLaMA-NAS** performs one-shot search for task-specific sub-networks:
- Instead of searching the full architecture space, LLaMA-NAS starts from an existing large model (e.g., LLaMA family) and searches for efficient sub-networks tailored to a target task
- Achieves compression and throughput gains simultaneously with task-specific specialization
- One-shot evaluation means the sub-network inherits pretrained weights from the parent, avoiding full retraining

## Architecture Search Space

NAS methods operate over a space of architectural decisions:

| Dimension | Options |
|-----------|---------|
| Depth | Number of layers |
| Width | Hidden dimension per layer |
| Attention | Head count, attention type (multi-head, linear, flash) |
| MoE | Expert count, routing strategy, top-k |
| Activation | ReLU, GeLU, SwiGLU, GeGLU |
| Normalization | LayerNorm, RMSNorm, DeepNorm |

## Proxy Metrics (Zero-Cost)

Zero-cost proxies estimate architecture quality without training:

- **SNIC** (Swift Neural Architecture Identifier with Complexity): Uses activation trajectories
- **NASWOT** (Neural Architecture Search Without Training): Score based on network's handshake graphs
- **GraDes** (Gradient Descent similarity): Measures gradient covariance structure
- **thermal** proxies: Treats network as a physical system; stability correlates with generalization

RZ-NAS's innovation is combining multiple proxies with a reflection module that learns which proxy types are reliable for which architecture families.

## Relationship to Evolutionary Strategies

NAS is a natural application of [[evolutionary-strategies]] — CMA-ES and its variants search efficiently over continuous architecture subspaces. The population of architecture variants is evaluated in parallel, mutations are CMA-adapted based on fitness correlations, and selection pressure converges to high-performing architectures.

## Connections
- [[concepts/maximum-occupancy-principle]]
- [[concepts/collm-nas]]
- [[log]]
- [[sources/articles/ml-evolution-benchmarking-protocol]]
- [[scratchpad/agent-sheets/researcher/carryover]]
- [[wiki/index]]
- [[concepts/llama-nas]]
- [[concepts/rz-nas]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-08-03]]
- [[concepts/neural-architecture-search]]
- [[concepts/bounded-memory-budget-optimization]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-07-15]]
- [[concepts/essa]]
- [[concepts/neural-architecture-search]]

- [[ml-evolution-benchmarking-protocol]] — source for CoLLM-NAS, RZ-NAS, LLaMA-NAS
- [[ml-evolution]] — NAS is the primary application of guided ML evolution
- [[evolutionary-strategies]] — the optimization engine underlying architecture search
- [[collm-nas]] — dual-LLM Navigator/Generator architecture
- [[rz-nas]] — zero-cost proxy + reflection module
- [[llama-nas]] — one-shot sub-network search from large models
- [[essa]] — gradient-free singular-value alignment; analogous philosophy to RZ-NAS's zero-cost proxies
- [[qes]] — residual correction for quantized fine-tuning; parallel to RZ-NAS's proxy accuracy problem
- [[scaling-laws]] — architecture search interacts with scaling laws; discovered architectures must be evaluated relative to their compute budget
- [[catastrophic-forgetting]] — architectural changes can cause forgetting; search must preserve capability

- [[concepts/maximum-occupancy-principle]]
- [[bounded-memory-budget-optimization]]
## Open Questions

1. CoLLM-NAS's dual-LLM approach requires two capable LLMs — does Navigator/Geneerator specialization improve over single-LLM proposals?
2. RZ-NAS's reflection module: is it learned once and reused, or fine-tuned per architecture family?
3. LLaMA-NAS compression gains: do they hold at frontier model scale, or only for already-compressed models?
4. Can zero-cost proxies be combined with [[mop-architecture]]'s exploration objective for curiosity-driven architecture search?
