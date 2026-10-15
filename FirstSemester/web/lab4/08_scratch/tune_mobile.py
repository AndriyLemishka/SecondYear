import os, subprocess
from PIL import Image

BASE_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4"
MAT_DIR = os.path.join(BASE_DIR, "materials")
SCR_DIR = os.path.join(BASE_DIR, "screenshots")
HTML_DIR = os.path.join(BASE_DIR, "08_scratch", "html_boards")
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def p2u(fname):
    return os.path.join(MAT_DIR, fname).replace(os.sep, "/")

LOGO_URL = p2u("Logo.svg")
CALC_URL = p2u("Calculator.svg")
LOC_URL = p2u("Location.svg")
INFO_URL = p2u("Information.svg")
HERO_URL = p2u("hero_bg.jpg")
BANNER_URL = p2u("fig3_banner.png")
VIDEO_URL = p2u("fig5_video.png")
HUB_KYIV_URL = p2u("ai_hub_kyiv.jpg")
HUB_LVIV_URL = p2u("ai_hub_lviv.jpg")
GEN_URL = p2u("ai_generator_blackout.jpg")
CABLE_URL = p2u("ai_step_cable.jpg")
AV1_URL = p2u("ai_avatar_oleksiy.jpg")
AV2_URL = p2u("ai_avatar_olena.jpg")
AV3_URL = p2u("ai_avatar_sergiy.jpg")

COMMON_HEAD = f"""
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }}
  body {{ width: 390px; background: #FFFFFF; color: #0F172A; -webkit-font-smoothing: antialiased; border: 1px solid #CBD5E1; }}
  .top-strip {{ background: #0F172A; color: #E2E8F0; padding: 6px 14px; display: flex; justify-content: space-between; font-size: 10px; font-weight: 500; }}
  .navbar {{ height: 52px; padding: 0 14px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #E2E8F0; background: #FFF; }}
  .sec {{ padding: 14px; }}
  .btn-pri {{ width: 100%; background: #005EC9; color: #FFF; border: none; padding: 10px; border-radius: 8px; font-size: 12px; font-weight: 700; cursor: pointer; text-align: center; }}
  .badge-g {{ background: #D1FAE5; color: #065F46; font-size: 9px; font-weight: 700; padding: 3px 6px; border-radius: 4px; display: inline-block; }}
  .card-box {{ background: #FFF; border: 1px solid #E2E8F0; border-radius: 10px; overflow: hidden; margin-bottom: 12px; }}
  .footer {{ background: #0F172A; color: #FFF; padding: 20px 14px 16px; font-size: 10px; }}
  .b-nav {{ height: 46px; background: #FFF; border-top: 1px solid #E2E8F0; display: flex; justify-content: space-around; align-items: center; font-size: 9px; font-weight: 700; color: #64748B; }}
</style>
"""

