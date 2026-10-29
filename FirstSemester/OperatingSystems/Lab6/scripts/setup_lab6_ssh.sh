#!/usr/bin/env bash
set -e

echo "=== 1. Creating Banner ==="
cat > /etc/ssh/banner.txt << 'EOF'
************************************************************
*  National University "Lviv Polytechnic"                  *
*  Department of CAD - Operating Systems Lab #6            *
*  Authorized Access Only! Student: Lemishka Andriy PP-14  *
************************************************************
EOF

echo "=== 2. Setting SSH Server Configuration ==="
mkdir -p /etc/ssh/sshd_config.d
cat > /etc/ssh/sshd_config.d/lab6.conf << 'EOF'
Port 22
Banner /etc/ssh/banner.txt
PermitRootLogin no
PasswordAuthentication yes
PubkeyAuthentication yes
AllowUsers user remote_ws2
EOF

systemctl daemon-reload
systemctl restart ssh.socket
systemctl restart ssh.service 2>/dev/null || true

echo "=== 3. Ensuring Users and Passwords ==="
id remote_ws2 || useradd -m -s /bin/bash remote_ws2
echo "user:12345" | chpasswd
echo "remote_ws2:Lab6Remote2026!" | chpasswd

echo "=== 4. Setting Up SSH Keys ==="
su - user -c '
mkdir -p ~/.ssh && chmod 700 ~/.ssh
if [ ! -f ~/.ssh/id_rsa ]; then
    ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa -N "" -q
fi
cat ~/.ssh/id_rsa.pub > ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
'

echo "=== 5. Creating Sample Test Archive for SCP/SFTP ==="
su - user -c '
mkdir -p ~/lab6_project/src ~/lab6_project/docs
echo "echo Hello from Remote SSH Server" > ~/lab6_project/src/main.sh
echo "Lab 6: Remote Access in Linux Ubuntu 26.04" > ~/lab6_project/docs/readme.txt
tar -czf ~/backup_lab6.tar.gz -C ~/ lab6_project
ls -lh ~/backup_lab6.tar.gz
'

echo "=== 6. Status and Network ==="
ss -tulpn | grep 22
systemctl status ssh.socket --no-pager
echo "SETUP_SUCCESSFUL"
