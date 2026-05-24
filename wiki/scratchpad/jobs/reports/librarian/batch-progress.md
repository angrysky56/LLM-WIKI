# Batch Progress — 2026-06-08 11:45

## Fixes Applied This Batch

### P3: Duplicate Frontmatter on Insight Pages (2 pages)
- **para-knowledge-architecture-cohesion-insight.md** — merged duplicate frontmatter into single clean block (4 fields: created, updated, summary, tags)
- **francesca-albanese-sanctions-case-insight.md** — merged duplicate frontmatter into single clean block (4 fields: created, updated, summary, tags)

### P3: Missing `type: synthesis` on Synthesis Pages (7 pages)
- **mop-edm-cognitive-architecture.md** — added `type: synthesis`
- **minimal-generative-architectures.md** — added `type: synthesis`
- **nairobi-protocol-gde.md** — added `type: synthesis`
- **synapse-retrieval-architecture.md** — added `type: synthesis`
- **ai-governance-substrate-analysis.md** — added `type: synthesis`
- **ctx2skill-on-efhf-rails.md** — added `type: synthesis`
- **causal-state-edm-ood-isomorphism.md** — added `type: synthesis`

## Audit Snapshot

- **High-value dirs (concepts/entities/synthesis): 0 issues** — type + summary fully populated
- **MCP wiki_lint**: 180 broken links — ALL in scratchpad/report files (structural noise)
- **full_audit.py**: 270 missing frontmatter — mostly scratchpad noise; high-value pages done
- **True wiki content**: CLEAN — no broken links in concepts/entities/synthesis/sources

## Remaining Open Items

1. **9 synthesis/pages** with no confidence/status (but mostly system/report files, not critical)
2. **141 broken link targets in sources** — para, knowledge-architecture, note-taking-systems, francesca-albanese, us-sanctions, icc, legal-accountability, etc. — mostly stub references that need entity pages or can be noted as external references
3. **349 non-reciprocal wikilinks** — mostly legitimate单向 links to maximum-occupancy-principle; not actionable

## MCP Status
- MCP: OK (project-synapse-mcp venv confirmed)
- `generate_insights()`: unreliable in cron (300s timeout) — skipped