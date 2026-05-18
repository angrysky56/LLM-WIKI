---
summary: Jobs system index
tags: [jobs, index]
updated: 2026-05-18T07:06:27Z
created: 2026-05-18T07:06:27Z
---

---
created: 2026-05-18
type: jobs
---

# Jobs System

Central task board where Ty assigns work and agents report back.

## Structure

```
scratchpad/jobs/
├── sheet.md          ← central task board (THIS FILE)
├── reports/          ← agent report submissions
│   ├── librarian/
│   ├── researcher/
│   ├── orcaid/
│   ├── arxiv/
│   ├── news/
│   └── ingest/
└── archives/         ← old completed tasks
```

## How It Works

1. **Ty** edits `sheet.md` to add tasks, set focus areas, flag priorities
2. **Agent** reads `sheet.md` at start of every run for instructions
3. **Agent** posts reports to `jobs/reports/{agent}/` with date-stamped filenames
4. **Agent** updates the Status column in `sheet.md` after each run
5. **Ty** reviews reports, delegates new work, archives done items

## Report Naming

```
{agent}-{YYYY-MM-DD}-{topic}.md
```

Examples:
- `librarian-2026-05-18-quality-audit.md`
- `arxiv-2026-05-18-top3-papers.md`
- `news-2026-05-18-global-headlines.md`
