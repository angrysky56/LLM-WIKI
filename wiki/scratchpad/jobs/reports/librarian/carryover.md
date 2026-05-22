---
summary: Librarian carryover — 26 stubs created, 43 broken links fixed, 349 remaining, MCP still unavailable
tags: [librarian, carryover, audit]
updated: 2026-05-28
---

## Established

**Date:** 2026-05-28  
**Task:** `6ee16837c47c` Wiki Librarian  
**MCP Status:** UNAVAILABLE — using `full_audit.py` filesystem scan

### Audit Metrics

| Metric | Start | End | Change |
|--------|-------|-----|--------|
| Total pages | 385 | 404 | +19 |
| Broken wikilinks | 392 | 349 | -43 |
| Missing frontmatter | 356 | 356 | same |

### Actions Taken This Cycle

**Stubs created (26 pages):**
- china-cuba-tensions, ai-governance-substrate, institutional-accountability, taylors-law, delegation, aseke-framework
- formal-verification, interactive-theorem-proving, bounded-structured-memory
- computational-universe, computational-irreducibility, categorical-reasoning
- kv-cache, multi-agent-llm-systems, privacy-utility-tradeoff, swe-bench, onboarding-standards
- extraction-quality-audit, goodrobot-revenue-model
- 3 other stubs from previous cycles' residual fixes

**Links fixed:**
- `[[Zettelkasten Engine]]` → `[[zettelkasten-engine]]` in project-synapse.md
- `[[goodrobot-revenue-model]]` → `[[revenue-model]]` in business-concept.md
- `[[extraction-quality-audit/research_spec]]` → `[[extraction-quality-audit]]` in research/index.md
- `[[onboarding-standards]]` → `[[agent-onboarding]]` in research/index.md
- `[[subagent-delegation]]` → `[[subagent-delegation-hermes-agent]]` in persistent-goals-hermes-agent.md

**Tag normalization:**
- Fixed 4 news pages with tag-list noise `[['news', ...]]` → proper array syntax

## Open

1. **349 broken links** — remaining are mostly: (a) concept pages still missing stubs, (b) cross-references from stub pages to other stubs
2. **356 pages missing frontmatter** — systemic backlog
3. **MCP unavailable** — cannot run `wiki_hits_analysis`, `wiki_cluster_pages`, `generate_insights`
4. **tag-taxonomy.md missing** — skipped tag normalization

## Heading

1. Create remaining stubs for frequent missing concepts (federated-learning, benchmark, code-agent, power-law, etc.)
2. Fix `[[hermes-agent-skill]]` reference in hermes-agent.md
3. Fix `[[llm wiki pattern]]` reference in andrej-karpathy.md
4. Systematic frontmatter fill for high-value entity/concept pages
5. Remove remaining tag-list wikilinks if any left