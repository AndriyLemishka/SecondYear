import time
import subprocess
from send_keys import text_to_scancodes

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

SHIFT_TAB = ['2a', '0f', '8f', 'aa']
TAB = ['0f', '8f']
CTRL_A = ['1d', '1e', '9e', '9d']
UP = ['e0', '48', 'e0', 'c8']
ENTER = ['1c', '9c']

# 1. Shift+Tab once to Parent domain
send_scancodes(SHIFT_TAB)
time.sleep(0.3)
send_scancodes(CTRL_A)
time.sleep(0.2)
send_scancodes(text_to_scancodes("office.com"))
time.sleep(0.3)

# 2. Tab to Server name (1), Tab to IP address (2), Tab to Add (3), Tab to list (4)
for i in range(4):
    send_scancodes(TAB)
    time.sleep(0.15)

# 3. Select 127.0.0.1 in list (Up arrow)
send_scancodes(UP)
time.sleep(0.3)

# 4. Tab to Remove button (1)
send_scancodes(TAB)
time.sleep(0.2)
# Click Remove
send_scancodes(ENTER)
time.sleep(0.5)

print("Parent domain office.com and removed 127.0.0.1")
