import sys
import docx

sys.stdout.reconfigure(encoding='utf-8')
doc = docx.Document(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 3\Лемішка А_ПП-24_ЛР3.docx")
for i, p in enumerate(doc.paragraphs):
    has_img = any('graphic' in r._r.xml for r in p.runs)
    if has_img or 'Рис' in p.text:
        print(f"P{i}: [img={has_img}] '{p.text}'")
