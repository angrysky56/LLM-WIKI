---
summary: Librarian carryover 2026-06-08 — 17 frontmatter fixes, 2 stubs, MCP OK
tags: [librarian, carryover, audit]
updated: 2026-06-08
---

## Established

**Date:** 2026-06-08
**MCP Status:** OK — project-synapse-mcp venv confirmed working
**Job:** `6ee16837c47c` marked done in jobs sheet (N/A next run)

### Audit Metrics

| Metric | Value | Change from prior |
|--------|-------|-------------------|
| Total pages | 588 | +10 |
| Missing frontmatter | 270 | -17 (287→270) |
| Broken wikilinks | 180 | -3 (183→180) |
| Orphans | 0 | same |

### Actions Taken This Cycle

1. **2 stubs created** — `code-generation.md`, `grpo.md` in `wiki/concepts/`
2. **10 concept pages fixed** — added `type: concept` to pages missing it: absence-of-worst-case-metric, academic-peer-review, aphantasia, arcuate-fasciculus, brocas-area, critical-analysis, cryptographic-vs-semantic-alignment, emergent-communication, eml-operator, feedback-activity
3. **3 entity/project pages fixed** — added `created` to: alphaevolve.md, goodrobot.md, agem.md
4. **6 paper sources fixed** — added `type: paper`: betteti-baggio-bullo-zampieri-idp-hopfield-2025, decoupling-perception-reasoning-vlm-post-training, deltabox-stateful-agent-checkpoint-rollback-2026, eidetic-learning-2021, odrzywolek-eml-2026, production-llm-agent-runtime-architecture-patterns
5. **hermes_agent.md** — fixed misordered frontmatter (type/sources/status/confidence before summary)
6. **edm-framework.md** — added `created`, `updated`, `confidence: 0.95`

### Remaining Issues

- **~180 broken wikilinks** — all in scratchpad/report files (structural noise, not content)
- **~270 pages missing frontmatter** — mostly scratchpad noise; high-value pages mostly done
- **8 synthesis pages with duplicate frontmatter** — cross-layer-drift-falsification (40 `---`), codegraph-hermes-integration-plan (58), librarian-report-2026-05-09 (58), research-brief-2026-05-09 (37), self-prompting-via-production-stage-architecture (13), essan-internal-representation (23), wiki-indexing-theory (11), research-brief-2026-05-13 (15) — need individual review

## Open

1. Duplicate frontmatter blocks on 8 synthesis pages (high-effort individual fixes)
2. ~270 frontmatter debt (scratchpad noise, low priority)
3. ~180 broken wikilinks in scratchpad (structural, not content)
4. Insight generation timed out (expected at 300s limit)

## Heading

- Job marked done — N/A next run
- If reactivated: tackle duplicate frontmatter blocks on synthesis pages