# -*- coding: utf-8 -*-
"""
Builder script that generates the complete, fully interactive Figma Plugin
for ChargeUA (Lab 4).
Includes:
  1. All 11 unique image assets (6 distinct station hubs, AI promo banner, video tutorial, generator, cable, avatars, hero)
  2. Prototype interactions (linkNodes, linkOverlay, linkClose) making all buttons clickable in Figma Simulation mode
  3. Flow starting points (Desktop, Mobile, Catalog)
  4. Automatic canvas cleanup of duplicated frames
  5. Clean coordinate placement without overlaps
"""

import os, io, base64
from PIL import Image

BASE_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4"
MAT_DIR = os.path.join(BASE_DIR, "materials")
OUT_PLUGIN = os.path.join(BASE_DIR, "05_figma_exports", "figma_builder_plugin.js")
OUT_CODE = os.path.join(BASE_DIR, "05_figma_exports", "charge", "code.js")
OUT_GENERATOR = os.path.join(BASE_DIR, "08_scratch", "generate_final_figma_plugin.py")

def read_svg(filename):
    p = os.path.join(MAT_DIR, filename)
    with open(p, "r", encoding="utf-8") as f:
        return f.read().replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

def get_b64_jpeg(filename, max_w, max_h, quality=75):
    p = os.path.join(MAT_DIR, filename)
    im = Image.open(p).convert("RGB")
    im.thumbnail((max_w, max_h))
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=quality, optimize=True)
    return base64.b64encode(buf.getvalue()).decode("ascii")

print("Processing SVG assets...")
svg_logo = read_svg("Logo.svg")
svg_calc = read_svg("Calculator.svg")
svg_loc = read_svg("Location.svg")
svg_info = read_svg("Information.svg")

print("Processing Image assets (including 6 distinct hubs & promo banner & video tutorial)...")
b64_hero = get_b64_jpeg("hero_bg.jpg", 640, 360, 75)
b64_hub_kyiv = get_b64_jpeg("ai_hub_kyiv.jpg", 420, 240, 75)
b64_hub_lviv = get_b64_jpeg("ai_hub_lviv.jpg", 420, 240, 75)
b64_hub_obolon = get_b64_jpeg("ai_hub_obolon.jpg", 420, 240, 75)
b64_hub_odesa = get_b64_jpeg("ai_hub_odesa.jpg", 420, 240, 75)
b64_hub_dnipro = get_b64_jpeg("ai_hub_dnipro.jpg", 420, 240, 75)
b64_hub_zhytomyr = get_b64_jpeg("ai_hub_zhytomyr.jpg", 420, 240, 75)

b64_banner_ai = get_b64_jpeg("ai_promo_banner.jpg", 420, 240, 75)
b64_video_tutorial = get_b64_jpeg("ai_video_tutorial.jpg", 420, 240, 75)

b64_generator = get_b64_jpeg("ai_generator_blackout.jpg", 420, 260, 75)
b64_cable = get_b64_jpeg("ai_step_cable.jpg", 360, 220, 75)
b64_video = get_b64_jpeg("video_frame_30.jpg", 960, 540, 85)
b64_banner = get_b64_jpeg("fig3_banner.png", 400, 200, 75)
b64_av1 = get_b64_jpeg("ai_avatar_oleksiy.jpg", 120, 120, 75)
b64_av2 = get_b64_jpeg("ai_avatar_olena.jpg", 120, 120, 75)
b64_av3 = get_b64_jpeg("ai_avatar_sergiy.jpg", 120, 120, 75)

print("Building interactive Figma JS code...")
# We will write the code to create the plugin
