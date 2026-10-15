# -*- coding: utf-8 -*-
import sys

with open("lab4/08_scratch/render_new_clean_figures.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add MAP_LVIV_URL
old_urls = 'AV3_URL = p2u("ai_avatar_sergiy.jpg")'
new_urls = '''AV3_URL = p2u("ai_avatar_sergiy.jpg")
MAP_LVIV_URL = p2u("map_lviv.jpg")'''
assert old_urls in content, "old_urls not found"
content = content.replace(old_urls, new_urls, 1)

# 2. Update map-canvas-desktop in fig13
old_map_css = '''.map-canvas-desktop {{ height: 380px; position: relative; background: radial-gradient(#CBD5E1 1.5px, #F1F5F9 1.5px); background-size: 18px 18px; }}
  .map-artery {{ position: absolute; background: #CBD5E1; }}'''
new_map_css = '''.map-canvas-desktop {{ height: 380px; position: relative; background: url('{MAP_LVIV_URL}') center/cover no-repeat; }}
  .map-artery {{ display: none; }}'''
assert old_map_css in content, "old_map_css not found"
content = content.replace(old_map_css, new_map_css, 1)

# 3. Update pins in fig13
old_pins = '''        <!-- Pins -->
        <div class="d-pin" style="top: 90px; left: 680px;">
          <div class="d-dot blue"></div>
          <div class="d-tag">Хаб «Київ-Поділ» · 120 кВт (3/4 вільно) 🔋</div>
        </div>

        <div class="d-pin" style="top: 130px; left: 240px;">
          <div class="d-dot"></div>
          <div class="d-tag">Хаб «Львів-Арена» · 160 кВт (5/6 вільно) 🔋</div>
        </div>

        <div class="d-pin" style="top: 250px; left: 740px;">
          <div class="d-dot warn"></div>
          <div class="d-tag">Хаб «Одеса-Порт» · 100 кВт (1/2 вільно) 🔋</div>
        </div>

        <div class="d-pin" style="top: 190px; left: 1040px;">
          <div class="d-dot blue"></div>
          <div class="d-tag">Хаб «Дніпро-Сіті» · 120 кВт (2/2 вільно) 🔋</div>
        </div>'''

new_pins = '''        <!-- Pins on Lviv Map -->
        <div class="d-pin" style="top: 120px; left: 480px;">
          <div class="d-dot"></div>
          <div class="d-tag">Хаб «Львів-Центр» · 120 кВт (3/4 вільно) 🔋</div>
        </div>

        <div class="d-pin" style="top: 250px; left: 320px;">
          <div class="d-dot"></div>
          <div class="d-tag">Хаб «Львів-Арена» · 160 кВт (5/6 вільно) 🔋</div>
        </div>

        <div class="d-pin" style="top: 140px; left: 880px;">
          <div class="d-dot blue"></div>
          <div class="d-tag">Хаб «Львів-Стрийська» · 120 кВт (2/2 вільно) 🔋</div>
        </div>

        <div class="d-pin" style="top: 260px; left: 820px;">
          <div class="d-dot warn"></div>
          <div class="d-tag">Хаб «Львів-Південний» · 100 кВт (1/2 вільно) 🔋</div>
        </div>'''

assert old_pins in content, "old_pins not found"
content = content.replace(old_pins, new_pins, 1)

# 4. Update map-canvas in tablet
old_tmap_css = '.map-canvas {{ width: 100%; height: 100%; background: radial-gradient(#CBD5E1 1.5px, #F1F5F9 1.5px); background-size: 12px 12px; position: relative; }}'
new_tmap_css = ".map-canvas {{ width: 100%; height: 100%; background: url('{MAP_LVIV_URL}') center/cover no-repeat; position: relative; }}"
assert old_tmap_css in content, "old_tmap_css not found"
content = content.replace(old_tmap_css, new_tmap_css)

# 5. Update Tablet Slicing (2 columns instead of 3)
old_tslice = '''# Render Tablet Full & Slice into 3 columns (Fig 15)
temp_tablet = os.path.join(HTML_DIR, "temp_tablet_full.png")
render_chrome(f15_path, temp_tablet, 768, 3300, scale=1.5)

im_t = Image.open(temp_tablet)
tw, th = im_t.size
slice_h_t = th // 3

# Combine 3 slices side-by-side with 12px gap
gap = 12
out_w_t = tw * 3 + gap * 2
board_t = Image.new("RGB", (out_w_t, slice_h_t), (241, 245, 249))

for i in range(3):
    box = (0, i * slice_h_t, tw, (i + 1) * slice_h_t)
    slice_img = im_t.crop(box)
    x = i * (tw + gap)
    board_t.paste(slice_img, (x, 0))'''

new_tslice = '''# Render Tablet Full & Slice into 2 columns (Fig 15 - balanced height)
temp_tablet = os.path.join(HTML_DIR, "temp_tablet_full.png")
render_chrome(f15_path, temp_tablet, 768, 3300, scale=1.5)

im_t = Image.open(temp_tablet)
tw, th = im_t.size
slice_h_t = th // 2

# Combine 2 slices side-by-side with 16px gap
gap = 16
out_w_t = tw * 2 + gap
board_t = Image.new("RGB", (out_w_t, slice_h_t), (241, 245, 249))

for i in range(2):
    box = (0, i * slice_h_t, tw, (i + 1) * slice_h_t)
    slice_img = im_t.crop(box)
    x = i * (tw + gap)
    board_t.paste(slice_img, (x, 0))'''

assert old_tslice in content, "old_tslice not found"
content = content.replace(old_tslice, new_tslice, 1)

# 6. Update Mobile Slicing (3 columns instead of 4)
old_mslice = '''# Render Mobile Full & Slice into 4 columns (Fig 16)
temp_mobile = os.path.join(HTML_DIR, "temp_mobile_full.png")
render_chrome(f16_path, temp_mobile, 390, 3600, scale=1.5)

im_m = Image.open(temp_mobile)
mw, mh = im_m.size
slice_h_m = mh // 4

out_w_m = mw * 4 + gap * 3
board_m = Image.new("RGB", (out_w_m, slice_h_m), (241, 245, 249))

for i in range(4):
    box = (0, i * slice_h_m, mw, (i + 1) * slice_h_m)
    slice_img = im_m.crop(box)
    x = i * (mw + gap)
    board_m.paste(slice_img, (x, 0))'''

new_mslice = '''# Render Mobile Full & Slice into 3 columns (Fig 16 - balanced height)
temp_mobile = os.path.join(HTML_DIR, "temp_mobile_full.png")
render_chrome(f16_path, temp_mobile, 390, 3600, scale=1.5)

im_m = Image.open(temp_mobile)
mw, mh = im_m.size
slice_h_m = mh // 3

out_w_m = mw * 3 + gap * 2
board_m = Image.new("RGB", (out_w_m, slice_h_m), (241, 245, 249))

for i in range(3):
    box = (0, i * slice_h_m, mw, (i + 1) * slice_h_m)
    slice_img = im_m.crop(box)
    x = i * (mw + gap)
    board_m.paste(slice_img, (x, 0))'''

assert old_mslice in content, "old_mslice not found"
content = content.replace(old_mslice, new_mslice, 1)

with open("lab4/08_scratch/render_new_clean_figures.py", "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Patch applied to render_new_clean_figures.py!")
