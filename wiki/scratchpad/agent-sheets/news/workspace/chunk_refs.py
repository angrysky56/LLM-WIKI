import os

refs = [
    "google-news-query-patterns.md",
    "excluded-topics.md",
    "http-fetch-failures.md",
    "two-phase-validation.md",
    "ccr-read-workaround.md",
    "cross-axis-analysis.md"
]

base = "/home/ty/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets/news/references"
for ref in refs:
    path = os.path.join(base, ref)
    if not os.path.exists(path):
        print(f"MISSING: {ref}")
        continue
    with open(path) as f:
        text = f.read()
    outdir = f"/tmp/ref_{ref.replace('.md','')}"
    os.makedirs(outdir, exist_ok=True)
    for i in range(0, len(text), 80):
        slug = f"chunk_{i:05d}"
        with open(os.path.join(outdir, f"{slug}.txt"), "w") as out:
            out.write(text[i:i+80])
    print(f"{ref}: {len(text)} bytes -> {outdir}/")