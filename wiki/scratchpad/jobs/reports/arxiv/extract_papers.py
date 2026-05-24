import pymupdf

papers = [
    ("2605.22821v1", "Tokenisation via Convex Relaxations"),
    ("2605.22816v1", "AwareVLN: Reasoning with Self-awareness for Vision-Language Navigation"),
    ("2605.22763v1", "Advancing Mathematics Research with AI-Driven Formal Proof Search"),
]

for arxiv_id, title in papers:
    path = f"/home/ty/Documents/paper-research/{arxiv_id}.pdf"
    txt_path = f"/home/ty/Documents/paper-research/{arxiv_id}.txt"
    try:
        doc = pymupdf.open(path)
        text = "\n".join(page.get_text() for page in doc)
        with open(txt_path, "w") as f:
            f.write(text[:10000])
        print(f"OK: {arxiv_id} — {len(text)} chars")
    except Exception as e:
        print(f"ERROR {arxiv_id}: {e}")