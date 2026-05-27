import os
import re
from pathlib import Path

wiki_root = Path("wiki")
all_pages = {}  # path -> set of outgoing links

# Collect all pages and their wikilinks
for md_file in wiki_root.rglob("*.md"):
    if "log.md" in str(md_file):
        continue
    try:
        content = md_file.read_text()
    except:
        continue

    links = set()
    # Find [[wikilinks]]
    for match in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content):
        links.add(match.strip().lower())

    all_pages[str(md_file)] = links

# Find pages that reference non-existent pages
broken_links = []
for src, links in all_pages.items():
    for link in links:
        link_slug = re.sub(r'[^a-z0-9-]', '-', link.lower())
        found = False
        for p in all_pages:
            p_slug = re.sub(r'[^a-z0-9-]', '-', p.lower())
            if link.lower() in p.lower() or link_slug in p_slug:
                found = True
                break
        if not found:
            broken_links.append((src, link))

print("BROKEN WIKILINKS (alias targets that don't exist):")
for src, link in sorted(broken_links):
    print(f"  [[{link}]] in {src}")

# Build inbound link map (simple approach)
print("\n--- Building inbound map ---")
inbound = {p: set() for p in all_pages}
for src, links in all_pages.items():
    for link in links:
        link_lower = link.lower()
        for p in all_pages:
            if link_lower in p.lower():
                inbound[p].add(src)

print(f"\nTotal pages: {len(all_pages)}")
print(f"Total broken links: {len(broken_links)}")

print("\nPAGES WITH ZERO INBOUND LINKS (orphans):")
orphan_count = 0
for p, ins in sorted(inbound.items()):
    if len(ins) == 0 and "log.md" not in p:
        print(f"  {p}")
        orphan_count += 1
print(f"Orphan count: {orphan_count}")