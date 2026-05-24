# arxiv-researcher — Better Arxiv Cron Agent

**Job ID**: `72599f850df2`  
**Schedule**: Daily 08:20 AM (cron) + manual trigger any time
**Delivery**: origin (Discord home channel)

---


The agent uses:
1. **curl fallback** for PDF download (bypasses MCP 429s)
2. **delegate_task subagents** for parallel paper research (one per paper)
3. **PyMuPDF** for PDF text extraction (MCP `read_paper` only works for server-downloaded files)
4. **wiki_write_page** for wiki ingestion (not filesystem writes)

---

## Workflow

### PHASE 1 — Discover Papers

```python
# discover_papers.py — use Python urllib, NOT curl | python3
import urllib.request, xml.etree.ElementTree as ET, json

def search_arxiv(query, max_results=10, categories="cs.AI+OR+cs.LG+OR+cs.CL"):
    url = f"https://export.arxiv.org/api/query?search_query={query}+AND+({categories})&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    with urllib.request.urlopen(url) as resp:
        root = ET.parse(resp).getroot()
    ns = {"a": "http://www.w3.org/2005/Atom"}
    papers = []
    for entry in root.findall("a:entry", ns):
        papers.append({
            "id": entry.find("a:id", ns).text.strip().split("/abs/")[-1],
            "title": entry.find("a:title", ns).text.strip().replace("\n", " "),
            "authors": [a.find("a:name", ns).text for a in entry.findall("a:author", ns)][:3],
            "published": entry.find("a:published", ns).text[:10],
            "summary": entry.find("a:summary", ns).text.strip()[:300],
            "categories": [c.get("term") for c in entry.findall("a:category", ns)][:5],
            "pdf_url": f"https://arxiv.org/pdf/{entry.find('a:id', ns).text.strip().split('/abs/')[-1]}",
        })
    return papers
```

Call this from a `terminal()` tool with a `.py` script, not a pipe.

### PHASE 2 — Select Top 3

Selection criteria:
- Novel contribution (not incremental on prior work)
- Relevance to active wiki research threads (check recent carryover)
- Technical depth sufficient to be useful

For each selected paper, write a **research brief**:
```markdown
## Selection {N}: {arxiv_id}
- Title: {title}
- Why selected: {2-3 sentence justification connecting to wiki threads}
- Wiki connections: efhf, mop-explorer, agentic-research (or similar)
```

### PHASE 3 — Download PDFs via curl (bypass MCP rate limits)

```bash
# Download 3 papers in parallel — curl is NOT rate-limited like MCP
# ALWAYS use absolute paths — workdir changes break relative paths
curl -s -L "https://arxiv.org/pdf/{id}" \
  -o /home/ty/Documents/paper-research/{id}.pdf \
  --max-time 60 -w "%{http_code}" &
curl -s -L "https://arxiv.org/pdf/{id}" \
  -o /home/ty/Documents/paper-research/{id}.pdf \
  --max-time 60 -w "%{http_code}" &
curl -s -L "https://arxiv.org/pdf/{id}" \
  -o /home/ty/Documents/paper-research/{id}.pdf \
  --max-time 60 -w "%{http_code}" &
wait
# Expected: "200" for each = success
```

Store in: `/home/ty/Documents/paper-research/{arxiv_id}v{version}.pdf`

### PHASE 4 — Delegate Research to Subagents

Use `delegate_task` with `tasks=[]` (batch mode) — one subagent per paper.
Each subagent gets its own isolated context and terminal session.

