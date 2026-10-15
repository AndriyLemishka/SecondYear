# -*- coding: utf-8 -*-
import os
import subprocess
from PIL import Image

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SCR_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4\screenshots"
HTML_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4\08_scratch\html_boards"
os.makedirs(HTML_DIR, exist_ok=True)

# -----------------------------------------------------------------------------
# DESKTOP WIREFRAME (FIG 05) - EXACT STYLE OF IMAGE 5 (GREY BLOCKS + DASHED DIVIDERS)
# -----------------------------------------------------------------------------
html_wf_desktop = """<!DOCTYPE html><html><head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, sans-serif; }
  body { background: #EDF2F7; padding: 25px; width: 540px; display: flex; justify-content: center; -webkit-font-smoothing: antialiased; }
  .wf-page { background: #FFFFFF; width: 490px; border: 1.5px solid #94A3B8; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 14px rgba(0,0,0,0.06); }
  .wf-sec { border-bottom: 1.5px dashed #CBD5E1; padding: 13px 18px; }
  .wf-tag { font-size: 10px; font-weight: 800; color: #64748B; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; }
  .wf-rect { background: #F1F5F9; border: 1px solid #CBD5E1; border-radius: 6px; padding: 9px; }
</style></head><body>
  <div class="wf-page">
    <!-- Header -->
    <div class="wf-sec" style="background:#F8FAFC; display:flex; justify-content:space-between; align-items:center;">
      <div style="font-weight:800; font-size:13px; color:#0F172A;">[LOGO] ChargeUA</div>
      <div style="font-size:9.5px; color:#64748B; font-weight:600;">Головна | Калькулятор | Карта | Хаби | Інструкція | Відгуки</div>
      <div style="background:#0F172A; color:#FFF; font-size:9px; font-weight:700; padding:4px 9px; border-radius:4px;">[Знайти хаб]</div>
    </div>

    <!-- Hero Section -->
    <div class="wf-sec">
      <div class="wf-tag">Hero Section</div>
      <div style="display:flex; gap:12px; align-items:center;">
        <div style="flex:1;">
          <div style="height:14px; background:#94A3B8; border-radius:3px; width:85%; margin-bottom:6px;"></div>
          <div style="height:8px; background:#CBD5E1; border-radius:3px; width:100%; margin-bottom:4px;"></div>
          <div style="height:8px; background:#CBD5E1; border-radius:3px; width:65%; margin-bottom:10px;"></div>
          <div style="display:flex; gap:6px;">
            <div style="height:22px; width:72px; background:#005EC9; border-radius:4px; display:flex; align-items:center; justify-content:center; color:#FFF; font-size:8px; font-weight:700;">Розрахувати</div>
            <div style="height:22px; width:62px; border:1px solid #94A3B8; border-radius:4px; display:flex; align-items:center; justify-content:center; font-size:8px; font-weight:700; color:#334155;">На карті</div>
          </div>
        </div>
        <div class="wf-rect" style="width:170px; height:92px; display:flex; align-items:center; justify-content:center; font-size:9.5px; color:#94A3B8; text-align:center;">
          [Hero Image (Car + Station)]
        </div>
      </div>
    </div>

    <!-- 3 Benefits Strip -->
    <div class="wf-sec">
      <div class="wf-tag">3 Benefits Strip</div>
      <div style="display:flex; gap:8px;">
        <div class="wf-rect" style="flex:1; font-size:9px; text-align:center; font-weight:600;">[Icon] Калькулятор</div>
        <div class="wf-rect" style="flex:1; font-size:9px; text-align:center; font-weight:600;">[Icon] Live-карта</div>
        <div class="wf-rect" style="flex:1; font-size:9px; text-align:center; font-weight:600;">[Icon] 100% Генератор</div>
      </div>
    </div>

    <!-- Interactive Calculator -->
    <div class="wf-sec">
      <div class="wf-tag">Interactive Calculator</div>
      <div class="wf-rect" style="height:76px; display:flex; flex-direction:column; justify-content:center; gap:6px;">
        <div style="font-size:9.5px; font-weight:700; color:#334155;">[Car Presets: Tesla | ID.4 | Leaf]</div>
        <div style="height:6px; background:#CBD5E1; border-radius:3px; width:92%; position:relative;">
          <div style="position:absolute; left:60%; top:-4px; width:14px; height:14px; border-radius:50%; background:#005EC9;"></div>
        </div>
        <div style="font-size:10.5px; font-weight:800; color:#0F172A;">652.50 ₴ · ~28 хв (CCS2 Ultra)</div>
      </div>
    </div>

    <!-- Live Map (Immediately after Calculator!) -->
    <div class="wf-sec" style="background:#F8FAFC;">
      <div class="wf-tag">Live-карта зарядної мережі (Online Map)</div>
      <div class="wf-rect" style="height:86px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:4px; border:1.5px dashed #94A3B8;">
        <div style="font-size:10px; font-weight:700; color:#005EC9;">🗺 [Інтерактивна Live-карта: 480+ станцій онлайн]</div>
        <div style="font-size:8.5px; color:#64748B;">[Фільтри: Вільні порти | Потужність >100 кВт | 🔋 Генератор ON]</div>
      </div>
    </div>

    <!-- Popular Stations Grid -->
    <div class="wf-sec">
      <div class="wf-tag">Popular Stations Grid</div>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
        <div class="wf-rect" style="height:64px; font-size:9px;">
          <div style="font-weight:700; color:#0F172A;">[Card] Хаб Київ-Поділ</div>
          <div style="color:#64748B; font-size:8px;">120 кВт CCS2 · 3/4 вільно</div>
          <div style="color:#059669; font-weight:700; font-size:8px; margin-top:2px;">🔋 Генератор ON</div>
        </div>
        <div class="wf-rect" style="height:64px; font-size:9px;">
          <div style="font-weight:700; color:#0F172A;">[Card] Хаб Львів-Арена</div>
          <div style="color:#64748B; font-size:8px;">160 кВт CCS2 · 5/6 вільно</div>
          <div style="color:#059669; font-weight:700; font-size:8px; margin-top:2px;">🔋 Генератор ON</div>
        </div>
      </div>
    </div>

    <!-- Blackout Protection -->
    <div class="wf-sec" style="background:#F8FAFC;">
      <div class="wf-tag">Blackout Protection (Резервне живлення)</div>
      <div class="wf-rect" style="height:54px; font-size:9px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center;">
        <div style="font-weight:700; color:#0F172A;">[Industrial Generator 160 kW Cummins Specs]</div>
        <div style="color:#64748B; font-size:8px;">Автономна робота 48 годин без електромережі · Супутниковий Starlink</div>
      </div>
    </div>

    <!-- Driver Reviews & How To Charge -->
    <div class="wf-sec">
      <div class="wf-tag">Як зарядитися за 3 кроки &amp; Відгуки водіїв</div>
      <div style="display:flex; gap:6px;">
        <div class="wf-rect" style="flex:1; font-size:8px; text-align:center;">[Крок 1: Карта] → [Крок 2: CCS2] → [Крок 3: Оплата]</div>
        <div class="wf-rect" style="flex:1; font-size:8px; text-align:center;">★★★★★ «Під час блекауту дуже виручило!»</div>
      </div>
    </div>

    <!-- Footer -->
    <div class="wf-sec" style="background:#0F172A; color:#FFF; font-size:9px; text-align:center; padding:15px;">
      [Footer 4 Columns &amp; Copyright ChargeUA 2026]
    </div>
  </div>
</body></html>"""

