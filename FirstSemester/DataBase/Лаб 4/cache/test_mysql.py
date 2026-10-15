import subprocess

passwords = ['', 'root', '1234', '12345', '123456', '12345678', 'password', 'admin', 'mysql', 'lemishka', 'pp24', '1111', 'qwerty', 'Root1234!', 'Root123!']
mysql_path = r'C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe'

found = False
for p in passwords:
    cmd = [mysql_path, '-u', 'root']
    if p:
        cmd.append(f'-p{p}')
    cmd.extend(['-e', 'SHOW DATABASES;'])
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f'SUCCESS! Password is: "{p}"')
        print(res.stdout)
        found = True
        break

if not found:
    print('Password not found in test list.')
