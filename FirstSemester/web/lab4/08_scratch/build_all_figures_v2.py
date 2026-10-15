# -*- coding: utf-8 -*-
"""
Generator for all 22 figures strictly matching the student reference report (ReadSpace, Kobrak Yaroslav)
Incorporating user feedback:
1. Fig 13 (Desktop Top): Hero visual (car & charging station) centered-right, 100% visible, not cut off.
2. Fig 14 (Desktop Bottom): Video demonstration, generator, reviews with real driver avatars, footer.
3. Fig 15 (Tablet): 3 vertical columns side by side showing full tablet page, with video/image as background.
4. Fig 16 (Mobile): 4 vertical columns side by side showing full mobile page, not cut off or short.
5. Fig 17 & 18: No "Figma AI" text in catalog & station titles.
6. Fig 19 (Overlays): Authentic mobile drawer and centered modal with dark dimmed backdrop.
7. Fig 09: Authentic Figma Contrast plugin window (before & after).
8. Fig 03: Authentic Relume AI sitemap tree hierarchy.
9. Fig 04: Authentic Relume AI 5 wireframe pages side by side.
"""

import os, subprocess

BASE_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4"
MAT_DIR = os.path.join(BASE_DIR, "materials")
SCR_DIR = os.path.join(BASE_DIR, "screenshots")
HTML_DIR = os.path.join(BASE_DIR, "08_scratch", "html_boards")
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

os.makedirs(SCR_DIR, exist_ok=True)
os.makedirs(HTML_DIR, exist_ok=True)

# Helper to normalize file URLs for Windows
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

