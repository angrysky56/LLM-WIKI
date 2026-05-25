---
summary: Librarian carryover 2026-06-19 — broken links zero, double-FM fixed on 2 pages, weil-gate stub created
tags: [librarian, carryover, audit]
updated: 2026-06-19
---

## Established

**Date:** 2026-06-19
**MCP Status:** Package import OK, MCP tools not registered in cron context (filesystem fallback)
**Trigger:** Scheduled cron

### Audit Metrics

| Metric | Value | Change |
|--------|-------|--------|
| Total pages | ~717 | stable |
| Broken wikilinks (core wiki) | 0 | -4 |
| Frontmatter gaps (core dirs) | 0 | stable |
| Orphans (0 inbound links) | 141 | unchanged |
| Non-reciprocal link pairs | 1297 | unchanged |

### Vault Health

- **Core wiki broken links:** ELIMINATED — 0 broken (was 4)
- **Double frontmatter blocks:** Fixed 2 pages (hermes-meta-cognition.md, spiral-architecture.md)
- **New stub created:** weil-gate.md (referenced in spiral-architecture.md)
- **MCP tools:** Package import OK, filesystem analysis fallback in use

### Fixed This Cycle

1. **Fixed double frontmatter on hermes-meta-cognition.md** — had two `---` blocks, consolidated into one clean block with all 8 required fields
2. **Fixed double frontmatter on spiral-architecture.md** — same pattern, consolidated
3. **Created weil-gate stub** — referenced as `[[weil-gate]]` in spiral-architecture.md connections section

## Open

1. **141 orphan pages** — high-value concepts with no inbound links (noted since 2026-06-16, low urgency)
2. **1297 non-reciprocal link pairs** — A→B without B→A; massive scope
3. `generate_insights()` — would timeout at 300s, skipping per protocol
4. Tag taxonomy normalization — not audited this cycle

## Heading

- Vault integrity excellent at core layer
- Broken link count at 0 — clean state
- Orphan reconnection remains the substantive open issue
- Non-reciprocal pairs: large scope, consider dedicated sprint