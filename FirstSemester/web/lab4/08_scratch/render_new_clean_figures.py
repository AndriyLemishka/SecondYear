# -*- coding: utf-8 -*-
"""
Render authentic, pixel-perfect figures for Lab 4:
  - fig13_desktop_top.png: Centered Video Hero (video_content.mp4 from LR3), Benefits Strip, Interactive Calculator with SLIDER (повзунок), Live Map with charging pins
  - fig14_desktop_bottom.png: Blackout Generator section, 3 Hub cards, 3 Steps (cable illustration, NO video box), Reviews, B2B form, Footer
  - fig15_tablet.png: Complete tall tablet page (768px) sliced into 3 equal columns flush side-by-side (matching ref_fig_15_Image61)
  - fig16_mobile.png: Complete tall mobile page (390px) matching user's media photo pixel-for-pixel, sliced into 4 equal columns flush side-by-side (matching ref_fig_16_Image64)
"""

import os, sys, subprocess
from PIL import Image

BASE_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4"
MAT_DIR = os.path.join(BASE_DIR, "materials")
SCR_DIR = os.path.join(BASE_DIR, "screenshots")
HTML_DIR = os.path.join(BASE_DIR, "08_scratch", "html_boards")
os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(SCR_DIR, exist_ok=True)

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def p2u(fname):
    return os.path.join(MAT_DIR, fname).replace(os.sep, "/")

LOGO_URL = p2u("Logo.svg")
CALC_URL = p2u("Calculator.svg")
LOC_URL = p2u("Location.svg")
INFO_URL = p2u("Information.svg")

VIDEO_FRAME_URL = p2u("video_frame_30.jpg")
GIF_LOOP_URL = p2u("hero_loop_opt.gif")
HERO_URL = p2u("hero_bg.jpg")
HUB_KYIV_URL = p2u("ai_hub_kyiv.jpg")
HUB_LVIV_URL = p2u("ai_hub_lviv.jpg")
GEN_URL = p2u("ai_generator_blackout.jpg")
CABLE_URL = p2u("ai_step_cable.jpg")
AV1_URL = p2u("ai_avatar_oleksiy.jpg")
AV2_URL = p2u("ai_avatar_olena.jpg")
AV3_URL = p2u("ai_avatar_sergiy.jpg")
MAP_LVIV_URL = p2u("map_lviv.jpg")

COMMON_HEAD = """
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }
  body { background: #FFFFFF; color: #0F172A; -webkit-font-smoothing: antialiased; }
</style>
"""

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
    print(f"Rendered: {os.path.basename(out_png)}")

