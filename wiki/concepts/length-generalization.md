---
created: 2026-05-21
updated: 2026-05-29
type: concept
summary: The failure of LLMs to generalize from short training sequences to longer inference sequences — a fundamental limitation of autoregressive transformers
tags: [llm, generalization, context-length, positional-encoding, autoregressive, scaling]
sources: ['https://arxiv.org/abs/2212.07106', 'https://arxiv.org/abs/2305.13230']
status: active
confidence: 0.8
---



# Length Generalization

Length generalization refers to the failure of large language models to perform well on sequences significantly longer than those encountered during training. A model trained on sequences of up to length L often degrades sharply when asked to process or generate sequences of length L+Δ, even when Δ is small.

## The Problem

Standard autoregressive transformers are trained on finite context windows. At inference time, when prompted with inputs longer than the training context, models exhibit:

- **Sharp quality degradation**: Accuracy drops non-smoothly, not gradually
- **Position collapse**: Tokens at positions beyond training length may receive near-random attention weights
- **Repetition and degeneration**: Models may loop, repeat, or produce incoherent output
- **Inability to use distant information**: Long-range dependencies learned during training fail to transfer

## Why It Happens

### Positional Encoding Limitations

Classical sinusoidal or learned positional encodings are absolute — each position gets a fixed embedding. When inference exceeds training length, the model has no embedding for positions beyond training max. Rotary Position Embeddings (RoPE) improved this somewhat by encoding *relative* positions, but length generalization remains imperfect.

### Attention Budget Mismatch

Models trained with a fixed context window develop attention patterns calibrated to that window. At longer contexts, attention heads may activate inappropriately — attending too much to padding tokens or failing to link distant relevant tokens.

### Distribution Shift in KV Caches

During training, the key-value cache patterns for tokens at position N are learned in the context of a specific cache size. Longer contexts change the statistical distribution of cache states.

## Key Research Directions

### Positional Encoding Extensions

| Method | Approach | Generalization Behavior |
|
--|
-|
|
| ALiBi | Bias added to attention scores based on distance | Extrapolates better than sinusoidal |
| RoPE | Rotates queries/keys to encode relative position | Best extrapolation among fixed encodings |
| Position Interpolation (PI) | Linearly rescales position indices | Smooths degradation but loses some resolution |
| YaRN | Extends RoPE with temperature scaling | Better高频 detail preservation |

### Length-Adaptive Training

Training at multiple context lengths and using curriculum learning — gradually increasing context length during fine-tuning — improves generalization but is computationally expensive.

### Memory-Augmented Approaches

Adding explicit long-term memory mechanisms (e.g., [[neural-long-term-memory]]) allows models to handle arbitrary-length context without requiring generalization from training length.

## Why It Matters for the Wiki

For Hermes Agent and LLM-WIKI:
- **Long documents**: Wiki concept pages can be longer than training context
- **Agentic loops**: Multi-step reasoning agents generate very long context histories
- **Cross-session memory**: The system needs to carry context across sessions

Length generalization failures directly impact the reliability of long-horizon agentic systems.

## Connections
- [[concepts/length-generalization]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-05-22]]
- [[concepts/attention-mechanism]]
- [[concepts/language-evolution]]
- [[log]]
- [[concepts/load-bearing-reasoning]]
- [[wiki/index]]
- [[concepts/chain-of-thought]]
- [[concepts/titans]]
- [[concepts/transformer-architecture]]
- [[concepts/neural-long-term-memory]]
- [[concepts/hidden-states]]
- [[length-generalization]]

- [[chain-of-thought]] — CoT generates long sequences that can trigger length generalization failures
- [[neural-long-term-memory]] — one solution to length generalization via explicit memory
- [[titans-test-time-memory|Titans]] — architecture designed with separate working and long-term memory
- [[hidden-states]] — KV cache behavior during length generalization involves hidden state dynamics
- [[load-bearing-reasoning]] — identifying which reasoning steps are robust to length and which collapse
- Concept: [[attention-mechanism]]
- Concept: [[titans]]
- Concept: [[transformer-architecture]]


## Open Questions

1. **Is there a theoretical length generalization limit for transformers?** Or does it scale with architecture and training data?
2. **Can length generalization be learned implicitly?** Some models show unexpected extrapolation ability with certain training regimes
3. **How does length generalization interact with reasoning?** Does CoT's benefit diminish on long problems due to position degradation?
