import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

ESC = ['01', '81']
RIGHT = ['e0', '4d', 'e0', 'cd']
DOWN = ['e0', '50', 'e0', 'd0']

# Close Action menu
send_scancodes(ESC)
time.sleep(0.3)

# Expand DHCP
send_scancodes(RIGHT)
time.sleep(0.5)

# Down to server.office.com
send_scancodes(DOWN)
time.sleep(0.4)

# Expand server.office.com
send_scancodes(RIGHT)
time.sleep(1.0)

print("Expanded DHCP and server.office.com")
