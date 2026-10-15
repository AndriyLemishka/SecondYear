import time
import subprocess
from send_keys import text_to_scancodes

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send(codes, sleep_after=0.4):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)
    time.sleep(sleep_after)

def type_text(text, sleep_after=0.3):
    codes = text_to_scancodes(text)
    if codes:
        send(codes, sleep_after=sleep_after)

ENTER = ['1c', '9c']
TAB = ['0f', '8f']
ALT_N = ['38', '31', 'b1', 'b8']
ALT_A = ['38', '1e', '9e', 'b8']

print("Starting New Scope Wizard automation...")

# Page 1: Welcome
send(ENTER, sleep_after=0.8) # Next

# Page 2: Scope Name
type_text("Office", sleep_after=0.4)
send(ENTER, sleep_after=0.8) # Next

# Page 3: IP Address Range
type_text("192.168.1.1", sleep_after=0.3)
send(TAB, sleep_after=0.2)
type_text("192.168.1.200", sleep_after=0.3)
send(TAB, sleep_after=0.2)
type_text("24", sleep_after=0.3)
send(ENTER, sleep_after=0.8) # Next

# Page 4: Add Exclusions
type_text("192.168.1.150", sleep_after=0.3)
send(TAB, sleep_after=0.2)
type_text("192.168.1.170", sleep_after=0.3)
send(TAB, sleep_after=0.2)
send(ENTER, sleep_after=0.6) # Add

type_text("192.168.1.2", sleep_after=0.3)
send(TAB, sleep_after=0.2)
type_text("192.168.1.3", sleep_after=0.3)
send(TAB, sleep_after=0.2)
send(ENTER, sleep_after=0.6) # Add

send(ALT_N, sleep_after=0.8) # Next

# Page 5: Lease Duration (8 days default)
send(ALT_N, sleep_after=0.8) # Next

# Page 6: Configure DHCP Options ("Yes" default)
send(ALT_N, sleep_after=0.8) # Next

# Page 7: Router (Default Gateway)
type_text("192.168.1.4", sleep_after=0.3)
send(TAB, sleep_after=0.2)
send(ENTER, sleep_after=0.6) # Add
send(ALT_N, sleep_after=0.8) # Next

# Page 8: Domain Name and DNS Servers
# Parent domain is already office.com
# Focus is on Parent domain or IP address?
# Let's press Alt+I to jump directly to IP address field
ALT_I = ['38', '17', '97', 'b8']
send(ALT_I, sleep_after=0.3)
type_text("192.168.1.5", sleep_after=0.3)
send(TAB, sleep_after=0.2)
send(ENTER, sleep_after=3.5) # Add (wait for DNS validation)
send(ALT_N, sleep_after=0.8) # Next

# Page 9: WINS Servers (leave blank)
send(ALT_N, sleep_after=0.8) # Next

# Page 10: Activate Scope ("Yes" default)
send(ALT_N, sleep_after=0.8) # Next

# Page 11: Completing the New Scope Wizard (Finish)
send(ENTER, sleep_after=1.5) # Finish

print("New Scope Wizard completed successfully!")
