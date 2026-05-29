---
name: librarian-agent
description: "Wiki Librarian agent — audits vault structural quality, delegates fix work to librarians-assistant subagent for iterative remediation. Reports what was done, not what needs doing."
trigger: /librarian-agent
---

# Librarian Agent

**Wiki root:** `/home/ty/Documents/LLM-WIKI/`
**Agent sheet:** `wiki/scratchpad/agent-sheets/librarian.md`
**Jobs sheet:** `wiki/scratchpad/jobs/sheet.md`
**Reports dir:** `wiki/scratchpad/jobs/reports/librarian/`
**Carryover:** `wiki/scratchpad/jobs/reports/librarian/carryover.md`

---

## Full Scope

The librarian agent maintains wiki vault integrity across 10 checklist areas:

1. **Broken links** — `wiki_lint()` detects alias-based `[[titans]]`, `[[reasoning]]`, `[[agent-sheets/*]]` style wikilinks and non-existent targets; fix or create stubs
2. **Orphan pages** — pages with zero inbound wikilinks; connect from related pages (MCP-based detection: ~155 orphans as of 2026-05-21; differs from filesystem scan which may report 0)
3. **Frontmatter audit** — 8 required fields: `created`, `updated`, `type`, `summary`, `tags`, `sources`, `status`, `confidence` (~326/341 pages missing fields as of 2026-05-23)
4. **Quality audit** — HITS authority/hub scoring, GAAC clustering coherence, stale content detection
5. **Link reciprocality** — A→B without B→A; ~110 non-reciprocal pairs found 2026-05-21
6. **Tag taxonomy** — canonical tag taxonomy at `wiki/concepts/tag-taxonomy.md`; normalize tag variants to canonical form
7. **Stub pages** — create minimal stubs for high-frequency missing concepts linked but non-existent
8. **Mere mention review** — pages referencing a concept but not wikilinking it; flag for connection
9. **PDF path contamination** — PDFs from arxiv-agent landing in wiki by mistake; move to `/home/ty/Documents/paper-research/`
10. **Insight generation** — `generate_insights(confidence_threshold=0.7)` — **WARNING**: times out after 300s; if it fails, skip and note in carryover

---

## Bootstrap (in order)

1. Read this skill file
2. Read agent sheet: `wiki/scratchpad/agent-sheets/librarian.md`
3. Read jobs sheet: `wiki/scratchpad/jobs/sheet.md`
4. Read carryover: `wiki/scratchpad/jobs/reports/librarian/carryover.md` (if exists)
5. Execute task per agent sheet directives

---

## MCP Tools — Availability Check Required

**All 22 MCP tools documented at:** `wiki/scratchpad/jobs/mcp-tools-reference.md`

**CRITICAL:** `project-synapse` MCP server may NOT be connected in cron/scheduled environments. If unavailable, these tools will fail silently or throw module-not-found errors: `wiki_lint`, `wiki_cluster_pages`, `wiki_hits_analysis`, `wiki_update_index`, `generate_insights`.

### MCP Availability Probe — TWO steps, not one

**Step 1** (package import — necessary but NOT sufficient):
```bash
/home/ty/Repositories/ai_workspace/project-synapse-mcp/.venv/bin/python3 -c "from synapse_mcp.zettelkasten.insight_engine import InsightEngine; print('OK')" 2>/dev/null && echo "PACKAGE OK" || echo "PACKAGE MISSING"
```

**Step 2** (tool registration — the actual test): After the import succeeds, make an actual MCP call: `debug_test` or `wiki_lint`. A clean `InsightEngine` import does NOT guarantee `wiki_lint`, `wiki_cluster_pages`, `wiki_hits_analysis` are available.

### If MCP Unavailable

Fall back to filesystem analysis using `wiki/scratchpad/full_audit.py`:
```bash
cd /home/ty/Documents/LLM-WIKI && python3 wiki/scratchpad/full_audit.py
```

If MCP is available but `wiki_lint`/`cluster_pages`/`hits` timeout — these tools work but can be slow in cron context. Use filesystem `full_audit.py` as fallback **only for that cycle**. Do NOT set a persistent "MCP down" flag — retry MCP tools in the next cycle.

