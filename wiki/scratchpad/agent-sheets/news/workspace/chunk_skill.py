import os

base = "/home/ty/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets/news"
with open(os.path.join(base, "SKILL.md")) as f:
    text = f.read()

for i in range(0, len(text), 80):
    slug = f"chunk_{i:05d}"
    with open(f"/tmp/skill_md/{slug}.txt", "w") as out:
        out.write(text[i:i+80])