---
summary: Attention-based neural architecture — foundation for BERT, GPT, and most modern LLMs; self-attention replaces recurrence, enabling parallel training
tags: [transformers, deep-learning, neural-architecture, attention, llm-architecture]
updated: 2026-05-28T14:04:34Z
---

---
created: 2026-05-25
updated: 2026-08-19
type: concept
summary: Attention-based neural architecture that processes sequences in parallel via self-attention — foundation for BERT, GPT, T5, and most modern LLMs
tags: [transformers, deep-learning, neural-architecture, attention, llm-architecture]
sources: https://arxiv.org/abs/1706.03762 (Vaswani et al. 2017)
status: active
confidence: 0.78
---

# Transformers

The transformer is a neural network architecture introduced by Vaswani et al. (2017, "Attention Is All You Need") that processes sequential data using **self-attention** rather than recurrence. It processes entire sequences in parallel, removing the sequential dependency that made RNNs slow to train on long contexts.

## Core Mechanism: Scaled Dot-Product Attention

For input tokens x₁,...,xₙ, the attention function computes:

```
Attention(Q, K, V) = softmax(QKᵀ / √d_k) · V
```

where Q (query), K (key), V (value) are linear projections of the input. The √d_k scaling prevents vanishing gradients in high-dimensional attention spaces.

**Multi-head attention** runs this in parallel across h heads, each with its own Q/K/V projections, then concatenates and projects the results. This allows the model to attend to different representation subspaces simultaneously.

## Architectural Variants

| Variant | Directionality | Use Cases | Examples |
|---------|---------------|-----------|----------|
| **Encoder-only** | Bidirectional | Classification, NER, QA | BERT, RoBERTa |
| **Decoder-only** | Causal (unidirectional) | Autoregressive generation | GPT-2/3/4, Llama, Claude |
| **Encoder-decoder** | Both | Sequence-to-sequence | T5, BART, FLAN-T5 |

Decoder-only transformers dominate current LLM work because causal masking (each token attends only to predecessors) enables efficient autoregressive generation and scales well with the causal attention optimization landscape.

## The Feed-Forward Network (FFN)

Each transformer layer contains a position-wise FFN: two linear transforms with a non-linearity (typically GELU or SwiGLU). In dense transformers, the FFN contains ~2/3 of the parameters. In MoE architectures (see [[mixture-of-experts]]), the FFN is replaced by expert sub-networks with a router selecting the active subset.

## Positional Encoding

Attention is inherently permutation-invariant — it treats the input as a set, not a sequence. Positional information must be injected:

- **Absolute**: Sinusoidal (original Vaswani) or learned embeddings
- **Relative**: RoPE (Rotary Position Embedding, used in Llama, Mistral) — encodes relative position via rotation in embedding space
- **ALiBi**: Attention with Linear Biases — adds bias proportional to key-query distance

RoPE has become dominant because it extrapolates to longer contexts than seen at training without explicit length generalization mechanisms.

## Key Scaling Properties

Transformers exhibit predictable scaling laws (Kaplan et al. 2020): loss decreases as a power law with model size, data size, and compute. This enabled the large-model era. The [[chinchilla-scaling]] work refined this, showing optimal training tokens should scale ~1:1 with parameters.

## Relationship to Recurrence

Pure transformers have no native recurrence — each layer processes the same input independently. [[recursive-transformers]] add recurrence by passing hidden states across layer steps. [[state-space-models]] (Mamba) offer an alternative long-range model with recurrence-like efficiency. [[titans]] adds explicit long-term memory layers on top of standard attention.

## Connections

- [[mixture-of-experts]]: Sparse MoE replaces dense FFN with routed expert sub-networks
- [[bounded-rationality]]: Transformers as the architectural substrate for bounded rational information processing
- [[recursive-transformers]]: Adding recurrence to the transformer architecture
- [[state-space-models]]: Alternative to attention for long-range dependencies (Mamba)
- [[titans]]: Adds neural long-term memory module to transformer stack
- [[inference-time-compute-scaling]]: How test-time compute (longer sequences, more layers) improves outputs
- [[concepts/load-bearing-reasoning]]: Attention heads as the load-bearing structure for reasoning traces
- [[chain-of-thought]]: Emergent reasoning behavior in large decoder-only transformers

## Limitations

- **Context length quadratic cost**: Full attention is O(n²) in sequence length. Many efficient variants (linear attention, sparse attention, state-space models) address this.
- **No native recurrence**: Pure transformers have no sequential inductive bias — recurrence must be added explicitly (see recursive-transformers, SSMs).
- **Memory bandwidth**: All weights must be in memory for every forward pass — unlike RNNs which have small recurrent state. MoE mitigates compute but not memory bandwidth.
