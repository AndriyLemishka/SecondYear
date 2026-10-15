net user Student Paword /add
net localgroup administrators Student /add
reg add "HKLM\SYSTEM\Setup" /v SetupType /t REG_DWORD /d 0 /f
reg add "HKLM\SYSTEM\Setup" /v OOBEInProgress /t REG_DWORD /d 0 /f
reg add "HKLM\SYSTEM\Setup" /v SetupPhase /t REG_DWORD /d 0 /f
shutdown /r /t 0
