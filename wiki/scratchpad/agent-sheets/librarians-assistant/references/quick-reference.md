# librarians-assistant — Fix Priority Quick Reference

## Theory

From `wiki/synthesis/wiki-indexing-theory.md`:
- **High-authority pages** (top HITS) = load-bearing nodes — prioritize content quality
- **GAAC same-cluster, no link** = missing connection — add reciprocal wikilinks
- **Reciprocal links** = thesaurus RT relationship (always bidirectional)
- **Tag taxonomy** = USE/UF/BT/NT/RT — normalize non-preferred tags per tag-taxonomy.md

## Priority Order (execute in this order)

### 1. Reciprocal Link Fixes (GAAC-driven)
Pattern: same cluster, no wikilink between pages
Fix: add `[[PageA]]` to PageB and `[[PageB]]` to PageA
Use `wiki_read_page` to verify context before adding links.

### 2. Tag Normalization (per tag-taxonomy.md)
Pattern: non-preferred tag in use
Fix: replace with canonical USE term

USE reference table (inline from tag-taxonomy.md):
| Non-preferred | USE instead |
|---|---|
| `embedding` | `embeddings` |
| `vector-embedding` | `embeddings` |
| `semantic-search` | `vector-search` |
| `ANN` | `vector-search` |
| `fulltext-search` | `keyword-search` |
| `graph-RAG` | `graphrag` |
| `PKM` | `knowledge-management` |
| `KG` | `knowledge-graph` |
| `taxonomy` | `controlled-vocabulary` |
| `scientometrics` | `science-of-science` |
| `bibliometrics` | `science-of-science` |
| `method` | `methodology` |

### 3. Frontmatter Completions
Pattern: missing `summary`, `tags`, `status`, `updated`
Fix: add all required frontmatter fields per the schema in wiki-indexing-theory.md
High-authority pages → ensure all fields present first

### 4. Orphan Reconnection
Pattern: page has zero incoming links
Fix: use `wiki_search` to find related pages, add reciprocal wikilinks

### 5. HITS Hub Page Link Expansion
Pattern: high-hub page (top 5 by HITS) with sparse outbound links
Fix: verify it comprehensively links to relevant authorities
Use judgment — not all hub pages need more links

## Batch Size
- **Stop at 50+ fixes** per run
- **Update batch-progress.md** every 15-20 fixes

## Related
- [[scratchpad/agent-sheets/librarians-assistant/references/quick-reference]]
- [[index]]

- [[quick-reference]]

## Hard Blockers (stop and report to librarian)
- Merge decision (similarity > 0.7)
- New page creation required
- Classification dispute (tag/type conflict)
- Circular reference unresolved
- High-authority page content correction needed
- Page that shouldn't exist