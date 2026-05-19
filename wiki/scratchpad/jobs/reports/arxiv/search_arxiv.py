#!/usr/bin/env python3
"""Search arXiv for recent ML/AI papers."""

import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import time
import sys

def search_arxiv(query, max_results=10, sort_by="submittedDate", sort_order="descending"):
    """Search arXiv API and return parsed results."""
    params = urllib.parse.urlencode({
        "search_query": query,
        "max_results": max_results,
        "sortBy": sort_by,
        "sortOrder": sort_order
    })
    url = f"https://export.arxiv.org/api/query?{params}"

    print(f"Querying: {url[:80]}...", file=sys.stderr)
    req = urllib.request.Request(url, headers={"User-Agent": "Hermes-Agent/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            data = response.read().decode("utf-8")
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return []

    ns = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(data)

    papers = []
    for entry in root.findall("a:entry", ns):
        try:
            title = entry.find("a:title", ns).text.strip().replace("\n", " ")
            arxiv_id = entry.find("a:id", ns).text.strip().split("/abs/")[-1]
            published = entry.find("a:published", ns).text[:10]
            authors = ", ".join(
                a.find("a:name", ns).text
                for a in entry.findall("a:author", ns)
            )[:200]
            summary = entry.find("a:summary", ns).text.strip()[:300]
            cats = ", ".join(c.get("term") for c in entry.findall("a:category", ns))
            papers.append({
                "title": title,
                "arxiv_id": arxiv_id,
                "published": published,
                "authors": authors,
                "summary": summary,
                "categories": cats,
                "pdf": f"https://arxiv.org/pdf/{arxiv_id}",
                "abs": f"https://arxiv.org/abs/{arxiv_id}"
            })
        except Exception as e:
            print(f"Warning: could not parse entry: {e}", file=sys.stderr)
            continue

    return papers

def print_paper(p, idx):
    print(f"\n{'='*60}")
    print(f"{idx+1}. {p['title']}")
    print(f"   arXiv: {p['arxiv_id']} | Published: {p['published']}")
    print(f"   Categories: {p['categories']}")
    print(f"   Authors: {p['authors'][:150]}...")
    print(f"   Abstract: {p['summary'][:250]}...")
    print(f"   PDF: {p['pdf']}")

if __name__ == "__main__":
    # Search latest in core ML/AI categories
    queries = [
        ("cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL", "cs.AI/cs.LG/cs.CL"),
        ("all:reinforcement+learning+agent", "RL agents"),
        ("all:LLM+OR+all:language+model+training", "LLM training"),
    ]

    all_papers = []
    seen_ids = set()

    for query, label in queries:
        papers = search_arxiv(query, max_results=8)
        time.sleep(5)  # Rate limit between queries

        for p in papers:
            if p["arxiv_id"] not in seen_ids:
                seen_ids.add(p["arxiv_id"])
                p["query_label"] = label
                all_papers.append(p)

        if len(all_papers) >= 15:
            break

    print(f"\n\n=== FOUND {len(all_papers)} PAPERS ===\n")
    for i, p in enumerate(all_papers[:15]):
        print_paper(p, i)