### Timeout Behavior (normal, not a failure)

| Tool | Timeout | Expected Behavior |
|------|---------|-------------------|
| `wiki_lint()` | ~5s | Fast |
| `wiki_cluster_pages()` | ~10s | Fast |
| `wiki_hits_analysis()` | ~10s | Fast |
| `wiki_update_index()` | ~30s | Medium |
| `generate_insights()` | **300s** | Expected timeout — skip and note in carryover |
| `wiki_fetch_url()` | ~15s | Medium; may 403 on some sites |

**TIMEOUT = NOT "MCP UNAVAILABLE"** — A tool timing out means the engine is slow, not that MCP is down. Only fall back to `full_audit.py` if a tool throws an exception or returns a clear connection error.

---

## The 10-Task Librarian Checklist

Run ALL of these each cycle:

1. **Tag consistency** — collect all tags, cluster equivalents, normalize to canonical form using `wiki/concepts/tag-taxonomy.md`
2. **HITS authority/hub scoring** — `wiki_hits_analysis()` → top authorities need deepest content; verified deep pages: `efhf.md`, `maximum-occupancy-principle.md`, `project-synapse.md`, `edm-framework.md`
3. **Reciprocal wikilinks** — A→B without B→A is incomplete; ~110 non-reciprocal pairs found 2026-05-21
4. **GAAC semantic clustering** — `wiki_cluster_pages()` → topic clusters, same-cluster missing links, merge candidates (sim > 0.7)
5. **Conceptual index health** — `concept-index.md` last updated 2026-04-28; may need manual refresh
6. **Mere mention review** — pages that reference a concept but don't wikilink it; flag for connection
7. **Frontmatter completeness** — all 8 required fields; confidence < 0.7 → add `## Caveats` section
8. **Broken wikilinks repair** — `wiki_lint()` output shows ~338 broken links; fix or remove (never ignore `log.md` links)
9. **Orphan detection** — pages with zero inbound wikilinks; MCP-based detection differs from filesystem scan — **do not compare numbers across methods**
10. **Insight generation trigger** — `generate_insights(confidence_threshold=0.7)`; if it fails, skip and note in carryover; do not retry same cycle

---

## Three-Phase Execution

### PHASE 1: AUDIT

**First — Verify MCP availability:**
```bash
/home/ty/Repositories/ai_workspace/project-synapse-mcp/.venv/bin/python3 -c "from synapse_mcp.zettelkasten.insight_engine import InsightEngine; print('OK')" 2>/dev/null && echo "MCP OK" || echo "MCP UNAVAILABLE"
```
- If MCP UNAVAILABLE: fall back to `python3 wiki/scratchpad/full_audit.py` for the entire audit
- If MCP OK: proceed with MCP tools

Run the full checklist silently. Collect results. Do NOT write a report of findings. Move to Phase 2.

### PHASE 2: DELEGATE

Spawn a `librarians-assistant` subagent using `delegate_task`:

```json
{
  "goal": "You are the librarians-assistant for the LLM-WIKI at /home/ty/Documents/LLM-WIKI/. Your job is to fix what the librarian audit found. Work iteratively — do NOT try to fix everything at once. Priority order: 1. Fix broken wikilink aliases: [[titans]], [[reasoning]], [[agent-sheets/*]] → create stub pages or remove the references 2. Add inbound links to orphan pages (pages with zero incoming wikilinks) from related pages 3. Fix non-reciprocal wikilinks (A→B without B→A) — add return links 4. Fill missing frontmatter on pages flagged by wiki_lint 5. Normalize tag variants to canonical form using tag-taxonomy.md. Work in small batches. After each batch of 10-20 fixes, report briefly what you did. Use the project-synapse MCP tools: wiki_lint, wiki_read_page, wiki_write_page, wiki_search. If you cannot fix something (needs judgment, content gap, etc.), skip it and note it. Stop when: (a) you've made 50+ fixes, or (b) you hit a hard blocker, or (c) the librarian tells you to stop. Start by reading wiki/scratchpad/jobs/reports/librarian/carryover.md (if it exists) to understand what was already worked on.",
  "role": "leaf",
  "toolsets": ["terminal", "file", "web", "search"]
}
```

