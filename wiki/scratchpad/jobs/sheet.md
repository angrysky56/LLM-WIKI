---
summary: Updated job status to done for news
updated: 2026-05-22T01:26:02Z
---

---
summary: Jobs sheet with fixed agent-sheet wikilinks
tags: [jobs, task-board, agent-instructions]
updated: 2026-05-22T01:30:00Z
---

# Jobs Sheet — Central Task Board

**Purpose**: Single source of truth for what each agent should be doing. Agents check here on every run for their current instructions, update their status when done, and post summaries to their report folder.

## Format

- **Pending**: Tasks queued for next run
- **In Progress**: Tasks currently being worked
- **Done**: Completed tasks (brief result + link to report)
- **Blocked**: Tasks waiting on something external

## Active Jobs

| Job ID | Job Name | Agent | Status | Last Run | Next Run | Agent Sheet |
|--------|----------|-------|--------|----------|----------|-------------|
| `eaaa6bdc8503` | world-news-daily | news | **done** | 2026-05-25 | 2026-05-26 8AM | [[agent-sheets/news]] |
| `8ea33cfa560a` | Wiki Researcher | researcher | **done** | 2026-06-09 | TBD | [[agent-sheets/researcher]] |
| `297092f3b347` | orcaid-verification-indexer | orcaid | pending | 2026-05-18 | 2026-05-19 9AM | [[agent-sheets/orcaid]] |
| `72599f850df2` | arxiv-top3-weekly | arxiv | **done** | 2026-05-24 | 2026-05-26 8:20AM | [[agent-sheets/arxiv]] |
| `c838e81a1496` | llm-wiki-raw-ingest | ingest | **done** | 2026-05-23 | | [[agent-sheets/ingest]] |
| `6ee16837c47c` | Wiki Librarian | librarian | **done** | 2026-06-03 | N/A | [[agent-sheets/librarian]] |
| `723e76246970` | Wiki Insights Generator | insights | pending | — | 2026-05-24 6AM | [[agent-sheets/insights]] |

## Task Delegation

### Ty → Agents

**Pending Tasks** (not yet assigned):
- [ ] *[Add tasks here]*

**In Progress**:
- [ ] *[Add tasks here]*

**Done**:
- [ ] *[Add completed tasks here]*

### Agent → (reports go in jobs/reports/{agent}/)

| Agent | Report Folder | Last Report |
|-------|--------------|-------------|
| librarian | `jobs/reports/librarian/` | — |
| researcher | `jobs/reports/researcher/` | — |
| orcaid | `jobs/reports/orcaid/` | — |
| arxiv | `jobs/reports/arxiv/` | — |
| news | `jobs/reports/news/` | [[news-2026-05-22-headlines]] |
| ingest | `jobs/reports/ingest/` | — |
| insights | `jobs/reports/insights/` | — |

## Instructions Per Agent

Each agent reads its own sheet on every run. These sheets are the source of truth — not this central sheet.

| Agent | Sheet | Purpose |
|-------|-------|---------|
| librarian | [[agent-sheets/librarian]] | Quality audit, orphan detection, link integrity |
| researcher | [[agent-sheets/researcher]] | Knowledge gap analysis, new topic research |
| orcaid | [[agent-sheets/orcaid]] | Verification sweep, drift detection, self-improve |
| arxiv | [[agent-sheets/arxiv]] | Top 3 paper discovery and ingestion |
| news | [[agent-sheets/news]] | Global news curation and wiki ingestion |
| ingest | [[agent-sheets/ingest]] | raw→wiki pipeline, file processing |
| insights | [[agent-sheets/insights]] | Zettelkasten insight generation and wiki integration |

**Each agent sheet contains:**
1. Read the agent sheet (STEP 0)
2. Read the central jobs sheet (STEP 1)
3. Execute assigned tasks
4. Write report to `jobs/reports/{agent}/`
5. Update this sheet's status column
6. Update own carryover in `jobs/reports/{agent}/carryover.md`
