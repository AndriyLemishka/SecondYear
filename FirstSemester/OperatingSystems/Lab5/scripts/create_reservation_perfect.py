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

ALT_A = ['38', '1e', '9e', 'b8']
ALT_C = ['38', '2e', 'ae', 'b8']
ENTER = ['1c', '9c']
TAB = ['0f', '8f']

# 1. Open New Reservation dialog (Alt+A then Enter)
send(ALT_A, sleep_after=0.4)
send(ENTER, sleep_after=1.0)

# 2. Type Reservation name
type_text("Gateway")
send(TAB)

# 3. In IP address, cursor is in 4th octet, type '4'
type_text("4")
send(TAB)

# 4. MAC address
type_text("1a2b3c4d5e6f")
send(TAB)

# 5. Description
type_text("Gateway Reservation")
time.sleep(0.5)

print("Filled reservation fields")
