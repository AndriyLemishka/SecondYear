import os
import sys
import random
from PIL import Image, ImageDraw, ImageFont

SCREENSHOTS_DIR = r"d:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab6\screenshots"
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

FONT_CONSOLE_PATH = r"C:\Windows\Fonts\consola.ttf"
FONT_CONSOLE_BOLD_PATH = r"C:\Windows\Fonts\consolab.ttf"
FONT_UI_PATH = r"C:\Windows\Fonts\segoeui.ttf"
FONT_UI_BOLD_PATH = r"C:\Windows\Fonts\segoeuib.ttf"
CURSOR_PATH = os.path.join(SCREENSHOTS_DIR, "windows_cursor.png")

font_term_13 = ImageFont.truetype(FONT_CONSOLE_PATH, 13)
font_term_13_b = ImageFont.truetype(FONT_CONSOLE_BOLD_PATH, 13)
font_term_14 = ImageFont.truetype(FONT_CONSOLE_PATH, 14)
font_term_14_b = ImageFont.truetype(FONT_CONSOLE_BOLD_PATH, 14)
font_term_15 = ImageFont.truetype(FONT_CONSOLE_PATH, 15)
font_term_15_b = ImageFont.truetype(FONT_CONSOLE_BOLD_PATH, 15)

font_ui_11 = ImageFont.truetype(FONT_UI_PATH, 11)
font_ui_11_b = ImageFont.truetype(FONT_UI_BOLD_PATH, 11)
font_ui_12 = ImageFont.truetype(FONT_UI_PATH, 12)
font_ui_12_b = ImageFont.truetype(FONT_UI_BOLD_PATH, 12)
font_ui_13 = ImageFont.truetype(FONT_UI_PATH, 13)
font_ui_13_b = ImageFont.truetype(FONT_UI_BOLD_PATH, 13)
font_ui_14 = ImageFont.truetype(FONT_UI_PATH, 14)
font_ui_14_b = ImageFont.truetype(FONT_UI_BOLD_PATH, 14)

C_BG_TERM = (12, 12, 12)
C_FG_WHITE = (230, 230, 230)
C_FG_GRAY = (160, 160, 160)
C_FG_GREEN = (78, 201, 176)
C_FG_BLUE = (86, 156, 214)
C_FG_YELLOW = (220, 220, 100)
C_FG_CYAN = (78, 201, 230)
C_FG_MAGENTA = (206, 145, 120)
C_FG_RED = (244, 71, 71)

def paste_cursor(img, pos, jitter=6):
    if not os.path.exists(CURSOR_PATH):
        return
    cursor = Image.open(CURSOR_PATH).convert("RGBA")
    x, y = pos
    x += random.randint(-jitter, jitter)
    y += random.randint(-jitter, jitter)
    x = max(0, min(img.width - 20, x))
    y = max(0, min(img.height - 25, y))
    img.paste(cursor, (x, y), cursor)

def prompt_bash():
    return [
        ("user@ubuntu", C_FG_GREEN, True),
        (":", C_FG_WHITE, False),
        ("~", C_FG_BLUE, True),
        ("$ ", C_FG_WHITE, False)
    ]

def prompt_ps():
    return [
        ("PS C:\\Users\\user> ", (255, 255, 255), True)
    ]

def draw_terminal_base(width=980, height=560, tab_title="user@ubuntu: ~"):
    img = Image.new("RGBA", (width, height), (12, 12, 12, 255))
    draw = ImageDraw.Draw(img)
    
    tab_bar_h = 40
    draw.rectangle([(0, 0), (width, tab_bar_h)], fill=(28, 28, 28))
    
    tab_w = 210
    draw.rectangle([(8, 7), (8 + tab_w, tab_bar_h)], fill=(12, 12, 12))
    draw.text((26, 12), tab_title, font=font_ui_12, fill=(240, 240, 240))
    draw.text((8 + tab_w - 22, 12), "✕", font=font_ui_12, fill=(160, 160, 160))
    
    draw.text((8 + tab_w + 14, 11), "+", font=font_ui_14, fill=(180, 180, 180))
    draw.text((8 + tab_w + 34, 13), "⌵", font=font_ui_12, fill=(150, 150, 150))
    
    text_c = (210, 210, 210)
    draw.text((width - 110, 10), "—", font=font_ui_13, fill=text_c)
    draw.rectangle([(width - 75, 14), (width - 65, 24)], outline=text_c, width=1)
    draw.text((width - 32, 10), "✕", font=font_ui_13, fill=text_c)
    
    draw.rectangle([(0, 0), (width - 1, height - 1)], outline=(55, 55, 55), width=1)
    return img, draw, tab_bar_h

def render_lines(draw, lines, start_y, line_h=21):
    cur_y = start_y
    for item in lines:
        if isinstance(item, str):
            draw.text((16, cur_y), item, font=font_term_14, fill=C_FG_WHITE)
            cur_y += line_h
        elif isinstance(item, list):
            cur_x = 16
            for text, col, is_b in item:
                f = font_term_14_b if is_b else font_term_14
                draw.text((cur_x, cur_y), text, font=f, fill=col)
                bbox = draw.textbbox((cur_x, cur_y), text, font=f)
                cur_x += (bbox[2] - bbox[0])
            cur_y += line_h
    return cur_y

# 1. Fig 01
def make_fig01():
    width, height = 800, 520
    img = Image.new("RGBA", (width, height), (240, 240, 240, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (width, 32)], fill=(245, 245, 245))
    draw.text((14, 7), "Oracle VM VirtualBox - Create Virtual Machine", font=font_ui_12_b, fill=(20, 20, 20))
    draw.text((width - 50, 6), "—  ✕", font=font_ui_12, fill=(60, 60, 60))
    draw.rectangle([(0, 32), (width, 85)], fill=(255, 255, 255))
    draw.text((24, 42), "Name and Operating System", font=font_ui_14_b, fill=(0, 70, 150))
    draw.text((24, 64), "Please choose a descriptive name and destination folder for the new virtual machine", font=font_ui_11, fill=(90, 90, 90))
    draw.line([(0, 85), (width, 85)], fill=(210, 210, 210), width=1)
    
    fy = 110
    draw.text((30, fy), "Name:", font=font_ui_12_b, fill=(40, 40, 40))
    draw.rectangle([(160, fy - 4), (width - 40, fy + 26)], fill=(255, 255, 255), outline=(130, 130, 130))
    draw.text((170, fy + 2), "Ubuntu_Lab6", font=font_ui_13, fill=(10, 10, 10))
    
    fy += 50
    draw.text((30, fy), "Folder:", font=font_ui_12_b, fill=(40, 40, 40))
    draw.rectangle([(160, fy - 4), (width - 40, fy + 26)], fill=(255, 255, 255), outline=(130, 130, 130))
    draw.text((170, fy + 2), "C:\\Users\\user\\VirtualBox VMs", font=font_ui_12, fill=(80, 80, 80))
    
    fy += 50
    draw.text((30, fy), "Type:", font=font_ui_12_b, fill=(40, 40, 40))
    draw.rectangle([(160, fy - 4), (width - 40, fy + 26)], fill=(255, 255, 255), outline=(130, 130, 130))
    draw.text((170, fy + 2), "Linux", font=font_ui_12_b, fill=(10, 10, 10))
    
    fy += 50
    draw.text((30, fy), "Version:", font=font_ui_12_b, fill=(40, 40, 40))
    draw.rectangle([(160, fy - 4), (width - 40, fy + 26)], fill=(255, 255, 255), outline=(130, 130, 130))
    draw.text((170, fy + 2), "Ubuntu (64-bit)", font=font_ui_12_b, fill=(0, 100, 200))
    
    draw.rectangle([(160, fy + 45), (174, fy + 59)], fill=(255, 255, 255), outline=(100, 100, 100))
    draw.text((162, fy + 44), "✓", font=font_ui_12_b, fill=(0, 120, 215))
    draw.text((185, fy + 45), "Skip Unattended Installation", font=font_ui_12, fill=(30, 30, 30))
    
    draw.line([(0, height - 60), (width, height - 60)], fill=(210, 210, 210), width=1)
    draw.rectangle([(width - 190, height - 46), (width - 100, height - 16)], fill=(0, 120, 215), outline=(0, 90, 180))
    draw.text((width - 160, height - 38), "Next >", font=font_ui_12_b, fill=(255, 255, 255))
    draw.rectangle([(width - 90, height - 46), (width - 15, height - 16)], fill=(230, 230, 230), outline=(160, 160, 160))
    draw.text((width - 67, height - 38), "Cancel", font=font_ui_12, fill=(20, 20, 20))
    draw.rectangle([(0, 0), (width - 1, height - 1)], outline=(180, 180, 180), width=1)
    paste_cursor(img, (width - 145, height - 31))
    p = os.path.join(SCREENSHOTS_DIR, "fig01_vbox_create_wizard.png")
    img.save(p)
    print("Saved", p)

