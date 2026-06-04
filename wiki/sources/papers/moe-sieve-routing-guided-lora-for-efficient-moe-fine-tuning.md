---
summary: Per-layer expert routing is highly skewed — cold experts rarely activated, top-25% routing covers most tokens; only tuning top-25% experts is competitive
tags: [mixture-of-experts, fine-tuning, lora, routing-skew, parameter-efficiency]
updated: 2026-05-25T17:39:07Z
created: 2026-05-25T17:39:07Z
---

---
created: 2026-05-25T17:37:22Z
updated: 2026-05-25
type: source
summary: Per-layer expert routing is highly skewed — cold experts rarely activated, top-25% routing covers most tokens; only tuning top-25% experts is competitive
tags: [mixture-of-experts, fine-tuning, lora, routing-skew, parameter-efficiency]
sources: https://arxiv.org/abs/2603.24044
status: reference
confidence: 0.85
---

# MoE-Sieve: Routing-Guided LoRA for Efficient MoE Fine-Tuning

**Authors:** Manzoni (2026)
**Venue:** arXiv:2603.24044

## Core Finding: Skewed Expert Utilization

The paper's most important empirical finding: **per-layer expert routing is highly skewed** — a small subset of experts handles most tokens at each layer, while many others are rarely activated ("cold experts").

This confirms the skewed utilization concern and provides quantitative measurements.

## Quantitative Evidence

- Top-25% most-routed experts per layer achieve competitive performance with full LoRA fine-tuning
- Mean performance difference: within ±1 percentage point
- LoRA trainable parameters reduced by **70-73%**
- Adapter checkpoint size reduced by **71-73%**
- Wall-clock training time reduced by **up to 50%**

## Implication for Routing Collapse

If only the top ~25% of experts per layer are worth adapting for downstream tasks (and the bottom ~75% add negligible value), this suggests:

1. **The routing distribution is already highly skewed pre-fine-tuning** — not symmetric across experts
2. **Cold experts may be "frozen in time"** — they represent older or less task-relevant specialization
3. **Adapting only top-routed experts is sufficient** — which is what MoE-Sieve shows
4. **Fine-tuning doesn't necessarily improve utilization of cold experts** — it actually may make them colder

This is a different framing of routing collapse: it's not that fine-tuning collapses a uniform distribution, but that it **compounds pre-existing skew**, making the already-hot experts even more dominant.

## Expert Selection Signal Matters

A key ablation: random expert selection at matched budget is ~2.5 percentage points worse than routing-guided selection. This means the routing signal carries real information about which experts are worth adapting.

## Non-Monotonic Variance

The paper also observes a non-monotonic relationship between expert count and seed-to-seed variance. This is consistent with the hypothesis that **adapting cold experts introduces gradient noise without improving accuracy** — cold experts may be doing something different enough from the task that adapting them hurts.

## Key Claims
- Per-layer routing is highly skewed (top ~25% of experts handle most tokens)
- Cold experts (bottom ~75%) add minimal value when adapted via LoRA
- Routing-guided expert selection outperforms random selection by ~2.5pp
- Cold expert adaptation introduces gradient noise without accuracy gains
- Seed-to-seed variance has a non-monotonic relationship with expert count

## Connections
- [[concepts/parameter-efficient-fine-tuning]]
- [[wiki/sources/papers/moe-sieve-routing-guided-lora-for-efficient-moe-fine-tuning]]
- [[concepts/mop-and-rlhf-interaction]]
- [[wiki/index]]
- [[wiki/sources/papers/moe-sieve-routing-guided-lora-for-efficient-moe-fine-tuning]]
- [[mixture-of-experts]] — the architecture studied
- [[mop-and-rlhf-interaction]] — confirms skewed utilization is real, not just theory
- [[parameter-efficient-fine-tuning]] — LoRA is the PEFT method used
- [[concepts/maximum-occupancy-principle]] — cold experts represent low-occupancy paths
