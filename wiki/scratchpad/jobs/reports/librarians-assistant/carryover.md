---
created: 2026-06-27
updated: 2026-06-27
type: carryover
summary: Librarians-assistant remediation carryover — tag normalization complete, reciprocal links and double frontmatter remain
tags: [librarians-assistant, carryover]
---

# Librarians-Assistant Carryover — 2026-06-27

## What Was Fixed
- **Tag taxonomy normalization (t_8f668600cf14102a): DONE**
  - Scanned 849 pages with tags (1204 unique tags before normalization)
  - Normalized 86 pages with 90 tag variant corrections (case/hyphen/space)
  - Case variants eliminated: 33 groups → 0
  - Hyphen/space variants eliminated: 4 groups → 0
  - Result: 1166 unique tags, all normalized to lowercase-hyphen form
  - Scope: all wiki/ subdirs (concepts, entities, synthesis, sources, scratchpad)

## Kanban Status
- [x] t_8f668600cf14102a (tag taxonomy): done — 2026-06-27

## What Remains
1. **Reciprocal link audit** — 795 non-reciprocal pairs; efficiency gate per carryover but worth revisiting if scope is bounded
2. **Double frontmatter block pages** — 8 pages with multiple `---` delimiters (markovian-carryover, tag-taxonomy, agent-taxonomies, replicant-mapping, research-brief-2026-05-09, research-brief-2026-05-13, two-council-architecture, harm-cases) — appear to be intentional section separators rather than duplicate blocks; investigation needed before fixing

## Hard Blockers
- None at core layer. Vault integrity is excellent.

## Notes
- MCP unavailable; used filesystem fallback
- Tag normalization rule: lowercase, hyphens, no spaces; preserve special tags (cs.AI, O(1), pass@k, etc.)
- 8 pages with multiple `---` delimitors require investigation before cleaning — some may be intentional section boundaries (markovian-carryover uses `---` as markdown ruler between sections)
- Reciprocal link audit: 795 non-reciprocal pairs identified; most are between closely related concept pages where return links would be noise