#!/usr/bin/env python3
import urllib.request
import xml.etree.ElementTree as ET
import ssl

def fetch_rss(query, max_items=10):
    url = f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US%3Aen"
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        with urllib.request.urlopen(url, context=ctx, timeout=15) as resp:
            root = ET.parse(resp).getroot()
        items = []
        for item in root.findall(".//item")[:max_items]:
            title = item.find("title")
            link = item.find("link")
            pub = item.find("pubDate")
            desc = item.find("description")
            items.append({
                "title": (title.text or "").strip(),
                "link": (link.text or "").strip(),
                "pubDate": (pub.text or "").strip(),
                "description": (desc.text or "").strip(),
            })
        return items
    except Exception as e:
        return [{"title": f"ERROR: {e}", "link": "", "pubDate": "", "description": ""}]

# Run targeted queries for emerging stories
queries = [
    ("openai_erdos", "OpenAI+Erdos+problem+breakthrough+may+2026"),
    ("ebola_latest", "Bundibugyo+Ebola+May+2026"),
    ("spacex_ipo", "SpaceX+IPO+June+2026"),
    ("vatican_ai", "Pope+Leo+AI+encyclical+may+2026"),
    ("california_ai", "California+AI+order+implementation+2026"),
    ("south_sudan", "South+Sudan+violence+May+2026"),
    ("Gemini_science", "Gemini+Google+science+May+27+2026"),
]

for name, query in queries:
    print(f"\n{'='*60}")
    print(f"TOPIC: {name} | QUERY: {query}")
    print('='*60)
    items = fetch_rss(query)
    for i, item in enumerate(items):
        print(f"\n[{i+1}] {item['title']}")
        print(f"    date: {item['pubDate']}")
        print(f"    link: {item['link'][:100]}...")