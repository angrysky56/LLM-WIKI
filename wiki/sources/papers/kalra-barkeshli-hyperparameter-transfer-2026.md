---
summary: μP's advantage over SP: almost entirely from maximizing embedding layer LR — simple fix resolves training instability bottleneck
tags: [paper, hyperparameter-transfer, LLM-training, embedding-LR, scaling-laws]
updated: 2026-05-21T16:53:08Z
created: 2026-05-21T16:53:08Z
---

---
created: 2026-05-21T16:52:00Z
updated: 2026-05-21T16:52:00Z
type: source
summary: "μP's advantage over standard parameterization (SP) for hyperparameter transfer is almost entirely from maximizing embedding layer learning rate — the embedding LR is a bottleneck in SP that induces training instabilities"
tags: [paper, hyperparameter-transfer, LLM-training, embedding-LR, scaling-laws, cs-LG]
sources: https://arxiv.org/abs/2605.21486
status: active
confidence: high
---

# Quantifying Hyperparameter Transfer and the Importance of Embedding Layer Learning Rate

**Authors**: Dayal Singh Kalra, Maissam Barkeshli

## Core Insight

The paper develops a **framework to quantify hyperparameter transfer** through three metrics: (1) quality of scaling law fit, (2) robustness to extrapolation errors, and (3) asymptotic loss penalty from parameterization choice. The key empirical finding: **μP's advantage over standard parameterization (SP) when training with AdamW arises almost entirely from maximizing the embedding layer learning rate**. In SP, the embedding LR acts as a bottleneck that induces training instabilities; increasing it by a factor of width to match μP dramatically smooths training and improves hyperparameter transfer.

## Key Claims

| Claim | Evidence |
|-------|----------|
| μP's benefit = maximizing embedding layer LR | Comprehensive ablations isolating each μP design choice |
| Embedding LR is a bottleneck in SP | Training instabilities disappear when embedding LR is increased by width factor |
| Weight decay improves scaling law fits | But hurts robustness of extrapolation in fixed token-per-parameter setting |
| Three-metric framework for hyperparameter transfer | Quality of fit / robustness to extrapolation / asymptotic loss penalty |

## Why This Matters

1. **Training stability at scale** — if the embedding LR is the key bottleneck, this is a simple fix that dramatically changes large-scale training dynamics
2. **Hyperparameter transfer** — understanding *why* μP transfers better is as important as knowing *that* it does; this paper provides the mechanistic account
3. **LLM training practice** — embedding layers are often treated as a minor component; this reframes them as critical to training stability and hyperparameter extrapolability
4. **Connection to scaling laws** — weight decay effects on scaling law fits suggest that regularization regime matters for extrapolation quality, not just in-sample performance

## Connections

- [[ml-evolution]] — hyperparameter transfer is foundational to autonomous model evolution (e.g. AlphaEvolve); understanding what's actually being transferred matters for MGA design
- [[superbpe]] — tokenization choices affect embedding layer dynamics; subword vs character vs other schemes may interact with embedding LR behavior
- [[eml-operator]] — if embedding layers are a bottleneck in SP, and EML provides a minimal computational substrate, there may be a connection to how embedding updates are computed vs how they're scheduled

## Caveats

- Empirical work on specific architectures (details in 10+28 pages)
- Fixing the embedding LR in SP doesn't fully replicate μP — other μP design choices still contribute, just much less than the embedding LR alone
