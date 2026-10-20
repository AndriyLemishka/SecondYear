$docx = "D:\Studing\SecondYear\FirstSemester\web\lab5\07_report\Покрокова_інструкція_хід_роботи_Лаб5.docx"
$pdf  = "D:\Studing\SecondYear\FirstSemester\web\lab5\07_report\Покрокова_інструкція_хід_роботи_Лаб5.pdf"

Write-Host "Converting DOCX to PDF..."
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

$rootPdf  = "D:\Studing\SecondYear\FirstSemester\web\lab5\Покрокова_інструкція_хід_роботи_Лаб5.pdf"
Copy-Item -Path $pdf -Destination $rootPdf -Force

Get-Item $pdf, $rootPdf | Select-Object FullName, Length
