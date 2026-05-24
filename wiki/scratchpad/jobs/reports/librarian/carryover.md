---
summary: Librarian carryover 2026-06-14 — vault stable, no changes
tags: [librarian, carryover, audit]
updated: 2026-06-14
---

## Established

**Date:** 2026-06-14  
**MCP Status:** OK — project-synapse-mcp venv confirmed working, but MCP tools not registered via synapse_mcp.wiki_tools (fallback: full_audit.py)
**Trigger:** Manual re-run of completed job

### Audit Metrics

| Metric | Value | Change from prior |
|--------|-------|-------------------|
| Total pages | 590 | -1 (591→590) |
| Missing frontmatter | 270 | same |
| Broken wikilinks | 181 | same |
| Orphans (filesystem) | 1 | +1 (critical-initialization-biological-neural-networks.md) |

### Vault Health

- **High-value dirs (concepts/entities/synthesis):** CLEAN — all load-bearing pages (efhf, maximum-occupancy-principle, project-synapse, edm-framework) have proper frontmatter
- **Sources (papers/articles/repositories):** ~50 article/news pages missing type/sources/status/confidence — mostly in `wiki/sources/news/` and `wiki/sources/articles/`
- **Scratchpad/report files:** 270 missing frontmatter, 181 broken wikilinks — structural noise, non-critical
- **PDF contamination:** None found

## Open

1. ~270 pages missing frontmatter — dominated by scratchpad noise (agent sheets, job reports)
2. ~181 broken wikilinks — all in scratchpad/report files, not wiki content
3. ~50 article/news sources still need type/sources/status/confidence in `wiki/sources/`
4. 1 orphaned paper: `wiki/sources/papers/critical-initialization-biological-neural-networks.md` — no inbound links
5. `generate_insights()` would timeout at 300s — skip if MCP unavailable

## Heading

- Vault is stable — no new issues introduced this cycle
- If continuing: focus on `wiki/sources/news/` article pages (add type/source/status/confidence)
- Orphan page `critical-initialization-biological-neural-networks.md` needs either a wikilink from a related page or a mention in a survey/overview page