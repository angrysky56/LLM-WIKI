---
name: librarians-assistant
description: "Wiki remediation agent — fixes broken links, orphans, non-reciprocal wikilinks, frontmatter, and tags identified by the Wiki Librarian audit. Runs after librarian at 08:50 AM daily."
trigger: /librarians-assistant
---

# Librarians Assistant

**Loads:** `wiki/scratchpad/agent-sheets/librarians-assistant.md` for full directives
**MCP tools reference:** `wiki/scratchpad/jobs/mcp-tools-reference.md` — all 22 tools documented with args, behaviors, and known issues
**Wiki root:** `/home/ty/Documents/LLM-WIKI`
**Runs after:** Wiki Librarian (`48a3a009a820`) — reads its carryover for context

---

## Bootstrap

1. Read this skill file (you just did)
2. Read your agent sheet: `wiki/scratchpad/agent-sheets/librarians-assistant.md`
3. Read the librarian's carryover: `wiki/scratchpad/jobs/reports/librarian/carryover.md`
4. Read the batch progress: `wiki/scratchpad/jobs/reports/librarian/batch-progress.md` (if it exists)
5. **Verify MCP availability before using your tools — TWO steps:**

```bash
# Step 1: Package import (necessary but NOT sufficient)
~/.venv/project-synapse-mcp/bin/python3 -c "from synapse_mcp.zettelkasten.insight_engine import InsightEngine; print('OK')" 2>/dev/null && echo "PACKAGE OK" || echo "PACKAGE MISSING"
```

This confirms `synapse_mcp` is in the project-synapse-mcp venv — but `InsightEngine` import does NOT guarantee `wiki_lint`, `wiki_cluster_pages`, etc. are registered MCP handlers.

```bash
# Step 2: Make an actual MCP call to verify tools are registered
# Try: debug_test, wiki_lint, or wiki_list_pages
```

If Step 1 succeeds but Step 2 fails (tool not found), MCP server is running but the tool wasn't registered. Use filesystem fallback.

**If MCP is unavailable:** Use direct filesystem fixes instead of MCP tools (see fallback below).
6. Execute per the agent sheet

---

## Your Tools (all via project-synapse MCP)

- `wiki_lint()` — detect remaining broken links, orphans, missing frontmatter
- `wiki_read_page` — read a page to fix it
- `wiki_write_page` — fix frontmatter, add wikilinks, normalize tags
- `wiki_search` — find related pages for orphan linking
- `wiki_cluster_pages()` — find same-cluster pages for cross-linking

---

## MCP Unavailable — Filesystem Fallback

When the MCP availability probe returns UNAVAILABLE, use direct filesystem operations instead:

1. **Broken wikilinks**: grep for `\[\[` patterns, resolve via filesystem read/write
2. **Orphan pages**: analyze wikilink graph with Python script
3. **Frontmatter**: use `grep -l "^---" wiki/**/*.md | xargs python3 -c "..."` for bulk operations
4. **Reciprocal link gaps**: compute wikilink graph, find asymmetric edges, add return links

---

## 10 Remediation Types

### 1. Broken Wikilinks
**Detection:** Wikilink targets (`[[page-slug]]`) that don't exist in the vault.
**Fix:** Create a stub page at the correct path, or normalize the wikilink to an existing page.
**Recovery command:**
```bash
cd ~/Documents/LLM-WIKI && python3 -c "
import re, os

dirs = ['wiki/concepts', 'wiki/entities', 'wiki/synthesis', 'wiki/sources']
all_md = {}
for root, _, files in os.walk('wiki'):
    for f in files:
        if f.endswith('.md'):
            all_md[f[:-3].lower()] = os.path.join(root, f)

broken = []
for d in dirs:
    if not os.path.exists(d): continue
    for root, _, files in os.walk(d):
        for f in files:
            if not f.endswith('.md'): continue
            path = os.path.join(root, f)
            with open(path) as fh: content = fh.read()
            links = re.findall(r'\[\[([^\]|]+)', content)
            for link in links:
                slug = link.strip().lower().replace(' ', '-').replace('/', '-')
                if slug not in all_md:
                    broken.append((path, link))

from collections import Counter
counter = Counter([link for _, link in broken])
for link, count in counter.most_common(20):
    print(f'  {link}: {count} references')
"
```

### 2. Orphan Pages
**Detection:** Pages with zero inbound wikilinks from other wiki content pages.
**Fix:** Search for related content and add wikilinks from or to the orphan.
**Recovery command:**
```bash
cd ~/Documents/LLM-WIKI && python3 wiki/scratchpad/full_audit.py 2>/dev/null | grep -i orphan
# Or via MCP (when available):
# wiki_lint() → parse "orphans" count and page list
```

