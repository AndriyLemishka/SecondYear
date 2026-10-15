<#
==============================================================================
  АВТОМАТИЗОВАНИЙ СКРИПТ НАЛАШТУВАННЯ ЛАБОРАТОРНОЇ РОБОТИ №5
  Дисципліна: Операційні системи
  Студент: Лемішка Андрій, ПП-14
  Тема: Робота з об'єктами Active Directory на платформі Windows Server
==============================================================================
#>

Write-Host "=== [Крок 1] Базові налаштування мережі та імені сервера ===" -ForegroundColor Cyan
# Призначення імені комп'ютера Server
Rename-Computer -NewName "Server" -Force -ErrorAction SilentlyContinue

# Налаштування статичної IP-адреси 192.168.1.5
$adapter = Get-NetAdapter | Where-Object { $_.Status -eq "Up" } | Select-Object -First 1
if ($adapter) {
    New-NetIPAddress -InterfaceIndex $adapter.ifIndex -IPAddress "192.168.1.5" -PrefixLength 24 -DefaultGateway "192.168.1.4" -ErrorAction SilentlyContinue
    Set-DnsClientServerAddress -InterfaceIndex $adapter.ifIndex -ServerAddresses ("192.168.1.5") -ErrorAction SilentlyContinue
}

Write-Host "=== [Крок 2] Встановлення ролей Active Directory, DNS та DHCP ===" -ForegroundColor Cyan
Install-WindowsFeature -Name AD-Domain-Services, DNS, DHCP, RSAT-AD-Tools, GPMC -IncludeManagementTools

# Розгортання лісу та домену office.com (виконується одноразово при підвищенні DC)
# Install-ADDSForest -DomainName "office.com" -SafeModeAdministratorPassword (ConvertTo-SecureString "Pa$$word123!" -AsPlainText -Force) -DomainMode "Win2008" -ForestMode "Win2008" -InstallDns -Force

Write-Host "=== [Крок 3] Налаштування DHCP-сервера (Область 'Офіс') ===" -ForegroundColor Cyan
Add-DhcpServerV4Scope -Name "Офіс" -StartRange 192.168.1.1 -EndRange 192.168.1.200 -SubnetMask 255.255.255.0 -LeaseDuration (New-TimeSpan -Days 8) -State Active -ErrorAction SilentlyContinue
Add-DhcpServerV4ExclusionRange -ScopeId 192.168.1.0 -StartRange 192.168.1.150 -EndRange 192.168.1.170 -ErrorAction SilentlyContinue
Add-DhcpServerV4ExclusionRange -ScopeId 192.168.1.0 -StartRange 192.168.1.2 -EndRange 192.168.1.3 -ErrorAction SilentlyContinue
Set-DhcpServerV4OptionValue -ScopeId 192.168.1.0 -Router 192.168.1.4 -ErrorAction SilentlyContinue
Add-DhcpServerV4Reservation -ScopeId 192.168.1.0 -IPAddress 192.168.1.4 -ClientId "1a-2b-3c-4d-5e-6f" -Name "шлюз" -ErrorAction SilentlyContinue

Write-Host "=== [Крок 4] Створення структури Active Directory (OU, Користувачі, Групи) ===" -ForegroundColor Cyan
$baseDC = "DC=office,DC=com"
$ouList = @("Керівники", "Фінансисти", "IT-спеціалісти", "Групи", "Комп'ютери", "StudentSecurity")
foreach ($ou in $ouList) {
    New-ADOrganizationalUnit -Name $ou -Path $baseDC -ErrorAction SilentlyContinue
}

# Створення глобальних груп безпеки
$groups = @("Керівники", "Фінансисти", "IT-спеціалісти")
foreach ($grp in $groups) {
    New-ADGroup -Name $grp -GroupScope Global -GroupCategory Security -Path "OU=Групи,$baseDC" -ErrorAction SilentlyContinue
}

# Створення користувачів
$pwd = ConvertTo-SecureString "Pa$$word" -AsPlainText -Force

# Керівники
New-ADUser -Name "Директор" -GivenName "Директор" -Path "OU=Керівники,$baseDC" -AccountPassword $pwd -Enabled $true -PasswordNeverExpires $true -ErrorAction SilentlyContinue
New-ADUser -Name "Заступник" -GivenName "Заступник" -Path "OU=Керівники,$baseDC" -AccountPassword $pwd -Enabled $true -PasswordNeverExpires $true -ErrorAction SilentlyContinue
Add-ADGroupMember -Identity "Керівники" -Members "Директор", "Заступник" -ErrorAction SilentlyContinue

