import time
import subprocess
from send_keys import text_to_scancodes

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

ENTER = ['1c', '9c']
TAB = ['0f', '8f']
SHIFT_TAB = ['2a', '0f', '8f', 'aa']

# Focus is currently on Add button!
# Press Enter to click Add
send_scancodes(ENTER)
time.sleep(0.5)

# Now type second exclusion: 192.168.1.2 to 192.168.1.3
# In this dialog, after clicking Add, focus is usually in Start IP address
send_scancodes(text_to_scancodes("192.168.1.2"))
time.sleep(0.3)
send_scancodes(TAB)
time.sleep(0.2)
send_scancodes(text_to_scancodes("192.168.1.3"))
time.sleep(0.3)
send_scancodes(TAB)
time.sleep(0.2)
send_scancodes(ENTER) # Click Add
time.sleep(0.5)

print("Added both exclusions")
