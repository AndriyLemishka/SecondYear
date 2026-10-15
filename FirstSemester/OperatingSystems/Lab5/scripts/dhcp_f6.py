import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

ESC = ['01', '81']
F6 = ['40', 'c0']
DOWN = ['e0', '50', 'e0', 'd0']

# Close menu
send_scancodes(ESC)
time.sleep(0.3)

# Press F6 to switch pane to tree
send_scancodes(F6)
time.sleep(0.3)

# Down to see where focus is
send_scancodes(DOWN)
time.sleep(0.3)

print("F6 pressed")
