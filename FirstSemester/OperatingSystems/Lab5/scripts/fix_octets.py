import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send(codes, sleep_after=0.2):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)
    time.sleep(sleep_after)

LEFT = ['e0', '4b', 'e0', 'cb']
RIGHT = ['e0', '4d', 'e0', 'cd']
BACKSPACE = ['0e', '8e']
KEY_2 = ['03', '83']
KEY_4 = ['05', '85']

# Move left 3 times to octet 1
for _ in range(3):
    send(LEFT)

# Erase the '4' in 194
send(BACKSPACE)
# Type '2'
send(KEY_2)

# Move right 3 times to octet 4
for _ in range(3):
    send(RIGHT)

# Erase the '2' in octet 4
send(BACKSPACE)
# Type '4'
send(KEY_4)

print("Fixed octets: 192.168.1.4")
