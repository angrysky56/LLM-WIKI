import pymupdf, sys

paper_id = sys.argv[1] if len(sys.argv) > 1 else "2605.30322"
version = "v1"
pdf_path = f"/home/ty/Documents/paper-research/{paper_id}{version}.pdf"
txt_path = f"/home/ty/Documents/paper-research/{paper_id}{version}.txt"

doc = pymupdf.open(pdf_path)
text = "\n".join(page.get_text() for page in doc)
with open(txt_path, "w") as f:
    f.write(text)
print(f"Extracted {len(text)} chars from {paper_id}")
print(f"First 2000 chars:\n{text[:2000]}")