### 3. Non-Reciprocal Wikilinks
**Detection:** Page A links to B, but B does not link back to A — creates asymmetric link relationships.
**Fix:** Add the missing return wikilink from B to A.
**Recovery command:**
```bash
cd ~/Documents/LLM-WIKI && grep -rl '\[\[target-page\]\]' wiki/concepts/ wiki/entities/ wiki/synthesis/ 2>/dev/null
# Check if reciprocal link already exists:
grep -l '\[\[source-page\]\]' wiki/concepts/target-page.md wiki/entities/target-page.md 2>/dev/null
```

### 4. Missing Frontmatter
**Detection:** Pages that lack required frontmatter fields (`type`, `summary`, `tags`, etc.).
**Fix:** Add the missing fields. Pages without any frontmatter need a complete block added.
**Recovery command:**
```bash
cd ~/Documents/LLM-WIKI && grep -rL '^---' wiki/concepts/ wiki/entities/ wiki/synthesis/ 2>/dev/null | head -20
# Verify which specific fields are missing:
for f in wiki/concepts/*.md; do
  if ! grep -q '^type:' "$f" 2>/dev/null; then
    echo "MISSING type: $f"
  fi
done
```

### 5. Duplicate/Malformed Frontmatter
**Detection:** Pages with two `---` frontmatter blocks concatenated, or fields appearing twice.
**Fix:** Merge into a single canonical frontmatter block, deduplicating fields (last value wins).
**Recovery command:**
```bash
cd ~/Documents/LLM-WIKI && for f in wiki/synthesis/insights/*.md; do
  count=$(grep -c '^---' "$f" 2>/dev/null || echo 0)
  if [ "$count" -gt 2 ]; then
    echo "DUPLICATE FRONTMATTER: $f (count=$count)"
  fi
done
```

### 6. Tag Normalization
**Detection:** Pages with non-standard tags, compound-tag arrays (`[['news', 'geopolitics', ...]]`), or inconsistent tag formatting.
**Fix:** Normalize tags to single-level strings in the frontmatter `tags` array.
**Recovery command:**
```bash
cd ~/Documents/LLM-WIKI && grep -rE '\[\[news.*\]\]' wiki/concepts/ wiki/entities/ wiki/synthesis/ 2>/dev/null | head -10
# Find compound-tag arrays in news/contextual sources:
grep -rn "news.*geopolitics" wiki/sources/ 2>/dev/null | head -5
```

### 7. PDF Path Contamination
**Detection:** PDF files that migrated into the wiki folder from wrong agent workdirs.
**Fix:** Move strays back to `paper-research/`.
**Recovery command:**
```bash
find ~/Documents/LLM-WIKI -name "*.pdf" -type f 2>/dev/null
# Move strays to correct location:
find ~/Documents/LLM-WIKI -name "*.pdf" -exec mv {} ~/Documents/paper-research/ \; 2>/dev/null
```

### 8. Stub Page Verification
**Detection:** Known stubs that should exist but may have been deleted or never created.
**Fix:** Verify existence; create if missing. Never recreate verified stubs.
**Recovery command:**
```bash
# Verify known stubs exist:
for stub in wolfram-physics-project aseke-framework extraction-quality-audit catastrophic-forgetting in-context-learning emergence agentic-oversight institutional-capture geopolitics evaluation agent-onboarding scaling-laws titans reasoning; do
  if [ -f "~/Documents/LLM-WIKI/wiki/concepts/${stub}.md" ]; then
    echo "EXISTS: $stub"
  else
    echo "MISSING: $stub"
  fi
done
```

### 9. Insight Page Dual-Frontmatter
**Detection:** Zettelkasten-generated insight pages with two concatenated frontmatter blocks (minimal auto-generated + full block).
**Fix:** Merge into a single block, deduplicating fields. Verify with `head -10` after cleaning.
**Recovery command:**
```bash
cd ~/Documents/LLM-WIKI && for f in wiki/synthesis/insights/*.md; do
  if grep -q '^---.*---.*---' "$f" 2>/dev/null; then
    echo "CHECK DUAL BLOCK: $f"
  fi
done
# Verify cleaning result:
head -10 ~/Documents/LLM-WIKI/wiki/synthesis/insights/para-knowledge-architecture-cohesion-insight.md
```

