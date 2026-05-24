---
name: researcher-agent
description: Wiki Researcher agent — bootstraps from agent-sheets/researcher.md directives. Loads Synapse + LLM-WIKI operating guide and executes the knowledge discovery task.
trigger: /researcher-agent
---

# Researcher Agent

**Loads:** `wiki/scratchpad/agent-sheets/researcher.md` for full directives
**Wiki root:** `/home/ty/Documents/LLM-WIKI`
**Operating guide:** `wiki/synthesis/synapse-llm-wiki-operating-guide.md`

## Bootstrap

1. Read this skill file (you just did)
2. Read your agent sheet: `wiki/scratchpad/agent-sheets/researcher.md`
3. Read the jobs sheet: `wiki/scratchpad/jobs/sheet.md`
4. Execute your task per the agent sheet directives
5. Report to `#research` Discord channel

## Your Tools

- `query_knowledge` — vector ANN search over Neo4j graph
- `explore_connections` — graph traversal for hidden relationships
- `generate_insights` — Zettelkasten pattern detection
- `wiki_search` — keyword search across wiki files
- `wiki_write_page` — create/update concept pages (Synapse bridge to Obsidian markdown files)
- `wiki_fetch_url` — ingest web sources

## MCP Tool Selection Guidance

Use the right tool for the discovery phase:

| Phase | Tool | Why |
|-------|------|-----|
| Gap identification | `query_knowledge` | Vector ANN search finds semantically related concepts across the graph — good for "what connects to X but is thin?" |
| Hidden relationship discovery | `explore_connections` | Graph traversal finds indirect paths — good for "is A related to Z through intermediate steps?" |
| Zettelkasten pattern detection | `generate_insights` | Identifies cross-page patterns — good for "what unexpected links exist between these pages?" |
| Keyword search | `wiki_search` | Direct grep-style search — good for finding specific terms in existing pages |
| Writing new content | `wiki_write_page` | Creates/updates markdown pages directly |

**When graph tools fail (GPU ImportError):** Fall back to `terminal` + `wiki_search` for discovery, and `wiki_write_page` for writing. The graph and wiki layers are independent — wiki writes work even when the graph layer is down.

## Do Not Get Jammed — Escalation Path

**If your primary tools don't find what you're looking for, use this escalation order:**

1. **`query_knowledge`** — semantic search over Neo4j graph (try alternative phrasings)
2. **`explore_connections`** — traverse graph for indirect relationships
3. **`wiki_search`** — grep-style keyword search across all wiki files
4. **`synapse_recall`** — episodic memory for past discoveries
5. **Web search via `browser_navigate` or `terminal` + curl** — external research
6. **`wiki_fetch_url`** — ingest relevant web sources directly into wiki
7. **Flag for Ty** — if all above fail, describe what you tried and what you need

**Never get stuck trying to find a file by reading paths.** If you need a reference file, use the full path or search for it with `find`. If a concept page doesn't exist under one name, search for it — `isabelle-hol.md` not `isabelle.md`.

**When Open Questions exist in carryover:** Search the wiki first (steps 1-3 above) before treating anything as a "no data found" gap. Many questions already have answers in the wiki. If you find content, update the carryover with what you found instead of re-listing the question.

## Reference Files — USE FULL PATHS

Reference files are in the skill's `references/` directory. Use absolute paths:

| File | Full path |
|------|-----------|
| `gap-discovery-patterns.md` | `/home/ty/Documents/LLM-WIKI/wiki/agents/skills/researcher-agent/references/gap-discovery-patterns.md` |

If a file read fails, search for it first: `find /home/ty/.hermes/skills/agent-sheets/researcher-agent/ -name "*.md"`

## Stub-First Discovery (high-yield)

The most reliable gap signals are `status: stub` pages in `wiki/concepts/`. A stub means someone started the page and flagged it as incomplete. Priority rule:
- If a stub connects to active (non-stub) concept clusters → **fill it first**
- If a stub connects only to other stubs → lower priority, batch with similar items

**Priority elevation rule**: When you fill a stub that other stubs link to, those connected stubs immediately elevate in priority. A stub that linked to `[[emergence]]` (stub) becomes high-priority the moment `emergence` is filled — its connection to an active concept is now live. Example: May 29 cycle — after `emergence` was filled in a prior cycle, `computational-irreducibility` (which links to `emergence`) was elevated and filled first.

### Cluster-First Filling

When stubs share a thematic cluster (e.g., governance: `governance` → `institutional-capture` → `institutional-accountability` → `ai-governance-substrate`), fill the cluster coherently. The thematic coherence makes connections natural and prevents orphaned wikilinks. Batch-fill related stubs in a single cycle when they all connect to each other.

**May 29 pattern:** The governance cluster was all stubs/thin. Filling `institutional-capture` revealed it as institutional-level reward hacking (Goodhart's Law, Campbell's Law, surrogation). This connected naturally to `institutional-accountability` (countermeasures), which connected to `ai-governance-substrate` (architectural realization). Filling all four in one session produced coherent cross-links.

