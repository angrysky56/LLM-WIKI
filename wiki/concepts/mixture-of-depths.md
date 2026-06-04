---
summary: Mixture of Depths — per-token adaptive depth routing in transformers, processing high-information tokens through all layers and skipping low-information tokens to save FLOPs at fixed quality
tags: [mixture-of-depths, adaptive-computation, transformer-architecture, routing, inference-efficiency, mixture-of-experts]
updated: 2026-06-04T14:07:23Z
---

---
created: 2026-06-16
updated: 2026-06-04
type: concept
summary: "Mixture of Depths (MoD) — adaptive computation that routes tokens through a variable number of transformer layers, allocating depth where it matters and skipping layers for tokens that don't need deep processing"
tags: [mixture-of-depths, adaptive-computation, transformer-architecture, routing, inference-efficiency, mixture-of-experts]
sources: [https://arxiv.org/abs/2404.02258 (MoD, Raposo et al. 2024), https://arxiv.org/abs/2402.17427 (Titans), https://arxiv.org/abs/2406.07584 (Mamba-2)]
status: active
confidence: 0.7
---

# Mixture of Depths

## Definition

**Mixture of Depths (MoD)** is an adaptive-computation technique for transformer architectures in which each token is routed through a *variable number of layers* rather than the full fixed depth of the model. Tokens deemed "easy" or low-information exit early (or skip a layer entirely); tokens deemed "hard" are processed by every layer. The result: a model that, on average, uses less compute per token than a fixed-depth transformer, while preserving quality on the tokens that need depth.

MoD is a member of the broader [[adaptive-computation]] family. Its distinguishing feature is that it varies *depth per token* (which layers to apply) rather than depth per input (early exit applies to all tokens) or compute per layer (MoE varies *width*, not depth).

## Mechanism

The MoD routing pattern:

1. At a given layer, a small routing network computes a per-token score from the token's hidden state.
2. Top-k tokens (by score) are processed by the layer; the rest skip it and pass through unchanged (residual connection only).
3. The output of the processed tokens is concatenated with the unprocessed tokens, and the sequence continues to the next layer.

The routing is *per-layer* and *binary*: each token either gets the full layer transformation or passes through unchanged. This is different from MoE routing (which selects an expert per token) and from early exit (which terminates the entire computation for a token).

The capacity budget `k` is fixed per layer (e.g., 50% of tokens are processed at each layer). This makes the total compute per forward pass *predictable* — the per-layer cost is constant regardless of input — which is the property that makes MoD attractive for serving at scale.

## Why It Matters

The motivation is straightforward. A fixed-depth transformer applies the same number of layers to every token, including high-frequency, low-information tokens (commas, articles, repeated boilerplate). For a 60-layer model processing 4K tokens, that's 240K layer applications — most of which do very little. MoD observes that a small fraction of tokens carry most of the "reasoning" and that the rest can be carried unchanged.

This is the same observation behind [[mixture-of-experts]] (sparse width instead of depth) and [[adaptive-computation-time]] (continuous depth instead of binary). MoD's contribution is the *binary per-layer routing* — simple, predictable, and amenable to standard transformer kernels.

The empirical results from the MoD paper (Raposo et al. 2024, Google Research): MoD models match the quality of fixed-depth baselines while using ~40–50% of the FLOPs on average per token. The savings compound at inference time, especially for long-context workloads where the per-layer cost is dominated by attention rather than the MLP.

## Connection to Adaptive Computation

MoD sits within the [[adaptive-computation]] family. Distinguishing axes:

| Technique | What varies | Granularity | Decision |
|---|---|---|---|
| **Early exit** | Depth (terminate) | Per input | Confidence threshold |
| **MoD** | Depth (skip layer) | Per token, per layer | Top-k routing |
| **MoE** | Width (select expert) | Per token, per layer | Top-k routing |
| **ACT** | Depth (continuous halting) | Per token | Learned halting prob |
| **MoR** (Mixture of Recursions) | Depth (recursive depth) | Per token | Recursion depth |

The shared underlying principle: *not all tokens need the same amount of computation*. The implementation choices differ in granularity (per input vs per token), decision type (continuous vs top-k), and architectural impact (skip a layer vs skip a recursion).

## Mixture of Depths vs Mixture of Experts

A common confusion: MoD and MoE both use top-k routing per layer, but they route to different things.

- **MoE**: every token passes through the layer, but the MLP is replaced by `k` expert MLPs and each token is routed to `k'` of them. Width varies, depth is fixed.
- **MoD**: each token either passes through the full layer transformation or skips it entirely. Depth varies, width is fixed.

In principle, MoD and MoE can be combined — a transformer block with both a MoD routing decision (skip or not) and a MoE routing decision (which expert if not skipping) — and there is some early work in this direction. The combined design lets the model vary both *how many* tokens get full processing and *which* expert processes them, with a single capacity budget that can be split between the two decisions.

## Scaling and Inference Implications

MoD has practical implications beyond per-token compute savings:

1. **Predictable serving cost** — because `k` is fixed, the per-step compute is constant. This is rare in the adaptive-computation family (early-exit models have variable latency) and is the property that makes MoD deployable in production serving stacks.

2. **Training/inference consistency** — MoD models are trained with the routing decision baked in; there is no train/test mismatch. This contrasts with some early-exit schemes that train a single model and then add exits at deployment.

3. **Long-context amortization** — for long sequences, MoD's per-token compute savings scale with sequence length. A 100K-token MoD model is roughly 2× cheaper than a fixed-depth 100K-token model on tokens that don't need full depth, which is most of them.

4. **Routing as learned importance** — the routing network's scores can be inspected as a learned measure of token importance. This is a small interpretability win — the model "knows" which tokens to focus on, and we can see it.

## Connection to Mixture of Recursions and Recursive Architectures

A natural extension of MoD is **Mixture of Recursions (MoR)**: instead of routing tokens through different *layers* of a fixed-depth model, route them through different *numbers of iterations* of a shared recursive block. MoR unifies MoD with the parameter-sharing idea: the same block is applied 1, 2, 4, ... times depending on the routing decision. The parameter count is fixed, but the *effective* depth per token varies.

This is a meaningful step toward parameter-efficient adaptive computation: instead of needing N copies of every layer (for N possible depths), the model needs one block applied up to N times. The tradeoff is that deep processing is *slower* (sequential recursion vs parallel layers), but the parameter and memory savings are substantial.

The [[titans]] paper and related test-time-training work push this further: a learnable memory module that is updated each time the recursive block is applied. The combination of recursive depth, test-time memory update, and per-token routing is the frontier of adaptive computation in 2026.

## Connections

- [[adaptive-computation]] (0.78) — MoD is one technique in the family; the canonical page covers early exit, MoD, and ACT.
- [[mixture-of-experts]] (high authority) — the width-varying analog; same routing mechanism, different routed resource.
- [[scaling-laws]] (0.85) — MoD is a way to break the "all tokens pay the same compute" assumption underlying classical scaling laws.
- [[mixture-of-recursions]] — the recursive extension; same idea, different parameter-sharing regime.
- [[bounded-rationality]] — the conceptual parent: fixed compute is wasteful when input complexity varies.
- [[inference-efficiency]] — the engineering reason MoD matters: lower FLOPs per token at the same quality.
- [[chain-of-thought]] — both are adaptive-compute schemes, but CoT adds *output* tokens rather than *internal* depth.
- [[sources/papers/mixture-of-recursions 1]] — the MoR source paper; linked for completeness.

## Source Anchors

- [[adaptive-computation]] (0.78) — the family overview; covers MoD, ACT, and early exit.
- [[mixture-of-experts]] (high authority) — the width-varying analog.
- [[scaling-laws]] (0.85) — the laws that MoD partially breaks (per-token compute is no longer uniform).
- [[sources/papers/mixture-of-recursions 1]] — the MoR paper; the recursive extension of MoD.

## See Also

- [[mixture-of-experts]] — the width analog of MoD.
- [[early-exit-transformers]] — the input-level analog.
- [[adaptive-computation-time]] — the continuous-depth ancestor.
- [[mixture-of-recursions]] — the recursive extension.
- [[routing-mechanisms]] — the routing-network pattern in the broader sense.
- [[conditional-computation]] — the conceptual parent.

## Open Questions

- [ ] Can MoD and MoE be jointly optimized with a shared capacity budget? Some early work exists but the design space is not fully characterized.
- [ ] How sensitive is MoD to the capacity budget `k`? Too small → quality degrades; too large → savings vanish. The right `k` is workload-dependent and there is no good theoretical predictor.
- [ ] Can the routing network be distilled into a simpler rule (e.g., "tokens after a period get full depth")? The paper shows that the learned routing is *partially* explainable by position and frequency, but not entirely.
- [ ] How does MoD interact with long-context attention? Most of the per-layer compute in long-context models is attention, not MLP — does MoD's savings shrink when the bottleneck is attention?
- [ ] Can MoD's routing decisions be used as an interpretability signal? The model knows which tokens to focus on; whether that knowledge aligns with human-judged importance is open.
