import time
import subprocess
from send_keys import text_to_scancodes

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send(codes, sleep_after=0.2):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)
    time.sleep(sleep_after)

def type_text(text, sleep_after=0.2):
    codes = text_to_scancodes(text)
    if codes:
        send(codes, sleep_after=sleep_after)

SHIFT_TAB = ['2a', '0f', '8f', 'aa']
BACKSPACE = ['0e', '8e']
LEFT = ['e0', '4b', 'e0', 'cb']

# Shift+Tab 3 times to get to IP address
for _ in range(3):
    send(SHIFT_TAB)

# In IP address, move all the way left
for _ in range(5):
    send(LEFT)

# Erase whatever is in octet 1
for _ in range(4):
    send(BACKSPACE)

type_text("192.")
type_text("168.")
type_text("1.")
type_text("4")

print("Set IP address to 192.168.1.4")
