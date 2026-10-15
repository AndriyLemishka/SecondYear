import time
import subprocess
from send_keys import text_to_scancodes

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send(codes, sleep_after=0.3):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)
    time.sleep(sleep_after)

def type_text(text, sleep_after=0.2):
    codes = text_to_scancodes(text)
    if codes:
        send(codes, sleep_after=sleep_after)

ALT_R = ['38', '13', '93', 'b8']
ALT_I = ['38', '17', '97', 'b8']
ALT_A = ['38', '1e', '9e', 'b8']
SHIFT_TAB = ['2a', '0f', '8f', 'aa']
TAB = ['0f', '8f']
DOWN = ['e0', '50', 'e0', 'd0']
CTRL_A = ['1d', '1e', '9e', '9d']
ENTER = ['1c', '9c']

# 1. Remove 127.0.0.1
send(ALT_R, sleep_after=0.4)

# 2. Jump to IP address (Alt+I)
send(ALT_I, sleep_after=0.3)
type_text("192.168.1.5", sleep_after=0.3)

# 3. Add (Alt+A)
send(ALT_A, sleep_after=2.0) # wait validation

# 4. Jump back to Available Options list
# Alt+O is "Available Options" hotkey!
ALT_O = ['38', '18', '98', 'b8']
send(ALT_O, sleep_after=0.3)

# Move down 9 times from 006 to 015
for _ in range(9):
    send(DOWN, sleep_after=0.15)

# Tab to String value
send(TAB, sleep_after=0.2)
send(CTRL_A, sleep_after=0.2)
type_text("office.com", sleep_after=0.3)

# Click OK
send(ENTER, sleep_after=1.0)

print("Scope Options 006 and 015 fixed cleanly!")
