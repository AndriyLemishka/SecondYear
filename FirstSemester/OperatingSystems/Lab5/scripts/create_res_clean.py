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

ALT_C = ['38', '2e', 'ae', 'b8']
ALT_A = ['38', '1e', '9e', 'b8']
ENTER = ['1c', '9c']
TAB = ['0f', '8f']

# 1. Close current dialog with Alt+C
send(ALT_C, sleep_after=0.5)

# 2. Reopen New Reservation dialog
send(ALT_A, sleep_after=0.4)
send(ENTER, sleep_after=1.0)

# 3. Type name
type_text("Gateway", sleep_after=0.3)
send(TAB, sleep_after=0.2)

# 4. Type full IP with dots
type_text("192.168.1.4", sleep_after=0.4)
send(TAB, sleep_after=0.2)

# 5. Type MAC address
type_text("1a2b3c4d5e6f", sleep_after=0.3)
send(TAB, sleep_after=0.2)

# 6. Type Description
type_text("Gateway Reservation", sleep_after=0.3)

print("Filled clean reservation")
