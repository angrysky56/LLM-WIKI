#!/usr/bin/env python3
"""Fix nested sources [[wikilink]] syntax that creates ghost wikilinks.
All these pages have sources field wikilinks that are ALSO present in body.
We reduce to sources: [] to eliminate ghost links while preserving actual coverage.
"""
import re
from pathlib import Path

pages = [
    'wiki/concepts/world-model.md',
    'wiki/concepts/agent-native-design.md',
    'wiki/concepts/machine-psychology.md',
    'wiki/concepts/openpraparat.md',
    'wiki/concepts/epistemic-energy.md',
    'wiki/concepts/ml-evolution.md',
    'wiki/concepts/meta_harness_loop.md',
    'wiki/concepts/language-evolution.md',
    'wiki/concepts/supertokens.md',
    'wiki/concepts/neural-long-term-memory.md',
    'wiki/concepts/causal-networks.md',
    'wiki/concepts/surprise-based-learning.md',
    'wiki/entities/projects/markovian-dev-agency.md',
    'wiki/entities/projects/efhf.md',
    'wiki/synthesis/self-prompting-via-production-stage-architecture.md',
]

for p in pages:
    text = Path(p).read_text()
    # Match sources: [[a]], [[b]], ...  (one or more double-bracket wikilinks)
    # Replace with sources: []
    new_text = re.sub(
        r'^sources:\s*\[\[.+?\]\](.*)$',
        r'sources: []\1',
        text,
        flags=re.MULTILINE
    )
    if new_text != text:
        Path(p).write_text(new_text)
        print(f'FIXED: {p}')
    else:
        print(f'NO CHANGE: {p}')

print('\nDone.')