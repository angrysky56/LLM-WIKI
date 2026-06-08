import json
data = json.load(open('/tmp/arxiv_results.json'))
# Deduplicate by id
seen = set()
unique = []
for p in data:
    pid = p.get('id','')
    if pid not in seen:
        seen.add(pid)
        unique.append(p)
print(f'Total unique: {len(unique)}')
print()
print('--- TOP PAPERS BY TITLE ---')
for i, p in enumerate(unique[:30]):
    pid = p.get('id','?')[:25]
    pub = p.get('published','?')[:10]
    cats = ','.join(p.get('categories',['?']))[:20]
    title = p.get('title','?')[:120]
    print(f'{i:3d}) [{pid}] {pub} | {cats}')
    print(f'     {title}')
    print()