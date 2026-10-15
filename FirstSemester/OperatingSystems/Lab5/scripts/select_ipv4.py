import time
import subprocess

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

def send_scancodes(codes):
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
    subprocess.run(cmd, check=True)

ESC = ['01', '81']
DOWN = ['e0', '50', 'e0', 'd0']

send_scancodes(ESC)
time.sleep(0.3)
send_scancodes(DOWN)
time.sleep(0.5)

print("Pressed Esc then Down")
