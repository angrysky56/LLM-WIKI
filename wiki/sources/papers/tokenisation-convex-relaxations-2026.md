---
created: 2026-05-24T00:00:00Z
updated: 2026-05-24T00:00:00Z
type: source
summary: "ConvexTok: LP-based tokeniser construction replaces greedy BPE, yielding tokenisers within 1% of optimal compression"
tags: [paper, arxiv, tokenisation, convex-optimization, vocabulary-learning, bpe, nlp]
sources: https://arxiv.org/abs/2605.22821
status: active
confidence: 0.85
---

# Tokenisation via Convex Relaxations (2026)

## Metadata
- **arXiv**: 2605.22821v1
- **Authors**: Jan Tempus, Philip Whittington, Craig W. Schmidt (ETH Zurich, Kensho Technologies)
- **Published**: 2026-05-21
- **Categories**: cs.CL, cs.LG

## Executive Summary

Current tokenisation algorithms (BPE, Unigram) are greedy — they make locally optimal merge decisions without considering the resulting vocabulary as a whole. This paper formulates tokeniser construction as a linear program (LP) and solves it with convex optimisation tools, producing an algorithm called **ConvexTok**. The LP solution provides a lower bound certifying how close any tokeniser is to optimal. Empirical results show ConvexTok tokenisers are within 1% of optimal compression, with the Bias rounding scheme consistently outperforming BPE on intrinsic metrics.

## Technical Approach

1. **Integer Program formulation**: Identify an integer program (IP) equivalent to the optimisation problem solved by tokenisation
2. **LP relaxation**: Relax the IP to a linear program, which can be solved efficiently with standard solvers
3. **Rounding schemes**: The LP solution contains "partial" tokens requiring discretisation — three rounding schemes are proposed: Bias (stochastic), Det (deterministic), and Random
4. **Lower bound certification**: Solving the LP provides a lower bound on compression achievable by any tokeniser on the dataset

The tokenisation problem is NP-hard; the key insight is that even though the integer program is intractable, its LP relaxation yields near-integral solutions (especially at larger vocabulary sizes), and the resulting tokenisers are within 1% of optimal.

## Key Results

- **Intrinsic metrics**: The Bias rounding scheme consistently outperforms all other tokenisers on compression rate, vocabulary utilisation, and Rényi entropy
- **Optimality bound**: At common vocabulary sizes, existing tokenisers are within 1% of optimal compression per the LP lower bound
- **Downstream language modeling**: The deterministic (Det) rounding scheme consistently performs best on bits-per-byte (BpB) and often outperforms BPE on downstream CORE tasks
- **Stability**: BPE is more stable to training dataset choice than ConvexTok across experiments

## Relevance to EFHF/AGEM/MOP Research

Tokenisation is a foundational data processing step that determines how information is chunked before it reaches model internals. ConvexTok's formal approach to vocabulary construction — framing it as a global optimisation problem with verifiable lower bounds — parallels the kind of principled, bounded verification that EFHF and verifier-graph enforce at the agent level. The "within 1% of optimal" certification pattern is directly analogous to the tightness guarantees that sheaf-consistency-enforcer and mop-explorer seek in their respective domains. The paper also touches on compression as a proxy for downstream quality, connecting to cost-model analysis in [[mop-explorer]].

## Key Quotes

> "BPE's use of greedily chosen pair-wise token-merging means that unnecessary intermediate tokens are created and compressive ability is lost."

> "Solving the LP provides a lower bound on the compression achieved by any tokeniser on the used dataset. Our method thus allows us to compute tight bounds on how close-to-optimal any tokeniser is."

## Connections
- [[efhf]], [[mop-explorer]], [[verifier-graph]], [[sheaf-consistency-enforcer]]