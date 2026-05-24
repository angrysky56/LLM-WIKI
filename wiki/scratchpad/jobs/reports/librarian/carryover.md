---
summary: Librarian carryover 2026-06-08 — 30 frontmatter fixes, 2 orphans, job marked done
tags: [librarian, carryover, audit]
updated: 2026-06-08
---

## Established

**Date:** 2026-06-08
**Task:** `6ee16837c47c` Wiki Librarian — job marked done, no pending next run
**MCP Status:** OK — project-synapse-mcp venv confirmed working

### Audit Metrics

| Metric | Value | Change from prior |
|--------|-------|-------------------|
| Total pages | 578 | ~same |
| Broken wikilinks | 171 | same (all in scratchpad/report files — structural noise) |
| Missing frontmatter | 282 | -22 (from 304) |
| Orphans | 2 | log, insights (system files, not content orphans) |

### Actions Taken This Cycle

1. **16 entity/tool pages fixed** — added missing type/sources/status/confidence: load-bearing-reasoning, wolfram-physics-project, project-synapse, efhf, zettelkasten-engine, gemini, hermes-agent, hipai-montague, isabelle, mamba, mcp-logic, neo4j, obsidian-skills-repo, obsidian, prover9, superbpe
2. **14 synthesis pages fixed** — added missing type/sources/status/confidence to all synthesis pages
3. **Orphan scan** — confirmed only 2 orphans (log.md, insights.md — system files with no inbound expected)

### Verified Deep Pages (load-bearing — already substantive)

- `efhf.md` — 5-layer architecture
- `maximum-occupancy-principle.md` — full math + Prover9 verification
- `project-synapse.md` — MCP server architecture
- `edm-framework.md` — EDM paper + simultaneous discovery problem
- `scaling-laws.md` — full treatment with Chinchilla inline

## Open

1. **~282 pages missing frontmatter** — mostly scratchpad/report noise; high-value concept/entity pages mostly done
2. **171 broken wikilinks** — ALL in scratchpad/report files; actual wiki content is clean
3. **8 synthesis pages with duplicate frontmatter** — 26-34 blocks each, need individual review (cross-layer-drift-falsification, codegraph-hermes-integration-plan, librarian-report-2026-05-09, research-brief-2026-05-09, self-prompting-via-production-stage-architecture, essan-internal-representation, wiki-indexing-theory, research-brief-2026-05-13)

## Heading

1. No further librarian runs scheduled — job marked done with N/A
2. If reactivated: handle duplicate frontmatter blocks on complex synthesis pages