#!/usr/bin/env python3
"""Better arXiv search - specifically for tool-use agents, web agents, computer use, function calling."""
import urllib.request, urllib.parse, xml.etree.ElementTree as ET, json, sys, time, os

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
            'summary': summary[:600],
        })
    return results

# More targeted queries for agentic systems week
queries = [
    # Tool use / function calling
    ('tool-use', 'cat:cs.AI+AND+ti:(tool+use+OR+function+calling+OR+tool+calling+OR+tool+augmented)'),
    ('tool-use-lg', 'cat:cs.LG+AND+ti:(tool+use+OR+function+calling+OR+tool+calling+OR+tool+augmented)'),
    ('tool-use-cl', 'cat:cs.CL+AND+ti:(tool+use+OR+function+calling+OR+tool+calling+OR+tool+augmented)'),
    # Web agents / browser agents / computer use
    ('web-agent', 'cat:cs.AI+AND+ti:(web+agent+OR+browser+agent+OR+computer+use+OR+gui+agent)'),
    ('web-agent-cl', 'cat:cs.CL+AND+ti:(web+agent+OR+browser+agent+OR+computer+use+OR+gui+agent)'),
    # Code agents
    ('code-agent', 'cat:cs.LG+AND+ti:(code+agent+OR+swe+bench+OR+code+generation+OR+software+engineering+agent)'),
    ('code-agent-cl', 'cat:cs.CL+AND+ti:(code+agent+OR+swe+bench+OR+code+generation+OR+software+engineering+agent)'),
    # Agent frameworks / architectures
    ('agent-framework', 'cat:cs.AI+AND+ti:(agent+framework+OR+agent+architecture+OR+multi+agent+OR+agentic+system)'),
    ('agent-lg', 'cat:cs.LG+AND+ti:(agent+framework+OR+agent+architecture+OR+multi+agent+OR+agentic+system)'),
    # Also search broadly in all fields for recent agent papers
    ('agent-broad', 'cat:cs.AI+AND+all:agentic+AND+all:(system+OR+framework+OR+benchmark)+AND+submittedDate:[20260501+TO+20260608]'),
]

all_papers = []
for label, q in queries:
    try:
        xml_data = search_arxiv(q, max_results=6)
        papers = parse_arxiv_xml(xml_data)
        for p in papers:
            p['query_source'] = label
        all_papers.extend(papers)
        time.sleep(5)
    except Exception as e:
        pass

# Deduplicate
seen = set()
unique = []
for p in all_papers:
    pid = p['id']
    if pid and pid not in seen:
        seen.add(pid)
        unique.append(p)

# Score by relevance
scored = []
for p in unique:
    t = p['title'].lower()
    s = p['summary'].lower()
    score = 0
    # Strong signals (5x)
    for kw in ['tool use', 'function calling', 'tool calling', 'tool augmented', 
               'web agent', 'browser agent', 'computer use', 'gui agent',
               'code agent', 'swe-bench', 'swe_bench', 'software engineering agent',
               'agent framework', 'multi-agent', 'agentic system', 'api calling',
               'tool learning', 'agent training', 'action space']:
        if kw in t: score += 5
        if kw in s: score += 2
    # Moderate signals (3x)
    for kw in ['agent', 'tool', 'code generation', 'software engineering',
               'reinforcement learning', 'environment']:
        if kw in t: score += 3
    # Penalize non-agent topics (but only strongly in title)
    for kw in ['drug', 'chemistry', 'biology', 'medical', 'clinical', 'protein']:
        if kw in t: score -= 5
    
    p['relevance_score'] = score
    scored.append(p)

scored.sort(key=lambda p: (-p['relevance_score'], p['published']))

# Select top candidates (more than 3 so we can pick the best)
top = scored[:10]

with open(os.path.join(OUTDIR, 'top_candidates.json'), 'w') as f:
    json.dump({
        'total_unique': len(unique),
        'top10': [{
            'id': p['id'],
            'title': p['title'],
            'published': p['published'],
            'authors': p['authors'][:4],
            'categories': p['categories'],
            'relevance_score': p['relevance_score'],
            'query_source': p['query_source'],
            'summary': p['summary'][:400],
        } for p in top]
    }, f, indent=2)

print(f"Total unique: {len(unique)}")
for i, p in enumerate(top[:10]):
    print(f"")
    print(f"--- Candidate {i+1} (Score: {p['relevance_score']}) ---")
    print(f"  ID: {p['id']}")
    print(f"  Title: {p['title'][:120]}")
    print(f"  Date: {p['published']}  Source: {p['query_source']}")
    print(f"  Cats: {', '.join(p['categories'])}")
    print(f"  Authors: {', '.join(p['authors'][:3])}")
    print(f"  Summary: {p['summary'][:300]}")