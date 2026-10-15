import time
import subprocess
from send_keys import text_to_scancodes

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send(codes, sleep_after=0.3):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)
    time.sleep(sleep_after)

def type_text(text, sleep_after=0.2):
    codes = text_to_scancodes(text)
    if codes:
        send(codes, sleep_after=sleep_after)

TAB = ['0f', '8f']
DOWN = ['e0', '50', 'e0', 'd0']
ENTER = ['1c', '9c']
ALT_I = ['38', '17', '97', 'b8']
ALT_A = ['38', '1e', '9e', 'b8']

# Focus is in tree on Scope Options
# Tab to middle list
send(TAB)
time.sleep(0.3)

# Down to 006 DNS Servers
send(DOWN)
time.sleep(0.3)

# Press Enter to open properties
send(ENTER)
time.sleep(1.0)

# Jump to IP address (Alt+I)
send(ALT_I)
type_text("192.168.1.5")
time.sleep(0.3)

# Click Add (Alt+A)
send(ALT_A)
time.sleep(3.0) # DNS validation

# Click OK (Enter)
send(ENTER)
time.sleep(1.0)

print("Configured 006 DNS Servers to 192.168.1.5")
