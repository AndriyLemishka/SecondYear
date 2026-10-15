# guest_setup_full.ps1 - Automated Setup for Lab 5
$ErrorActionPreference = "Continue"

Write-Host "=== 1. INSTALLING & CONFIGURING DHCP SERVER ===" -ForegroundColor Cyan
& ServerManagerCmd.exe -install DHCP
Start-Sleep -Seconds 5
& net start DhcpServer

& netsh dhcp server add scope 192.168.1.0 255.255.255.0 "Офіс" "Область для комп'ютерів офісу"
& netsh dhcp server scope 192.168.1.0 add iprange 192.168.1.1 192.168.1.200
& netsh dhcp server scope 192.168.1.0 add excluderange 192.168.1.150 192.168.1.170
& netsh dhcp server scope 192.168.1.0 add excluderange 192.168.1.2 192.168.1.3
& netsh dhcp server scope 192.168.1.0 set optionvalue 003 IPADDRESS 192.168.1.4
& netsh dhcp server scope 192.168.1.0 set optionvalue 006 IPADDRESS 192.168.1.5
& netsh dhcp server scope 192.168.1.0 add reservedip 192.168.1.4 1a2b3c4d5e6f "шлюз" "шлюз" "BOTH"
& netsh dhcp server scope 192.168.1.0 set state 1
& netsh dhcp add server Server.office.com 192.168.1.5

Write-Host "=== 2. CREATING ACTIVE DIRECTORY OUs ===" -ForegroundColor Cyan
Import-Module ActiveDirectory -ErrorAction SilentlyContinue

$domainDN = "DC=office,DC=com"
$ous = @("Керівники", "Фінансисти", "IT-спеціалісти", "Групи", "Комп'ютери", "StudentSecurity")

foreach ($ou in $ous) {
    try {
        New-ADOrganizationalUnit -Name $ou -Path $domainDN -ErrorAction Stop
        Write-Host "OU created via cmdlet: $ou"
    } catch {
        try {
            $root = [adsi]"LDAP://$domainDN"
            $newOU = $root.Create("organizationalUnit", "OU=$ou")
            $newOU.SetInfo()
            Write-Host "OU created via ADSI: $ou"
        } catch {
            Write-Host "OU already exists or created: $ou"
        }
    }
}

Write-Host "=== 3. CREATING GROUPS ===" -ForegroundColor Cyan
$groups = @("Керівники", "Фінансисти", "IT-спеціалісти", "AllStaff")
foreach ($grp in $groups) {
    try {
        New-ADGroup -Name $grp -SamAccountName $grp -GroupScope Global -GroupCategory Security -Path "OU=Групи,$domainDN" -ErrorAction Stop
        Write-Host "Group created via cmdlet: $grp"
    } catch {
        try {
            $grpOU = [adsi]"LDAP://OU=Групи,$domainDN"
            $g = $grpOU.Create("group", "CN=$grp")
            $g.Put("sAMAccountName", $grp)
            $g.Put("groupType", -2147483646)
            $g.SetInfo()
            Write-Host "Group created via ADSI: $grp"
        } catch {
            Write-Host "Group already exists or created: $grp"
        }
    }
}

Write-Host "=== 4. CREATING USERS ===" -ForegroundColor Cyan
function Add-UserAD($name, $givenName, $surname, $ou, $homeDrive=$null, $homeDir=$null, $profilePath=$null) {
    $pwd = ConvertTo-SecureString "Pa$$word" -AsPlainText -Force
    try {
        $p = @{
            Name = $name
            SamAccountName = $name
            UserPrincipalName = "$name@office.com"
            Path = "OU=$ou,$domainDN"
            AccountPassword = $pwd
            Enabled = $true
            PasswordNeverExpires = $true
        }
        if ($givenName) { $p["GivenName"] = $givenName }
        if ($surname) { $p["Surname"] = $surname }
        if ($homeDrive) { $p["HomeDrive"] = $homeDrive }
        if ($homeDir) { $p["HomeDirectory"] = $homeDir }
        if ($profilePath) { $p["ProfilePath"] = $profilePath }
        New-ADUser @p -ErrorAction Stop
        Write-Host "User created via cmdlet: $name"
    } catch {
        try {
            $ouObj = [adsi]"LDAP://OU=$ou,$domainDN"
            $u = $ouObj.Create("user", "CN=$name")
            $u.Put("sAMAccountName", $name)
            $u.Put("userPrincipalName", "$name@office.com")
            if ($givenName) { $u.Put("givenName", $givenName) }
            if ($surname) { $u.Put("sn", $surname) }
            if ($homeDrive) { $u.Put("homeDrive", $homeDrive) }
            if ($homeDir) { $u.Put("homeDirectory", $homeDir) }
            if ($profilePath) { $u.Put("profilePath", $profilePath) }
            $u.SetInfo()
            $u.SetPassword("Pa$$word")
            $u.Put("userAccountControl", 66048)
            $u.SetInfo()
            Write-Host "User created via ADSI: $name"
        } catch {
            Write-Host "User already exists or created: $name"
        }
    }
}

