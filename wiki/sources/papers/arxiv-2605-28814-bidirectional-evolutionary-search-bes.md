---
created: 2026-05-31
updated: 2026-05-31
type: source
summary: Bidirectional Evolutionary Search (BES) combines forward candidate evolution with backward goal decomposition to overcome entropy-shell limitations of tree search in LLM self-improvement.
tags: [paper, arxiv, research, LLM, search, self-improvement, inference-scaling]
---

# Self-Improving Language Models with Bidirectional Evolutionary Search (BES)

**arXiv:** [2605.28814](https://arxiv.org/abs/2605.28814) | **Authors:** Xu et al. (Harvard, MIT) | **Date:** 2026-05-27

## Overview

Existing LLM self-improvement methods (best-of-N sampling, tree search) face two fundamental limitations: sparse verification signals and confinement to narrow entropy shells (candidates only explored within the model's high-probability regions). BES addresses both.

## Core Contribution: Bidirectional Evolutionary Search

BES couples **forward candidate evolution** with **backward goal decomposition**:

1. **Forward search**: Evolution operators recombine partial trajectories to generate candidates difficult to obtain from a single model rollout, escaping the narrow entropy shell that constrains expansion-only search
2. **Backward search**: Recursively decomposes the original task into checkable sub-goals, producing dense intermediate feedback that guides forward search

### Theoretical Motivation

The authors prove that expansion-only search candidates are confined to a narrow entropy shell (Theorem 4.4a), and that backward search can exponentially reduce required samples to find a correct answer.

## Key Results

- Consistent gains on challenging post-training tasks where mainstream algorithms fail
- Outperforms existing open-source frameworks on three open problem-solving benchmarks at inference time
- Applicable to both post-training sample generation and test-time scaling

## Related

- [[reinforcement-learning-from-human-feedback]] — RLHF context
- [[test-time-scaling]] — inference-time computation allocation
- [[tree-of-thoughts]] — related search-based reasoning approach
- [[best-of-n-sampling]] — baseline method
- [[evolutionary-algorithms]] — evolution operators background