$item = Get-ChildItem -Path "D:\Studing\SecondYear\FirstSemester\Numerical methods\Lab3" -Filter "*ЛР3*.docx" | Select-Object -First 1
if ($null -eq $item) {
    Write-Output "DOCX file not found"
    exit 1
}

$docPath = $item.FullName
$pdfPath = [System.IO.Path]::ChangeExtension($docPath, ".pdf")

try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $doc = $word.Documents.Open($docPath)
    $doc.SaveAs([ref]$pdfPath, [ref]17)
    $doc.Close()
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
    Write-Output "PDF generated successfully: $pdfPath"
} catch {
    Write-Output "Error: $($_.Exception.Message)"
}