### 10. Top Authority Pages — Depth Before Links
**Detection:** Load-bearing concept pages (efhf, maximum-occupancy-principle, project-synapse, edm-framework) that need substantive content, not just wikilinks.
**Fix:** When linking to these pages from elsewhere, add explanatory content in the same paragraph. Don't add bare wikilinks.
**Recovery command:**
```bash
# Audit top authorities for thin content:
for page in efhf maximum-occupancy-principle project-synapse edm-framework; do
  lines=$(wc -l < "~/Documents/LLM-WIKI/wiki/concepts/${page}.md" 2>/dev/null || echo 0)
  echo "LINES: $lines — $page"
done
```

---

## Key Paths

```
Wiki:                        ~/Documents/LLM-WIKI/
Agent sheet:                 ~/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets/librarians-assistant.md
Librarian carryover:         ~/Documents/LLM-WIKI/wiki/scratchpad/jobs/reports/librarian/carryover.md
Batch progress:              ~/Documents/LLM-WIKI/wiki/scratchpad/jobs/reports/librarian/batch-progress.md
Assistant carryover:        ~/Documents/LLM-WIKI/wiki/scratchpad/jobs/reports/librarians-assistant/carryover.md
MCP tools reference:        ~/Documents/LLM-WIKI/wiki/scratchpad/jobs/mcp-tools-reference.md
Full audit script:          ~/Documents/LLM-WIKI/wiki/scratchpad/full_audit.py
Cron toolsets reference:    ~/.hermes/skills/agent-sheets/librarians-assistant/references/cron-toolsets.md
```

---

## Workflow

