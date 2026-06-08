import json
d = json.load(open('/tmp/arxiv_agentic/top_candidates.json'))
print("=== SUMMARIES ===")
for i, p in enumerate(d['top10'][:5]):
    print(f"\n--- CANDIDATE {i+1}: {p['title'][:100]} ---")
    print(f"ID: {p['id']}")
    print(f"SUMMARY: {p['summary'][:300]}")