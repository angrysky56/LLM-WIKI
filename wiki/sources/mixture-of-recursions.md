---
summary: MoR unifies parameter sharing and adaptive token-level computation via learned recursive depth routing — connects to causal state assignment and compiled-transformer execution models.
tags: [adaptive-computation, recursive-transformers, efficient-transformers, parameter-sharing, routing, kv-cache, latent-reasoning, token-routing, transformer-architecture, sources]
updated: 2026-04-17T02:11:07Z
created: 2026-04-17T02:11:07Z
---

# Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation

**Authors:** Sangmin Bae, Yujin Kim, Reza Bayat, Sungnyun Kim, Jiyoun Ha, Tal Schuster, Adam Fisch, Hrayr Harutyunyan, Ziwei Ji, Aaron Courville, Se-Young Yun (KAIST AI, Mila, Google DeepMind, Google Research)
**Source:** https://arxiv.org/html/2507.10524v3
**Archived:** `Clippings/papers/2026/Mixture-of-Recursions Learning Dynamic Recursive Depths for Adaptive Token-Level Computation.md`

---

## Core Contribution

MoR is a unified framework inside a single **Recursive Transformer** that simultaneously achieves:

1. **Parameter efficiency** — a shared layer stack is reused across recursion steps (weight tying), reducing unique parameter count by a factor of the recursion number
2. **Adaptive computation** — lightweight routers trained end-to-end assign each token a different recursion depth, concentrating FLOPs on harder tokens
3. **Memory efficiency** — KV pairs are cached only for tokens active at each recursion depth, reducing memory traffic and boosting throughput

Across 135M–1.7B parameter scales, MoR establishes a new **Pareto frontier**: equal training FLOPs, smaller model size, lower validation perplexity, better few-shot accuracy, higher throughput than vanilla and recursive baselines.

---

## Architecture

### Recursive Transformer Substrate

Rather than $L$ unique layers, the model partitions into $N_r$ recursion blocks sharing a single parameter pool $\Phi'$. The hidden state evolves as:

