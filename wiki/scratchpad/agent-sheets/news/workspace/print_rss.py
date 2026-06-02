import json
with open('/home/ty/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets/news/workspace/rss_today.json') as f:
    data = json.load(f)
for feed, payload in data.items():
    print(f'=== {feed} ===')
    if not payload.get('ok'):
        print(f'  ERROR: {payload.get("error")}')
        continue
    for i, item in enumerate(payload.get('items', []), 1):
        print(f'  {i}. {item["title"][:140]} | {item["pubDate"][:30]}')
    print()
