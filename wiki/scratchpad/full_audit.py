from pathlib import Path
import re

wiki_dirs = [Path('wiki/concepts'), Path('wiki/entities'), Path('wiki/synthesis'), Path('wiki/sources')]
all_pages = set()
for d in wiki_dirs:
    for f in d.rglob('*.md'):
        all_pages.add(f.stem.lower())

truly_broken = []
for d in wiki_dirs:
    for f in d.rglob('*.md'):
        text = f.read_text()
        links = re.findall(r'\[\[([^\]|]+)\]\]', text)
        for link in links:
            slug = link.lower().replace(' ', '-').strip()
            if slug not in all_pages and slug not in ('index', 'log'):
                truly_broken.append((f, link, slug))

from collections import Counter
counter = Counter(x[2] for x in truly_broken)
print('Missing stubs by ref count:')
for slug, count in counter.most_common(30):
    print(f'  {slug}: {count}')