html_mob = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}</head><body>
  <div class="top-strip"><span>● 480+ станцій онлайн</span><span>0 800 300 400</span></div>
  <div class="navbar">
    <div style="display:flex; align-items:center; gap:8px;">
      <img src="{LOGO_URL}" style="width:24px; height:24px;">
      <span style="font-size:16px; font-weight:800; color:#005EC9;">ChargeUA</span>
    </div>
    <div style="font-size:18px;">☰</div>
  </div>

  <!-- SECTION 1: HERO & PERKS -->
  <div class="sec">
    <div style="font-size:10px; font-weight:800; color:#005EC9; margin-bottom:4px;">⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР</div>
    <h1 style="font-size:22px; font-weight:800; line-height:1.25; margin-bottom:8px;">Заряджайте авто без стресу</h1>
    <p style="font-size:12px; color:#64748B; line-height:1.5; margin-bottom:12px;">Усі зарядні станції України з онлайн-статусом світла та генераторів під час блекаутів.</p>
    <button class="btn-pri" style="margin-bottom:14px;">Розрахувати зарядку →</button>
    <img src="{HERO_URL}" style="width:100%; border-radius:10px; object-fit:cover; margin-bottom:12px;">
    <div style="font-size:11px; color:#475569; line-height:1.7;">
      <div>✓ Точний калькулятор витрат батареї</div>
      <div>✓ Live-карта 480+ станцій онлайн</div>
      <div>✓ 100% захист генераторами у блекаут</div>
    </div>
  </div>

  <!-- SECTION 2: CALCULATOR -->
  <div class="sec" style="background:#F8FAFC; border-top:1px solid #E2E8F0; border-bottom:1px solid #E2E8F0;">
    <div style="font-weight:800; font-size:15px; margin-bottom:8px;">Калькулятор вартості</div>
    <div style="font-size:11px; color:#64748B; margin-bottom:10px;">Volkswagen ID.4 (77 кВт·год) · 20% → 80%</div>
    <div style="height:6px; background:#E2E8F0; border-radius:3px; margin-bottom:8px;"><div style="width:75%; height:100%; background:#005EC9; border-radius:3px;"></div></div>
    <div style="font-size:20px; font-weight:800; color:#0F172A; margin:6px 0 2px;">652.50 ₴</div>
    <div style="font-size:10px; font-weight:700; color:#005EC9; margin-bottom:10px;">● Час на 120 кВт DC: ~28 хв</div>
    <button class="btn-pri" style="background:#0F172A;">Знайти найближчий хаб</button>
  </div>

  <!-- SECTION 3: HOW IT WORKS & CABLE -->
  <div class="sec">
    <div style="font-weight:800; font-size:15px; margin-bottom:8px;">Як зарядитися за 3 кроки:</div>
    <img src="{CABLE_URL}" style="width:100%; border-radius:8px; object-fit:cover; margin-bottom:10px;">
    <div style="font-size:11px; color:#475569; line-height:1.6;">
      <div>1. Знайдіть вільну станцію на карті</div>
      <div>2. Підключіть конектор CCS2</div>
      <div>3. Оплатіть в 1 клік Apple Pay</div>
    </div>
  </div>

  <!-- SECTION 4: BLACKOUT RESILIENCE -->
  <div class="sec" style="background:#0F172A; color:#FFF;">
    <div style="font-size:10px; font-weight:800; color:#00E5FF;">ЕНЕРГОНЕЗАЛЕЖНІСТЬ 24/7</div>
    <div style="font-size:17px; font-weight:800; margin:4px 0 8px;">Зарядка у повні блекаути</div>
    <p style="font-size:11px; color:#CBD5E1; line-height:1.5;">Промислові дизель-генератори 160 кВА на кожному ключовому вузлі мережі.</p>
    <img src="{GEN_URL}" style="width:100%; border-radius:8px; margin-top:10px; object-fit:cover;">
  </div>

  <!-- SECTION 5: POPULAR HUBS -->
  <div class="sec">
    <div style="font-weight:800; font-size:15px; margin-bottom:10px;">Популярні хаби мережі:</div>
    <div class="card-box">
      <img src="{HUB_KYIV_URL}" style="width:100%; height:130px; object-fit:cover;">
      <div style="padding:10px;">
        <div style="font-weight:800; font-size:13px;">Хаб «Київ-Поділ» · 120 кВт</div>
        <div style="font-size:10px; color:#64748B; margin:2px 0 6px;">вул. Сагайдачного, 12 · 14.50 ₴</div>
        <div class="badge-g" style="margin-bottom:8px;">🔋 Генератор ON · Вільний (3/4)</div>
        <button class="btn-pri">Прокласти маршрут (Waze / Maps)</button>
      </div>
    </div>
    <div class="card-box">
      <img src="{HUB_LVIV_URL}" style="width:100%; height:130px; object-fit:cover;">
      <div style="padding:10px;">
        <div style="font-weight:800; font-size:13px;">Хаб «Арена Львів» · 160 кВт</div>
        <div style="font-size:10px; color:#64748B; margin:2px 0 6px;">вул. Стрийська, 199 · 15.00 ₴</div>
        <div class="badge-g" style="margin-bottom:8px;">🔋 Сонячний навіс + Дизель</div>
        <button class="btn-pri">Прокласти маршрут (Waze / Maps)</button>
      </div>
    </div>
  </div>

  <!-- SECTION 6: VIDEO GUIDE -->
  <div class="sec" style="background:#F8FAFC; border-top:1px solid #E2E8F0; border-bottom:1px solid #E2E8F0;">
    <div style="font-weight:800; font-size:14px; margin-bottom:6px;">Відеоінструкція водія:</div>
    <img src="{VIDEO_URL}" style="width:100%; border-radius:8px; object-fit:cover; margin-bottom:8px;">
    <p style="font-size:11px; color:#64748B;">45-секундний гайд швидкого підключення та оплати.</p>
  </div>

  <!-- SECTION 7: REVIEWS -->
  <div class="sec">
    <div style="font-weight:800; font-size:14px; margin-bottom:8px;">Відгуки реальних водіїв:</div>
    <div style="border:1px solid #E2E8F0; border-radius:8px; padding:10px; margin-bottom:8px; background:#FFF;">
      <div style="color:#F59E0B; font-size:11px; margin-bottom:4px;">★★★★★</div>
      <div style="font-size:11px; color:#334155; margin-bottom:6px;">«Під час блекауту зарядився за 25 хв на Подолі!»</div>
      <div style="display:flex; align-items:center; gap:6px;">
        <img src="{AV1_URL}" style="width:24px; height:24px; border-radius:50%; object-fit:cover;">
        <span style="font-size:10px; font-weight:700;">Олексій (Tesla Y)</span>
      </div>
    </div>
    <div style="border:1px solid #E2E8F0; border-radius:8px; padding:10px; margin-bottom:8px; background:#FFF;">
      <div style="color:#F59E0B; font-size:11px; margin-bottom:4px;">★★★★★</div>
      <div style="font-size:11px; color:#334155; margin-bottom:6px;">«Зручний калькулятор витрат і точний кілометраж.»</div>
      <div style="display:flex; align-items:center; gap:6px;">
        <img src="{AV2_URL}" style="width:24px; height:24px; border-radius:50%; object-fit:cover;">
        <span style="font-size:10px; font-weight:700;">Олена (Nissan Leaf)</span>
      </div>
    </div>
  </div>

  <!-- SECTION 8: FORM -->
  <div class="sec" style="background:#F1F5F9; border-radius:8px; margin:0 14px 14px;">
    <div style="font-weight:800; font-size:13px; margin-bottom:4px;">Маєте локацію?</div>
    <div style="font-size:10px; color:#64748B; margin-bottom:8px;">Встановіть зарядну станцію ChargeUA</div>
    <input type="text" placeholder="Ім'я та номер телефону" style="width:100%; height:32px; border:1px solid #CBD5E1; border-radius:6px; padding:0 8px; font-size:11px; margin-bottom:6px; background:#FFF;">
    <button class="btn-pri" style="padding:8px; font-size:11px;">Подати заявку</button>
  </div>

  <!-- SECTION 9: FOOTER & BOTTOM NAV -->
  <div class="footer">
    <div style="display:flex; align-items:center; gap:6px; margin-bottom:6px;">
      <img src="{LOGO_URL}" style="width:18px; height:18px; filter:brightness(0) invert(1);">
      <span style="font-size:15px; font-weight:800;">ChargeUA</span>
    </div>
    <p style="font-size:10px; color:#94A3B8; margin-bottom:8px;">Національний агрегатор зарядної інфраструктури.</p>
    <div style="font-size:9px; color:#64748B; border-top:1px solid #1E293B; padding-top:8px;">
      © 2026 ChargeUA · ПП-24 · САПР
    </div>
  </div>

  <div class="b-nav">
    <span style="color:#005EC9;">🏠 Головна</span>
    <span>🗺️ Карта</span>
    <span>⚡ Кальк</span>
    <span>👤 Профіль</span>
  </div>
