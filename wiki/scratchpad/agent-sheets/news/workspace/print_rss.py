import json
with open('/tmp/rss_standard.json') as f:
    data = json.load(f)

for name, d in data.items():
    print(f"\n=== {name} ({d['status']}) ===")
    for i, item in enumerate(d['items']):
        print(f"  [{i+1}] {item['title'][:120]}")
        print(f"       {item['link'][:120]}")
        if item['desc']:
            print(f"       {item['desc'][:120]}")