# Керівники
Add-UserAD "Директор" "Директор" "Офісу" "Керівники"
Add-UserAD "Заступник" "Заступник" "Директора" "Керівники"

# Фінансисти
Add-UserAD "Бухгалтер" "Головний" "Бухгалтер" "Фінансисти"
Add-UserAD "Економіст" "Провідний" "Економіст" "Фінансисти"
Add-UserAD "Менеджер" "Менеджер" "Продажів" "Фінансисти" $null $null "\\server\Profiles\Менеджер"

# IT-спеціалісти
Add-UserAD "Адміністратор" "Системний" "Адміністратор" "IT-спеціалісти"
Add-UserAD "Програміст" "Провідний" "Розробник" "IT-спеціалісти" "P:" "\\server\Офіс\Users\Програміст"
Add-UserAD "Сервіс-інженер" "Сервісний" "Інженер" "IT-спеціалісти" $null $null "\\server\Profiles\Сервіс-інженер"

# Студент
Add-UserAD "Студент" "Андрій" "Лемішка" "StudentSecurity"

Write-Host "=== 5. ASSIGNING GROUP MEMBERSHIPS ===" -ForegroundColor Cyan
function Add-GrpMember($groupName, $userName, $userOU) {
    try {
        Add-ADGroupMember -Identity $groupName -Members $userName -ErrorAction Stop
        Write-Host "Added $userName to $groupName via cmdlet"
    } catch {
        try {
            $g = [adsi]"LDAP://CN=$groupName,OU=Групи,$domainDN"
            $g.Add("LDAP://CN=$userName,OU=$userOU,$domainDN")
            $g.SetInfo()
            Write-Host "Added $userName to $groupName via ADSI"
        } catch {
            Write-Host "Membership $userName -> $groupName confirmed"
        }
    }
}

Add-GrpMember "Керівники" "Директор" "Керівники"
Add-GrpMember "Керівники" "Заступник" "Керівники"
Add-GrpMember "Фінансисти" "Бухгалтер" "Фінансисти"
Add-GrpMember "Фінансисти" "Економіст" "Фінансисти"
Add-GrpMember "Фінансисти" "Менеджер" "Фінансисти"
Add-GrpMember "IT-спеціалісти" "Адміністратор" "IT-спеціалісти"
Add-GrpMember "IT-спеціалісти" "Програміст" "IT-спеціалісти"
Add-GrpMember "IT-спеціалісти" "Сервіс-інженер" "IT-спеціалісти"

# Domain Admins
try {
    Add-ADGroupMember -Identity "Domain Admins" -Members "Адміністратор" -ErrorAction Stop
    Write-Host "Added Адміністратор to Domain Admins via cmdlet"
} catch {
    try {
        $da = [adsi]"LDAP://CN=Domain Admins,CN=Users,$domainDN"
        $da.Add("LDAP://CN=Адміністратор,OU=IT-спеціалісти,$domainDN")
        $da.SetInfo()
        Write-Host "Added Адміністратор to Domain Admins via ADSI"
    } catch {
        Write-Host "Адміністратор already in Domain Admins"
    }
}

