import json
d = json.load(open('/tmp/arxiv_agentic/selection.json'))
for i, p in enumerate(d['top5'][:3]):
    print(f"CANDIDATE {i+1}: {p['title'][:100]}")
    print(f"SUMMARY: {p['summary'][:250]}")
    print()