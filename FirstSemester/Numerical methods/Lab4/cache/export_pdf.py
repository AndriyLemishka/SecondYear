import os
import base64
import subprocess

def export_to_pdf():
    docx_file = os.path.abspath(os.path.join("Lab4", "Лемішка_Андрій_ЛР4_ПП24.docx"))
    pdf_file = os.path.abspath(os.path.join("Lab4", "Лемішка_Андрій_ЛР4_ПП24.pdf"))

    if not os.path.exists(docx_file):
        print(f"Error: {docx_file} does not exist")
        return

    ps_script = f"""
    $docPath = "{docx_file}"
    $pdfPath = "{pdf_file}"

    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    try {{
        $doc = $word.Documents.Open($docPath)
        $doc.SaveAs([ref]$pdfPath, [ref]17)
        $doc.Close()
        Write-Output "SUCCESS: $pdfPath"
    }} finally {{
        $word.Quit()
        [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
    }}
    """

    encoded = base64.b64encode(ps_script.encode("utf-16le")).decode("ascii")
    res = subprocess.run(["powershell", "-NoProfile", "-EncodedCommand", encoded], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)

if __name__ == "__main__":
    export_to_pdf()