def render_figure(name, html_content, width, height, scale=1.5):
    html_path = os.path.join(HTML_DIR, f"{name}.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    out_png = os.path.join(SCR_DIR, f"{name}.png")
    cmd = [
        CHROME_PATH,
        "--headless=new",
        f"--window-size={width},{height}",
        "--hide-scrollbars",
        f"--force-device-scale-factor={scale}",
        f"--screenshot={out_png}",
        f"file:///{html_path.replace(os.sep, '/')}"
    ]
    subprocess.run(cmd, check=True)
    print(f"Rendered {name}.png ({width}x{height})")

COMMON_HEAD = """
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: #FFFFFF;
    color: #0F172A;
    -webkit-font-smoothing: antialiased;
  }
</style>
"""

# =============================================================================
# 01. fig01_user_flows
# =============================================================================
html_fig01 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F8FAFC; padding: 30px; width: 1188px; }}
  .flow-box {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 20px 24px; margin-bottom: 18px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }}
  .title {{ font-size: 15px; font-weight: 700; color: #005EC9; margin-bottom: 14px; display: flex; align-items: center; gap: 8px; }}
  .steps {{ display: flex; align-items: center; gap: 10px; }}
  .step {{ background: #F8FAFC; border: 1.5px solid #CBD5E1; border-radius: 8px; padding: 10px 14px; font-size: 12px; font-weight: 600; text-align: center; min-width: 130px; }}
  .step.start {{ background: #005EC9; color: #FFF; border-color: #005EC9; }}
  .step.success {{ background: #D1FAE5; color: #047857; border-color: #A7F3D0; font-weight: 700; }}
  .arrow {{ color: #94A3B8; font-weight: 800; font-size: 18px; }}
</style></head><body>
  <div style="font-size:20px; font-weight:800; margin-bottom:20px;">User Flow · Сценарії взаємодії водіїв з платформою ChargeUA</div>
  
  <div class="flow-box">
    <div class="title">Сценарій 1 · Підбір електромобіля та точний розрахунок вартості (US-01)</div>
    <div class="steps">
      <div class="step start">Головна сторінка</div><div class="arrow">→</div>
      <div class="step">CTA «Розрахувати»</div><div class="arrow">→</div>
      <div class="step">Модель (Tesla / ID.4)</div><div class="arrow">→</div>
      <div class="step">Слайдер 20% → 80%</div><div class="arrow">→</div>
      <div class="step">Порівняння тарифів</div><div class="arrow">→</div>
      <div class="step success">Рекомендована станція</div>
    </div>
  </div>

  <div class="flow-box">
    <div class="title">Сценарій 2 · Екстрений пошук працюючої станції під час блекауту (US-02)</div>
    <div class="steps">
      <div class="step start">Головна сторінка</div><div class="arrow">→</div>
      <div class="step">Карта станцій</div><div class="arrow">→</div>
      <div class="step">Фільтр «🔋 З генератором»</div><div class="arrow">→</div>
      <div class="step">Слот CCS2 (120 кВт)</div><div class="arrow">→</div>
      <div class="step">Бронювання на 20 хв</div><div class="arrow">→</div>
      <div class="step success">Маршрут у Waze / Maps</div>
    </div>
  </div>

  <div class="flow-box">
    <div class="title">Сценарій 3 · Подання B2B-заявки на встановлення зарядної станції (US-03)</div>
    <div class="steps">
      <div class="step start">Головна сторінка</div><div class="arrow">→</div>
      <div class="step">Розділ «Для бізнесу»</div><div class="arrow">→</div>
      <div class="step">Форма партнера</div><div class="arrow">→</div>
      <div class="step">Валідація контактів</div><div class="arrow">→</div>
      <div class="step">Клік «Подати заявку»</div><div class="arrow">→</div>
      <div class="step success">Оверлей «Заявку прийнято»</div>
    </div>
  </div>
</body></html>"""

# =============================================================================
# 02. fig02_user_flow_2
# =============================================================================
html_fig02 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F8FAFC; padding: 30px; width: 1404px; }}
  .grid {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 16px; margin-top: 20px; }}
  .card {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 12px; overflow: hidden; }}
  .head {{ background: #005EC9; color: #FFF; padding: 12px; font-size: 13px; font-weight: 700; text-align: center; }}
  .head.dark {{ background: #0F172A; }}
  .list {{ padding: 14px; display: flex; flex-direction: column; gap: 8px; }}
  .item {{ background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 8px 10px; font-size: 11px; color: #334155; font-weight: 500; }}
  .item strong {{ color: #005EC9; }}
</style></head><body>
  <div style="font-size:22px; font-weight:800;">Інформаційна архітектура та структура розділів сайту ChargeUA</div>
  <div style="font-size:14px; color:#64748B; margin-top:4px;">5 обов'язкових розділів веб-сервісу з деталізацією блоків головної сторінки</div>
  <div class="grid">
    <div class="card">
      <div class="head">1 · Головна (Home)</div>
      <div class="list">
        <div class="item"><strong>1.</strong> Header + Brand Logo</div>
        <div class="item"><strong>2.</strong> Hero + Quick Car Picker</div>
        <div class="item"><strong>3.</strong> Калькулятор зарядки</div>
        <div class="item"><strong>4.</strong> Live-карта 480+ станцій</div>
        <div class="item"><strong>5.</strong> Блок «Енергонезалежність»</div>
        <div class="item"><strong>6.</strong> Відеодемонстрація</div>
        <div class="item"><strong>7.</strong> Як це працює (3 кроки)</div>
        <div class="item"><strong>8.</strong> Відгуки водіїв</div>
        <div class="item"><strong>9.</strong> Footer & Контакти</div>
      </div>
    </div>
    <div class="card">
      <div class="head dark">2 · Карта станцій</div>
      <div class="list">
        <div class="item">Пошук за локацією / містом</div>
        <div class="item">Фільтр конекторів (CCS2/Type2)</div>
        <div class="item">Фільтр «🔋 З генератором»</div>
        <div class="item">Сортування за потужністю</div>
        <div class="item">Прев'ю карток хабів</div>
      </div>
    </div>
    <div class="card">
      <div class="head dark">3 · Сторінка станції</div>
      <div class="list">
        <div class="item">Фото локації та координати</div>
        <div class="item">Статус портів онлайн (2/4)</div>
        <div class="item">Тарифи (14.50 ₴/кВт·год)</div>
        <div class="item">Бронювання конектора CCS2</div>
        <div class="item">Маршрут у Waze / Maps</div>
      </div>
    </div>
    <div class="card">
      <div class="head dark">4 · Тарифи & Калькулятор</div>
      <div class="list">
        <div class="item">База популярних авто (Tesla/ID.4)</div>
        <div class="item">Слайдер ємності батареї</div>
        <div class="item">Тип струму (AC повільна / DC швидка)</div>
        <div class="item">Порівняння тарифів операторів</div>
      </div>
    </div>
    <div class="card">
      <div class="head dark">5 · Для бізнесу (B2B)</div>
      <div class="list">
        <div class="item">Умови партнерства для локацій</div>
        <div class="item">Калькулятор дохідності станції</div>
        <div class="item">Резервне генераторне живлення</div>
        <div class="item">Форма партнерської заявки</div>
      </div>
    </div>
  </div>
</body></html>"""

# =============================================================================
# 03. fig03_sitemap_relume (AUTHENTIC RELUME AI SITEMAP TREE)
# =============================================================================
html_fig03 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F3F4F6; padding: 40px; width: 900px; display: flex; flex-direction: column; align-items: center; }}
  .tree-node {{ background: #FFF; border: 1.5px solid #E5E7EB; border-radius: 14px; padding: 16px 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }}
  .node-title {{ font-size: 14px; font-weight: 700; color: #111827; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #F3F4F6; padding-bottom: 8px; margin-bottom: 8px; }}
  .node-items {{ display: flex; flex-direction: column; gap: 4px; font-size: 11.5px; color: #4B5563; }}
  .connector-v {{ width: 2px; height: 35px; background: #D1D5DB; }}
  .connector-h {{ width: 680px; height: 2px; background: #D1D5DB; position: relative; }}
  .connector-h::before {{ content: ""; position: absolute; left: 0; top: 0; width: 2px; height: 20px; background: #D1D5DB; }}
  .connector-h::after {{ content: ""; position: absolute; right: 0; top: 0; width: 2px; height: 20px; background: #D1D5DB; }}
  .mid-drop-1 {{ position: absolute; left: 226px; top: 0; width: 2px; height: 20px; background: #D1D5DB; }}
  .mid-drop-2 {{ position: absolute; left: 454px; top: 0; width: 2px; height: 20px; background: #D1D5DB; }}
  .child-grid {{ display: grid; grid-template-columns: repeat(4, 190px); gap: 24px; margin-top: 18px; }}
</style></head><body>
  <div style="font-size:12px; font-weight:800; color:#6B7280; text-transform:uppercase; letter-spacing:1px; margin-bottom:14px;">Relume AI · Sitemap Generator</div>
  <div class="tree-node" style="width: 280px;">
    <div class="node-title"><span>📄 Home Page</span><span style="font-size:10px; color:#9CA3AF;">9 sections</span></div>
    <div class="node-items">
      <div>Navbar & Brand Logo</div>
      <div>Hero (Car + Charging Station)</div>
      <div>Why ChargeUA (3 Benefits)</div>
      <div>EV Calculator & Matcher</div>
      <div>Stations Live Map Overview</div>
      <div>Blackout Generator Station</div>
      <div>Video Demonstration</div>
      <div>Testimonials (Driver Reviews)</div>
      <div>Footer & Support</div>
    </div>
  </div>
  <div class="connector-v"></div>
  <div class="connector-h"><div class="mid-drop-1"></div><div class="mid-drop-2"></div></div>
  <div class="child-grid">
    <div class="tree-node">
      <div class="node-title"><span>📍 Stations Map</span></div>
      <div class="node-items">
        <div>Search & Location Filter</div>
        <div>Connector Type Chips</div>
        <div>Generator ON Filter</div>
        <div>Station Cards Grid</div>
        <div>Cluster Map Pins</div>
        <div>Footer</div>
      </div>
    </div>
    <div class="tree-node">
      <div class="node-title"><span>⚡ Station Details</span></div>
      <div class="node-items">
        <div>Hub Photo Gallery</div>
        <div>Connectors Live Status</div>
        <div>Tariff & Billing Specs</div>
        <div>Booking Slot Modal</div>
        <div>Waze / Maps Navigation</div>
        <div>Footer</div>
      </div>
    </div>
    <div class="tree-node">
      <div class="node-title"><span>🔋 Tariffs & Calc</span></div>
      <div class="node-items">
        <div>EV Model Presets</div>
        <div>Battery Slider 0-100%</div>
        <div>AC / DC Comparison</div>
        <div>Network Rates Comparison</div>
        <div>Savings vs Petrol</div>
        <div>Footer</div>
      </div>
    </div>
    <div class="tree-node">
      <div class="node-title"><span>💼 For Business</span></div>
      <div class="node-items">
        <div>Host Partner Benefits</div>
        <div>Commercial ROI Model</div>
        <div>Backup Generator Kit</div>
        <div>Station Installation Form</div>
        <div>FAQ Accordion</div>
        <div>Footer</div>
      </div>
    </div>
  </div>
</body></html>"""

# =============================================================================
# 04. fig04_wireframes_relume (5 WIREFRAME PAGES SIDE BY SIDE)
# =============================================================================
html_fig04 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F3F4F6; padding: 25px; width: 1100px; }}
  .pages-row {{ display: flex; gap: 18px; justify-content: center; }}
  .wire-col {{ background: #FFF; border: 1px solid #D1D5DB; border-radius: 8px; width: 200px; padding: 12px; display: flex; flex-direction: column; gap: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }}
  .wire-head {{ font-size: 11px; font-weight: 700; color: #111827; border-bottom: 1px solid #E5E7EB; padding-bottom: 6px; text-align: center; }}
  .wire-block {{ background: #F9FAFB; border: 1px dashed #CBD5E1; border-radius: 4px; padding: 8px 6px; font-size: 9.5px; color: #64748B; text-align: center; }}
  .wire-block.main {{ background: #F1F5F9; border-style: solid; font-weight: 600; color: #1E293B; }}
</style></head><body>
  <div style="font-size:16px; font-weight:800; color:#111827; margin-bottom:14px; text-align:center;">Relume AI · Згенеровані низькодеталізовані каркаси (5 сторінок сайту)</div>
  <div class="pages-row">
    <div class="wire-col">
      <div class="wire-head">01 · Home Page</div>
      <div class="wire-block">Header [Logo | Nav | CTA]</div>
      <div class="wire-block main" style="height:60px; display:flex; align-items:center; justify-content:center;">Hero [H1 | Copy | Visual]</div>
      <div class="wire-block">Benefits [3x Icon Cards]</div>
      <div class="wire-block main">Calculator [Slider | Price]</div>
      <div class="wire-block">Live Map [Hubs Overview]</div>
      <div class="wire-block">Generator Backup Block</div>
      <div class="wire-block">Video Tutorial Preview</div>
      <div class="wire-block">Testimonials [Driver Reviews]</div>
      <div class="wire-block">Footer [4 Columns]</div>
    </div>
    <div class="wire-col">
      <div class="wire-head">02 · Stations Map</div>
      <div class="wire-block">Header</div>
      <div class="wire-block">Search & Filters Bar</div>
      <div class="wire-block main" style="height:140px; display:flex; align-items:center; justify-content:center;">Interactive Map Container</div>
      <div class="wire-block">Station Cards List</div>
      <div class="wire-block">Pagination</div>
      <div class="wire-block">Footer</div>
    </div>
    <div class="wire-col">
      <div class="wire-head">03 · Station Details</div>
      <div class="wire-block">Header</div>
      <div class="wire-block main" style="height:80px; display:flex; align-items:center; justify-content:center;">Station Photo Hero</div>
      <div class="wire-block">Telemetry & Port Statuses</div>
      <div class="wire-block">Tariff Pricing Table</div>
      <div class="wire-block">Booking Form Modal</div>
      <div class="wire-block">Nearby Amenities</div>
      <div class="wire-block">Footer</div>
    </div>
    <div class="wire-col">
      <div class="wire-head">04 · Tariffs & Calc</div>
      <div class="wire-block">Header</div>
      <div class="wire-block main" style="height:90px; display:flex; align-items:center; justify-content:center;">Full Calculator Suite</div>
      <div class="wire-block">Network Operator Rates</div>
      <div class="wire-block">Comparison Matrix</div>
      <div class="wire-block">Savings Counter</div>
      <div class="wire-block">Footer</div>
    </div>
    <div class="wire-col">
      <div class="wire-head">05 · For Business</div>
      <div class="wire-block">Header</div>
      <div class="wire-block main" style="height:70px; display:flex; align-items:center; justify-content:center;">B2B Proposal Hero</div>
      <div class="wire-block">Partner Revenue Model</div>
      <div class="wire-block">Installation Steps</div>
      <div class="wire-block">Contact Form</div>
      <div class="wire-block">FAQ Accordion</div>
      <div class="wire-block">Footer</div>
    </div>
  </div>
</body></html>"""

# =============================================================================
# 05. fig05_wireframe_desktop (FULL TALL COLUMN WIREFRAME)
# =============================================================================
html_fig05 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #E2E8F0; padding: 25px; width: 520px; display: flex; justify-content: center; }}
  .wf-page {{ background: #FFF; width: 470px; border: 1.5px solid #94A3B8; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.06); }}
  .wf-sec {{ border-bottom: 1.5px dashed #CBD5E1; padding: 14px 18px; }}
  .wf-tag {{ font-size: 10px; font-weight: 700; color: #64748B; text-transform: uppercase; margin-bottom: 6px; }}
  .wf-rect {{ background: #F1F5F9; border: 1px solid #CBD5E1; border-radius: 6px; padding: 10px; }}
</style></head><body>
  <div class="wf-page">
    <div class="wf-sec" style="background:#F8FAFC; display:flex; justify-content:space-between; align-items:center;">
      <div style="font-weight:800; font-size:13px; color:#334155;">[LOGO] ChargeUA</div>
      <div style="font-size:10px; color:#64748B;">Home | Calc | Map | Tariffs | B2B</div>
      <div style="background:#0F172A; color:#FFF; font-size:9px; padding:4px 8px; border-radius:4px;">[BTN]</div>
    </div>
    <div class="wf-sec">
      <div class="wf-tag">Hero Section</div>
      <div style="display:flex; gap:10px;">
        <div style="flex:1;">
          <div style="height:14px; background:#94A3B8; border-radius:3px; width:80%; margin-bottom:6px;"></div>
          <div style="height:8px; background:#CBD5E1; border-radius:3px; width:100%; margin-bottom:4px;"></div>
          <div style="height:8px; background:#CBD5E1; border-radius:3px; width:60%; margin-bottom:10px;"></div>
          <div style="display:flex; gap:6px;">
            <div style="height:22px; width:65px; background:#334155; border-radius:4px;"></div>
            <div style="height:22px; width:55px; border:1px solid #94A3B8; border-radius:4px;"></div>
          </div>
        </div>
        <div class="wf-rect" style="width:170px; height:90px; display:flex; align-items:center; justify-content:center; font-size:10px; color:#94A3B8;">[Hero Image (Car + Station)]</div>
      </div>
    </div>
    <div class="wf-sec">
      <div class="wf-tag">3 Benefits Strip</div>
      <div style="display:flex; gap:8px;">
        <div class="wf-rect" style="flex:1; font-size:9px;">[Icon] Calculator</div>
        <div class="wf-rect" style="flex:1; font-size:9px;">[Icon] Live Map</div>
        <div class="wf-rect" style="flex:1; font-size:9px;">[Icon] 100% Generator</div>
      </div>
    </div>
    <div class="wf-sec">
      <div class="wf-tag">Interactive Calculator</div>
      <div class="wf-rect" style="height:80px; display:flex; flex-direction:column; justify-content:center; gap:6px;">
        <div style="font-size:10px; font-weight:700;">[Car Presets: Tesla | ID.4 | Leaf]</div>
        <div style="height:6px; background:#CBD5E1; border-radius:3px; width:90%;"></div>
        <div style="font-size:11px; font-weight:800; color:#0F172A;">652.50 UAH · ~28 min</div>
      </div>
    </div>
    <div class="wf-sec">
      <div class="wf-tag">Popular Stations Grid</div>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
        <div class="wf-rect" style="height:70px; font-size:9px;">[Card] Kyiv Hub<br>120 kW · Gen ON</div>
        <div class="wf-rect" style="height:70px; font-size:9px;">[Card] Lviv Hub<br>160 kW · Gen ON</div>
      </div>
    </div>
    <div class="wf-sec" style="background:#F8FAFC;">
      <div class="wf-tag">Blackout Protection</div>
      <div class="wf-rect" style="height:65px; font-size:9.5px; display:flex; align-items:center; justify-content:center;">[Industrial Generator 160 kW Specs]</div>
    </div>
    <div class="wf-sec">
      <div class="wf-tag">Driver Reviews</div>
      <div style="display:flex; gap:6px;">
        <div class="wf-rect" style="flex:1; font-size:8.5px;">[Av] "Super fast!"</div>
        <div class="wf-rect" style="flex:1; font-size:8.5px;">[Av] "Saved my trip"</div>
      </div>
    </div>
    <div class="wf-sec" style="background:#0F172A; color:#FFF; font-size:9px; text-align:center; padding:16px;">
      [Footer 4 Columns & Copyright ChargeUA 2026]
    </div>
  </div>
</body></html>"""

# =============================================================================
# 06. fig06_wireframe_mobile (FULL TALL COLUMN MOBILE WIREFRAME)
# =============================================================================
html_fig06 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #E2E8F0; padding: 25px; width: 400px; display: flex; justify-content: center; }}
  .wf-page {{ background: #FFF; width: 340px; border: 1.5px solid #94A3B8; border-radius: 8px; overflow: hidden; }}
  .wf-sec {{ border-bottom: 1.5px dashed #CBD5E1; padding: 12px 14px; }}
  .wf-tag {{ font-size: 9.5px; font-weight: 700; color: #64748B; text-transform: uppercase; margin-bottom: 4px; }}
  .wf-rect {{ background: #F1F5F9; border: 1px solid #CBD5E1; border-radius: 6px; padding: 8px; }}
</style></head><body>
  <div class="wf-page">
    <div class="wf-sec" style="display:flex; justify-content:space-between; align-items:center; background:#F8FAFC;">
      <div style="font-weight:800; font-size:12px;">ChargeUA</div>
      <div style="font-size:16px;">[☰]</div>
    </div>
    <div class="wf-sec">
      <div class="wf-tag">Hero (Mobile)</div>
      <div style="height:12px; background:#94A3B8; border-radius:3px; width:75%; margin-bottom:6px;"></div>
      <div style="height:7px; background:#CBD5E1; border-radius:3px; width:90%; margin-bottom:8px;"></div>
      <div class="wf-rect" style="height:75px; display:flex; align-items:center; justify-content:center; font-size:9px; color:#94A3B8; margin-bottom:8px;">[Hero Visual]</div>
      <div style="height:26px; background:#0F172A; border-radius:4px;"></div>
    </div>
    <div class="wf-sec">
      <div class="wf-tag">Benefits</div>
      <div class="wf-rect" style="font-size:9px; margin-bottom:4px;">• Accurate Calculator</div>
      <div class="wf-rect" style="font-size:9px; margin-bottom:4px;">• Live Map 480+ Hubs</div>
      <div class="wf-rect" style="font-size:9px;">• 100% Generator Backup</div>
    </div>
    <div class="wf-sec">
      <div class="wf-tag">Mobile Calculator</div>
      <div class="wf-rect" style="height:65px; font-size:9.5px;">[Slider] 20% → 80%<br><strong>652.50 UAH (~28 min)</strong></div>
    </div>
    <div class="wf-sec">
      <div class="wf-tag">Stations</div>
      <div class="wf-rect" style="height:65px; font-size:9px; margin-bottom:6px;">[Hub Kyiv-Podil · 120 kW]</div>
      <div class="wf-rect" style="height:65px; font-size:9px;">[Hub Arena Lviv · 160 kW]</div>
    </div>
    <div class="wf-sec">
      <div class="wf-tag">Generator Blackout</div>
      <div class="wf-rect" style="height:55px; font-size:9px;">[Backup Generator Info]</div>
    </div>
    <div class="wf-sec">
      <div class="wf-tag">Reviews</div>
      <div class="wf-rect" style="height:45px; font-size:8.5px;">★★★★★ "Saved my trip"</div>
    </div>
    <div class="wf-sec" style="background:#0F172A; color:#FFF; font-size:9px; text-align:center;">
      [Mobile Footer & Copyright]
    </div>
  </div>
</body></html>"""

# =============================================================================
# 07. fig07_brand_colors
# =============================================================================
html_fig07 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F8FAFC; padding: 30px; width: 1291px; }}
  .grid {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 16px; margin-top: 20px; }}
  .box {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.03); }}
  .swatch {{ height: 110px; }}
  .info {{ padding: 12px; }}
  .name {{ font-size: 13px; font-weight: 700; color: #0F172A; margin-bottom: 2px; }}
  .hex {{ font-size: 12px; font-weight: 600; color: #64748B; font-family: monospace; }}
  .role {{ font-size: 10.5px; color: #94A3B8; margin-top: 4px; }}
</style></head><body>
  <div style="font-size:22px; font-weight:800;">Колірні стилі та дизайн-токени ChargeUA (Figma Color Variables)</div>
  <div style="font-size:14px; color:#64748B; margin-top:4px;">Семантична палітра бренду, узгоджена з результатами Лабораторної роботи №3</div>
  <div class="grid">
    <div class="box">
      <div class="swatch" style="background:#005EC9;"></div>
      <div class="info"><div class="name">Primary</div><div class="hex">#005EC9</div><div class="role">Основні CTA, активні стани</div></div>
    </div>
    <div class="box">
      <div class="swatch" style="background:#004BB5;"></div>
      <div class="info"><div class="name">Primary Hover</div><div class="hex">#004BB5</div><div class="role">Стан наведення кнопок</div></div>
    </div>
    <div class="box">
      <div class="swatch" style="background:#00E5FF;"></div>
      <div class="info"><div class="name">Accent Cyan</div><div class="hex">#00E5FF</div><div class="role">Неонові індикатори, акценти</div></div>
    </div>
    <div class="box">
      <div class="swatch" style="background:#0F172A;"></div>
      <div class="info"><div class="name">Dark Navy</div><div class="hex">#0F172A</div><div class="role">Основні тексти, Topbar, Footer</div></div>
    </div>
    <div class="box">
      <div class="swatch" style="background:#047857;"></div>
      <div class="info"><div class="name">Success Green</div><div class="hex">#047857</div><div class="role">Статус «🔋 Генератор ON»</div></div>
    </div>
    <div class="box">
      <div class="swatch" style="background:#F8FAFC; border-bottom:1px solid #E2E8F0;"></div>
      <div class="info"><div class="name">Surface Bg</div><div class="hex">#F8FAFC</div><div class="role">Фон карток та секцій</div></div>
    </div>
  </div>
</body></html>"""

# =============================================================================
# 08. fig08_wireframe_fixes
# =============================================================================
html_fig08 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F8FAFC; padding: 30px; width: 1382px; }}
  .compare {{ display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 20px; }}
  .col-box {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 14px; padding: 24px; }}
  .head-tag {{ display: inline-block; padding: 4px 12px; border-radius: 6px; font-size: 11px; font-weight: 800; margin-bottom: 14px; }}
  .head-tag.bad {{ background: #FEE2E2; color: #DC2626; }}
  .head-tag.good {{ background: #D1FAE5; color: #047857; }}
  .item-row {{ background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px; margin-bottom: 12px; font-size: 12.5px; }}
  .item-row strong {{ display: block; margin-bottom: 4px; }}
</style></head><body>
  <div style="font-size:22px; font-weight:800;">Аудит низькодеталізованого каркаса та впроваджені UX-виправлення</div>
  <div style="font-size:14px; color:#64748B; margin-top:4px;">Порівняння початкової ШІ-генерації каркасу та оптимізованого фінального макета</div>
  <div class="compare">
    <div class="col-box">
      <div class="head-tag bad">ПОЧАТКОВИЙ ВАРІАНТ (ШІ-КАРКАС)</div>
      <div class="item-row">
        <strong style="color:#DC2626;">❌ Розмитий фокус у Hero:</strong>
        Три однакові кнопки дії без візуального пріоритету розсіювали увагу водія.
      </div>
      <div class="item-row">
        <strong style="color:#DC2626;">❌ Відсутність швидких пресетів у калькуляторі:</strong>
        Користувач мав вручну вводити ємність батареї без підказки моделі.
      </div>
      <div class="item-row">
        <strong style="color:#DC2626;">❌ Відсутність фільтра генераторів:</strong>
        Станції показувалися загальним списком без статусу живлення під час аварійних відключень.
      </div>
      <div class="item-row">
        <strong style="color:#DC2626;">❌ Занижені розміри тач-зон (24 px):</strong>
        Чекбокси та перемикачі на мобільних пристроях не відповідали стандарту WCAG 2.1 (≥ 44 px).
      </div>
    </div>
    <div class="col-box">
      <div class="head-tag good">ОПТИМІЗОВАНИЙ ВАРІАНТ (ПІСЛЯ UX-АУДИТУ)</div>
      <div class="item-row">
        <strong style="color:#047857;">✓ Чітка візуальна ієрархія Hero:</strong>
        1 Primary кнопка («Розрахувати зарядку») + 1 контурна Secondary («Знайти на карті»).
      </div>
      <div class="item-row">
        <strong style="color:#047857;">✓ Пресети авто в 1 клік:</strong>
        Швидкі чипи Tesla Model Y, VW ID.4, Nissan Leaf миттєво підставляють ємність батареї.
      </div>
      <div class="item-row">
        <strong style="color:#047857;">✓ Виділений фільтр «🔋 З генератором»:</strong>
        Зелений статусний бейдж із гарантією 100% Uptime під час блекаутів.
      </div>
      <div class="item-row">
        <strong style="color:#047857;">✓ Оптимізовані інтерактивні зони (48 px):</strong>
        Усі інтерактивні елементи збільшено до 48 px для зручного керування однією рукою за кермом.
      </div>
    </div>
  </div>
</body></html>"""

# =============================================================================
# 09. fig09_contrast_plugin (AUTHENTIC FIGMA CONTRAST PLUGIN WINDOW)
# =============================================================================
html_fig09 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #E2E8F0; padding: 25px; width: 800px; display: flex; justify-content: center; gap: 20px; }}
  .plugin-win {{ background: #FFFFFF; border-radius: 12px; width: 370px; box-shadow: 0 10px 25px rgba(0,0,0,0.15); overflow: hidden; border: 1px solid #CBD5E1; }}
  .win-title {{ background: #1E293B; color: #FFF; padding: 10px 14px; font-size: 13px; font-weight: 700; display: flex; justify-content: space-between; align-items: center; }}
  .win-tabs {{ display: flex; border-bottom: 1px solid #E2E8F0; background: #F8FAFC; }}
  .win-tab {{ padding: 8px 16px; font-size: 12px; font-weight: 600; color: #64748B; }}
  .win-tab.active {{ color: #005EC9; border-bottom: 2px solid #005EC9; background: #FFF; }}
  .win-body {{ padding: 14px; }}
  .action-row {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }}
  .scan-btn {{ background: #FFF; border: 1.5px solid #0F172A; border-radius: 6px; padding: 6px 14px; font-size: 11.5px; font-weight: 700; color: #0F172A; }}
  .issue-item {{ display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid #F1F5F9; font-size: 12px; }}
  .badge-fail {{ background: #EF4444; color: #FFF; font-size: 10px; font-weight: 800; padding: 3px 8px; border-radius: 999px; }}
  .badge-pass {{ background: #10B981; color: #FFF; font-size: 10px; font-weight: 800; padding: 3px 8px; border-radius: 999px; }}
  .badge-warn {{ background: #F1F5F9; color: #64748B; font-size: 10px; font-weight: 600; padding: 3px 8px; border-radius: 4px; }}
</style></head><body>
  <!-- Ліве вікно: ДО ВИПРАВЛЕННЯ -->
  <div class="plugin-win">
    <div class="win-title">
      <div style="display:flex; align-items:center; gap:6px;"><span>✅</span> Contrast</div>
      <div>✕</div>
    </div>
    <div class="win-tabs">
      <div class="win-tab">Select</div>
      <div class="win-tab active">Scan</div>
    </div>
    <div class="win-body">
      <div class="action-row">
        <div style="font-size:12px; font-weight:700;">Found 4 issues</div>
        <button class="scan-btn">Scan selection</button>
      </div>
      <div class="issue-item">
        <span>Т  Текст «З генератором»</span>
        <span class="badge-fail">FAIL 2.54:1</span>
      </div>
      <div class="issue-item">
        <span>Т  Підпис порту CCS2</span>
        <span class="badge-fail">FAIL 2.85:1</span>
      </div>
      <div class="issue-item">
        <span>Т  Другорядний підпис</span>
        <span class="badge-warn">Requires Sample</span>
      </div>
      <div class="issue-item">
        <span>Т  Рамка поля пошуку</span>
        <span class="badge-warn">UI 2.9:1</span>
      </div>
      <div style="margin-top:14px; font-size:11px; color:#64748B;">
        <input type="checkbox" checked> AA &nbsp;&nbsp; <input type="checkbox"> AAA
      </div>
    </div>
  </div>

  <!-- Праве вікно: ПІСЛЯ ВИПРАВЛЕННЯ ТОКЕНАМИ -->
  <div class="plugin-win">
    <div class="win-title">
      <div style="display:flex; align-items:center; gap:6px;"><span>✅</span> Contrast</div>
      <div>✕</div>
    </div>
    <div class="win-tabs">
      <div class="win-tab">Select</div>
      <div class="win-tab active">Scan</div>
    </div>
    <div class="win-body">
      <div class="action-row">
        <div style="font-size:12px; font-weight:700; color:#047857;">Found 0 issues 🎉</div>
        <button class="scan-btn" style="background:#0F172A; color:#FFF;">Scan page 👆</button>
      </div>
      <div class="issue-item">
        <span>Т  Текст «З генератором» (#047857)</span>
        <span class="badge-pass">PASS 5.48:1</span>
      </div>
      <div class="issue-item">
        <span>Т  Підпис порту CCS2 (#0F172A)</span>
        <span class="badge-pass">PASS 17.8:1</span>
      </div>
      <div class="issue-item">
        <span>Т  Кнопка Primary (#FFFFFF/#005EC9)</span>
        <span class="badge-pass">PASS 6.10:1</span>
      </div>
      <div class="issue-item">
        <span>Т  CTA (#0F172A / #00E5FF)</span>
        <span class="badge-pass">PASS 9.12:1</span>
      </div>
      <div style="margin-top:14px; font-size:11px; color:#64748B;">
        <input type="checkbox" checked> AA &nbsp;&nbsp; <input type="checkbox" checked> AAA
      </div>
    </div>
  </div>
</body></html>"""

# =============================================================================
# 10. fig10_typography
# =============================================================================
html_fig10 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F8FAFC; padding: 30px; width: 1166px; }}
  .t-table {{ width: 100%; border-collapse: collapse; margin-top: 18px; background: #FFF; border-radius: 12px; overflow: hidden; border: 1.5px solid #E2E8F0; }}
  .t-table th, .t-table td {{ padding: 12px 18px; border-bottom: 1px solid #E2E8F0; text-align: left; font-size: 12.5px; }}
  .t-table th {{ background: #F1F5F9; font-weight: 700; color: #475569; }}
</style></head><body>
  <div style="font-size:22px; font-weight:800;">Типографічна система (Inter · 12 текстових стилів)</div>
  <table class="t-table">
    <tr><th>Стиль</th><th>Розмір / Інтерліньяж</th><th>Насиченість</th><th>Зразок тексту</th></tr>
    <tr><td><strong>Display / H1</strong></td><td>44 px / 52 px</td><td>Bold (700)</td><td style="font-size:20px; font-weight:700;">Швидка зарядка по всій Україні</td></tr>
    <tr><td><strong>Heading / H2</strong></td><td>32 px / 40 px</td><td>Bold (700)</td><td style="font-size:17px; font-weight:700;">Енергонезалежність 24/7 у блекаути</td></tr>
    <tr><td><strong>Heading / H3</strong></td><td>24 px / 32 px</td><td>Semi Bold (600)</td><td style="font-size:15px; font-weight:600;">Калькулятор вартості сесії</td></tr>
    <tr><td><strong>Heading / H4</strong></td><td>18 px / 26 px</td><td>Bold (700)</td><td style="font-size:14px; font-weight:700;">Хаб «Київ-Поділ» · 120 кВт CCS2</td></tr>
    <tr><td><strong>Body / Large</strong></td><td>16 px / 24 px</td><td>Regular (400)</td><td style="font-size:13px;">Знаходьте найближчі станції за лічені секунди.</td></tr>
    <tr><td><strong>Body / Medium</strong></td><td>14 px / 20 px</td><td>Regular / Medium</td><td style="font-size:12.5px;">Тариф: 14.50 ₴/кВт·год · Вільні слоти (3/4)</td></tr>
    <tr><td><strong>Body / Small</strong></td><td>12 px / 16 px</td><td>Semi Bold (600)</td><td style="font-size:11px; font-weight:600;">Популярні конектори: Type 2, CCS 2, CHAdeMO</td></tr>
    <tr><td><strong>Caption / Micro</strong></td><td>11 px / 14 px</td><td>Bold (700)</td><td style="font-size:10px; font-weight:700; color:#047857;">🔋 ГЕНЕРАТОР ON · 100% UPTIME</td></tr>
  </table>
</body></html>"""

# =============================================================================
# 11. fig11_spacing_grid
# =============================================================================
html_fig11 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F8FAFC; padding: 30px; width: 1166px; }}
  .box {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 20px; margin-bottom: 20px; }}
  .bars {{ display: flex; align-items: flex-end; gap: 18px; margin-top: 14px; }}
  .bar-col {{ display: flex; flex-direction: column; align-items: center; gap: 6px; }}
  .bar {{ background: #005EC9; border-radius: 4px; width: 44px; }}
  .radii {{ display: flex; gap: 20px; margin-top: 14px; }}
  .r-box {{ width: 80px; height: 80px; background: #EFF6FF; border: 2px solid #005EC9; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700; color: #005EC9; }}
</style></head><body>
  <div style="font-size:22px; font-weight:800; margin-bottom:16px;">Система відступів (Spacing), заокруглень (Radii) та сітки (Grid)</div>
  <div class="box">
    <div style="font-size:14px; font-weight:700;">1. Шкала відступів (Spacing Scale: 4, 8, 12, 16, 24, 32, 48, 64 px)</div>
    <div class="bars">
      <div class="bar-col"><div class="bar" style="height:12px;"></div><span style="font-size:10px;">4px</span></div>
      <div class="bar-col"><div class="bar" style="height:20px;"></div><span style="font-size:10px;">8px</span></div>
      <div class="bar-col"><div class="bar" style="height:30px;"></div><span style="font-size:10px;">12px</span></div>
      <div class="bar-col"><div class="bar" style="height:40px;"></div><span style="font-size:10px;">16px</span></div>
      <div class="bar-col"><div class="bar" style="height:55px;"></div><span style="font-size:10px;">24px</span></div>
      <div class="bar-col"><div class="bar" style="height:70px;"></div><span style="font-size:10px;">32px</span></div>
      <div class="bar-col"><div class="bar" style="height:90px;"></div><span style="font-size:10px;">48px</span></div>
      <div class="bar-col"><div class="bar" style="height:115px;"></div><span style="font-size:10px;">64px</span></div>
    </div>
  </div>
  <div class="box">
    <div style="font-size:14px; font-weight:700;">2. Радіуси скруглення (Corner Radii: 6, 8, 12, 16, 24 px, Full)</div>
    <div class="radii">
      <div class="r-box" style="border-radius:6px;">6px (Tags)</div>
      <div class="r-box" style="border-radius:8px;">8px (Inputs)</div>
      <div class="r-box" style="border-radius:12px;">12px (Cards)</div>
      <div class="r-box" style="border-radius:16px;">16px (Modals)</div>
      <div class="r-box" style="border-radius:24px;">24px (Hero)</div>
      <div class="r-box" style="border-radius:999px;">Pill</div>
    </div>
  </div>
</body></html>"""

# =============================================================================
# 12. fig12_figma_ai_illustrations
# =============================================================================
html_fig12 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F8FAFC; padding: 25px; width: 1600px; }}
  .grid-top {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 20px; }}
  .grid-bot {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }}
  .card {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 12px; overflow: hidden; }}
  .card img {{ width: 100%; height: 175px; object-fit: cover; display: block; }}
  .info {{ padding: 12px 14px; }}
  .t1 {{ font-size: 13px; font-weight: 700; color: #0F172A; margin-bottom: 2px; }}
  .t2 {{ font-size: 11px; color: #64748B; }}
</style></head><body>
  <div style="font-size:22px; font-weight:800; margin-bottom:4px;">Тематичні ілюстрації та аватари цільових користувачів (Figma AI / Imagen)</div>
  <div style="font-size:14px; color:#64748B; margin-bottom:18px;">4 ілюстрації інфраструктури в палітрі бренду (#005EC9, #00E5FF) + 3 аватари персон водіїв з ЛР1</div>
  <div class="grid-top">
    <div class="card">
      <img src="file:///{HUB_KYIV_URL}">
      <div class="info"><div class="t1">Хаб «Київ-Поділ»</div><div class="t2">Швидкісні колонки 120 кВт CCS2 біля Андріївської церкви</div></div>
    </div>
    <div class="card">
      <img src="file:///{HUB_LVIV_URL}">
      <div class="info"><div class="t1">Хаб «Арена Львів»</div><div class="t2">Ультрашвидкісний хаб 160 кВт із сонячним навісом на трасі М06</div></div>
    </div>
    <div class="card">
      <img src="file:///{GEN_URL}">
      <div class="info"><div class="t1">Резервний генератор</div><div class="t2">Промисловий дизель-генератор для живлення в блекаути</div></div>
    </div>
    <div class="card">
      <img src="file:///{CABLE_URL}">
      <div class="info"><div class="t1">Підключення CCS2</div><div class="t2">Процес зарядки та світлодіодний індикатор з'єднання</div></div>
    </div>
  </div>
  <div class="grid-bot">
    <div class="card" style="display:flex; align-items:center; padding:12px; gap:14px;">
      <img src="file:///{AV1_URL}" style="width:65px; height:65px; border-radius:50%; flex-shrink:0;">
      <div><div class="t1">Олексій (28 років)</div><div class="t2">IT-спеціаліст, водій Tesla Model Y (персонаж з ЛР1)</div></div>
    </div>
    <div class="card" style="display:flex; align-items:center; padding:12px; gap:14px;">
      <img src="file:///{AV2_URL}" style="width:65px; height:65px; border-radius:50%; flex-shrink:0;">
      <div><div class="t1">Олена (26 років)</div><div class="t2">Міська жителька, водійка Nissan Leaf (персонаж з ЛР1)</div></div>
    </div>
    <div class="card" style="display:flex; align-items:center; padding:12px; gap:14px;">
      <img src="file:///{AV3_URL}" style="width:65px; height:65px; border-radius:50%; flex-shrink:0;">
      <div><div class="t1">Сергій (40 років)</div><div class="t2">Менеджер комерційного парку електробусів (B2B сегмент)</div></div>
    </div>
  </div>
</body></html>"""

# =============================================================================
# 13. fig13_desktop_top (DESKTOP HOMEPAGE UPPER HALF - HERO VISUAL FIXED!)
# =============================================================================
html_fig13 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ width: 1440px; margin: 0; background: #FFFFFF; }}
  .topbar {{ background: #0F172A; color: #FFF; font-size: 11px; padding: 7px 60px; display: flex; justify-content: space-between; }}
  header {{ height: 76px; padding: 0 60px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #E2E8F0; }}
  .hero-wrap {{ position: relative; width: 1440px; height: 500px; background: #FFFFFF; overflow: hidden; }}
  .hero-img {{ position: absolute; right: 0; top: 0; width: 62%; height: 100%; object-fit: contain; object-position: right center; z-index: 1; }}
  .hero-content {{ position: relative; z-index: 2; width: 50%; padding: 45px 0 45px 60px; }}
  .benefit-strip {{ padding: 24px 60px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; background: #F8FAFC; border-top: 1px solid #E2E8F0; border-bottom: 1px solid #E2E8F0; }}
  .b-card {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; display: flex; align-items: center; gap: 14px; }}
  .b-card img {{ width: 38px; height: 38px; }}
  .calc-block {{ padding: 40px 60px; background: #FFFFFF; }}
  .calc-card {{ background: #F8FAFC; border: 1.5px solid #CBD5E1; border-radius: 16px; padding: 24px 32px; display: grid; grid-template-columns: 1.2fr 1fr; gap: 32px; align-items: center; }}
</style></head><body>
  <div class="topbar">
    <div>● Мережа ChargeUA: 480+ станцій онлайн по Україні | 100% телеметрія в реальному часі</div>
    <div>Гаряча лінія 24/7: 0 800 300 400 | UA</div>
  </div>
  <header>
    <div style="display:flex; align-items:center; gap:10px;">
      <img src="file:///{LOGO_URL}" style="height:36px;">
      <span style="font-size:22px; font-weight:800; color:#005EC9;">ChargeUA</span>
    </div>
    <div style="display:flex; gap:28px; font-size:14px; font-weight:600; color:#334155;">
      <span style="color:#005EC9;">Головна</span>
      <span>Калькулятор</span>
      <span>Карта станцій</span>
      <span>Тарифи</span>
      <span>Для бізнесу</span>
    </div>
    <div style="display:flex; gap:12px;">
      <button style="background:#FFF; border:1px solid #CBD5E1; padding:9px 18px; border-radius:8px; font-weight:600; font-size:13px;">Увійти</button>
      <button style="background:#005EC9; color:#FFF; border:none; padding:9px 18px; border-radius:8px; font-weight:700; font-size:13px;">Завантажити додаток</button>
    </div>
  </header>

  <div class="hero-wrap">
    <img src="file:///{HERO_URL}" class="hero-img">
    <div class="hero-content">
      <div style="background:#EFF6FF; color:#005EC9; border:1px solid #BFDBFE; display:inline-block; padding:4px 12px; border-radius:999px; font-size:11px; font-weight:700; margin-bottom:14px;">
        ⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР ЗАРЯДНИХ СТАНЦІЙ
      </div>
      <h1 style="font-size:38px; font-weight:800; line-height:1.15; margin-bottom:14px; color:#0F172A;">
        Швидка та надійна зарядка електромобілів по всій Україні
      </h1>
      <p style="font-size:15px; color:#475569; line-height:1.5; margin-bottom:22px; max-width:460px;">
        Знаходьте найближчі станції, розраховуйте вартість за лічені секунди та подорожуйте без хвилювань навіть під час блекаутів.
      </p>
      <div style="display:flex; gap:12px; margin-bottom:22px;">
        <button style="background:#005EC9; color:#FFF; border:none; padding:12px 24px; border-radius:8px; font-size:14px; font-weight:700;">Розрахувати зарядку →</button>
        <button style="background:#FFF; color:#0F172A; border:1.5px solid #CBD5E1; padding:12px 20px; border-radius:8px; font-size:14px; font-weight:600;">Знайти на карті</button>
      </div>
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="font-size:12px; color:#64748B; font-weight:600;">Популярні конектори:</span>
        <span style="background:#F1F5F9; border:1px solid #CBD5E1; border-radius:999px; padding:3px 10px; font-size:11px; font-weight:600;">Type 2 (22 кВт)</span>
        <span style="background:#F1F5F9; border:1px solid #CBD5E1; border-radius:999px; padding:3px 10px; font-size:11px; font-weight:600;">CCS 2 (160 кВт)</span>
        <span style="background:#D1FAE5; color:#047857; border:1px solid #A7F3D0; border-radius:999px; padding:3px 10px; font-size:11px; font-weight:700;">🔋 З генератором</span>
      </div>
    </div>
  </div>

  <div class="benefit-strip">
    <div class="b-card">
      <img src="file:///{CALC_URL}">
      <div><strong style="font-size:14px; display:block;">Точний калькулятор витрат</strong><span style="font-size:12px; color:#64748B;">Автоматичний підбір моделі авто та тарифу</span></div>
    </div>
    <div class="b-card">
      <img src="file:///{LOC_URL}">
      <div><strong style="font-size:14px; display:block;">Live-карта 480+ станцій</strong><span style="font-size:12px; color:#64748B;">Актуальний статус зайнятості та наявності світла</span></div>
    </div>
    <div class="b-card">
      <img src="file:///{INFO_URL}">
      <div><strong style="font-size:14px; display:block;">100% Енергонезалежність</strong><span style="font-size:12px; color:#64748B;">Робота від генераторів під час аварійних відключень</span></div>
    </div>
  </div>

  <div class="calc-block">
    <div style="font-size:24px; font-weight:800; margin-bottom:6px;">Інтерактивний калькулятор зарядки ChargeUA</div>
    <div style="font-size:14px; color:#64748B; margin-bottom:20px;">Оберіть модель електрокара та розрахуйте тривалість сесії й вартість</div>
    <div class="calc-card">
      <div>
        <div style="font-size:13px; font-weight:700; margin-bottom:8px;">Модель автомобіля:</div>
        <div style="display:flex; gap:8px; margin-bottom:18px;">
          <button style="background:#005EC9; color:#FFF; border:none; padding:8px 14px; border-radius:6px; font-size:12px; font-weight:700;">Volkswagen ID.4 (77 кВт·год)</button>
          <button style="background:#FFF; border:1px solid #CBD5E1; padding:8px 14px; border-radius:6px; font-size:12px;">Tesla Model Y</button>
          <button style="background:#FFF; border:1px solid #CBD5E1; padding:8px 14px; border-radius:6px; font-size:12px;">Nissan Leaf</button>
        </div>
        <div style="font-size:13px; font-weight:700; margin-bottom:6px;">Рівень заряду батареї (20% → 80%):</div>
        <div style="height:8px; background:#CBD5E1; border-radius:4px; width:100%; position:relative; margin-bottom:8px;">
          <div style="height:100%; background:#005EC9; border-radius:4px; width:60%;"></div>
        </div>
        <div style="display:flex; justify-content:space-between; font-size:11px; color:#64748B;">
          <span>20% (15.4 кВт·год)</span><span>80% (61.6 кВт·год)</span>
        </div>
      </div>
      <div style="background:#FFF; border:1px solid #E2E8F0; border-radius:12px; padding:18px;">
        <div style="font-size:12px; color:#64748B;">Орієнтовна вартість сесії:</div>
        <div style="font-size:28px; font-weight:800; color:#0F172A; margin:4px 0;">652.50 ₴ <span style="font-size:13px; color:#64748B; font-weight:400;">(14.50 ₴/кВт·год)</span></div>
        <div style="font-size:12px; color:#047857; font-weight:700; margin-bottom:12px;">● Час на 120 кВт DC: ~28 хв | Економія vs Бензин: ~1 420 ₴</div>
        <button style="width:100%; height:40px; background:#005EC9; color:#FFF; border:none; border-radius:8px; font-weight:700; font-size:13px;">Знайти найближчу вільну станцію</button>
      </div>
    </div>
  </div>
</body></html>"""

# =============================================================================
# 14. fig14_desktop_bottom (DESKTOP HOMEPAGE LOWER HALF)
# =============================================================================
html_fig14 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ width: 1440px; margin: 0; background: #FFFFFF; padding-bottom: 0; }}
  .sec {{ padding: 36px 60px; }}
  .gen-box {{ background: #0F172A; color: #FFF; border-radius: 16px; padding: 32px; display: grid; grid-template-columns: 1fr 1fr; gap: 32px; align-items: center; }}
  .stations-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 20px; }}
  .s-card {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 12px; overflow: hidden; }}
  .s-card img {{ width: 100%; height: 160px; object-fit: cover; display: block; }}
  .rev-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 20px; }}
  .r-card {{ background: #F8FAFC; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 20px; }}
  footer {{ background: #0F172A; color: #FFF; padding: 40px 60px 24px; }}
</style></head><body>
  <div class="sec">
    <div class="gen-box">
      <div>
        <div style="color:#00E5FF; font-size:11px; font-weight:800; letter-spacing:1px; margin-bottom:8px;">ЕНЕРГОНЕЗАЛЕЖНІСТЬ 24/7</div>
        <div style="font-size:28px; font-weight:800; margin-bottom:12px; line-height:1.2;">Заряджайте авто навіть під час повних блекаутів</div>
        <p style="font-size:14px; color:#CBD5E1; line-height:1.5; margin-bottom:20px;">
          Ключові хаби ChargeUA обладнано промисловими дизель-генераторами 160–250 кВт. Автоматичний перехід на резервне живлення за 8 секунд гарантує 100% Uptime зарядної мережі.
        </p>
        <button style="background:#00E5FF; color:#0F172A; border:none; padding:12px 22px; border-radius:8px; font-weight:800; font-size:13px;">Показати станції зі світлом</button>
      </div>
      <div>
        <img src="file:///{GEN_URL}" style="width:100%; height:230px; object-fit:cover; border-radius:12px; border:1px solid #334155;">
      </div>
    </div>
  </div>

  <div class="sec" style="background:#F8FAFC;">
    <div style="font-size:24px; font-weight:800;">Популярні зарядні хаби мережі</div>
    <div style="font-size:14px; color:#64748B;">Швидкісні станції з гарантованим живленням та живою телеметрією</div>
    <div class="stations-grid">
      <div class="s-card">
        <img src="file:///{HUB_KYIV_URL}">
        <div style="padding:16px;">
          <div style="font-size:15px; font-weight:700;">Хаб «Київ-Поділ» · 120 кВт CCS2</div>
          <div style="font-size:12px; color:#64748B; margin-bottom:10px;">м. Київ, вул. Сагайдачного, 12</div>
          <div style="background:#D1FAE5; color:#047857; display:inline-block; padding:3px 8px; border-radius:4px; font-size:11px; font-weight:700; margin-bottom:12px;">🔋 Генератор ON · Вільний (3/4)</div>
          <button style="width:100%; height:38px; background:#005EC9; color:#FFF; border:none; border-radius:6px; font-weight:700; font-size:12px;">Забронювати конектор CCS2</button>
        </div>
      </div>
      <div class="s-card">
        <img src="file:///{HUB_LVIV_URL}">
        <div style="padding:16px;">
          <div style="font-size:15px; font-weight:700;">Хаб «Арена Львів» · 160 кВт CCS2</div>
          <div style="font-size:12px; color:#64748B; margin-bottom:10px;">м. Львів, вул. Стрийська, 199</div>
          <div style="background:#D1FAE5; color:#047857; display:inline-block; padding:3px 8px; border-radius:4px; font-size:11px; font-weight:700; margin-bottom:12px;">🔋 Сонячний навіс + Дизель</div>
          <button style="width:100%; height:38px; background:#005EC9; color:#FFF; border:none; border-radius:6px; font-weight:700; font-size:12px;">Забронювати конектор CCS2</button>
        </div>
      </div>
      <div class="s-card">
        <div style="position:relative;">
          <img src="file:///{VIDEO_URL}">
          <div style="position:absolute; inset:0; background:rgba(0,0,0,0.3); display:flex; align-items:center; justify-content:center;">
            <div style="width:48px; height:48px; background:#FFF; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:18px;">▶</div>
          </div>
        </div>
        <div style="padding:16px;">
          <div style="font-size:15px; font-weight:700;">Відеогайд: як зарядитися за 3 кроки</div>
          <div style="font-size:12px; color:#64748B; margin-bottom:10px;">Покрокова інструкція підключення кабелю CCS2</div>
          <button style="width:100%; height:38px; background:#FFF; border:1.5px solid #CBD5E1; color:#0F172A; border-radius:6px; font-weight:700; font-size:12px;">Переглянути відео (0:45)</button>
        </div>
      </div>
    </div>
  </div>

  <div class="sec">
    <div style="font-size:24px; font-weight:800;">Відгуки реальних водіїв</div>
    <div style="font-size:14px; color:#64748B;">Що кажуть власники електромобілів про сервіс ChargeUA</div>
    <div class="rev-grid">
      <div class="r-card">
        <div style="color:#F59E0B; margin-bottom:8px;">★★★★★</div>
        <p style="font-size:13px; line-height:1.5; margin-bottom:14px;">«Під час блекауту на Подолі зарядився за 25 хвилин. Генератор гуде, станція стабільна, кава поруч. Найкращий сервіс!»</p>
        <div style="display:flex; align-items:center; gap:10px;">
          <img src="file:///{AV1_URL}" style="width:42px; height:42px; border-radius:50%; object-fit:cover;">
          <div><div style="font-size:13px; font-weight:700;">Олексій К.</div><div style="font-size:11px; color:#64748B;">Водій Tesla Model Y · Київ</div></div>
        </div>
      </div>
      <div class="r-card">
        <div style="color:#F59E0B; margin-bottom:8px;">★★★★★</div>
        <p style="font-size:13px; line-height:1.5; margin-bottom:14px;">«Дуже зручний калькулятор. Одразу видно скільки кіловат потрібно і яка буде фінальна вартість без прихованих платежів.»</p>
        <div style="display:flex; align-items:center; gap:10px;">
          <img src="file:///{AV2_URL}" style="width:42px; height:42px; border-radius:50%; object-fit:cover;">
          <div><div style="font-size:13px; font-weight:700;">Олена М.</div><div style="font-size:11px; color:#64748B;">Водійка Nissan Leaf · Львів</div></div>
        </div>
      </div>
      <div class="r-card">
        <div style="color:#F59E0B; margin-bottom:8px;">★★★★★</div>
        <p style="font-size:13px; line-height:1.5; margin-bottom:14px;">«Для комерційного парку функція бронювання слотів — знахідка. Жодних простоїв та черг на трасі Київ-Львів.»</p>
        <div style="display:flex; align-items:center; gap:10px;">
          <img src="file:///{AV3_URL}" style="width:42px; height:42px; border-radius:50%; object-fit:cover;">
          <div><div style="font-size:13px; font-weight:700;">Сергій В.</div><div style="font-size:11px; color:#64748B;">Менеджер електрофлоту</div></div>
        </div>
      </div>
    </div>
  </div>

  <footer>
    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:24px;">
      <div>
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
          <img src="file:///{LOGO_URL}" style="height:32px;">
          <span style="font-size:20px; font-weight:800;">ChargeUA</span>
        </div>
        <div style="font-size:12px; color:#94A3B8; max-width:300px;">Національний агрегатор та веб-помічник зарядної інфраструктури України.</div>
      </div>
      <div style="display:flex; gap:60px; font-size:13px; color:#CBD5E1;">
        <div><strong style="color:#FFF; display:block; margin-bottom:10px;">Навігація</strong><div>Головна</div><div>Калькулятор</div><div>Карта станцій</div></div>
        <div><strong style="color:#FFF; display:block; margin-bottom:10px;">Для бізнесу</strong><div>Встановити хаб</div><div>Резервне живлення</div><div>B2B партнерство</div></div>
        <div><strong style="color:#FFF; display:block; margin-bottom:10px;">Контакти</strong><div>0 800 300 400</div><div>support@charge.ua</div><div>Київ, Поділ</div></div>
      </div>
    </div>
    <div style="border-top:1px solid #1E293B; padding-top:16px; font-size:11px; color:#64748B;">
      © 2026 ChargeUA · Лемішка Андрій, ПП-24 · Кафедра САПР, НУ «Львівська політехніка»
    </div>
  </footer>
</body></html>"""

# =============================================================================
# 15. fig15_tablet (3 COLUMNS OF 768px TABLET SCREEN SIDE BY SIDE)
# =============================================================================
html_fig15 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F3F4F6; padding: 25px; width: 1249px; }}
  .tablet-cols {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }}
  .t-col {{ background: #FFF; border: 1.5px solid #CBD5E1; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }}
  .t-sec {{ padding: 16px 20px; border-bottom: 1px solid #E2E8F0; }}
</style></head><body>
  <div style="font-size:18px; font-weight:800; margin-bottom:14px; text-align:center;">Головна сторінка, Tablet 768px (повна адаптивна версія у 3 колонки)</div>
  <div class="tablet-cols">
    <!-- Колонка 1: Header, Hero з фоновим відео/зображенням, 3 бенефіти -->
    <div class="t-col">
      <div style="background:#0F172A; color:#FFF; font-size:9.5px; padding:6px 16px; display:flex; justify-content:space-between;">
        <span>● 480+ станцій онлайн</span><span>0 800 300 400</span>
      </div>
      <div style="padding:12px 16px; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #E2E8F0;">
        <span style="font-weight:800; color:#005EC9; font-size:16px;">ChargeUA</span>
        <span style="font-size:18px;">☰</span>
      </div>
      <div style="position:relative; height:240px; overflow:hidden; background:#F8FAFC;">
        <img src="file:///{HERO_URL}" style="position:absolute; right:-20px; top:0; width:80%; height:100%; object-fit:contain; opacity:0.85;">
        <div style="position:relative; z-index:2; padding:20px 16px; background:linear-gradient(90deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.85) 60%, rgba(255,255,255,0.2) 100%); height:100%;">
          <div style="font-size:9px; font-weight:700; color:#005EC9; margin-bottom:4px;">⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР</div>
          <div style="font-size:20px; font-weight:800; line-height:1.2; margin-bottom:8px;">Швидка зарядка по всій Україні</div>
          <div style="font-size:11px; color:#475569; margin-bottom:12px;">Знайдіть вільну станцію навіть під час блекаутів.</div>
          <button style="background:#005EC9; color:#FFF; border:none; padding:8px 14px; border-radius:6px; font-size:11px; font-weight:700;">Розрахувати →</button>
        </div>
      </div>
      <div class="t-sec">
        <div style="font-size:12px; font-weight:700; margin-bottom:8px;">Чому обирають ChargeUA:</div>
        <div style="display:flex; flex-direction:column; gap:6px; font-size:11px; color:#334155;">
          <div>• 📊 Точний калькулятор витрат батареї</div>
          <div>• 🗺️ Live-карта 480+ станцій онлайн</div>
          <div>• 🔋 100% захист генераторами в блекаут</div>
        </div>
      </div>
    </div>

    <!-- Колонка 2: Калькулятор, генераторний блок, популярні хаби -->
    <div class="t-col">
      <div class="t-sec" style="background:#F8FAFC;">
        <div style="font-size:13px; font-weight:700; margin-bottom:6px;">Калькулятор зарядки</div>
        <div style="font-size:11px; color:#005EC9; font-weight:600; margin-bottom:4px;">Volkswagen ID.4 · 20% → 80%</div>
        <div style="font-size:18px; font-weight:800; color:#0F172A; margin-bottom:6px;">652.50 ₴ (~28 хв)</div>
        <button style="width:100%; height:32px; background:#005EC9; color:#FFF; border:none; border-radius:6px; font-size:11px; font-weight:700;">Знайти станцію</button>
      </div>
      <div class="t-sec">
        <div style="font-size:12px; font-weight:700; margin-bottom:6px;">Енергонезалежність у блекаути</div>
        <img src="file:///{GEN_URL}" style="width:100%; height:120px; object-fit:cover; border-radius:6px; margin-bottom:6px;">
        <div style="font-size:10.5px; color:#64748B;">Дизель-генератори 160 кВт гарантують живлення за 8 секунд.</div>
      </div>
      <div class="t-sec">
        <div style="font-size:12px; font-weight:700; margin-bottom:6px;">Хаб «Київ-Поділ» · 120 кВт</div>
        <img src="file:///{HUB_KYIV_URL}" style="width:100%; height:100px; object-fit:cover; border-radius:6px; margin-bottom:6px;">
        <div style="font-size:10.5px; color:#047857; font-weight:700;">● Генератор ON · Слот CCS2 вільний</div>
      </div>
    </div>

    <!-- Колонка 3: Відео, Відгуки водіїв, Підвал -->
    <div class="t-col">
      <div class="t-sec">
        <div style="font-size:12px; font-weight:700; margin-bottom:6px;">Відеоінструкція користувача</div>
        <img src="file:///{VIDEO_URL}" style="width:100%; height:110px; object-fit:cover; border-radius:6px; margin-bottom:6px;">
        <div style="font-size:10.5px; color:#64748B;">Як підключити CCS2 за 3 прості кроки.</div>
      </div>
      <div class="t-sec">
        <div style="font-size:12px; font-weight:700; margin-bottom:8px;">Відгуки водіїв:</div>
        <div style="display:flex; align-items:center; gap:8px; margin-bottom:8px;">
          <img src="file:///{AV1_URL}" style="width:32px; height:32px; border-radius:50%;">
          <div style="font-size:10.5px;"><strong>Олексій (Tesla Y):</strong> «Під час блекауту зарядився за 25 хв!»</div>
        </div>
        <div style="display:flex; align-items:center; gap:8px;">
          <img src="file:///{AV2_URL}" style="width:32px; height:32px; border-radius:50%;">
          <div style="font-size:10.5px;"><strong>Олена (Leaf):</strong> «Калькулятор розраховує до копійки.»</div>
        </div>
      </div>
      <div style="background:#0F172A; color:#FFF; padding:16px; font-size:10px;">
        <div style="font-weight:800; font-size:13px; margin-bottom:4px;">ChargeUA</div>
        <div style="color:#94A3B8; margin-bottom:8px;">Агрегатор електрозарядок України.</div>
        <div style="color:#64748B;">© 2026 ChargeUA · ПП-24</div>
      </div>
    </div>
  </div>
</body></html>"""

# =============================================================================
# 16. fig16_mobile (4 COLUMNS OF 390px MOBILE SCREEN SIDE BY SIDE)
# =============================================================================
html_fig16 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F3F4F6; padding: 25px; width: 1632px; }}
  .mob-cols {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }}
  .m-col {{ background: #FFF; border: 1.5px solid #CBD5E1; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }}
  .m-sec {{ padding: 14px 16px; border-bottom: 1px solid #E2E8F0; }}
</style></head><body>
  <div style="font-size:18px; font-weight:800; margin-bottom:14px; text-align:center;">Головна сторінка, Mobile 390px (повний мобільний скрол у 4 колонки)</div>
  <div class="mob-cols">
    <!-- Колонка 1: Topbar, Header, Hero з видимим авто, CTA -->
    <div class="m-col">
      <div style="background:#0F172A; color:#FFF; font-size:9px; padding:5px 12px; display:flex; justify-content:space-between;">
        <span>● 480+ станцій онлайн</span><span>UA</span>
      </div>
      <div style="padding:10px 14px; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #E2E8F0;">
        <span style="font-weight:800; color:#005EC9; font-size:16px;">ChargeUA</span>
        <span style="font-size:18px;">☰</span>
      </div>
      <div style="padding:16px 14px;">
        <div style="font-size:8.5px; font-weight:700; color:#005EC9; margin-bottom:4px;">⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР</div>
        <div style="font-size:20px; font-weight:800; line-height:1.2; margin-bottom:8px;">Заряджайте авто без стресу</div>
        <div style="font-size:11px; color:#475569; margin-bottom:12px;">Усі мережі на одній карті з фільтром генераторів у блекаути.</div>
        <img src="file:///{HERO_URL}" style="width:100%; height:130px; object-fit:cover; border-radius:8px; margin-bottom:12px;">
        <button style="width:100%; height:36px; background:#005EC9; color:#FFF; border:none; border-radius:6px; font-weight:700; font-size:11px;">Розрахувати зарядку →</button>
      </div>
      <div class="m-sec" style="background:#F8FAFC;">
        <div style="font-size:11px; font-weight:700; margin-bottom:4px;">Переваги сервісу:</div>
        <div style="font-size:10px; color:#475569;">• Калькулятор витрат батареї<br>• Жива карта 480+ станцій<br>• 100% автономні генератори</div>
      </div>
    </div>

    <!-- Колонка 2: Калькулятор та покроковий гайд -->
    <div class="m-col">
      <div class="m-sec">
        <div style="font-size:13px; font-weight:800; margin-bottom:6px;">Калькулятор вартості</div>
        <div style="font-size:10px; color:#64748B; margin-bottom:8px;">VW ID.4 (77 кВт·год) · 20% → 80%</div>
        <div style="height:6px; background:#CBD5E1; border-radius:3px; margin-bottom:8px;">
          <div style="height:100%; background:#005EC9; border-radius:3px; width:60%;"></div>
        </div>
        <div style="font-size:18px; font-weight:800; color:#0F172A; margin-bottom:4px;">652.50 ₴</div>
        <div style="font-size:10px; color:#047857; font-weight:700; margin-bottom:10px;">Час DC 120 кВт: ~28 хв</div>
        <button style="width:100%; height:34px; background:#0F172A; color:#FFF; border:none; border-radius:6px; font-size:11px; font-weight:700;">Знайти хаб зі світлом</button>
      </div>
      <div class="m-sec">
        <div style="font-size:12px; font-weight:700; margin-bottom:8px;">Як зарядитися за 3 кроки:</div>
        <img src="file:///{CABLE_URL}" style="width:100%; height:110px; object-fit:cover; border-radius:6px; margin-bottom:8px;">
        <div style="font-size:10px; color:#475569;">1. Знайдіть вільну станцію<br>2. Підключіть конектор CCS2<br>3. Оплатіть в 1 клік Apple Pay</div>
      </div>
    </div>

    <!-- Колонка 3: Станції, генераторний захист -->
    <div class="m-col">
      <div class="m-sec">
        <div style="font-size:12px; font-weight:700; margin-bottom:6px;">Хаб «Київ-Поділ» · 120 кВт</div>
        <img src="file:///{HUB_KYIV_URL}" style="width:100%; height:100px; object-fit:cover; border-radius:6px; margin-bottom:6px;">
        <div style="font-size:9.5px; color:#047857; font-weight:700; margin-bottom:8px;">🔋 Генератор ON · Вільний (3/4)</div>
        <button style="width:100%; height:32px; background:#005EC9; color:#FFF; border:none; border-radius:6px; font-size:10px; font-weight:700;">Забронювати CCS2</button>
      </div>
      <div class="m-sec">
        <div style="font-size:12px; font-weight:700; margin-bottom:6px;">Захист від блекаутів</div>
        <img src="file:///{GEN_URL}" style="width:100%; height:90px; object-fit:cover; border-radius:6px; margin-bottom:6px;">
        <div style="font-size:9.5px; color:#475569;">Дизель-генератори 160 кВт на кожному опорному хабі мережі.</div>
      </div>
    </div>

    <!-- Колонка 4: Відгуки, Футер, Bottom Navigation Bar -->
    <div class="m-col">
      <div class="m-sec">
        <div style="font-size:12px; font-weight:700; margin-bottom:6px;">Відгуки водіїв:</div>
        <div style="display:flex; align-items:center; gap:8px; margin-bottom:8px;">
          <img src="file:///{AV1_URL}" style="width:30px; height:30px; border-radius:50%;">
          <div style="font-size:10px;"><strong>Олексій (Tesla):</strong> «Зарядився в блекаут за 25 хв!»</div>
        </div>
        <div style="display:flex; align-items:center; gap:8px;">
          <img src="file:///{AV2_URL}" style="width:30px; height:30px; border-radius:50%;">
          <div style="font-size:10px;"><strong>Олена (Leaf):</strong> «Зручний калькулятор.»</div>
        </div>
      </div>
      <div style="background:#0F172A; color:#FFF; padding:14px; font-size:9.5px;">
        <div style="font-weight:800; font-size:12px; margin-bottom:4px;">ChargeUA</div>
        <div style="color:#94A3B8; margin-bottom:6px;">Агрегатор електрозарядок.</div>
        <div style="color:#64748B;">© 2026 ChargeUA · ПП-24</div>
      </div>
      <div style="background:#FFF; border-top:1px solid #CBD5E1; padding:8px 12px; display:flex; justify-content:space-around; font-size:10px; font-weight:700; color:#64748B;">
        <span style="color:#005EC9;">🏠 Головна</span>
        <span>🗺️ Карта</span>
        <span>🔋 Кальк</span>
        <span>👤 Профіль</span>
      </div>
    </div>
  </div>
</body></html>"""

# =============================================================================
# 17. fig17_catalog_details_desktop (2 DESKTOP PAGES SIDE BY SIDE - NO FIGMA AI!)
# =============================================================================
html_fig17 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F3F4F6; padding: 25px; width: 1291px; }}
  .cols {{ display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }}
  .desk-page {{ background: #FFF; border: 1.5px solid #CBD5E1; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }}
  .d-head {{ height: 50px; padding: 0 20px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #E2E8F0; }}
  .d-body {{ padding: 20px; }}
</style></head><body>
  <div style="font-size:18px; font-weight:800; margin-bottom:14px; text-align:center;">Сторінки «Каталог станцій» та «Деталі станції» (Desktop 1440)</div>
  <div class="cols">
    <!-- Ліва сторінка: Каталог та карта -->
    <div class="desk-page">
      <div class="d-head">
        <span style="font-weight:800; color:#005EC9; font-size:15px;">ChargeUA</span>
        <span style="font-size:11px; color:#64748B;">Каталог / Карта</span>
      </div>
      <div class="d-body">
        <div style="font-size:16px; font-weight:800; margin-bottom:4px;">Карта та каталог станцій ChargeUA</div>
        <div style="font-size:11px; color:#64748B; margin-bottom:12px;">Пошук серед 480+ станцій України з живою телеметрією</div>
        <div style="background:#F8FAFC; border:1px solid #CBD5E1; border-radius:8px; padding:8px 12px; font-size:11px; color:#64748B; margin-bottom:10px;">
          🔍 Введіть місто або назву станції (Київ, Львів, Одеса)...
        </div>
        <div style="display:flex; gap:6px; margin-bottom:14px;">
          <span style="background:#005EC9; color:#FFF; font-size:10px; font-weight:700; padding:3px 8px; border-radius:4px;">Всі станції</span>
          <span style="background:#D1FAE5; color:#047857; font-size:10px; font-weight:700; padding:3px 8px; border-radius:4px;">🔋 З генератором</span>
          <span style="background:#F1F5F9; font-size:10px; padding:3px 8px; border-radius:4px;">CCS2 (120+ кВт)</span>
        </div>
        <div style="display:flex; flex-direction:column; gap:10px;">
          <div style="border:1px solid #E2E8F0; border-radius:8px; padding:10px; display:flex; gap:12px;">
            <img src="file:///{HUB_KYIV_URL}" style="width:90px; height:60px; object-fit:cover; border-radius:6px;">
            <div>
              <div style="font-size:12px; font-weight:700;">Хаб «Київ-Поділ» · 120 кВт CCS2</div>
              <div style="font-size:10px; color:#64748B;">вул. Сагайдачного, 12</div>
              <div style="font-size:10px; color:#047857; font-weight:700; margin-top:2px;">● Генератор ON · Вільний (3/4)</div>
            </div>
          </div>
          <div style="border:1px solid #E2E8F0; border-radius:8px; padding:10px; display:flex; gap:12px;">
            <img src="file:///{HUB_LVIV_URL}" style="width:90px; height:60px; object-fit:cover; border-radius:6px;">
            <div>
              <div style="font-size:12px; font-weight:700;">Хаб «Арена Львів» · 160 кВт CCS2</div>
              <div style="font-size:10px; color:#64748B;">вул. Стрийська, 199</div>
              <div style="font-size:10px; color:#047857; font-weight:700; margin-top:2px;">● Сонячний навіс · Вільний (2/4)</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Права сторінка: Деталі станції -->
    <div class="desk-page">
      <div class="d-head">
        <span style="font-weight:800; color:#005EC9; font-size:15px;">ChargeUA</span>
        <span style="font-size:11px; color:#64748B;">Хаб «Київ-Поділ»</span>
      </div>
      <div class="d-body">
        <img src="file:///{HUB_KYIV_URL}" style="width:100%; height:130px; object-fit:cover; border-radius:8px; margin-bottom:12px;">
        <div style="font-size:17px; font-weight:800; margin-bottom:2px;">Хаб ChargeUA «Київ-Поділ»</div>
        <div style="font-size:11px; color:#64748B; margin-bottom:10px;">м. Київ, вул. Петра Сагайдачного, 12</div>
        <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:12px; font-size:11.5px; margin-bottom:14px;">
          <div>• Потужність: <strong>120 кВт DC</strong> (2x CCS2, 1x Type 2)</div>
          <div>• Тариф: <strong>14.50 ₴/кВт·год</strong></div>
          <div style="color:#047857; font-weight:700; margin-top:2px;">• Резервне живлення: Дизель 160 кВт (100% Uptime)</div>
        </div>
        <button style="width:100%; height:40px; background:#005EC9; color:#FFF; border:none; border-radius:8px; font-weight:700; font-size:12.5px; margin-bottom:8px;">Забронювати конектор CCS2 на 20 хв</button>
        <button style="width:100%; height:34px; background:#FFF; border:1px solid #CBD5E1; color:#0F172A; border-radius:8px; font-weight:600; font-size:11.5px;">Прокласти маршрут у Waze</button>
      </div>
    </div>
  </div>
</body></html>"""

# =============================================================================
# 18. fig18_catalog_details_mobile (2 MOBILE PAGES SIDE BY SIDE - NO FIGMA AI!)
# =============================================================================
html_fig18 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F3F4F6; padding: 25px; width: 750px; }}
  .cols {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
  .mob-page {{ background: #FFF; border: 1.5px solid #CBD5E1; border-radius: 12px; overflow: hidden; }}
  .m-head {{ height: 44px; padding: 0 14px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #E2E8F0; }}
  .m-body {{ padding: 14px; }}
</style></head><body>
  <div style="font-size:16px; font-weight:800; margin-bottom:14px; text-align:center;">Сторінки «Каталог» та «Деталі станції» (Mobile 390)</div>
  <div class="cols">
    <!-- Ліва сторінка: Каталог Mobile -->
    <div class="mob-page">
      <div class="m-head">
        <span style="font-weight:800; color:#005EC9; font-size:14px;">ChargeUA</span>
        <span style="font-size:14px;">☰</span>
      </div>
      <div class="m-body">
        <div style="font-size:14px; font-weight:800; margin-bottom:6px;">Каталог станцій</div>
        <div style="background:#F8FAFC; border:1px solid #CBD5E1; border-radius:6px; padding:6px 10px; font-size:10px; color:#64748B; margin-bottom:8px;">
          🔍 Пошук (Київ, Львів)...
        </div>
        <div style="border:1px solid #E2E8F0; border-radius:6px; padding:8px; margin-bottom:8px;">
          <div style="font-size:11px; font-weight:700;">Хаб «Київ-Поділ» · 120 кВт</div>
          <div style="font-size:9.5px; color:#047857; font-weight:700;">● Генератор ON · Слот CCS2 вільний</div>
        </div>
        <div style="border:1px solid #E2E8F0; border-radius:6px; padding:8px;">
          <div style="font-size:11px; font-weight:700;">Хаб «Арена Львів» · 160 кВт</div>
          <div style="font-size:9.5px; color:#047857; font-weight:700;">● Сонячний навіс + Дизель</div>
        </div>
      </div>
    </div>

    <!-- Права сторінка: Деталі станції Mobile -->
    <div class="mob-page">
      <div class="m-head">
        <span style="font-weight:800; color:#005EC9; font-size:14px;">ChargeUA</span>
        <span style="font-size:14px;">✕</span>
      </div>
      <div class="m-body">
        <img src="file:///{HUB_KYIV_URL}" style="width:100%; height:95px; object-fit:cover; border-radius:6px; margin-bottom:8px;">
        <div style="font-size:13px; font-weight:800;">Хаб «Київ-Поділ»</div>
        <div style="font-size:10px; color:#64748B; margin-bottom:8px;">вул. Петра Сагайдачного, 12</div>
        <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:6px; padding:8px; font-size:10px; margin-bottom:10px;">
          <div>120 кВт DC · 14.50 ₴/кВт·год</div>
          <div style="color:#047857; font-weight:700;">Дизель 160 кВт ON</div>
        </div>
        <button style="width:100%; height:34px; background:#005EC9; color:#FFF; border:none; border-radius:6px; font-size:11px; font-weight:700;">Забронювати CCS2</button>
      </div>
    </div>
  </div>
</body></html>"""

# =============================================================================
# 19. fig19_overlays (AUTHENTIC OVERLAYS: MOBILE DRAWER + DIMMED MODAL)
# =============================================================================
html_fig19 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F3F4F6; padding: 25px; width: 898px; display: flex; justify-content: center; gap: 30px; }}
  .drawer-card {{ background: #FFF; border: 1.5px solid #CBD5E1; border-radius: 14px; width: 340px; padding: 24px; box-shadow: 0 10px 25px rgba(0,0,0,0.08); }}
  .modal-container {{ position: relative; width: 440px; height: 350px; background: rgba(15,23,42,0.7); border-radius: 14px; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 25px rgba(0,0,0,0.15); }}
  .modal-card {{ background: #FFF; border-radius: 12px; width: 380px; padding: 24px; text-align: center; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.2); }}
</style></head><body>
  <!-- Мобільне меню оверлей -->
  <div class="drawer-card">
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #E2E8F0; padding-bottom:12px; margin-bottom:16px;">
      <div style="display:flex; align-items:center; gap:8px;">
        <img src="file:///{LOGO_URL}" style="height:24px;">
        <span style="font-weight:800; color:#005EC9; font-size:16px;">ChargeUA</span>
      </div>
      <span style="font-size:18px; font-weight:700; color:#64748B;">✕</span>
    </div>
    <div style="display:flex; flex-direction:column; gap:14px; font-size:14px; font-weight:600; color:#1E293B; margin-bottom:24px;">
      <div style="color:#005EC9;">Головна</div>
      <div>Калькулятор зарядки</div>
      <div>Карта станцій</div>
      <div>Тарифи операторів</div>
      <div>Для бізнесу (B2B)</div>
      <div>FAQ & Підтримка</div>
    </div>
    <button style="width:100%; height:42px; background:#005EC9; color:#FFF; border:none; border-radius:8px; font-weight:700; font-size:13px;">Закрити меню</button>
  </div>

  <!-- Модальне вікно підтвердження на затемненому фоні -->
  <div class="modal-container">
    <div class="modal-card">
      <div style="background:#D1FAE5; color:#047857; display:inline-block; padding:4px 12px; border-radius:999px; font-size:11px; font-weight:700; margin-bottom:12px;">
        ● Бронювання підтверджено
      </div>
      <h3 style="font-size:18px; font-weight:800; color:#0F172A; margin-bottom:8px;">Дякуємо! Слот CCS2 заброньовано</h3>
      <p style="font-size:12px; color:#64748B; line-height:1.5; margin-bottom:18px;">
        Вам надіслано SMS із кодом доступу до станції «Київ-Поділ». Час резерву: <strong>20 хвилин</strong>.
      </p>
      <button style="width:100%; height:40px; background:#0F172A; color:#FFF; border:none; border-radius:8px; font-weight:700; font-size:12.5px;">Зрозуміло, відкрити маршрут</button>
    </div>
  </div>
</body></html>"""

# =============================================================================
# 20. fig20_buttons_matrix (36 VARIANTS: 3 TYPES X 6 STATES X 2 SIZES)
# =============================================================================
html_fig20 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F8FAFC; padding: 25px; width: 1600px; }}
  .b-table {{ width: 100%; border-collapse: collapse; background: #FFF; border-radius: 12px; overflow: hidden; border: 1.5px solid #E2E8F0; }}
  .b-table th, .b-table td {{ padding: 10px 14px; text-align: center; border: 1px solid #E2E8F0; font-size: 11.5px; }}
  .b-table th {{ background: #F1F5F9; font-weight: 700; color: #475569; }}
  .btn {{ border-radius: 6px; font-weight: 700; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; }}
  .btn-lg {{ height: 44px; padding: 0 18px; font-size: 13px; }}
  .btn-sm {{ height: 34px; padding: 0 14px; font-size: 11px; }}
  .p-def {{ background: #005EC9; color: #FFF; border: none; }}
  .p-hov {{ background: #004BB5; color: #FFF; border: none; }}
  .p-act {{ background: #003A8F; color: #FFF; border: none; }}
  .p-foc {{ background: #005EC9; color: #FFF; border: 2px solid #00E5FF; }}
  .p-dis {{ background: #CBD5E1; color: #64748B; border: none; }}
  .c-def {{ background: #00E5FF; color: #0F172A; border: none; }}
  .c-hov {{ background: #00B8D4; color: #0F172A; border: none; }}
  .c-act {{ background: #0097A7; color: #FFF; border: none; }}
  .c-foc {{ background: #00E5FF; color: #0F172A; border: 2px solid #005EC9; }}
  .c-dis {{ background: #CBD5E1; color: #64748B; border: none; }}
  .s-def {{ background: #FFF; color: #0F172A; border: 1.5px solid #CBD5E1; }}
  .s-hov {{ background: #F1F5F9; color: #0F172A; border: 1.5px solid #94A3B8; }}
  .s-act {{ background: #E2E8F0; color: #0F172A; border: 1.5px solid #64748B; }}
  .s-foc {{ background: #FFF; color: #0F172A; border: 2px solid #005EC9; }}
  .s-dis {{ background: #F8FAFC; color: #94A3B8; border: 1.5px solid #E2E8F0; }}
</style></head><body>
  <div style="font-size:22px; font-weight:800; margin-bottom:14px;">Компонент Button: 3 типи × 6 станів × 2 розміри (36 варіантів у системі)</div>
  <table class="b-table">
    <tr><th>Тип / Розмір</th><th>Default</th><th>Hover</th><th>Active</th><th>Focus</th><th>Disabled</th><th>Loading</th></tr>
    <tr><td><strong>Primary Large (44px)</strong></td><td><div class="btn btn-lg p-def">Кнопка</div></td><td><div class="btn btn-lg p-hov">Кнопка</div></td><td><div class="btn btn-lg p-act">Кнопка</div></td><td><div class="btn btn-lg p-foc">Кнопка</div></td><td><div class="btn btn-lg p-dis">Кнопка</div></td><td><div class="btn btn-lg p-def">⌛ Завантаження</div></td></tr>
    <tr><td><strong>Primary Small (34px)</strong></td><td><div class="btn btn-sm p-def">Кнопка</div></td><td><div class="btn btn-sm p-hov">Кнопка</div></td><td><div class="btn btn-sm p-act">Кнопка</div></td><td><div class="btn btn-sm p-foc">Кнопка</div></td><td><div class="btn btn-sm p-dis">Кнопка</div></td><td><div class="btn btn-sm p-def">⌛ ...</div></td></tr>
    <tr><td><strong>Accent CTA Large (44px)</strong></td><td><div class="btn btn-lg c-def">Кнопка</div></td><td><div class="btn btn-lg c-hov">Кнопка</div></td><td><div class="btn btn-lg c-act">Кнопка</div></td><td><div class="btn btn-lg c-foc">Кнопка</div></td><td><div class="btn btn-lg c-dis">Кнопка</div></td><td><div class="btn btn-lg c-def">⌛ Завантаження</div></td></tr>
    <tr><td><strong>Accent CTA Small (34px)</strong></td><td><div class="btn btn-sm c-def">Кнопка</div></td><td><div class="btn btn-sm c-hov">Кнопка</div></td><td><div class="btn btn-sm c-act">Кнопка</div></td><td><div class="btn btn-sm c-foc">Кнопка</div></td><td><div class="btn btn-sm c-dis">Кнопка</div></td><td><div class="btn btn-sm c-def">⌛ ...</div></td></tr>
    <tr><td><strong>Secondary Large (44px)</strong></td><td><div class="btn btn-lg s-def">Кнопка</div></td><td><div class="btn btn-lg s-hov">Кнопка</div></td><td><div class="btn btn-lg s-act">Кнопка</div></td><td><div class="btn btn-lg s-foc">Кнопка</div></td><td><div class="btn btn-lg s-dis">Кнопка</div></td><td><div class="btn btn-lg s-def">⌛ Завантаження</div></td></tr>
    <tr><td><strong>Secondary Small (34px)</strong></td><td><div class="btn btn-sm s-def">Кнопка</div></td><td><div class="btn btn-sm s-hov">Кнопка</div></td><td><div class="btn btn-sm s-act">Кнопка</div></td><td><div class="btn btn-sm s-foc">Кнопка</div></td><td><div class="btn btn-sm s-dis">Кнопка</div></td><td><div class="btn btn-sm s-def">⌛ ...</div></td></tr>
  </table>
</body></html>"""

# =============================================================================
# 21. fig21_inputs_controls
# =============================================================================
html_fig21 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F8FAFC; padding: 25px; width: 1249px; }}
  .grid {{ display: grid; grid-template-columns: 1.2fr 1fr; gap: 24px; margin-top: 16px; }}
  .card {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 20px; }}
  .inp {{ width: 100%; height: 44px; border-radius: 8px; border: 1.5px solid #CBD5E1; padding: 0 14px; font-size: 13px; margin-bottom: 12px; display: flex; align-items: center; }}
</style></head><body>
  <div style="font-size:22px; font-weight:800;">Поля вводу та елементи керування (Inputs, Chips, Checkboxes, Switches)</div>
  <div class="grid">
    <div class="card">
      <div style="font-size:14px; font-weight:700; margin-bottom:12px;">Стани полів введення (TextField):</div>
      <div class="inp" style="color:#64748B;">Default: Введіть ім'я...</div>
      <div class="inp" style="border-color:#005EC9; box-shadow:0 0 0 3px rgba(0,94,201,0.15); color:#0F172A; font-weight:600;">Focus: Андрій Лемішка|</div>
      <div class="inp" style="border-color:#EF4444; background:#FEF2F2; color:#DC2626;">Error: Некоректний номер телефону!</div>
      <div class="inp" style="background:#F1F5F9; color:#94A3B8; border-color:#E2E8F0;">Disabled: Поле заблоковане</div>
    </div>
    <div class="card">
      <div style="font-size:14px; font-weight:700; margin-bottom:12px;">Чіпи, чекбокси та перемикачі:</div>
      <div style="display:flex; gap:8px; margin-bottom:16px;">
        <span style="background:#005EC9; color:#FFF; padding:6px 14px; border-radius:999px; font-size:12px; font-weight:700;">Type 2 (Активний)</span>
        <span style="background:#F1F5F9; border:1px solid #CBD5E1; padding:6px 14px; border-radius:999px; font-size:12px;">CCS 2</span>
        <span style="background:#D1FAE5; color:#047857; padding:6px 14px; border-radius:999px; font-size:12px; font-weight:700;">🔋 З генератором</span>
      </div>
      <div style="display:flex; flex-direction:column; gap:10px; font-size:13px; color:#334155;">
        <div><input type="checkbox" checked> Погоджуюсь з умовами публічної оферти (Зона 48px)</div>
        <div><input type="radio" checked> Швидка зарядка DC (120 кВт)</div>
        <div><input type="checkbox" checked role="switch"> Увімкнути сповіщення про завершення сесії</div>
      </div>
    </div>
  </div>
</body></html>"""

# =============================================================================
# 22. fig22_cards_nav
# =============================================================================
html_fig22 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F8FAFC; padding: 25px; width: 1083px; }}
  .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 16px; }}
  .box {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 12px; overflow: hidden; }}
</style></head><body>
  <div style="font-size:22px; font-weight:800;">Основні компоненти-організми: Картка станції, Шапка, Підвал, Навігація</div>
  <div class="grid">
    <div class="box">
      <img src="file:///{HUB_KYIV_URL}" style="width:100%; height:160px; object-fit:cover;">
      <div style="padding:16px;">
        <div style="font-size:15px; font-weight:700;">Хаб «Київ-Поділ» · 120 кВт CCS2</div>
        <div style="font-size:12px; color:#64748B; margin-bottom:8px;">вул. Петра Сагайдачного, 12</div>
        <div style="background:#D1FAE5; color:#047857; display:inline-block; padding:3px 8px; border-radius:4px; font-size:11px; font-weight:700; margin-bottom:12px;">🔋 Генератор ON · 3/4 порти вільні</div>
        <button style="width:100%; height:38px; background:#005EC9; color:#FFF; border:none; border-radius:6px; font-weight:700; font-size:12px;">Забронювати конектор CCS2</button>
      </div>
    </div>
    <div class="box" style="padding:18px; display:flex; flex-direction:column; justify-content:space-between;">
      <div>
        <div style="font-size:14px; font-weight:700; margin-bottom:10px;">Header Desktop & Mobile:</div>
        <div style="border:1px solid #E2E8F0; border-radius:8px; padding:10px 14px; display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
          <div style="display:flex; align-items:center; gap:6px;"><img src="file:///{LOGO_URL}" style="height:20px;"><strong style="color:#005EC9; font-size:13px;">ChargeUA</strong></div>
          <div style="font-size:10px; color:#64748B;">Головна | Карта | Кальк | B2B</div>
          <button style="background:#005EC9; color:#FFF; border:none; padding:4px 8px; border-radius:4px; font-size:10px; font-weight:700;">Вхід</button>
        </div>
        <div style="border:1px solid #E2E8F0; border-radius:8px; padding:8px 12px; display:flex; justify-content:space-between; align-items:center;">
          <span style="font-weight:800; color:#005EC9; font-size:12px;">ChargeUA (Mobile)</span>
          <span style="font-size:14px;">☰</span>
        </div>
      </div>
      <div style="background:#0F172A; color:#FFF; border-radius:8px; padding:14px; font-size:10.5px;">
        <strong>Footer Component:</strong> 4 колонки навігації, підтримка 0 800 300 400, соцмережі та копірайт.
      </div>
    </div>
  </div>
</body></html>"""

# Dictionary of all 22 figures
figures = [
    ("fig01_user_flows", html_fig01, 1188, 632),
    ("fig02_user_flow_2", html_fig02, 1404, 877),
    ("fig03_sitemap_relume", html_fig03, 900, 640),
    ("fig04_wireframes_relume", html_fig04, 1100, 660),
    ("fig05_wireframe_desktop", html_fig05, 520, 1100),
    ("fig06_wireframe_mobile", html_fig06, 400, 1100),
    ("fig07_brand_colors", html_fig07, 1291, 585),
    ("fig08_wireframe_fixes", html_fig08, 1382, 600),
    ("fig09_contrast_plugin", html_fig09, 800, 520),
    ("fig10_typography", html_fig10, 1166, 600),
    ("fig11_spacing_grid", html_fig11, 1166, 550),
    ("fig12_figma_ai_illustrations", html_fig12, 1600, 480),
    ("fig13_desktop_top", html_fig13, 1440, 1080),
    ("fig14_desktop_bottom", html_fig14, 1440, 1150),
    ("fig15_tablet", html_fig15, 1249, 780),
    ("fig16_mobile", html_fig16, 1632, 620),
    ("fig17_catalog_details_desktop", html_fig17, 1291, 620),
    ("fig18_catalog_details_mobile", html_fig18, 750, 480),
    ("fig19_overlays", html_fig19, 898, 420),
    ("fig20_buttons_matrix", html_fig20, 1600, 580),
    ("fig21_inputs_controls", html_fig21, 1249, 500),
    ("fig22_cards_nav", html_fig22, 1083, 560)
]

print("Starting generation of all 22 figures...")
for name, html, w, h in figures:
    render_figure(name, html, w, h, scale=1.5)

print("All 22 figures rendered successfully!")
