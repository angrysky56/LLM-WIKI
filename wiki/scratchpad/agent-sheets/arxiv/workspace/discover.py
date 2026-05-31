#!/usr/bin/env python3
import urllib.request, urllib.error, xml.etree.ElementTree as ET, time

SEEN_IDS = {
    '2605.30353','2605.30351','2605.30350','2605.30348','2605.30345',
    '2605.30344','2605.30343','2605.30341','2605.30337','2605.30336',
    '2605.30335','2605.30334','2605.30333','2605.30330','2605.30329',
    '2605.30327','2605.30326','2605.30324','2605.30323','2605.30322',
    '2605.30319','2605.30318','2605.30315','2605.30311','2605.30310',
    '2605.30295','2605.30292','2605.30290','2605.30289','2605.30288',
    '2605.30314','2605.30314v1'
}

url = "https://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.SE&sortBy=submittedDate&sortOrder=descending&max_results=100"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=45) as resp:
        root = ET.parse(resp).getroot()
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code}")
    exit(1)

ns = {'a': 'http://www.w3.org/2005/Atom'}
new_papers = []
for entry in root.findall('a:entry', ns):
    aid = entry.find('a:id', ns).text.strip().split('/abs/')[-1]
    if aid not in SEEN_IDS:
        title = entry.find('a:title', ns).text.strip().replace('\n', ' ')
        pub = entry.find('a:published', ns).text[:10]
        summary = entry.find('a:summary', ns).text.strip()[:300].replace('\n', ' ')
        authors = [a.find('a:name', ns).text for a in entry.findall('a:author', ns)][:3]
        cats = [c.get('term') for c in entry.findall('a:category', ns)][:3]
        pdf_url = f"https://arxiv.org/pdf/{aid}"
        new_papers.append({
            'id': aid, 'title': title, 'published': pub,
            'summary': summary, 'authors': authors, 'categories': cats,
            'pdf_url': pdf_url
        })
        print(f"[NEW] {pub} | {aid} | {title[:80]}")
        print(f"      cats={cats} authors={authors}")
        print()

print(f"\nTotal new papers (not in SEEN_IDS): {len(new_papers)}")
