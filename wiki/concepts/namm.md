---
created: 2026-06-17
updated: 2026-07-21
type: concept
summary: NAMM — Neural Attention Memory Models that replace heuristic KV cache rules with learned retention strategies; architectural alternative to Control LLM for managing forgetting in LLMs
tags: [kv-cache, attention, memory-model, llm-inference, ml-evolution, catastrophic-forgetting, continual-learning]
sources: wiki/sources/articles/ml-evolution-benchmarking-protocol.md
status: active
confidence: 0.75
---

# NAMM

## Definition

NAMM (Neural Attention Memory Models) are a class of learned memory models that replace heuristic KV cache eviction policies with trainable retention strategies. Rather than using fixed rules (e.g., LRU, sliding window) to decide which key-value pairs to keep in the attention cache, NAMM learns which past tokens are worth attending to based on the current context.

The core motivation: standard KV cache management uses handcrafted eviction heuristics that don't adapt to the specific structure of a given model's attention patterns. NAMM replaces this with a learned controller that decides cache behavior based on end-to-end training signals.

## Relationship to Control LLM

NAMM and Control LLM both address catastrophic forgetting in LLMs, but through different mechanisms:

| Aspect | Control LLM | NAMM |
|--------|-------------|------|
| **Mechanism** | Architectural bifurcation — frozen vs trainable branches | Learned cache retention — which KV pairs to keep |
| **Target** | Prevents weight updates from overwriting prior knowledge | Prevents old contextual information from being lost |
| **Level** | Weight/model level | Inference/contextual level |
| **Memory cost** | Doubles model size (two branches) | Scales with KV cache budget |
| **Complementary?** | Yes — could be combined | Yes — could be combined |

The critical difference: Control LLM preserves *what the model knows* (weight-level); NAMM preserves *what the model can attend to* (context-level). A model could theoretically use both — Control LLM for weight-level stability and NAMM for context-level retrieval.

## How NAMM Works

A NAMM controller (typically a small neural network) observes:
- Current attention states
- Cache occupancy metrics
- Token importance signals

And outputs a decision for each KV pair: **retain** or **evict**.

The controller is trained jointly with the base model using a loss that balances:
1. Task performance (retain what's relevant for current task)
2. Cache efficiency (evict what's not needed to stay within budget)
3. Retrieval quality (don't evict things that will be needed later)

## Connection to Continual Learning

NAMM is fundamentally a **context-level continual learning** mechanism. It manages the streaming context window as if it were a sequence of learning episodes — deciding what to keep from each "episode" (context window) based on what predicts useful for future episodes.

This is parallel to weight-level continual learning methods, but operates at inference time rather than training time. The advantage: no gradient updates needed, no catastrophic forgetting of weight-level knowledge.

## Limitations

1. **Training complexity**: NAMM requires co-training with the base model or a separate learning phase, adding overhead.

2. **Short-term vs long-term tradeoffs**: The controller optimizes for retention within its training distribution. Novel out-of-distribution contexts may trigger poor retention decisions.

3. **Doesn't address weight-level forgetting**: NAMM preserves context, not weights. A model fine-tuned after context is learned will still suffer forgetting at the weight level.

4. **Budget sensitivity**: Performance depends heavily on the KV cache budget size. Too small and the controller can't keep useful information; too large and the problem is trivial.

## Open Questions

1. **Learned vs heuristic**: Is a learned controller actually better than a well-tuned heuristic for most LLMs? The gap may be small for models with predictable attention patterns.

2. **Cross-task transfer**: Can a NAMM controller trained on one domain transfer to new domains without retraining?

3. **Combining with Control LLM**: Could both mechanisms be used together — Control LLM for weight-level stability and NAMM for context-level retrieval? What does the architecture look like?

4. **Relationship to episodic memory**: NAMM is effectively an episodic memory mechanism operating at the attention level. How does this connect to the MOP schema-based episodic memory?

## Connections
- [[concepts/namm]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-07-20]]
- [[log]]
- [[concepts/rz-nas]]
- [[concepts/kv-cache]]
- [[sources/articles/ml-evolution-benchmarking-protocol]]
- [[concepts/qes]]
- [[concepts/control-llm]]
- [[concepts/continual-learning]]
- [[concepts/llm-inference]]
- [[wiki/index]]
- [[concepts/catastrophic-forgetting]]

- [[kv-cache]]: the underlying mechanism NAMM learns to manage
- [[llm-inference]]: NAMM is an inference-time optimization for memory management
- [[catastrophic-forgetting]]: NAMM addresses forgetting at the contextual level; Control LLM addresses at the weight level — both are mitigation strategies from the same source
- [[control-llm]]: architectural cousin — same problem (forgetting), different level (weights vs context)
- [[namm]]: self-reference
- [[concepts/maximum-occupancy-principle]]: MOP's memory budget concepts may inform principled NAMM cache sizing
- [[bounded-structured-memory]]: both deal with bounded memory management; NAMM at the attention layer, BSM at the agent scaffolding level
- [[continual-learning]]
- [[qes]]
- [[ml-evolution-benchmarking-protocol]]
- [[rz-nas]]