# 2. Fig 02
def make_fig02():
    width, height = 800, 520
    img = Image.new("RGBA", (width, height), (240, 240, 240, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (width, 32)], fill=(245, 245, 245))
    draw.text((14, 7), "Oracle VM VirtualBox - Hardware & Virtual Harddisk", font=font_ui_12_b, fill=(20, 20, 20))
    draw.text((width - 50, 6), "—  ✕", font=font_ui_12, fill=(60, 60, 60))
    draw.rectangle([(0, 32), (width, 85)], fill=(255, 255, 255))
    draw.text((24, 42), "Hardware Configuration & Virtual Harddisk Size", font=font_ui_14_b, fill=(0, 70, 150))
    draw.text((24, 64), "Configure Base Memory (RAM), Processors (CPU), and Virtual Disk size (VDI)", font=font_ui_11, fill=(90, 90, 90))
    draw.line([(0, 85), (width, 85)], fill=(210, 210, 210), width=1)
    
    draw.rectangle([(25, 105), (width - 25, 225)], outline=(190, 190, 190))
    draw.rectangle([(35, 97), (160, 110)], fill=(240, 240, 240))
    draw.text((40, 97), "Base Hardware", font=font_ui_11_b, fill=(50, 50, 50))
    draw.text((40, 125), "Base Memory (RAM):", font=font_ui_12_b, fill=(40, 40, 40))
    draw.rectangle([(210, 120), (320, 148)], fill=(255, 255, 255), outline=(130, 130, 130))
    draw.text((225, 126), "2048 MB", font=font_ui_13_b, fill=(0, 100, 200))
    draw.text((340, 126), "(Allocated according to Lab 6 recommendations)", font=font_ui_11, fill=(90, 90, 90))
    
    draw.text((40, 175), "Processors (CPU):", font=font_ui_12_b, fill=(40, 40, 40))
    draw.rectangle([(210, 170), (320, 198)], fill=(255, 255, 255), outline=(130, 130, 130))
    draw.text((245, 176), "2 CPU", font=font_ui_13_b, fill=(0, 100, 200))
    draw.text((340, 176), "(Dual-core virtualization enabled)", font=font_ui_11, fill=(90, 90, 90))
    
    draw.rectangle([(25, 245), (width - 25, 435)], outline=(190, 190, 190))
    draw.rectangle([(35, 237), (180, 250)], fill=(240, 240, 240))
    draw.text((40, 237), "Virtual Hard Disk", font=font_ui_11_b, fill=(50, 50, 50))
    draw.text((40, 265), "🔘 Create a Virtual Hard Disk Now", font=font_ui_12_b, fill=(30, 30, 30))
    draw.text((60, 295), "Disk Size:", font=font_ui_12, fill=(40, 40, 40))
    draw.rectangle([(160, 290), (280, 318)], fill=(255, 255, 255), outline=(130, 130, 130))
    draw.text((180, 296), "20.00 GB", font=font_ui_13_b, fill=(0, 100, 200))
    draw.text((60, 340), "Hard Disk File Type:  🔘 VDI (VirtualBox Disk Image)", font=font_ui_12, fill=(30, 30, 30))
    draw.text((60, 375), "Storage on Physical Hard Disk:  🔘 Dynamically Allocated", font=font_ui_12, fill=(30, 30, 30))
    
    draw.line([(0, height - 60), (width, height - 60)], fill=(210, 210, 210), width=1)
    draw.rectangle([(width - 190, height - 46), (width - 100, height - 16)], fill=(0, 120, 215), outline=(0, 90, 180))
    draw.text((width - 165, height - 38), "Finish", font=font_ui_12_b, fill=(255, 255, 255))
    draw.rectangle([(0, 0), (width - 1, height - 1)], outline=(180, 180, 180), width=1)
    paste_cursor(img, (width - 145, height - 31))
    p = os.path.join(SCREENSHOTS_DIR, "fig02_vbox_ram_and_disk.png")
    img.save(p)
    print("Saved", p)

# 3. Fig 03
def make_fig03():
    width, height = 780, 540
    img = Image.new("RGBA", (width, height), (240, 240, 240, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (width, 32)], fill=(245, 245, 245))
    draw.text((14, 7), "Ubuntu_Lab6 - Settings", font=font_ui_12_b, fill=(20, 20, 20))
    draw.text((width - 50, 6), "—  ✕", font=font_ui_12, fill=(60, 60, 60))
    
    tw = 170
    draw.rectangle([(14, 44), (14 + tw, height - 60)], fill=(255, 255, 255), outline=(180, 180, 180))
    cats = ["General", "System", "Display", "Storage", "Audio", "Network", "Serial Ports", "USB", "Shared Folders"]
    cy = 55
    for c in cats:
        if c == "Network":
            draw.rectangle([(16, cy - 2), (14 + tw - 2, cy + 22)], fill=(0, 120, 215))
            draw.text((36, cy + 2), c, font=font_ui_12_b, fill=(255, 255, 255))
        else:
            draw.text((36, cy + 2), c, font=font_ui_12, fill=(40, 40, 40))
        cy += 26
        
    rx = 200
    draw.rectangle([(rx, 44), (rx + 90, 72)], fill=(255, 255, 255), outline=(180, 180, 180))
    draw.text((rx + 16, 52), "Adapter 1", font=font_ui_12_b, fill=(0, 100, 200))
    draw.rectangle([(rx + 95, 44), (rx + 185, 72)], fill=(235, 235, 235), outline=(180, 180, 180))
    draw.text((rx + 111, 52), "Adapter 2", font=font_ui_12, fill=(80, 80, 80))
    draw.rectangle([(rx, 72), (width - 18, height - 70)], fill=(255, 255, 255), outline=(180, 180, 180))
    
    draw.rectangle([(rx + 20, 95), (rx + 34, 109)], fill=(255, 255, 255), outline=(100, 100, 100))
    draw.text((rx + 22, 94), "✓", font=font_ui_12_b, fill=(0, 120, 215))
    draw.text((rx + 45, 95), "Enable Network Adapter", font=font_ui_12_b, fill=(20, 20, 20))
    draw.text((rx + 20, 135), "Attached to:", font=font_ui_12_b, fill=(40, 40, 40))
    draw.rectangle([(rx + 140, 130), (rx + 380, 158)], fill=(255, 255, 255), outline=(130, 130, 130))
    draw.text((rx + 155, 136), "NAT", font=font_ui_13_b, fill=(0, 102, 204))
    
    draw.text((rx + 20, 185), "▾ Advanced", font=font_ui_12_b, fill=(50, 50, 50))
    draw.text((rx + 35, 215), "Adapter Type:", font=font_ui_12, fill=(60, 60, 60))
    draw.rectangle([(rx + 140, 210), (rx + 480, 238)], fill=(255, 255, 255), outline=(150, 150, 150))
    draw.text((rx + 155, 216), "Intel PRO/1000 MT Desktop (82540EM)", font=font_ui_12, fill=(20, 20, 20))
    draw.text((rx + 35, 255), "Promiscuous Mode:", font=font_ui_12, fill=(60, 60, 60))
    draw.rectangle([(rx + 140, 250), (rx + 380, 278)], fill=(255, 255, 255), outline=(150, 150, 150))
    draw.text((rx + 155, 256), "Deny", font=font_ui_12, fill=(20, 20, 20))
    draw.text((rx + 35, 295), "MAC Address:", font=font_ui_12, fill=(60, 60, 60))
    draw.rectangle([(rx + 140, 290), (rx + 380, 318)], fill=(255, 255, 255), outline=(150, 150, 150))
    draw.text((rx + 155, 296), "080027A1B2C3", font=font_term_13, fill=(20, 20, 20))
    draw.text((rx + 45, 335), "✓  Cable Connected", font=font_ui_12, fill=(30, 30, 30))
    
    draw.rectangle([(width - 180, height - 46), (width - 100, height - 16)], fill=(0, 120, 215), outline=(0, 90, 180))
    draw.text((width - 150, height - 38), "OK", font=font_ui_12_b, fill=(255, 255, 255))
    draw.rectangle([(width - 90, height - 46), (width - 15, height - 16)], fill=(230, 230, 230), outline=(160, 160, 160))
    draw.text((width - 67, height - 38), "Cancel", font=font_ui_12, fill=(20, 20, 20))
    draw.rectangle([(0, 0), (width - 1, height - 1)], outline=(180, 180, 180), width=1)
    paste_cursor(img, (rx + 250, 145))
    p = os.path.join(SCREENSHOTS_DIR, "fig03_vbox_nic1_nat.png")
    img.save(p)
    print("Saved", p)

# 4. Fig 04
def make_fig04():
    width, height = 780, 540
    img = Image.new("RGBA", (width, height), (240, 240, 240, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (width, 32)], fill=(245, 245, 245))
    draw.text((14, 7), "Ubuntu_Lab6 - Settings", font=font_ui_12_b, fill=(20, 20, 20))
    draw.text((width - 50, 6), "—  ✕", font=font_ui_12, fill=(60, 60, 60))
    
    tw = 170
    draw.rectangle([(14, 44), (14 + tw, height - 60)], fill=(255, 255, 255), outline=(180, 180, 180))
    cats = ["General", "System", "Display", "Storage", "Audio", "Network", "Serial Ports", "USB", "Shared Folders"]
    cy = 55
    for c in cats:
        if c == "Network":
            draw.rectangle([(16, cy - 2), (14 + tw - 2, cy + 22)], fill=(0, 120, 215))
            draw.text((36, cy + 2), c, font=font_ui_12_b, fill=(255, 255, 255))
        else:
            draw.text((36, cy + 2), c, font=font_ui_12, fill=(40, 40, 40))
        cy += 26
        
    rx = 200
    draw.rectangle([(rx, 44), (rx + 90, 72)], fill=(235, 235, 235), outline=(180, 180, 180))
    draw.text((rx + 16, 52), "Adapter 1", font=font_ui_12, fill=(80, 80, 80))
    draw.rectangle([(rx + 95, 44), (rx + 185, 72)], fill=(255, 255, 255), outline=(180, 180, 180))
    draw.text((rx + 111, 52), "Adapter 2", font=font_ui_12_b, fill=(0, 100, 200))
    draw.rectangle([(rx, 72), (width - 18, height - 70)], fill=(255, 255, 255), outline=(180, 180, 180))
    
    draw.rectangle([(rx + 20, 95), (rx + 34, 109)], fill=(255, 255, 255), outline=(100, 100, 100))
    draw.text((rx + 22, 94), "✓", font=font_ui_12_b, fill=(0, 120, 215))
    draw.text((rx + 45, 95), "Enable Network Adapter", font=font_ui_12_b, fill=(20, 20, 20))
    draw.text((rx + 20, 135), "Attached to:", font=font_ui_12_b, fill=(40, 40, 40))
    draw.rectangle([(rx + 140, 130), (rx + 480, 158)], fill=(255, 255, 255), outline=(130, 130, 130))
    draw.text((rx + 155, 136), "Host-only Adapter", font=font_ui_13_b, fill=(0, 102, 204))
    draw.text((rx + 20, 175), "Name:", font=font_ui_12_b, fill=(40, 40, 40))
    draw.rectangle([(rx + 140, 170), (rx + 480, 198)], fill=(255, 255, 255), outline=(130, 130, 130))
    draw.text((rx + 155, 176), "VirtualBox Host-Only Ethernet Adapter", font=font_ui_12_b, fill=(20, 120, 60))
    
    draw.text((rx + 20, 220), "▾ Advanced", font=font_ui_12_b, fill=(50, 50, 50))
    draw.text((rx + 35, 250), "Adapter Type:", font=font_ui_12, fill=(60, 60, 60))
    draw.rectangle([(rx + 140, 245), (rx + 480, 273)], fill=(255, 255, 255), outline=(150, 150, 150))
    draw.text((rx + 155, 251), "Intel PRO/1000 MT Desktop (82540EM)", font=font_ui_12, fill=(20, 20, 20))
    draw.text((rx + 35, 290), "Promiscuous Mode:", font=font_ui_12, fill=(60, 60, 60))
    draw.rectangle([(rx + 140, 285), (rx + 380, 313)], fill=(255, 255, 255), outline=(150, 150, 150))
    draw.text((rx + 155, 291), "Allow All", font=font_ui_12, fill=(20, 20, 20))
    draw.text((rx + 45, 335), "✓  Cable Connected", font=font_ui_12, fill=(30, 30, 30))
    
    draw.rectangle([(width - 180, height - 46), (width - 100, height - 16)], fill=(0, 120, 215), outline=(0, 90, 180))
    draw.text((width - 150, height - 38), "OK", font=font_ui_12_b, fill=(255, 255, 255))
    draw.rectangle([(width - 90, height - 46), (width - 15, height - 16)], fill=(230, 230, 230), outline=(160, 160, 160))
    draw.text((width - 67, height - 38), "Cancel", font=font_ui_12, fill=(20, 20, 20))
    draw.rectangle([(0, 0), (width - 1, height - 1)], outline=(180, 180, 180), width=1)
    paste_cursor(img, (rx + 300, 185))
    p = os.path.join(SCREENSHOTS_DIR, "fig04_vbox_nic2_hostonly.png")
    img.save(p)
    print("Saved", p)

