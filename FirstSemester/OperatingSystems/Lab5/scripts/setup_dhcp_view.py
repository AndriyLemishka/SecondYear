import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

# Maximize DHCP window: Alt+Space (38 39 b9 b8) then 'x' (2d ad)
ALT_SPACE_X = ['38', '39', 'b9', 'b8', '2d', 'ad']
send_scancodes(ALT_SPACE_X)
time.sleep(0.5)

# Press Right arrow to see if DHCP node expands
RIGHT = ['e0', '4d', 'e0', 'cd']
send_scancodes(RIGHT)
time.sleep(0.5)

# If not expanded, let's also try Action menu: Alt+A (38 1e 9e b8)
ALT_A = ['38', '1e', '9e', 'b8']
send_scancodes(ALT_A)
time.sleep(0.5)

print("Maximized and checked Action menu")
