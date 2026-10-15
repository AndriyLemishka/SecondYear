import time
import subprocess
from send_keys import text_to_scancodes

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

TAB = ['0f', '8f']
SHIFT_TAB = ['2a', '0f', '8f', 'aa']
ENTER = ['1c', '9c']
UP = ['e0', '48', 'e0', 'c8']
DOWN = ['e0', '50', 'e0', 'd0']
CTRL_A = ['1d', '1e', '9e', '9d']
ALT_D = ['38', '20', 'a0', 'b8']

# Focus is currently on IP address field (192.168.1.5)
# Tab to Add button
send_scancodes(TAB)
time.sleep(0.3)

# Click Add
send_scancodes(ENTER)
time.sleep(1.0)

# In Windows DNS step, clicking Add sometimes validates DNS server (may take 2 seconds)
time.sleep(2.0)

# Now fix Parent domain: press Alt+D or Shift+Tabs
send_scancodes(ALT_D)
time.sleep(0.3)
send_scancodes(CTRL_A)
time.sleep(0.2)
send_scancodes(text_to_scancodes("office.com"))
time.sleep(0.3)

print("DNS server added and parent domain set to office.com")
