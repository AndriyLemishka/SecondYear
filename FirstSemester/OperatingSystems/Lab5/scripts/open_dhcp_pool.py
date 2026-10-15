import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

SHIFT_TAB = ['2a', '0f', '8f', 'aa']
TAB = ['0f', '8f']
RIGHT = ['e0', '4d', 'e0', 'cd']
DOWN = ['e0', '50', 'e0', 'd0']
UP = ['e0', '48', 'e0', 'c8']

# Move focus to tree
send_scancodes(SHIFT_TAB)
time.sleep(0.3)

# Down to Scope [192.168.1.0]
send_scancodes(DOWN)
time.sleep(0.3)

# Expand Scope
send_scancodes(RIGHT)
time.sleep(0.5)

# Down to Address Pool
send_scancodes(DOWN)
time.sleep(0.4)

print("Navigated to Address Pool")
