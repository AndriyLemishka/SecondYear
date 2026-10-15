import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

SHIFT_TAB = ['2a', '0f', '8f', 'aa']
UP = ['e0', '48', 'e0', 'c8']

# Send Shift+Tab to move from column header to left tree
send_scancodes(SHIFT_TAB)
time.sleep(0.3)

# Press Up 8 times to navigate to IT-спеціалісти
for i in range(8):
    send_scancodes(UP)
    time.sleep(0.2)

print("Shift-tabbed to tree and pressed Up 8 times")
