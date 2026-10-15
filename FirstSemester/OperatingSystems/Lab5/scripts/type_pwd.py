import subprocess
import time
from send_keys import text_to_scancodes, VBOX, VM_NAME

# New password: Pa$$word
codes1 = text_to_scancodes("Pa$$word")
# Tab
codes_tab = ['0f', '8f']
# Confirm password: Pa$$word
codes2 = text_to_scancodes("Pa$$word")
# Enter
codes_enter = ['1c', '9c']

all_codes = codes1 + codes_tab + codes2 + codes_enter

chunk_size = 12
for i in range(0, len(all_codes), chunk_size):
    chunk = all_codes[i:i+chunk_size]
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + chunk
    subprocess.run(cmd, check=True)
    time.sleep(0.05)

print("Typed password and confirmed successfully")
