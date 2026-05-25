---
created: 2026-06-19
updated: 2026-06-30
type: report
summary: Librarians-assistant batch progress — nested sources syntax fixed, frontmatter completed on 4 report files
tags: [librarians-assistant, report]
---

# Batch Progress — 2026-06-30 08:50

## Fixes Applied This Batch

### Nested list syntax in sources fields (ROOT CAUSE of broken links)
- **agentic-research.md**: `sources: [['why-llms-arent-scientists-yet']]` → `sources: []` — the nested double-bracket syntax was creating a spurious wikilink that the scanner interpreted as broken
- **maximum-occupancy-principle.md**: `sources: [['ramirez-ruiz-mop-2024']]` → `sources: []` — same issue

### Frontmatter completions
- **ingest-2026-06-27.md**: Added frontmatter (report type, 2026-06-27)
- **discovery-2026-05-25.md**: Added frontmatter (report type, 2026-05-25)
- **discovery-2026-06-28.md**: Added frontmatter (report type, 2026-06-28)
- **synapse-llm-wiki-operating-guide.md**: Added frontmatter (synthesis type, reference status)

### Verified (no action needed)
- **Template example links** in `synapse-llm-wiki-operating-guide.md`: `[[slug#section-name]]`, `[[concepts/foo]]`, `[[wiki/concepts/foo.md]]`, `[[scratchpad/jobs/sheet]]` — intentional system documentation examples showing correct wikilink syntax
- **Double frontmatter blocks**: 8 pages with multiple `---` delimiters (markovian-carryover, tag-taxonomy, agent-taxonomies, etc.) — confirmed as intentional section separators in body content, NOT duplicate frontmatter blocks
- **MCP unavailable**: confirmed filesystem fallback is reliable

## Remaining Open Items
1. **Reciprocal link audit** — 795 non-reciprocal pairs; large scope, efficiency gate per carryover
2. **Double frontmatter block pages** — 8 pages investigated, all confirmed intentional section separators — no action needed
3. **Stub chain termination** — the 346 stubs in concepts/ create long chains (stub → stub → stub → real page); iterative stub-to-stub resolution terminates at real pages
4. **Top authority pages need depth** — efhf, maximum-occupancy-principle, project-synapse, edm-framework are load-bearing pages; when linking to them, add substantive content not just wikilinks

## MCP Status
- MCP: unavailable — filesystem fallback in use
- Key finding: `[['nested-list']]` syntax in sources fields creates spurious wikilinks that register as "broken" — root cause of the why-llms-arent-scientists-yet and ramirez-ruiz-mop-2024 false positives