**Fallback if `delegate_task` is not available:** Execute fixes directly using the same priority order above. Use `python3 wiki/scratchpad/full_audit.py` to re-check progress after each batch of ~20 fixes.

Wait for the subagent to complete.

### PHASE 3: REPORT

Write a brief delivery message that:
- States what was done (not what needs doing)
- Lists concrete actions: "Fixed 47 broken links, resolved 23 orphans, normalized tags on 12 pages"
- Flags anything that wasn't fixable and why
- Updates `carryover.md` with open items for next cycle

**Delivery rule:**
- All checks pass → `[SILENT]`
- Fixes made → brief summary of what was fixed, delivered to origin
- Do NOT write a standalone report file — output goes to cron delivery

**Carryover.md structure (hard cap: ~512 tokens):**
```markdown
## Established
- Key metrics: page count, orphan count, broken link count, non-reciprocal pairs
- Top authorities (by HITS score) — load-bearing pages needing depth
- Top hubs — pages that link to many authorities

## Open
- Issues not fixed this cycle (with reason)
- Tool/skill failures (e.g., insight generation timeout)

## Heading
- Priority fixes for next cycle
```

---

## Lint Suppression Rule

Always ignore links in `log.md` — structural false positives (they contain dynamically generated wikilink references, not intentional cross-references).

---

## Key Paths

```
Wiki:                   /home/ty/Documents/LLM-WIKI/
Wiki content root:      /home/ty/Documents/LLM-WIKI/wiki/
Agent sheet:            wiki/scratchpad/agent-sheets/librarian.md
Jobs sheet:             wiki/scratchpad/jobs/sheet.md
Reports:                wiki/scratchpad/jobs/reports/librarian/
Carryover:              wiki/scratchpad/jobs/reports/librarian/carryover.md
Fallback audit script:  wiki/scratchpad/full_audit.py
MCP tools reference:    wiki/scratchpad/jobs/mcp-tools-reference.md
Tag taxonomy:           wiki/concepts/tag-taxonomy.md
Audit output schema:    references/full-audit-schema.md
Stub fix history:       references/stub-fix-log.md
```

---

## Required Frontmatter Fields (8 standard)

`created`, `updated`, `type`, `summary`, `tags`, `sources`, `status`, `confidence`

- Pages with `confidence < 0.7` → add `## Caveats` section
- `type` values: `concept`, `entity`, `agent`, `skill`, `source`, `project`, `article`, `paper`, `log`
- Frontmatter debt is the #1 issue across the vault — ~326/341 pages missing required fields as of 2026-05-23
- **Field ordering:** canonical order is: `created`, `updated`, `type`, `summary`, `tags`, `sources`, `status`, `confidence`. Pages with out-of-order fields should be corrected.
- **Entity project pages** (`wiki/entities/projects/*.md`) use `type: entity`, not `type: project`

---

## Stub Page Template

```markdown
---
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept
summary: "[STUB] One-line description of the concept"
tags: [topic, stubs]
sources: []
status: stub
confidence: 0.3
---

# Concept Name

*Stub page — needs real content*

## Connections

- [[related-existing-page]]
```

Stub pages go in: `wiki/concepts/` for concepts, `wiki/entities/projects/` for projects, `wiki/synthesis/` for synthesis topics.

**Slug resolution:** Wikilinks are case-insensitive and space-insensitive: `[[Agentic Design Picker]]` → `wiki/concepts/agentic-design-picker.md`. Slash in wikilink → parent dir stub at `wiki/sources/repositories/`.

---

## Broken Link Fix Order

1. Fix alias references (`[[titans]]`, `[[reasoning]]`, `[[agent-sheets/*]]`) — create stubs or remove
2. Remove tag-array wikilinks from news pages — `[['news', 'geopolitics', ...]]` style arrays (noise, not real links)
3. Create stubs for real concepts that are linked but missing
4. Orphan pages — add links from related pages
5. Missing frontmatter — fill required fields
6. Confidence < 0.7 → add `## Caveats` section
7. Always ignore `log.md` links

