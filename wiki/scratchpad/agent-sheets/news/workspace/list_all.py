import os
d = "/home/ty/Documents/LLM-WIKI/wiki/sources/news/2026"
files = sorted(os.listdir(d))
lines = []
for f in files:
    lines.append(f)
out = "\n".join(lines)
os.makedirs("/tmp/allfiles", exist_ok=True)
for i in range(0, len(out), 78):
    with open(f"/tmp/allfiles/chunk_{i:05d}.txt", "w") as f:
        f.write(out[i:i+78])
print(f"{len(lines)} files")