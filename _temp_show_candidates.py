import json
d = json.load(open('/tmp/arxiv_agentic/selection.json'))
for i, p in enumerate(d['top5'][:3]):
    print(f"CANDIDATE {i+1}")
    print(f"ID: {p['id']}")
    print(f"TITLE: {p['title'][:150]}")
    print(f"DATE: {p['published']}")
    print(f"SCORE: {p['relevance_score']}")
    print(f"CATS: {', '.join(p['categories'])}")
    print(f"AUTHORS: {', '.join(p.get('authors',['?'])[:3])}")
    print(f"SUMMARY: {p['summary'][:300]}")
    print()