# -----------------------------------------------------------------------------
# MOBILE WIREFRAME (FIG 06) - EXACT STYLE OF IMAGE 5 (GREY BLOCKS + DASHED DIVIDERS)
# -----------------------------------------------------------------------------
html_wf_mobile = """<!DOCTYPE html><html><head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, sans-serif; }
  body { background: #EDF2F7; padding: 25px; width: 420px; display: flex; justify-content: center; -webkit-font-smoothing: antialiased; }
  .wf-page { background: #FFFFFF; width: 360px; border: 1.5px solid #94A3B8; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 14px rgba(0,0,0,0.06); }
  .wf-sec { border-bottom: 1.5px dashed #CBD5E1; padding: 12px 14px; }
  .wf-tag { font-size: 9.5px; font-weight: 800; color: #64748B; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 5px; }
  .wf-rect { background: #F1F5F9; border: 1px solid #CBD5E1; border-radius: 6px; padding: 8px; }
</style></head><body>
  <div class="wf-page">
    <!-- Mobile Header -->
    <div class="wf-sec" style="display:flex; justify-content:space-between; align-items:center; background:#F8FAFC;">
      <div style="font-weight:800; font-size:12px; color:#0F172A;">[LOGO] ChargeUA</div>
      <div style="font-size:14px; font-weight:700; color:#334155;">[☰ Меню]</div>
    </div>

    <!-- Mobile Hero -->
    <div class="wf-sec">
      <div class="wf-tag">Hero (Mobile 390px)</div>
      <div style="height:12px; background:#94A3B8; border-radius:3px; width:80%; margin-bottom:5px;"></div>
      <div style="height:7px; background:#CBD5E1; border-radius:3px; width:92%; margin-bottom:8px;"></div>
      <div class="wf-rect" style="height:72px; display:flex; align-items:center; justify-content:center; font-size:9px; color:#94A3B8; margin-bottom:8px;">
        [Hero Visual (Авто + Хаб)]
      </div>
      <div style="height:26px; background:#005EC9; border-radius:4px; display:flex; align-items:center; justify-content:center; color:#FFF; font-size:9px; font-weight:700;">
        Знайти найближчу станцію (GPS)
      </div>
    </div>

    <!-- Mobile Benefits -->
    <div class="wf-sec">
      <div class="wf-tag">3 Benefits Strip</div>
      <div style="display:flex; flex-direction:column; gap:4px;">
        <div class="wf-rect" style="font-size:8.5px; font-weight:600;">• Калькулятор витрат (автопресети)</div>
        <div class="wf-rect" style="font-size:8.5px; font-weight:600;">• Live-карта: 480+ хабів із живою телеметрією</div>
        <div class="wf-rect" style="font-size:8.5px; font-weight:600;">• 100% захист від блекаутів завдяки генераторам</div>
      </div>
    </div>

    <!-- Mobile Calculator -->
    <div class="wf-sec">
      <div class="wf-tag">Мобільний калькулятор</div>
      <div class="wf-rect" style="display:flex; flex-direction:column; gap:4px;">
        <div style="font-size:8.5px; color:#64748B;">Модель: Tesla Model 3 · Батарея 20% → 80%</div>
        <div style="height:5px; background:#CBD5E1; border-radius:2px; width:90%;"></div>
        <div style="font-size:10px; font-weight:800; color:#0F172A; text-align:center;">652.50 ₴ · ~28 хв (CCS2)</div>
      </div>
    </div>

    <!-- Mobile Live Map (Immediately after Calculator!) -->
    <div class="wf-sec" style="background:#F8FAFC;">
      <div class="wf-tag">Live-карта (Mobile View)</div>
      <div class="wf-rect" style="height:80px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:4px; border:1.5px dashed #94A3B8;">
        <div style="font-size:9.5px; font-weight:700; color:#005EC9;">🗺 [Мобільна карта станцій]</div>
        <div style="font-size:8px; color:#64748B;">[Швидкі фільтри: Вільні | 160 кВт | 🔋 Gen]</div>
      </div>
    </div>

    <!-- Mobile Hub Card -->
    <div class="wf-sec">
      <div class="wf-tag">Популярні станції</div>
      <div class="wf-rect" style="margin-bottom:6px;">
        <div style="font-size:9px; font-weight:700;">Хаб «Київ-Поділ» · 120 кВт CCS2</div>
        <div style="font-size:8px; color:#64748B;">вул. Сагайдачного, 12 · 🔋 Генератор ON</div>
        <div style="margin-top:4px; height:22px; background:#005EC9; border-radius:4px; display:flex; align-items:center; justify-content:center; color:#FFF; font-size:8px; font-weight:700;">
          Прокласти маршрут CCS2
        </div>
      </div>
    </div>

    <!-- Mobile Blackout Protection -->
    <div class="wf-sec" style="background:#0B132B; color:#FFF; border-radius:6px; margin:4px;">
      <div style="font-size:9px; font-weight:800; color:#4ADE80;">⚡ Резервне живлення 160 кВт</div>
      <div style="font-size:8px; color:#94A3B8; margin-top:2px;">180+ станцій працюють під час аварійних відключень через генератори Cummins.</div>
    </div>

    <!-- Mobile Reviews -->
    <div class="wf-sec">
      <div class="wf-tag">Відгуки водіїв</div>
      <div class="wf-rect" style="font-size:8px;">
        ★★★★★ «Під час блекауту виручило!» — Олексій К. (Tesla)
      </div>
    </div>

    <!-- Mobile Footer & Bottom Nav -->
    <div class="wf-sec" style="background:#0F172A; color:#FFF; font-size:8px; text-align:center; padding:10px;">
      <div>© 2026 ChargeUA · Мобільна версія</div>
      <div style="color:#64748B; font-size:7.5px; margin-top:2px;">Гаряча лінія 24/7: 0 800 300 400</div>
    </div>
    <div style="background:#005EC9; color:#FFF; display:flex; justify-content:space-around; padding:8px 0; font-size:8.5px; font-weight:700;">
      <div>🗺 Карта</div>
      <div>🧮 Калькулятор</div>
      <div>⚡ Хаби</div>
    </div>
  </div>
</body></html>"""

