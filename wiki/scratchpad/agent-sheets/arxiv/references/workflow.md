# arxiv — 6-Phase Research Workflow

## PHASE 1 — Discover Papers

```python
import urllib.request, xml.etree.ElementTree as ET

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

## PHASE 2 — Select Top 3

Selection criteria:
- Novel contribution (not incremental on prior work)
- Relevance to active wiki research threads
- Technical depth sufficient to be useful

## PHASE 3 — Download PDFs via curl (NOT MCP)

```bash
curl -s -L "https://arxiv.org/pdf/{id}" -o /home/ty/Documents/paper-research/{id}.pdf --max-time 60 -w "%{http_code}" &
curl -s -L "https://arxiv.org/pdf/{id}" -o /home/ty/Documents/paper-research/{id}.pdf --max-time 60 -w "%{http_code}" &
curl -s -L "https://arxiv.org/pdf/{id}" -o /home/ty/Documents/paper-research/{id}.pdf --max-time 60 -w "%{http_code}" &
wait
```

**Expected: "200" for each = success.**

## PHASE 4 — Delegate Research to Subagents

Use `delegate_task` with `tasks=[]` — one subagent per paper. Each subagent writes to `wiki/sources/papers/{slug}.md` and appends to `papers-YYYY-MM-DD-researched.md`.

## PHASE 5 — Assemble Final Report

Read all three research summaries from `papers-YYYY-MM-DD-researched.md`. Write final report to `wiki/scratchpad/jobs/reports/arxiv/arxiv-YYYY-MM-DD-top-papers.md`.

## PHASE 6 — Update Carryover

Write to `wiki/scratchpad/agent-sheets/arxiv/carryover.md`:
- This cycle's selection theme
- Trending topics worth deeper coverage next cycle
- Any papers worth revisiting

## Critical Paths

| Path | Value |
|------|-------|
| Wiki root | `/home/ty/Documents/LLM-WIKI` |
| Paper storage | `/home/ty/Documents/paper-research/` |
| Daily reports | `wiki/scratchpad/jobs/reports/arxiv/` |
| Carryover | `wiki/scratchpad/agent-sheets/arxiv/carryover.md` |