import json, sys

d = json.load(open('/tmp/arxiv_agentic/selection.json'))
lines = []
lines.append('---')
lines.append('created: 2026-06-08')
lines.append('type: source')
lines.append('summary: arXiv agentic systems paper selections')
lines.append('tags: [arxiv, agentic-systems, work-in-progress]')
lines.append('status: reference')
lines.append('---')
lines.append('')
lines.append('# arXiv Agentic Systems — Paper Candidates')
lines.append('')
lines.append(f'Total unique papers found: {d["total_unique"]}')
lines.append('')

for i, p in enumerate(d['top5']):
    lines.append(f'## Candidate {i+1}: {p["title"]}')
    lines.append(f'- **arXiv ID:** `{p["id"]}`')
    lines.append(f'- **Published:** {p["published"]}')
    lines.append(f'- **Categories:** {", ".join(p["categories"])}')
    lines.append(f'- **Relevance Score:** {p["relevance_score"]}')
    lines.append(f'- **Authors:** {", ".join(p.get("authors",["unknown"])[:4])}')
    lines.append(f'- **Summary:** {p["summary"][:400]}')
    lines.append('')

open('/home/ty/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets/arxiv/workspace/candidate-papers.md', 'w').write('\n'.join(lines))
print("Written successfully")