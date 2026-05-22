#!/usr/bin/env python3
import re
from pathlib import Path

all_pages = list(Path('wiki').rglob('*.md'))
all_pages = [p for p in all_pages if 'log.md' not in str(p)]

found = {}
for p in all_pages:
    content = p.read_text()
    # Look for tag-list patterns like [['news', 'geopolitics', ...]]
    if "[['news" in content or "['geopolitics'" in content.lower():
        matches = re.findall(r"\[\[[^\]]+\]\]+", content)
        for m in matches[:3]:
            if p not in found:
                found[str(p)] = []
            found[str(p)].append(m[:80])

print(f'Files with tag-list patterns: {len(found)}')
for p, ms in found.items():
    for m in ms:
        print(f'  {p}: {m}')