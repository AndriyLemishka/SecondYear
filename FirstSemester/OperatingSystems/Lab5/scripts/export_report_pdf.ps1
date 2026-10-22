
$docx = "D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\reports\Лемішка_ПП_14_Лаб_5.docx"
$pdf  = "D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\reports\Лемішка_ПП_14_Лаб_5.pdf"

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

$rootDocx = "D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\Лемішка_ПП_14_Лаб_5.docx"
$rootPdf  = "D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\Лемішка_ПП_14_Лаб_5.pdf"

try {
    Copy-Item -Path $docx -Destination $rootDocx -Force
    Copy-Item -Path $pdf -Destination $rootPdf -Force
    Write-Host "Copied to root successfully."
} catch {
    Write-Host "Note: root copy locked, reports/ is canonical."
}

Get-Item $pdf | Select-Object Name, Length, LastWriteTime
