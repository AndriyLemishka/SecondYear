import os
import sys
import random
import subprocess
import time
from PIL import Image

VBOX = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
CURSOR_PATH = r"d:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\windows_cursor.png"

def capture_screen_with_cursor(output_path, hover_pos=None, jitter=6, vm_name="WindowsServer2008"):
    import uuid
    raw_path = rf"d:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\raw_screen_{uuid.uuid4().hex[:8]}.png"
    cmd = [VBOX, "controlvm", vm_name, "screenshotpng", raw_path]
    for _ in range(5):
        try:
            subprocess.run(cmd, check=True)
            break
        except subprocess.CalledProcessError:
            time.sleep(0.5)
    
    img = Image.open(raw_path).convert("RGBA")
    w, h = img.width, img.height
    
    # Robustly find and erase any existing static/stamped cursor (especially at 400, 300 or anywhere)
    for cy in range(0, h - 19):
        found = False
        for cx in range(0, w - 12):
            if (max(img.getpixel((cx, cy))[:3]) < 50 and
                max(img.getpixel((cx, cy+1))[:3]) < 50 and
                max(img.getpixel((cx+1, cy+1))[:3]) < 50 and
                max(img.getpixel((cx, cy+2))[:3]) < 50 and
                min(img.getpixel((cx+1, cy+2))[:3]) > 200 and
                max(img.getpixel((cx+2, cy+2))[:3]) < 50):
                # Found existing cursor at (cx, cy)! Erase it cleanly:
                bg = img.getpixel((max(0, cx - 4), max(0, cy - 3)))
                for ey in range(cy - 2, min(h, cy + 24)):
                    for ex in range(cx - 2, min(w, cx + 18)):
                        img.putpixel((ex, ey), bg)
                found = True
                break
        if found:
            break
                
    if hover_pos is not None:
        hx, hy = hover_pos
        dx = random.randint(-jitter, jitter)
        dy = random.randint(-jitter, jitter)
        target_x = max(0, min(img.width - 20, hx + dx))
        target_y = max(0, min(img.height - 25, hy + dy))
        
        cursor = Image.open(CURSOR_PATH).convert("RGBA")
        img.paste(cursor, (target_x, target_y), cursor)
        print(f"Pasted dynamic cursor at ({target_x}, {target_y}) [intended ({hx}, {hy})]")
    
    img.convert("RGB").save(output_path)
    if os.path.exists(raw_path):
        try:
            os.remove(raw_path)
        except Exception:
            pass
    print(f"Successfully captured {output_path} from {vm_name}")

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else "current_screen.png"
    x = int(sys.argv[2]) if len(sys.argv) > 2 else random.randint(150, 650)
    y = int(sys.argv[3]) if len(sys.argv) > 3 else random.randint(150, 450)
    vm = sys.argv[4] if len(sys.argv) > 4 else "WindowsServer2008"
    capture_screen_with_cursor(out, (x, y), vm_name=vm)
