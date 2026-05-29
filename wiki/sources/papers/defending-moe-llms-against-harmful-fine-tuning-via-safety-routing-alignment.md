---
summary: Fine-tuning causes significant routing drift for harmful inputs in MoE LLMs — SafeMoE penalizes routing gap to preserve safety routing
tags: [mixture-of-experts, fine-tuning, routing-drift, safety, harmful-fine-tuning, security]
updated: 2026-05-25T17:39:06Z
created: 2026-05-25T17:39:06Z
---

---
created: 2026-05-25T17:36:36Z
updated: 2026-05-25
type: source
summary: Fine-tuning causes significant routing drift for harmful inputs in MoE LLMs — SafeMoE penalizes routing gap to preserve safety routing
tags: [mixture-of-experts, fine-tuning, routing-drift, safety, harmful-fine-tuning, security]
sources: https://arxiv.org/abs/2509.22745
status: reference
confidence: 0.9
---

# Defending MoE LLMs against Harmful Fine-Tuning via Safety Routing Alignment

**Authors:** Kim et al. (2025)
**Venue:** arXiv:2509.22745

## Core Finding: Routing Drift After Fine-Tuning

This is the most directly relevant paper to the open question. The key finding: **routing decisions for harmful inputs drift significantly after fine-tuning** — the paper's analysis shows that the routing weights for harmful tokens change substantially post-fine-tuning, meaning the safety-critical experts that were aligned in the pre-fine-tuned model are no longer handling those tokens.

This is empirical confirmation that MoE routing is not stable through fine-tuning.

## Quantitative Evidence

- **OLMoE harmfulness score: 62.0** after fine-tuning (vs. aligned baseline before)
- SafeMoE reduces this to **5.0** while maintaining task utility within 1% degradation
- Tested on open-source MoE LLMs ranging from **7B to 141B parameters**
- Works across gpt-oss and Llama 4 architectures

## The Mechanism

MoE LLMs use a "safety routing" mechanism: harmful inputs are routed to safety-critical experts that have been aligned. After fine-tuning, this routing breaks down — the gating function changes and harmful tokens get routed elsewhere (or across less-aligned experts), bypassing the safety mechanism.

This is the first **direct empirical measurement of routing change under fine-tuning** — exactly what the [[mop-and-rlhf-interaction]] open question was asking about.

## SafeMoE Solution

The proposed defense penalizes the gap between fine-tuned routing weights and the initial safety-aligned model's routing weights:

`L_total = L_task + λ · ||W_finetuned - W_aligned||²`

This preserves the pre-fine-tuned routing distribution for safety-critical inputs while allowing task adaptation elsewhere.

## Relevance to MoE+RLHF

1. **Confirms routing collapse/drift is real**: Fine-tuning (including RLHF) measurably changes expert routing
2. **Scale-independent**: Observed across 7B to 141B models — not a small-scale artifact
3. **The KL penalty approach**: SafeMoE uses a routing-space KL-like penalty — analogous to Path 1 in [[mop-and-rlhf-interaction]] (occupancy-relative regularization)
4. **Connection to harmful fine-tuning**: RLHF is a form of fine-tuning; the same routing drift mechanism likely applies to standard RLHF

## Key Claims
- Harmful inputs' routing weights drift significantly after fine-tuning (empirically confirmed)
- OLMoE harmfulness score goes from aligned → 62.0 post-fine-tuning without SafeMoE
- Routing drift is observed across architectures (7B–141B) and multiple MoE systems
- Routing-space regularization (penalizing the gap) effectively preserves routing structure
- Only 2% overhead for the safety mechanism

## Connections
- [[concepts/mop-and-rlhf-interaction]]
- [[wiki/index]]
- [[defending-moe-llms-against-harmful-fine-tuning-via-safety-routing-alignment]]
- [[defending-moe-llms-against-harmful-fine-tuning-via-safety-routing-alignment]]
- [[mixture-of-experts]] — the architecture affected
- [[mop-and-rlhf-interaction]] — directly answers routing collapse question; SafeMoE's routing penalty is Path 1 in practice
- [[adversarial-training]] — harmful fine-tuning (HFT) is an adversarial attack on alignment
- [[reward-hacking]] — routing drift may be a form of reward hacking for the safety objective
