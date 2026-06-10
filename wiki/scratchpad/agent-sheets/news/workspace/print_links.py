import json, os
with open('/tmp/rss_standard.json') as f:
    data = json.load(f)
lines = []
for name, d in data.items():
    lines.append(f'=== {name} ===')
    for i, item in enumerate(d['items'][:5]):
        link = item.get('link', '')
        lines.append(f'  [{i+1}] {link[:140]}')
    lines.append('')
out = "\n".join(lines)
os.makedirs("/tmp/links", exist_ok=True)
for i in range(0, len(out), 80):
    with open(f"/tmp/links/chunk_{i:05d}.txt", "w") as f:
        f.write(out[i:i+80])