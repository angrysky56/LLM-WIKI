import json
d = json.load(open('/tmp/arxiv_agentic/top_candidates.json'))
for i, p in enumerate(d['top10'][:10]):
    print(f"{i+1}|{p['id']}|{p['relevance_score']}|{p['published']}|{','.join(p['categories'])}|{p['title'][:120]}")
print("===SEPARATOR===")
d2 = json.load(open('/tmp/arxiv_agentic/selection.json'))
for i, p in enumerate(d2['top5']):
    print(f"{i+1}|{p['id']}|{p['relevance_score']}|{p['published']}|{','.join(p['categories'])}|{p['title'][:120]}")