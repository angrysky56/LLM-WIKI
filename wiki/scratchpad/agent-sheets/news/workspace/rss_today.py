#!/usr/bin/env python3
"""Broad RSS sweep — 5 primary feeds, top 15 per feed."""
import httpx, xml.etree.ElementTree as ET, urllib3, json, sys
urllib3.disable_warnings()

client = httpx.Client(timeout=20.0, verify=False, follow_redirects=True,
                       headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'})

feeds = {
    'BBC World': 'http://feeds.bbci.co.uk/news/world/rss.xml',
    'Al Jazeera': 'https://www.aljazeera.com/xml/rss/all.xml',
    'NYT World': 'https://rss.nytimes.com/services/xml/rss/nyt/World.xml',
    'Guardian': 'https://www.theguardian.com/world/rss',
    'Bloomberg': 'https://feeds.bloomberg.com/markets/news.rss',
}

results = {}
for name, url in feeds.items():
    try:
        r = client.get(url)
        if r.status_code != 200:
            results[name] = {'error': f'HTTP {r.status_code}', 'items': []}
            continue
        root = ET.fromstring(r.text)
        items = []
        for item in root.findall('.//item')[:20]:
            items.append({
                'title': (item.findtext('title') or '').strip(),
                'link': (item.findtext('link') or '').strip(),
                'pubDate': (item.findtext('pubDate') or '').strip(),
                'description': (item.findtext('description') or '').strip()[:400],
                'source': (item.findtext('source') or '').strip(),
            })
        results[name] = {'items': items}
    except Exception as e:
        results[name] = {'error': str(e), 'items': []}

with open('/home/ty/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets/news/workspace/rss_today.json', 'w') as f:
    json.dump(results, f, indent=2)

for name, data in results.items():
    print(f"\n=== {name} ({len(data.get('items', []))} items) ===")
    if 'error' in data:
        print(f"  ERROR: {data['error']}")
        continue
    for i, it in enumerate(data['items'][:12], 1):
        print(f"  {i}. {it['title'][:120]}")
