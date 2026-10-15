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
RIGHT = ['e0', '4d', 'e0', 'cd']
LEFT = ['e0', '4b', 'e0', 'cb']

# Focus is in Description.
# Shift+Tab twice to IP address
send(SHIFT_TAB)
send(SHIFT_TAB)

# Move to octet 1
send(LEFT)
send(LEFT)
send(LEFT)

# Erase the '4' and type '192'
send(BACKSPACE)
type_text("192")

# Move to octet 4
send(RIGHT)
send(RIGHT)
send(RIGHT)

# Type '4' in octet 4
type_text("4")

print("Fixed IP address to 192.168.1.4")
