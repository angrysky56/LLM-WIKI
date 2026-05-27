# news — RSS Discovery Workflow

## STEP 1 — Read the Central Jobs Sheet (Optional)

Read `wiki/scratchpad/jobs/sheet.md` to check if Ty has flagged any priority regions, topics, or events. The overseer owns this sheet — do NOT write to it. If the sheet is stale or empty, proceed with default topic queries.

## STEP 1 — Discover News via RSS

**Use RSS as primary discovery. Do NOT use web search to search the wiki or re-read existing wiki content as a news discovery mechanism.**

### Topic Queries

```bash
curl -s "https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US%3Aen"
```

**Topic list:**
- `geopolitics+may+2026`
- `AI+tech+policy+regulation+may+2026`
- `science+breakthrough+may+2026`
- `economy+trade+tariff+may+2026`
- `AI+science+math+breakthrough+2026`

Parse RSS items: extract `<title>`, `<link>`, `<pubDate>` for each `<item>`.

## STEP 2 — Check Article Index (Skip Duplicates)

Before ingesting any story, check if its URL or a near-duplicate slug already appears in:
- `wiki/scratchpad/agent-sheets/news/carryover.md` under `## Article Index`
- Any `headlines-YYYY-MM-DD.md` from the last 7 days

If the story is already indexed, skip it (no re-ingest, no re-write). Add new articles to the index at the bottom of carryover.md.

**Target: 3-5 significant new stories per cycle.**

## STEP 3 — Select Significant Stories

Criteria for ingestion:
- Will this matter in 6 months?
- Does it connect to existing wiki threads?
- Is it globally significant, not just local noise?

Aim for 3-5 stories per cycle.

## STEP 4 — Write to Clippings + Synthesis

For each significant story:
1. Write raw clipping with frontmatter to `Clippings/news/YYYY/[slug].md`
2. Write synthesis to `wiki/synthesis/news/[slug].md`
3. If it relates to existing projects/concepts: update those pages with cross-links
4. Tag appropriately

## STEP 5 — Write Your Report

Save to: `wiki/synthesis/news/headlines-YYYY-MM-DD.md`

## STEP 6 — Update Jobs Sheet (OVERSEER WRITES THIS — DO NOT TOUCH)

The **overseer** owns the central sheet. Do NOT patch or modify `wiki/scratchpad/jobs/sheet.md`. Update your own carryover (STEP 7) instead.

## STEP 7 — Update Your Carryover

Write to `wiki/scratchpad/agent-sheets/news/carryover.md`:
- Themes emerging this week
- Stories to keep monitoring
- Regions/events needing continued attention
- New article URLs added to index