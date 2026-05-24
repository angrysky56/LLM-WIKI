#!/usr/bin/env python3
"""Discover recent papers from arXiv API"""
import urllib.request
import xml.etree.ElementTree as ET
import json
from datetime import datetime, timedelta

def search_arxiv(query, max_results=15, categories="cs.AI+OR+cs.LG+OR+cs.CL"):
    url = (f"https://export.arxiv.org/api/query?"
           f"search_query={query}+AND+({categories})"
           f"&max_results={max_results}&sortBy=submittedDate&sortOrder=descending")
    print(f"Querying: {url[:120]}...")
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            root = ET.parse(resp).getroot()
        ns = {"a": "http://www.w3.org/2005/Atom"}
        papers = []
        for entry in root.findall("a:entry", ns):
            paper = {
                "id": entry.find("a:id", ns).text.strip().split("/abs/")[-1],
                "title": entry.find("a:title", ns).text.strip().replace("\n", " "),
                "authors": [a.find("a:name", ns).text for a in entry.findall("a:author", ns)][:3],
                "published": entry.find("a:published", ns).text[:10],
                "summary": entry.find("a:summary", ns).text.strip()[:300],
                "categories": [c.get("term") for c in entry.findall("a:category", ns)][:5],
                "pdf_url": f"https://arxiv.org/pdf/{entry.find('a:id', ns).text.strip().split('/abs/')[-1]}",
            }
            papers.append(paper)
        return papers
    except Exception as e:
        print(f"Error: {e}")
        return []

# Try recent submissions (last 7 days)
today = datetime.now()
date_cutoff = (today - timedelta(days=7)).strftime("%Y-%m-%d")

print(f"\n=== arXiv Discovery — {today.strftime('%Y-%m-%d')} ===")
print(f"Date cutoff: {date_cutoff}")

# Search 1: agentic AI, autonomous systems
p1 = search_arxiv("agentic+OR+autonomous+OR+agent+architecture", max_results=15)
# Search 2: reasoning, planning, tool use
p2 = search_arxiv("reasoning+OR+planning+OR+tool+use+OR+memory", max_results=15)
# Search 3: RL, reward modeling, self-improvement
p3 = search_arxiv("reinforcement+OR+reward+OR+self-improve+OR+alignment", max_results=15)

all_papers = p1 + p2 + p3
# Dedupe by ID
seen = set()
unique = []
for p in all_papers:
    if p['id'] not in seen:
        seen.add(p['id'])
        unique.append(p)

# Filter to recent (last 7 days)
recent = [p for p in unique if p['published'] >= date_cutoff]

print(f"\nTotal unique papers: {len(unique)}, Recent (7d): {len(recent)}")
print("\n--- Recent Papers ---")
for i, p in enumerate(recent[:12], 1):
    print(f"\n{i}. [{p['id']}] {p['title'][:80]}")
    print(f"   Authors: {', '.join(p['authors'])}")
    print(f"   Published: {p['published']} | Categories: {', '.join(p['categories'][:3])}")
    print(f"   Summary: {p['summary'][:150]}...")

# Save for reference
with open("/home/ty/Documents/LLM-WIKI/wiki/scratchpad/jobs/reports/arxiv/discovered_papers.json", "w") as f:
    json.dump(recent, f, indent=2)
print(f"\nSaved {len(recent)} papers to discovered_papers.json")