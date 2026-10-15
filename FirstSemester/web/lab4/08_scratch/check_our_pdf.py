import pypdf

pdf_path = r'd:\Studing\SecondYear\FirstSemester\web\lab4\07_report\Лемішка_ПП-24_Л4_ChargeUA.pdf'
reader = pypdf.PdfReader(pdf_path)
print(f"Total pages in our PDF: {len(reader.pages)}")
for i, page in enumerate(reader.pages):
    txt = page.extract_text()
    matching = []
    for n in range(1, 25):
        if f"Рисунок {n}" in txt:
            matching.append(f"Рисунок {n}")
    print(f"Page {i+1}: {', '.join(matching) if matching else '(no figure caption)'}")
