import time
import subprocess
from send_keys import text_to_scancodes

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send(codes, sleep_after=0.25):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)
    time.sleep(sleep_after)

def type_text(text, sleep_after=0.2):
    codes = text_to_scancodes(text)
    if codes:
        send(codes, sleep_after=sleep_after)

DOWN = ['e0', '50', 'e0', 'd0']
UP = ['e0', '48', 'e0', 'c8']
TAB = ['0f', '8f']
SHIFT_TAB = ['2a', '0f', '8f', 'aa']
ENTER = ['1c', '9c']
SPACE = ['39', 'b9']
CTRL_A = ['1d', '1e', '9e', '9d']

# 1. Down 4 times to 006 DNS Servers
for _ in range(4):
    send(DOWN)

# Tab to Data entry: IP address list
# In 006 DNS Servers, tab order:
# List of options -> Server name -> Resolve -> IP address -> Add -> List of IPs -> Remove -> Up -> Down -> OK
send(TAB) # Server name
send(TAB) # Resolve
send(TAB) # IP address
type_text("192.168.1.5")
send(TAB) # Add button
send(ENTER) # Click Add
time.sleep(2.0) # wait validation

send(TAB) # List of IPs
send(UP) # Select 127.0.0.1
send(TAB) # Remove button
send(ENTER) # Click Remove
time.sleep(0.5)

# Now move focus back to options list: Shift+Tab multiple times
for _ in range(8):
    send(SHIFT_TAB)

# Now down to 015 DNS Domain Name (it's 9 items down from 006)
for _ in range(9):
    send(DOWN)

# Tab to String value
send(TAB)
send(CTRL_A)
type_text("office.com")

# Press Enter to click OK
send(ENTER, sleep_after=1.0)

print("Scope options 006 and 015 updated!")
