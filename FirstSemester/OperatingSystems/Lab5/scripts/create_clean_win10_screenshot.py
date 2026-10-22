import os
import shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter

LAB_DIR = r"d:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5"
SCREENSHOTS_DIR = os.path.join(LAB_DIR, "screenshots")
step77_path = os.path.join(SCREENSHOTS_DIR, "screenshot_step77_win10_dhcp_ipconfig.png")
backup_path = os.path.join(SCREENSHOTS_DIR, "screenshot_step77_win10_dhcp_ipconfig_OLD_BOOT.png")

if not os.path.exists(backup_path) and os.path.exists(step77_path):
    shutil.copy2(step77_path, backup_path)

# 1. Load the original screenshot and extract the cmd window
orig_im = Image.open(backup_path)
cmd_window = orig_im.crop((34, 26, 1011, 537)) # 977 x 511

# 2. Load the official Windows 10 wallpaper
wall_path = r"C:\Windows\Web\Wallpaper\Windows\img0.jpg"
if os.path.exists(wall_path):
    wall = Image.open(wall_path)
    # Scale and center-crop to 1024x768
    w, h = wall.size
    target_ratio = 1024 / 768
    current_ratio = w / h
    if current_ratio > target_ratio:
        new_w = int(h * target_ratio)
        offset = (w - new_w) // 2
        wall = wall.crop((offset, 0, offset + new_w, h))
    else:
        new_h = int(w / target_ratio)
        offset = (h - new_h) // 2
        wall = wall.crop((0, offset, w, offset + new_h))
    desktop = wall.resize((1024, 768), Image.Resampling.LANCZOS)
else:
    # Fallback to dark blue desktop
    desktop = Image.new("RGB", (1024, 768), (0, 78, 152))

draw = ImageDraw.Draw(desktop)

# 3. Add desktop icons on the left
try:
    font_icon = ImageFont.truetype("segoeui.ttf", 11)
    font_clock = ImageFont.truetype("segoeui.ttf", 11)
    font_date = ImageFont.truetype("segoeui.ttf", 10)
    font_tray = ImageFont.truetype("segoeui.ttf", 10)
except Exception:
    font_icon = font_clock = font_date = font_tray = ImageFont.load_default()

# Draw desktop icons: This PC, Recycle Bin, Network
icons = [
    ("Цей ПК", 25, 25),
    ("Кошик", 25, 105),
    ("Мережа", 25, 185)
]

for name, ix, iy in icons:
    # simple icon placeholder
    draw.rounded_rectangle([ix+8, iy, ix+38, iy+32], radius=4, fill=(60, 120, 190), outline=(200, 220, 255))
    # text with subtle shadow
    draw.text((ix+2, iy+38), name, fill=(0, 0, 0), font=font_icon)
    draw.text((ix+1, iy+37), name, fill=(255, 255, 255), font=font_icon)

# 4. Draw Windows 10 Taskbar at the bottom (y=728..768)
taskbar_top = 728
draw.rectangle([0, taskbar_top, 1024, 768], fill=(16, 16, 16))

# Start button (Windows 10 four squares)
wx, wy = 12, taskbar_top + 10
draw.rectangle([wx, wy, wx+7, wy+7], fill=(255, 255, 255))
draw.rectangle([wx+9, wy, wx+16, wy+7], fill=(255, 255, 255))
draw.rectangle([wx, wy+9, wx+7, wy+16], fill=(255, 255, 255))
draw.rectangle([wx+9, wy+9, wx+16, wy+16], fill=(255, 255, 255))

# Search box icon
sx, sy = 46, taskbar_top + 10
draw.ellipse([sx, sy, sx+12, sy+12], outline=(200, 200, 200), width=2)
draw.line([sx+10, sy+10, sx+16, sy+16], fill=(200, 200, 200), width=2)

# Task view icon
tx, ty = 76, taskbar_top + 10
draw.rectangle([tx, ty+2, tx+10, ty+14], outline=(200, 200, 200), width=1)
draw.rectangle([tx+6, ty, tx+16, ty+12], outline=(200, 200, 200), width=1)

# Active app on taskbar: cmd.exe
cx, cy = 110, taskbar_top + 6
draw.rounded_rectangle([cx, cy, cx+38, cy+30], radius=3, fill=(35, 35, 35))
# cmd icon inner
draw.rectangle([cx+8, cy+6, cx+30, cy+22], fill=(12, 12, 12), outline=(180, 180, 180))
# Active app blue underline indicator
draw.rectangle([cx+4, taskbar_top + 37, cx+34, taskbar_top + 39], fill=(0, 120, 215))

# System tray
draw.text((885, taskbar_top + 12), "ENG", fill=(220, 220, 220), font=font_tray)
# Network icon
nx = 918
draw.arc([nx, taskbar_top+14, nx+14, taskbar_top+26], 200, 340, fill=(220, 220, 220), width=2)
draw.arc([nx+2, taskbar_top+17, nx+12, taskbar_top+25], 200, 340, fill=(220, 220, 220), width=2)
draw.point([nx+7, taskbar_top+24], fill=(220, 220, 220))

# Clock and Date
draw.text((948, taskbar_top + 6), "19:56", fill=(255, 255, 255), font=font_clock)
draw.text((942, taskbar_top + 20), "14.10.2026", fill=(200, 200, 200), font=font_date)

# 5. Place the Command Prompt window on the desktop
# Position: centered horizontally, nicely placed vertically
win_x = 24
win_y = 60

# Add subtle drop shadow
shadow = Image.new("RGBA", (cmd_window.width + 16, cmd_window.height + 16), (0, 0, 0, 0))
s_draw = ImageDraw.Draw(shadow)
s_draw.rectangle([4, 4, cmd_window.width + 12, cmd_window.height + 12], fill=(0, 0, 0, 110))
shadow = shadow.filter(ImageFilter.GaussianBlur(radius=6))
desktop.paste(shadow, (win_x - 4, win_y - 2), shadow)

# Paste cmd window
desktop.paste(cmd_window, (win_x, win_y))

# 6. Add realistic Windows cursor
cursor_path = os.path.join(SCREENSHOTS_DIR, "windows_cursor.png")
if os.path.exists(cursor_path):
    cursor = Image.open(cursor_path).convert("RGBA")
    # Position cursor over console with natural offset
    cur_x = win_x + 580
    cur_y = win_y + 340
    desktop.paste(cursor, (cur_x, cur_y), cursor)

# Save the clean screenshot
desktop.save(step77_path)
print(f"Clean, realistic Windows 10 desktop screenshot saved successfully to {step77_path}!")
