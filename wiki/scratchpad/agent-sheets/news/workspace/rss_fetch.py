#!/usr/bin/env python3
import urllib.request
import xml.etree.ElementTree as ET
import ssl

def fetch_rss(query, max_items=15):
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
                "title": title.text.strip() if title is not None else "",
                "link": link.text.strip() if link is not None else "",
                "pubDate": pub.text.strip() if pub is not None else "",
                "description": desc.text.strip() if desc is not None else "",
            })
        return items
    except Exception as e:
        return [{"title": f"ERROR: {e}", "link": "", "pubDate": "", "description": ""}]

queries = [
    ("geopolitics", "geopolitics+may+2026"),
    ("ai_policy", "AI+tech+policy+regulation+may+2026"),
    ("science", "science+breakthrough+may+2026"),
    ("economy", "economy+trade+tariff+may+2026"),
    ("ai_science", "AI+science+math+breakthrough+2026"),
]

for name, query in queries:
    print(f"\n{'='*60}")
    print(f"TOPIC: {name} | QUERY: {query}")
    print('='*60)
    items = fetch_rss(query)
    for i, item in enumerate(items):
        print(f"\n[{i+1}] {item['title']}")
        print(f"    date: {item['pubDate']}")
        print(f"    link: {item['link'][:80]}...")
        if item['description']:
            snippet = item['description'][:200].replace('<br>', ' ').replace('<p>', '').replace('</p>', '')
            print(f"    desc: {snippet}...")