</body></html>"""

p_mob_html = os.path.join(HTML_DIR, "mobile_full_tuned.html")
with open(p_mob_html, "w", encoding="utf-8") as f:
    f.write(html_mob)

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

p_mob_tall = os.path.join(HTML_DIR, "mobile_tall_tuned.png")
render_chrome(p_mob_html, p_mob_tall, 390, 3950, scale=1.5)

im_mob = Image.open(p_mob_tall)
mw, mh = im_mob.size
print("Mobile tall size:", mw, mh)

m_sh = mh // 4
m1 = im_mob.crop((0, 0, mw, m_sh))
m2 = im_mob.crop((0, m_sh, mw, 2 * m_sh))
m3 = im_mob.crop((0, 2 * m_sh, mw, 3 * m_sh))
m4 = im_mob.crop((0, 3 * m_sh, mw, mh))
if m4.size[1] != m_sh:
    m4 = m4.resize((mw, m_sh))

m_gap = 16
comp_mw = mw * 4 + m_gap * 3
comp_mob = Image.new("RGB", (comp_mw, m_sh), (255, 255, 255))
comp_mob.paste(m1, (0, 0))
comp_mob.paste(m2, (mw + m_gap, 0))
comp_mob.paste(m3, (2 * (mw + m_gap), 0))
comp_mob.paste(m4, (3 * (mw + m_gap), 0))
comp_mob.save(os.path.join(SCR_DIR, "fig16_mobile.png"))
print("Saved tuned fig16_mobile.png")
