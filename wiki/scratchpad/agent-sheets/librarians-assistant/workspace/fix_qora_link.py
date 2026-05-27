#!/usr/bin/env python3
import os

os.chdir('/home/ty/Documents/LLM-WIKI/wiki')

fixes = []

# Fix [[qora|QLoRA]] in lora.md -> [[lora|QLoRA]] (self-reference is fine for disambiguation)
f = 'concepts/lora.md'
with open(f, 'r') as fh:
    content = fh.read()
new_content = content.replace('[[qora|QLoRA]]', '[[lora|QLoRA]]')
if new_content != content:
    with open(f, 'w') as fh:
        fh.write(new_content)
    fixes.append(f"Fixed qora->lora in {f}")
else:
    fixes.append(f"No qora fix needed in {f}")

# Fix [[bounded-representation-capacity]] in arxiv carryover -> [[bounded-representation-capacity]]
# These are carryovers that won't be fixed by creating concepts; leave as stubs or fix manually

# Fix [[diffusion-models]] in generative-ai.md - we just created the stub

# Fix [[tool-use]] in autonomous-agents.md - we just created the stub

# Fix GoodRobot cross-refs - these point to wiki/projects/goodrobot/ paths
# The source is wiki/entities/projects/goodrobot.md which is shut down
# The targets point to wiki/projects/goodrobot/shut-down-entity etc.
# These should be fixed to point to the correct active files

for msg in fixes:
    print(msg)
print(f"\nTotal fixes: {len(fixes)}")