import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

ESC = ['01', '81']
SHIFT_TAB = ['2a', '0f', '8f', 'aa']
DOWN = ['e0', '50', 'e0', 'd0']

# Close dialog
send_scancodes(ESC)
time.sleep(0.4)

# Go to tree
send_scancodes(SHIFT_TAB)
time.sleep(0.2)
send_scancodes(SHIFT_TAB)
time.sleep(0.2)

# Go down 5 times to Групи
for i in range(5):
    send_scancodes(DOWN)
    time.sleep(0.2)

print("Navigated to Групи")
