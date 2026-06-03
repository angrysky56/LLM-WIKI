#!/usr/bin/env python3
"""Focused Google News RSS query for the two stories whose article URL failed."""
import httpx, xml.etree.ElementTree as ET, urllib3, json
urllib3.disable_warnings()
client = httpx.Client(timeout=20.0, verify=False, follow_redirects=True,
                       headers={'User-Agent': 'Mozilla/5.0'})

queries = {
    'trump-espriella-colombia': 'https://news.google.com/rss/search?q=Trump+endorses+De+La+Espriella+Colombia&hl=en-US&gl=US&ceid=US:en',
    'trump-canada-51st-state': 'https://news.google.com/rss/search?q=Trump+Canada+51st+state+trade+talks&hl=en-US&gl=US&ceid=US:en',
}
out = {}
for k, url in queries.items():
    try:
        r = client.get(url)
        if r.status_code != 200:
            out[k] = {'error': f'HTTP {r.status_code}'}
            continue
        root = ET.fromstring(r.text)
        items = []
        for item in root.findall('.//item')[:8]:
            items.append({
                'title': (item.findtext('title') or '').strip(),
                'link': (item.findtext('link') or '').strip(),
                'pubDate': (item.findtext('pubDate') or '').strip(),
                'description': (item.findtext('description') or '').strip()[:500],
            })
        out[k] = {'items': items}
    except Exception as e:
        out[k] = {'error': str(e)}

with open('/home/ty/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets/news/workspace/rss_focused.json', 'w') as f:
    json.dump(out, f, indent=2)

for k, v in out.items():
    print(f"\n=== {k} ===")
    if 'error' in v:
        print(f"  ERROR: {v['error']}")
        continue
    for i, it in enumerate(v['items']):
        print(f"\n  {i+1}. {it['title'][:140]}")
        print(f"     PUB: {it['pubDate'][:30]}")
        print(f"     DESC: {it['description'][:200]}")
