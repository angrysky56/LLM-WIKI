#!/usr/bin/env python3
import os

os.chdir('/home/ty/Documents/LLM-WIKI/wiki')

fixes = []

# 1. Fix [[grpo]] in group-relative-policy-optimization.md
f = 'concepts/group-relative-policy-optimization.md'
with open(f, 'r') as fh:
    content = fh.read()
new_content = content.replace('[[grpo]]', '[[group-relative-policy-optimization]]')
if new_content != content:
    with open(f, 'w') as fh:
        fh.write(new_content)
    fixes.append(f"Fixed grpo in {f}")
else:
    fixes.append(f"No grpo change needed in {f}")

# 2. Fix [[qora]] in lora.md (qora doesn't exist, use lora or quantized-lora)
f = 'concepts/lora.md'
with open(f, 'r') as fh:
    content = fh.read()
new_content = content.replace('[[qora]]', '[[quantization]]')
if new_content != content:
    with open(f, 'w') as fh:
        fh.write(new_content)
    fixes.append(f"Fixed qora in {f}")
else:
    fixes.append(f"No qora change needed in {f}")

# 3. Fix [[MOP]] in neural-architecture-search.md -> [[mop-architecture]]
f = 'concepts/neural-architecture-search.md'
with open(f, 'r') as fh:
    content = fh.read()
new_content = content.replace('[[MOP]]', '[[mop-architecture]]')
if new_content != content:
    with open(f, 'w') as fh:
        fh.write(new_content)
    fixes.append(f"Fixed MOP in {f}")
else:
    fixes.append(f"No MOP change needed in {f}")

# 4. Fix [[MOP]] in rz-nas.md -> [[mop-architecture]]
f = 'concepts/rz-nas.md'
with open(f, 'r') as fh:
    content = fh.read()
new_content = content.replace('[[MOP]]', '[[mop-architecture]]')
if new_content != content:
    with open(f, 'w') as fh:
        fh.write(new_content)
    fixes.append(f"Fixed MOP in {f}")
else:
    fixes.append(f"No MOP change needed in {f}")

# 5. Fix [[test-time-compute-scaling]] in parallel-reasoning.md
f = 'concepts/parallel-reasoning.md'
with open(f, 'r') as fh:
    content = fh.read()
new_content = content.replace('[[test-time-compute-scaling]]', '[[inference-time-compute-scaling]]')
if new_content != content:
    with open(f, 'w') as fh:
        fh.write(new_content)
    fixes.append(f"Fixed test-time-compute-scaling in {f}")
else:
    fixes.append(f"No test-time-compute-scaling change needed in {f}")

# 6. Fix [[quantization]] in parameter-efficient-fine-tuning.md (already correct, but check)
f = 'concepts/parameter-efficient-fine-tuning.md'
with open(f, 'r') as fh:
    content = fh.read()
# quantization page doesn't exist, but this is a valid concept - leave as-is

# 7. Fix [[quantization]] in qes.md -> [[quantized-lora]] or [[llm-training]]
f = 'concepts/qes.md'
with open(f, 'r') as fh:
    content = fh.read()
new_content = content.replace('[[quantization]]', '[[llm-training]]')
if new_content != content:
    with open(f, 'w') as fh:
        fh.write(new_content)
    fixes.append(f"Fixed quantization in {f}")
else:
    fixes.append(f"No quantization change needed in {f}")

# 8. Fix [[bradley-terry]] in opendeepthink-parallel-reasoning.md
f = 'concepts/opendeepthink-parallel-reasoning.md'
with open(f, 'r') as fh:
    content = fh.read()
new_content = content.replace('[[bradley-terry]]', '[[reward-modeling]]')
if new_content != content:
    with open(f, 'w') as fh:
        fh.write(new_content)
    fixes.append(f"Fixed bradley-terry in {f}")
else:
    fixes.append(f"No bradley-terry change needed in {f}")

# 9. Fix [[imagination]] Planning-stub link
f = 'concepts/imagination.md'
with open(f, 'r') as fh:
    content = fh.read()
# Planning-stub is a teaching example, remove it
new_content = content.replace('[[Planning-stub]]', '[[planning]]')
if new_content != content:
    with open(f, 'w') as fh:
        fh.write(new_content)
    fixes.append(f"Fixed Planning-stub in {f}")
else:
    fixes.append(f"No Planning-stub change needed in {f}")

# 10. Fix [[counterfactual-reasoning]]
f = 'concepts/imagination.md'
with open(f, 'r') as fh:
    content = fh.read()
new_content = content.replace('[[counterfactual-reasoning]]', '[[counterfactual]]')
if new_content != content:
    with open(f, 'w') as fh:
        fh.write(new_content)
    fixes.append(f"Fixed counterfactual-reasoning in {f}")
else:
    fixes.append(f"No counterfactual-reasoning change needed in {f}")

for msg in fixes:
    print(msg)
print(f"\nTotal fixes: {len(fixes)}")