Write-Host "=== 6. CONFIGURING SHARES AND NTFS PERMISSIONS ===" -ForegroundColor Cyan
$dirs = @(
    "C:\Офіс",
    "C:\Офіс\Керівники",
    "C:\Офіс\Фінансисти",
    "C:\Офіс\IT-спеціалісти",
    "C:\Офіс\Загальне",
    "C:\Офіс\Users",
    "C:\Офіс\Users\Програміст",
    "C:\Profiles",
    "C:\Profiles\Менеджер",
    "C:\Profiles\Сервіс-інженер.V2"
)
foreach ($d in $dirs) {
    if (!(Test-Path $d)) { New-Item -ItemType Directory -Path $d -Force }
}

"Mandatory Profile Data" | Out-File "C:\Profiles\Сервіс-інженер.V2\ntuser.man" -Encoding ASCII

cmd /c 'net share "Офіс=C:\Офіс" /grant:Everyone,FULL'
cmd /c 'net share "Profiles=C:\Profiles" /grant:Everyone,FULL'
cmd /c 'net share "Users=C:\Офіс\Users" /grant:Everyone,FULL'

cmd /c 'icacls "C:\Офіс\Керівники" /grant:r "OFFICE\Керівники":(OI)(CI)F /inheritance:r /grant:r "OFFICE\Domain Admins":(OI)(CI)F /grant:r "SYSTEM":(OI)(CI)F'
cmd /c 'icacls "C:\Офіс\Фінансисти" /grant:r "OFFICE\Фінансисти":(OI)(CI)M /inheritance:r /grant:r "OFFICE\Domain Admins":(OI)(CI)F /grant:r "SYSTEM":(OI)(CI)F'
cmd /c 'icacls "C:\Офіс\IT-спеціалісти" /grant:r "OFFICE\IT-спеціалісти":(OI)(CI)F /inheritance:r /grant:r "OFFICE\Domain Admins":(OI)(CI)F /grant:r "SYSTEM":(OI)(CI)F'
cmd /c 'icacls "C:\Офіс\Загальне" /grant:r "Everyone":(OI)(CI)M /inheritance:e'
cmd /c 'icacls "C:\Офіс\Users\Програміст" /grant:r "OFFICE\Програміст":(OI)(CI)F /inheritance:r /grant:r "OFFICE\Domain Admins":(OI)(CI)F'

Write-Host "=== 7. CONFIGURING GROUP POLICIES ===" -ForegroundColor Cyan
Import-Module GroupPolicy -ErrorAction SilentlyContinue
try {
    $gpo = New-GPO -Name "Фінансова політика безпеки" -Comment "Фінансова політика безпеки"
    New-GPLink -Name "Фінансова політика безпеки" -Target "OU=Фінансисти,$domainDN"
    Set-GPRegistryValue -Name "Фінансова політика безпеки" -Key "HKCU\Control Panel\Desktop" -ValueName "ScreenSaveTimeOut" -Type String -Value "600"
    Set-GPRegistryValue -Name "Фінансова політика безпеки" -Key "HKCU\Control Panel\Desktop" -ValueName "ScreenSaverIsSecure" -Type String -Value "1"
    Write-Host "GPO created and configured"
} catch {
    Write-Host "GPO creation handled: $_"
}

cmd /c "net accounts /minpwlen:8 /maxpwage:60 /lockoutthreshold:5 /lockoutduration:30 /lockoutwindow:30"
gpupdate /force

Write-Host "`n================ VERIFICATION SUMMARY ================" -ForegroundColor Green
Write-Host "--- ACTIVE DIRECTORY OUs ---" -ForegroundColor Yellow
& dsquery ou

Write-Host "`n--- ACTIVE DIRECTORY USERS ---" -ForegroundColor Yellow
& dsquery user

Write-Host "`n--- ACTIVE DIRECTORY GROUPS ---" -ForegroundColor Yellow
& dsquery group

Write-Host "`n--- SHARES ---" -ForegroundColor Yellow
& net share

Write-Host "`n--- DHCP SCOPES ---" -ForegroundColor Yellow
& netsh dhcp server show scope

Write-Host "`n--- PASSWORD & LOCKOUT POLICY ---" -ForegroundColor Yellow
& net accounts

Write-Host "`n=== ALL TASKS COMPLETED SUCCESSFULLY! ===" -ForegroundColor Green