**Subagent task template:**
```
Research the paper at /home/ty/Documents/paper-research/{arxiv_id}v{version}.pdf

OUTPUT FORMAT — produce a wiki source page at:
/home/ty/Documents/LLM-WIKI/wiki/sources/papers/{slug}.md

Include:
- Paper metadata (title, authors, arxiv ID, published date, categories)
- Executive summary (what problem does it solve? what's the key innovation?)
- Technical approach (key methods, architecture, algorithms)
- Key results (metrics, benchmarks, comparisons to prior work)
- Relevance to EFHF/AGEM/MOP research 
  (connect to: efhf, mop-explorer, agentic-research, verifier-graph, mcp-logic, 
   graphrag, maximum-occupancy-principle, sheaf-consistency-enforcer)
- Key quotes from the paper (use > blockquote format)
- Structural insights (what does this reveal about the design space?)

Also append to /home/ty/Documents/LLM-WIKI/wiki/scratchpad/jobs/reports/arxiv/papers-YYYY-MM-DD-researched.md:
---
### {arxiv_id} — {title-slug}
[single paragraph summary + one key finding]
---

Context to read before writing:
- wiki/synthesis/efhf-mcp-configuration.md — EFHF architecture context
- wiki/concepts/agentic-research.md — agentic research thread
- wiki/concepts/reward-modeling.md — reward/cost assignment concepts
- wiki/scratchpad/jobs/reports/arxiv/carryover.md — recent selection themes
```

### PHASE 5 — Assemble Final Report

Read all three research summaries from `papers-YYYY-MM-DD-researched.md`.
Write final report to `wiki/scratchpad/jobs/reports/arxiv/arxiv-YYYY-MM-DD-top-papers.md`.

```markdown
# arxiv Report — YYYY-MM-DD

## Papers Processed

### 1. **{title}** (arxiv:{id})
- Why selected: {justification}
- Status: ingested → wiki/sources/papers/{slug}.md
- Wiki connections: {list}

### 2. ...
### 3. ...

## Wiki Updates
- New pages: 3 ({slug1}.md, {slug2}.md, {slug3}.md)
- Tags added: paper, arxiv, {thematic tags}

## Notes
- All 3 papers share theme: {common thread if any}
- MCP download hit rate limit → used curl fallback
- arXiv rate limit events: {N}
```

### PHASE 6 — Update Jobs Sheet + Carryover

1. Patch `wiki/scratchpad/jobs/sheet.md` status to `**done**`
2. Write `wiki/scratchpad/jobs/reports/arxiv/carryover.md` with:
   - This cycle's selection theme
   - Trending topics worth deeper coverage next cycle
   - Any papers worth revisiting

---

## Critical Patterns

### Pattern 1: MCP fails → curl fallback immediately
```
if mcp_download → 429 or timeout:
    curl -s -L "https://arxiv.org/pdf/{id}" -o {storage_path}/{id}.pdf
```
Don't retry MCP twice before falling back. One failure = switch to curl.

### Pattern 2: Subagent verification
Subagents self-report completion but may be wrong. Verify:
- Wiki source page exists: `search_files(target="files", path="{WIKI}/wiki/sources/papers", pattern="{slug}")`
- Report section appended: `grep -c "{arxiv_id}" papers-YYYY-MM-DD-researched.md`
If verification fails, re-run that paper's research.

### Pattern 3: PDF extraction via PyMuPDF
```python
import pymupdf
doc = pymupdf.open("/home/ty/Documents/paper-research/2605.18703v1.pdf")
text = "\n".join(page.get_text() for page in doc)
# Save for subagent context if needed
with open("/home/ty/Documents/paper-research/2605.18703.txt", "w") as f:
    f.write(text)
```

### Pattern 4: Wiki path in cron context
```python
import os
WIKI = os.environ.get("WIKI_PATH", "/home/ty/Documents/LLM-WIKI")
PAPER_STORAGE = "/home/ty/Documents/paper-research"
```

---

## Error Handling

| Failure | Action |
|---------|--------|
| arXiv API down | Deliver partial results; note in report |
| MCP rate limit | Fall back to curl immediately |
| PDF extraction fails | Use arxiv abstract + first page only |
| Subagent fails | Re-run that paper's research inline |
| Wiki write fails | Write to filesystem, ingest next cycle |

---

## Quality Standards

- Select for **significance**, not recency alone
- Wiki pages must cross-link to existing concepts (no orphans)
- Research summaries capture the "why should I care" not just method
- Report notes any rate limit events for audit trail