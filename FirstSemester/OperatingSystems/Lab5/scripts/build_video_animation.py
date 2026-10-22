import os
import sys
import json
import subprocess
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont, ImageFilter

LAB_DIR = r"d:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5"
REPORTS_DIR = os.path.join(LAB_DIR, "reports")
SCREENSHOTS_DIR = os.path.join(LAB_DIR, "screenshots")
SCRIPTS_DIR = os.path.join(LAB_DIR, "scripts")

JSON_PATH = os.path.join(SCRIPTS_DIR, "steps_data.json")
OUT_MP4 = os.path.join(REPORTS_DIR, "Відео_інструкція_Лаб5.mp4")
ROOT_MP4 = os.path.join(LAB_DIR, "Відео_інструкція_Лаб5.mp4")

WIDTH = 1280
HEIGHT = 720
FPS = 24
STEP_FRAMES = 30 # 1.25s per step
INTRO_FRAMES = 72 # 3.0s
OUTRO_FRAMES = 72 # 3.0s

# Fonts
def get_font(size, bold=False):
    try:
        font_name = "segoeuib.ttf" if bold else "segoeui.ttf"
        return ImageFont.truetype(font_name, size)
    except Exception:
        try:
            font_name = "arialbd.ttf" if bold else "arial.ttf"
            return ImageFont.truetype(font_name, size)
        except Exception:
            return ImageFont.load_default()

font_title_lg = get_font(24, bold=True)
font_title_md = get_font(18, bold=True)
font_title_sm = get_font(15, bold=True)
font_body = get_font(12, bold=False)
font_body_bold = get_font(12, bold=True)
font_small = get_font(10, bold=False)
font_small_bold = get_font(10, bold=True)

def wrap_text(text, font, max_width):
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split(" ")
        curr = ""
        for w in words:
            test = curr + (" " if curr else "") + w
            bbox = font.getbbox(test)
            w_px = bbox[2] - bbox[0]
            if w_px <= max_width:
                curr = test
            else:
                if curr:
                    lines.append(curr)
                curr = w
        if curr:
            lines.append(curr)
    return lines

def create_base_background():
    im = Image.new("RGB", (WIDTH, HEIGHT), (15, 23, 42))
    draw = ImageDraw.Draw(im)
    # subtle gradient simulation
    for y in range(HEIGHT):
        r = int(11 + (y / HEIGHT) * 14)
        g = int(17 + (y / HEIGHT) * 20)
        b = int(32 + (y / HEIGHT) * 25)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))
    return im

