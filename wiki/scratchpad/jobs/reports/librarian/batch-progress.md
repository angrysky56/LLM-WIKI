# Batch Progress — 2026-05-29 09:20

## Fixes Applied This Batch

### Broken Wikilinks Fixed (2 pages)
- wiki/entities/tools/hermes-agent.md: `[[hermes-agent-skill]]` → `[[hermes-agent]]`
- wiki/entities/people/andrej-karpathy.md: `[[LLM Wiki Pattern|wiki/sources/llm-wiki-pattern]]` → `[[llm-wiki-pattern]]`

### Stubs Created (22 pages)
- accountability.md, governance.md, institutional-design.md
- category-theory.md, mathematical-reasoning.md
- formal-methods.md, proof-assistant.md
- attention-mechanism.md, transformer-architecture.md
- agentic-hierarchy.md, subagent-delegation.md, multi-agent-coordination.md
- data-privacy.md, federated-learning.md
- benchmark.md, code-agent.md
- power-law.md, power-law-scaling.md, scaling-laws.md
- allometric-scaling.md
- great-power-rivalry.md, proxy-signalling.md

### Frontmatter Completions (6 concept pages)
- affective-ai-inner-architecture.md: added type, sources, status, confidence
- agentic-research.md: added type, sources, status, confidence; fixed tags (was `[[agentic-research]]`)
- length-generalization.md: cleaned duplicate frontmatter, added sources, status
- chain-of-thought.md: cleaned duplicate frontmatter, fixed summary trailing period
- rag.md: added created, updated, type, sources, status, confidence; normalized tags to lowercase
- reward-modeling.md: added created, updated, sources, status, confidence; added tags
- spin-vs-substrate.md: added type, sources, status, confidence
- neural-long-term-memory.md: added type, sources, status, confidence
- meta_harness_loop.md: added type, sources, status, confidence
- mechanistic-interpretability.md: added sources, status, confidence
- activation-steering.md: added sources, status, confidence

## Remaining Open Items
- 331 broken links remain (mostly news-tag arrays and non-value stubs)
- 346 pages missing frontmatter (large backlog; focus on concept/entity pages)
- 284 orphan pages (mostly news articles with no expected inbound links)
- MCP still unavailable — using full_audit.py filesystem scan

## Next Batch Starts With
- P3: Continue frontmatter for high-value concept/entity pages (hidden-states already complete, proceed to graphrag, memex, etc.)
- P1: Some of the 22 new stubs need reciprocal links back from pages that reference them