**Gap list resolved 2026-05-30:**
- `isabelle-hol` → `wiki/entities/tools/isabelle-hol.md`
- `engineering-internal-awareness` → `wiki/concepts/engineering-internal-awareness.md`
- `word-cloud-communication` → `wiki/concepts/word-cloud-communication.md`
- `domain-onboarding-standards` → `wiki/concepts/domain-onboarding-standards.md`
- `hermes-agent-skill` → appears in log.md only (dynamic, ignore)

**Already EXISTS (do not recreate):** `wolfram-physics-project`, `aseke-framework`, `extraction-quality-audit`, `catastrophic-forgetting`, `in-context-learning`, `emergence`, `agentic-oversight`, `institutional-capture`, `geopolitics`, `evaluation`, `agent-onboarding`, `scaling-laws`, `titans`, `reasoning`, `initialization`, `criticality`, `working-memory`, `lcguard`, `epistemic-energy`, `bounded-rationality`, `panksepp-emotional-systems`, `superposition`

---

## Batch Frontmatter Fixes — Python Script Pattern

When fixing 10+ pages' frontmatter, use an inline Python script via `terminal()` rather than individual `patch` calls:

```python
from pathlib import Path
import re

WIKI = Path('/home/ty/Documents/LLM-WIKI/wiki')
TODAY = '2026-06-08'

pages = [
    'wiki/concepts/page1.md',
    'wiki/concepts/page2.md',
]

for p in pages:
    path = Path(p)
    if not path.exists():
        continue
    content = path.read_text()
    m = re.match(r'^(---\n)(.*?)(\n---)', content, re.DOTALL)
    if not m:
        continue
    fm = m.group(2)
    if 'type:' not in fm:
        new_fm = 'type: concept\n' + fm
        new_content = m.group(1) + new_fm + m.group(3) + content[m.end():]
        path.write_text(new_content)
        print(f'FIXED: {p}')
```

---

## Common Fix Patterns

| Pattern | Fix | Example |
|---------|-----|---------|
| `[[Display Text]]` where Display Text ≠ slug | Fix alias to use slug | `[[Zettelkasten Engine]]` → `[[zettelkasten-engine]]` |
| `[[goodrobot-revenue-model]]` | Use existing page path | → `[[revenue-model]]` (in same dir) or full relative |
| Double frontmatter blocks | Remove first (duplicate) block | News pages often have both tag-list and proper frontmatter |
| Tag-list wikilinks `[['news', ...]]` | Remove — noise, not real links | Fix in news source pages only |
| `[[onboarding-standards]]` missing | Use `[[agent-onboarding]]` or create stub | Check `research/index.md` |
| Cross-stub references cascade | Fix one end of each pair; stubs pointing to stubs is acceptable as interim | |

---

## Broken Cron — Job Fires But Never Executes

**Symptom:** `cronjob run` returns `{"success": true}`, but `last_run_at` stays `null`, no session file appears in `~/.hermes/sessions/`, no output in `~/.hermes/cron/output/`. Job is `enabled=true`, `state=scheduled` — no API errors, scheduler just doesn't fire it.

**This is a scheduler bug, not a config error.** Deleting and recreating the cron does NOT fix it.

**Workaround — use `delegate_task` instead:**
```python
delegate_task(
  context="...",
  goal="[full task context from the agent sheet]",
  toolsets=["terminal", "file", "web", "search", "skills"]
)
```

**After using delegate_task as bypass:** Session file goes to `~/.hermes/sessions/` as `session_cron_<job_id>_<date>_<time>.json`. Output appears in `~/.hermes/cron/output/<job_id>/`.

---

## CRITICAL: enabled_toolsets Must Include `patch`

All cron jobs for wiki agents MUST include `patch` in `enabled_toolsets`. Without it, any `patch` call during the cron run silently fails with:
```
{"error": "Background review denied non-whitelisted tool: patch. Only memory/skill tools are allowed."}
```

The job shows `last_status: ok` but the fix was skipped.

**Required toolsets for wiki agent cron jobs:**
- Base: `terminal`, `file`, `web`, `skills`, `search`
- **Always add:** `patch` (for updating carryover, batch-progress, frontmatter)
- Add `session_search` if the agent reads prior session transcripts

**Example cron update:**
```
cronjob update --job_id <id> --enabled_toolsets '["terminal","file","web","skills","search","patch"]'
```