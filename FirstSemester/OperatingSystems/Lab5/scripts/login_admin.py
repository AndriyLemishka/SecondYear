import time
import subprocess
from send_keys import text_to_scancodes, VBOX, VM_NAME

# Clear field with Ctrl+A, Backspace
cmd_clear = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode', '1d', '1e', '9e', '9d', '0e', '8e']
subprocess.run(cmd_clear, check=True)
time.sleep(0.3)

# Type Pa$$word + Enter
pw = "Pa$$word"
codes = text_to_scancodes(pw) + ['1c', '9c']

chunk_size = 12
for i in range(0, len(codes), chunk_size):
    chunk = codes[i:i+chunk_size]
    cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + chunk
    subprocess.run(cmd, check=True)
    time.sleep(0.05)

print("Typed Pa$$word and pressed Enter")
