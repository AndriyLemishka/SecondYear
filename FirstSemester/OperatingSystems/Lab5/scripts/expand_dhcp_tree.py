import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

DOWN = ['e0', '50', 'e0', 'd0']
RIGHT = ['e0', '4d', 'e0', 'cd']

# Tree currently at DHCP root
# Down to server.office.com
send_scancodes(DOWN)
time.sleep(0.3)

# Right to expand server.office.com
send_scancodes(RIGHT)
time.sleep(0.5)

# Down to IPv4
send_scancodes(DOWN)
time.sleep(0.3)

# Right to expand IPv4
send_scancodes(RIGHT)
time.sleep(0.5)

# Down to Scope [192.168.1.0]
send_scancodes(DOWN)
time.sleep(0.3)

# Right to expand Scope
send_scancodes(RIGHT)
time.sleep(0.5)

# Down to Address Pool
send_scancodes(DOWN)
time.sleep(0.3)

print("Expanded DHCP tree to Address Pool")
