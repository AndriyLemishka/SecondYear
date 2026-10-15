import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

DOWN = ['e0', '50', 'e0', 'd0']
ALT_A = ['38', '1e', '9e', 'b8']
ENTER = ['1c', '9c']

# Down twice: Address Leases (1), Reservations (2)
send_scancodes(DOWN)
time.sleep(0.3)
send_scancodes(DOWN)
time.sleep(0.3)

# Open Action menu (Alt+A)
send_scancodes(ALT_A)
time.sleep(0.5)

# In Reservations Action menu, option 1 is "New Reservation..."
send_scancodes(ENTER)
time.sleep(1.0)

print("Opened New Reservation dialog")
