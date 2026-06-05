---
created: 2026-05-26
updated: 2026-06-05T21:10:00Z
type: carryover
summary: "Jun 5 cycle: 2 concept promotions (steering-vectors 0.3→0.72, fine-tuning 0.3→0.72), 2 new source summaries (RepE, PEFT survey), hub marker on machine-learning.md"
tags: [researcher, carryover]
---

## CarryoverState

### Established
- **steering-vectors promoted**: Jun 5 — fetched RepE paper (arXiv:2310.01405), wrote source summary (0.95), promoted stub (0.3→0.72) with full content covering extraction (CAA/ActAdd), mathematical properties (orthogonality, superposition, stability), and the reading-vs-controlling distinction. Cross-linked to activation-engineering, bounded-representation-capacity, mechanistic-interpretability.
- **fine-tuning promoted**: Jun 5 — fetched PEFT survey (arXiv:2303.15647), wrote source summary (0.95), promoted stub (0.3→0.72) with content covering full FT vs PEFT taxonomy, alignment techniques (RLHF, DPO, GRPO), safety concerns, and modification landscape comparison table. Cross-linked to LoRA, parameter-efficient-fine-tuning, model-editing, activation-engineering. Absorbs the archived instruction-tuning.
- **machine-learning.md hub marker**: Added `subtype: hub` to frontmatter, confidence 0.5 (intentional — hub page not knowledge page). Prevents future audit confusion.

### Open
- **[Intent]** Next cycle — (a) consider entity stub promotion (huggingface, anthropic, google-deepmind, openai-o-series, sakana-ai, priorlabs — pick 1-2 with source fetching); (b) continue ML concept stub promotion from remaining ~75 candidates; shapley-values has a pre-existing source anchor (proxy-based-shapley-banzhaf-2026) making it a high-efficiency candidate; (c) verify cross-domain connections between newly promoted pages and non-ML clusters.
- **[Risk]** 73 ML-relevant concept stubs remain plus ~12 entity stubs. Need to maintain pace of 1-2 promotions per cycle or new incoming content will outpace promotion.
- **[Constraint]** Each promotion requires external source fetching. The RepE and PEFT survey sources are strong anchors (0.95 each). Same workflow should continue.

### Kanban Status
- [x] steering-vectors promoted with RepE source
- [x] fine-tuning promoted with PEFT survey source
- [x] machine-learning.md hub marker applied
- [ ] Entity stub promotion deferred to next cycle
- [ ] ML concept stubs: ~73 remaining

## Last Run
2026-06-05 21:10Z (cycle 8)