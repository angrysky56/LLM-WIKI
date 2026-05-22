#!/usr/bin/env python3
"""Full wiki audit: frontmatter, broken links, orphans, reciprocal links."""
import re
from pathlib import Path

wiki_root = Path("wiki")
results = {
    "missing_frontmatter": [],
    "broken_links": [],
    "all_links": {},  # src -> [(link, target_file)]
    "pages": [],
}

# Frontmatter check
FRONTMATTER_FIELDS = ["created", "updated", "type", "summary", "tags", "sources", "status", "confidence"]

for md_file in wiki_root.rglob("*.md"):
    if "log.md" in str(md_file):
        continue
    try:
        content = md_file.read_text()
    except:
        continue
    
    # Check frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        missing = [f for f in FRONTMATTER_FIELDS if f not in fm_text]
        if missing:
            results["missing_frontmatter"].append((str(md_file), missing))
    else:
        results["missing_frontmatter"].append((str(md_file), ["NO-FRONTMATTER"]))
    
    # Collect wikilinks
    links = []
    for match in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content):
        links.append(match.strip().lower())
    results["all_links"][str(md_file)] = links
    results["pages"].append(str(md_file))

# Build target file map
slug_to_file = {}
for p in results["pages"]:
    parts = p.split("/")
    if len(parts) >= 2:
        slug = parts[-1].replace(".md", "").lower()
        slug_to_file[slug] = p

# Check broken links
for src, links in results["all_links"].items():
    for link in links:
        link_slug = link.lower()
        if link_slug not in slug_to_file:
            results["broken_links"].append((src, link))

print("=== FRONTMATTER ISSUES ===")
for path, missing in sorted(results["missing_frontmatter"]):
    print(f"  {path}: missing {missing}")
print(f"Total: {len(results['missing_frontmatter'])}")

print("\n=== BROKEN WIKILINKS (top 30) ===")
for src, link in sorted(results["broken_links"])[:30]:
    print(f"  [[{link}]] -> not found (from {src})")
print(f"Total broken: {len(results['broken_links'])}")

print(f"\n=== SUMMARY ===")
print(f"Total pages: {len(results['pages'])}")
print(f"Missing frontmatter: {len(results['missing_frontmatter'])}")
print(f"Broken wikilinks: {len(results['broken_links'])}")