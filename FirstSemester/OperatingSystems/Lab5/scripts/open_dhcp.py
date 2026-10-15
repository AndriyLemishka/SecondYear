import time
import subprocess
from send_keys import text_to_scancodes

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

# Win+R: Left GUI (e0 5b) + 'r' (13) + release 'r' (93) + release GUI (e0 db)
WIN_R = ['e0', '5b', '13', '93', 'e0', 'db']
send_scancodes(WIN_R)
time.sleep(0.8)

# Type dhcpmgmt.msc
codes = text_to_scancodes("dhcpmgmt.msc\n")
send_scancodes(codes)
time.sleep(2.0)

print("Opened dhcpmgmt.msc")
