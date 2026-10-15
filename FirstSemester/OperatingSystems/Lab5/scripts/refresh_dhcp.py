import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

ALT_F4 = ['38', '3e', 'be', 'b8']
F5 = ['3f', 'bf']
RIGHT = ['e0', '4d', 'e0', 'cd']
DOWN = ['e0', '50', 'e0', 'd0']

# Close services.msc
send_scancodes(ALT_F4)
time.sleep(0.8)

# Now in DHCP console: refresh
send_scancodes(F5)
time.sleep(1.0)

# Expand DHCP
send_scancodes(RIGHT)
time.sleep(0.5)

# Down to server.office.com
send_scancodes(DOWN)
time.sleep(0.3)

# Expand server.office.com
send_scancodes(RIGHT)
time.sleep(1.0)

print("Closed services and refreshed DHCP")
