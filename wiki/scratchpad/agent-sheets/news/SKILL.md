---
name: news
description: "Daily global news curator — RSS discovery, significance filtering, clippings archive + synthesis wiki delivery, deliver headlines report. Schedule: 07:30 AM."
tags: [news, global-news, rss, daily]
triggers:
  - cron: "30 7 * * *"
  - manual: delegate_task
updated: 2026-05-27
created_by: agent
---

# news — Global News Curator

Scan global news via RSS, identify 3-5 significant stories, ingest to wiki, deliver headlines report. **Use RSS for discovery — NOT wiki search.**

## Tool Protocol

**Use `terminal()` with `cat` / `ls` for ALL file reads in cron context.** `read_file` is not available for background/cron execution. Use MCP tools for wiki operations.

## Quick Start

1. Read carryover: `cat wiki/scratchpad/agent-sheets/news/carryover.md`
2. Read jobs sheet for Ty-flagged regions/topics
3. Query RSS feeds (NOT wiki search) — 5-7 topic queries
4. Check article index for duplicates (carryover + recent headlines)
5. Select 3-5 globally significant stories
6. Process each story (Steps 1-4 below)
7. Deliver headlines report
8. **Update carryover** (REQUIRED — Final Step)

## Workflow

### Step 1 — RSS Discovery

Use web_search for news discovery. Build queries dynamically — do NOT hardcode month/year:

```
# Topic queries — use current context, not hardcoded dates
geopolitics conflict
science breakthrough discovery
economy trade energy
AI breakthrough
AI policy regulation
climate transition
health pandemic epidemic
```

**Dynamic dates**: Use `date +%B+%Y` in terminal to get current month if you need time context.

### Step 2 — Significance Filtering

From RSS results, select **3-5 stories** using these criteria:

| Criterion | Weight |
|-----------|--------|
| Global consequence (affects >1 country or domain) | High |
| Novelty (genuinely new development, not rehash) | High |
| Relevance to Ty's interests (AI, science, geopolitics) | Medium |
| Source quality (established outlets, official reports) | Medium |

**Skip**: Local crime, celebrity news, sports scores, opinion pieces, clickbait.

### Step 3 — Ingest Each Story

For each selected story:

```
1. CHECK for duplicates:
   synapse_recall(query="{headline or topic}")
   → Also check carryover "## Stories Covered" section
   → If already covered, skip

2. WRITE clipping:
   wiki_write_page(path="Clippings/articles/{year}/{slug}.md", content=...)
   Frontmatter:
   
   created: {today}
   updated: {today}
   type: source
   summary: "{headline}"
   tags: [news, {topic}]
   sources: {url}
   status: active
   

3. WRITE synthesis (if story is consequential enough):
   wiki_write_page(path="wiki/synthesis/{slug}.md", content=...)
   → Include: what happened, why it matters, connections to existing wiki topics
   → Cross-link to relevant concept/entity pages

4. RECORD to episodic memory:
   synapse_remember(content="News {today}: {headline} — {one-line significance}")
```

### Step 4 — Deliver Headlines Report

Write report to: `wiki/scratchpad/jobs/reports/news/headlines-{YYYY-MM-DD}.md`

Format your delivery response as:

```
**World News — {YYYY-MM-DD}**

**{N} stories** | significance threshold: global/multi-domain

1. **{Headline}** — {1-2 sentence summary}
   → [[wiki-page]] | Source: {outlet}

2. **{Headline}** — ...
```

If no stories meet the significance threshold, respond `[SILENT]`.

### Final Step — Update Carryover (REQUIRED)

Write to `wiki/scratchpad/agent-sheets/news/carryover.md`:

```yaml
---
created: {original date}
updated: {today's date}
type: carryover
summary: "{N} stories: {brief titles}"
tags: [news, carryover]
---
```

Include:
- **What Was Done**: Stories covered (title + slug + significance rationale)
- **What Remains**: `- [ ]` checklist (ongoing threads to follow, developing stories)
- **Kanban Status**: Items already surfaced
- **Article Index**: Recent slugs for dedup (last 7 days)

## Critical Paths

- **Clippings**: `Clippings/articles/{year}/{slug}.md`
- **Synthesis**: `wiki/synthesis/{slug}.md`
- **Reports**: `wiki/scratchpad/jobs/reports/news/headlines-YYYY-MM-DD.md`
- **Carryover**: `wiki/scratchpad/agent-sheets/news/carryover.md`

## MCP Tools

| Tool | Purpose |
|------|---------|
| `synapse_recall` | Check for duplicate stories |
| `synapse_remember` | Record headlines to episodic memory |
| `wiki_write_page` | Create clipping and synthesis pages |
| `wiki_search` | Find related wiki pages for cross-linking (NOT for discovery) |
| `wiki_update_index` | Refresh index after new pages |

## Fallback Patterns

- **RSS/web search unavailable**: Note in carryover, `[SILENT]`
- **MCP unavailable**: Deliver headlines as text-only report, skip wiki pages, note in carryover
- **No significant stories**: `[SILENT]` (this is fine — don't force volume)

## Quality Standards

- Ingest for significance, not volume
- A single globally consequential story beats 10 local ones
- Write with context — don't just headline dump
- Cross-link to existing wiki threads when creating synthesis
- Skip if already indexed (check carryover article index)
- **Never hardcode dates in RSS queries** — use dynamic date resolution