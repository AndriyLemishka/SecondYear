import pypdf

reader = pypdf.PdfReader(r'C:\Users\andri_gxiil3v\.gemini\antigravity\brain\8b923188-aa44-470c-a9a2-49b2c3b66742\.user_uploaded\media_1791471127621_e26a7f88.pdf')
with open('lab4/08_scratch/reference_all_pages.txt', 'w', encoding='utf-8') as f:
    for i, p in enumerate(reader.pages):
        f.write(f"\n{'='*30} PAGE {i+1} {'='*30}\n")
        f.write(p.extract_text() + "\n")
print(f"Dumped {len(reader.pages)} pages.")
