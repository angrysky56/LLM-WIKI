---
summary: Session start — corrections, cron audit, todo
tags: [scratchpad, session-start]
updated: 2026-05-18T06:47:07Z
---

---
created: 2026-05-18T00:50:00Z
type: scratchpad
---

## 2026-05-18 [00:50] — meta

**Session start.** Hindsight memory system was just installed. This is the first real entry.

Ty corrected several things from old memory that was being injected:

1. **GoodRobot is SHUT DOWN** — not active. The entity page says it's active but it's outdated.
2. **OrCAID config** — was wrong. Should be `minimax/anthropic` (not just minimax). The prefix issue confused me before but apparently it's since been straightened out. Actual working config is `LLM_MODEL=minimax/MiniMax-M2.7` + `LLM_BASE_URL=https://api.minimax.io/v1` — but Ty says it's set right with minimax/anthropic. Need to verify.
3. **Graph/DB quality issues** — from librarian reports are mostly fixed now. The 68% orphan rate and Person misclassification pandemic are substantially improved as of 2026-05-13 audit.

**Ty wants:**
- Scratchpad folder in wiki — DONE (wiki/scratchpad/index.md)
- My own notebook/journal there
- A skill for scratchpad management
- Review cron jobs and suggest improvements

## 2026-05-18 [01:10] — cron audit

**Cron jobs reviewed (6 total):**

| Job | Name | Schedule | Skills | Status |
|-----|------|----------|--------|--------|
| `6ee16837c47c` | Wiki Librarian (weekly) | Mon 6AM | none | last: 2026-05-11, ok |
| `8ea33cfa560a` | Wiki Researcher (biweekly) | Mon/Thu 9AM | arxiv, project-synapse | last: 2026-05-14, ok |
| `297092f3b347` | orcaid-verification-indexer | every 6h | orcaid-verification-bridge, delegation-verification | last: 2026-05-18 00:01, ok |
| `72599f850df2` | arxiv-top3-weekly | Daily 10AM | arxiv, project-synapse | last: 2026-05-17 12:18, ok |
| `eaaa6bdc8503` | world-news-daily | Daily 9AM | project-synapse | last: 2026-05-17 13:08, ok |
| `c838e81a1496` | llm-wiki-raw-ingest | Daily 11AM | project-synapse | last: 2026-05-17 11:59, ok |

**Issues I see:**

1. **Wiki Librarian** — weekly but last ran 2026-05-11, next run is 2026-05-18. That's 7 days ago. If it ran ok last time, probably fine — just noting it.

2. **Wiki Researcher** — uses `gemini-2.5-flash` via openrouter explicitly. The others use `null` model (inherit from config). This is the only job with explicit provider override — could be a problem if openrouter pricing changes or the model gets deprecated. Consider standardizing.

3. **Overlap: arxiv-top3-weekly (10AM) + llm-wiki-raw-ingest (11AM)** — back-to-back. The raw-ingest might be pulling in papers discovered by arxiv-top3? If there's a data dependency, these should be sequential (arxiv first, then ingest). Currently they run independently.

4. **world-news-daily (9AM) + Wiki Researcher (9AM)** — same hour. Both use `project-synapse`. Potential resource contention? They run at the exact same time.

5. **orcID verification-indexer** — every 6 hours. This is a passive scanner. Could be improved by also triggering OrCAID self-improve if drift rates are high? Currently it only scans already-written logs.

6. **No delivery optimization** — all 6 jobs deliver to `origin` (current Discord channel). If Ty is away or频道 is busy, outputs pile up. Consider:
   - Batching low-priority jobs (librarian, news) to `local` and summarize weekly
   - Or routing to a dedicated `#agent-reports` channel if one exists

## 2026-05-18 [01:20] — todo

Follow up on:
- [ ] Verify OrCAID actual current config (minimax/anthropic vs what I have in memory)
- [ ] GoodRobot entity page needs `status: shut_down` update
- [ ] Write scratchpad skill
- [ ] Check if there's a `#agent-reports` or similar channel for batching cron outputs
