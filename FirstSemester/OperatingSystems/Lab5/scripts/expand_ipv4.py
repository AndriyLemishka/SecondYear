import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

DOWN = ['e0', '50', 'e0', 'd0']
UP = ['e0', '48', 'e0', 'c8']
RIGHT = ['e0', '4d', 'e0', 'cd']

# In current_screen.png, server.office.com is selected in the tree.
# Down once selects IPv4
send_scancodes(DOWN)
time.sleep(0.3)

# Expand IPv4
send_scancodes(RIGHT)
time.sleep(0.5)

# Down once selects Scope [192.168.1.0] Офіс
send_scancodes(DOWN)
time.sleep(0.3)

# Expand Scope
send_scancodes(RIGHT)
time.sleep(0.5)

# Down once selects Address Pool
send_scancodes(DOWN)
time.sleep(0.5)

print("Expanded IPv4 and Scope to Address Pool")
