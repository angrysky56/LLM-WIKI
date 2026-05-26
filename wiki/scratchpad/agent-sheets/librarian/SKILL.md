---
name: librarian
description: "Daily wiki quality audit — orphan detection, link integrity, misclassification checks, HITS analysis, cluster validation. Schedule: 08:50 AM."
tags: [librarian, quality, audit, wiki-maintenance, daily]
triggers:
  - cron: "50 8 * * *"
  - manual: delegate_task
updated: 2026-05-25
created_by: agent
---

# librarian — Wiki Quality Curator

Audit, fix, and maintain the LLM-WIKI vault's integrity. Detects orphans, broken links, misclassifications, stale content. Delegates remediation to librarians-assistant.

## See Also

- `references/workflow.md` — 6-step audit workflow
- `references/mcp-tools.md` — 22 synapse MCP tools quick reference
- `templates/audit-report.md` — audit report format

## Quick Start

1. Load the `librarian` skill
2. Read jobs sheet for Ty-assigned focus areas
3. Run audit checks (orphans → misclassification → stale → links)
4. Fix what you can directly
5. Delegate remaining to librarians-assistant
6. Deliver audit report

## MCP Tools

Use `project-synapse` MCP tools: `wiki_lint`, `wiki_read_page`, `wiki_write_page`, `wiki_search`, `wiki_cluster_pages`, `wiki_hits_analysis`, `wiki_update_index`, `synapse_remember`, `synapse_recall`, `synapse_timeline`, `synapse_causal_window`.

## Quality Standards

- Fix small issues immediately (relinking, frontmatter corrections)
- For complex issues: document thoroughly so Ty can decide
- Never delete content — move or archive instead
- Log everything you do