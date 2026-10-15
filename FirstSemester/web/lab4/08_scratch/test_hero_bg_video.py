# -*- coding: utf-8 -*-
import os, subprocess
from PIL import Image

BASE_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4"
MAT_DIR = os.path.join(BASE_DIR, "materials")
HTML_DIR = os.path.join(BASE_DIR, "08_scratch", "html_boards")
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def p2u(fname):
    return os.path.join(MAT_DIR, fname).replace(os.sep, "/")

LOGO_URL = p2u("Logo.svg")
CALC_URL = p2u("Calculator.svg")
LOC_URL = p2u("Location.svg")
INFO_URL = p2u("Information.svg")
VIDEO_URL = p2u("video_content.mp4")
GIF_URL = p2u("hero_loop_opt.gif")
FRAME_URL = p2u("video_frame_30.jpg")

html = f"""<!DOCTYPE html><html><head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, sans-serif; }}
  body {{ width: 1440px; background: #FFFFFF; color: #0F172A; }}

  .top-bar {{ background: #0B132B; color: #FFF; padding: 10px 60px; font-size: 12px; font-weight: 500; display: flex; justify-content: space-between; align-items: center; }}
  .pulse-dot {{ display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #10B981; margin-right: 6px; }}

  .header {{ height: 76px; padding: 0 60px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #E2E8F0; background: #FFF; }}
  .logo-box {{ display: flex; align-items: center; gap: 10px; }}
  .nav-links {{ display: flex; gap: 28px; font-size: 14px; font-weight: 600; color: #334155; }}
  .nav-links a {{ text-decoration: none; color: inherit; }}
  .btn-header {{ background: #0077E6; color: #FFF; border: none; padding: 10px 22px; font-size: 13px; font-weight: 700; border-radius: 8px; cursor: pointer; }}

  /* HERO WITH VIDEO BACKGROUND PLAYING AS GIF */
  .hero-sec {{ position: relative; height: 530px; overflow: hidden; background: #FFFFFF; }}
  .hero-video-bg-wrap {{ position: absolute; top: 0; right: 0; width: 980px; height: 530px; overflow: hidden; }}
  .hero-video-bg {{ width: 100%; height: 100%; object-fit: cover; object-position: right center; display: block; }}
  .hero-fade-overlay {{ position: absolute; top: 0; left: 0; width: 440px; height: 100%; background: linear-gradient(90deg, #FFFFFF 0%, #FFFFFF 25%, rgba(255,255,255,0.9) 60%, rgba(255,255,255,0) 100%); }}

  .hero-content {{ position: relative; z-index: 10; padding: 50px 60px 0; max-width: 680px; }}
  .hero-tag {{ display: inline-flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 800; color: #0077E6; letter-spacing: 0.5px; margin-bottom: 14px; }}
  .hero-h1 {{ font-size: 42px; font-weight: 800; line-height: 1.18; color: #0F172A; letter-spacing: -0.8px; margin-bottom: 16px; }}
  .hero-sub {{ font-size: 16px; color: #64748B; line-height: 1.55; margin-bottom: 26px; }}
  
  .hero-actions {{ display: flex; gap: 16px; margin-bottom: 26px; }}
  .btn-primary {{ background: #0077E6; color: #FFF; border: none; padding: 14px 28px; font-size: 15px; font-weight: 700; border-radius: 8px; cursor: pointer; box-shadow: 0 4px 14px rgba(0,119,230,0.3); }}
  .btn-secondary {{ background: #FFFFFF; color: #0F172A; border: 1.5px solid #CBD5E1; padding: 14px 26px; font-size: 15px; font-weight: 700; border-radius: 8px; cursor: pointer; }}

  .hero-chips {{ display: flex; gap: 10px; }}
  .chip {{ background: #F8FAFC; border: 1px solid #E2E8F0; padding: 7px 16px; border-radius: 20px; font-size: 12px; font-weight: 600; color: #334155; }}
  .chip-green {{ background: #ECFDF5; border-color: #A7F3D0; color: #059669; font-weight: 700; }}

  .hero-video-badge {{ position: absolute; bottom: 20px; right: 40px; z-index: 10; background: rgba(11, 19, 43, 0.88); backdrop-filter: blur(6px); color: #FFF; font-size: 11px; font-weight: 700; padding: 6px 14px; border-radius: 6px; display: flex; align-items: center; gap: 8px; border: 1px solid rgba(255,255,255,0.2); box-shadow: 0 4px 12px rgba(0,0,0,0.3); }}
  .live-dot {{ width: 8px; height: 8px; border-radius: 50%; background: #00E5FF; box-shadow: 0 0 8px #00E5FF; }}

  /* BENEFITS STRIP */
  .strip-sec {{ padding: 24px 60px; }}
  .strip-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }}
  .strip-card {{ background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 14px; padding: 20px 24px; display: flex; align-items: center; gap: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.03); }}
  .strip-icon {{ width: 44px; height: 44px; flex-shrink: 0; }}

  /* CALCULATOR SECTION WITH SLIDER */
  .calc-sec {{ padding: 16px 60px 28px; }}
  .calc-wrap {{ background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 20px; padding: 34px 44px; box-shadow: 0 4px 16px rgba(0,0,0,0.04); }}
  .calc-top-row {{ display: grid; grid-template-columns: 1.4fr 1fr; gap: 40px; align-items: center; }}
  .car-pills {{ display: flex; gap: 12px; margin: 16px 0 22px; }}
  .car-pill {{ background: #F8FAFC; border: 1.5px solid #E2E8F0; padding: 10px 18px; border-radius: 8px; font-size: 13px; font-weight: 600; color: #334155; cursor: pointer; }}
  .car-pill.active {{ background: #0077E6; border-color: #0077E6; color: #FFF; }}

  .slider-box {{ background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 18px 22px; margin-bottom: 8px; }}
  .slider-header {{ display: flex; justify-content: space-between; font-size: 13px; font-weight: 700; color: #0F172A; margin-bottom: 12px; }}
  .slider-rail {{ position: relative; height: 10px; background: #E2E8F0; border-radius: 5px; margin: 34px 0 12px; }}
  .slider-fill {{ position: absolute; left: 20%; width: 60%; height: 100%; background: #0077E6; border-radius: 5px; }}
  .slider-knob {{ position: absolute; left: 80%; top: 50%; transform: translate(-50%, -50%); width: 26px; height: 26px; border-radius: 50%; background: #FFF; border: 3.5px solid #0077E6; box-shadow: 0 3px 10px rgba(0,119,230,0.4); }}
  .slider-badge {{ position: absolute; top: -28px; left: 80%; transform: translateX(-50%); background: #0077E6; color: #FFF; font-size: 11px; font-weight: 800; padding: 3px 8px; border-radius: 5px; white-space: nowrap; }}
  .slider-ticks {{ display: flex; justify-content: space-between; font-size: 11px; color: #64748B; font-weight: 600; }}

  .calc-res-card {{ background: #F0F7FF; border: 1.5px solid #BFDBFE; border-radius: 16px; padding: 26px 30px; }}
  .res-price {{ font-size: 34px; font-weight: 800; color: #0077E6; margin-bottom: 4px; }}
  .res-meta {{ font-size: 13px; color: #475569; margin-bottom: 16px; }}

  /* LIVE MAP SECTION */
  .map-sec {{ padding: 16px 60px 40px; }}
  .map-card {{ border: 1.5px solid #CBD5E1; border-radius: 20px; overflow: hidden; background: #FFFFFF; box-shadow: 0 6px 20px rgba(0,0,0,0.04); }}
  .map-top {{ padding: 20px 28px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #E2E8F0; background: #FAFAFA; }}
  .map-canvas-desktop {{ height: 360px; position: relative; background: radial-gradient(#CBD5E1 1.5px, #F1F5F9 1.5px); background-size: 18px 18px; }}
  .map-artery {{ position: absolute; background: #CBD5E1; }}
  .map-artery-h1 {{ top: 80px; left: 0; right: 0; height: 4px; }}
  .map-artery-h2 {{ top: 240px; left: 0; right: 0; height: 4px; }}
  .map-artery-v1 {{ top: 0; bottom: 0; left: 340px; width: 4px; }}
  .map-artery-v2 {{ top: 0; bottom: 0; left: 680px; width: 4px; }}
  .map-artery-v3 {{ top: 0; bottom: 0; left: 1020px; width: 4px; }}

  .d-pin {{ position: absolute; transform: translate(-50%, -50%); display: flex; flex-direction: column; align-items: center; }}
  .d-dot {{ width: 16px; height: 16px; border-radius: 50%; background: #10B981; border: 3px solid #FFF; box-shadow: 0 0 0 3px #10B981, 0 4px 8px rgba(0,0,0,0.2); }}
  .d-dot.blue {{ background: #0077E6; box-shadow: 0 0 0 3px #0077E6, 0 4px 8px rgba(0,0,0,0.2); }}
  .d-dot.warn {{ background: #F59E0B; box-shadow: 0 0 0 3px #F59E0B, 0 4px 8px rgba(0,0,0,0.2); }}
  .d-tag {{ background: #0B132B; color: #FFF; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 5px; margin-top: 6px; box-shadow: 0 3px 8px rgba(0,0,0,0.25); white-space: nowrap; }}
</style></head><body>
  <div class="top-bar">
    <div><span class="pulse-dot"></span>Мережа ChargeUA: 480+ станцій онлайн по Україні | 100% телеметрія в реальному часі</div>
    <div>Гаряча лінія 24/7: 0 800 300 400 | UA</div>
  </div>

  <header class="header">
    <div class="logo-box">
      <img src="{LOGO_URL}" style="width:34px; height:34px;">
      <span style="font-size:22px; font-weight:800; color:#0077E6;">ChargeUA</span>
    </div>
    <div class="nav-links">
      <a href="#">Головна</a>
      <a href="#">Калькулятор</a>
      <a href="#">Карта станцій</a>
      <a href="#">Тарифи</a>
      <a href="#">Для бізнесу</a>
    </div>
    <div>
      <button style="background:transparent; border:1px solid #CBD5E1; color:#0F172A; padding:10px 18px; font-size:13px; font-weight:700; border-radius:8px; margin-right:10px; cursor:pointer;">Увійти</button>
      <button class="btn-header">Завантажити додаток</button>
    </div>
  </header>

  <!-- HERO WITH BACKGROUND VIDEO LOOP (GIF) -->
  <section class="hero-sec">
    <div class="hero-video-bg-wrap">
      <img src="{GIF_URL}" class="hero-video-bg" alt="ChargeUA Video Loop">
      <div class="hero-fade-overlay"></div>
    </div>

    <div class="hero-content">
      <div class="hero-tag">⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР ЗАРЯДНИХ СТАНЦІЙ</div>
      <h1 class="hero-h1">Швидка та надійна зарядка<br>електромобілів по всій Україні</h1>
      <p class="hero-sub">Знаходьте найближчі станції, розраховуйте вартість за лічені секунди<br>та подорожуйте без хвилювань навіть під час блекаутів.</p>
      
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
    </div>

    <div class="hero-video-badge">
      <span class="live-dot"></span>
      ⚡ Live Video Loop · video_content.mp4 (ЛР №3)
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

  <!-- LIVE MAP SECTION -->
  <section class="map-sec">
    <div class="map-card">
      <div class="map-top">
        <div>
          <h3 style="font-size:20px; font-weight:800; color:#0F172A;">Live-карта зарядної мережі України</h3>
          <p style="font-size:13px; color:#64748B; margin-top:2px;">Реальний статус підключення портів та наявність резервного електропостачання</p>
        </div>
        <div style="display:flex; gap:10px;">
          <button class="chip" style="background:#0077E6; color:#FFF; border:none; cursor:pointer;">Всі хаби (480+)</button>
          <button class="chip" style="cursor:pointer;">⚡ Ultra-Fast (>100 кВт)</button>
          <button class="chip chip-green" style="cursor:pointer;">🔋 Працює від генератора</button>
        </div>
      </div>

      <div class="map-canvas-desktop">
        <div class="map-artery map-artery-h1"></div>
        <div class="map-artery map-artery-h2"></div>
        <div class="map-artery map-artery-v1"></div>
        <div class="map-artery map-artery-v2"></div>
        <div class="map-artery map-artery-v3"></div>

        <!-- Pins -->
        <div class="d-pin" style="top: 80px; left: 680px;">
          <div class="d-dot blue"></div>
          <div class="d-tag">Хаб «Київ-Поділ» · 120 кВт (3/4 вільно) 🔋</div>
        </div>

        <div class="d-pin" style="top: 120px; left: 240px;">
          <div class="d-dot"></div>
          <div class="d-tag">Хаб «Львів-Арена» · 160 кВт (5/6 вільно) 🔋</div>
        </div>

        <div class="d-pin" style="top: 240px; left: 740px;">
          <div class="d-dot warn"></div>
          <div class="d-tag">Хаб «Одеса-Порт» · 100 кВт (1/2 вільно) 🔋</div>
        </div>

        <div class="d-pin" style="top: 180px; left: 1040px;">
          <div class="d-dot blue"></div>
          <div class="d-tag">Хаб «Дніпро-Сіті» · 120 кВт (2/2 вільно) 🔋</div>
        </div>
      </div>
    </div>
  </section>
</body></html>
"""

test_html_path = os.path.join(HTML_DIR, "test_hero_bg_video.html")
fig13_html_path = os.path.join(HTML_DIR, "fig13_desktop_top.html")
with open(test_html_path, "w", encoding="utf-8") as f:
    f.write(html)
with open(fig13_html_path, "w", encoding="utf-8") as f:
    f.write(html)

out_test_png = os.path.join(BASE_DIR, "screenshots", "test_hero_bg_video.png")
out_fig13_png = os.path.join(BASE_DIR, "screenshots", "fig13_desktop_top.png")

cmd = [
    CHROME_PATH,
    "--headless=new",
    "--window-size=1440,1720",
    "--hide-scrollbars",
    "--force-device-scale-factor=1.5",
    f"--screenshot={out_fig13_png}",
    f"file:///{fig13_html_path.replace(os.sep, '/')}"
]
subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

import shutil
shutil.copyfile(out_fig13_png, out_test_png)
print("Rendered updated fig13_desktop_top.png successfully!")

