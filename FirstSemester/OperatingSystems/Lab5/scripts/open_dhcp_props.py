import time
import subprocess
from send_keys import text_to_scancodes

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

TAB = ['0f', '8f']
ENTER = ['1c', '9c']
ALT_S = ['38', '1f', '9f', 'b8']

# Press Tab to focus the services list
send_scancodes(TAB)
time.sleep(0.3)

# Type 'dhcp' to jump directly to DHCP Server
codes = text_to_scancodes("dhcp")
send_scancodes(codes)
time.sleep(0.4)

# Open Properties
send_scancodes(ENTER)
time.sleep(1.0)

print("Opened DHCP Server properties")
