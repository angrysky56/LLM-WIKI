---
name: librarians-assistant
description: "Wiki remediation subagent — fix open issues from librarian audit in batches, report progress, carry open items forward. Schedule: after librarian."
tags: [wiki-remediation, wiki-maintenance, daily]
triggers:
  - cron: "50 8 * * *"
  - manual: delegate_task
updated: 2026-05-25
created_by: agent
---

# librarians-assistant — Wiki Remediation Subagent

Fix the open wiki health issues identified by the librarian audit. Work in batches, report progress, carry open items to the next cycle. **Read the librarian's carryover for your task list — priorities come from there, not hardcoded instructions.**

## See Also

- `references/workflow.md` — 6-step fix workflow
- `references/quick-reference.md` — fix priority order

## Quick Start

1. Load the `librarians-assistant` skill
2. Read librarian carryover → your task list
3. Read batch-progress.md → resume where last run stopped
4. Execute fixes in priority order (stop at 50+ or hard blocker)
5. Update batch-progress.md every 15-20 fixes
6. Deliver brief Discord report

## Fix Priority Order

1. Broken wikilink aliases → create stub pages
2. Orphan pages → connect to cluster
3. Non-reciprocal links → add reverse links
4. Frontmatter completions → add summary/tags/status
5. Tag normalization → standardize tags per taxonomy

## Quality Standards

- Fix incrementally — don't try to fix everything in one run
- Never delete content — move or archive instead
- If a link target genuinely doesn't exist: create a stub, don't remove the wikilink
- Log everything in batch-progress.md