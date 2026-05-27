#!/usr/bin/env python3
import urllib.request, urllib.parse, xml.etree.ElementTree as ET, sys, json

ids = ["2605.27345","2605.27333","2605.27322","2605.27315","2605.27313","2605.27311","2605.27298","2605.27296"]
url = "https://export.arxiv.org/api/query?id_list=" + ",".join(ids)

with urllib.request.urlopen(url, timeout=30) as resp:
    root = ET.parse(resp).getroot()

ns = {'a': 'http://www.w3.org/2005/Atom'}
papers = []
for entry in root.findall('a:entry', ns):
    eid = entry.find('a:id', ns).text.strip().split('/abs/')[-1]
    title = entry.find('a:title', ns).text.strip().replace('\n', ' ')
    summary = entry.find('a:summary', ns).text.strip()[:300]
    authors = [a.find('a:name', ns).text for a in entry.findall('a:author', ns)][:3]
    cats = [c.get('term') for c in entry.findall('a:category', ns)][:4]
    papers.append({
        'id': eid,
        'title': title,
        'authors': authors,
        'summary': summary,
        'categories': cats
    })

print(json.dumps(papers, indent=2))