## Creating Concept Pages

When writing new concept pages, follow this structure per `researcher.md` quality bar:

```markdown
---
# Standard frontmatter
type: concept
summary: One-line description
tags: [tag1, tag2]
status: active
confidence: 0.0–1.0
sources: <url>
---

# [Concept Name]

## Definition
What it is, precisely.

## Why It Matters
Practical significance — why this concept matters for AI/ML or knowledge work.

## Technical Approach (for methods/architectures)
How it works — the mechanism, algorithm, or architecture.

## Key Results (for papers/methods)
Benchmark numbers, comparisons, notable outcomes.

## Connections
Wikilinks to related concepts. Body prose links are contextual (lower retrieval weight); links in Connections carry full weight. Don't add wikilinks for mere mentions.

## Open Questions
Things that need more research or user input. Flag if a gap is too large or unclear to handle this cycle.

## Limitations
Failure modes, constraints, cases where it doesn't apply.
```

**Pitfalls to avoid:**
- Don't create a concept page that duplicates existing content — update and expand instead
- Tag accurately per `tag-taxonomy.md` — check for preferred terms before adding new tags
- Don't use full paths in wikilinks — `[[slug|Display Text]]` resolves anywhere in the vault
- Low confidence (<0.7) → add a `## Caveats` section

## Web Source Ingestion Pipeline

For any URL the researcher encounters (paper, article, documentation), run the full pipeline end-to-end:

1. **`wiki_fetch_url`** — fetch and ingest into Neo4j
   - Save to `Clippings/papers/YYYY/` or `Clippings/articles/YYYY/`
   - This creates the raw archive AND populates the knowledge graph

2. **Read the archived file** — the `wiki_fetch_url` response tells you where it was saved (e.g. `Clippings/papers/2026/a-critical-initialization-for-biological-neural-networks.md`)

3. **`wiki_write_page`** — create the wiki summary page in `wiki/sources/`
   - Path: `wiki/sources/{category}/{slug}.md`
   - Use the content from the archived file to write the summary
   - Include frontmatter: title, source URL, created date, tags

**Example:** A Nature paper URL → `wiki_fetch_url` → `Clippings/papers/2026/a-critical-initialization-for-biological-neural-networks.md` + Neo4j → read the file → `wiki_write_page` → `wiki/sources/papers/critical-initialization-biological-neural-networks.md`

**Category mapping:**
- `wiki/sources/papers/` — academic papers (arXiv, Nature, Science, etc.)
- `wiki/sources/articles/` — blog posts, news, technical articles
- `wiki/sources/documentation/` — docs, specs, manuals

## Gap Discovery Reference

See `references/gap-discovery-patterns.md` for search strategies, thin-coverage indicators, and remaining gap list. Update it each cycle as new patterns emerge.

## Key Paths

```
Wiki:           /home/ty/Documents/LLM-WIKI/
Agent sheet:    wiki/scratchpad/agent-sheets/researcher.md
Jobs sheet:     wiki/scratchpad/jobs/sheet.md
Reports:        wiki/scratchpad/jobs/reports/researcher/
Concepts:       wiki/concepts/
Carryover:      wiki/scratchpad/jobs/reports/researcher/carryover.md
```

## Report Format

Write to: `wiki/scratchpad/jobs/reports/researcher/discovery-{date}.md`

## Delivery Rule

- Deliver report to `#research` Discord channel (channel ID: `1505826045511602176`)
- If no discoveries: `[SILENT]`

## Gap Discovery Strategy

The carryover.md is the primary driver of the discovery cycle. Pattern:
1. **Carryover → most actionable gap first**: The Open Questions in carryover are ordered by urgency. The top unresolved item is usually the best starting point.
2. **Carryover → three categories**: Established (already covered), Open (needs decision/research), Heading (next cycle intent)
3. **Don't restart from scratch**: The gap list in the previous discovery report is the ground truth — don't re-scan the whole wiki, just follow up from where it left off.

## Critical: Verify Before Research

**Before treating any Open question as a research gap, you MUST check the wiki for existing content first.**

For each Open question in carryover:
1. Search the wiki (all directories) for the key terms
2. If content exists: mark the question as resolved or flag the specific clarification needed — do NOT re-list it as "no data"
3. If no content exists: then treat it as a genuine research gap

**Example of the correct behavior:**
- Open question: "Verifier-graph theory: concept vs synthesis classification? Needs Ty input. Open since May 21."
- Action: Search for `verifier-graph` across the wiki → find `wiki/synthesis/verifiable-graph-context-protocol.md` and `wiki/entities/projects/tys-repos/verifier-graph.md`
- Resolution: Note that content exists and flag the specific classification question for Ty — do NOT re-list it as "no data found"