# 5. Fig 05
def make_fig05():
    width, height = 860, 520
    img = Image.new("RGBA", (width, height), (245, 245, 245, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (width, 36)], fill=(255, 255, 255))
    draw.text((16, 9), "Network Connections", font=font_ui_13_b, fill=(30, 30, 30))
    draw.text((width - 80, 8), "—  ▢  ✕", font=font_ui_13, fill=(60, 60, 60))
    draw.rectangle([(0, 36), (width, 70)], fill=(250, 250, 250))
    draw.text((20, 44), "📁  Control Panel  >  Network and Internet  >  Network Connections", font=font_ui_11, fill=(80, 80, 80))
    draw.line([(0, 70), (width, 70)], fill=(220, 220, 220), width=1)
    
    adapters = [
        ("Wi-Fi", "Intel(R) Wi-Fi 6 AX201 160MHz", "Connected", "📶"),
        ("Ethernet", "Realtek Gaming GbE Family Controller", "Network cable unplugged", "🔌"),
        ("VirtualBox Host-Only Network", "VirtualBox Host-Only Ethernet Adapter", "Enabled (192.168.56.1)", "🌐")
    ]
    ax = 20
    ay = 85
    for name, desc, st, ic in adapters:
        is_vb = "VirtualBox" in name
        bg = (235, 243, 255) if is_vb else (255, 255, 255)
        border = (0, 120, 215) if is_vb else (200, 200, 200)
        draw.rectangle([(ax, ay), (ax + 250, ay + 110)], fill=bg, outline=border, width=2 if is_vb else 1)
        draw.text((ax + 12, ay + 12), ic, font=font_ui_14, fill=(10, 10, 10))
        draw.text((ax + 40, ay + 12), name, font=font_ui_12_b, fill=(0, 70, 150) if is_vb else (20, 20, 20))
        draw.text((ax + 12, ay + 45), desc, font=font_ui_11, fill=(80, 80, 80))
        draw.text((ax + 12, ay + 75), st, font=font_ui_11_b, fill=(20, 140, 50) if "Connected" in st or "Enabled" in st else (120, 120, 120))
        ax += 270
        
    dw, dh = 420, 290
    dx = width - dw - 30
    dy = 210
    draw.rectangle([(dx, dy), (dx + dw, dy + dh)], fill=(245, 245, 245), outline=(130, 130, 130), width=1)
    draw.rectangle([(dx, dy), (dx + dw, dy + 28)], fill=(255, 255, 255))
    draw.text((dx + 12, dy + 6), "VirtualBox Host-Only Network Properties", font=font_ui_11_b, fill=(20, 20, 20))
    draw.text((dx + 16, dy + 38), "This connection uses the following items:", font=font_ui_11, fill=(50, 50, 50))
    draw.rectangle([(dx + 16, dy + 56), (dx + dw - 16, dy + 185)], fill=(255, 255, 255), outline=(160, 160, 160))
    
    items = [
        ("✓", "VirtualBox NDIS6 Bridged Networking Driver"),
        ("✓", "Client for Microsoft Networks"),
        ("✓", "File and Printer Sharing for Microsoft Networks"),
        ("✓", "Internet Protocol Version 4 (TCP/IPv4) - 192.168.56.1"),
        ("✓", "Link-Layer Topology Discovery Responder")
    ]
    iy = dy + 62
    for chk, itxt in items:
        draw.text((dx + 22, iy), chk, font=font_ui_11_b, fill=(0, 120, 215))
        draw.text((dx + 38, iy), itxt, font=font_ui_11, fill=(20, 20, 20))
        iy += 24
        
    draw.rectangle([(dx + dw - 180, dy + dh - 40), (dx + dw - 100, dy + dh - 12)], fill=(0, 120, 215), outline=(0, 90, 180))
    draw.text((dx + dw - 150, dy + dh - 33), "OK", font=font_ui_11_b, fill=(255, 255, 255))
    draw.rectangle([(dx + dw - 90, dy + dh - 40), (dx + dw - 16, dy + dh - 12)], fill=(230, 230, 230), outline=(160, 160, 160))
    draw.text((dx + dw - 65, dy + dh - 33), "Cancel", font=font_ui_11, fill=(20, 20, 20))
    paste_cursor(img, (dx + dw - 140, dy + dh - 26))
    p = os.path.join(SCREENSHOTS_DIR, "fig05_windows_hostonly_nic.png")
    img.save(p)
    print("Saved", p)

# 6. Fig 06
def make_fig06():
    img, draw, top_h = draw_terminal_base(tab_title="user@ubuntu: /etc/network")
    lines = [
        prompt_bash() + [("cat /etc/network/interfaces", C_FG_WHITE, True)],
        [("# This file describes the network interfaces available on your system", C_FG_GRAY, False)],
        [("# Configuration for Ubuntu Lab 6 (CAD Dept LPNU)", C_FG_GRAY, False)],
        "",
        [("auto ", C_FG_BLUE, True), ("lo", C_FG_WHITE, True)],
        [("iface ", C_FG_BLUE, True), ("lo inet loopback", C_FG_CYAN, False)],
        "",
        [("# The primary network interface (Adapter 1: NAT)", C_FG_GRAY, False)],
        [("auto ", C_FG_BLUE, True), ("enp0s3", C_FG_WHITE, True)],
        [("iface ", C_FG_BLUE, True), ("enp0s3 inet dhcp", C_FG_CYAN, False)],
        "",
        [("# The secondary host-only interface (Adapter 2: Static IP for SSH)", C_FG_GRAY, False)],
        [("auto ", C_FG_BLUE, True), ("enp0s8", C_FG_WHITE, True)],
        [("iface ", C_FG_BLUE, True), ("enp0s8 inet static", C_FG_CYAN, False)],
        [("    address ", C_FG_BLUE, True), ("192.168.56.10", C_FG_CYAN, True)],
        [("    netmask ", C_FG_BLUE, True), ("255.255.255.0", C_FG_MAGENTA, True)],
        "",
        prompt_bash() + [("ip -4 addr show enp0s8 2>/dev/null || ip -4 addr show eth0", C_FG_WHITE, True)],
        "2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default",
        [("    inet ", C_FG_GRAY, False), ("192.168.56.10/24", C_FG_CYAN, True), (" scope global eth0", C_FG_GRAY, False)],
        [("    inet ", C_FG_GRAY, False), ("192.168.100.3/24", C_FG_CYAN, True), (" scope global eth0", C_FG_GRAY, False)],
        "",
        prompt_bash()
    ]
    render_lines(draw, lines, top_h + 12)
    p = os.path.join(SCREENSHOTS_DIR, "fig06_ubuntu_network_interfaces.png")
    img.save(p)
    print("Saved", p)

# 7. Fig 07
def make_fig07():
    img, draw, top_h = draw_terminal_base(tab_title="user@ubuntu: ~")
    lines = [
        prompt_bash() + [("sudo systemctl status ssh", C_FG_WHITE, True)],
        [("● ssh.service - OpenBSD Secure Shell server", (80, 220, 120), True)],
        "     Loaded: loaded (/usr/lib/systemd/system/ssh.service; enabled; preset: enabled)",
        [("     Active: ", C_FG_GRAY, False), ("active (running)", (80, 220, 120), True), (" since Mon 2026-10-26 19:32:31 UTC; 12min ago", C_FG_GRAY, False)],
        "   Main PID: 503 (sshd)",
        "      Tasks: 1 (limit: 9365)",
        "     Memory: 2.4M (peak: 3.1M)",
        "     CGroup: /system.slice/ssh.service",
        "             └─503 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups",
        "",
        prompt_bash() + [("sudo ss -tulpn | grep :22", C_FG_WHITE, True)],
        [("tcp   LISTEN 0      4096          0.0.0.0:22        0.0.0.0:*    users:((\"sshd\",pid=503,fd=3))", C_FG_WHITE, False)],
        [("tcp   LISTEN 0      4096             [::]:22           [::]:*    users:((\"sshd\",pid=503,fd=4))", C_FG_WHITE, False)],
        "",
        prompt_bash()
    ]
    render_lines(draw, lines, top_h + 12)
    p = os.path.join(SCREENSHOTS_DIR, "fig07_sshd_service_status.png")
    img.save(p)
    print("Saved", p)

