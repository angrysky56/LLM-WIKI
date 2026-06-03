import urllib.request, xml.etree.ElementTree as ET, json, time, sys

def search_arxiv(query, max_results=15, categories="cs.AI"):
    url = f"https://export.arxiv.org/api/query?search_query={query}+AND+({categories})&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (LLM-WIKI arxiv-agent)"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    root = ET.fromstring(data)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    papers = []
    for entry in root.findall("a:entry", ns):
        papers.append({
            "id": entry.find("a:id", ns).text.strip().split("/abs/")[-1],
            "title": entry.find("a:title", ns).text.strip().replace("\n", " "),
            "authors": [a.find("a:name", ns).text for a in entry.findall("a:author", ns)][:4],
            "published": entry.find("a:published", ns).text[:10],
            "summary": entry.find("a:summary", ns).text.strip()[:400],
            "categories": [c.get("term") for c in entry.findall("a:category", ns)][:5],
        })
    return papers

queries = [
    "agentic system reliability safety",
    "LLM agent evaluation benchmark",
    "skill acquisition tool use",
    "monitoring oversight",
    "trace process verification",
]

results = {}
for q in queries:
    for attempt in range(4):
        try:
            results[q] = search_arxiv(q)
            print(f"OK {q}: {len(results[q])} results", file=sys.stderr)
            break
        except Exception as e:
            wait = 30 * (attempt + 1)
            print(f"FAIL {q} attempt {attempt+1}: {e}; waiting {wait}s", file=sys.stderr)
            time.sleep(wait)
    time.sleep(5)

# Filter to last 3 days (2026-06-01 onwards)
import datetime
cutoff = datetime.date(2026, 6, 1)
filtered = {}
for q, ps in results.items():
    filtered[q] = [p for p in ps if datetime.date.fromisoformat(p["published"]) >= cutoff]
    print(f"FILTERED {q}: {len(filtered[q])} from {cutoff}", file=sys.stderr)

with open("/home/ty/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets/arxiv/workspace/phase1_raw.json", "w") as f:
    json.dump(filtered, f, indent=2)
print(json.dumps(filtered, indent=2)[:2000])
