import time
import subprocess
from send_keys import text_to_scancodes

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

# Win+R
WIN_R = ['e0', '5b', '13', '93', 'e0', 'db']
send_scancodes(WIN_R)
time.sleep(0.8)

# Type services.msc
codes = text_to_scancodes("services.msc\n")
send_scancodes(codes)
time.sleep(2.5)

print("Opened services.msc")