def render_intro_frame(alpha=1.0):
    base = create_base_background()
    draw = ImageDraw.Draw(base)
    
    # Coat of arms
    coat_path = os.path.join(SCREENSHOTS_DIR, "lp_coat_of_arms.jpg")
    if os.path.exists(coat_path):
        coat = Image.open(coat_path).convert("RGBA")
        coat.thumbnail((140, 140), Image.Resampling.LANCZOS)
        cx = (WIDTH - coat.width) // 2
        base.paste(coat, (cx, 50), coat)
        
    # University & Department
    t1 = "НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ «ЛЬВІВСЬКА ПОЛІТЕХНІКА»"
    b1 = font_title_md.getbbox(t1)
    draw.text(((WIDTH - (b1[2]-b1[0]))//2, 210), t1, fill=(241, 245, 249), font=font_title_md)
    
    t2 = "Кафедра «Систем автоматизованого проектування» (САПР)"
    b2 = font_body_bold.getbbox(t2)
    draw.text(((WIDTH - (b2[2]-b2[0]))//2, 245), t2, fill=(148, 163, 184), font=font_body_bold)
    
    # Card Center
    draw.rounded_rectangle([200, 290, 1080, 480], radius=16, fill=(30, 41, 59), outline=(56, 189, 248), width=2)
    
    t3 = "ЛАБОРАТОРНА РОБОТА №5"
    b3 = font_title_lg.getbbox(t3)
    draw.text(((WIDTH - (b3[2]-b3[0]))//2, 315), t3, fill=(56, 189, 248), font=font_title_lg)
    
    t4 = "«Встановлення та конфігурація служби каталогів Active Directory,"
    b4 = font_title_sm.getbbox(t4)
    draw.text(((WIDTH - (b4[2]-b4[0]))//2, 365), t4, fill=(248, 250, 252), font=font_title_sm)
    
    t4_2 = "служб мережевої інфраструктури (DNS, DHCP, GPO) та клієнта Windows 10»"
    b4_2 = font_title_sm.getbbox(t4_2)
    draw.text(((WIDTH - (b4_2[2]-b4_2[0]))//2, 395), t4_2, fill=(248, 250, 252), font=font_title_sm)
    
    t5 = "ПОВНА ПОКРОКОВА ВІДЕО-ДЕМОНСТРАЦІЯ НАТИСКАНЬ (83 КРОКИ)"
    b5 = font_body_bold.getbbox(t5)
    draw.text(((WIDTH - (b5[2]-b5[0]))//2, 440), t5, fill=(52, 211, 153), font=font_body_bold)
    
    # Submitter & Teacher
    sub1 = "Виконав: студент групи ПП-14 Андрій ЛЕМІШКА"
    draw.text((250, 520), sub1, fill=(241, 245, 249), font=font_body_bold)
    
    sub2 = "Перевірила: викладач кафедри САПР Наталія НЕСТОР"
    draw.text((250, 550), sub2, fill=(148, 163, 184), font=font_body)
    
    city = "Львів – 2026"
    b_city = font_body.getbbox(city)
    draw.text(((WIDTH - (b_city[2]-b_city[0]))//2, 640), city, fill=(148, 163, 184), font=font_body)
    
    if alpha < 1.0:
        black = Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 0))
        base = Image.blend(black, base, alpha)
        
    return base

def render_outro_frame(alpha=1.0):
    base = create_base_background()
    draw = ImageDraw.Draw(base)
    
    t_top = "УСІ 83 КРОКИ ЛАБОРАТОРНОЇ РОБОТИ УСПІШНО ВИКОНАНО!"
    b_top = font_title_lg.getbbox(t_top)
    draw.text(((WIDTH - (b_top[2]-b_top[0]))//2, 60), t_top, fill=(16, 185, 129), font=font_title_lg)
    
    # Summary Box
    draw.rounded_rectangle([160, 120, 1120, 570], radius=16, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
    
    items = [
        "✓   Контролер домену Active Directory Domain Services (AD DS) та ліс office.com розгорнуто",
        "✓   Службу DNS успішно інтегровано та налаштовано для обслуговування зони домену",
        "✓   Ієрархію OUs (Керівники, Фінансисти, IT, Групи), користувачів та групи безпеки створено",
        "✓   Службу DHCP авторизовано: створено область «Офіс», виключення та параметри 003, 006, 015",
        "✓   Створено статичне резервування IP-адреси шлюзу 192.168.1.4 за MAC-адресою",
        "✓   Об'єкт групової політики (GPO) «Фінансова політика безпеки» з блокуванням 600 с застосовано",
        "✓   Спільні мережеві ресурси SMB (C:\\Офіс, C:\\Profiles) та диск P: для програміста підключено",
        "✓   Клієнтську станцію Windows 10 успішно приєднано до домену office.com та перевірено"
    ]
    
    for idx, itm in enumerate(items):
        y_pos = 160 + idx * 48
        draw.text((200, y_pos), itm, fill=(241, 245, 249), font=font_body_bold)
        
    t_end = "Дякую за увагу!  |  Львів – 2026"
    b_end = font_title_md.getbbox(t_end)
    draw.text(((WIDTH - (b_end[2]-b_end[0]))//2, 620), t_end, fill=(56, 189, 248), font=font_title_md)
    
    if alpha < 1.0:
        black = Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 0))
        base = Image.blend(black, base, alpha)
        
    return base

def render_step_static(step_num, step_data, total_steps=83):
    title, text, img_name, cap = step_data
    
    base = create_base_background()
    draw = ImageDraw.Draw(base)
    
    # 1. Load screenshot
    img_path = os.path.join(SCREENSHOTS_DIR, img_name)
    if not os.path.exists(img_path):
        img_path = os.path.join(LAB_DIR, img_name)
        
    if os.path.exists(img_path):
        shot = Image.open(img_path).convert("RGB")
        # Resize to fit 854 x 640
        shot_resized = shot.resize((854, 640), Image.Resampling.LANCZOS)
        
        # Paste shot at (32, 36)
        base.paste(shot_resized, (32, 36))
        # Frame border around screenshot
        draw.rectangle([31, 35, 32 + 854, 36 + 640], outline=(51, 65, 85), width=2)
    else:
        draw.rectangle([32, 36, 32 + 854, 36 + 640], fill=(20, 20, 20), outline=(200, 50, 50))
        draw.text((200, 300), f"Image not found: {img_name}", fill=(255, 100, 100), font=font_title_sm)

    # 2. Right HUD Card (x=906, y=36, w=342, h=640)
    cx, cy, cw, ch = 906, 36, 342, 640
    draw.rounded_rectangle([cx, cy, cx+cw, cy+ch], radius=12, fill=(17, 24, 39), outline=(30, 41, 59), width=2)
    
    # Step badge (pill)
    draw.rounded_rectangle([cx+16, cy+16, cx+150, cy+46], radius=15, fill=(37, 99, 235))
    badge_text = f"КРОК {step_num} / {total_steps}"
    draw.text((cx+26, cy+22), badge_text, fill=(255, 255, 255), font=font_small_bold)
    
    # Status indicator
    draw.ellipse([cx+cw-40, cy+25, cx+cw-30, cy+35], fill=(16, 185, 129))
    draw.text((cx+cw-115, cy+23), "ВИКОНАНО", fill=(16, 185, 129), font=font_small_bold)
    
    # Step Title
    clean_title = title.split(".", 1)[-1].strip() if "." in title else title
    wrapped_title = wrap_text(clean_title, font_title_sm, max_width=cw - 32)
    curr_y = cy + 58
    for l in wrapped_title[:3]:
        draw.text((cx+16, curr_y), l, fill=(248, 250, 252), font=font_title_sm)
        curr_y += 20
        
    # Divider
    curr_y += 6
    draw.line([(cx+16, curr_y), (cx+cw-16, curr_y)], fill=(51, 65, 85), width=1)
    curr_y += 12
    
    # Action instructions header
    draw.text((cx+16, curr_y), "ПОСЛІДОВНІСТЬ НАТИСКАНЬ:", fill=(56, 189, 248), font=font_small_bold)
    curr_y += 20
    
    # Action instructions text lines
    action_lines = wrap_text(text, font_body, max_width=cw - 32)
    for l in action_lines[:15]:
        draw.text((cx+16, curr_y), l, fill=(203, 213, 225), font=font_body)
        curr_y += 17
        if curr_y > cy + ch - 40:
            break
            
    # Bottom card footer
    draw.line([(cx+16, cy+ch-36), (cx+cw-16, cy+ch-36)], fill=(51, 65, 85), width=1)
    draw.text((cx+16, cy+ch-26), "Лабораторна робота №5  •  ПП-14", fill=(100, 116, 139), font=font_small)

    return base

def draw_progress_bar(im, current_frame, total_frames, step_num, total_steps=83):
    draw = ImageDraw.Draw(im)
    bx, by, bw, bh = 32, 694, 1216, 8
    draw.rounded_rectangle([bx, by, bx+bw, by+bh], radius=4, fill=(30, 41, 59))
    
    progress = max(0.0, min(1.0, current_frame / total_frames))
    fill_w = int(bw * progress)
    if fill_w > 4:
        draw.rounded_rectangle([bx, by, bx+fill_w, by+bh], radius=4, fill=(56, 189, 248))
        
    # Timecode
    sec_cur = current_frame // FPS
    sec_tot = total_frames // FPS
    tc_cur = f"{sec_cur//60:02d}:{sec_cur%60:02d}"
    tc_tot = f"{sec_tot//60:02d}:{sec_tot%60:02d}"
    info = f"Крок {step_num} з {total_steps}  |  {tc_cur} / {tc_tot}"
    draw.text((WIDTH - 200, 706), info, fill=(148, 163, 184), font=font_small)

def main():
    print("Loading steps data...")
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        steps = json.load(f)
        
    total_steps = len(steps)
    print(f"Total steps to render: {total_steps}")
    
    total_frames = INTRO_FRAMES + (total_steps * STEP_FRAMES) + OUTRO_FRAMES
    print(f"Total video frames: {total_frames} ({total_frames/FPS:.1f} seconds at {FPS} FPS)")
    
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    print(f"Using FFmpeg: {ffmpeg_exe}")
    
    # Start ffmpeg process piping raw RGB frames
    cmd = [
        ffmpeg_exe,
        "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-preset", "fast",
        "-crf", "20",
        OUT_MP4
    ]
    
    print("Launching FFmpeg encoder...")
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    
    frame_count = 0
    
    # 1. Render Intro
    print("Rendering Intro...")
    intro_base = render_intro_frame(1.0)
    for f in range(INTRO_FRAMES):
        if f < 12:
            alpha = f / 12.0
            im = render_intro_frame(alpha)
        elif f > INTRO_FRAMES - 12:
            alpha = (INTRO_FRAMES - f) / 12.0
            im = render_intro_frame(alpha)
        else:
            im = intro_base.copy()
            
        draw_progress_bar(im, frame_count, total_frames, 0, total_steps)
        proc.stdin.write(im.tobytes())
        frame_count += 1
        
    # 2. Render all 83 Steps
    print("Rendering all 83 steps...")
    for idx, s in enumerate(steps, 1):
        if idx % 10 == 0 or idx == total_steps:
            print(f"  Processing step {idx} / {total_steps} (frame {frame_count}/{total_frames})...")
            
        step_base = render_step_static(idx, s, total_steps)
        for sf in range(STEP_FRAMES):
            im = step_base.copy()
            draw_progress_bar(im, frame_count, total_frames, idx, total_steps)
            proc.stdin.write(im.tobytes())
            frame_count += 1
            
    # 3. Render Outro
    print("Rendering Outro...")
    outro_base = render_outro_frame(1.0)
    for f in range(OUTRO_FRAMES):
        if f < 12:
            alpha = f / 12.0
            im = render_outro_frame(alpha)
        elif f > OUTRO_FRAMES - 12:
            alpha = (OUTRO_FRAMES - f) / 12.0
            im = render_outro_frame(alpha)
        else:
            im = outro_base.copy()
            
        draw_progress_bar(im, frame_count, total_frames, total_steps, total_steps)
        proc.stdin.write(im.tobytes())
        frame_count += 1
        
    proc.stdin.close()
    proc.wait()
    
    print("FFmpeg encoding finished!")
    if os.path.exists(OUT_MP4):
        size_mb = os.path.getsize(OUT_MP4) / (1024 * 1024)
        print(f"SUCCESS! Video created at:\n{OUT_MP4} ({size_mb:.2f} MB)")
        shutil.copy2(OUT_MP4, ROOT_MP4)
        print(f"Copied to root directory:\n{ROOT_MP4}")
    else:
        print("ERROR: Output MP4 was not created!")
        print(proc.stderr.read().decode("utf-8", errors="ignore"))

if __name__ == "__main__":
    main()
