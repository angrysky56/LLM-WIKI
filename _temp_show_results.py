#!/usr/bin/env python3
import json
data = json.load(open('/tmp/arxiv_results.json'))
print(f'Total results: {len(data)}')
print(f'{"#":>3} {"arXiv ID":<20} {"Date":<12} {"Categories":<20} {"Title":<80}')
print('-'*135)
for i, p in enumerate(data[:30]):
    pid = p.get('id','?')[:20]
    pub = p.get('published','?')[:10]
    cats = ','.join(p.get('categories',['?']))[:20]
    title = p.get('title','?')[:80]
    ql = p.get('query_label','?')
    print(f'{i:3d} {pid:<20} {pub:<12} {cats:<20} {title}')