p_d = os.path.join(HTML_DIR, "fig05_wireframe_desktop.html")
p_m = os.path.join(HTML_DIR, "fig06_wireframe_mobile.html")

with open(p_d, "w", encoding="utf-8") as f:
    f.write(html_wf_desktop)
with open(p_m, "w", encoding="utf-8") as f:
    f.write(html_wf_mobile)

out_d = os.path.join(SCR_DIR, "fig05_wireframe_desktop.png")
out_m = os.path.join(SCR_DIR, "fig06_wireframe_mobile.png")

cmd_d = [CHROME_PATH, "--headless=new", "--window-size=540,1100", "--hide-scrollbars", "--force-device-scale-factor=2", f"--screenshot={out_d}", f"file:///{p_d.replace(os.sep, '/')}"]
cmd_m = [CHROME_PATH, "--headless=new", "--window-size=420,1100", "--hide-scrollbars", "--force-device-scale-factor=2", f"--screenshot={out_m}", f"file:///{p_m.replace(os.sep, '/')}"]

subprocess.run(cmd_d, check=True)
subprocess.run(cmd_m, check=True)

im_d = Image.open(out_d)
im_m = Image.open(out_m)
print(f"Generated fig05_wireframe_desktop: {im_d.size}")
print(f"Generated fig06_wireframe_mobile: {im_m.size}")
