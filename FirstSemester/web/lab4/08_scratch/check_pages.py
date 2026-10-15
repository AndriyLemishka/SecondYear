import pypdf

pdf_path = r'C:\Users\andri_gxiil3v\.gemini\antigravity\brain\8b923188-aa44-470c-a9a2-49b2c3b66742\.user_uploaded\media_1791471127621_e26a7f88.pdf'
reader = pypdf.PdfReader(pdf_path)
print(f"Total pages in reference: {len(reader.pages)}")
for i, page in enumerate(reader.pages):
    txt = page.extract_text()
    figs = [f"Рисунок {n}" for n in range(1, 25) if f"Рисунок {n}" in txt or f"рисунк" in txt and str(n) in txt]
    matching = []
    for n in range(1, 25):
        if f"Рисунок {n}" in txt:
            matching.append(f"Рисунок {n}")
    if matching:
        print(f"Page {i+1}: {', '.join(matching)}")