$$h_t^{\ell+1} = f(h_t^\ell;\, \Phi'_{\ell \bmod (L/N_r)})$$

Several parameter-sharing strategies are explored: **Cycle** (blocks reused cyclically), **Sequence** (same block applied consecutively), and **Middle** variants that preserve full-capacity first/last layers.

### Routing: Expert-choice vs. Token-choice

**Expert-choice routing** — each recursion depth selects its preferred top-$k$ tokens by score. Uses hierarchical filtering: only tokens selected at depth $r$ can proceed to $r+1$, mimicking early-exit with learned-from-scratch routing. Guarantees load balance but risks information leakage during training.

**Token-choice routing** — each token commits upfront to a full recursion depth via top-1 gating on its routing scores. No leakage, but requires a balancing loss. The token is assigned recursion $i$ times and its state updates recursively.

### KV Caching Strategies

**Recursion-wise caching** — only tokens active at depth $r$ cache their KV pairs there; attention is restricted to locally cached tokens. Reduces IO and cache size proportionally.

**Recursive KV sharing** — since all tokens traverse at least the first recursion block, only first-block KV pairs are cached and reused across all subsequent recursions. Query length shrinks per depth; key/value length stays full. Zero recomputation, at the cost of some cross-depth mismatch.

---

## Latent Space Reasoning Framing

MoR provides a pretraining framework for **latent space reasoning** — non-verbal "thinking" by iterating a single parameter block. Unlike approaches that prepend continuous prompts before generation, MoR performs this latent thinking *during decoding of each token*, dynamically adjusting thinking depth per token along the model's vertical axis. Simpler tokens exit early; complex tokens recurse more.

---

## Connections to This Wiki

### → [[causal-state-edm-ood-isomorphism]]

The per-token recursion depth pattern MoR learns is a direct empirical proxy for **causal state complexity**. In the epsilon machine framing developed in that synthesis: a token that routes to shallow recursion is lumpable with the existing causal state — the current context is sufficient to predict it. A token routed to maximum depth is informationally "harder" — the model must iterate its representation more before it resolves, analogous to a state-splitting event or an OOD observation that requires deeper causal processing.

This creates a potential **routing-as-OOD-signal**: tokens that consistently demand maximum recursion depth across a corpus may be disruptive tokens in the EDM sense — they force the model's internal epsilon machine to perform extra state resolution. The recursion depth histogram over a document could therefore serve as a lightweight disruption signal without needing citation network data.

Conversely, the causal state isomorphism suggests a principled criterion for router training: rather than arbitrary top-$k$ load balancing, routers could be guided to assign deeper recursion to tokens that maximally increase the statistical complexity of the model's predictive distribution — directly optimizing for causal state coverage.

### → [[i-built-a-tiny-computer-inside-a-transformer]] (Clippings/articles/2026)

The compiled-transformer article treats the residual stream as working memory and each layer as a deterministic state-transition step — a fixed program compiled into weights. MoR operates on the same substrate but inverts the design philosophy: rather than hard-coding how many state transitions each computation requires, MoR *learns* that allocation from data.

The two approaches are complementary halves of the same idea:

| Compiled Transformer (Moran / Percepta) | Mixture-of-Recursions |
|---|---|
| Fixed program, variable input | Variable depth, shared weights |
| Deterministic state transitions | Stochastically routed state iterations |
| Residual stream = machine registers | Residual stream = evolving token state |
| Layer = explicit machine step | Recursion block = learned thinking step |
| Depth determined by program | Depth determined by router |

The "continuous depth-wise batching" optimization in MoR — grouping tokens at different recursion stages into a single batch since they share weights — is structurally equivalent to batching execution across different program steps in a shared interpreter. This is precisely Percepta's setup: a single interpreter in the weights, programs supplied at inference time. MoR is the trained analog of that compiled architecture.

A natural synthesis: MoR-style routing could identify *which tokens need deterministic subroutines* (deep recursion, high complexity) vs. which can be handled by shallow probabilistic inference (early exit). The compiled-transformer work then provides the substrate for those deterministic subroutines to be embedded directly in the weights rather than offloaded to external tools.

---

## Key Empirical Results

- At equal training FLOPs, MoR with recursion $N_r=3$ matches or beats vanilla transformers at 2–3× the parameter count
- Token-choice routing outperforms expert-choice in most settings despite load-balancing complexity
- Recursive KV sharing provides the best memory/throughput trade-off; recursion-wise caching gives tighter accuracy
- Middle-Cycle parameter sharing consistently outperforms Cycle and Sequence across scales
- Continuous depth-wise batching further boosts inference throughput beyond KV reduction alone

---

## Open Questions

1. Can recursion depth histograms serve as a lightweight OOD / disruption signal, analogous to EDM's Δ score? (→ [[causal-state-edm-ood-isomorphism]])
2. Could router training loss be reformulated as a causal state entropy objective rather than load balancing?
3. How does MoR interact with mechanistic interpretability — do shared weights develop cleaner circuits precisely because they must generalize across recursion depths?
4. What is the relationship between MoR's adaptive vertical depth and mixture-of-experts' adaptive horizontal width? Is there a unified routing geometry?
5. Can the compiled-transformer (Percepta) paradigm be extended to dynamically allocated depth — a router that switches between probabilistic and deterministic execution modes per token?

---

## Related Pages

- [[causal-state-edm-ood-isomorphism]] — token routing depth as causal state complexity proxy; disruption signal connection
- [[efficient-transformers]] — broader efficiency landscape
- [[mixture-of-depths]] — direct predecessor (MoD); MoR generalizes MoD routing to recursive weight-shared architectures
- [[recursive-transformers]] — architectural substrate
- [[adaptive-computation]] — early-exit and dynamic depth literature
- [[latent-reasoning]] — latent space "thinking" before/during token generation
- [[kv-cache]] — memory bottleneck MoR partially addresses