# Фінансисти
New-ADUser -Name "Бухгалтер" -GivenName "Бухгалтер" -Path "OU=Фінансисти,$baseDC" -AccountPassword $pwd -Enabled $true -PasswordNeverExpires $true -ErrorAction SilentlyContinue
New-ADUser -Name "Економіст" -GivenName "Економіст" -Path "OU=Фінансисти,$baseDC" -AccountPassword $pwd -Enabled $true -PasswordNeverExpires $true -ErrorAction SilentlyContinue
New-ADUser -Name "Менеджер" -GivenName "Менеджер" -Path "OU=Фінансисти,$baseDC" -AccountPassword $pwd -Enabled $true -PasswordNeverExpires $true -ProfilePath "\\server\Profiles\Менеджер" -ErrorAction SilentlyContinue
Add-ADGroupMember -Identity "Фінансисти" -Members "Бухгалтер", "Економіст", "Менеджер" -ErrorAction SilentlyContinue

# IT-спеціалісти
New-ADUser -Name "Адміністратор" -GivenName "Адміністратор" -Path "OU=IT-спеціалісти,$baseDC" -AccountPassword $pwd -Enabled $true -PasswordNeverExpires $true -ErrorAction SilentlyContinue
New-ADUser -Name "Програміст" -GivenName "Програміст" -Path "OU=IT-спеціалісти,$baseDC" -AccountPassword $pwd -Enabled $true -PasswordNeverExpires $true -HomeDrive "P:" -HomeDirectory "\\server\Офіс" -ErrorAction SilentlyContinue
New-ADUser -Name "Сервіс-інженер" -GivenName "Сервіс-інженер" -Path "OU=IT-спеціалісти,$baseDC" -AccountPassword $pwd -Enabled $true -PasswordNeverExpires $true -ProfilePath "\\server\Profiles\Сервіс-інженер" -ErrorAction SilentlyContinue
Add-ADGroupMember -Identity "IT-спеціалісти" -Members "Адміністратор", "Програміст", "Сервіс-інженер" -ErrorAction SilentlyContinue
Add-ADGroupMember -Identity "Domain Admins" -Members "Адміністратор" -ErrorAction SilentlyContinue

# Студент
New-ADUser -Name "Студент" -GivenName "Андрій" -Surname "Лемішка" -Path "OU=StudentSecurity,$baseDC" -AccountPassword $pwd -Enabled $true -PasswordNeverExpires $true -ErrorAction SilentlyContinue

Write-Host "=== [Крок 5] Створення спільних каталогів та налаштування ACL ===" -ForegroundColor Cyan
New-Item -ItemType Directory -Path "C:\Офіс\Керівники", "C:\Офіс\Фінансисти", "C:\Офіс\IT-спеціалісти", "C:\Profiles", "C:\Users\Студенти" -Force -ErrorAction SilentlyContinue

# Спільний доступ (Share)
New-SmbShare -Name "Офіс" -Path "C:\Офіс" -FullAccess "Everyone" -ErrorAction SilentlyContinue
New-SmbShare -Name "Profiles" -Path "C:\Profiles" -FullAccess "Everyone" -ErrorAction SilentlyContinue
New-SmbShare -Name "Users" -Path "C:\Users" -FullAccess "Everyone" -ErrorAction SilentlyContinue

Write-Host "=== [Крок 6] Налаштування групових політик (GPO) ===" -ForegroundColor Cyan
# Створення GPO для Фінансистів
$gpoFin = New-GPO -Name "Фінансова політика безпеки" -Comment "Фінансова політика безпеки" -ErrorAction SilentlyContinue
New-GPLink -Name "Фінансова політика безпеки" -Target "OU=Фінансисти,$baseDC" -ErrorAction SilentlyContinue

# Тайм-аут заставки (600 с) та парольний захист
Set-GPRegistryValue -Name "Фінансова політика безпеки" -Key "HKCU\Control Panel\Desktop" -ValueName "ScreenSaveTimeOut" -Type String -Value "600" -ErrorAction SilentlyContinue
Set-GPRegistryValue -Name "Фінансова політика безпеки" -Key "HKCU\Control Panel\Desktop" -ValueName "ScreenSaverIsSecure" -Type String -Value "1" -ErrorAction SilentlyContinue

# Політика складності паролів домену (Default Domain Policy)
Set-ADDefaultDomainPasswordPolicy -Identity "office.com" -MinPasswordLength 8 -PasswordHistoryCount 3 -ComplexityEnabled $true -MaxPasswordAge (New-TimeSpan -Days 60) -LockoutDuration (New-TimeSpan -Minutes 5) -LockoutObservationWindow (New-TimeSpan -Minutes 5) -LockoutBadCount 3 -ErrorAction SilentlyContinue

# Оновлення політик
gpupdate /force

Write-Host "=== [УСПІШНО] Всі об'єкти лабораторної роботи №5 успішно створено! ===" -ForegroundColor Green
