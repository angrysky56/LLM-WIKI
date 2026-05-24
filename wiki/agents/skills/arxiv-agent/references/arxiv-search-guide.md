# arXiv Search Guide

Complete reference for arXiv paper discovery, download, and metadata extraction.

---

## Discovery Methods

### Primary: arXiv API (export.arxiv.org)

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

**Rate limits:**
- Max 4 requests/second
- 429 → exponential backoff: 1s, 2s, 4s, 8s
- Batch boolean queries over separate calls

### Fallback: HTML List Pages (API down or rate-limited)

```bash
# Get recent paper IDs for a category — ALWAYS works
curl -s --max-time 10 "https://arxiv.org/list/cs.AI/recent" | \
  grep -o '[0-9]\{4\}\.[0-9]\{5\}' | sort -u | head -10

# Also works for other categories
curl -s --max-time 10 "https://arxiv.org/list/cs.LG/recent"
curl -s --max-time 10 "https://arxiv.org/list/cs.CL/recent"
```

**Flow when API is down:**
1. Scrape `arxiv.org/list/cs.AI/recent` for IDs
2. Attempt API metadata fetch with backoff (1s, 2s, 4s, 8s)
3. If API still fails → download PDF directly via curl, extract title/author from PDF first page via PyMuPDF
4. Queue any papers that couldn't have metadata resolved for next cycle's API retry

---

## arXiv API Query Construction

**Field-specific searches:**
- `ti:"exact phrase"` — search titles only
- `au:"author name"` — search by author
- `abs:"keyword"` — search abstracts only

**Combining terms:**
```bash
# Exact phrase match
"multi-agent systems"

# OR for broader coverage
"AI agents" OR "software agents" OR "intelligent agents"

# AND for narrow focus
"deep learning" AND "transformer"

# Exclude with ANDNOT
"machine learning" ANDNOT "survey"
```

**Category filtering (highly recommended):**
- `cs.AI` — Artificial Intelligence
- `cs.MA` — Multi-Agent Systems
- `cs.LG` — Machine Learning
- `cs.CL` — Computation and Language (NLP)
- `cs.CV` — Computer Vision
- `cs.RO` — Robotics
- `cs.HC` — Human-Computer Interaction
- `cs.CR` — Cryptography and Security

**Date filtering (YYYY-MM-DD):**
- `date_to:"2015-12-31"` — for foundational/classic work
- `date_from:"2023-01-01"` — for recent developments
- Both together: `date_from:"2023-01-01" AND date_to:"2024-12-31"`

**Example queries:**
```bash
# RL papers by title
ti:"reinforcement learning" AND (cat:cs.LG OR cat:cs.AI)

# Hinton's deep learning work
au:"Hinton" AND "deep learning" AND cat:cs.LG

# Exclude surveys, focus on multi-agent
"multi-agent" ANDNOT "survey" AND cat:cs.MA

# Attention + transformer in NLP
abs:"transformer" AND ti:"attention" AND cat:cs.CL
```

---

## PDF Download

### curl (Primary — bypasses MCP rate limits)

```bash
# ALWAYS use absolute paths
curl -s -L "https://arxiv.org/pdf/{id}" \
  -o /home/ty/Documents/paper-research/{id}.pdf \
  --max-time 60 -w "%{http_code}"

# Parallel downloads (3 papers)
curl -s -L "https://arxiv.org/pdf/2501.12345" \
  -o /home/ty/Documents/paper-research/2501.12345.pdf \
  --max-time 60 -w "%{http_code}" &
curl -s -L "https://arxiv.org/pdf/2502.23456" \
  -o /home/ty/Documents/paper-research/2502.23456.pdf \
  --max-time 60 -w "%{http_code}" &
curl -s -L "https://arxiv.org/pdf/2503.34567" \
  -o /home/ty/Documents/paper-research/2503.34567.pdf \
  --max-time 60 -w "%{http_code}" &
wait
# Expected: "200" for each = success
```

**Storage path:** `/home/ty/Documents/paper-research/{arxiv_id}v{version}.pdf`

### Verification (ALWAYS verify after download)

```bash
ls -la /home/ty/Documents/paper-research/{id}.pdf
# Confirm file exists at the correct absolute path, not in current workdir
```

---

## PDF Text Extraction (PyMuPDF)

```bash
pip install pymupdf  # install once; may not be in environment
```

```python
import pymupdf

doc = pymupdf.open(f"/home/ty/Documents/paper-research/{arxiv_id}.pdf")
text = "\n".join(page.get_text() for page in doc)
# First 2 pages are usually enough for title, authors, abstract

# Save extracted text for subagent context
with open(f"/home/ty/Documents/paper-research/{arxiv_id}.txt", "w") as f:
    f.write(text)
```

**When to use:** MCP `read_paper` only works for server-downloaded files. For curl-downloaded PDFs, use PyMuPDF directly.

---

## MCP Fallback Pattern

```python
if mcp_download → 429 or timeout:
    # Immediate switch to curl
    curl -s -L "https://arxiv.org/pdf/{id}" -o {storage_path}/{id}.pdf
```

**One failure = switch to curl. Do NOT retry MCP twice.**

---

## Duplicate Batch Detection

arXiv batches are dated by submission date, not processing date. A Friday-UTC batch processed Saturday may appear again Monday.

**Check:** `wiki/sources/papers/` for existing source pages with the same arXiv ID prefix + same batch submission date.

If found: skip re-ingesting — update jobs sheet and carryover only.

---

## Key URLs

| Purpose | URL |
|---------|-----|
| API query | `https://export.arxiv.org/api/query?search_query=...` |
| PDF direct | `https://arxiv.org/pdf/{id}` |
| Abstract page | `https://arxiv.org/abs/{id}` |
| Category list (recent) | `https://arxiv.org/list/cs.AI/recent` |
| Category list (by date) | `https://arxiv.org/list/cs.AI/2505` (year-month) |