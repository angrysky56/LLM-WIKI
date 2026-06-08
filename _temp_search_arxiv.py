#!/usr/bin/env python3
"""Search arXiv for agentic systems papers."""
import urllib.request, urllib.parse, xml.etree.ElementTree as ET, json, sys, time

def search_arxiv(query, max_results=8):
    url = f'http://export.arxiv.org/api/query?search_query={urllib.parse.quote(query)}&sortBy=submittedDate&sortOrder=descending&max_results={max_results}'
    req = urllib.request.Request(url, headers={'User-Agent': 'HermesResearch/1.0'})
    resp = urllib.request.urlopen(req, timeout=30)
    return resp.read().decode('utf-8')

queries = [
    ('agent tool use', 'cat:cs.AI+AND+all:agent+AND+all:(tool+use+OR+function+calling+OR+code+generation)'),
    ('web agents', 'cat:cs.AI+AND+all:(web+agent+OR+browser+agent+OR+computer+use)'),
    ('agent systems LG', 'cat:cs.LG+AND+all:agent+AND+all:(tool+use+OR+function+calling+OR+web+agent)'),
    ('agent systems CL', 'cat:cs.CL+AND+all:agent+AND+all:(tool+use+OR+function+calling+OR+web+agent)'),
    ('code agents', 'cat:cs.LG+AND+all:(code+generation+OR+code+agent+OR+software+engineering+agent)'),
]

all_results = []
ns = {'a': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}

for label, q in queries:
    print(f'[{label}] Querying...', file=sys.stderr)
    try:
        xml_data = search_arxiv(q, max_results=8)
        root = ET.fromstring(xml_data)
        entries = root.findall('a:entry', ns)
        print(f'  Found {len(entries)} entries', file=sys.stderr)
        for entry in entries:
            id_elem = entry.find('a:id', ns)
            title = entry.find('a:title', ns)
            summary_el = entry.find('a:summary', ns)
            published = entry.find('a:published', ns)
            authors = [a.find('a:name', ns).text for a in entry.findall('a:author', ns)]
            cats_primary = [c.get('term') for c in entry.findall('arxiv:primary_category', ns)]
            
            pid = id_elem.text.strip().split('/')[-1] if id_elem is not None else '?'
            t = title.text.strip().replace('\n', ' ') if title is not None else '?'
            s = summary_el.text.strip().replace('\n', ' ') if summary_el is not None else '?'
            
            all_results.append({
                'id': pid,
                'title': t,
                'published': published.text.strip() if published is not None else '?',
                'authors': authors[:5],
                'categories': cats_primary,
                'summary': s[:400],
                'query_label': label,
            })
    except Exception as e:
        print(f'  FAILED: {e}', file=sys.stderr)
    time.sleep(5)

print(json.dumps(all_results, indent=2))