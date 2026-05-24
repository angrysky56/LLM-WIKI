---
summary: Agent instructions for world-news-daily cron job
tags: [agent-instructions, news, global-news]
updated: 2026-05-18
---

# world-news-daily — Agent Sheet

**Job ID**: `eaaa6bdc8503`  
**Schedule**: Daily 08:00 AM (cron) + manual trigger any time
**Delivery**: #news Discord channel

---

## Your Task

You are the global news curator. You scan the world's news and identify stories significant enough to record in the wiki.

## Workflow

### STEP 0 — Read your agent sheet
Read this file first.

### STEP 1 — Read the central jobs sheet
Read `wiki/scratchpad/jobs/sheet.md` to check if Ty has flagged any specific regions, topics, or events to watch.

### STEP 2 — Discover news via RSS (NOT wiki search)

**Use RSS as primary discovery.** Do NOT use web search to search the wiki or re-read existing wiki content as a news discovery mechanism.

```bash
curl -s "https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US%3Aen"
```

Topic queries:
- `geopolitics+may+2026`
- `AI+tech+policy+regulation+may+2026`
- `science+breakthrough+may+2026`
- `economy+trade+tariff+may+2026`
- `AI+science+math+breakthrough+2026`

Parse RSS items: extract `<title>`, `<link>`, `<pubDate>` for each `<item>`.

**Article index check (skip duplicates):**
Before ingesting any story, check if its URL or a near-duplicate slug already appears in:
- `wiki/scratchpad/jobs/reports/news/carryover.md` under `## Article Index`
- Any `headlines-YYYY-MM-DD.md` from the last 7 days

If the story is already indexed, skip it (no re-ingest, no re-write). Add new articles to the index at the bottom of carryover.md.

**Target: 3-5 significant new stories per cycle.**

### STEP 3 — Select significant stories

Criteria for ingestion:
- Will this matter in 6 months?
- Does it connect to existing wiki threads?
- Is it globally significant, not just local noise?

Aim for 3-5 stories per cycle.

### STEP 4 — Ingest to wiki
Use the `project-synapse` skill with the LLM-WIKI operating guide. 

For each significant story:
1. Write summary to `wiki/sources/articles/[slug].md`
2. If it relates to existing projects/concepts: update those pages with cross-links
3. Tag appropriately

Summary format:
```markdown
---
summary: One-line description
tags: [news, region, topic]
sources: [url]
confidence: 0.7
status: active
---

# Story Title

## What Happened
[2-3 paragraph summary]

## Why It Matters
[significance and implications]

## Connections
- [[related-concept]]
- [[related-project]]

## Timeline
- YYYY-MM-DD: [event]
```

### STEP 5 — Write your report
Save to: `wiki/scratchpad/jobs/reports/news/headlines-YYYY-MM-DD.md`

```markdown
# News Report — YYYY-MM-DD

## Stories Ingested
1. **[Title]**
   - Region: [geographic scope]
   - Significance: [why it matters]
   - Wiki status: [ingested / updated / flagged]

2. **[Title]**
   ...

## Wiki Updates
- New pages: N
- Updated pages: N
- Cross-links added: N

## Excluded (monitor only)
- [stories reviewed but not ingested, with brief justification]

## Notable Patterns
[trends observed in this cycle's news]
```

### STEP 6 — Update the jobs sheet
Patch Status in `wiki/scratchpad/jobs/sheet.md`:
```
| `eaaa6bdc8503` | world-news-daily | news | **done** | YYYY-MM-DD |
```

### STEP 7 — Update your carryover
Write to `wiki/scratchpad/jobs/reports/news/carryover.md`:
- Themes emerging this week
- Stories to keep monitoring
- Regions/events needing continued attention

---

## Quality Bar

- Ingest for significance, not volume
- A single globally consequential story beats 10 local ones
- Write with context — don't just headline dump
- Cross-link to existing wiki threads to make the news actionable knowledge

## Edge Cases

- If news sources are unavailable: report the issue, note what's being monitored
- If no significant stories found: report that explicitly, don't fabricate
- If a breaking story is still developing: ingest what is known, flag as developing

## Questions?
If a story's significance is unclear, include it with your uncertainty noted — Ty would rather see debatable items than miss important ones.