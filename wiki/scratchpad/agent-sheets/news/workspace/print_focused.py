import json
with open('/home/ty/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets/news/workspace/rss_focused.json') as f:
    data = json.load(f)
for q, items in data.items():
    print(f'=== {q} ===')
    if isinstance(items, dict) and 'error' in items:
        print(f'  ERROR: {items["error"]}')
        continue
    for i, item in enumerate(items[:8], 1):
        print(f'  {i}. {item["title"][:160]}')
        if item.get("desc"):
            print(f'      {item["desc"][:200]}')
        print(f'      [{item["pubDate"][:30]}]')
    print()
