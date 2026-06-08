#!/usr/bin/env python3
"""arXiv search + download + extract for agentic systems theme."""
import urllib.request, urllib.parse, xml.etree.ElementTree as ET, json, sys, time, os, re

# Configuration
OUTDIR = "/tmp/arxiv_agentic"
os.makedirs(OUTDIR, exist_ok=True)

def search_arxiv(query, max_results=10):
    url = f'http://export.arxiv.org/api/query?search_query={urllib.parse.quote(query)}&sortBy=submittedDate&sortOrder=descending&max_results={max_results}'
    req = urllib.request.Request(url, headers={'User-Agent': 'HermesResearch/1.0'})
    resp = urllib.request.urlopen(req, timeout=30)
    return resp.read().decode('utf-8')

def parse_arxiv_xml(xml_data):
    ns = {'a': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
    root = ET.fromstring(xml_data)
    entries = root.findall('a:entry', ns)
    results = []
    for entry in entries:
        id_el = entry.find('a:id', ns)
        title_el = entry.find('a:title', ns)
        summary_el = entry.find('a:summary', ns)
        published_el = entry.find('a:published', ns)
        authors = [a.find('a:name', ns).text or '' for a in entry.findall('a:author', ns)]
        cats = [c.get('term','') for c in entry.findall('arxiv:primary_category', ns)]
        
        paper_id = id_el.text.strip().split('/')[-1] if id_el is not None and id_el.text else ''
        title = title_el.text.strip().replace('\n',' ').strip() if title_el is not None and title_el.text else ''
        summary = summary_el.text.strip().replace('\n',' ').strip() if summary_el is not None and summary_el.text else ''
        published = published_el.text.strip()[:10] if published_el is not None and published_el.text else ''
        
        results.append({
            'id': paper_id,
            'title': title,
            'published': published,
            'authors': authors[:6],
            'categories': cats,
            'summary': summary[:500],
        })
    return results

# Step 1: Search across multiple queries
queries = [
    ('agent-tool-use', 'cat:cs.AI+AND+all:agent+AND+all:(tool+use+OR+function+calling+OR+code+generation)'),
    ('web-agents', 'cat:cs.AI+AND+all:(web+agent+OR+browser+agent+OR+computer+use)'),
    ('code-agents', 'cat:cs.LG+AND+all:(code+generation+OR+code+agent+OR+software+engineering+agent)'),
    ('agent-systems', 'cat:cs.LG+AND+all:agent+AND+all:(tool+use+OR+function+calling+OR+web+agent)'),
    ('llm-as-agent', 'cat:cs.CL+AND+all:agent+AND+all:(tool+use+OR+function+calling+OR+web+agent)'),
]

all_papers = []
for label, q in queries:
    try:
        xml_data = search_arxiv(q, max_results=8)
        papers = parse_arxiv_xml(xml_data)
        for p in papers:
            p['query_source'] = label
        all_papers.extend(papers)
        time.sleep(5)
    except Exception as e:
        pass

# Deduplicate by id
seen = set()
unique = []
for p in all_papers:
    pid = p['id']
    if pid and pid not in seen:
        seen.add(pid)
        unique.append(p)

# Score papers by relevance to agentic systems theme
# Prefer: tool use, function calling, code gen, web agents, computer use, software engineering
scored = []
for p in unique:
    t = p['title'].lower()
    s = p['summary'].lower()
    score = 0
    for kw in ['tool use', 'function calling', 'tool calling', 'code generation', 'code agent',
               'web agent', 'browser agent', 'computer use', 'software engineering',
               'agent benchmark', 'agent evaluation', 'agent framework', 'multi-agent',
               'tool learning', 'agentic', 'action space', 'api calling']:
        if kw in t: score += 5
        if kw in s: score += 2
    # Penalize papers that are about agents in other domains (e.g., biology agents)
    for kw in ['drug', 'chemistry', 'biology', 'medical', 'clinical', 'protein', 'molecule']:
        if kw in t: score -= 3
    p['relevance_score'] = score
    scored.append(p)

# Sort by relevance then recency
scored.sort(key=lambda p: (-p['relevance_score'], p['published']))

# Select top 3
top3 = scored[:5]  # Get 5 to have choices after checking existing coverage

# Write selection metadata
with open(os.path.join(OUTDIR, 'selection.json'), 'w') as f:
    json.dump({
        'total_unique': len(unique),
        'top5': [{
            'id': p['id'],
            'title': p['title'],
            'published': p['published'],
            'authors': p['authors'][:3],
            'categories': p['categories'],
            'relevance_score': p['relevance_score'],
            'summary': p['summary'][:300],
        } for p in top3]
    }, f, indent=2)

print(f"Total unique papers: {len(unique)}")
for i, p in enumerate(top3):
    print(f"\n--- Candidate {i+1}: {p['title'][:90]} ---")
    print(f"  ID: {p['id']}")
    print(f"  Date: {p['published']}  Score: {p['relevance_score']}")
    print(f"  Categories: {', '.join(p['categories'])}")
    print(f"  Authors: {', '.join(p['authors'][:3])}")
    print(f"  Summary: {p['summary'][:200]}...")