---
summary: Central task board for agent job dispatch
tags: [jobs, task-board, agent-instructions]
updated: 2026-05-18T14:00:00Z
created: 2026-05-18T07:06:09Z
---

---
created: 2026-05-18
type: jobs
---

# Jobs Sheet — Central Task Board

**Purpose**: Single source of truth for what each agent should be doing. Agents check here on every run for their current instructions, update their status when done, and post summaries to their report folder.

## Format

- **Pending**: Tasks queued for next run
- **In Progress**: Tasks currently being worked
- **Done**: Completed tasks (brief result + link to report)
- **Blocked**: Tasks waiting on something external

## Active Jobs

| Job ID | Job Name | Agent | Status | Last Run | Next Run | Notes |
|--------|----------|-------|--------|----------|----------|-------|
| `6ee16837c47c` | Wiki Librarian | librarian | pending | 2026-05-11 | 2026-05-18 6AM | Weekly quality audit |
| `8ea33cfa560a` | Wiki Researcher | researcher | pending | 2026-05-14 | 2026-05-18 9AM | Mon/Thu discovery |
| `297092f3b347` | orcaid-verification-indexer | orcaid | pending | 2026-05-18 | 2026-05-18 12PM | Every 6h |
| `72599f850df2` | arxiv-top3-weekly | arxiv | pending | 2026-05-17 | 2026-05-18 10AM | Top 3 papers |
| `eaaa6bdc8503` | world-news-daily | news | done | 2026-05-18 | 2026-05-19 9AM | Daily global news |
| `c838e81a1496` | llm-wiki-raw-ingest | ingest | pending | 2026-05-17 | 2026-05-18 11AM | Raw→wiki pipeline |

## Task Delegation

### Ty → Agents

**Pending Tasks** (not yet assigned):
- [ ] *[Add tasks here]*

**In Progress**:
- [ ] *[Add tasks here]*

**Done**:
- [ ] *[Add completed tasks here]*

### Agent → Ty (reports go in jobs/reports/{agent}/)

| Agent | Report Folder | Last Report |
|-------|--------------|-------------|
| librarian | `jobs/reports/librarian/` | — |
| researcher | `jobs/reports/researcher/` | — |
| orcaid | `jobs/reports/orcaid/` | — |
| arxiv | `jobs/reports/arxiv/` | — |
| news | `jobs/reports/news/` | — |
| ingest | `jobs/reports/ingest/` | — |

## Instructions Per Agent

### librarian
1. Read this sheet to get current task focus
2. Run quality audit (orphan rate, misclassifications, entity health)
3. Write report to `jobs/reports/librarian/audit-YYYY-MM-DD.md`
4. Update your status above when done

### researcher
1. Read this sheet for discovery focus areas
2. Run knowledge gap analysis and new topic research
3. Write report to `jobs/reports/researcher/discovery-YYYY-MM-DD.md`
4. Update your status above when done

### orcaid
1. Read this sheet — check if any drift correction tasks are queued
2. Run verification index sweep
3. If drift_rate > threshold: flag here and optionally trigger self_improve
4. Write report to `jobs/reports/orcaid/verification-YYYY-MM-DD.md`
5. Update your status above when done

### arxiv
1. Read this sheet for any paper focus areas Ty has specified
2. Search for top 3 relevant papers (or use default: newest ML/AI papers)
3. Ingest summaries to wiki
4. Write report to `jobs/reports/arxiv/papers-YYYY-MM-DD.md`
5. Update your status above when done

### news
1. Read this sheet — check if Ty has flagged any specific regions/topics
2. Run global news scan
3. Ingest significant stories to wiki
4. Write report to `jobs/reports/news/headlines-YYYY-MM-DD.md`
5. Update your status above when done

### ingest
1. Read this sheet — check if any priority sources need ingestion
2. Run raw→wiki ingest pipeline
3. Write report to `jobs/reports/ingest/ingest-YYYY-MM-DD.md`
4. Update your status above when done
