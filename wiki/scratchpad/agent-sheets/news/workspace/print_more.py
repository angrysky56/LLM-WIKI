#!/usr/bin/env python3
"""Check full Bloomberg list (all 20) — top 12 was cut off."""
import json
with open('/home/ty/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets/news/workspace/rss_today.json') as f:
    data = json.load(f)

print("=== Bloomberg ALL ===")
for i, it in enumerate(data['Bloomberg']['items']):
    print(f"  {i+1}. [{it['pubDate'][:25]}] {it['title'][:140]}")

print("\n=== Al Jazeera ALL ===")
for i, it in enumerate(data['Al Jazeera']['items']):
    print(f"  {i+1}. [{it['pubDate'][:25]}] {it['title'][:140]}")

print("\n=== NYT World ALL ===")
for i, it in enumerate(data['NYT World']['items']):
    print(f"  {i+1}. [{it['pubDate'][:25]}] {it['title'][:140]}")
