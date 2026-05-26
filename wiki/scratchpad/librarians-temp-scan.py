#!/usr/bin/env python3
import os, re
from pathlib import Path

# Full scan for nested sources syntax that causes ghost wikilinks
print('=== Ghost wikilink sources: nested list ===')
found = []
for f in Path('wiki').rglob('*.md'):
    if 'Clippings' in str(f) or 'raw' in str(f):
        continue
    text = f.read_text()
    # Match: sources: [['something']] — YAML list containing a list (the problematic nested form)
    if re.search(r'sources:\s*\[\s*\[', text):
        found.append(str(f))

if found:
    for f in found:
        print(f'  {f}')
else:
    print('  None found — clean')

# Check frontmatter completeness on key files
print()
print('=== Frontmatter check: synthesis/republican-party-duplicate ===')
text = Path('wiki/synthesis/republican-party-duplicate.md').read_text()
has_fm = text.startswith('---')
has_created = 'created:' in text
has_type = 'type:' in text
print(f'  frontmatter: {has_fm}, created: {has_created}, type: {has_type}')

print()
print('=== Frontmatter check: entities/projects/goodrobot ===')
text = Path('wiki/entities/projects/goodrobot.md').read_text()
has_fm = text.startswith('---')
has_created = 'created:' in text
has_type = 'type:' in text
print(f'  frontmatter: {has_fm}, created: {has_created}, type: {has_type}')

print()
print('=== Reciprocal link check: republican-party-duplicate -> republican-party ===')
text = Path('wiki/synthesis/republican-party-duplicate.md').read_text()
if '[[republican-party]]' in text:
    print('  Has link to republican-party')
else:
    print('  MISSING link to republican-party')

print()
print('=== Checking all 16 nested-sources pages for body wikilinks ===')
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
    # Extract sources field value
    m = re.search(r'sources:\s*(.+)', text)
    if m:
        sources_val = m.group(1).strip()
        print(f'  {p}: sources={sources_val[:80]}')