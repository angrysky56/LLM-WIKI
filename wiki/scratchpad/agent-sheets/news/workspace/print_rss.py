#!/usr/bin/env python3
"""Print RSS discovery results in readable format"""
import json
with open('/home/ty/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets/news/workspace/rss_output.json') as f:
    data = json.load(f)

for name, feed in data.items():
    status = feed.get('status', 'unknown')
    items = feed.get('items', [])
    print(f"\n{'='*60}")
    print(f"{name}  (status={status})")
    print(f"{'='*60}")
    if status == 'error':
        print(f"  ERROR: {feed.get('error', 'unknown')}")
        continue
    if not items:
        print("  (no items)")
        continue
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item['title']}")
        if item.get('pubDate'):
            print(f"     {item['pubDate']}")
        if item.get('description'):
            desc = item['description'][:150].replace('\n', ' ')
            print(f"     {desc}")
        print()