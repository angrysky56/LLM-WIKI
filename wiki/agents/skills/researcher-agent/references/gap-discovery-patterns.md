# Gap Discovery Patterns — Researcher Agent Reference

## Core Discovery Strategy

The carryover.md is the primary driver of the discovery cycle. Pattern:
1. **Carryover → most actionable gap first**: The Open Questions in carryover are ordered by urgency. The top unresolved item is usually the best starting point.
2. **Carryover → three categories**: Established (already covered), Open (needs decision/research), Heading (next cycle intent)
3. **Don't restart from scratch**: The gap list in the previous discovery report is the ground truth — don't re-scan the whole wiki, just follow up from where it left off.

## Stub-First Discovery (high-yield)

The most reliable gap signals are `status: stub` pages in `wiki/concepts/`. A stub means someone started the page and flagged it as incomplete.

### Priority Rules

| Condition | Priority |
|-----------|----------|
| Stub connects to active (non-stub) cluster | **High** — fill first |
| Stub connects only to other stubs | **Low** — batch with similar |
| Stub is linked to by multiple other stubs | **Elevated** — filling it elevates all linking stubs |
| Stub has high out-degree links | **High** — acts as hub for cluster |

### Priority Elevation Rule

When you fill a stub that other stubs link to, those connected stubs immediately elevate in priority:
- Stub A links to `[[emergence]]` (stub) → Stub A is medium priority
- `emergence` gets filled → Stub A is now high priority (connection to active concept is live)

**Real example (May 29 cycle):** `computational-irreducibility` linked to `emergence` (filled prior cycle) → elevated and filled first. `institutional-capture` linked to `institutional-accountability` → both filled in same cluster batch.

## Thin-Coverage Indicators

Beyond `status: stub`, these patterns indicate thin coverage:

1. **Short page + many wikilinks**: Page has 5+ outgoing links but less than 200 words of content — a "hub" page that's a navigation stub without substance
2. **High fan-out cluster**: A concept cluster where all pages reference each other but none have body content — orphaned cluster
3. **Concept with `confidence: 0.3`**: Low confidence flag correlates with thin coverage
4. **Tag-only summary**: A page whose summary is just the tag name rehashed — no real content
5. **Empty `## Why It Matters`**: Sections that exist but are empty or stub-tier

## Cluster-First vs Scattered Fill

### Cluster-First (recommended)

Stubs that share a thematic cluster (e.g., governance, emergence, reasoning) should be filled together. Benefits:
- Cross-links form naturally as you write
- Connections section writes itself
- Wiki lint stays clean

**Cluster examples from May 2026:**
- **Governance cluster**: `governance` → `institutional-capture` → `institutional-accountability` → `ai-governance-substrate` → `agentic-oversight`
- **Emergence cluster**: `emergence` → `computational-irreducibility` → `open-ended-evolution` → `scaling-laws`

### Scattered Fill

Stubs with no thematic relationship to each other, or stubs in different domains, should be filled by whatever has the strongest active connections that cycle.

## Cross-Link Check

After filling a page, check that all outgoing links in `## Connections` are reciprocated. This is the librarian's job but the researcher can do a first pass:

```bash
# Find non-reciprocal links (pages that link to this one but this one doesn't link back)
# From within the wiki directory:
rg "\[\[pagename\]\]" wiki/concepts/ -l  # who links TO pagename
```

## Gap List Management

The carryover.md is the ground truth for gaps. The discovery report's Gap Analysis section is a checkpoint, not a restart. The workflow:

1. Read carryover Open questions
2. Identify stubs that address those questions
3. Fill stubs in priority order
4. Update carryover Established with what was filled
5. Write new Open questions if new gaps discovered
6. Update carryover Heading with next cycle intent

## Remaining Gap List (as of Jun 9, 2026)

**Transformer infrastructure cluster (3 pages) — COMPLETE Jun 9:**
- `attention-mechanism` — filled (scaled dot-product attention, MHA, Flash Attention, GQA/MQA)
- `transformer-architecture` — filled (encoder-decoder, decoder-only, scaling)
- `kv-cache` — filled (PagedAttention, MQA/GQA memory reduction)

**Agent architecture cluster (2 pages) — COMPLETE Jun 9:**
- `autonomous-research` — filled (six-stage pipeline, failure modes, SEG Scientist)
- `agent-leak-benchmark` — filled (reconstruction attacks, LCGuard source)

**Reasoning/search cluster (3 pages) — COMPLETE Jun 9:**
- `causal-reasoning` — filled (SCM, do-calculus, counterfactuals, causal discovery)
- `MCTS` — filled (UCB1, AlphaZero, game-playing impact)
- `evolutionary-strategies` — filled (CMA-ES, NES, ML evolution)

**Security cluster (1 page) — COMPLETE Jun 9:**
- `adversarial-training` — filled (PGD/BIM, robust training, LLM applications)

**Governance cluster:** governance, agentic-oversight, accountability — all filled as of Jun 4.
`reward-hacking` — filled Jun 8 (connects to `institutional-capture` and `reward-modeling`).

**~125 stubs remaining** (134 total - 9 filled this cycle). Next priority: llm-agent-architecture, code-generation, video-llm.

## Search Strategies for Thin Coverage

| Strategy | Command |
|----------|---------|
| Find all stubs | `rg "status: stub" wiki/concepts/ -l` |
| Stub count | `rg "status: stub" wiki/concepts/ -l \| wc -l` |
| Low confidence stubs | `rg "confidence: 0\.[0-4]" wiki/concepts/` |
| Short pages with links | Find pages < 200 words AND have `## Connections` |
| Orphan stubs (only link to stubs) | For each stub, check if all link targets are also stubs |
| Check for duplicate stubs | `rg "\[\[stubname\]\]" wiki/` (search full vault for links to the stub) |

## Open Questions to Watch

These questions from carryover have been open multiple cycles. Before re-listing as "no data", ALWAYS search the wiki first — content may already exist:

1. MoE routing collapse under RLHF: no empirical data
2. Adaptive budget learning: no clear paper yet
3. Hybrid reward models (ELHSR + SD-Search): emerging direction, no full treatment
4. Reward hacking detectability: no reliable early-warning signal (surfaced Jun 8)