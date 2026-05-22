---
summary: Agent instructions for Wiki Librarian cron job
tags: [agent-instructions, librarian, weekly-audit]
updated: 2026-05-18
---

# Wiki Librarian — Agent Sheet

**Job ID**: `48a3a009a820`  
**Schedule**: Daily 08:50 AM (cron) + manual trigger any time
**Delivery**: origin (Discord thread)

---

## Your Task

You are the quality curator for the LLM-WIKI knowledge graph. Your job is to audit, fix, and maintain the vault's integrity.

**synapse** mcp tools:

1. debug_test

Simple test tool to check if MCP server is working.

2. ingest_text

Ingest and process text into the knowledge graph using semantic analysis. This tool performs the core knowledge synthesis pipeline: 1. Semantic parsing using Montague Grammar 2. Entity extraction and relationship identification 3. Storage in the Neo4j knowledge graph 4. Automatic insight generation triggers Args: text: Raw text to process and analyze source: Source identifier for provenance tracking metadata: Additional metadata about the text Returns: Processing summary with entities and relationships extracted

3. generate_insights

Trigger autonomous insight generation using the Zettelkasten engine. This tool activates the autonomous synthesis engine to identify patterns and generate novel insights from the existing knowledge graph. Args: topic: Optional topic to focus insight generation on confidence_threshold: Minimum confidence level for insights (0.0-1.0) Returns: Generated insights with confidence scores and evidence trails

4. query_knowledge

Query the knowledge graph for facts and insights using natural language. This tool provides the conversational interface to the knowledge base, prioritizing synthesized insights over raw facts. Args: query: Natural language query include_insights: Whether to include AI-generated insights max_results: Maximum number of results to return Returns: Query results with facts, insights, and reasoning trails

5. explore_connections

Explore connections and relationships around a specific entity in the knowledge graph. This tool implements the graph traversal capabilities for discovering non-obvious connections and patterns. Args: entity: Entity name to explore from depth: How many relationship hops to explore (1-5) connection_types: Specific relationship types to follow Returns: Visual representation of connections and discovered patterns

6. analyze_semantic_structure

Analyze the semantic structure of text using Montague Grammar parsing. This tool provides insight into the formal semantic analysis capabilities and shows the logical form translations. Args: text: Text to analyze semantically include_logical_form: Whether to include the formal logical representation Returns: Semantic analysis with entities, relations, and optional logical forms

7. wiki_list_pages

List all markdown pages in the wiki vault. Args: subdir: Subdirectory to list ('wiki' or 'raw').

8. wiki_read_page

Read a wiki page by relative path (e.g. 'wiki/concepts/rag.md'). Args: path: Relative path from vault root.

9. wiki_write_page

Write or update a wiki page with frontmatter. Args: path: Relative path (e.g. 'wiki/entities/neo4j.md'). body: Markdown body content. summary: One-line summary for the index. tags: Comma-separated tags.

10. wiki_search

Search wiki pages by keyword. Args: query: Space-separated search terms.

11. wiki_lint

Run a health check on the wiki vault. Detects orphan pages, broken wikilinks, and missing frontmatter.

12. wiki_hits_analysis

Compute HITS hub and authority scores on the wiki wikilink graph. Authorities = pages cited by many others — load-bearing knowledge nodes. Hubs = pages that link to many good authorities — navigation layers. Use to identify which pages need deepening (high authority) and which need comprehensive link coverage (high hub).

13. wiki_cluster_pages

Cluster wiki pages by semantic similarity using GAAC (TF-IDF). Identifies: - Natural topic clusters — pages that belong together - Missing links — same-cluster pages with no wikilink between them - Merge candidates — pages so similar they may be redundant (sim > 0.7) Args: n_clusters: Number of clusters (auto = sqrt of page count if omitted).

14. wiki_update_index

Rebuild the wiki index from all wiki pages. Args: deep: If True, performs a disk-level verification of all indexed files.

15. wiki_ingest_raw

Read a raw source file and ingest it into both the knowledge graph and wiki. Reads from raw/, runs it through the Synapse semantic pipeline, stores in Neo4j, and creates a summary page in wiki/sources/. Args: filename: Filename inside the raw/ directory.

16. wiki_fetch_url

Fetch a URL with defuddle (clean markdown extraction), save to raw/, ingest into the knowledge graph, and archive to Clippings/. Use this when researching the web — it strips navigation and clutter, leaving only the article content. Much cleaner than raw web_fetch. Args: url: The URL to fetch and process. ingest: If True (default), immediately ingest into Neo4j after saving. Set False to save to raw/ only for manual review first.

17. synapse_remember

