import os
for d in ["/home/ty/Documents/LLM-WIKI/wiki/sources/news/2026", "/home/ty/Documents/LLM-WIKI/Clippings/articles/2026"]:
    print(f"\n=== {d} ===")
    if os.path.isdir(d):
        files = sorted(os.listdir(d))[-20:]
        for f in files:
            print(f"  {f}")
    else:
        print("  (does not exist)")