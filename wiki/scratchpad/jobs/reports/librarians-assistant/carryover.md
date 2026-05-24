# Librarians-Assistant Carryover — 2026-06-08

## What Was Fixed

### P3: Duplicate Frontmatter on Insight Pages (2 pages)
- `wiki/synthesis/insights/para-knowledge-architecture-cohesion-insight.md` — merged duplicate frontmatter blocks into single clean block
- `wiki/synthesis/insights/francesca-albanese-sanctions-case-insight.md` — merged duplicate frontmatter blocks into single clean block

### P3: Missing `type: synthesis` on Synthesis Pages (7 pages)
- `mop-edm-cognitive-architecture.md`
- `minimal-generative-architectures.md`
- `nairobi-protocol-gde.md`
- `synapse-retrieval-architecture.md`
- `ai-governance-substrate-analysis.md`
- `ctx2skill-on-efhf-rails.md`
- `causal-state-edm-ood-isomorphism.md`

## What Remains

1. **141 broken link targets in sources** (wiki/sources/) — para, knowledge-architecture, note-taking-systems, francesca-albanese, us-sanctions, icc, legal-accountability — these are mostly knowledge graph entity references that should map to entity pages or remain as external references
2. **349 non-reciprocal wikilinks** — mostly legitimate单向 links to maximum-occupancy-principle; not actionable
3. **9 synthesis/pages with no confidence/status** (system files, not critical)

## Hard Blockers

- **141 broken links in sources**: These are primarily entity references (para, knowledge-architecture, etc.) embedded in insight pages from the Zettelkasten engine. Creating entity pages for all of these is beyond scope — they represent the system's own terminology rather than missing external references.

## Heading

1. High-value wiki content (concepts/entities/synthesis) is now CLEAN — 0 broken links, 0 missing type/summary
2. This cycle: 9 fixes applied
3. If reactivated: audit the 141 source-level broken links for actual content gaps (vs. internal terminology)