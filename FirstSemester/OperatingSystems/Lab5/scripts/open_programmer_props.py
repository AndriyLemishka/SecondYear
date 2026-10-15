import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

TAB = ['0f', '8f']
UP = ['e0', '48', 'e0', 'c8']
DOWN = ['e0', '50', 'e0', 'd0']
ALT_ENTER = ['38', '1c', '9c', 'b8']
CTRL_TAB = ['1d', '0f', '8f', '9d']

# Press Tab to move to right pane
send_scancodes(TAB)
time.sleep(0.3)

# Press Down 2 times: first select first item (Адміністратор), then second item (Програміст)
send_scancodes(DOWN)
time.sleep(0.2)
send_scancodes(DOWN)
time.sleep(0.3)

# Open Properties (Alt+Enter)
send_scancodes(ALT_ENTER)
time.sleep(1.0)

# Switch to Profile tab (Ctrl+Tab 3 times)
for i in range(3):
    send_scancodes(CTRL_TAB)
    time.sleep(0.2)

print("Opened Програміст Profile tab")
