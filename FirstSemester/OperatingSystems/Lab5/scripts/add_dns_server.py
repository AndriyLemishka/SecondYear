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
ALT_R = ['38', '13', '93', 'b8']
ENTER = ['1c', '9c']

# Focus is on IP address field
send_scancodes(text_to_scancodes("192.168.1.5"))
time.sleep(0.3)

# Click Add (Alt+A)
send_scancodes(ALT_A)
time.sleep(0.8)

# Tab to list box
send_scancodes(TAB)
time.sleep(0.3)

# Remove 127.0.0.1 (Alt+R)
send_scancodes(ALT_R)
time.sleep(0.5)

print("Configured DNS Server 192.168.1.5")
