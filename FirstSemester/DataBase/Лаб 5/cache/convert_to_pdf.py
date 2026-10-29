import os
import subprocess

docx_file = os.path.abspath(r"Лаб 5\Лемішка А_ПП-24_ЛР5.docx")
out_dir = os.path.abspath(r"Лаб 5")
pdf_file = os.path.join(out_dir, "Лемішка А_ПП-24_ЛР5.pdf")

converted = False
try:
    import win32com.client
    print("Attempting conversion via Microsoft Word COM...")
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    doc = word.Documents.Open(docx_file)
    doc.SaveAs(pdf_file, FileFormat=17) # 17 = wdFormatPDF
    doc.Close()
    word.Quit()
    print("Successfully converted via MS Word!")
    converted = True
except Exception as e:
    print("MS Word failed:", e)

if not converted:
    print("Attempting conversion via LibreOffice headless...")
    cmd = f'soffice --headless --convert-to pdf "{docx_file}" --outdir "{out_dir}"'
    subprocess.run(cmd, shell=True, check=True)
    print("Successfully converted via LibreOffice!")

if os.path.exists(pdf_file):
    print(f"PDF verified: {pdf_file} ({os.path.getsize(pdf_file)} bytes)")
else:
    print("PDF was not created.")
