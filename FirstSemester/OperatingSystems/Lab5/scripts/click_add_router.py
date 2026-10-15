import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

TAB = ['0f', '8f']
ENTER = ['1c', '9c']

# Tab 4 times to Add button
for i in range(4):
    send_scancodes(TAB)
    time.sleep(0.15)

# Press Enter to click Add
send_scancodes(ENTER)
time.sleep(0.5)

print("Clicked Add on Router")
