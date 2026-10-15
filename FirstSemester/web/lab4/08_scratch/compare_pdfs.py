import pypdf

def get_page_info(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    res = []
    for i, page in enumerate(reader.pages):
        txt = page.extract_text()
        figs = []
        for n in range(1, 25):
            if f"Рисунок {n}" in txt or f"Рис. {n}" in txt:
                figs.append(f"Рис.{n}")
        headings = []
        for h in ["МЕТА", "ЗМІСТ", "ХІД РОБОТИ", "Розділ 1", "Розділ 2", "Розділ 3", "Промпт-паспорт", "Відповіді на контрольні", "Висновки", "Використані джерела"]:
            if h.lower() in txt.lower():
                headings.append(h)
        res.append((i+1, figs, headings))
    return res

ref_info = get_page_info(r'C:\Users\andri_gxiil3v\.gemini\antigravity\brain\8b923188-aa44-470c-a9a2-49b2c3b66742\.user_uploaded\media_1791471127621_e26a7f88.pdf')
our_info = get_page_info(r'd:\Studing\SecondYear\FirstSemester\web\lab4\07_report\Лемішка_ПП-24_Л4_ChargeUA.pdf')

print(f"{'Page':<5} | {'Reference Figures':<20} | {'Reference Headings':<25} | {'Our Figures':<20} | {'Our Headings':<25}")
print("-" * 105)
max_len = max(len(ref_info), len(our_info))
for p in range(1, max_len + 1):
    ref_f = ", ".join(ref_info[p-1][1]) if p <= len(ref_info) else "-"
    ref_h = ", ".join(ref_info[p-1][2]) if p <= len(ref_info) else "-"
    our_f = ", ".join(our_info[p-1][1]) if p <= len(our_info) else "-"
    our_h = ", ".join(our_info[p-1][2]) if p <= len(our_info) else "-"
    print(f"{p:<5} | {ref_f:<20} | {ref_h:<25} | {our_f:<20} | {our_h:<25}")
