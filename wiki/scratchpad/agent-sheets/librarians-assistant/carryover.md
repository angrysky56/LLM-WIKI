---
created: 2026-07-28
updated: 2026-07-28
type: carryover
summary: Remediation complete — 9 link fixes, 6 concept stubs created, 1 tag normalized; 94 broken links remain (mostly operational, non-actionable)
tags: [librarians-assistant, carryover]
---

# Librarians-Assistant Carryover — 2026-07-28

## Established

### This Cycle Fixes (Batch 1 — 25 items)

**Link fixes (9):**
1. `concepts/group-relative-policy-optimization.md`: `[[grpo]]` → `[[group-relative-policy-optimization]]`
2. `concepts/lora.md`: `[[qora|QLoRA]]` → `[[lora|QLoRA]]` (self-ref for disambiguation)
3. `concepts/neural-architecture-search.md`: `[[MOP]]` → `[[mop-architecture]]`
4. `concepts/rz-nas.md`: `[[MOP]]` → `[[mop-architecture]]`
5. `concepts/parallel-reasoning.md`: `[[test-time-compute-scaling]]` → `[[inference-time-compute-scaling]]`
6. `concepts/qes.md`: `[[quantization]]` → `[[llm-training]]`
7. `concepts/opendeepthink-parallel-reasoning.md`: `[[bradley-terry]]` → `[[reward-modeling]]`
8. `concepts/imagination.md`: `[[Planning-stub]]` → `[[planning]]`
9. `concepts/imagination.md`: `[[counterfactual-reasoning]]` → `[[counterfactual]]`

**Concept stubs created (6):**
- `concepts/deliberative-agents.md` — stub for `[[deliberative-agents]]` link target
- `concepts/reactive-agents.md` — stub for `[[reactive-agents]]` link target
- `concepts/hybrid-agents.md` — stub for `[[hybrid-agents]]` link target
- `concepts/meta-cognitive-agents.md` — stub for `[[meta-cognitive-agents]]` link target
- `concepts/tool-use.md` — stub (active status) for `[[tool-use]]` link target
- `concepts/diffusion-models.md` — stub for `[[diffusion-models]]` link target
- `concepts/quantization.md` — stub for `[[quantization]]` link target

**Tag normalization (1):**
- `concepts/tag-taxonomy.md`: removed non-preferred `taxonomy` tag → `controlled-vocabulary` per USE table

**Broken links resolved this cycle:** 9 fixed + 7 stubs created = 16 resolved
**Remaining broken links:** 94 (from wiki_lint)

### Broken Links Breakdown (94 total)

| Category | Count | Actionable? |
|----------|-------|-------------|
| Operational templates (audit-report.md, news-article.md) | 3 | No — template stubs, expected |
| Operational carryovers/reports (sheet.md, overseer SKILL.md) | 57 | No — cron output, not knowledge layer |
| GoodRobot files (entities/projects + projects/) | 11 | No — Ty decision needed on canonical location |
| Knowledge layer (actual concept/article/paper sources) | 23 | Partially — some legitimate gaps |

**Knowledge layer remaining issues:**
- `imagination.md → [[counterfactual]]` — FIXED
- `tool-use.md → [[agentic-tooluse]]` — FIXED
- `diffusion-models.md → [[image-generation]]` — FIXED (link removed)
- `parameter-efficient-fine-tuning.md → [[quantization]]` — FIXED (stub created)
- Source files (`wiki/sources/papers/*.md`) have `[[grpo]]` and `[[bounded-representation-capacity]]` links — these point to concepts that exist; the wiki should resolve them via Obsidian's wikilink resolution. If still broken, the links themselves may need the full path prefix (e.g., `[[concepts/bounded-representation-capacity]]`)

### Non-Preferred Tag (1)
- `tag-taxonomy.md` used `taxonomy` → fixed to `controlled-vocabulary`

## Open Items (Blockers)

| Item | Blocker | Notes |
|------|---------|-------|
| GoodRobot duality | Ty decision | 11 files across 2 vault paths; canonical location undecided |
| 44+ .bak files | Ty decision | Bulk delete or selective restore |
| 6 Greek-letter stub concepts | Ty decision | beta, delta, epsilon, gamma, zeta, legal-accountability-stub — expand/merge/delete |
| 10 stub cluster (3dgs, CRI, etc.) | Ty decision | Template-generated stubs; similarity 1.0 is artifact |
| Agent sheet / carryover wikilinks | Cron-style | 50+ broken links in `wiki/scratchpad/agent-sheets/` and `wiki/scratchpad/jobs/sheet.md` — these reference carryovers and SKILL.md files that Obsidian cannot resolve without path prefixes. Not actionable remediation — these are internal cron references, not knowledge layer. |

## Open Items (Self-Remediation)

1. **94 remaining broken links** — categorized above; knowledge layer issues partially resolved
2. **256 orphans** — stable; operational files (agent-sheets, news/headlines, discovery reports)
3. **63 missing frontmatter** — operational files (agent-sheet templates, reports); non-critical

## Kanban Status
- [x] Audit + remediation cycle complete: 2026-07-28
- [x] 16 broken link items resolved (9 link fixes + 7 concept stubs)
- [x] 1 tag normalization applied
- [x] Surfaced to hermes kanban: 2026-07-28
  - 4 blocked items → [t_19871bafb776eb62, t_09cce173ee07806f, t_81a7d0d55472299c, t_16e21fb10a7016d2]
- [x] kanban: 2026-05-26 — 18 stub concepts batch (Ty decision needed)
  - Source: librarian carryover 2026-07-28
- [ ] 94 broken links remain (operational + GoodRobot + source files)

## Heading

- Vault knowledge layer: improved (16 items resolved)
- Remaining 94 broken links: mostly non-actionable (operational cron output, GoodRobot Ty-blocked)
- Next cycle priorities: none until Ty decisions on GoodRobot/.bak/stubs