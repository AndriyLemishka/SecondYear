import os, subprocess
from PIL import Image

BASE_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4"
MAT_DIR = os.path.join(BASE_DIR, "materials")
SCR_DIR = os.path.join(BASE_DIR, "screenshots")
HTML_DIR = os.path.join(BASE_DIR, "08_scratch", "html_boards")
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def render_chrome(html_path, out_png, width, height, scale=1.5):
    cmd = [
        CHROME_PATH,
        "--headless=new",
        f"--window-size={width},{height}",
        "--hide-scrollbars",
        f"--force-device-scale-factor={scale}",
        f"--screenshot={out_png}",
        f"file:///{html_path.replace(os.sep, '/')}"
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# 1. TABLET 768
# Let's test height 4300 for tablet_full.html
p_tab_html = os.path.join(HTML_DIR, "tablet_full.html")
p_tab_tall = os.path.join(HTML_DIR, "tablet_tall_4300.png")
render_chrome(p_tab_html, p_tab_tall, 768, 4300, scale=1.5)

im_tab = Image.open(p_tab_tall)
tw, th = im_tab.size
print("Tablet tall 4300 size:", tw, th)

# Find where content actually ends (where footer ends, non-white pixels from bottom)
# Crop and slice into 3 equal columns
sh = th // 3
s1 = im_tab.crop((0, 0, tw, sh))
s2 = im_tab.crop((0, sh, tw, 2 * sh))
s3 = im_tab.crop((0, 2 * sh, tw, th))
if s3.size[1] != sh:
    s3 = s3.resize((tw, sh))

gap = 20
comp_w = tw * 3 + gap * 2
comp_tab = Image.new("RGB", (comp_w, sh), (255, 255, 255))
comp_tab.paste(s1, (0, 0))
comp_tab.paste(s2, (tw + gap, 0))
comp_tab.paste(s3, (2 * (tw + gap), 0))
comp_tab.save(os.path.join(SCR_DIR, "fig15_tablet.png"))
print("Saved tuned fig15_tablet.png")
