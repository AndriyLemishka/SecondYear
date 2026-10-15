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

TAB = ['0f', '8f']
ENTER = ['1c', '9c']
ESC = ['01', '81']

# Focus is on Reservation name
type_text("Gateway")
send(TAB)

# IP address field (last octet)
type_text("4")
send(TAB)

# MAC address
type_text("1a2b3c4d5e6f")
send(TAB)

# Description
type_text("Gateway Reservation")
send(TAB)

print("Filled reservation dialog")
