# Librarians-Assistant Carryover — 2026-05-31

## What Was Fixed

### P3: Frontmatter Completion (50+ pages)
- 40 concept pages: design-thinking, alqr-memory-estimates, reasoning, hermes_agent, absence-of-worst-case-metric, academic-peer-review, apphantasia, arcuate-fasciculus, brocas-area, critical-analysis, cryptographic-vs-semantic-alignment, emergent-communication, eml-operator, feedback-activity, feedforward-activity, frame-transmission, hopfield-network, hyperphantasia, institutional-capture-vs-species-framing, language-evolution, ml-evolution, myelination, open-ended-evolution, persistent-knowledge-compilation, research-methodology, scientific-writing, sheffer-stroke, spontaneous-activity-reshaping-hypothesis, surprise-based-learning, symbolic-regression, tag-taxonomy, titans, wernickes-area, astar-structural-pathfinding
- 4 people entity pages: dhruv-trehan, paras-chopra, roger-koenig-robert, tyler-hall
- 14 project/entity pages: mop-explorer, tys-repos, advanced-reasoning-mcp, aseke-compass-mcp, ast-mcp-server, conscience-servitor, ethical-ai-core, graph-rlm, hipai-montague, mcp-coordinator, mcp-logic, nexus, project-synapse-mcp, sentience-metaphysics, sheaf-consistency-enforcer, toward-transcendent-moral-instrumentality, verifier-graph, claude-code, agem, alphaevolve, goodrobot

### P1: Reciprocal Wikilinks (verified)
- efhf ↔ maximum-occupancy-principle — ALREADY reciprocal (efhf.md sources: [[maximum-occupancy-principle]], MOP links to efhf in connections)
- hermes_agent.md → load-bearing-reasoning — ALREADY has return link from reasoning.md

## What Remains

1. **~250-300 pages missing frontmatter** — agent carryovers, scratchpad files, news sources (not high-value)
2. **8 synthesis pages with extreme duplicate frontmatter** (26-34 blocks): cross-layer-drift-falsification, codegraph-hermes-integration-plan, librarian-report-2026-05-09, research-brief-2026-05-09, self-prompting-via-production-stage-architecture, essan-internal-representation, wiki-indexing-theory, research-brief-2026-05-13 — need individual targeted review, too complex for bulk cleaner
3. **MCP unavailable** — cannot use wiki_lint, wiki_cluster_pages, generate_insights; using full_audit.py + direct filesystem ops
4. **Broken wikilinks** — all in scratchpad/report files (structural noise per librarian carryover); content layer is clean

## Hard Blockers

- MCP unavailable — using full_audit.py + direct filesystem ops
- Complex synthesis pages with 26-34 frontmatter blocks — need individual review, not safe to auto-clean

## Heading

1. Continue frontmatter completion for remaining entity/synthesis pages
2. Complex synthesis pages with extreme duplicate blocks (individual review)
3. Run full_audit.py to verify broken link count dropped