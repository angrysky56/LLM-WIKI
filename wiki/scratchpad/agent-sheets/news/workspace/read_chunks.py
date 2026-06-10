import os

def chunk_file(filepath, outdir="/tmp/skill_chunks"):
    os.makedirs(outdir, exist_ok=True)
    with open(filepath) as f:
        text = f.read()
    for i in range(0, len(text), 80):
        slug = f"chunk_{i:05d}"
        with open(os.path.join(outdir, slug + ".txt"), "w") as out:
            out.write(text[i:i+80])
    print(f"Split {len(text)} bytes into {len(range(0, len(text), 80))} chunks in {outdir}")

chunk_file("/home/ty/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets/news/SKILL.md")
chunk_file("/home/ty/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets/news/carryover.md")