"""
Fix double frontmatter blocks in wiki pages.
The pattern: some pages have TWO '---' frontmatter blocks due to conversion bugs.
The first block is typically partial/duplicate tags, the second is the real frontmatter.
Fix = keep the LAST complete frontmatter block, discard the partial first block.
"""
from pathlib import Path
import re

def find_real_frontmatter(text):
    """Find the LAST block that looks like valid frontmatter."""
    lines = text.split('\n')
    dash_locations = [i for i, l in enumerate(lines) if l.strip() == '---']
    
    if len(dash_locations) < 2:
        return None
    
    # Find all complete blocks (between a pair of --- delimiters)
    complete_blocks = []
    for i in range(len(dash_locations) - 1):
        open_idx = dash_locations[i]
        close_idx = dash_locations[i + 1]
        content = '\n'.join(lines[open_idx + 1:close_idx]).strip()
        complete_blocks.append((open_idx, close_idx, content))
    
    # Find the last block that has frontmatter keys
    best_block = None
    for open_idx, close_idx, content in reversed(complete_blocks):
        first_lines = [l.strip() for l in content.split('\n') if l.strip()][:3]
        if any(re.match(r'^[a-z][a-z_-]*:', l) for l in first_lines):
            best_block = (open_idx, close_idx, content)
            break
    
    return best_block

def fix_file(path):
    text = Path(path).read_text()
    
    block = find_real_frontmatter(text)
    if block is None:
        return False
    
    open_idx, close_idx, fm_content = block
    lines = text.split('\n')
    
    # The markdown content starts AFTER the last closing ---
    last_close = max(i for i, l in enumerate(lines) if l.strip() == '---')
    markdown = '\n'.join(lines[last_close + 1:]).lstrip('\n')
    
    # Check if already fixed (exactly one block)
    dash_count = text.count('\n---\n')
    if dash_count == 1:
        return False  # Already clean
    
    # Reconstruct: single clean frontmatter + markdown
    new_text = '---\n' + fm_content + '\n---\n\n' + markdown
    Path(path).write_text(new_text)
    return True

# Run on concepts + entities + synthesis
if __name__ == '__main__':
    wiki_dirs = [Path('wiki/concepts'), Path('wiki/entities'), Path('wiki/synthesis')]
    fixed_count = 0
    errors = []
    
    for d in wiki_dirs:
        for f in d.rglob('*.md'):
            try:
                if fix_file(f):
                    print(f'FIXED: {f}')
                    fixed_count += 1
            except Exception as e:
                errors.append((str(f), str(e)))
    
    print(f'\nTotal fixed: {fixed_count}')
    if errors:
        print(f'Errors: {len(errors)}')