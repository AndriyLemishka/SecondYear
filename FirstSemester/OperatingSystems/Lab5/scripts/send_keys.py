import sys
import subprocess
import time

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
VM_NAME = "WindowsServer2008"

KEY_MAP = {
    'a': ['1e', '9e'], 'b': ['30', 'b0'], 'c': ['2e', 'ae'], 'd': ['20', 'a0'],
    'e': ['12', '92'], 'f': ['21', 'a1'], 'g': ['22', 'a2'], 'h': ['23', 'a3'],
    'i': ['17', '97'], 'j': ['24', 'a4'], 'k': ['25', 'a5'], 'l': ['26', 'a6'],
    'm': ['32', 'b2'], 'n': ['31', 'b1'], 'o': ['18', '98'], 'p': ['19', '99'],
    'q': ['10', '90'], 'r': ['13', '93'], 's': ['1f', '9f'], 't': ['14', '94'],
    'u': ['16', '96'], 'v': ['2f', 'af'], 'w': ['11', '91'], 'x': ['2d', 'ad'],
    'y': ['15', '95'], 'z': ['2c', 'ac'],
    '0': ['0b', '8b'], '1': ['02', '82'], '2': ['03', '83'], '3': ['04', '84'],
    '4': ['05', '85'], '5': ['06', '86'], '6': ['07', '87'], '7': ['08', '88'],
    '8': ['09', '89'], '9': ['0a', '8a'],
    ' ': ['39', 'b9'], '\n': ['1c', '9c'], '\r': ['1c', '9c'], '\t': ['0f', '8f'],
    '.': ['34', 'b4'], ',': ['33', 'b3'], '-': ['0c', '8c'], '=': ['0d', '8d'],
    '/': ['35', 'b5'], '\\': ['2b', 'ab'], ';': ['27', 'a7'], "'": ['28', 'a8'],
    '[': ['1a', '9a'], ']': ['1b', '9b'], '`': ['29', 'a9']
}

SHIFT_MAP = {
    ':': ['27', 'a7'], '"': ['28', 'a8'], '<': ['33', 'b3'], '>': ['34', 'b4'],
    '?': ['35', 'b5'], '_': ['0c', '8c'], '+': ['0d', '8d'], '{': ['1a', '9a'],
    '}': ['1b', '9b'], '|': ['2b', 'ab'], '~': ['29', 'a9'], '!': ['02', '82'],
    '@': ['03', '83'], '#': ['04', '84'], '$': ['05', '85'], '%': ['06', '86'],
    '^': ['07', '87'], '&': ['08', '88'], '*': ['09', '89'], '(': ['0a', '8a'],
    ')': ['0b', '8b']
}

def text_to_scancodes(text):
    codes = []
    for ch in text:
        if ch in KEY_MAP:
            codes.extend(KEY_MAP[ch])
        elif ch in SHIFT_MAP:
            codes.append('2a') # Shift press
            codes.extend(SHIFT_MAP[ch])
            codes.append('aa') # Shift release
        elif ch.isupper() and ch.lower() in KEY_MAP:
            codes.append('2a')
            codes.extend(KEY_MAP[ch.lower()])
            codes.append('aa')
    return codes

def send_text(text, delay_between=0.04):
    chunk_size = 12
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        codes = text_to_scancodes(chunk)
        if codes:
            cmd = [VBOX, 'controlvm', VM_NAME, 'keyboardputscancode'] + codes
            subprocess.run(cmd, check=True)
            time.sleep(delay_between)

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == '--file':
        with open(sys.argv[2], 'r', encoding='utf-8') as f:
            for line in f:
                line_str = line.strip()
                if line_str and not line_str.startswith('#'):
                    print(f"Typing: {line_str}")
                    send_text(line_str + '\n')
                    time.sleep(0.25)
    elif len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:]) + '\n'
        send_text(text)
