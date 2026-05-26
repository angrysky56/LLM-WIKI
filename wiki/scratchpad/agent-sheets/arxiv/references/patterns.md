# arxiv — Critical Patterns

## Pattern 1: MCP Fails → curl Fallback Immediately

```
if mcp_download → 429 or timeout:
    curl -s -L "https://arxiv.org/pdf/{id}" -o {storage_path}/{id}.pdf
```
Don't retry MCP twice before falling back. One failure = switch to curl.

## Pattern 2: Subagent Verification

Subagents self-report completion but may be wrong. Verify:
- Wiki source page exists: `search_files(target="files", path="{WIKI}/wiki/sources/papers", pattern="{slug}")`
- Report section appended: `grep -c "{arxiv_id}" papers-YYYY-MM-DD-researched.md`

If verification fails, re-run that paper's research.

## Pattern 3: PDF Extraction via PyMuPDF

```python
import pymupdf
doc = pymupdf.open("/home/ty/Documents/paper-research/2605.18703v1.pdf")
text = "\n".join(page.get_text() for page in doc)
with open("/home/ty/Documents/paper-research/2605.18703.txt", "w") as f:
    f.write(text)
```

## Pattern 4: Wiki Path in Cron Context

```python
import os
WIKI = os.environ.get("WIKI_PATH", "/home/ty/Documents/LLM-WIKI")
PAPER_STORAGE = "/home/ty/Documents/paper-research"
```

## Error Handling

| Failure | Action |
|---------|--------|
| arXiv API down | Deliver partial results; note in report |
| MCP rate limit | Fall back to curl immediately |
| PDF extraction fails | Use arxiv abstract + first page only |
| Subagent fails | Re-run that paper's research inline |
| Wiki write fails | Write to filesystem, ingest next cycle |