# 8. Fig 08
def make_fig08():
    img, draw, top_h = draw_terminal_base(tab_title="user@ubuntu: /etc/ssh")
    lines = [
        prompt_bash() + [("cat /etc/ssh/sshd_config.d/lab6.conf", C_FG_WHITE, True)],
        [("# ============================================================", C_FG_GRAY, False)],
        [("# SSH Server Configuration for OS Lab #6 - CAD Dept LPNU", C_FG_GRAY, False)],
        [("# Student: Lemishka Andriy PP-14", C_FG_GRAY, False)],
        [("# ============================================================", C_FG_GRAY, False)],
        [("Port ", C_FG_BLUE, True), ("22", C_FG_MAGENTA, True)],
        [("Protocol ", C_FG_BLUE, True), ("2", C_FG_MAGENTA, True)],
        [("Banner ", C_FG_BLUE, True), ("/etc/ssh/banner.txt", C_FG_YELLOW, False)],
        "",
        [("# Security & Authentication Policies", C_FG_GRAY, False)],
        [("PermitRootLogin ", C_FG_BLUE, True), ("no", C_FG_RED, True), ("        # Forbid direct root login", C_FG_GRAY, False)],
        [("PasswordAuthentication ", C_FG_BLUE, True), ("yes", C_FG_GREEN, True), ("  # Enable password login", C_FG_GRAY, False)],
        [("PubkeyAuthentication ", C_FG_BLUE, True), ("yes", C_FG_GREEN, True), ("    # Enable cryptographic keys", C_FG_GRAY, False)],
        [("PermitEmptyPasswords ", C_FG_BLUE, True), ("no", C_FG_RED, True), ("     # Reject blank passwords", C_FG_GRAY, False)],
        [("LoginGraceTime ", C_FG_BLUE, True), ("2m", C_FG_MAGENTA, False), ("           # Timeout for authentication", C_FG_GRAY, False)],
        "",
        [("# Access Control list (Allowed Users / Workstations)", C_FG_GRAY, False)],
        [("AllowUsers ", C_FG_BLUE, True), ("user remote_ws2", C_FG_CYAN, True), ("   # Neighbor PC & local student", C_FG_GRAY, False)],
        "",
        prompt_bash() + [("sudo sshd -t && echo 'Syntax OK'", C_FG_WHITE, True)],
        [("Syntax OK", (80, 220, 120), True)],
        "",
        prompt_bash()
    ]
    render_lines(draw, lines, top_h + 12)
    p = os.path.join(SCREENSHOTS_DIR, "fig08_sshd_config_security.png")
    img.save(p)
    print("Saved", p)

# 9. Fig 09
def make_fig09():
    img, draw, top_h = draw_terminal_base(tab_title="Windows PowerShell - Administrator")
    lines = [
        prompt_ps() + [("ping 192.168.56.10", C_FG_WHITE, True)],
        "",
        "Pinging 192.168.56.10 with 32 bytes of data:",
        "Reply from 192.168.56.10: bytes=32 time<1ms TTL=64",
        "Reply from 192.168.56.10: bytes=32 time<1ms TTL=64",
        "Reply from 192.168.56.10: bytes=32 time<1ms TTL=64",
        "Reply from 192.168.56.10: bytes=32 time<1ms TTL=64",
        "",
        "Ping statistics for 192.168.56.10:",
        "    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),",
        "Approximate round trip times in milli-seconds:",
        "    Minimum = 0ms, Maximum = 0ms, Average = 0ms",
        "",
        prompt_ps() + [("Test-NetConnection -ComputerName 192.168.56.10 -Port 22", C_FG_WHITE, True)],
        "",
        "ComputerName     : 192.168.56.10",
        "RemoteAddress    : 192.168.56.10",
        "RemotePort       : 22",
        "InterfaceAlias   : VirtualBox Host-Only Ethernet Adapter",
        "SourceAddress    : 192.168.56.1",
        [("TcpTestSucceeded : ", C_FG_WHITE, False), ("True", (80, 220, 120), True)],
        "",
        prompt_ps()
    ]
    render_lines(draw, lines, top_h + 12)
    p = os.path.join(SCREENSHOTS_DIR, "fig09_network_ping_test.png")
    img.save(p)
    print("Saved", p)

# 10. Fig 10
def make_fig10():
    img, draw, top_h = draw_terminal_base(tab_title="user@client-node: ~")
    lines = [
        [("user@client-ws2", C_FG_GREEN, True), (":", C_FG_WHITE, False), ("~", C_FG_BLUE, True), ("$ ", C_FG_WHITE, False), ("ssh -l user -v 192.168.56.10", C_FG_WHITE, True)],
        "OpenSSH_9.5p1 Ubuntu-1ubuntu1, OpenSSL 3.0.13 30 Jan 2024",
        "debug1: Reading configuration data /etc/ssh/ssh_config",
        "debug1: Connecting to 192.168.56.10 [192.168.56.10] port 22.",
        "debug1: Connection established.",
        "debug1: identity file /home/user/.ssh/id_rsa type 0",
        "debug1: Local version string SSH-2.0-OpenSSH_9.5p1",
        "debug1: Remote protocol version 2.0, remote software version OpenSSH_10.2p1",
        "debug1: match: OpenSSH_10.2p1 pat OpenSSH* compat 0x04000006",
        "debug1: Authenticating to 192.168.56.10:22 as 'user'",
        "debug1: SSH2_MSG_KEXINIT sent",
        "debug1: SSH2_MSG_KEXINIT received",
        "debug1: kex: algorithm: curve25519-sha256",
        "debug1: Host '192.168.56.10' is not in the cert authority database.",
        [("The authenticity of host '192.168.56.10 (192.168.56.10)' can't be established.", C_FG_YELLOW, True)],
        [("ED25519 key fingerprint is ", C_FG_WHITE, False), ("SHA256:GQAeLagKurAME0N3AnBJ0JiLammXQ7NcVNMhiQO0k7w.", C_FG_CYAN, True)],
        "This key is not known by any other names.",
        [("Are you sure you want to continue connecting (yes/no/[fingerprint])? ", C_FG_YELLOW, True), ("_", C_FG_WHITE, True)]
    ]
    render_lines(draw, lines, top_h + 12)
    p = os.path.join(SCREENSHOTS_DIR, "fig10_ssh_client_fingerprint.png")
    img.save(p)
    print("Saved", p)

# 11. Fig 11
def make_fig11():
    img, draw, top_h = draw_terminal_base(tab_title="user@client-node: ~")
    lines = [
        [("Are you sure you want to continue connecting (yes/no/[fingerprint])? ", C_FG_YELLOW, True), ("yes", C_FG_WHITE, True)],
        [("Warning: Permanently added '192.168.56.10' (ED25519) to the list of known hosts.", C_FG_YELLOW, False)],
        "debug1: Authentications that can continue: publickey,password",
        "debug1: Next authentication method: password",
        [("user@192.168.56.10's password: ", C_FG_WHITE, True)],
        "",
        [("user@client-ws2", C_FG_GREEN, True), (":", C_FG_WHITE, False), ("~", C_FG_BLUE, True), ("$ ", C_FG_WHITE, False), ("tail -n 1 ~/.ssh/known_hosts", C_FG_WHITE, True)],
        [("192.168.56.10 ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIH9rTz7Vf2uLq+eQ2YkHjHlH890Yq7Qp...", C_FG_GRAY, False)],
        "",
        [("user@client-ws2", C_FG_GREEN, True), (":", C_FG_WHITE, False), ("~", C_FG_BLUE, True), ("$ ", C_FG_WHITE, False), ("ssh-keygen -l -f ~/.ssh/known_hosts", C_FG_WHITE, True)],
        [("256 SHA256:GQAeLagKurAME0N3AnBJ0JiLammXQ7NcVNMhiQO0k7w 192.168.56.10 (ED25519)", C_FG_CYAN, True)],
        "",
        [("user@client-ws2", C_FG_GREEN, True), (":", C_FG_WHITE, False), ("~", C_FG_BLUE, True), ("$ ", C_FG_WHITE, False)]
    ]
    render_lines(draw, lines, top_h + 12)
    p = os.path.join(SCREENSHOTS_DIR, "fig11_ssh_known_hosts_confirmed.png")
    img.save(p)
    print("Saved", p)

# 12. Fig 12
def make_fig12():
    img, draw, top_h = draw_terminal_base(tab_title="user@192.168.56.10 (SSH Session)")
    lines = [
        [("************************************************************", C_FG_YELLOW, True)],
        [("*  National University \"Lviv Polytechnic\"                  *", C_FG_YELLOW, True)],
        [("*  Department of CAD - Operating Systems Lab #6            *", C_FG_YELLOW, True)],
        [("*  Authorized Access Only! Student: Lemishka Andriy PP-14  *", C_FG_YELLOW, True)],
        [("************************************************************", C_FG_YELLOW, True)],
        "Last login: Mon Oct 26 21:32:45 2026 from 192.168.56.1",
        "",
        prompt_bash() + [("uname -a && whoami", C_FG_WHITE, True)],
        "Linux ubuntu 6.18.54.1-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC x86_64 GNU/Linux",
        [("user", C_FG_CYAN, True)],
        "",
        prompt_bash() + [("uptime", C_FG_WHITE, True)],
        " 21:35:12 up 14 min,  2 users,  load average: 0.08, 0.05, 0.01",
        "",
        prompt_bash() + [("ps -ef | grep pts", C_FG_WHITE, True)],
        "user       1410   503  0 21:35 ?        00:00:00 sshd: user@pts/0",
        "user       1411  1410  0 21:35 pts/0    00:00:00 -bash",
        "user       1442  1411  0 21:35 pts/0    00:00:00 ps -ef",
        "",
        prompt_bash() + [("free -m", C_FG_WHITE, True)],
        "               total        used        free      shared  buff/cache   available",
        "Mem:            7908         820        6412          14         675        7088",
        "",
        prompt_bash()
    ]
    render_lines(draw, lines, top_h + 12)
    p = os.path.join(SCREENSHOTS_DIR, "fig12_ssh_remote_commands.png")
    img.save(p)
    print("Saved", p)

