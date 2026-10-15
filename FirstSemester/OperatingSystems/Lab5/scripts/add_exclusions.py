import time
import subprocess
from send_keys import text_to_scancodes

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

TAB = ['0f', '8f']
ALT_A = ['38', '1e', '9e', 'b8']

# Focus is currently on Start IP address
# Exclusion 1: 192.168.1.150 to 192.168.1.170
send_scancodes(text_to_scancodes("192.168.1.150"))
time.sleep(0.3)
send_scancodes(TAB)
time.sleep(0.2)
send_scancodes(text_to_scancodes("192.168.1.170"))
time.sleep(0.3)
# Click Add (Alt+A)
send_scancodes(ALT_A)
time.sleep(0.5)

# Focus moves back to Start IP address or we can type next
# Exclusion 2: 192.168.1.2 to 192.168.1.3
send_scancodes(text_to_scancodes("192.168.1.2"))
time.sleep(0.3)
send_scancodes(TAB)
time.sleep(0.2)
send_scancodes(text_to_scancodes("192.168.1.3"))
time.sleep(0.3)
# Click Add (Alt+A)
send_scancodes(ALT_A)
time.sleep(0.5)

print("Added exclusions")
