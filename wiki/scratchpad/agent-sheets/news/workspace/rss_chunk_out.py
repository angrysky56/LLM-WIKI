import json

def chunk_output(data, outdir="/tmp/rss_out"):
    import os
    os.makedirs(outdir, exist_ok=True)
    lines = []
    for name, d in data.items():
        lines.append(f"\n=== {name} ({d['status']}) ===")
        for i, item in enumerate(d['items']):
            lines.append(f"  [{i+1}] {item['title'][:120]}")
    text = "\n".join(lines)
    for i in range(0, len(text), 80):
        slug = f"chunk_{i:05d}"
        with open(os.path.join(outdir, f"{slug}.txt"), "w") as out:
            out.write(text[i:i+80])
    print(f"Wrote {len(lines)} lines as {len(range(0,len(text),80))} chunks")

with open('/tmp/rss_standard.json') as f:
    data = json.load(f)
chunk_output(data)