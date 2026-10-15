import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

# Alt+Tab to cycle to Server Manager
# Alt down (38), Tab (0f 8f), Alt up (b8)
ALT_TAB = ['38', '0f', '8f', 'b8']
send_scancodes(ALT_TAB)
time.sleep(1.0)

print("Alt-tabbed")
