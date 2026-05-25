# Librarians-Assistant Carryover — 2026-06-19

## What Was Fixed
- **openpraparat.md elevation**: Replaced stub with full concept content derived from `utimula-openpraparat-2025.md` source paper — added Architecture, Key Results, and Connections sections with real content
- **artificial-life.md stub created**: New stub at `wiki/concepts/artificial-life.md` to resolve broken link from openpraparat.md — contains self-connections back to openpraparat and open-ended-evolution
- **Verified broken wikilinks: 0** (concepts/entities/synthesis — clean)
- **Verified orphan pages: 0** — openpraparat.md was the sole orphan; resolved
- **Verified frontmatter gaps: 0** in concepts/entities/synthesis

## What Remains
1. **Tag taxonomy normalization** — 1287 unique tags with inconsistent casing (UPPERCASE acronyms mixed with lowercase prefixes like `ai-`, `llm-`); large scope, needs dedicated sprint
2. **Reciprocal link audit** — 795 non-reciprocal pairs; efficiency gate per carryover but worth revisiting if scope is bounded
3. **Double frontmatter block pages** — 8 pages with multiple `---` delimiters (markovian-carryover, tag-taxonomy, agent-taxonomies, replicant-mapping, research-brief-2026-05-09, research-brief-2026-05-13, two-council-architecture, harm-cases) — these appear to be intentional section separators rather than duplicate blocks; investigation needed before fixing

## Hard Blockers
- None at core layer. Vault integrity is excellent.

## Notes
- MCP unavailable; using filesystem fallback
- 8 pages with multiple `---` delimitors require investigation before cleaning — some may be intentional section boundaries (markovian-carryover uses `---` as markdown ruler between sections)
- Reciprocal link audit: 795 non-reciprocal pairs identified; most are between closely related concept pages where return links would be noise (e.g., `metacognitive-architecture-closed-loop-self-regulation -> omcd` vs. vice versa — omcd links back to many other pages already)
