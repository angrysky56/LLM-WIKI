# librarians-assistant — Fix Priority Quick Reference

## Priority Order (execute in this order)

1. **Broken wikilink aliases** → create stub pages
   - Pattern: `[[target-page]]` exists but `target-page.md` doesn't
   - Fix: create minimal stub at `wiki/path/target-page.md`

2. **Orphan pages** → connect to cluster
   - Pattern: page has outgoing links but no incoming links
   - Fix: `wiki_search` for related pages, add reciprocal links

3. **Non-reciprocal links** → add reverse links
   - Pattern: A links to B but B doesn't link to A
   - Fix: add `[[A]]` to B (and vice versa if appropriate)

4. **Frontmatter completions** → fill missing fields
   - Pattern: missing `summary`, `tags`, `status`, `updated`
   - Fix: add all required frontmatter fields

5. **Tag normalization** → standardize per taxonomy
   - Pattern: inconsistent tags (singular vs plural, typos)
   - Fix: map to canonical tags per tag-taxonomy.md

## Batch Size

- **Stop at 50+ fixes** per run
- **Update batch-progress.md** every 15-20 fixes

## Hard Blockers (stop and report)

- Needs content creation beyond scope
- Needs human judgment on classification
- Circular reference that can't be resolved
- Page that genuinely shouldn't exist (flag for librarian)