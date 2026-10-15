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

ALT_I = ['38', '17', '97', 'b8']
ALT_A = ['38', '1e', '9e', 'b8']
ESC = ['01', '81']

# Jump to IP address (Alt+I)
send(ALT_I)
# In IP address, let's type 192.168.1.4
type_text("192.168.1.4")
time.sleep(0.4)

print("Fixed reservation IP")