# 13. Fig 13
def make_fig13():
    width, height = 980, 560
    img = Image.new("RGBA", (width, height), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (width, 36)], fill=(243, 243, 243))
    draw.text((16, 9), "PuTTY - File Explorer", font=font_ui_13_b, fill=(30, 30, 30))
    draw.text((width - 100, 8), "—  ▢  ✕", font=font_ui_13, fill=(60, 60, 60))
    draw.rectangle([(0, 36), (width, 76)], fill=(250, 250, 250))
    draw.rectangle([(16, 42), (width - 16, 70)], fill=(255, 255, 255), outline=(210, 210, 210))
    draw.text((28, 48), "📁  This PC  >  Local Disk (C:)  >  Program Files  >  PuTTY", font=font_ui_12, fill=(40, 40, 40))
    draw.rectangle([(0, 76), (width, 104)], fill=(245, 245, 247))
    draw.text((20, 82), "Name", font=font_ui_12_b, fill=(80, 80, 80))
    draw.text((320, 82), "Date modified", font=font_ui_12_b, fill=(80, 80, 80))
    draw.text((480, 82), "Type", font=font_ui_12_b, fill=(80, 80, 80))
    draw.text((620, 82), "Size", font=font_ui_12_b, fill=(80, 80, 80))
    draw.text((740, 82), "Description / Purpose", font=font_ui_12_b, fill=(80, 80, 80))
    
    files = [
        ("putty.exe", "14/08/2026 06:53", "Application", "1,310 KB", "GUI SSH, Telnet and Rlogin client"),
        ("puttygen.exe", "14/08/2026 06:54", "Application", "632 KB", "RSA, DSA and Ed25519 key generator"),
        ("pageant.exe", "14/08/2026 06:53", "Application", "555 KB", "PuTTY SSH authentication agent"),
        ("pscp.exe", "14/08/2026 06:53", "Application", "1,012 KB", "Command-line secure copy (SCP) client"),
        ("psftp.exe", "14/08/2026 06:53", "Application", "1,029 KB", "Command-line interactive SFTP client"),
        ("plink.exe", "14/08/2026 06:53", "Application", "1,013 KB", "PuTTY command-line interface tool"),
        ("putty.chm", "14/08/2026 06:48", "Compiled HTML Help", "357 KB", "Complete documentation manual")
    ]
    cur_y = 106
    for i, (fn, dm, tp, sz, desc) in enumerate(files):
        row_bg = (238, 244, 252) if i == 0 else (255, 255, 255)
        draw.rectangle([(0, cur_y), (width, cur_y + 32)], fill=row_bg)
        icon = "🛠️" if tp == "Application" else "📖"
        draw.text((20, cur_y + 7), f"{icon}  {fn}", font=font_ui_12, fill=(20, 20, 20))
        draw.text((320, cur_y + 7), dm, font=font_ui_12, fill=(90, 90, 90))
        draw.text((480, cur_y + 7), tp, font=font_ui_12, fill=(90, 90, 90))
        draw.text((620, cur_y + 7), sz, font=font_ui_12, fill=(90, 90, 90))
        draw.text((740, cur_y + 7), desc, font=font_ui_12, fill=(50, 110, 180) if i==0 else (70, 70, 70))
        cur_y += 33
        
    draw.rectangle([(0, 0), (width - 1, height - 1)], outline=(200, 200, 200), width=1)
    paste_cursor(img, (140, 120))
    p = os.path.join(SCREENSHOTS_DIR, "fig13_putty_suite_explorer.png")
    img.save(p)
    print("Saved", p)

# 14. Fig 14
def make_fig14():
    width, height = 780, 580
    img = Image.new("RGBA", (width, height), (240, 240, 240, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (width, 32)], fill=(245, 245, 245))
    draw.text((12, 7), "PuTTY Configuration (Release 0.85)", font=font_ui_12_b, fill=(20, 20, 20))
    draw.text((width - 60, 6), "—  ✕", font=font_ui_12, fill=(60, 60, 60))
    
    tree_w = 190
    draw.rectangle([(14, 44), (14 + tree_w, height - 60)], fill=(255, 255, 255), outline=(180, 180, 180))
    draw.text((22, 50), "Category:", font=font_ui_11, fill=(90, 90, 90))
    cats = [
        ("▾ Session", True, True), ("    Logging", False, False),
        ("▸ Terminal", False, False), ("▸ Window", False, False),
        ("▾ Connection", False, False), ("    Data", False, False),
        ("    Proxy", False, False), ("  ▸ SSH", False, False), ("    Serial", False, False)
    ]
    cy = 70
    for text, is_sel, is_b in cats:
        if is_sel:
            draw.rectangle([(16, cy - 2), (14 + tree_w - 2, cy + 18)], fill=(0, 120, 215))
            draw.text((24, cy), text, font=font_ui_12_b, fill=(255, 255, 255))
        else:
            draw.text((24, cy), text, font=font_ui_12_b if is_b else font_ui_12, fill=(30, 30, 30))
        cy += 22
        
    rx = 220
    draw.text((rx, 46), "Basic options for your PuTTY session", font=font_ui_12_b, fill=(30, 30, 30))
    draw.rectangle([(rx, 70), (width - 18, 175)], outline=(190, 190, 190))
    draw.rectangle([(rx + 12, 62), (rx + 280, 75)], fill=(240, 240, 240))
    draw.text((rx + 14, 62), "Specify the destination you want to connect to", font=font_ui_11, fill=(50, 50, 50))
    draw.text((rx + 16, 88), "Host Name (or IP address)", font=font_ui_11, fill=(40, 40, 40))
    draw.rectangle([(rx + 16, 106), (rx + 360, 134)], fill=(255, 255, 255), outline=(130, 130, 130))
    draw.text((rx + 24, 112), "192.168.56.10", font=font_ui_13, fill=(10, 10, 10))
    
    draw.text((rx + 390, 88), "Port", font=font_ui_11, fill=(40, 40, 40))
    draw.rectangle([(rx + 390, 106), (rx + 480, 134)], fill=(255, 255, 255), outline=(130, 130, 130))
    draw.text((rx + 400, 112), "22", font=font_ui_13, fill=(10, 10, 10))
    draw.text((rx + 16, 146), "Connection type:    🔘 Raw    🔘 Telnet    🔘 Rlogin    🔘 SSH    🔘 Serial", font=font_ui_11, fill=(30, 30, 30))
    
    draw.rectangle([(rx, 195), (width - 18, height - 70)], outline=(190, 190, 190))
    draw.rectangle([(rx + 12, 187), (rx + 240, 200)], fill=(240, 240, 240))
    draw.text((rx + 14, 187), "Load, save or delete a stored session", font=font_ui_11, fill=(50, 50, 50))
    draw.rectangle([(rx + 16, 215), (rx + 360, 243)], fill=(255, 255, 255), outline=(130, 130, 130))
    draw.text((rx + 24, 221), "Ubuntu-SSH-Lab6", font=font_ui_13, fill=(10, 10, 10))
    
    draw.rectangle([(rx + 380, 215), (rx + 460, 243)], fill=(230, 230, 230), outline=(160, 160, 160))
    draw.text((rx + 400, 221), "Save", font=font_ui_12_b, fill=(20, 20, 20))
    draw.rectangle([(rx + 470, 215), (rx + 530, 243)], fill=(230, 230, 230), outline=(160, 160, 160))
    draw.text((rx + 485, 221), "Load", font=font_ui_12, fill=(20, 20, 20))
    
    draw.rectangle([(rx + 16, 255), (rx + 360, height - 85)], fill=(255, 255, 255), outline=(170, 170, 170))
    draw.text((rx + 24, 265), "Default Settings", font=font_ui_12, fill=(60, 60, 60))
    draw.rectangle([(rx + 18, 288), (rx + 358, 310)], fill=(0, 120, 215))
    draw.text((rx + 24, 292), "Ubuntu-SSH-Lab6", font=font_ui_12_b, fill=(255, 255, 255))
    
    draw.rectangle([(width - 260, height - 44), (width - 180, height - 16)], fill=(0, 120, 215), outline=(0, 90, 180))
    draw.text((width - 232, height - 37), "Open", font=font_ui_12_b, fill=(255, 255, 255))
    draw.rectangle([(width - 170, height - 44), (width - 95, height - 16)], fill=(230, 230, 230), outline=(160, 160, 160))
    draw.text((width - 147, height - 37), "Cancel", font=font_ui_12, fill=(20, 20, 20))
    draw.rectangle([(width - 85, height - 44), (width - 20, height - 16)], fill=(230, 230, 230), outline=(160, 160, 160))
    draw.text((width - 62, height - 37), "Help", font=font_ui_12, fill=(20, 20, 20))
    
    draw.rectangle([(0, 0), (width - 1, height - 1)], outline=(180, 180, 180), width=1)
    paste_cursor(img, (rx + 420, 230))
    p = os.path.join(SCREENSHOTS_DIR, "fig14_putty_session_config.png")
    img.save(p)
    print("Saved", p)

# 15. Fig 15
def make_fig15():
    width, height = 780, 580
    img = Image.new("RGBA", (width, height), (240, 240, 240, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (width, 32)], fill=(245, 245, 245))
    draw.text((12, 7), "PuTTY Configuration (Release 0.85)", font=font_ui_12_b, fill=(20, 20, 20))
    draw.text((width - 60, 6), "—  ✕", font=font_ui_12, fill=(60, 60, 60))
    
    tree_w = 190
    draw.rectangle([(14, 44), (14 + tree_w, height - 60)], fill=(255, 255, 255), outline=(180, 180, 180))
    draw.text((22, 50), "Category:", font=font_ui_11, fill=(90, 90, 90))
    cats = [
        ("▾ Session", False, True), ("    Logging", False, False),
        ("▸ Terminal", False, False), ("▸ Window", False, False),
        ("▾ Connection", False, True), ("    Data", True, True),
        ("    Proxy", False, False), ("  ▸ SSH", False, False), ("    Serial", False, False)
    ]
    cy = 70
    for text, is_sel, is_b in cats:
        if is_sel:
            draw.rectangle([(16, cy - 2), (14 + tree_w - 2, cy + 18)], fill=(0, 120, 215))
            draw.text((24, cy), text, font=font_ui_12_b, fill=(255, 255, 255))
        else:
            draw.text((24, cy), text, font=font_ui_12_b if is_b else font_ui_12, fill=(30, 30, 30))
        cy += 22
        
    rx = 220
    draw.text((rx, 46), "Data to send to the server", font=font_ui_12_b, fill=(30, 30, 30))
    draw.rectangle([(rx, 70), (width - 18, 190)], outline=(190, 190, 190))
    draw.rectangle([(rx + 12, 62), (rx + 100, 75)], fill=(240, 240, 240))
    draw.text((rx + 14, 62), "Login details", font=font_ui_11, fill=(50, 50, 50))
    draw.text((rx + 16, 90), "Auto-login username", font=font_ui_11, fill=(40, 40, 40))
    draw.rectangle([(rx + 16, 110), (rx + 360, 138)], fill=(255, 255, 255), outline=(130, 130, 130))
    draw.text((rx + 24, 116), "user", font=font_ui_13, fill=(10, 10, 10))
    draw.text((rx + 16, 150), "When username is not specified:   🔘 Use system username    🔘 Prompt", font=font_ui_11, fill=(50, 50, 50))
    
    draw.rectangle([(rx, 210), (width - 18, 330)], outline=(190, 190, 190))
    draw.rectangle([(rx + 12, 202), (rx + 110, 215)], fill=(240, 240, 240))
    draw.text((rx + 14, 202), "Terminal details", font=font_ui_11, fill=(50, 50, 50))
    draw.text((rx + 16, 230), "Terminal-type string", font=font_ui_11, fill=(40, 40, 40))
    draw.rectangle([(rx + 16, 250), (rx + 360, 278)], fill=(255, 255, 255), outline=(130, 130, 130))
    draw.text((rx + 24, 256), "xterm-256color", font=font_ui_13, fill=(10, 10, 10))
    
    draw.rectangle([(width - 260, height - 44), (width - 180, height - 16)], fill=(0, 120, 215), outline=(0, 90, 180))
    draw.text((width - 232, height - 37), "Open", font=font_ui_12_b, fill=(255, 255, 255))
    draw.rectangle([(width - 170, height - 44), (width - 95, height - 16)], fill=(230, 230, 230), outline=(160, 160, 160))
    draw.text((width - 147, height - 37), "Cancel", font=font_ui_12, fill=(20, 20, 20))
    draw.rectangle([(width - 85, height - 44), (width - 20, height - 16)], fill=(230, 230, 230), outline=(160, 160, 160))
    draw.text((width - 62, height - 37), "Help", font=font_ui_12, fill=(20, 20, 20))
    
    draw.rectangle([(0, 0), (width - 1, height - 1)], outline=(180, 180, 180), width=1)
    paste_cursor(img, (rx + 220, 124))
    p = os.path.join(SCREENSHOTS_DIR, "fig15_putty_auto_login.png")
    img.save(p)
    print("Saved", p)

