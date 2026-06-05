---
summary: Jun 6 cycle: FlashAttention source fetched, llm-kernel-optimization promoted (0.3→0.72), instruction-tuning archived, 29 periphery stubs batch-archived
tags: [discovery, report, weekly]
updated: 2026-06-05T20:12:20Z
created: 2026-06-05T20:12:20Z
---

# Discovery Report — 2026-06-06

## Discovery Cycle
- Topics researched: 4 (llm-kernel-optimization, FlashAttention, instruction-tuning, periphery-stub batch)
- New pages created: 1 (FlashAttention source summary)
- Pages updated: 3 (llm-kernel-optimization promoted, instruction-tuning archived, index updated)
- Pages batch-archived: 29 (periphery non-AI concept/entity stubs)
- Cross-links added: 6+ (llm-kernel-optimization → flashattention-2022, attention-mechanism, transformers, inference-efficiency, llm-inference, quantization, etc.)

## Pages Created

| Page | Action | Status | Confidence |
|------|--------|--------|------------|
| [[sources/papers/flashattention-2022]] | created | active | 0.95 |

## Pages Updated

| Page | Action | Status | Confidence |
|------|--------|--------|------------|
| [[llm-kernel-optimization]] | promoted from stub | active | 0.3 → 0.72 |
| [[instruction-tuning]] | archived | archived | 0.3 |
| (29 periphery stubs) | batch-archived | archived | 0.3 |

## Carryover Open Items Resolved

- **(a) llm-kernel-optimization** — ✅ Promoted with FlashAttention (arXiv:2205.14135) as source anchor. Fetched and ingested the paper, wrote source summary page, wrote full reference content covering IO-aware attention kernels, quantization kernels, kernel fusion, and serving optimizations (PagedAttention/FlashDecoding). Confidence 0.72.
- **(b) instruction-tuning** — ✅ Checked: only source link (waldis-2026-instructions-shape-production) is itself an empty stub. No replacement source found. Archived as absorbed by broader fine-tuning concept.
- **(c) machine-learning.md** — Evaluated: 71 words, 13+ connections, body is mostly a nav hub with no real content. Conclusion: this is fine as a hub page. Machine learning is too broad and well-covered externally to need a definition page. Leave as-is.
- **(d) mass archive pass** — ✅ Batch-archived 29 clear periphery stubs: non-AI topics (alzheimers, lean-manufacturing, geopolitics-adjacent), too-broad umbrella concepts (pure-mathematics, methodology, technology, science, tools), non-AI entities (JWST, ESA, NASA), tool stubs (overlayfs, sqlite, taplo), and spike/experiment notes.
- **(e) hub cross-link audit** — ✅ mcp-logic (entities/projects/tys-repos/mcp-logic.md) adequately linked to its project ecosystem (efhf, categorical-reasoning, tys-repos). All inbound references (world-model, agent-native-design, eml-operator, epistemic-energy etc.) are concept pages using mcp-logic as a cross-reference — no reciprocal obligation. mop-edm-cognitive-architecture (synthesis) has 20+ comprehensive reciprocal connections. Both pass.

## Gap Analysis

- **Before this cycle**: 192 stubs (status: stub), 354 pages with confidence: 0.3
- **After this cycle**: 161 stubs (status: stub), 353 pages with confidence: 0.3
- **Net change**: −29 stubs (−31 archive +2 status changes: +1 promoted to active, +1 archived separately)
- **Remaining**: 161 stubs — 75 concepts, 12 entities, 74 synthesis/news
- Synthesis/news stubs (74) are a distinct category — news summary pages that naturally stay as stub unless a news event becomes significant enough to promote

## Open Items for Next Cycle

- [ ] **remaining ML-relevant concept stubs could use promotion**: nlp, language-models, graph-theory, network-theory, representation-learning, pattern-recognition, steering-vectors, sledgehammer (theorem proving), high-performance-computing, shapley-values, open-source-ai — these are genuine ML/AI topics with reference-quality content potential
- [ ] **entity stubs still at 12**: huggingface, anthropic, google-deepmind, openai-o-series, sakana-ai, priorlabs, priorlabstabpfn, darwinian-evolver — all AI-relevant entities that could be promoted with research
- [ ] **machine-learning.md hub page**: confirmed as hub, not content page — add a note in frontmatter to mark it explicitly as hub type to avoid future confusion
- [ ] **fine-tuning.md** (63 words, still a stub) — if promoted, it would properly absorb the archived instruction-tuning concept