1. Read carryover from last librarian run — understand what was already fixed and what remains
2. Read batch-progress.md if it exists — know where previous assistant run stopped
3. **Always verify MCP availability first** (see Bootstrap step 5)
4. Run fixes in priority order (from carryover's "What Remains")
5. Write progress every 15-20 fixes to batch-progress.md
6. When done (50+ fixes or hard blocker): update assistant carryover with open items

---

## Known Pitfalls

### CRITICAL: All cron jobs need full `enabled_toolsets`
If any tool is missing from `enabled_toolsets`, the call silently fails and the job shows `last_status: ok` while the work was skipped. See `references/cron-toolsets.md` for the complete toolset table, error → missing-tool mapping, and job ID reference.

### CRITICAL: execute_code is NOT available to cron agents
The "Primary Frontmatter Fix Workflow" section shows `terminal` heredoc as the **fallback** — this pattern is unreliable in cron context (triggers `pending_approval`). Preferred fallback order:
1. **`wiki_write_page`** (MCP) — best for wiki pages, bypasses filesystem
2. **`write_file`** (toolset) — direct overwrite, reliable for targeted fixes
3. **Terminal heredoc** — only if both above are unavailable; risks `pending_approval`

When using `write_file` to fix frontmatter, read the file first with `read_file`, then write corrected content with `write_file`. Prefer `wiki_write_page` (MCP) over filesystem writes wherever possible.

### generate_insights CLI — use correct pattern
The Zettelkasten engine times out at 300s via MCP. For CLI insight generation, use:
```bash
timeout --kill-after=10s 580s uv run python ~/.venvs/project-synapse-mcp/scripts/generate_insights.py --topic general --print --max-runtime 540
```
Exit codes: 0=success, 3=timeout (file may be valid), 1=init failure. Do NOT use `~/.hermes/scripts/generate_insights.sh` — that script does not exist.

### write_file safety
`write_file` OVERWRITES the entire file. Use it only when:
- You have freshly read the full file (not offset-limited)
- You are constructing the content from scratch (e.g., merging duplicate blocks)
- You have verified the current state before overwriting

Do NOT use `write_file` as a substitute for `patch` when fixing small targeted issues — `patch` is safer for surgical edits.

### Template wikilink examples vs. real broken links
Some pages contain intentional template syntax in their documentation/body. These appear as broken links but are NOT real issues:
- `synapse-llm-wiki-operating-guide.md` contains `[[page-slug]]`, `[[slug]]`, `[[Display]]` — these are **template examples** in the Wikilink Rules section. Do NOT create stubs for these.

### Orphan counts differ by method
MCP `wiki_lint()` reports ~155 orphans (Neo4j graph), while `full_audit.py` filesystem scan may report 0 — these are not comparable; use MCP results when available.

### Top authorities need depth, not just links
efhf, maximum-occupancy-principle, project-synapse, edm-framework are load-bearing pages — when linking to them, add substantive content, not just wikilinks.

---

## Known Stub List (verified 2026-05-30 — do not recreate)

`wolfram-physics-project`, `aseke-framework`, `extraction-quality-audit`, `catastrophic-forgetting`, `in-context-learning`, `emergence`, `agentic-oversight`, `institutional-capture`, `geopolitics`, `evaluation`, `agent-onboarding`, `scaling-laws`, `titans`, `reasoning` — all verified existing.

---

## Correct Bulk Duplicate Frontmatter Cleaner

**The `split('\n---\n')` approach FAILS for files missing the closing `---`.** Use this instead:

```python
import re

def fix_frontmatter_missing_closing(path):
    """Fix frontmatter with duplicate fields and NO closing '---' delimiter."""
    with open(path, 'r') as f:
        lines = f.read().split('\n')

    if lines[0] != '---':
        return False, "no opening ---"

    fm_end = -1
    for i in range(1, len(lines)):
        if lines[i].startswith('# ') or (lines[i].strip() and not re.match(r'^[\w-]+:', lines[i])):
            fm_end = i - 1
            break
    while fm_end >= 0 and lines[fm_end].strip() == '':
        fm_end -= 1

    fm_lines = lines[0:fm_end+1]
    body_lines = lines[fm_end+1:]

    fields = {}
    for line in fm_lines[1:]:
        m = re.match(r'^(\w[\w-]*):(.*)', line)
        if m:
            fields[m.group(1)] = line

    order = ['created', 'updated', 'type', 'summary', 'tags', 'sources', 'status', 'confidence']
    new_fm_lines = ['---']
    for key in order:
        if key in fields:
            new_fm_lines.append(fields[key])
    new_fm_lines.append('---')

    with open(path, 'w') as f:
        f.write('\n'.join(new_fm_lines) + '\n' + '\n'.join(body_lines))
    return True, f"cleaned, kept {len(fields)} fields"
```

---

## MCP Status — Correct Understanding

**MCP probe — TWO steps, not one:**

Step 1 (package import):
```bash
~/.venv/project-synapse-mcp/bin/python3 -c "from synapse_mcp.zettelkasten.insight_engine import InsightEngine; print('OK')" 2>/dev/null && echo "PACKAGE OK" || echo "PACKAGE MISSING"
```

Step 2 (tool registration):
After the import succeeds, make an actual MCP call: `debug_test` or `wiki_lint`. If it returns, tools are registered.

**If MCP is down (import fails):** Fall back to filesystem via `python3 wiki/scratchpad/full_audit.py`.

---

## Primary Frontmatter Fix Workflow (MCP Unavailable)

When filling missing `type`/`sources`/`status`/`confidence` on 10+ pages, use batch Python via `terminal` heredoc:

```bash
cd ~/Documents/LLM-WIKI && python3 << 'PYEOF'
import re, os

pages = [
    ("wiki/concepts/page1.md", ["type", "sources", "status", "confidence"]),
    ("wiki/concepts/page2.md", ["sources", "status"]),
]
for path, missing in pages:
    if not os.path.exists(path):
        print(f"SKIP: {path} does not exist")
        continue
    with open(path) as f:
        content = f.read()
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        print(f"NO FM: {path}")
        continue
    fm_text = fm_match.group(1)
    body = content[fm_match.end():]
    updates = {"sources": "[]", "status": "active", "confidence": "0.8"}
    for key, val in updates.items():
        if key not in fm_text and key in missing:
            fm_text += f"\n{key}: {val}"
    with open(path, "w") as f:
        f.write(f"---\n{fm_text}\n---{body}")
    print(f"OK: {os.path.basename(path)}")

print("Done.")
PYEOF
```

---

## Reciprocal Link Pre-Verification

Before creating reciprocal links, check if they already exist:
```bash
grep -l '\[\[target-page\]\]' ~/Documents/LLM-WIKI/wiki/concepts/*.md ~/Documents/LLM-WIKI/wiki/entities/*.md ~/Documents/LLM-WIKI/wiki/synthesis/*.md 2>/dev/null
```

Common pairs that are ALREADY reciprocal (skip creation):
- `efhf.md` ↔ `maximum-occupancy-principle.md`
- `markovian-dev-agency.md` → `hermes-agent.md`
- `hermes_agent.md` → `load-bearing-reasoning.md`

---

## Delivery Rule

- Delivery: origin (Discord thread)
- Report: "Fixed N broken links, resolved N orphans, normalized N pages, added N wikilinks"
- If nothing left to do: `[Librarians-assistant — no open items]`
- Do NOT write a report file — output goes to cron delivery