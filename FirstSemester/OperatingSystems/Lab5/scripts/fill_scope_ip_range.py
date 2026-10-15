import time
import subprocess
from send_keys import text_to_scancodes

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

TAB = ['0f', '8f']

# Focus is on Start IP address
send_scancodes(text_to_scancodes("192.168.1.1"))
time.sleep(0.3)

# Tab to End IP address
send_scancodes(TAB)
time.sleep(0.2)
send_scancodes(text_to_scancodes("192.168.1.200"))
time.sleep(0.3)

# Tab to Length
send_scancodes(TAB)
time.sleep(0.2)
# Length field is already 24 by default for Class C, but let's make sure
send_scancodes(text_to_scancodes("24"))
time.sleep(0.3)

print("Filled IP range")
