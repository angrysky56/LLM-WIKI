---
summary: Librarian carryover — 10 stubs created, broken links down 328→314, MCP still unavailable
tags: [librarian, carryover, audit]
updated: 2026-05-29
---

## Established

**Date:** 2026-05-29  
**Task:** `6ee16837c47c` Wiki Librarian  
**MCP Status:** UNAVAILABLE — using `full_audit.py` filesystem scan

### Audit Metrics

| Metric | Start | End | Change |
|--------|-------|-----|--------|
| Total pages | 437 | 437 | same |
| Broken wikilinks | 328 | 314 | -14 |
| Missing frontmatter | 349 | 349 | same |
| Stubs created this cycle | — | 10 | +10 |

### Top Authorities (by prior HITS — MCP only)
- efhf, maximum-occupancy-principle, project-synapse, edm-framework
- These load-bearing pages need depth; frontmatter still incomplete on most

### Stubs Created This Cycle
- in-context-learning.md, catastrophic-forgetting.md, emergence.md, scaling-law.md
- agentic-oversight.md, institutional-capture.md, geopolitics.md
- evaluation.md, isabelle-hol.md, agent-onboarding.md

## Open

1. **349 pages missing frontmatter** — systemic backlog; `hermes_agent.md` frontmatter fixed this cycle as proof-of-concept
2. **314 broken links** — reduced from 328 by stub creation; remaining are mostly:
   - `[['news', ...]]` tag-list noise in audit/report files (structural false positives)
   - Cross-stub references to other stubs still being resolved
   - `[[hermes-agent-skill]]` in log.md (dynamic, ignore)
3. **MCP unavailable** — cannot run `wiki_hits_analysis`, `wiki_cluster_pages`, `generate_insights`
4. **tag-taxonomy.md missing** — skipped tag normalization
5. `[[llm-wiki-pattern]]` referenced as concept but source page exists at `sources/articles/llm-wiki-pattern.md` — not a broken link, just needs concept page
6. `[[engineering-internal-awareness]]` referenced in ingest reports but no target found

## Heading

1. Create `wiki/concepts/llm-wiki-pattern.md` (concept) — heavily referenced but only exists as source article
2. Systematic frontmatter fill for high-value pages: entities/projects, concepts with `status: reference`
3. Fix `engineering-internal-awareness` reference or create stub
4. Fix tag-list wikilinks `[['news', ...]]` in remaining audit/report files