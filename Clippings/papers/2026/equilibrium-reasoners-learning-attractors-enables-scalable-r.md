---
title: Equilibrium Reasoners: Learning Attractors Enables Scalable Reasoning
source: https://arxiv.org/abs/2605.21488
created: 2026-05-21T16:49:52Z
tags: [clippings]
---

## Title:Equilibrium Reasoners: Learning Attractors Enables Scalable Reasoning

Authors:[Benhao Huang](https://arxiv.org/search/cs?searchtype=author&query=Huang,+B), [Zhengyang Geng](https://arxiv.org/search/cs?searchtype=author&query=Geng,+Z), [Zico Kolter](https://arxiv.org/search/cs?searchtype=author&query=Kolter,+Z)

[View PDF](https://arxiv.org/pdf/2605.21488) [HTML (experimental)](https://arxiv.org/html/2605.21488v1)

> Abstract:Scaling test-time compute by iteratively updating a latent state has emerged as a powerful paradigm for reasoning. Yet the internal mechanisms that enable these iterative models to generalize beyond memorized patterns remain unclear. We hypothesize that generalizable reasoning arises from learning task-conditioned attractors: latent dynamical systems whose stable fixed points correspond to valid solutions.  
> We formalize this process through Equilibrium Reasoners (EqR), which enable test-time scaling without external verifiers or task-specific priors. EqR scales internal dynamics along two axes: depth, by running more iterations, and breadth, by aggregating stochastic trajectories from multiple initializations. Empirically, gains from test-time scaling are tightly coupled with stronger convergence toward solution-aligned attractors.  
> This attractor perspective allows neural networks to adaptively allocate test-time compute based on task difficulty. While simple cases converge within 1 to 5 iteration steps, harder cases benefit from massive test-time scaling. By unrolling up to the equivalent of 40,000 layers, scalable latent reasoning boosts accuracy from 2.6% for feedforward models to over 99% on Sudoku-Extreme. These results suggest that learned attractor landscapes provide a useful mechanistic lens for understanding scalable reasoning in iterative latent models.

| Comments: |
| --- |
| Subjects: | Machine Learning (cs.LG) |
| Cite as: | [arXiv:2605.21488](https://arxiv.org/abs/2605.21488) \[cs.LG\] |
|  | (or [arXiv:2605.21488v1](https://arxiv.org/abs/2605.21488v1) \[cs.LG\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2605.21488](https://doi.org/10.48550/arXiv.2605.21488) |

## Submission history

From: Benhao Huang \[[view email](https://arxiv.org/show-email/6f3f340b/2605.21488)\]  
**\[v1\]** Wed, 20 May 2026 17:59:48 UTC (21,616 KB)  

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2605.21488) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))