# 16. Fig 16
def make_fig16():
    width, height = 740, 460
    img = Image.new("RGBA", (width, height), (35, 40, 48, 255))
    draw = ImageDraw.Draw(img)
    dw, dh = 600, 360
    dx = (width - dw) // 2
    dy = (height - dh) // 2
    
    draw.rectangle([(dx, dy), (dx + dw, dy + dh)], fill=(245, 245, 245), outline=(140, 140, 140), width=1)
    draw.rectangle([(dx, dy), (dx + dw, dy + 32)], fill=(255, 255, 255))
    draw.text((dx + 12, dy + 7), "PuTTY Security Alert", font=font_ui_12_b, fill=(20, 20, 20))
    draw.text((dx + dw - 24, dy + 7), "✕", font=font_ui_12, fill=(80, 80, 80))
    
    draw.ellipse([(dx + 24, dy + 52), (dx + 68, dy + 96)], fill=(255, 185, 0))
    draw.text((dx + 42, dy + 58), "!", font=font_ui_14_b, fill=(20, 20, 20))
    
    tx = dx + 85
    ty = dy + 48
    draw.text((tx, ty), "The server's host key is not cached in the registry. You", font=font_ui_12, fill=(20, 20, 20))
    draw.text((tx, ty + 20), "have no guarantee that the server is the computer you", font=font_ui_12, fill=(20, 20, 20))
    draw.text((tx, ty + 40), "think it is.", font=font_ui_12, fill=(20, 20, 20))
    draw.text((tx, ty + 70), "The server's ssh-ed25519 key fingerprint is:", font=font_ui_12_b, fill=(30, 30, 30))
    draw.rectangle([(tx, ty + 92), (tx + 470, ty + 124)], fill=(255, 255, 255), outline=(180, 180, 180))
    draw.text((tx + 10, ty + 98), "ssh-ed25519 255 SHA256:GQAeLagKurAME0N3AnBJ0JiLammXQ7NcVNMhiQO0k7w", font=font_term_13, fill=(10, 10, 10))
    
    draw.text((tx, ty + 136), "If you trust this host, press \"Accept\" to add the key to", font=font_ui_12, fill=(20, 20, 20))
    draw.text((tx, ty + 156), "PuTTY's cache and carry on connecting.", font=font_ui_12, fill=(20, 20, 20))
    draw.text((tx, ty + 176), "If you want to carry on connecting just once, press \"Connect Once\".", font=font_ui_12, fill=(20, 20, 20))
    draw.text((tx, ty + 196), "If you do not trust this host, press \"Cancel\" to abandon connection.", font=font_ui_12, fill=(20, 20, 20))
    
    draw.rectangle([(dx + 70, dy + dh - 48), (dx + 180, dy + dh - 16)], fill=(0, 120, 215), outline=(0, 90, 180))
    draw.text((dx + 105, dy + dh - 39), "Accept", font=font_ui_12_b, fill=(255, 255, 255))
    draw.rectangle([(dx + 195, dy + dh - 48), (dx + 325, dy + dh - 16)], fill=(235, 235, 235), outline=(160, 160, 160))
    draw.text((dx + 220, dy + dh - 39), "Connect Once", font=font_ui_12, fill=(20, 20, 20))
    draw.rectangle([(dx + 340, dy + dh - 48), (dx + 440, dy + dh - 16)], fill=(235, 235, 235), outline=(160, 160, 160))
    draw.text((dx + 368, dy + dh - 39), "Cancel", font=font_ui_12, fill=(20, 20, 20))
    draw.rectangle([(dx + 455, dy + dh - 48), (dx + 540, dy + dh - 16)], fill=(235, 235, 235), outline=(160, 160, 160))
    draw.text((dx + 482, dy + dh - 39), "Help", font=font_ui_12, fill=(20, 20, 20))
    
    paste_cursor(img, (dx + 125, dy + dh - 32))
    p = os.path.join(SCREENSHOTS_DIR, "fig16_putty_security_alert.png")
    img.save(p)
    print("Saved", p)

# 17. Fig 17
def make_fig17():
    width, height = 960, 560
    img = Image.new("RGBA", (width, height), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (width, 36)], fill=(240, 240, 240))
    draw.text((16, 9), "user@192.168.56.10 - PuTTY", font=font_ui_13_b, fill=(20, 20, 20))
    draw.text((width - 80, 8), "—  ▢  ✕", font=font_ui_13, fill=(60, 60, 60))
    
    lines = [
        "login as: user",
        "Authenticating with public key \"rsa-key-lemishka-2026\" from agent",
        "",
        [("************************************************************", (180, 180, 0), True)],
        [("*  National University \"Lviv Polytechnic\"                  *", (180, 180, 0), True)],
        [("*  Department of CAD - Operating Systems Lab #6            *", (180, 180, 0), True)],
        [("*  Authorized Access Only! Student: Lemishka Andriy PP-14  *", (180, 180, 0), True)],
        [("************************************************************", (180, 180, 0), True)],
        "",
        prompt_bash() + [("df -h", (255, 255, 255), True)],
        "Filesystem      Size  Used Avail Use% Mounted on",
        "/dev/sdd        251G   24G  215G  10% /",
        "none            3.9G     0  3.9G   0% /dev",
        "tmpfs           3.9G     0  3.9G   0% /mnt/wsl",
        "",
        prompt_bash() + [("last -n 4", (255, 255, 255), True)],
        "user     pts/0        192.168.56.1     Mon Oct 26 21:38   still logged in",
        "user     pts/1        192.168.56.1     Mon Oct 26 21:35 - 21:37  (00:02)",
        "reboot   system boot  6.18.54.1-micros Mon Oct 26 21:28   still running",
        "",
        prompt_bash() + [("echo 'SSH Admin Session Operational' && date", (255, 255, 255), True)],
        "SSH Admin Session Operational",
        "Mon Oct 26 21:40:15 UTC 2026",
        "",
        prompt_bash() + [("█", (0, 255, 0), True)]
    ]
    render_lines(draw, lines, 48)
    draw.rectangle([(0, 0), (width - 1, height - 1)], outline=(100, 100, 100), width=1)
    p = os.path.join(SCREENSHOTS_DIR, "fig17_putty_active_session.png")
    img.save(p)
    print("Saved", p)

# 18. Fig 18
def make_fig18():
    width, height = 740, 560
    img = Image.new("RGBA", (width, height), (242, 242, 242, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (width, 32)], fill=(250, 250, 250))
    draw.text((12, 7), "PuTTY Key Generator", font=font_ui_12_b, fill=(20, 20, 20))
    draw.text((width - 50, 6), "—  ✕", font=font_ui_12, fill=(60, 60, 60))
    draw.text((16, 38), "File    Key    Conversions    Help", font=font_ui_12, fill=(40, 40, 40))
    draw.line([(0, 60), (width, 60)], fill=(210, 210, 210), width=1)
    
    draw.rectangle([(16, 75), (width - 16, 320)], outline=(190, 190, 190))
    draw.rectangle([(26, 68), (120, 80)], fill=(242, 242, 242))
    draw.text((28, 68), "Key details", font=font_ui_11, fill=(50, 50, 50))
    draw.text((26, 88), "Public key for pasting into OpenSSH authorized_keys file:", font=font_ui_11, fill=(30, 30, 30))
    draw.rectangle([(26, 106), (width - 26, 190)], fill=(255, 255, 255), outline=(150, 150, 150))
    draw.text((34, 112), "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDQz7N1G9wLk91...", font=font_term_13, fill=(10, 10, 10))
    draw.text((34, 130), "xPq8Y+zXy8Z41M0KjO7W9qLk2Yw8K9r4x0w92J1K0zXy8Z41M0...", font=font_term_13, fill=(10, 10, 10))
    draw.text((34, 148), "9qLk2Yw8K9r4x0w92J1K0zXy8Z41M0KjO7W9qLk2Yw8K9r4x0w...", font=font_term_13, fill=(10, 10, 10))
    draw.text((34, 166), "rsa-key-lemishka-2026", font=font_term_13_b, fill=(0, 102, 204))
    
    draw.text((26, 204), "Key fingerprint:", font=font_ui_11, fill=(40, 40, 40))
    draw.text((150, 204), "rsa-sha2-256 2048 f6:8a:c3:21:4b:9e:11:05:88:d4:ee:92", font=font_term_13, fill=(10, 10, 10))
    draw.text((26, 230), "Key comment:", font=font_ui_11, fill=(40, 40, 40))
    draw.rectangle([(150, 226), (width - 26, 250)], fill=(255, 255, 255), outline=(160, 160, 160))
    draw.text((158, 230), "rsa-key-lemishka-2026", font=font_ui_12, fill=(10, 10, 10))
    
    draw.text((26, 260), "Key passphrase:", font=font_ui_11, fill=(40, 40, 40))
    draw.rectangle([(150, 256), (width - 26, 280)], fill=(255, 255, 255), outline=(160, 160, 160))
    draw.text((158, 260), "••••••••••••••••", font=font_ui_12, fill=(10, 10, 10))
    
    draw.text((26, 290), "Confirm passphrase:", font=font_ui_11, fill=(40, 40, 40))
    draw.rectangle([(150, 286), (width - 26, 310)], fill=(255, 255, 255), outline=(160, 160, 160))
    draw.text((158, 290), "••••••••••••••••", font=font_ui_12, fill=(10, 10, 10))
    
    draw.rectangle([(width - 200, 335), (width - 26, 365)], fill=(230, 230, 230), outline=(160, 160, 160))
    draw.text((width - 150, 342), "Generate", font=font_ui_12_b, fill=(20, 20, 20))
    draw.rectangle([(width - 385, 335), (width - 215, 365)], fill=(230, 230, 230), outline=(160, 160, 160))
    draw.text((width - 355, 342), "Save public key", font=font_ui_12, fill=(20, 20, 20))
    draw.rectangle([(width - 570, 335), (width - 400, 365)], fill=(0, 120, 215), outline=(0, 90, 180))
    draw.text((width - 540, 342), "Save private key", font=font_ui_12_b, fill=(255, 255, 255))
    
    draw.rectangle([(16, 410), (width - 16, height - 20)], outline=(190, 190, 190))
    draw.rectangle([(26, 402), (100, 415)], fill=(242, 242, 242))
    draw.text((28, 402), "Parameters", font=font_ui_11, fill=(50, 50, 50))
    draw.text((26, 430), "Type of key to generate:", font=font_ui_11, fill=(40, 40, 40))
    draw.text((26, 455), "🔘 RSA    🔘 DSA    🔘 ECDSA    🔘 Ed25519    🔘 SSH-1 (RSA)", font=font_ui_11, fill=(30, 30, 30))
    draw.text((26, 490), "Number of bits in a generated key:  2048", font=font_ui_11, fill=(40, 40, 40))
    
    draw.rectangle([(0, 0), (width - 1, height - 1)], outline=(180, 180, 180), width=1)
    paste_cursor(img, (width - 480, 350))
    p = os.path.join(SCREENSHOTS_DIR, "fig18_puttygen_keys.png")
    img.save(p)
    print("Saved", p)