# ==============================================================================
# 1. FIG 13: DESKTOP TOP (CENTERED VIDEO HERO + SLIDER + LIVE MAP)
# ==============================================================================
html_fig13 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ width: 1440px; background: #FFFFFF; }}
  
  .top-bar {{ background: #0B132B; color: #FFF; padding: 10px 60px; font-size: 12px; font-weight: 500; display: flex; justify-content: space-between; align-items: center; }}
  .pulse-dot {{ display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #10B981; margin-right: 6px; }}

  .header {{ height: 76px; padding: 0 60px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #E2E8F0; background: #FFF; }}
  .logo-box {{ display: flex; align-items: center; gap: 10px; }}
  .nav-links {{ display: flex; gap: 28px; font-size: 14px; font-weight: 600; color: #334155; }}
  .nav-links a {{ text-decoration: none; color: inherit; }}
  .btn-header {{ background: #0077E6; color: #FFF; border: none; padding: 10px 22px; font-size: 13px; font-weight: 700; border-radius: 8px; cursor: pointer; }}

  /* HERO - FULLY CENTERED WITH VIDEO PLAYER */
  .hero-sec {{ padding: 48px 60px 40px; text-align: center; background: radial-gradient(circle at 50% 20%, #F0F7FF 0%, #FFFFFF 70%); }}
  .hero-tag {{ display: inline-flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 800; color: #0077E6; letter-spacing: 0.5px; margin-bottom: 14px; }}
  .hero-h1 {{ font-size: 44px; font-weight: 800; line-height: 1.18; color: #0F172A; letter-spacing: -0.8px; margin-bottom: 16px; max-width: 980px; margin-left: auto; margin-right: auto; }}
  .hero-sub {{ font-size: 16.5px; color: #64748B; line-height: 1.55; max-width: 760px; margin: 0 auto 26px; }}
  
  .hero-actions {{ display: flex; justify-content: center; gap: 16px; margin-bottom: 24px; }}
  .btn-primary {{ background: #0077E6; color: #FFF; border: none; padding: 14px 30px; font-size: 15px; font-weight: 700; border-radius: 8px; cursor: pointer; box-shadow: 0 4px 14px rgba(0,119,230,0.3); }}
  .btn-secondary {{ background: #FFFFFF; color: #0F172A; border: 1.5px solid #CBD5E1; padding: 14px 26px; font-size: 15px; font-weight: 700; border-radius: 8px; cursor: pointer; }}

  .hero-chips {{ display: flex; justify-content: center; gap: 12px; margin-bottom: 34px; }}
  .chip {{ background: #F8FAFC; border: 1px solid #E2E8F0; padding: 7px 16px; border-radius: 20px; font-size: 12px; font-weight: 600; color: #334155; }}
  .chip-green {{ background: #ECFDF5; border-color: #A7F3D0; color: #059669; font-weight: 700; }}

  /* CENTERED VIDEO SHOWCASE */
  .hero-video-box {{ max-width: 1100px; margin: 0 auto; position: relative; border-radius: 20px; overflow: hidden; border: 1.5px solid #CBD5E1; box-shadow: 0 16px 40px rgba(0,119,230,0.12); background: #0B132B; }}
  .hero-video-img {{ width: 100%; height: 460px; object-fit: cover; display: block; }}
  .video-center-play {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 72px; height: 72px; border-radius: 50%; background: rgba(0, 119, 230, 0.92); display: flex; align-items: center; justify-content: center; box-shadow: 0 6px 24px rgba(0,119,230,0.5); border: 2px solid #FFF; cursor: pointer; }}
  .video-center-play svg {{ fill: #FFF; width: 28px; height: 28px; margin-left: 4px; }}
  .video-top-tag {{ position: absolute; top: 18px; left: 22px; background: rgba(11,19,43,0.85); backdrop-filter: blur(6px); color: #FFF; font-size: 12px; font-weight: 700; padding: 6px 14px; border-radius: 6px; display: flex; align-items: center; gap: 8px; }}
  .video-bar {{ position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(11,19,43,0.9), transparent); padding: 18px 24px 14px; display: flex; justify-content: space-between; align-items: center; color: #FFF; font-size: 12px; font-weight: 600; }}

  /* BENEFITS STRIP */
  .strip-sec {{ padding: 30px 60px; }}
  .strip-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }}
  .strip-card {{ background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 14px; padding: 22px 24px; display: flex; align-items: center; gap: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.03); }}
  .strip-icon {{ width: 48px; height: 48px; flex-shrink: 0; }}

  /* CALCULATOR SECTION */
  .calc-sec {{ padding: 20px 60px 30px; }}
  .calc-wrap {{ background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 20px; padding: 36px 44px; box-shadow: 0 4px 16px rgba(0,0,0,0.04); }}
  .calc-top-row {{ display: grid; grid-template-columns: 1.4fr 1fr; gap: 40px; align-items: center; }}
  .car-pills {{ display: flex; gap: 12px; margin: 18px 0 24px; }}
  .car-pill {{ background: #F8FAFC; border: 1.5px solid #E2E8F0; padding: 10px 18px; border-radius: 8px; font-size: 13px; font-weight: 600; color: #334155; cursor: pointer; }}
  .car-pill.active {{ background: #0077E6; border-color: #0077E6; color: #FFF; }}

  /* SLIDER CONTROL */
  .slider-box {{ background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 18px 22px; margin-bottom: 8px; }}
  .slider-header {{ display: flex; justify-content: space-between; font-size: 13px; font-weight: 700; color: #0F172A; margin-bottom: 12px; }}
  .slider-rail {{ position: relative; height: 10px; background: #E2E8F0; border-radius: 5px; margin: 20px 0 10px; }}
  .slider-fill {{ position: absolute; left: 20%; width: 60%; height: 100%; background: #0077E6; border-radius: 5px; }}
  .slider-knob {{ position: absolute; left: 80%; top: 50%; transform: translate(-50%, -50%); width: 26px; height: 26px; border-radius: 50%; background: #FFF; border: 3.5px solid #0077E6; box-shadow: 0 3px 10px rgba(0,119,230,0.4); cursor: pointer; }}
  .slider-badge {{ position: absolute; top: -28px; left: 80%; transform: translateX(-50%); background: #0077E6; color: #FFF; font-size: 11px; font-weight: 800; padding: 3px 8px; border-radius: 5px; white-space: nowrap; }}
  .slider-ticks {{ display: flex; justify-content: space-between; font-size: 11px; color: #64748B; font-weight: 600; }}

  .calc-res-card {{ background: #F0F7FF; border: 1.5px solid #BFDBFE; border-radius: 16px; padding: 26px 30px; }}
  .res-price {{ font-size: 34px; font-weight: 800; color: #0077E6; margin-bottom: 4px; }}
  .res-meta {{ font-size: 13px; color: #475569; margin-bottom: 16px; }}

  /* LIVE MAP SECTION */
  .map-sec {{ padding: 20px 60px 40px; }}
  .map-card {{ border: 1.5px solid #CBD5E1; border-radius: 20px; overflow: hidden; background: #FFFFFF; box-shadow: 0 6px 20px rgba(0,0,0,0.04); }}
  .map-top {{ padding: 20px 28px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #E2E8F0; background: #FAFAFA; }}
  .map-canvas-desktop {{ height: 380px; position: relative; background: url('{MAP_LVIV_URL}') center/cover no-repeat; }}
  .map-artery {{ display: none; }}
  .map-artery-h1 {{ top: 90px; left: 0; right: 0; height: 4px; }}
  .map-artery-h2 {{ top: 250px; left: 0; right: 0; height: 4px; }}
  .map-artery-v1 {{ top: 0; bottom: 0; left: 340px; width: 4px; }}
  .map-artery-v2 {{ top: 0; bottom: 0; left: 680px; width: 4px; }}
  .map-artery-v3 {{ top: 0; bottom: 0; left: 1020px; width: 4px; }}

  .d-pin {{ position: absolute; transform: translate(-50%, -50%); display: flex; flex-direction: column; align-items: center; cursor: pointer; }}
  .d-dot {{ width: 16px; height: 16px; border-radius: 50%; background: #10B981; border: 3px solid #FFF; box-shadow: 0 0 0 3px #10B981, 0 4px 8px rgba(0,0,0,0.2); }}
  .d-dot.blue {{ background: #0077E6; box-shadow: 0 0 0 3px #0077E6, 0 4px 8px rgba(0,0,0,0.2); }}
  .d-dot.warn {{ background: #F59E0B; box-shadow: 0 0 0 3px #F59E0B, 0 4px 8px rgba(0,0,0,0.2); }}
  .d-tag {{ background: #0B132B; color: #FFF; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 5px; margin-top: 6px; box-shadow: 0 3px 8px rgba(0,0,0,0.25); white-space: nowrap; }}
</style></head><body>
  <!-- TOP BAR -->
  <div class="top-bar">
    <div><span class="pulse-dot"></span>Мережа ChargeUA: 480+ станцій онлайн по Україні | 100% телеметрія в реальному часі</div>
    <div>Гаряча лінія 24/7: 0 800 300 400 | UA</div>
  </div>

  <!-- HEADER -->
  <header class="header">
    <div class="logo-box">
      <img src="{LOGO_URL}" style="width:34px; height:34px;">
      <span style="font-size:22px; font-weight:800; color:#0077E6;">ChargeUA</span>
    </div>
    <div class="nav-links">
      <a href="#">Головна</a>
      <a href="#">Калькулятор</a>
      <a href="#">Карта станцій</a>
      <a href="#">Популярні хаби</a>
      <a href="#">Інструкція</a>
      <a href="#">Відгуки</a>
    </div>
    <div>
      <button class="btn-header">Знайти станцію</button>
    </div>
  </header>

  <!-- CENTERED VIDEO HERO -->
  <section class="hero-sec">
    <div class="hero-tag">⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР ЗАРЯДНИХ СТАНЦІЙ</div>
    <h1 class="hero-h1">Швидка та надійна зарядка електромобілів по всій Україні</h1>
    <p class="hero-sub">Знаходьте найближчі станції, розраховуйте вартість за лічені секунди та подорожуйте без хвилювань навіть під час блекаутів.</p>
    
    <div class="hero-actions">
      <button class="btn-primary">Розрахувати зарядку →</button>
      <button class="btn-secondary">Знайти на карті</button>
    </div>

    <div class="hero-chips">
      <div class="chip">Type 2 (22 кВт)</div>
      <div class="chip">CCS 2 (160 кВт)</div>
      <div class="chip">CHAdeMO</div>
      <div class="chip chip-green">🔋 З генератором</div>
    </div>

    <!-- Centered Video Showcase from Lab 3 -->
    <div class="hero-video-box">
      <img src="{VIDEO_FRAME_URL}" class="hero-video-img" alt="ChargeUA Video Presentation">
      <div class="video-center-play">
        <svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
      </div>
      <div class="video-top-tag">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00E5FF;"></span>
        Відеопрезентація ChargeUA 4K · 100% автономність мережі (video_content.mp4)
      </div>
      <div class="video-bar">
        <div>▶ 0:45 / 1:30 · Презентація швидкої зарядної станції 160 кВт з буферним живленням</div>
        <div>1080p 60fps · 480+ станцій онлайн</div>
      </div>
    </div>
  </section>

  <!-- BENEFITS STRIP -->
  <section class="strip-sec">
    <div class="strip-grid">
      <div class="strip-card">
        <img src="{CALC_URL}" class="strip-icon">
        <div>
          <div style="font-size:16px; font-weight:800; color:#0F172A; margin-bottom:3px;">Точний калькулятор витрат</div>
          <div style="font-size:13px; color:#64748B;">Автоматичний підбір моделі авто та тарифу</div>
        </div>
      </div>
      <div class="strip-card">
        <img src="{LOC_URL}" class="strip-icon">
        <div>
          <div style="font-size:16px; font-weight:800; color:#0F172A; margin-bottom:3px;">Live-карта 480+ станцій</div>
          <div style="font-size:13px; color:#64748B;">Актуальний статус зайнятості та світла онлайн</div>
        </div>
      </div>
      <div class="strip-card">
        <img src="{INFO_URL}" class="strip-icon">
        <div>
          <div style="font-size:16px; font-weight:800; color:#0F172A; margin-bottom:3px;">100% Енергонезалежність</div>
          <div style="font-size:13px; color:#64748B;">Робота від потужних генераторів у блекаути</div>
        </div>
      </div>
    </div>
  </section>

  <!-- CALCULATOR SECTION WITH SLIDER -->
  <section class="calc-sec">
    <div class="calc-wrap">
      <h2 style="font-size:26px; font-weight:800; color:#0F172A; margin-bottom:6px;">Інтерактивний калькулятор зарядки ChargeUA</h2>
      <p style="font-size:14px; color:#64748B; margin-bottom:20px;">Оберіть модель електрокара та регулюйте рівень заряду за допомогою повзунка:</p>
      
      <div class="calc-top-row">
        <div>
          <div style="font-size:13px; font-weight:700; color:#0F172A; margin-bottom:8px;">Модель автомобіля:</div>
          <div class="car-pills">
            <div class="car-pill active">Volkswagen ID.4 (77 кВт·год)</div>
            <div class="car-pill">Tesla Model 3</div>
            <div class="car-pill">Nissan Leaf</div>
            <div class="car-pill">Hyundai Ioniq 5</div>
          </div>

          <!-- SLIDER CONTROL (ПОВЗУНОК) -->
          <div class="slider-box">
            <div class="slider-header">
              <span>Регулювання рівня батареї (Повзунок %):</span>
              <span style="color:#0077E6;">20% → 80% (Додано +46.2 кВт·год)</span>
            </div>
            <div class="slider-rail">
              <div class="slider-fill"></div>
              <div class="slider-knob"></div>
              <div class="slider-badge">80% (Цільовий)</div>
            </div>
            <div class="slider-ticks">
              <span>0% (Розряджена)</span>
              <span>20% (Старт)</span>
              <span>50%</span>
              <span style="color:#0077E6; font-weight:700;">80% (Рекомендовано DC)</span>
              <span>100% (Повна)</span>
            </div>
          </div>
        </div>

        <div class="calc-res-card">
          <div style="font-size:13px; font-weight:700; color:#475569; text-transform:uppercase; margin-bottom:8px;">Орієнтовна вартість сесії:</div>
          <div class="res-price">652.50 ₴</div>
          <div class="res-meta">Тариф: 14.12 ₴/кВт·год · 46.2 кВт·год енергії</div>
          <div style="font-size:13px; color:#0F172A; font-weight:600; margin-bottom:18px;">
            ● Час на DC 120 кВт: <b>~28 хвилин</b> | Економія vs бензин: <b>~1 420 ₴</b>
          </div>
          <button class="btn-primary" style="width:100%;">Знайти найближчу вільну станцію</button>
        </div>
      </div>
    </div>
  </section>

  <!-- LIVE MAP SECTION WITH FULL SETTINGS & FILTER CONTROLS -->
  <section class="map-sec">
    <div class="map-card" style="padding: 24px 28px;">
      <div class="map-top" style="padding:0; background:transparent; border-bottom:none;">
        <div>
          <h3 style="font-size:22px; font-weight:800; color:#0F172A;">Live-карта зарядної мережі України</h3>
          <p style="font-size:13.5px; color:#64748B; margin-top:3px;">Фільтруйте за типами конекторів, статусом вільних портів та наявністю автономного генератора</p>
        </div>
      </div>

      <!-- MAP CONTROLS & FILTER SETTINGS BAR (Налаштування карти) -->
      <div style="display:flex; align-items:center; gap:12px; background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; padding:10px 16px; margin:16px 0;">
        <div style="display:flex; align-items:center; gap:8px; background:#FFFFFF; border:1.5px solid #005EC9; border-radius:8px; padding:8px 14px; width:340px;">
          <span style="color:#005EC9; font-size:14px;">🔍</span>
          <span style="font-size:12.5px; font-weight:500; color:#0F172A;">м. Львів, вул. Стрийська, 199</span>
        </div>
        <div style="display:flex; gap:8px; align-items:center;">
          <button class="chip active" style="background:#005EC9; color:#FFF; border:none; padding:8px 14px; border-radius:8px; font-weight:700; font-size:12px; cursor:pointer;">⚡ Всі (480+)</button>
          <button class="chip" style="background:#FFFFFF; border:1px solid #CBD5E1; padding:8px 14px; border-radius:8px; font-weight:600; font-size:12px; color:#0F172A; cursor:pointer;">CCS 2 (160 кВт)</button>
          <button class="chip" style="background:#FFFFFF; border:1px solid #CBD5E1; padding:8px 14px; border-radius:8px; font-weight:600; font-size:12px; color:#0F172A; cursor:pointer;">Type 2 (22 кВт)</button>
          <button class="chip chip-green" style="background:#ECFDF5; border:1.5px solid #047857; color:#047857; padding:8px 14px; border-radius:8px; font-weight:700; font-size:12px; cursor:pointer;">🔋 З генератором [ON]</button>
        </div>
        <div style="display:flex; align-items:center; gap:8px; margin-left:auto; background:#FFFFFF; border:1px solid #CBD5E1; border-radius:8px; padding:8px 14px;">
          <span style="width:18px; height:18px; background:#005EC9; color:#FFF; border-radius:4px; display:inline-flex; align-items:center; justify-content:center; font-size:11px; font-weight:bold;">✓</span>
          <span style="font-size:12px; font-weight:600; color:#0F172A;">Тільки вільні (48px)</span>
        </div>
      </div>

      <div class="map-canvas-desktop">
        <div class="map-artery map-artery-h1"></div>
        <div class="map-artery map-artery-h2"></div>
        <div class="map-artery map-artery-v1"></div>
        <div class="map-artery map-artery-v2"></div>
        <div class="map-artery map-artery-v3"></div>

        <!-- Pins on Lviv Map -->
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
        </div>
      </div>
    </div>
  </section>
</body></html>
"""

# ==============================================================================
# 2. FIG 14: DESKTOP BOTTOM (GENERATOR, HUBS, STEPS, REVIEWS, B2B, FOOTER)
# ==============================================================================
html_fig14 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ width: 1440px; background: #FFFFFF; }}
  
  .sec-gen {{ padding: 30px 60px; }}
  .banner-box {{ background: #0B132B; border-radius: 20px; padding: 40px 50px; display: grid; grid-template-columns: 1.1fr 1fr; gap: 40px; align-items: center; color: #FFF; }}
  .gen-h2 {{ font-size: 32px; font-weight: 800; line-height: 1.25; margin-bottom: 14px; }}
  .gen-p {{ font-size: 15px; line-height: 1.6; color: #CBD5E1; margin-bottom: 24px; }}
  .btn-gen {{ background: #00E5FF; color: #0F172A; border: none; padding: 13px 26px; border-radius: 8px; font-size: 14px; font-weight: 800; cursor: pointer; }}

  .hubs-sec {{ padding: 20px 60px 30px; }}
  .hubs-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 20px; }}
  .hub-card {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 16px; overflow: hidden; }}
  .hub-img {{ width: 100%; height: 180px; object-fit: cover; }}
  .hub-content {{ padding: 18px 20px; }}
  .hub-tag {{ display: inline-flex; align-items: center; gap: 4px; padding: 4px 9px; border-radius: 6px; font-size: 11px; font-weight: 700; background: #DCFCE7; color: #15803D; margin-bottom: 14px; }}
  .btn-route {{ display: block; width: 100%; background: #0077E6; color: #FFF; border: none; padding: 12px 0; font-size: 13px; font-weight: 700; border-radius: 8px; text-align: center; cursor: pointer; }}

  .steps-sec {{ padding: 20px 60px 30px; }}
  .steps-box {{ background: #F8FAFC; border: 1.5px solid #E2E8F0; border-radius: 20px; padding: 36px 44px; }}
  .steps-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 24px; }}
  .step-card {{ background: #FFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 24px; }}
  .step-num {{ width: 36px; height: 36px; border-radius: 50%; background: #0077E6; color: #FFF; font-size: 16px; font-weight: 800; display: flex; align-items: center; justify-content: center; margin-bottom: 14px; }}

  .rev-sec {{ padding: 20px 60px 30px; }}
  .rev-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 20px; }}
  .rev-card {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 14px; padding: 24px; }}
  .rev-author {{ display: flex; align-items: center; gap: 12px; margin-top: 16px; }}
  .rev-av {{ width: 42px; height: 42px; border-radius: 50%; object-fit: cover; }}

  .form-sec {{ padding: 20px 60px 40px; }}
  .form-box {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 20px; padding: 36px 44px; text-align: center; max-width: 1000px; margin: 0 auto; }}
  .form-row {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin: 24px 0 20px; }}
  .form-input {{ height: 46px; border: 1.5px solid #CBD5E1; border-radius: 8px; padding: 0 16px; font-size: 13px; outline: none; }}

  .footer {{ background: #0B132B; color: #FFF; padding: 50px 60px 30px; }}
  .footer-grid {{ display: grid; grid-template-columns: 2fr 1fr 1fr 1.2fr; gap: 40px; margin-bottom: 40px; }}
  .f-col-title {{ font-size: 14px; font-weight: 700; color: #FFF; margin-bottom: 14px; }}
  .f-col-links {{ display: flex; flex-direction: column; gap: 10px; font-size: 13px; color: #94A3B8; }}
  .f-bottom {{ border-top: 1px solid #1E293B; padding-top: 24px; display: flex; justify-content: space-between; font-size: 12px; color: #64748B; }}
</style></head><body>
  <!-- GENERATOR BLACKOUT -->
  <div class="sec-gen">
    <div class="banner-box">
      <div>
        <div style="font-size:12px; font-weight:800; color:#10B981; letter-spacing:0.5px; margin-bottom:8px;">⚡ ЕНЕРГОНЕЗАЛЕЖНІСТЬ 24/7</div>
        <div class="gen-h2">Заряджайте авто навіть під час повних блекаутів</div>
        <div class="gen-p">Ключові хаби ChargeUA обладнано промисловими дизель-генераторами 160–250 кВт. Автоматичний перехід на резервне живлення за 8 секунд гарантує 100% Uptime зарядної мережі.</div>
        <button class="btn-gen">Показати станції зі світлом</button>
      </div>
      <div>
        <img src="{GEN_URL}" style="width:100%; height:260px; object-fit:cover; border-radius:14px; border:1px solid rgba(255,255,255,0.2);">
      </div>
    </div>
  </div>

  <!-- POPULAR HUBS -->
  <div class="hubs-sec">
    <div style="font-size:26px; font-weight:800; color:#0F172A;">Популярні зарядні хаби мережі</div>
    <div style="font-size:14px; color:#64748B; margin-top:4px;">Швидкісні станції з гарантованим живленням та живою телеметрією</div>
    <div class="hubs-grid">
      <div class="hub-card">
        <img src="{HUB_KYIV_URL}" class="hub-img">
        <div class="hub-content">
          <div style="font-size:16px; font-weight:800; color:#0F172A;">Хаб «Київ-Поділ» · 120 кВт CCS2</div>
          <div style="font-size:13px; color:#64748B; margin:4px 0 10px;">м. Київ, вул. Сагайдачного, 12</div>
          <div class="hub-tag">🔋 Генератор ON · Вільний (3/4)</div>
          <button class="btn-route">Прокласти маршрут (Waze / Maps)</button>
        </div>
      </div>
      <div class="hub-card">
        <img src="{HUB_LVIV_URL}" class="hub-img">
        <div class="hub-content">
          <div style="font-size:16px; font-weight:800; color:#0F172A;">Хаб «Арена Львів» · 160 кВт CCS2</div>
          <div style="font-size:13px; color:#64748B; margin:4px 0 10px;">м. Львів, вул. Стрийська, 199</div>
          <div class="hub-tag">🔋 Сонячний навіс + Дизель</div>
          <button class="btn-route">Прокласти маршрут (Waze / Maps)</button>
        </div>
      </div>
      <div class="hub-card">
        <img src="{HUB_KYIV_URL}" class="hub-img">
        <div class="hub-content">
          <div style="font-size:16px; font-weight:800; color:#0F172A;">Хаб «Київ-Оболонь» · 120 кВт CCS2</div>
          <div style="font-size:13px; color:#64748B; margin:4px 0 10px;">просп. Оболонський, 1-Б · 4 порти</div>
          <div class="hub-tag">⚡ Мережа онлайн · Вільний (2/4)</div>
          <button class="btn-route">Прокласти маршрут (Waze / Maps)</button>
        </div>
      </div>
    </div>
  </div>

  <!-- HOW IT WORKS (3 STEPS - CLEAN, NO VIDEO) -->
  <div class="steps-sec">
    <div class="steps-box">
      <div style="font-size:12px; font-weight:800; color:#0077E6; margin-bottom:6px;">ПРОСТИЙ АЛГОРИТМ</div>
      <div style="font-size:24px; font-weight:800; color:#0F172A;">Як зарядитися за 3 кроки: від пошуку до повної батареї</div>
      <div style="font-size:14px; color:#64748B; margin-top:4px;">Зручний покроковий процес без складної реєстрації, передплат чи очікування в чергах.</div>
      <div class="steps-grid">
        <div class="step-card">
          <div class="step-num">1</div>
          <div style="font-size:15px; font-weight:800; color:#0F172A; margin-bottom:8px;">Знайдіть вільну станцію</div>
          <div style="font-size:13px; color:#64748B; line-height:1.5;">Фільтруйте за потужністю, роз'ємом або наявністю генератора на живій карті ChargeUA.</div>
        </div>
        <div class="step-card">
          <div class="step-num">2</div>
          <div style="font-size:15px; font-weight:800; color:#0F172A; margin-bottom:8px;">Підключіть конектор CCS2</div>
          <div style="font-size:13px; color:#64748B; line-height:1.5;">Вставте кабель у роз'єм електрокара — світловий смарт-індикатор спалахне зеленим.</div>
        </div>
        <div class="step-card">
          <div class="step-num">3</div>
          <div style="font-size:15px; font-weight:800; color:#0F172A; margin-bottom:8px;">Оплатіть у 1 клік</div>
          <div style="font-size:13px; color:#64748B; line-height:1.5;">Apple Pay, Google Pay або банківська картка. Жодних обов'язкових депозитів.</div>
        </div>
      </div>
    </div>
  </div>

  <!-- DRIVER REVIEWS -->
  <div class="rev-sec">
    <div style="font-size:24px; font-weight:800; color:#0F172A;">Відгуки реальних водіїв</div>
    <div style="font-size:14px; color:#64748B; margin-top:4px;">Що кажуть власники електрокарів про сервіс ChargeUA</div>
    <div class="rev-grid">
      <div class="rev-card">
        <div style="color:#F59E0B; font-size:14px; margin-bottom:10px;">★★★★★</div>
        <div style="font-size:13px; line-height:1.55; color:#334155;">«Під час блекауту на Подолі зарядився за 25 хвилин. Генератор гуде, станція стабільна, кава поруч. Найкращий сервіс!»</div>
        <div class="rev-author">
          <img src="{AV1_URL}" class="rev-av">
          <div><div style="font-size:13px; font-weight:700;">Олексій К.</div><div style="font-size:11px; color:#64748B;">Водій Tesla Model Y · Київ</div></div>
        </div>
      </div>
      <div class="rev-card">
        <div style="color:#F59E0B; font-size:14px; margin-bottom:10px;">★★★★★</div>
        <div style="font-size:13px; line-height:1.55; color:#334155;">«Дуже зручний калькулятор. Одразу видно скільки кіловат потрібно і яка буде фінальна вартість без прихованих платежів.»</div>
        <div class="rev-author">
          <img src="{AV2_URL}" class="rev-av">
          <div><div style="font-size:13px; font-weight:700;">Олена М.</div><div style="font-size:11px; color:#64748B;">Водійка Nissan Leaf · Львів</div></div>
        </div>
      </div>
      <div class="rev-card">
        <div style="color:#F59E0B; font-size:14px; margin-bottom:10px;">★★★★★</div>
        <div style="font-size:13px; line-height:1.55; color:#334155;">«Для комерційного автопарку зручний моніторинг вільних станцій — це знахідка. Жодних простоїв та черг на трасі Київ-Львів.»</div>
        <div class="rev-author">
          <img src="{AV3_URL}" class="rev-av">
          <div><div style="font-size:13px; font-weight:700;">Сергій В.</div><div style="font-size:11px; color:#64748B;">Керівник автопарку електробусів</div></div>
        </div>
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <div class="footer">
    <div class="footer-grid">
      <div>
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:14px;">
          <img src="{LOGO_URL}" style="width:32px; height:32px; filter:brightness(0) invert(1);">
          <span style="font-size:22px; font-weight:800; color:#FFF;">ChargeUA</span>
        </div>
        <p style="font-size:13px; line-height:1.6; color:#94A3B8;">Національний агрегатор та веб-помічник зарядної інфраструктури України.</p>
      </div>
      <div>
        <div class="f-col-title">Навігація</div>
        <div class="f-col-links">
          <span>Головна</span>
          <span>Калькулятор</span>
          <span>Карта станцій</span>
          <span>Як зарядитись</span>
        </div>
      </div>
      <div>
        <div class="f-col-title">Розділи сайту</div>
        <div class="f-col-links">
          <span>Популярні хаби</span>
          <span>Як зарядитися (3 кроки)</span>
          <span>Відгуки водіїв</span>
          <span>Гарантія Uptime 100%</span>
        </div>
      </div>
      <div>
        <div class="f-col-title">Контакти</div>
        <div class="f-col-links">
          <span>0 800 300 400</span>
          <span>support@charge.ua</span>
          <span>м. Київ, вул. Подолу, 12</span>
          <span>Telegram Бот</span>
        </div>
      </div>
    </div>
    <div class="f-bottom">
      <div>© 2026 ChargeUA · Лемішка Андрій, ПП-24 · Кафедра САПР, НУ «Львівська політехніка»</div>
      <div>Політика приватності · Умови використання</div>
    </div>
  </div>
</body></html>
"""

# ==============================================================================
# 3. FIG 15: TABLET (CONTINUOUS 768px PAGE SLICED INTO 3 COLUMNS FLUSH)
# ==============================================================================
html_tablet_full = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ width: 768px; background: #FFFFFF; color: #0F172A; }}
  
  .t-top {{ background: #0B132B; color: #FFF; padding: 8px 24px; font-size: 11px; display: flex; justify-content: space-between; }}
  .t-head {{ height: 64px; padding: 0 24px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #E2E8F0; background: #FFF; }}
  
  .t-hero {{ position: relative; overflow: hidden; min-height: 440px; padding: 36px 28px; background: #FFFFFF; display: flex; align-items: center; }}
  .t-hero-bg {{ position: absolute; right: 0; top: 0; width: 530px; height: 100%; object-fit: cover; z-index: 1; }}
  .t-hero-overlay {{ position: absolute; inset: 0; background: linear-gradient(to right, #FFFFFF 0%, rgba(255,255,255,0.95) 45%, rgba(255,255,255,0.25) 82%, rgba(255,255,255,0) 100%); z-index: 2; }}
  .t-hero-content {{ position: relative; z-index: 3; max-width: 440px; text-align: left; }}
  .t-hero-tag {{ font-size: 11px; font-weight: 800; color: #0077E6; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 10px; }}
  .t-hero-h1 {{ font-size: 28px; font-weight: 800; line-height: 1.2; color: #0F172A; margin-bottom: 12px; }}
  .t-hero-p {{ font-size: 13.5px; color: #64748B; margin-bottom: 20px; line-height: 1.5; }}
  .t-hero-btns {{ display: flex; gap: 10px; margin-bottom: 18px; }}
  .t-hero-chips {{ display: flex; gap: 8px; flex-wrap: wrap; }}
  .t-chip {{ font-size: 10.5px; font-weight: 700; padding: 4px 10px; border-radius: 14px; background: #FFF; border: 1px solid #CBD5E1; color: #0F172A; }}
  .t-chip.gen {{ background: #DCFCE7; border-color: #16A34A; color: #15803D; }}
  .t-live-badge {{ position: absolute; bottom: 16px; right: 20px; z-index: 3; background: rgba(15, 23, 42, 0.88); backdrop-filter: blur(4px); color: #FFF; font-size: 10px; font-weight: 700; padding: 5px 10px; border-radius: 6px; display: flex; align-items: center; gap: 6px; }}
  .t-live-dot {{ width: 6px; height: 6px; border-radius: 50%; background: #00E5FF; }}

  .t-strip {{ padding: 20px 24px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; background: #F8FAFC; border-top: 1px solid #E2E8F0; border-bottom: 1px solid #E2E8F0; }}
  .t-strip-card {{ background: #FFF; border: 1px solid #E2E8F0; border-radius: 10px; padding: 14px; display: flex; align-items: center; gap: 10px; }}
  
  .t-calc {{ padding: 32px 24px; }}
  .t-calc-box {{ border: 1.5px solid #CBD5E1; border-radius: 16px; padding: 24px; background: #FFF; }}
  
  .t-map {{ padding: 32px 24px; background: #F8FAFC; border-top: 1px solid #E2E8F0; }}
  .t-map-box {{ height: 260px; border-radius: 14px; border: 1px solid #CBD5E1; background: radial-gradient(#CBD5E1 1.5px, #F1F5F9 1.5px); background-size: 14px 14px; position: relative; }}

  .t-gen {{ padding: 36px 24px; background: #0B132B; color: #FFF; }}
  
  .t-hubs {{ padding: 36px 24px; }}
  .t-hubs-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-top: 16px; }}
  .t-hub-card {{ border: 1px solid #E2E8F0; border-radius: 12px; overflow: hidden; }}
  .t-hub-img {{ width: 100%; height: 160px; object-fit: cover; }}

  .t-steps {{ padding: 36px 24px; background: #F8FAFC; border-top: 1px solid #E2E8F0; }}
  .t-step-item {{ background: #FFF; border: 1px solid #E2E8F0; border-radius: 10px; padding: 16px; margin-bottom: 12px; }}

  .t-revs {{ padding: 36px 24px; }}
  .t-rev-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 14px; }}
  .t-rev-card {{ background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 16px; }}
  
  .t-foot {{ background: #0B132B; color: #94A3B8; padding: 32px 24px; border-top: 1px solid #1E293B; font-size: 12px; }}
</style></head><body>
  <div class="t-top">
    <div>● 480+ станцій онлайн | Генератори ON</div>
    <div>0 800 300 400</div>
  </div>

  <header class="t-head">
    <div style="display:flex; align-items:center; gap:8px;">
      <img src="{LOGO_URL}" style="width:28px; height:28px;">
      <span style="font-size:20px; font-weight:800; color:#0077E6;">ChargeUA</span>
    </div>
    <div style="font-size:13px; font-weight:600; color:#334155;">Головна · Калькулятор · Карта · Хаби · Відгуки</div>
    <button style="background:#0077E6; color:#FFF; border:none; padding:8px 18px; border-radius:6px; font-size:12px; font-weight:700;">Знайти</button>
  </header>

  <section class="t-hero">
    <img src="{GIF_LOOP_URL}" class="t-hero-bg">
    <div class="t-hero-overlay"></div>
    <div class="t-hero-content">
      <div class="t-hero-tag">⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР ЗАРЯДНИХ СТАНЦІЙ</div>
      <h1 class="t-hero-h1">Швидка та надійна зарядка електромобілів по всій Україні</h1>
      <p class="t-hero-p">Знаходьте найближчі станції, розраховуйте вартість за секунди та подорожуйте без хвилювань навіть під час блекаутів.</p>
      <div class="t-hero-btns">
        <button style="background:#0077E6; color:#FFF; border:none; padding:12px 22px; border-radius:8px; font-size:13px; font-weight:700; cursor:pointer;">Розрахувати зарядку →</button>
        <button style="background:#FFF; color:#0F172A; border:1px solid #CBD5E1; padding:12px 18px; border-radius:8px; font-size:13px; font-weight:600; cursor:pointer;">Знайти на карті</button>
      </div>
      <div class="t-hero-chips">
        <span class="t-chip">Type 2 (22 кВт)</span>
        <span class="t-chip">CCS 2 (160 кВт)</span>
        <span class="t-chip gen">🔋 З генератором</span>
      </div>
    </div>
  </section>

  <div class="t-strip">
    <div class="t-strip-card"><img src="{CALC_URL}" style="width:32px; height:32px;"><div><div style="font-weight:700; font-size:12px;">Калькулятор</div><div style="font-size:10px; color:#64748B;">Розрахунок за 3 сек</div></div></div>
    <div class="t-strip-card"><img src="{LOC_URL}" style="width:32px; height:32px;"><div><div style="font-weight:700; font-size:12px;">Live-карта</div><div style="font-size:10px; color:#64748B;">480+ станцій онлайн</div></div></div>
    <div class="t-strip-card"><img src="{INFO_URL}" style="width:32px; height:32px;"><div><div style="font-weight:700; font-size:12px;">Блекаут-захист</div><div style="font-size:10px; color:#64748B;">100% автономність</div></div></div>
  </div>

  <section class="t-calc">
    <div class="t-calc-box">
      <div style="font-size:18px; font-weight:800; margin-bottom:4px;">Калькулятор вартості зарядки</div>
      <div style="font-size:13px; color:#0077E6; font-weight:600; margin-bottom:14px;">Volkswagen ID.4 · 20% → 80%</div>
      
      <!-- SLIDER -->
      <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; padding:14px 18px; margin-bottom:16px;">
        <div style="display:flex; justify-content:space-between; font-size:12px; font-weight:700;"><span>Повзунок рівня заряду:</span><span style="color:#0077E6;">+46.2 кВт·год</span></div>
        <div style="position:relative; height:8px; background:#E2E8F0; border-radius:4px; margin:16px 0 8px;">
          <div style="position:absolute; left:20%; width:60%; height:100%; background:#0077E6; border-radius:4px;"></div>
          <div style="position:absolute; left:80%; top:50%; transform:translate(-50%, -50%); width:22px; height:22px; border-radius:50%; background:#FFF; border:3px solid #0077E6;"></div>
          <div style="position:absolute; top:-24px; left:80%; transform:translateX(-50%); background:#0077E6; color:#FFF; font-size:10px; font-weight:700; padding:2px 6px; border-radius:4px;">80%</div>
        </div>
      </div>

      <div style="background:#F0F7FF; border:1px solid #BFDBFE; border-radius:12px; padding:18px;">
        <div style="font-size:26px; font-weight:800; color:#0077E6;">652.50 ₴ (~28 хв)</div>
        <div style="font-size:12px; color:#475569; margin:4px 0 12px;">Тариф: 14.12 ₴/кВт·год · Економія: ~1 420 ₴ vs бензин</div>
        <button style="width:100%; background:#0077E6; color:#FFF; border:none; padding:11px 0; border-radius:6px; font-weight:700; font-size:13px;">Знайти вільну станцію</button>
      </div>
    </div>
  </section>

  <!-- LIVE MAP WITH CONTROLS -->
  <section class="t-map">
    <div style="font-size:18px; font-weight:800; color:#0F172A; margin-bottom:2px;">Live-карта зарядної мережі</div>
    <div style="font-size:12px; color:#64748B; margin-bottom:10px;">Налаштування фільтрів: конектори та генератори онлайн</div>

    <div style="display:flex; gap:8px; align-items:center; background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:8px 12px; margin-bottom:12px;">
      <div style="display:flex; align-items:center; gap:6px; background:#FFF; border:1px solid #005EC9; border-radius:6px; padding:5px 9px; font-size:11px; font-weight:600; width:180px;">
        <span>🔍</span> <span>вул. Стрийська, 199</span>
      </div>
      <button style="background:#005EC9; color:#FFF; border:none; padding:5px 9px; border-radius:6px; font-size:10.5px; font-weight:700;">⚡ Всі</button>
      <button style="background:#FFF; border:1px solid #CBD5E1; color:#0F172A; padding:5px 9px; border-radius:6px; font-size:10.5px; font-weight:600;">CCS 2</button>
      <button style="background:#ECFDF5; border:1px solid #047857; color:#047857; padding:5px 9px; border-radius:6px; font-size:10.5px; font-weight:700;">🔋 Генератор</button>
      <div style="display:flex; align-items:center; gap:5px; margin-left:auto; font-size:10.5px; font-weight:600; color:#0F172A;">
        <span style="color:#005EC9; font-weight:bold;">✓</span> Вільні
      </div>
    </div>
    <div class="t-map-box">
      <div style="position:absolute; top:40px; left:240px; transform:translate(-50%,-50%); text-align:center;">
        <div style="width:14px; height:14px; border-radius:50%; background:#0077E6; border:2px solid #FFF; margin:0 auto;"></div>
        <div style="background:#0B132B; color:#FFF; font-size:9px; font-weight:700; padding:3px 7px; border-radius:4px; margin-top:3px;">Київ · 120 кВт (3/4) 🔋</div>
      </div>
      <div style="position:absolute; top:70px; left:80px; transform:translate(-50%,-50%); text-align:center;">
        <div style="width:14px; height:14px; border-radius:50%; background:#10B981; border:2px solid #FFF; margin:0 auto;"></div>
        <div style="background:#0B132B; color:#FFF; font-size:9px; font-weight:700; padding:3px 7px; border-radius:4px; margin-top:3px;">Львів · 160 кВт (5/6) 🔋</div>
      </div>
      <div style="position:absolute; top:180px; left:300px; transform:translate(-50%,-50%); text-align:center;">
        <div style="width:14px; height:14px; border-radius:50%; background:#F59E0B; border:2px solid #FFF; margin:0 auto;"></div>
        <div style="background:#0B132B; color:#FFF; font-size:9px; font-weight:700; padding:3px 7px; border-radius:4px; margin-top:3px;">Одеса · 100 кВт (1/2) 🔋</div>
      </div>
    </div>
  </section>

  <!-- GENERATOR -->
  <section class="t-gen">
    <div style="font-size:11px; font-weight:800; color:#10B981; margin-bottom:4px;">⚡ ЕНЕРГОНЕЗАЛЕЖНІСТЬ 100%</div>
    <div style="font-size:22px; font-weight:800; margin-bottom:8px;">Заряджайте авто під час блекаутів</div>
    <div style="font-size:13px; color:#CBD5E1; margin-bottom:14px;">180+ станцій мережі обладнані промисловими дизель-генераторами 160 кВт.</div>
    <img src="{GEN_URL}" style="width:100%; height:200px; object-fit:cover; border-radius:10px;">
  </section>

  <!-- HUBS -->
  <section class="t-hubs">
    <div style="font-size:18px; font-weight:800; margin-bottom:4px;">Популярні зарядні хаби</div>
    <div class="t-hubs-grid">
      <div class="t-hub-card">
        <img src="{HUB_KYIV_URL}" class="t-hub-img">
        <div style="padding:12px;">
          <div style="font-weight:700; font-size:13px;">Хаб «Київ-Поділ» · 120 кВт</div>
          <div style="font-size:11px; color:#64748B; margin:3px 0 6px;">вул. Сагайдачного, 12</div>
          <div style="font-size:10px; font-weight:700; color:#15803D; background:#DCFCE7; display:inline-block; padding:2px 6px; border-radius:4px; margin-bottom:8px;">🔋 Генератор ON</div>
          <button style="width:100%; background:#0077E6; color:#FFF; border:none; padding:8px 0; border-radius:6px; font-size:11px; font-weight:700;">Маршрут</button>
        </div>
      </div>
      <div class="t-hub-card">
        <img src="{HUB_LVIV_URL}" class="t-hub-img">
        <div style="padding:12px;">
          <div style="font-weight:700; font-size:13px;">Хаб «Арена Львів» · 160 кВт</div>
          <div style="font-size:11px; color:#64748B; margin:3px 0 6px;">вул. Стрийська, 199</div>
          <div style="font-size:10px; font-weight:700; color:#15803D; background:#DCFCE7; display:inline-block; padding:2px 6px; border-radius:4px; margin-bottom:8px;">🔋 Сонячний навіс</div>
          <button style="width:100%; background:#0077E6; color:#FFF; border:none; padding:8px 0; border-radius:6px; font-size:11px; font-weight:700;">Маршрут</button>
        </div>
      </div>
    </div>
  </section>

  <!-- STEPS -->
  <section class="t-steps">
    <div style="font-size:18px; font-weight:800; margin-bottom:12px;">Як зарядитися за 3 кроки</div>
    <div class="t-step-item"><b>1. Знайдіть станцію на карті</b> — Фільтруйте за потужністю, конектором та світлом.</div>
    <div class="t-step-item"><b>2. Підключіть конектор CCS2</b> — Світловий смарт-індикатор спалахне зеленим.</div>
    <div class="t-step-item"><b>3. Оплатіть у 1 клік</b> — Apple Pay, Google Pay або банківська картка.</div>
  </section>

  <!-- REVIEWS -->
  <section class="t-revs">
    <div style="font-size:18px; font-weight:800; margin-bottom:12px;">Відгуки водіїв</div>
    <div class="t-rev-grid">
      <div class="t-rev-card">
        <div style="color:#F59E0B; font-size:12px;">★★★★★</div>
        <div style="font-size:12px; margin:6px 0;">«Зарядився на Подолі під час блекауту за 25 хвилин. Все супер!»</div>
        <div style="font-weight:700; font-size:11px;">Олексій К. (Tesla Model Y)</div>
      </div>
      <div class="t-rev-card">
        <div style="color:#F59E0B; font-size:12px;">★★★★★</div>
        <div style="font-size:12px; margin:6px 0;">«Зручний калькулятор витрат і точний кілометраж.»</div>
        <div style="font-weight:700; font-size:11px;">Олена М. (Nissan Leaf)</div>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="t-foot">
    <div style="font-size:16px; font-weight:800; color:#FFF; margin-bottom:6px;">ChargeUA</div>
    <div>© 2026 ChargeUA · Лемішка Андрій, ПП-24 · Кафедра САПР, НУ «Львівська політехніка»</div>
  </footer>
</body></html>
"""

# ==============================================================================
# 4. FIG 16: MOBILE (CONTINUOUS 390px PAGE MATCHING USER'S PHOTO PIXEL-FOR-PIXEL)
# ==============================================================================
html_mobile_full = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ width: 390px; background: #FFFFFF; color: #0F172A; }}

  .top-bar {{ background: #0B132B; color: #FFFFFF; padding: 7px 16px; font-size: 10px; font-weight: 500; display: flex; justify-content: space-between; align-items: center; }}
  .pulse-dot {{ display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: #10B981; margin-right: 4px; }}

  .header {{ height: 56px; padding: 0 16px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #E2E8F0; background: #FFFFFF; }}
  .logo-wrap {{ display: flex; align-items: center; gap: 8px; }}
  .logo-text {{ font-size: 19px; font-weight: 800; color: #0077E6; letter-spacing: -0.3px; }}
  .burger-btn {{ width: 28px; height: 28px; display: flex; flex-direction: column; justify-content: center; gap: 4px; cursor: pointer; }}
  .burger-line {{ width: 20px; height: 2px; background: #0F172A; border-radius: 2px; }}

  .hero-sec {{ position: relative; overflow: hidden; min-height: 410px; padding: 22px 16px 20px; background: #FFFFFF; }}
  .hero-bg {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: 1; }}
  .hero-overlay {{ position: absolute; inset: 0; background: linear-gradient(to bottom, rgba(255,255,255,0.98) 0%, rgba(255,255,255,0.88) 48%, rgba(255,255,255,0.35) 100%); z-index: 2; }}
  .hero-content {{ position: relative; z-index: 3; }}
  .hero-badge {{ font-size: 10.5px; font-weight: 700; color: #0077E6; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; }}
  .hero-title {{ font-size: 27px; font-weight: 800; line-height: 1.16; color: #0F172A; letter-spacing: -0.5px; margin-bottom: 8px; }}
  .hero-sub {{ font-size: 13px; line-height: 1.45; color: #334155; margin-bottom: 14px; }}
  .hero-chips {{ display: flex; gap: 8px; margin-bottom: 14px; }}
  .m-chip {{ font-size: 10px; font-weight: 700; padding: 4px 10px; border-radius: 12px; background: #FFF; border: 1px solid #CBD5E1; color: #0F172A; }}
  .m-chip.gen {{ background: #DCFCE7; border-color: #16A34A; color: #15803D; }}
  .btn-primary {{ display: block; width: 100%; background: #0077E6; color: #FFFFFF; border: none; padding: 13px 0; font-size: 13.5px; font-weight: 700; border-radius: 8px; cursor: pointer; text-align: center; text-decoration: none; box-shadow: 0 3px 8px rgba(0,119,230,0.25); margin-bottom: 8px; }}
  .btn-secondary {{ display: block; width: 100%; background: #FFFFFF; color: #0F172A; border: 1px solid #CBD5E1; padding: 10px 0; font-size: 12.5px; font-weight: 600; border-radius: 8px; cursor: pointer; text-align: center; margin-bottom: 12px; }}
  .m-live-badge {{ background: rgba(15, 23, 42, 0.90); backdrop-filter: blur(4px); color: #FFF; font-size: 10px; font-weight: 700; padding: 6px 10px; border-radius: 6px; display: flex; align-items: center; justify-content: center; gap: 6px; }}
  .m-live-dot {{ width: 6px; height: 6px; border-radius: 50%; background: #00E5FF; }}

  .calc-sec {{ padding: 36px 16px; background: #F8FAFC; border-top: 1px solid #EDF2F7; }}
  .calc-card {{ background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 22px 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.03); }}
  .calc-h3 {{ font-size: 17px; font-weight: 800; color: #0F172A; margin-bottom: 4px; }}
  .calc-model {{ font-size: 13px; font-weight: 600; color: #0077E6; margin-bottom: 14px; }}

  .slider-wrap {{ margin: 12px 0 16px; }}
  .slider-labels {{ display: flex; justify-content: space-between; font-size: 11px; font-weight: 600; color: #64748B; margin-bottom: 6px; }}
  .slider-track {{ position: relative; height: 8px; background: #E2E8F0; border-radius: 4px; }}
  .slider-fill {{ position: absolute; left: 20%; width: 60%; height: 100%; background: #0077E6; border-radius: 4px; }}
  .slider-thumb {{ position: absolute; left: 80%; top: 50%; transform: translate(-50%, -50%); width: 22px; height: 22px; border-radius: 50%; background: #FFFFFF; border: 3px solid #0077E6; box-shadow: 0 2px 6px rgba(0,119,230,0.4); cursor: pointer; }}
  .slider-tooltip {{ position: absolute; top: -24px; left: 80%; transform: translateX(-50%); background: #0077E6; color: #FFF; font-size: 9px; font-weight: 800; padding: 2px 5px; border-radius: 4px; }}
  .slider-scale {{ display: flex; justify-content: space-between; font-size: 10px; color: #94A3B8; margin-top: 6px; }}

  .calc-price {{ font-size: 21px; font-weight: 800; color: #0F172A; margin-bottom: 4px; }}
  .calc-details {{ font-size: 11.5px; color: #64748B; margin-bottom: 16px; }}

  .map-sec {{ padding: 36px 16px; background: #F8FAFC; border-top: 1px solid #E2E8F0; }}
  .map-box {{ position: relative; height: 190px; border-radius: 12px; overflow: hidden; border: 1px solid #CBD5E1; background: #E2E8F0; }}
  .map-canvas {{ width: 100%; height: 100%; background: url('{MAP_LVIV_URL}') center/cover no-repeat; position: relative; }}
  .map-pin {{ position: absolute; transform: translate(-50%, -50%); display: flex; flex-direction: column; align-items: center; }}
  .pin-dot {{ width: 12px; height: 12px; border-radius: 50%; background: #10B981; border: 2px solid #FFFFFF; box-shadow: 0 0 0 2px #10B981; }}
  .pin-dot.fast {{ background: #0077E6; box-shadow: 0 0 0 2px #0077E6; }}
  .pin-dot.busy {{ background: #F59E0B; box-shadow: 0 0 0 2px #F59E0B; }}
  .pin-label {{ background: #0B132B; color: #FFF; font-size: 8px; font-weight: 700; padding: 2px 5px; border-radius: 3px; margin-top: 2px; white-space: nowrap; }}

  .hubs-sec {{ padding: 36px 16px; background: #FFFFFF; }}
  .sec-heading {{ font-size: 18px; font-weight: 800; color: #0F172A; margin-bottom: 16px; }}
  .hub-card {{ border: 1px solid #E2E8F0; border-radius: 12px; overflow: hidden; margin-bottom: 22px; background: #FFFFFF; }}
  .hub-img {{ width: 100%; height: 140px; object-fit: cover; display: block; }}
  .hub-body {{ padding: 14px 16px; }}
  .hub-title {{ font-size: 14px; font-weight: 700; color: #0F172A; margin-bottom: 3px; }}
  .hub-addr {{ font-size: 11px; color: #64748B; margin-bottom: 8px; }}
  .hub-badge {{ display: inline-flex; align-items: center; gap: 4px; background: #DCFCE7; color: #15803D; font-size: 10px; font-weight: 700; padding: 3px 8px; border-radius: 4px; margin-bottom: 10px; }}
  .btn-outline {{ display: block; width: 100%; background: #F8FAFC; border: 1px solid #0077E6; color: #0077E6; padding: 9px 0; font-size: 12px; font-weight: 700; border-radius: 6px; text-align: center; cursor: pointer; }}

  .gen-sec {{ padding: 38px 16px; background: #0B132B; color: #FFFFFF; }}
  .gen-badge {{ font-size: 10px; font-weight: 800; color: #10B981; margin-bottom: 6px; }}
  .gen-title {{ font-size: 17px; font-weight: 800; line-height: 1.25; margin-bottom: 8px; }}
  .gen-sub {{ font-size: 12px; line-height: 1.45; color: #94A3B8; margin-bottom: 14px; }}
  .gen-img {{ width: 100%; height: 130px; object-fit: cover; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); }}

  .steps-sec {{ padding: 36px 16px; background: #FFFFFF; }}
  .step-card {{ display: flex; gap: 12px; padding: 12px 14px; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; margin-bottom: 10px; }}
  .step-num {{ width: 28px; height: 28px; border-radius: 50%; background: #0077E6; color: #FFFFFF; font-size: 12px; font-weight: 800; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }}
  .step-info {{ flex: 1; }}
  .step-title {{ font-size: 12.5px; font-weight: 700; color: #0F172A; margin-bottom: 2px; }}
  .step-desc {{ font-size: 11px; color: #64748B; line-height: 1.35; }}

  .rev-sec {{ padding: 36px 16px; background: #F8FAFC; border-top: 1px solid #E2E8F0; }}
  .rev-card {{ background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px; padding: 14px 16px; margin-bottom: 14px; }}
  .rev-stars {{ color: #F59E0B; font-size: 11px; margin-bottom: 4px; }}
  .rev-text {{ font-size: 11.5px; color: #334155; line-height: 1.4; margin-bottom: 8px; }}
  .rev-author {{ display: flex; align-items: center; gap: 8px; }}
  .rev-av {{ width: 28px; height: 28px; border-radius: 50%; object-fit: cover; }}
  .rev-name {{ font-size: 11px; font-weight: 700; color: #0F172A; }}
  .rev-car {{ font-size: 10px; color: #64748B; }}

  .footer {{ background: #0B132B; color: #FFFFFF; padding: 32px 16px 85px; border-top: 1px solid #1E293B; }}
  .f-logo {{ font-size: 17px; font-weight: 800; color: #0077E6; margin-bottom: 6px; }}
  .f-desc {{ font-size: 11px; color: #94A3B8; line-height: 1.4; margin-bottom: 16px; }}
  .f-copy {{ font-size: 10px; color: #64748B; }}

  .bottom-nav {{ position: fixed; bottom: 0; left: 0; width: 390px; height: 54px; background: #FFFFFF; border-top: 1px solid #E2E8F0; display: flex; justify-content: space-around; align-items: center; z-index: 100; box-shadow: 0 -2px 10px rgba(0,0,0,0.05); }}
  .nav-item {{ display: flex; flex-direction: column; align-items: center; font-size: 9px; font-weight: 600; color: #64748B; cursor: pointer; }}
  .nav-item.active {{ color: #0077E6; }}
  .nav-icon {{ font-size: 16px; margin-bottom: 2px; }}
</style></head><body>
  <div class="top-bar">
    <div><span class="pulse-dot"></span>480+ станцій онлайн</div>
    <div>0 800 300 400</div>
  </div>

  <header class="header">
    <div class="logo-wrap">
      <img src="{LOGO_URL}" style="width:24px; height:24px;">
      <span class="logo-text">ChargeUA</span>
    </div>
    <div class="burger-btn">
      <div class="burger-line"></div>
      <div class="burger-line"></div>
      <div class="burger-line"></div>
    </div>
  </header>

  <section class="hero-sec">
    <img src="{GIF_LOOP_URL}" class="hero-bg">
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <div class="hero-badge">⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР</div>
      <h1 class="hero-title">Заряджайте авто<br>без стресу</h1>
      <p class="hero-sub">Усі мережі на одній карті з фільтром генераторів у блекаути.</p>
      
      <div class="hero-chips">
        <span class="m-chip">⚡ CCS 2 (160 кВт)</span>
        <span class="m-chip gen">🔋 Тільки генератор</span>
      </div>

      <button class="btn-primary">Розрахувати зарядку →</button>
      <button class="btn-secondary">Знайти найближчий хаб</button>
    </div>
  </section>

  <section class="calc-sec">
    <div class="calc-card">
      <div class="calc-h3">Калькулятор витрат</div>
      <div class="calc-model">VW ID.4 · 20% → 80%</div>

      <div class="slider-wrap">
        <div class="slider-labels">
          <span>Рівень заряду батареї (Повзунок)</span>
          <span style="color:#0077E6;">+46.2 кВт·год</span>
        </div>
        <div class="slider-track">
          <div class="slider-fill"></div>
          <div class="slider-thumb"></div>
          <div class="slider-tooltip">80%</div>
        </div>
        <div class="slider-scale">
          <span>0%</span>
          <span>20% (Старт)</span>
          <span>50%</span>
          <span style="color:#0077E6; font-weight:700;">80% (Ціль)</span>
          <span>100%</span>
        </div>
      </div>

      <div class="calc-price">652.50 ₴ (~28 хв)</div>
      <div class="calc-details">Тариф: 14.12 ₴/кВт·год · 46.2 кВт</div>
      <button class="btn-primary">Знайти вільну станцію</button>
    </div>
  </section>

  <section class="map-sec">
    <h2 class="sec-heading">Live-карта зарядної мережі</h2>
    <div style="font-size:11px; color:#64748B; margin-top:-6px; margin-bottom:10px;">Фільтрація та статус конекторів онлайн:</div>

    <!-- Mobile Map Filter Controls -->
    <div style="display:flex; align-items:center; gap:6px; background:#FFF; border:1.5px solid #005EC9; border-radius:7px; padding:6px 10px; margin-bottom:8px;">
      <span style="font-size:12px;">🔍</span>
      <span style="font-size:11px; font-weight:500; color:#0F172A;">м. Львів, вул. Стрийська, 199</span>
    </div>

    <div style="display:flex; gap:6px; margin-bottom:8px; overflow-x:auto;">
      <span style="background:#005EC9; color:#FFF; font-size:10px; font-weight:700; padding:5px 9px; border-radius:6px; white-space:nowrap;">⚡ Всі</span>
      <span style="background:#FFF; border:1px solid #CBD5E1; color:#0F172A; font-size:10px; font-weight:600; padding:5px 9px; border-radius:6px; white-space:nowrap;">CCS 2 (160 кВт)</span>
      <span style="background:#ECFDF5; border:1px solid #047857; color:#047857; font-size:10px; font-weight:700; padding:5px 9px; border-radius:6px; white-space:nowrap;">🔋 Генератор ON</span>
    </div>

    <div style="display:flex; align-items:center; gap:6px; font-size:10.5px; font-weight:600; color:#0F172A; margin-bottom:10px;">
      <span style="width:14px; height:14px; background:#005EC9; color:#FFF; border-radius:3px; display:inline-flex; align-items:center; justify-content:center; font-size:9px;">✓</span>
      <span>Тільки вільні конектори прямо зараз</span>
    </div>

    <div class="map-box">
      <div class="map-canvas">
        <div class="map-pin" style="top: 40px; left: 140px;">
          <div class="pin-dot fast"></div>
          <div class="pin-label">Київ · 120 кВт (3/4)</div>
        </div>
        <div class="map-pin" style="top: 50px; left: 45px;">
          <div class="pin-dot fast"></div>
          <div class="pin-label">Львів · 160 кВт (4/4)</div>
        </div>
        <div class="map-pin" style="top: 130px; left: 170px;">
          <div class="pin-dot busy"></div>
          <div class="pin-label">Одеса · 100 кВт (1/2)</div>
        </div>
        <div class="map-pin" style="top: 85px; left: 260px;">
          <div class="pin-dot fast"></div>
          <div class="pin-label">Дніпро · 120 кВт (2/2)</div>
        </div>
      </div>
    </div>
  </section>


  <section class="hubs-sec">
    <h2 class="sec-heading">Популярні зарядні хаби</h2>
    <div class="hub-card">
      <img src="{HUB_KYIV_URL}" class="hub-img">
      <div class="hub-body">
        <div class="hub-title">Хаб «Київ-Поділ» · 120 кВт CCS2</div>
        <div class="hub-addr">вул. Сагайдачного, 12 · 4 порти (3 вільно)</div>
        <div class="hub-badge">🔋 Працює від генератора</div>
        <button class="btn-outline">Прокласти маршрут</button>
      </div>
    </div>
    <div class="hub-card">
      <img src="{HUB_LVIV_URL}" class="hub-img">
      <div class="hub-body">
        <div class="hub-title">Хаб «Арена Львів» · 160 кВт CCS2</div>
        <div class="hub-addr">вул. Стрийська, 199 · 6 портів (5 вільно)</div>
        <div class="hub-badge">🔋 Сонячний навіс + Дизель</div>
        <button class="btn-outline">Прокласти маршрут</button>
      </div>
    </div>
  </section>

  <section class="gen-sec">
    <div class="gen-badge">⚡ ЕНЕРГОНЕЗАЛЕЖНІСТЬ 100%</div>
    <h2 class="gen-title">Заряджайте авто навіть під час повних блекаутів</h2>
    <p class="gen-sub">180+ станцій обладнані дизель-генераторами 160 кВт.</p>
    <img src="{GEN_URL}" class="gen-img">
  </section>

  <section class="steps-sec">
    <h2 class="sec-heading">Як зарядитися за 3 кроки</h2>
    <div class="step-card">
      <div class="step-num">1</div>
      <div class="step-info"><div class="step-title">Знайдіть станцію на карті</div><div class="step-desc">Фільтруйте за потужністю, конектором та світлом.</div></div>
    </div>
    <div class="step-card">
      <div class="step-num">2</div>
      <div class="step-info"><div class="step-title">Підключіть конектор CCS2</div><div class="step-desc">Вставте кабель у роз'єм електромобіля.</div></div>
    </div>
    <div class="step-card">
      <div class="step-num">3</div>
      <div class="step-info"><div class="step-title">Оплатіть у 1 клік</div><div class="step-desc">Apple Pay, Google Pay або картка без переплат.</div></div>
    </div>
  </section>

  <section class="rev-sec">
    <h2 class="sec-heading">Відгуки водіїв</h2>
    <div class="rev-card">
      <div class="rev-stars">★★★★★</div>
      <p class="rev-text">«Під час блекауту зарядився за 25 хв на Подолі! Все стабільно.»</p>
      <div class="rev-author">
        <img src="{AV1_URL}" class="rev-av">
        <div><div class="rev-name">Олексій К.</div><div class="rev-car">Tesla Model Y</div></div>
      </div>
    </div>
    <div class="rev-card">
      <div class="rev-stars">★★★★★</div>
      <p class="rev-text">«Калькулятор дуже точний, розрахував витрати до копійки.»</p>
      <div class="rev-author">
        <img src="{AV2_URL}" class="rev-av">
        <div><div class="rev-name">Олена М.</div><div class="rev-car">Nissan Leaf</div></div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="f-logo">ChargeUA</div>
    <p class="f-desc">Національний агрегатор та веб-помічник зарядної інфраструктури України.</p>
    <div class="f-copy">© 2026 ChargeUA · Лемішка Андрій, ПП-24</div>
  </footer>

  <nav class="bottom-nav">
    <div class="nav-item active"><span class="nav-icon">⚡</span>Головна</div>
    <div class="nav-item"><span class="nav-icon">🗺</span>Карта</div>
    <div class="nav-item"><span class="nav-icon">🧮</span>Калькулятор</div>
  </nav>
</body></html>
"""

# Write HTML files
f13_path = os.path.join(HTML_DIR, "fig13_desktop_top.html")
f14_path = os.path.join(HTML_DIR, "fig14_desktop_bottom.html")
f15_path = os.path.join(HTML_DIR, "tablet_full.html")
f16_path = os.path.join(HTML_DIR, "mobile_full.html")

with open(f13_path, "w", encoding="utf-8") as f: f.write(html_fig13)
with open(f14_path, "w", encoding="utf-8") as f: f.write(html_fig14)
with open(f15_path, "w", encoding="utf-8") as f: f.write(html_tablet_full)
with open(f16_path, "w", encoding="utf-8") as f: f.write(html_mobile_full)

print("Generated HTML files.")

# Render Desktop Top (Fig 13)
out_f13 = os.path.join(SCR_DIR, "fig13_desktop_top.png")
render_chrome(f13_path, out_f13, 1440, 2050, scale=1.5)

# Render Desktop Bottom (Fig 14)
out_f14 = os.path.join(SCR_DIR, "fig14_desktop_bottom.png")
render_chrome(f14_path, out_f14, 1440, 1850, scale=1.5)

# Render Tablet Full & Slice into 2 columns (Fig 15 - balanced height)
temp_tablet = os.path.join(HTML_DIR, "temp_tablet_full.png")
render_chrome(f15_path, temp_tablet, 768, 2900, scale=1.5)

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
    board_t.paste(slice_img, (x, 0))

out_f15 = os.path.join(SCR_DIR, "fig15_tablet.png")
board_t.save(out_f15, quality=95)
print(f"Generated sliced Tablet: {out_f15} ({board_t.size})")

# Render Mobile Full & Slice into 3 columns (Fig 16 - balanced height)
temp_mobile = os.path.join(HTML_DIR, "temp_mobile_full.png")
render_chrome(f16_path, temp_mobile, 390, 3100, scale=1.5)

im_m = Image.open(temp_mobile)
mw, mh = im_m.size
slice_h_m = mh // 3

out_w_m = mw * 3 + gap * 2
board_m = Image.new("RGB", (out_w_m, slice_h_m), (241, 245, 249))

for i in range(3):
    box = (0, i * slice_h_m, mw, (i + 1) * slice_h_m)
    slice_img = im_m.crop(box)
    x = i * (mw + gap)
    board_m.paste(slice_img, (x, 0))

out_f16 = os.path.join(SCR_DIR, "fig16_mobile.png")
board_m.save(out_f16, quality=95)
print(f"Generated sliced Mobile: {out_f16} ({board_m.size})")

print("ALL 4 FIGURES RENDERED AND SLICED PERFECTLY!")
