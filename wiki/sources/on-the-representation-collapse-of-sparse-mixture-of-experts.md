---
summary: Routing mechanism encourages token clustering around expert centroids — representation collapse, addressed via hypersphere routing
tags: [mixture-of-experts, routing, representation-collapse, fine-tuning, multilingual]
updated: 2026-05-25T17:39:05Z
created: 2026-05-25T17:39:05Z
---

---
created: 2026-05-25T17:35:36Z
updated: 2026-05-25
type: source
summary: Routing mechanism encourages token clustering around expert centroids, causing representation collapse — addressed via hypersphere routing on cross-lingual tasks
tags: [mixture-of-experts, routing, representation-collapse, fine-tuning, multilingual]
sources: https://arxiv.org/abs/2204.09179
status: reference
confidence: 0.85
---

# On the Representation Collapse of Sparse Mixture of Experts

**Authors:** Chi et al., Microsoft Research (2022)
**Venue:** arXiv:2204.09179

## Core Finding

The routing mechanism in sparse MoE encourages tokens to cluster around expert centroids — a **representation collapse** problem where the diversity benefit of MoE is undermined by the routing collapsing tokens into a few experts.

The paper demonstrates this empirically in cross-lingual pre-training: the routing scores concentrate, meaning fewer experts do most of the work and the specialization benefit degrades.

## Proposed Solution

Estimate routing scores between tokens and experts on a **low-dimensional hypersphere**. This prevents collapse by regularizing the geometry of token-expert matching. The approach achieves consistent gains across 7 multilingual benchmarks.

## Relevance to Routing Collapse Under RLHF

This is the *pre-training analogue* of the RLHF routing collapse question. The collapse mechanism is the same: the routing function converges to a degenerate distribution (all tokens routing to the same experts) rather than maintaining diverse utilization.

The hypersphere solution shows that architectural/geometric regularization can address routing degeneracy — relevant to all three resolution paths in [[mop-and-rlhf-interaction]].

## Key Claims
- Token clustering around expert centroids is a structural tendency of MoE routing
- This occurs during pre-training, not just fine-tuning
- Low-dimensional hypersphere regularization is an effective fix
- Cross-lingual experiments confirm the problem is real and the fix works

## Connections
- [[mixture-of-experts]]
- [[mop-and-rlhf-interaction]] — routing collapse is the core tension
- [[maximum-occupancy-principle]] — MOP's entropy objective is the opposite of collapse
