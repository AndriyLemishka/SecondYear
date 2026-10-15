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

# Close Програміст Properties
send_scancodes(ESC)
time.sleep(0.4)

# Press Up once to select Адміністратор
send_scancodes(UP)
time.sleep(0.3)

# Open Properties
send_scancodes(ALT_ENTER)
time.sleep(1.0)

# Switch to Member Of tab (General -> Address -> Account -> Profile -> Telephones -> Organization -> Remote Desktop Services -> COM+ -> Member Of)
# In standard 2008 R2 User Properties, Member Of is usually tab 9 or 10.
# Let's send Ctrl+Tab 8 times:
for i in range(8):
    send_scancodes(CTRL_TAB)
    time.sleep(0.2)

print("Opened Адміністратор Properties and switched to Member Of")
