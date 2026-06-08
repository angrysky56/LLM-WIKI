import json
d = json.load(open('/tmp/arxiv_agentic/top_candidates.json'))
for i, p in enumerate(d['top10'][:10]):
    print(f"CANDIDATE {i+1}")
    print(f"ID: {p['id']}")
    print(f"SCORE: {p['relevance_score']}")
    print(f"TITLE: {p['title'][:150]}")
    print(f"DATE: {p['published']}")
    print(f"SOURCE: {p['query_source']}")
    print(f"CATS: {', '.join(p['categories'])}")
    print(f"AUTHORS: {', '.join(p.get('authors',['?'])[:3])}")
    print(f"SUMMARY: {p['summary'][:300]}")
    print()