#!/usr/bin/env python3
"""Scan sources fields for nested [[wikilink]] patterns that create ghost wikilinks."""
import re
from pathlib import Path

# Pages with nested sources syntax
targets = [
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
    'wiki/scratchpad/jobs/reports/librarians-assistant/carryover.md',
    'wiki/scratchpad/jobs/reports/librarian/batch-progress.md',
]

for p in targets:
    text = Path(p).read_text()
    # Extract sources field
    m = re.search(r'^sources:\s*(.+?)(?=\n\w|\Z)', text, re.MULTILINE | re.DOTALL)
    if m:
        sources_line = m.group(1).strip()
        # Check if any [[...]] appears in the sources field value
        wiki_links = re.findall(r'\[\[([^\]]+)\]\]', sources_line)
        if wiki_links:
            # Now check if each link appears as a body wikilink too
            body_links = re.findall(r'\[\[([^\]]+)\]\]', text)
            body_slugs = [l.strip().lower().replace(' ', '-') for l in body_links]

            print(f'\n=== {p} ===')
            print(f'  Sources: {sources_line[:100]}')
            print(f'  Ghost wikilinks in sources: {wiki_links}')
            print(f'  Body has wikilinks: {body_links[:5]}...')
            missing_in_body = [l for l in wiki_links if l.lower().replace(' ', '-') not in body_slugs]
            if missing_in_body:
                print(f'  ** Missing in body: {missing_in_body}')
            else:
                print(f'  All sources have body wikilinks — OK to empty sources field')