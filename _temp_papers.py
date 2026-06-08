import json, sys
data = json.load(open('/tmp/arxiv_results.json'))

# Deduplicate by id
seen = set()
unique = []
for p in data:
    pid = p.get('id','')
    if pid not in seen:
        seen.add(pid)
        unique.append(p)

# Output paper details one per line, pipe-safe
for i, p in enumerate(unique[:25]):
    pid = p.get('id','?')
    pub = p.get('published','?')[:10]
    cats = ','.join(p.get('categories',['?']))
    title = p.get('title','?').replace('\n',' ').strip()
    # Output as pipe-delimited
    print(f'PAPER|{i}|{pid}|{pub}|{cats}|{title}')