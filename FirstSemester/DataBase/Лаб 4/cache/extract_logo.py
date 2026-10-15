from PIL import Image
import docx

doc = docx.Document(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 3\Лемішка А_ПП-24_ЛР3.docx")
blob = doc.part.rels['rId6'].target_part.blob
with open(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\logo_lp.png", "wb") as f:
    f.write(blob)
im = Image.open(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\logo_lp.png")
print("Logo size:", im.size)
