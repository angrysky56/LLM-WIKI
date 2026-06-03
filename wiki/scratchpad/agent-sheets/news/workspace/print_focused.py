#!/usr/bin/env python3
"""Print full details for top stories from the broad sweep."""
import json
with open('/home/ty/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets/news/workspace/rss_today.json') as f:
    data = json.load(f)

# Selected high-signal items to dig into
selected = [
    ('BBC World', 0, 'US-Iran Kuwait'),
    ('BBC World', 1, 'Israel strikes southern Lebanon'),
    ('BBC World', 2, 'Ukrainian drones St Petersburg'),
    ('Al Jazeera', 0, 'Kuwait Bahrain Iran barrage'),
    ('Al Jazeera', 6, 'Iran Kuwait Bahrain escalation'),
    ('NYT World', 0, 'Iran Kuwait attack'),
    ('NYT World', 1, 'Ukraine strikes St Petersburg'),
    ('NYT World', 4, 'Russia strikes Kyiv'),
    ('NYT World', 5, 'Ebola Kenya setback'),
    ('NYT World', 11, 'Trump Canada 51st state'),
    ('Guardian', 0, 'Kenyans fear US Ebola'),
    ('Guardian', 6, 'Trump 25% Brazil tariffs'),
    ('Bloomberg', 3, 'SpaceX IPO'),
    ('Bloomberg', 8, 'Oil Iran-US clashes'),
]

for feed, idx, label in selected:
    items = data.get(feed, {}).get('items', [])
    if idx >= len(items):
        print(f"\n[SKIP] {feed} #{idx} — only {len(items)} items")
        continue
    it = items[idx]
    print(f"\n{'='*70}")
    print(f"### {feed} #{idx} — {label}")
    print(f"{'='*70}")
    print(f"TITLE: {it['title']}")
    print(f"PUB:   {it['pubDate']}")
    print(f"LINK:  {it['link']}")
    print(f"DESC:  {it['description']}")
