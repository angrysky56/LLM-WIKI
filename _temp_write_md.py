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

# Write results to a markdown file
lines = []
lines.append('# arXiv Agentic Systems Papers\n')
lines.append(f'Total unique results: {len(unique)}\n')
lines.append('')
for i, p in enumerate(unique[:25]):
    pid = p.get('id','?')
    pub = p.get('published','?')[:10]
    cats = ','.join(p.get('categories',['?']))
    title = p.get('title','?').replace('\n',' ').strip()
    summary = p.get('summary','?').replace('\n',' ').strip()[:300]
    authors = ', '.join(p.get('authors',['?'])[:4])
    ql = p.get('query_label','?')
    
    lines.append(f'## {i+1}. {title}')
    lines.append(f'- **ID:** `{pid}`')
    lines.append(f'- **Date:** {pub}')
    lines.append(f'- **Categories:** {cats}')
    lines.append(f'- **Authors:** {authors}')
    lines.append(f'- **Query:** {ql}')
    lines.append(f'- **Summary:** {summary}')
    lines.append('')

open('/tmp/arxiv_results.md','w').write('\n'.join(lines))