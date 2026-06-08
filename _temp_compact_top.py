import json, sys
d = json.load(open('/tmp/arxiv_agentic/top_candidates.json'))
for i, p in enumerate(d['top10'][:10]):
    sys.stdout.write(f"CANDIDATE {i+1}\nID: {p['id']}\nSCORE: {p['relevance_score']}\nTITLE: {p['title'][:120]}\nPUB: {p['published']}\nCATS: {','.join(p['categories'])}\nAUTHORS: {','.join(p.get('authors',['?'])[:3])}\n\n")