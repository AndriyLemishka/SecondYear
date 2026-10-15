import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

ESC = ['01', '81']
DOWN = ['e0', '50', 'e0', 'd0']
ENTER = ['1c', '9c']
ALT_E = ['38', '12', '92', 'b8'] # Startup type combo hotkey
ALT_S = ['38', '1f', '9f', 'b8'] # Start button
KEY_A = ['1e', '9e'] # 'a' for Automatic

# Close DHCP Client props
send_scancodes(ESC)
time.sleep(0.4)

# Move down to DHCP Server
send_scancodes(DOWN)
time.sleep(0.3)

# Open DHCP Server Properties
send_scancodes(ENTER)
time.sleep(1.0)

# Jump to Startup type combo (Alt+E)
send_scancodes(ALT_E)
time.sleep(0.3)

# Press 'a' twice to select Automatic
send_scancodes(KEY_A)
time.sleep(0.2)
send_scancodes(KEY_A)
time.sleep(0.2)

# Press Alt+S to Start service
send_scancodes(ALT_S)
time.sleep(3.0)

# Press Enter to click OK
send_scancodes(ENTER)
time.sleep(1.0)

print("Started DHCP Server service and set to Automatic")
