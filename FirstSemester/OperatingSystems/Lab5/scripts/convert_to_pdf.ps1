$docxPath = "D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\reports\Покрокова_інструкція_натискань_Лаб5.docx"
$pdfPath  = "D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\reports\Покрокова_інструкція_натискань_Лаб5.pdf"

Write-Host "Initializing Word COM object..."
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = [Microsoft.Office.Interop.Word.WdAlertLevel]::wdAlertsNone

try {
    Write-Host "Opening document: $docxPath"
    $doc = $word.Documents.Open($docxPath, $false, $true)
    Write-Host "Saving as PDF: $pdfPath"
    $doc.SaveAs([ref]$pdfPath, [ref]17)
    $doc.Close($false)
    Write-Host "Conversion completed successfully!"
} catch {
    Write-Error $_.Exception.Message
} finally {
    $word.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
}

$rootDocx = "D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\Покрокова_інструкція_натискань_Лаб5.docx"
$rootPdf  = "D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\Покрокова_інструкція_натискань_Лаб5.pdf"

Copy-Item -Path $docxPath -Destination $rootDocx -Force
Copy-Item -Path $pdfPath -Destination $rootPdf -Force

Write-Host "Files updated in root directory as well."
Get-Item $pdfPath | Select-Object Name, Length, LastWriteTime
