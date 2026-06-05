---
created: 2026-05-26
updated: 2026-06-06T08:10:00Z
type: carryover
summary: "Jun 6 cycle: FlashAttention source fetched + ingested, llm-kernel-optimization promoted (0.3→0.72), instruction-tuning archived (absorbed by fine-tuning), 29 periphery stubs batch-archived"
tags: [researcher, carryover]
---

## CarryoverState

### Established
- **llm-kernel-optimization promoted**: Jun 6 — fetched FlashAttention paper (arXiv:2205.14135), wrote source summary (0.95), promoted stub (0.3→0.72) with real content covering IO-aware attention, quantization, and serving kernels. Cross-linked to 6+ pages.
- **instruction-tuning archived**: Jun 6 — only source anchor (waldis-2026) is also an empty stub. Absorbed by general fine-tuning concept.
- **machine-learning.md confirmed hub**: Evaluated per carryover directive. 71 words, mostly connections list. Works as navigation hub — leave as-is.
- **29 periphery stubs batch-archived**: Jun 6 — non-AI topics (alzheimers, lean-manufacturing, india-energy-strategy, etc.), umbrella concepts (pure-mathematics, methodology, technology, science, tools), non-AI entities (JWST, ESA, NASA), tool stubs (sqlite, overlayfs, taplo, profiles), spike notes. Batch script: `/tmp/batch_archive_stubs.py`.
- **Hub audit**: mcp-logic (entity) and mop-edm-cognitive-architecture (synthesis) both adequately cross-linked. Reciprocal connections verified. No action needed.

### Open
- **[Intent]** Next cycle — (a) promote one or more ML-relevant concept stubs (nlp, language-models, graph-theory, steering-vectors, sledgehammer, shapley-values, open-source-ai — pick 1-2 with source anchors); (b) consider promoting entity stubs (huggingface, anthropic, google-deepmind, openai-o-series, sakana-ai, priorlabs); (c) evaluate fine-tuning.md for promotion (currently 63-word stub that would absorb the archived instruction-tuning); (d) add explicit hub-type marker to machine-learning.md frontmatter to prevent future confusion.
- **[Risk]** 161 stubs remain — 75 concepts, 12 entities, 74 synthesis/news. Remaining concepts are genuine ML/AI topics that need research to promote (external URL fetches). Synthesis/news stubs (74) are a distinct category — don't touch unless a news event becomes significant enough for promotion.
- **[Constraint]** Real-gap stub promotions now require external source fetching each time. The FlashAttention fetch worked cleanly. Each promotion cycle = 1-2 URL fetches + writing.

### Kanban Status
- [x] llm-kernel-optimization promoted with FlashAttention source
- [x] instruction-tuning archived (no replacement source)
- [x] machine-learning.md evaluated as hub page
- [x] 29 periphery stubs batch-archived
- [x] Hub audit: mcp-logic + mop-edm-cognitive-architecture both pass

## Last Run
2026-06-06 08:10Z (cycle 7)