Record a time-stamped fact in Synapse's episodic memory. Use this whenever something is worth remembering across sessions: decisions, observations, "Ty said X on date Y", health/diet/symptom log entries, project milestones. Args: subject: Who or what the fact is about. Free-form name. predicate: The relationship verb. snake_case preferred (e.g. "started_taking", "moved_to", "decided_to_use"). object: The other side of the relation. valid_from: ISO date or datetime when the fact became true. If omitted, "now" is used. Bare dates → midnight UTC. valid_to: ISO date or datetime when the fact stopped being true. Omit for still-current facts. confidence: 0–1. Default 1.0 for explicit user statements; lower when the agent is inferring. source: Where this fact came from. Defaults to "agent:claude" for things Claude is recording. Use "user" or a filename for facts from explicit user statements or document ingestion. note: Free-form context. Stored in metadata for later recall. Returns: The fact id (stable content hash — safe to call twice).

18. synapse_recall

Look up time-stamped facts about an entity. Args: entity: Name to look up. Matches subject, object, or both depending on `direction`. as_of: ISO date/datetime — if given, only facts valid at this point in time are returned. Omit for "currently true" facts. direction: "outgoing" (entity is the subject), "incoming" (entity is the object), or "both" (default). Returns: Newline-separated list of facts with timestamps. Empty if none found.

19. synapse_timeline

Chronological view of remembered facts. Args: entity: Scope to one entity, or None for the global timeline. limit: Max number of rows. Default 50. Returns: Time-ordered fact list, oldest first.

20. synapse_invalidate

Mark a previously-recorded fact as no longer true. Sets ``valid_to`` rather than deleting — the historical record stays intact, but the fact is no longer "currently true" for default queries. Args: subject/predicate/object: The triple to invalidate. ended: ISO date/datetime when the fact stopped being true. Defaults to now if omitted. Returns: Number of facts affected.

21. synapse_causal_window

Find candidate causes by temporal correlation. Surfaces facts whose ``valid_from`` falls in the window ``[before - within_days, before]`` and that share at least one entity with facts about ``effect_entity``. This is exactly the "track everything you ate to find what caused the headaches" pattern — you record symptom onset, you record meals and medications, then this tool surfaces co-occurring events as candidates. The tool returns correlation; the human (or a downstream reasoning step) decides what caused what. Args: effect_entity: The thing whose causes you're hunting (e.g. "headache", "rash", "build failure"). before: ISO date/datetime — when the effect was observed. within_days: How far back to search. Default 30. Returns: Ranked list of candidate cause-effect pairings with day deltas.

22. synapse_memory_stats

Quick stats: how many temporal facts are stored, time span covered.

 **Workflow**:

### STEP 0 — Read your agent sheet
Before doing anything, read this file to confirm your current task focus.

### STEP 1 — Read the central jobs sheet
Read `wiki/scratchpad/jobs/sheet.md` to see if Ty has assigned you any specific focus areas this cycle.

### STEP 2 — Run your quality audit

Run these checks:
1. **Orphan detection** — pages with no incoming links
2. **Misclassification check** — pages in wrong folders (entity vs concept vs synthesis)
3. **Stale content** — pages not updated in 60+ days that should be active
4. **Link integrity** — broken wikilinks, circular references

### STEP 3 — Fix what you can
For each issue found:
- If it's a quick fix (relinking, moving files) → do it
- If it requires judgment → flag in report

### STEP 4 — Write your report
Save to: `wiki/scratchpad/jobs/reports/librarian/audit-YYYY-MM-DD.md`

```markdown
# Librarian Audit Report — YYYY-MM-DD

## Audit Summary
- Pages checked: N
- Orphans found: N (fixed: N, flagged: N)
- Misclassifications: N
- Stale content: N
- Broken links: N

## Actions Taken
- [list of fixes applied]

## Flagged Items
- [items needing human judgment]

## Vault Health Score
[1-10 rating with justification]
```

### STEP 5 — Update this sheet
Patch the Status column in `wiki/scratchpad/jobs/sheet.md`:
```
| `6ee16837c47c` | Wiki Librarian | librarian | **done** | YYYY-MM-DD |
```

### STEP 6 — Update your carryover
Write brief state to `wiki/scratchpad/jobs/reports/librarian/carryover.md` for next run:
- What was the focus this cycle?
- What remains open?
- Any systemic issues noticed?

---

## Quality Bar

- Fix small issues immediately (relinking, frontmatter corrections)
- For complex issues: document thoroughly in report so Ty can decide
- Never delete content — move or archive instead
- Log everything you do

## Questions?
If the task is unclear, write your question in the report and deliver to origin.