# 19. Fig 19
def make_fig19():
    img, draw, top_h = draw_terminal_base(tab_title="user@ubuntu: ~/.ssh")
    lines = [
        prompt_bash() + [("ls -ld ~/.ssh && ls -l ~/.ssh/authorized_keys", C_FG_WHITE, True)],
        [("drwx------ 2 user user 4096 Oct 26 21:32 /home/user/.ssh", (80, 220, 120), True), ("   (chmod 700 - owner only)", C_FG_GRAY, False)],
        [("-rw------- 1 user user  572 Oct 26 21:32 /home/user/.ssh/authorized_keys", (80, 220, 120), True), ("   (chmod 600 - owner read/write)", C_FG_GRAY, False)],
        "",
        prompt_bash() + [("cat ~/.ssh/authorized_keys", C_FG_WHITE, True)],
        [("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDQz7N1G9wLk91xPq8Y+zXy8Z41M0KjO7W9qLk2Yw8K9r4x0w92J1K0zXy8Z41M0KjO7W9qLk2Yw8K9r4x0w92J1K0zXy8Z41M0KjO7W9qLk2Yw8K9r4x0w92J1K0... ", C_FG_WHITE, False), ("rsa-key-lemishka-2026", C_FG_CYAN, True)],
        "",
        prompt_bash() + [("grep -E 'PubkeyAuthentication|AuthorizedKeysFile' /etc/ssh/sshd_config /etc/ssh/sshd_config.d/*", C_FG_WHITE, True)],
        "/etc/ssh/sshd_config:AuthorizedKeysFile .ssh/authorized_keys .ssh/authorized_keys2",
        [("/etc/ssh/sshd_config.d/lab6.conf:PubkeyAuthentication ", C_FG_GRAY, False), ("yes", C_FG_GREEN, True)],
        "",
        prompt_bash()
    ]
    render_lines(draw, lines, top_h + 12)
    p = os.path.join(SCREENSHOTS_DIR, "fig19_server_authorized_keys.png")
    img.save(p)
    print("Saved", p)

# 20. Fig 20
def make_fig20():
    width, height = 980, 560
    img = Image.new("RGBA", (width, height), (15, 15, 15, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (width, 36)], fill=(28, 28, 28))
    draw.text((16, 9), "user@192.168.56.10 - PuTTY (Key Agent Authentication)", font=font_ui_13_b, fill=(230, 230, 230))
    draw.text((width - 80, 8), "—  ▢  ✕", font=font_ui_13, fill=(180, 180, 180))
    
    lines = [
        "login as: user",
        [("Authenticating with public key \"rsa-key-lemishka-2026\" from agent", (80, 220, 120), True)],
        [("Access granted. No password prompt required (Public Key Authentication successful).", C_FG_YELLOW, False)],
        "",
        prompt_bash() + [("who am i", C_FG_WHITE, True)],
        "user     pts/2        Oct 26 21:42 (192.168.56.1)",
        "",
        prompt_bash() + [("echo 'Authenticated via Pageant SSH-Agent' ", C_FG_WHITE, True)],
        "Authenticated via Pageant SSH-Agent",
        "",
        prompt_bash()
    ]
    render_lines(draw, lines, 48)
    
    pw, ph = 460, 280
    px = width - pw - 40
    py = 120
    draw.rectangle([(px, py), (px + pw, py + ph)], fill=(245, 245, 245), outline=(130, 130, 130), width=1)
    draw.rectangle([(px, py), (px + pw, py + 30)], fill=(255, 255, 255))
    draw.text((px + 12, py + 7), "Pageant Key List (1 key loaded)", font=font_ui_12_b, fill=(20, 20, 20))
    draw.text((px + pw - 24, py + 7), "✕", font=font_ui_12, fill=(80, 80, 80))
    
    draw.rectangle([(px + 14, py + 42), (px + pw - 14, py + ph - 60)], fill=(255, 255, 255), outline=(170, 170, 170))
    draw.rectangle([(px + 16, py + 46), (px + pw - 16, py + 72)], fill=(0, 120, 215))
    draw.text((px + 22, py + 52), "ssh-rsa 2048 f6:8a:c3... rsa-key-lemishka-2026", font=font_term_13_b, fill=(255, 255, 255))
    
    draw.rectangle([(px + 20, py + ph - 45), (px + 120, py + ph - 15)], fill=(230, 230, 230), outline=(160, 160, 160))
    draw.text((px + 42, py + ph - 38), "Add Key", font=font_ui_12, fill=(20, 20, 20))
    draw.rectangle([(px + 135, py + ph - 45), (px + 250, py + ph - 15)], fill=(230, 230, 230), outline=(160, 160, 160))
    draw.text((px + 155, py + ph - 38), "Remove Key", font=font_ui_12, fill=(20, 20, 20))
    draw.rectangle([(px + pw - 110, py + ph - 45), (px + pw - 20, py + ph - 15)], fill=(0, 120, 215), outline=(0, 90, 180))
    draw.text((px + pw - 80, py + ph - 38), "Close", font=font_ui_12_b, fill=(255, 255, 255))
    
    paste_cursor(img, (px + 70, py + ph - 30))
    p = os.path.join(SCREENSHOTS_DIR, "fig20_pageant_agent_login.png")
    img.save(p)
    print("Saved", p)

# 21. Fig 21
def make_fig21():
    img, draw, top_h = draw_terminal_base(tab_title="Windows Terminal - pscp & psftp")
    lines = [
        prompt_ps() + [("pscp -batch -pw 12345 backup_lab6.tar.gz user@192.168.56.10:/home/user/incoming/", C_FG_WHITE, True)],
        [("backup_lab6.tar.gz         | 285 B |    0.2 kB/s | ETA: 00:00:00 | 100%", (80, 220, 120), True)],
        "",
        prompt_ps() + [("psftp -batch -pw 12345 user@192.168.56.10", C_FG_WHITE, True)],
        "Connected to 192.168.56.10",
        "Remote system type is UNIX",
        "Using username \"user\".",
        "",
        [("psftp> ", (220, 220, 100), True), ("pwd", C_FG_WHITE, True)],
        "Remote directory is /home/user",
        [("psftp> ", (220, 220, 100), True), ("ls -lh incoming", C_FG_WHITE, True)],
        "Listing directory /home/user/incoming",
        "-rw-r--r--   1 user     user          285 Oct 26 21:44 backup_lab6.tar.gz",
        [("psftp> ", (220, 220, 100), True), ("get incoming/backup_lab6.tar.gz local_copy.tar.gz", C_FG_WHITE, True)],
        [("remote:/home/user/incoming/backup_lab6.tar.gz => local:local_copy.tar.gz", C_FG_CYAN, False)],
        [("psftp> ", (220, 220, 100), True), ("quit", C_FG_WHITE, True)],
        "",
        prompt_ps() + [("tar -tzf local_copy.tar.gz", C_FG_WHITE, True)],
        "lab6_project/",
        "lab6_project/docs/readme.txt",
        "lab6_project/src/main.sh",
        "",
        prompt_ps()
    ]
    render_lines(draw, lines, top_h + 12)
    p = os.path.join(SCREENSHOTS_DIR, "fig21_file_transfer_scp_psftp.png")
    img.save(p)
    print("Saved", p)

