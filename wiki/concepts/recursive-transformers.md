---
created: 2026-06-16
updated: 2026-06-25
type: concept
summary: "Recursive transformer architectures reuse shared layer blocks across multiple forward passes per token, enabling adaptive per-token computation depth without proportional parameter increase"
tags: [recursive-transformers, ml-architectures, adaptive-computation, reasoning, parameter-sharing, routing]
sources: https://arxiv.org/html/2507.10524v3 (Mixture-of-Recursions)
status: active
confidence: 0.7
---

# Recursive Transformers

## Definition

Recursive transformers are transformer architectures that apply the same layer block multiple times per token, with each pass updating the hidden state before the next. Rather than $L$ unique layers (each with distinct weights), a recursive transformer shares a single parameter pool $\Phi'$ across $N_r$ recursion steps. The hidden state evolves as:

$$h_t^{\ell+1} = f(h_t^\ell;\, \Phi'_{\ell \bmod (L/N_r)})$$

This is distinct from standard transformers (each layer is unique) and from standard weight tying (e.g., Universal Transformers, which apply the same block repeatedly but without learned per-token routing).

## Why It Matters

Recursion enables **adaptive per-token computation** — the model learns to route easy tokens to shallow recursion (1-2 passes) and hard tokens to deep recursion (maximum depth). This concentrates FLOPs where they're most needed, improving efficiency without sacrificing expressiveness.

The key insight from the Mixture-of-Recursions (MoR) paper: a single shared layer stack, reused via lightweight routing, achieves equal quality to a model with 2-3× more unique parameters at the same training compute budget.

## Technical Approach

### Parameter Sharing Strategies

Three strategies for sharing $L$ layers across $N_r$ recursion blocks:

- **Cycle**: blocks reused cyclically — `Block_0, Block_1, ..., Block_{N_r-1}, Block_0, Block_1, ...`
- **Sequence**: the same block applied consecutively $N_r$ times
- **Middle**: preserves full-capacity first and last layers, shares only middle blocks (avoids compressing input/output representation)

Middle-Cycle consistently outperforms the others across model scales.

### Routing Mechanisms

Two complementary approaches:

**Token-choice routing**: each token commits upfront to a full recursion depth via top-1 gating on its routing scores. The token's state is then updated by applying the shared block $i$ times recursively. No information leakage, but requires a load-balancing auxiliary loss.

**Expert-choice routing**: each recursion depth selects its top-$k$ tokens by score. Only tokens selected at depth $r$ proceed to depth $r+1$. Guarantees load balance but introduces information leakage during training (tokens know their depth selection).

### KV Caching for Recursion

Two strategies:
- **Recursion-wise caching**: only cache KV for tokens active at each recursion depth. Attention is restricted to locally cached tokens. Proportional memory reduction.
- **Recursive KV sharing**: only first-block KV pairs are cached and reused across all recursions. Zero recomputation at the cost of cross-depth mismatch.

## Key Results (from MoR paper)

| Metric | Result |
|--------|--------|
| Parameter efficiency | MoR with $N_r=3$ matches vanilla at 2-3× fewer parameters |
| Validation perplexity | Lower than vanilla and recursive baselines at equal FLOPs |
| Few-shot accuracy | Better than comparable baselines |
| Throughput | Higher than vanilla at equal quality |

## Connections to Other Concepts

- [[mixture-of-recursions]] — the primary paper on this architecture
- [[mixture-of-depths]] — direct predecessor; MoR generalizes MoD routing to weight-shared architectures
- [[reasoning]] — recursive computation as substrate for multi-step reasoning; latent space thinking during token generation
- [[latent-reasoning]] — per-token recursion depth is latent reasoning; thinking happens vertically within the recursion stack, not just horizontally in the context
- [[adaptive-computation]] — early-exit literature; MoR provides learned adaptive depth within a single forward pass
- [[efficient-transformers]] — broader efficiency landscape; parameter sharing is one approach
- [[kv-cache]] — memory bottleneck recursive transformers partially address via depth-wise caching
- [[causal-state-edm-ood-isomorphism]] — MoR's per-token recursion depth pattern may serve as a proxy for causal state complexity; tokens routed to maximum depth are informationally "harder"

## Limitations

- **Router training complexity**: token-choice routing requires careful load-balancing; expert-choice has leakage
- **Shared weights limit circuit specialization**: the same parameters must generalize across all recursion depths, potentially limiting expressiveness per depth
- **Not a drop-in replacement**: recursive transformers require architectural changes and routing training, not just weight sharing

## Open Questions

1. Can recursion depth histograms serve as a lightweight OOD/disruption signal (analogous to EDM's Δ score)?
2. How does MoR interact with mechanistic interpretability — do shared weights develop cleaner circuits?
3. Is there a unified routing geometry that also covers mixture-of-experts' adaptive horizontal width?
4. Can compiled-transformer (Percepta) deterministic subroutines be embedded alongside MoR's probabilistic routing?