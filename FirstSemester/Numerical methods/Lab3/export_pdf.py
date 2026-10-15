import base64
import subprocess

ps_script = """
$dir = "D:\\Studing\\SecondYear\\FirstSemester\\Numerical methods\\Lab3"
$files = Get-ChildItem -Path $dir -Filter "*.docx"
$target = $null
foreach ($f in $files) {
    if ($f.Name -match "Лемішка|ЛР3") {
        $target = $f
        break
    }
}
if ($null -eq $target) {
    Write-Output "DOCX not found"
    exit 1
}

$docPath = $target.FullName
$pdfPath = [System.IO.Path]::ChangeExtension($docPath, ".pdf")

$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $doc = $word.Documents.Open($docPath)
    $doc.SaveAs([ref]$pdfPath, [ref]17)
    $doc.Close()
    Write-Output "SUCCESS: $pdfPath"
} finally {
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
}
"""

encoded = base64.b64encode(ps_script.encode("utf-16le")).decode("ascii")
res = subprocess.run(["powershell", "-NoProfile", "-EncodedCommand", encoded], capture_output=True, text=True)
print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)
