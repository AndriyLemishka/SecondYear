
$reportsDir = "D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\reports"
$docx = (Get-ChildItem -Path $reportsDir -Filter "*5.docx" | Where-Object { $_.Length -gt 3000000 }).FullName
$pdf = [System.IO.Path]::ChangeExtension($docx, "pdf")

Write-Host "DOCX source:" $docx
Write-Host "PDF target:" $pdf

$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $doc = $word.Documents.Open($docx, $false, $true)
    $doc.SaveAs([ref]$pdf, [ref]17)
    $doc.Close($false)
    Write-Host "PDF exported successfully!"
} catch {
    Write-Error $_.Exception.Message
} finally {
    $word.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
}

$rootDocx = "D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\" + [System.IO.Path]::GetFileName($docx)
$rootPdf  = "D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\" + [System.IO.Path]::GetFileName($pdf)

Copy-Item -Path $docx -Destination $rootDocx -Force
Copy-Item -Path $pdf -Destination $rootPdf -Force

Get-Item $pdf | Select-Object Name, Length, LastWriteTime