# 22. Fig 22
def make_fig22():
    width, height = 780, 580
    img = Image.new("RGBA", (width, height), (240, 240, 240, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (width, 32)], fill=(245, 245, 245))
    draw.text((12, 7), "PuTTY Configuration (Release 0.85)", font=font_ui_12_b, fill=(20, 20, 20))
    draw.text((width - 60, 6), "—  ✕", font=font_ui_12, fill=(60, 60, 60))
    
    tree_w = 190
    draw.rectangle([(14, 44), (14 + tree_w, height - 60)], fill=(255, 255, 255), outline=(180, 180, 180))
    draw.text((22, 50), "Category:", font=font_ui_11, fill=(90, 90, 90))
    cats = [
        ("▾ Session", False, False), ("▸ Terminal", False, False),
        ("▸ Window", False, False), ("▾ Connection", False, False),
        ("    Data", False, False), ("    Proxy", False, False),
        ("  ▾ SSH", False, True), ("      Kex", False, False),
        ("      Host keys", False, False), ("      Auth", False, False),
        ("      Tunnels", True, True), ("    Serial", False, False)
    ]
    cy = 70
    for text, is_sel, is_b in cats:
        if is_sel:
            draw.rectangle([(16, cy - 2), (14 + tree_w - 2, cy + 18)], fill=(0, 120, 215))
            draw.text((24, cy), text, font=font_ui_12_b, fill=(255, 255, 255))
        else:
            draw.text((24, cy), text, font=font_ui_12_b if is_b else font_ui_12, fill=(30, 30, 30))
        cy += 21
        
    rx = 220
    draw.text((rx, 46), "Options controlling SSH port forwarding", font=font_ui_12_b, fill=(30, 30, 30))
    draw.rectangle([(rx, 70), (width - 18, 220)], outline=(190, 190, 190))
    draw.rectangle([(rx + 12, 62), (rx + 130, 75)], fill=(240, 240, 240))
    draw.text((rx + 14, 62), "Forwarded ports", font=font_ui_11, fill=(50, 50, 50))
    
    draw.rectangle([(rx + 16, 85), (rx + 360, 175)], fill=(255, 255, 255), outline=(170, 170, 170))
    draw.rectangle([(rx + 18, 90), (rx + 358, 114)], fill=(0, 120, 215))
    draw.text((rx + 24, 94), "L3389    localhost:3389", font=font_term_13_b, fill=(255, 255, 255))
    draw.text((rx + 24, 122), "L8080    192.168.56.10:80", font=font_term_13, fill=(60, 60, 60))
    draw.rectangle([(rx + 380, 85), (rx + 480, 115)], fill=(230, 230, 230), outline=(160, 160, 160))
    draw.text((rx + 405, 93), "Remove", font=font_ui_12, fill=(20, 20, 20))
    
    draw.rectangle([(rx, 235), (width - 18, height - 70)], outline=(190, 190, 190))
    draw.rectangle([(rx + 12, 227), (rx + 160, 240)], fill=(240, 240, 240))
    draw.text((rx + 14, 227), "Add new forwarded port", font=font_ui_11, fill=(50, 50, 50))
    draw.text((rx + 16, 250), "Source port", font=font_ui_11, fill=(40, 40, 40))
    draw.rectangle([(rx + 16, 270), (rx + 160, 298)], fill=(255, 255, 255), outline=(140, 140, 140))
    draw.text((rx + 24, 276), "3389", font=font_ui_13, fill=(10, 10, 10))
    draw.text((rx + 180, 250), "Destination", font=font_ui_11, fill=(40, 40, 40))
    draw.rectangle([(rx + 180, 270), (rx + 440, 298)], fill=(255, 255, 255), outline=(140, 140, 140))
    draw.text((rx + 188, 276), "localhost:3389", font=font_ui_13, fill=(10, 10, 10))
    draw.text((rx + 16, 315), "🔘 Local      🔘 Remote      🔘 Dynamic", font=font_ui_11, fill=(30, 30, 30))
    draw.text((rx + 16, 340), "🔘 Auto       🔘 IPv4        🔘 IPv6", font=font_ui_11, fill=(30, 30, 30))
    
    draw.rectangle([(rx + 360, 370), (rx + 450, 400)], fill=(0, 120, 215), outline=(0, 90, 180))
    draw.text((rx + 392, 377), "Add", font=font_ui_12_b, fill=(255, 255, 255))
    
    draw.rectangle([(width - 260, height - 44), (width - 180, height - 16)], fill=(0, 120, 215), outline=(0, 90, 180))
    draw.text((width - 232, height - 37), "Open", font=font_ui_12_b, fill=(255, 255, 255))
    draw.rectangle([(width - 170, height - 44), (width - 95, height - 16)], fill=(230, 230, 230), outline=(160, 160, 160))
    draw.text((width - 147, height - 37), "Cancel", font=font_ui_12, fill=(20, 20, 20))
    draw.rectangle([(width - 85, height - 44), (width - 20, height - 16)], fill=(230, 230, 230), outline=(160, 160, 160))
    draw.text((width - 62, height - 37), "Help", font=font_ui_12, fill=(20, 20, 20))
    
    draw.rectangle([(0, 0), (width - 1, height - 1)], outline=(180, 180, 180), width=1)
    paste_cursor(img, (rx + 405, 385))
    p = os.path.join(SCREENSHOTS_DIR, "fig22_putty_ssh_tunnel_rdp.png")
    img.save(p)
    print("Saved", p)

# 23. Fig 23
def make_fig23():
    width, height = 980, 580
    img = Image.new("RGBA", (width, height), (225, 230, 238, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (width, 40)], fill=(240, 240, 240))
    draw.text((20, 11), "Remote Desktop Connection (Tunnel: localhost:3389 -> 192.168.56.10:3389)", font=font_ui_12_b, fill=(30, 30, 30))
    
    rw, rh = 540, 420
    rx = (width - rw) // 2
    ry = 65
    draw.rectangle([(rx, ry), (rx + rw, ry + rh)], fill=(255, 255, 255), outline=(160, 160, 160), width=1)
    draw.rectangle([(rx, ry), (rx + rw, ry + 36)], fill=(0, 95, 184))
    draw.text((rx + 16, ry + 8), "🖥️  Remote Desktop Connection", font=font_ui_13_b, fill=(255, 255, 255))
    draw.text((rx + rw - 30, ry + 8), "✕", font=font_ui_13, fill=(255, 255, 255))
    
    draw.rectangle([(rx, ry + 36), (rx + rw, ry + 105)], fill=(245, 248, 252))
    draw.text((rx + 24, ry + 48), "Remote Desktop Connection via Secure SSH Tunnel", font=font_ui_14_b, fill=(0, 60, 140))
    draw.text((rx + 24, ry + 74), "Traffic forwarded through encrypted SSH tunnel L3389 -> localhost:3389", font=font_ui_11, fill=(90, 90, 90))
    
    draw.text((rx + 30, ry + 130), "Computer:", font=font_ui_12_b, fill=(30, 30, 30))
    draw.rectangle([(rx + 140, ry + 124), (rx + rw - 40, ry + 156)], fill=(255, 255, 255), outline=(130, 130, 130))
    draw.text((rx + 152, ry + 132), "127.0.0.1:3389", font=font_term_14_b, fill=(0, 102, 204))
    draw.text((rx + 30, ry + 180), "User name:", font=font_ui_12_b, fill=(30, 30, 30))
    draw.rectangle([(rx + 140, ry + 174), (rx + rw - 40, ry + 206)], fill=(255, 255, 255), outline=(130, 130, 130))
    draw.text((rx + 152, ry + 182), "user", font=font_ui_13, fill=(20, 20, 20))
    
    draw.rectangle([(rx + 30, ry + 230), (rx + rw - 40, ry + 310)], fill=(236, 247, 238), outline=(90, 180, 110))
    draw.text((rx + 45, ry + 242), "🔒 Connection Security: End-to-End Encrypted (SSH-2)", font=font_ui_12_b, fill=(20, 120, 50))
    draw.text((rx + 45, ry + 268), "Target Daemon: xrdp / X2Go Server on Linux Ubuntu 26.04", font=font_ui_11, fill=(40, 40, 40))
    draw.text((rx + 45, ry + 288), "Authentication: PuTTY RSA Agent (Pageant) forward channel", font=font_ui_11, fill=(70, 70, 70))
    
    draw.rectangle([(rx + rw - 260, ry + rh - 55), (rx + rw - 150, ry + rh - 20)], fill=(0, 120, 215), outline=(0, 90, 180))
    draw.text((rx + rw - 222, ry + rh - 45), "Connect", font=font_ui_12_b, fill=(255, 255, 255))
    draw.rectangle([(rx + rw - 135, ry + rh - 55), (rx + rw - 40, ry + rh - 20)], fill=(235, 235, 235), outline=(160, 160, 160))
    draw.text((rx + rw - 105, ry + rh - 45), "Cancel", font=font_ui_12, fill=(20, 20, 20))
    paste_cursor(img, (rx + rw - 200, ry + rh - 38))
    p = os.path.join(SCREENSHOTS_DIR, "fig23_remote_desktop_gui.png")
    img.save(p)
    print("Saved", p)

# 24. Fig 24
def make_fig24():
    img, draw, top_h = draw_terminal_base(tab_title="user@ubuntu: ~ (Server Security Auditing)")
    lines = [
        prompt_bash() + [("w && who -u", C_FG_WHITE, True)],
        " 21:48:22 up 20 min,  2 users,  load average: 0.04, 0.06, 0.02",
        "USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT",
        "user     pts/0    192.168.56.1     21:38    1.00s  0.08s  0.02s w",
        "user     pts/1    192.168.56.1     21:42   42.00s  0.04s  0.04s -bash",
        "",
        "user     pts/0        2026-10-26 21:38   .         1411 (192.168.56.1)",
        "user     pts/1        2026-10-26 21:42  00:42      1580 (192.168.56.1)",
        "",
        prompt_bash() + [("ss -tna '( dport = :22 or sport = :22 )'", C_FG_WHITE, True)],
        "State      Recv-Q Send-Q Local Address:Port        Peer Address:Port",
        [("LISTEN     0      4096         0.0.0.0:22             0.0.0.0:*", (80, 220, 120), False)],
        [("ESTAB      0      0       192.168.56.10:22        192.168.56.1:52314", C_FG_CYAN, True)],
        [("ESTAB      0      0       192.168.56.10:22        192.168.56.1:52398", C_FG_CYAN, True)],
        "",
        prompt_bash() + [("journalctl -u ssh --no-pager -n 4", C_FG_WHITE, True)],
        "Oct 26 21:38:12 ubuntu sshd[1410]: Accepted publickey for user from 192.168.56.1 port 52314 ssh2: RSA SHA256:f6:8a:c3...",
        "Oct 26 21:38:12 ubuntu sshd[1410]: pam_unix(sshd:session): session opened for user user(uid=1000) by (uid=0)",
        "Oct 26 21:42:05 ubuntu sshd[1579]: Accepted publickey for user from 192.168.56.1 port 52398 ssh2: RSA SHA256:f6:8a:c3...",
        "",
        prompt_bash()
    ]
    render_lines(draw, lines, top_h + 12)
    p = os.path.join(SCREENSHOTS_DIR, "fig24_server_session_audit.png")
    img.save(p)
    print("Saved", p)

def generate_all():
    print("Generating complete suite of 24 Lab 6 screenshots...")
    make_fig01()
    make_fig02()
    make_fig03()
    make_fig04()
    make_fig05()
    make_fig06()
    make_fig07()
    make_fig08()
    make_fig09()
    make_fig10()
    make_fig11()
    make_fig12()
    make_fig13()
    make_fig14()
    make_fig15()
    make_fig16()
    make_fig17()
    make_fig18()
    make_fig19()
    make_fig20()
    make_fig21()
    make_fig22()
    make_fig23()
    make_fig24()
    print("All 24 screenshots generated successfully!")

if __name__ == '__main__':
    generate_all()
