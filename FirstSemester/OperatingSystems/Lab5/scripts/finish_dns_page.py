import time
import subprocess
from send_keys import text_to_scancodes

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

CTRL_A = ['1d', '1e', '9e', '9d']
ALT_D = ['38', '20', 'a0', 'b8']
ALT_R = ['38', '13', '93', 'b8']
TAB = ['0f', '8f']
UP = ['e0', '48', 'e0', 'c8']

# Focus Parent domain (Alt+D)
send_scancodes(ALT_D)
time.sleep(0.3)
send_scancodes(CTRL_A)
time.sleep(0.2)
send_scancodes(text_to_scancodes("office.com"))
time.sleep(0.3)

# Tab to list box
send_scancodes(TAB)
time.sleep(0.2)
send_scancodes(TAB)
time.sleep(0.2)

# Select 127.0.0.1
send_scancodes(UP)
time.sleep(0.2)

# Click Remove (Alt+R)
send_scancodes(ALT_R)
time.sleep(0.5)

print("Parent domain office.com set and 127.0.0.1 removed")
