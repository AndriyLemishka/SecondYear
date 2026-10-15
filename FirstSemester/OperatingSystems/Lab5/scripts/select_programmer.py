import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

ESC = ['01', '81']
UP = ['e0', '48', 'e0', 'c8']
ALT_ENTER = ['38', '1c', '9c', 'b8']
CTRL_TAB = ['1d', '0f', '8f', '9d']

# Close Сервіс-інженер
send_scancodes(ESC)
time.sleep(0.4)

# Press Up once to select Програміст
send_scancodes(UP)
time.sleep(0.3)

# Open Properties
send_scancodes(ALT_ENTER)
time.sleep(1.0)

# Switch to Profile tab
for i in range(3):
    send_scancodes(CTRL_TAB)
    time.sleep(0.2)

print("Opened Програміст Profile")
