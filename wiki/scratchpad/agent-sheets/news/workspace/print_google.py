import json, os

with open('/tmp/rss_google.json') as f:
    data = json.load(f)

lines = []
for name, d in data.items():
    status = d['status']
    n = len(d['items'])
    lines.append(f"{name}: {status} ({n} items)")
    for i, item in enumerate(d['items']):
        lines.append(f"  [{i+1}] {item['title'][:120]}")

text = "\n".join(lines)
os.makedirs('/tmp/google_out', exist_ok=True)
for i in range(0, len(text), 80):
    slug = f"chunk_{i:05d}"
    with open(f"/tmp/google_out/{slug}.txt", "w") as out:
        out.write(text[i:i+80])
print(f"{len(lines)} lines into {len(range(0,len(text),80))} chunks")