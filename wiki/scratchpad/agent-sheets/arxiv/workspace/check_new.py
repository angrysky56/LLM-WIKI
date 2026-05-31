#!/usr/bin/env python3
"""Check for papers newer than 2026-05-28 submission date."""
import urllib.request, urllib.error, xml.etree.ElementTree as ET

def fetch_latest(url, label):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            root = ET.parse(resp).getroot()
    except urllib.error.HTTPError as e:
        print(f"HTTPError {e.code} for {label}")
        return []
    ns = {'a': 'http://www.w3.org/2005/Atom'}
    results = []
    for entry in root.findall('a:entry', ns):
        aid = entry.find('a:id', ns).text.strip().split('/abs/')[-1]
        title = entry.find('a:title', ns).text.strip().replace('\n', ' ')
        pub = entry.find('a:published', ns).text[:10]
        cats = [c.get('term') for c in entry.findall('a:category', ns)][:2]
        authors = [a.find('a:name', ns).text for a in entry.findall('a:author', ns)][:2]
        results.append((pub, aid, title, cats, authors))
    return results

# Check start=0 and start=50 to see what dates are in the feed
for start in [0, 50]:
    url = f"https://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.SE&sortBy=submittedDate&sortOrder=descending&max_results=50&start={start}"
    print(f"\n=== start={start} ===")
    papers = fetch_latest(url, f"start={start}")
    dates = set()
    for pub, aid, title, cats, authors in papers:
        dates.add(pub)
    print(f"Unique submission dates in this slice: {sorted(dates)}")
    if start == 0:
        print("Newest 5 papers:")
        for pub, aid, title, cats, authors in papers[:5]:
            print(f"  {pub} | {aid} | {title[:70]}")

# Also check cs.SE specifically for any missed papers
print("\n=== cs.SE separate query ===")
url = "https://export.arxiv.org/api/query?search_query=cat:cs.SE&sortBy=submittedDate&sortOrder=descending&max_results=20"
papers = fetch_latest(url, "cs.SE")
dates = set(pub for pub, *_ in papers)
print(f"cs.SE dates: {sorted(dates)}")
for pub, aid, title, cats, authors in papers[:5]:
    print(f"  {pub} | {aid} | {title[:70]}")
