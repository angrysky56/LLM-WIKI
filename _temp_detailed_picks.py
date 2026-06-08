import json

# Read both result sets
d_all = json.load(open('/tmp/arxiv_agentic/top_candidates.json'))
d_first = json.load(open('/tmp/arxiv_agentic/selection.json'))

# Build a combined lookup
combined = {}
for p in d_all['top10'] + d_first['top5']:
    combined[p['id']] = p

# Papers I'm considering for agentic systems theme
targets = [
    '2605.31268v1',  # Mellum2 - open code+tool use model
    '2605.18332v1',  # Same Signal - SWE agent behavior analysis
    '2606.04896v2',  # Channel Fracture - multi-agent memory
    '2505.14246v1',  # Visual Agentic RFT - training agents with tool use
    '2604.14668v1',  # GUI Agents
    '2605.11928v1',  # Sim-to-Real for tool use agents
    '2606.05711v2',  # Beyond tokens - latent communication in MAS
]

for pid in targets:
    p = combined.get(pid)
    if not p:
        print(f"*** {pid}: NOT FOUND ***")
        continue
    print(f"=== {p['title'][:120]} ===")
    print(f"ID: {pid} | SCORE: {p.get('relevance_score','?')} | PUB: {p['published']}")
    print(f"CATS: {', '.join(p['categories'])}")
    print(f"SUMMARY: {p['summary'][:400]}")
    print()