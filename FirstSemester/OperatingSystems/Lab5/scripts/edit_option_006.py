import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send(codes, sleep_after=0.3):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)
    time.sleep(sleep_after)

UP = ['e0', '48', 'e0', 'c8']
DOWN = ['e0', '50', 'e0', 'd0']
ENTER = ['1c', '9c']

# Press Up to unselect multiple and select item 1
send(UP)
time.sleep(0.3)

# Press Down once to select item 2 (006 DNS Servers)
send(DOWN)
time.sleep(0.3)

# Press Enter to open its properties
send(ENTER)
time.sleep(1.0)

print("Opened 006 DNS Servers properties")
