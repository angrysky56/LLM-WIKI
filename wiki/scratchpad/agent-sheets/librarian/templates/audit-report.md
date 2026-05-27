# Librarian Audit Report — YYYY-MM-DD

## Theory Anchor
This audit follows `wiki/synthesis/wiki-indexing-theory.md` — 6 concrete improvements.
HITS authority scores identify load-bearing nodes. GAAC clustering identifies missing links.

---

## HITS Analysis

### Top Authorities (load-bearing nodes — need richest content)
| Page | Authority Score | Status |
|------|---------------|--------|
| ... | ... | ... |

### Top Hubs (navigation layers — need comprehensive link coverage)
| Page | Hub Score | Link Count | Status |
|------|-----------|------------|--------|
| ... | ... | ... | ... |

---

## GAAC Clustering

### Missing Connections (same cluster, no wikilink)
| Page A | Page B | Cluster | Action |
|--------|---------|---------|--------|
| ... | ... | ... | add reciprocal link |

### Merge Candidates (similarity > 0.7)
| Page A | Page B | Similarity | Recommendation |
|--------|---------|------------|-----------------|
| ... | ... | ... | flag for human judgment |

---

## Tag Taxonomy Compliance

### Non-Preferred Tags Found
| Page | Non-Preferred Tag | USE Instead | Status |
|------|-------------------|-------------|--------|
| ... | ... | ... | fixed / flagged |

---

## Link Integrity

### Reciprocal Link Gaps (A→B exists, B→A missing)
| Page A | Page B | Fix |
|--------|--------|-----|
| ... | ... | add [[A]] to B |

### Orphans (zero incoming links)
| Page | Cluster | Fix |
|------|---------|-----|
| ... | ... | connect to cluster hub |

### Broken Links
| Page | Broken Target | Fix |
|------|--------------|-----|
| ... | ... | create stub / remove link |

---

## Frontmatter Completeness

### High-Authority Pages Missing Fields
| Page | Missing Fields | Priority |
|------|---------------|----------|
| ... | ... | high |

### General Missing Frontmatter
| Page | Missing | Status |
|------|---------|--------|
| ... | ... | fixed / flagged |

---

## Audit Summary
- Pages checked: N
- Orphans: N (fixed: N, flagged: N)
- Non-reciprocal links: N (fixed: N, flagged: N)
- Tag violations: N (fixed: N, flagged: N)
- Frontmatter gaps: N (fixed: N, flagged: N)
- Missing connections found (GAAC): N
- Merge candidates: N

---

## Actions Taken
- [list of fixes applied]

## Flagged Items (need human judgment)
- [items requiring Ty decision]

## Vault Health Score
[1-10 rating with justification based on HITS authority coverage + link reciprocity + tag compliance]