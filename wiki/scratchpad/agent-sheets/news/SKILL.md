---
name: news
description: "Daily global news curator — RSS discovery, significance filtering, wiki article ingestion, deliver headlines report. Schedule: 08:00 AM."
tags: [news, global-news, rss, daily]
triggers:
  - cron: "0 8 * * *"
  - manual: delegate_task
updated: 2026-05-25
created_by: agent
---

# news — Global News Curator

Scan global news via RSS, identify 3-5 significant stories, ingest to wiki, deliver headlines report. **Use RSS for discovery — NOT wiki search.**

## See Also

- `references/workflow.md` — RSS discovery workflow
- `references/rss-queries.md` — topic query list
- `templates/news-article.md` — article summary format
- `templates/headlines-report.md` — daily report format

## Quick Start

1. Load the `news` skill
2. Read jobs sheet for Ty-flagged regions/topics
3. Query RSS feeds (NOT wiki search) — 5-7 topic queries
4. Check article index for duplicates (carryover + recent headlines)
5. Select 3-5 globally significant stories
6. Ingest to wiki as `wiki/sources/articles/{slug}.md`
7. Deliver headlines report

## RSS Topic Queries

```
geopolitics+may+2026
AI+tech+policy+regulation+may+2026
science+breakthrough+may+2026
economy+trade+tariff+may+2026
AI+science+math+breakthrough+2026
```

## Quality Standards

- Ingest for significance, not volume
- A single globally consequential story beats 10 local ones
- Write with context — don't just headline dump
- Cross-link to existing wiki threads
- Skip if already indexed (check carryover article index)