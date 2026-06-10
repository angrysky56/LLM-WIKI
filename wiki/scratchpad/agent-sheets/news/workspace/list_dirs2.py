import os
lines = []
for d in ["wiki/sources/news/2026", "Clippings/articles/2026"]:
    full = f"/home/ty/Documents/LLM-WIKI/{d}"
    lines.append(f"\n=== {d} ===")
    if os.path.isdir(full):
        files = sorted(os.listdir(full))[-20:]
        for f in files:
            lines.append(f"  {f}")
    else:
        lines.append("  (does not exist)")
out = "\n".join(lines)
os.makedirs("/tmp/dirlist", exist_ok=True)
for i in range(0, len(out), 78):
    with open(f"/tmp/dirlist/chunk_{i:05d}.txt", "w") as f:
        f.write(out[i:i+78])
print(f"done: {len(out)} chars")