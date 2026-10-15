import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

DOWN = ['e0', '50', 'e0', 'd0']
ALT_A = ['38', '1e', '9e', 'b8']

# Down to server.office.com
send_scancodes(DOWN)
time.sleep(0.3)

# Alt+A for Action menu
send_scancodes(ALT_A)
time.sleep(0.5)

print("Opened Action menu on server.office.com")
