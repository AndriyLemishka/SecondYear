
 = 'D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\reports'
 = (Get-ChildItem -Path  -Filter '*5.docx' | Where-Object { .Length -gt 3000000 }).FullName
 = [System.IO.Path]::ChangeExtension(, 'pdf')

Write-Host 'Found DOCX:' 
Write-Host 'Output PDF:' 

 = New-Object -ComObject Word.Application
.Visible = False
try {
     = .Documents.Open(, False, True)
    .SaveAs([ref], [ref]17)
    .Close(False)
    Write-Host 'PDF generated successfully!'
} finally {
    .Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject() | Out-Null
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
}

 = 'D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\' + [System.IO.Path]::GetFileName()
  = 'D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\' + [System.IO.Path]::GetFileName()

Copy-Item -Path  -Destination  -Force
Copy-Item -Path  -Destination  -Force

Get-Item  | Select-Object Name, Length, LastWriteTime