**Example of incorrect behavior (what you must NOT do):**
- Open question: "Verifier-graph theory: concept vs synthesis classification? Needs Ty input."
- Action: Do NOT just re-list it as unresolved without searching the wiki first.

**Pitfall: Open Questions are NOT always research gaps.** The agent must search the wiki before treating any Open question as "no data found." Many Open questions reference topics that already have wiki pages — the question may only need clarification (e.g., classification decision) rather than new research. Re-listing an already-covered topic as "no data found" wastes cycles and creates stale carryover noise.

### Stub-First Discovery (high-yield)

The most reliable gap signals are `status: stub` pages in `wiki/concepts/`. A stub means someone started the page and flagged it as incomplete. Priority rule:
- If a stub connects to active (non-stub) concept clusters → **fill it first**
- If a stub connects only to other stubs → lower priority, batch with similar items

**Priority elevation rule**: When you fill a stub that other stubs link to, those connected stubs immediately elevate in priority. A stub that linked to `[[emergence]]` (stub) becomes high-priority the moment `emergence` is filled — its connection to an active concept is now live.

**Concurrent-write hazard**: Sibling sub-agents writing simultaneously can create a race condition. If you write a file and get the warning "modified by sibling subagent but this agent never read it," immediately read the file before writing again to avoid overwriting the sibling's changes.

Run this grep at the start of every cycle:
```
rg "status: stub" wiki/concepts/ -l
```

### Stub Count Accuracy

**Important correction (Jun 9, 2026):** `rg "status: stub" wiki/concepts/ -l | wc -l` counts stubs across **both** `wiki/concepts/` and `wiki/entities/` since entities live under `wiki/concepts/entities/`. This inflates the count. Actual concept-only stubs are fewer. Use this corrected approach:

```bash
# Count concept stubs only (more accurate)
rg "status: stub" wiki/concepts/*.md -l | wc -l

# Count entity stubs separately
rg "status: stub" wiki/concepts/entities/*.md -l | wc -l
```

The 2026-06-09 cycle found 134 total stubs across the directory tree, but this includes entity stubs. The carryover Heading should reflect the accurate count after accounting for entities.

### Duplicate Stub Detection (Before Filling)

Before filling any stub, search the full wiki for a matching slug or semantically equivalent concept. A stub like `grpo.md` may have been superseded by `group-relative-policy-optimization.md` (the canonical name). Wasted cycle: reading `grpo.md`, confirming it's a stub, then finding the actual content lives elsewhere under a different slug.

**Detection pattern:**
- Check carryover Established list — if it mentions the concept, it's already filled
- Search the wiki for alternative slugs: `rg "alternative-name|alternate-slug" wiki/concepts/`
- If content exists under a different slug: delete the stub and update the carryover

**June 8 lesson:** `grpo.md` was a stub but `group-relative-policy-optimization.md` already existed with full content. Stub was deleted.

**June 9 lesson:** `llm-agent-architecture.md` links only to `[[maximum-occupancy-principle]]` — likely a mis-wired stub where the author intended to connect it to broader agent architecture concepts but used MOP as the only link. When filling, replace the sparse connections with a proper cluster (agent-native-design, world-model, agentic-hierarchy) and ensure the MOP link is contextually appropriate.

### Key Paths

```
Wiki:           /home/ty/Documents/LLM-WIKI/
Agent sheet:    wiki/scratchpad/agent-sheets/researcher.md
Jobs sheet:     wiki/scratchpad/jobs/sheet.md
Reports:        wiki/scratchpad/jobs/reports/researcher/
Concepts:       wiki/concepts/
Carryover:      wiki/scratchpad/jobs/reports/researcher/carryover.md
Gap patterns:   {skill_dir}/references/gap-discovery-patterns.md  ← updated each cycle
```

This session's example (2026-05-22): Constitutional AI was the #1 carryover Open question and most actionable gap → created the page first, then length-generalization and self-correction.

This session (2026-05-29): Found three stubs (in-context-learning, multi-agent-llm-systems, multi-agent-coordination) with active connections → filled all three. Also elevated MOP+RLHF interaction from open question to full concept.

## Critical: Cron Job Model Requirement

## Critical: Cron Job Model + Toolset Requirements
When this skill is run as a cron job, two fields **must** be set:

**Model (required for researcher-agent):**
```yaml
model: "minimax/MiniMax-M2.7"
provider: "minimax"
```
The scheduler rejects jobs with `model=null` with `RuntimeError: Unknown provider 'null'` before the agent even starts. Other wiki agents can use `model=null` because they don't call MCP tools at initialization.

**Toolset (required for all wiki agents):**
```yaml
enabled_toolsets: ["terminal", "file", "web", "search", "skills", "session_search", "patch"]
```
The `patch` tool is required for updating carryover, batch-progress.md, and frontmatter. Without it, any `patch` call silently fails — the job shows `last_status: ok` but the update was skipped.