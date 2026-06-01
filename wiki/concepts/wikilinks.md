---
summary: Wikilinks — Obsidian double-bracket syntax, retrieval-weight hierarchy, cross-cluster linking conventions
tags: [wikilinks, linking-syntax, obsidian, knowledge-management, wiki, navigation]
updated: 2026-06-01T09:16:55Z
---

---
created: 2026-06-03
updated: 2026-09-14
type: concept
summary: "Wikilinks — Obsidian's [[double-bracket]] syntax for semantic linking and the retrieval-weight hierarchy across wiki zones"
tags: [wikilinks, linking-syntax, obsidian, knowledge-management, wiki, navigation]
sources: []
status: active
confidence: 0.65
---

# Wikilinks

## Definition

A wikilink (also called a wiki link or internal link) is a hyperlink within a wiki page that points to another page in the same wiki, using a simplified syntax rather than a full URL. In Obsidian, the convention is `[[pagename]]` or `[[pagename|Display Text]]` for an alias. The wiki's MCP tools resolve these links to their target files regardless of subfolder — `[[neo4j]]` resolves to `neo4j.md` anywhere in the vault.

Wikilinks are the primary connective tissue of this knowledge graph. Unlike hyperlinks, which connect to external URLs, wikilinks express *conceptual relationships* between notes. The wiki's `query_knowledge` pipeline uses wikilinks as a retrieval signal: links in `## Connections` sections carry more retrieval weight than inline prose links.

## Syntax

### Basic
```
[[pagename]]                    → renders as "pagename", links to pagename.md
[[pagename|Display Text]]       → renders as "Display Text", links to pagename.md
```

### Wikilinks vs. Markdown Links

| Feature | Wikilink | Markdown Link |
|---------|----------|---------------|
| Syntax | `[[name]]` | `[text](url)` |
| Resolves to | Any vault file | Any URL or file path |
| Broken link detection | Obsidian flags them | No native detection |
| Bidirectional graph | Automatic via links | Manual |
| Display text | Defaults to filename | Customizable |

### Resolving Ambiguity

When multiple files share a basename (e.g., `concepts/agents.md` and `entities/agents.md`), Obsidian's link resolution follows this precedence:

1. Exact filename match in same folder
2. Exact filename match in root
3. Unique fuzzy match across vault
4. If multiple matches: disambiguation required (use full path)

The MCP `wiki_search` tool uses the same resolution logic.

## Retrieval Weight Hierarchy

The wiki distinguishes link weights for retrieval purposes:

**High weight** — Links in `## Connections` sections: explicit semantic relationships, used as primary retrieval signals by the `query_knowledge` pipeline's Stage 3 (wikilink expansion).

**Medium weight** — Links in `## See Also` or `## Related` sections: weaker associations, included in graph traversal but not primary signals.

**Low weight** — Inline prose links: contextual usage, included in full-text search but not in the structured wikilink graph.

This hierarchy means that when upgrading a stub, the `## Connections` section is the most important part — it's the part the knowledge graph actually uses.

## Cross-Cluster Linking

Wikilinks enable cross-cluster bridges — connections between established knowledge clusters that surface non-obvious relationships. For example, a page linking `maximum-occupancy-principle` (a physics/RL theory) to a security concept creates a path that a purely topical search would miss.

High-value cross-cluster links:
- Connect an established hub page to a new frontier concept
- Bridge two different domain clusters (e.g., MOP/EFHF × knowledge-graph)
- Link a source summary to its canonical concept page

## Connections

- [[synthesis/synapse-retrieval-architecture]]: The query_knowledge pipeline that uses wikilinks as a retrieval signal (Stage 3)
- [[maximum-occupancy-principle]]: Hub page demonstrating the retrieval-weight hierarchy
- [[concept-index]]: Navigation hub that relies on wikilinks for cluster mapping
- [[knowledge-management]]: Where wikilinks fit in the broader KM discipline
- [[information-architecture]]: Structural design of which wikilinks carry what weight

## Open Questions

1. **Should prose links in body count more?** The current system underweights inline wikilinks. A concept used in body prose (not just Connections) may be more central to the page's argument — should that increase its retrieval weight?

2. **Circular link detection:** Self-referential link chains (A→B→C→A) create navigation loops. Should these be flagged as errors or allowed as valid reasoning loops?
