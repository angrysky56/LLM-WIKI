---
summary: Librarian carryover 2026-06-17 — 22 frontmatter gaps fixed, all core wiki clean
tags: [librarian, carryover, audit]
updated: 2026-06-17
---

## Established

**Date:** 2026-06-17
**MCP Status:** OK (package import succeeds, MCP tools not registered in cron context — using full_audit.py fallback)
**Trigger:** Scheduled cron

### Audit Metrics

| Metric | Value | Change |
|--------|-------|--------|
| Total pages | ~715 | stable |
| Broken wikilinks (core wiki) | 0 | stable |
| Frontmatter gaps (core dirs) | 0 | -22 from 22 |
| Orphans (0 inbound links) | 141 | unchanged |
| Non-reciprocal link pairs | 1297 | unchanged |

### Vault Health

- **High-value dirs (concepts/entities/synthesis):** CLEAN — all 22 missing frontmatter pages fixed (2026-06-17)
- **Core wiki broken links:** ELIMINATED — 0 broken (last: 2026-06-16)
- **PDF contamination:** None
- **MCP tools:** Package import OK, but tools not registered in cron context — using filesystem analysis

### Fixed This Cycle

**22 frontmatter gaps closed** — all 8 required fields now present:
- concepts: markovian-carryover (+updated), astar-structural-pathfinding (+sources), para-methodology (+sources), metacognitive-architecture-closed-loop-self-regulation (+sources)
- entities: note-taking-systems-stub, knowledge-architecture-stub, us-sanctions-stub, legal-accountability-stub (all +sources), goodrobot (consolidated double-FM, +status)
- synthesis: 13 pages received missing fields (created/sources/status/confidence as appropriate)

## Open

1. **141 orphan pages** — high-value concepts with no inbound links (noted since 2026-06-16, low urgency)
2. **1297 non-reciprocal link pairs** — A→B without B→A; massive scope, would require systematic traversal
3. `generate_insights()` — would timeout at 300s, skipping per protocol
4. Tag taxonomy normalization — not audited this cycle

## Heading

- Vault integrity excellent at core layer (concepts/entities/synthesis)
- Orphan reconnection is the remaining substantive issue — requires content judgment
- Non-reciprocal pairs: large scope, consider dedicated sprint in future