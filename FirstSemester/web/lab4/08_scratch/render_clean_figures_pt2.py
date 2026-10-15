# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4"
MAT_DIR = os.path.join(BASE_DIR, "materials")
SCR_DIR = os.path.join(BASE_DIR, "screenshots")
HTML_DIR = os.path.join(BASE_DIR, "08_scratch", "html_boards")
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def p2u(fname):
    return os.path.join(MAT_DIR, fname).replace(os.sep, "/")

LOGO_URL = p2u("Logo.svg")
HUB_KYIV_URL = p2u("ai_hub_kyiv.jpg")
HUB_LVIV_URL = p2u("ai_hub_lviv.jpg")
GEN_URL = p2u("ai_generator_blackout.jpg")
CABLE_URL = p2u("ai_step_cable.jpg")
AV1_URL = p2u("ai_avatar_oleksiy.jpg")
AV2_URL = p2u("ai_avatar_olena.jpg")
AV3_URL = p2u("ai_avatar_sergiy.jpg")

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

# =============================================================================
# FIG 19: AUTHENTIC OVERLAYS: DRAWER + ASSISTANT ROUTE MODAL (NO BOOKING!)
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

  <!-- Модальне вікно помічника на затемненому фоні -->
  <div class="modal-container">
    <div class="modal-card">
      <div style="background:#D1FAE5; color:#047857; display:inline-block; padding:4px 12px; border-radius:999px; font-size:11px; font-weight:700; margin-bottom:12px;">
        ● Маршрут побудовано
      </div>
      <h3 style="font-size:18px; font-weight:800; color:#0F172A; margin-bottom:8px;">Помічник ChargeUA: Станцію обрано!</h3>
      <p style="font-size:12px; color:#64748B; line-height:1.5; margin-bottom:18px;">
        Хаб «Київ-Поділ» (120 кВт CCS2) додано до маршруту. Додаток автоматично моніторить статус портів та світла.
      </p>
      <button style="width:100%; height:40px; background:#0F172A; color:#FFF; border:none; border-radius:8px; font-weight:700; font-size:12.5px;">Відкрити Waze / Google Maps</button>
    </div>
  </div>
</body></html>"""

# =============================================================================
# FIG 17: CATALOG & DETAILS DESKTOP (NO BOOKING, ONLY ASSISTANT ROUTE)
# =============================================================================
html_fig17 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F8FAFC; padding: 25px; width: 1291px; }}
  .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 16px; }}
  .card {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 12px; overflow: hidden; }}
  .card-pad {{ padding: 20px; }}
  .badge {{ background: #D1FAE5; color: #047857; padding: 3px 8px; border-radius: 6px; font-size: 11px; font-weight: 700; }}
</style></head><body>
  <div style="font-size:22px; font-weight:800;">Сторінки «Каталог станцій» та «Деталі локації» (Desktop 1440)</div>
  <div class="grid">
    <div class="card">
      <div style="background:#0F172A; color:#FFF; padding:12px 16px; font-size:12px; font-weight:700;">Сторінка 02 · Каталог та Карта станцій</div>
      <div class="card-pad">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
          <input type="text" value="Київ, Поділ..." style="height:36px; border:1px solid #CBD5E1; border-radius:6px; padding:0 12px; width:65%; font-size:12px;">
          <span class="badge">🔋 142 станції онлайн</span>
        </div>
        <div style="display:flex; gap:10px; align-items:center; background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:10px; margin-bottom:10px;">
          <img src="file:///{HUB_KYIV_URL}" style="width:70px; height:50px; object-fit:cover; border-radius:6px;">
          <div style="flex:1;">
            <div style="font-size:12.5px; font-weight:700;">Хаб «Київ-Поділ» · 120 кВт CCS2</div>
            <div style="font-size:11px; color:#64748B;">вул. Сагайдачного, 12 · 14.50 ₴/кВт·год</div>
          </div>
          <button style="height:32px; background:#005EC9; color:#FFF; border:none; border-radius:6px; padding:0 12px; font-size:11px; font-weight:700;">Маршрут</button>
        </div>
        <div style="display:flex; gap:10px; align-items:center; background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:10px;">
          <img src="file:///{HUB_LVIV_URL}" style="width:70px; height:50px; object-fit:cover; border-radius:6px;">
          <div style="flex:1;">
            <div style="font-size:12.5px; font-weight:700;">Хаб «Арена Львів» · 160 кВт CCS2</div>
            <div style="font-size:11px; color:#64748B;">вул. Стрийська, 199 · 15.00 ₴/кВт·год</div>
          </div>
          <button style="height:32px; background:#005EC9; color:#FFF; border:none; border-radius:6px; padding:0 12px; font-size:11px; font-weight:700;">Маршрут</button>
        </div>
      </div>
    </div>

    <div class="card">
      <div style="background:#005EC9; color:#FFF; padding:12px 16px; font-size:12px; font-weight:700;">Сторінка 03 · Детальна картка станції (Live Telemetry)</div>
      <div class="card-pad">
        <img src="file:///{HUB_KYIV_URL}" style="width:100%; height:120px; object-fit:cover; border-radius:8px; margin-bottom:12px;">
        <div style="font-size:16px; font-weight:800; margin-bottom:4px;">Хаб «Київ-Поділ» (EcoFactor Network)</div>
        <div style="font-size:12px; color:#64748B; margin-bottom:12px;">м. Київ, вул. Петра Сагайдачного, 12 · 24/7</div>
        <div style="display:flex; justify-content:space-between; background:#ECFDF5; border:1px solid #A7F3D0; padding:8px 12px; border-radius:6px; margin-bottom:12px; font-size:12px;">
          <span style="color:#047857; font-weight:700;">🔋 Дизель-генератор 160 кВА активний</span>
          <span style="font-weight:700;">2x CCS2 Вільні</span>
        </div>
        <button style="width:100%; height:38px; background:#005EC9; color:#FFF; border:none; border-radius:8px; font-weight:700; font-size:12.5px;">Прокласти маршрут у навігаторі (Waze/Maps)</button>
      </div>
    </div>
  </div>
</body></html>"""

# =============================================================================
# FIG 18: CATALOG & DETAILS MOBILE (NO BOOKING)
# =============================================================================
html_fig18 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F8FAFC; padding: 20px; width: 750px; display: flex; gap: 20px; justify-content: center; }}
  .phone {{ width: 330px; background: #FFF; border: 1.5px solid #CBD5E1; border-radius: 18px; padding: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.04); }}
</style></head><body>
  <div class="phone">
    <div style="font-size:11px; font-weight:800; color:#005EC9; text-transform:uppercase; margin-bottom:8px;">Мобільний Каталог (390px)</div>
    <div style="font-size:15px; font-weight:800; margin-bottom:10px;">Станції поруч (Київ)</div>
    <div style="background:#F1F5F9; border-radius:8px; padding:10px; margin-bottom:10px;">
      <img src="file:///{HUB_KYIV_URL}" style="width:100%; height:80px; object-fit:cover; border-radius:6px; margin-bottom:6px;">
      <div style="font-weight:700; font-size:12px;">Хаб «Поділ» · 120 кВт</div>
      <div style="font-size:10.5px; color:#64748B; margin-bottom:8px;">14.50 ₴/кВт·год · 🔋 Генератор ON</div>
      <button style="width:100%; height:32px; background:#005EC9; color:#FFF; border:none; border-radius:6px; font-size:11px; font-weight:700;">Прокласти маршрут</button>
    </div>
  </div>

  <div class="phone">
    <div style="font-size:11px; font-weight:800; color:#005EC9; text-transform:uppercase; margin-bottom:8px;">Деталі станції (390px)</div>
    <img src="file:///{HUB_KYIV_URL}" style="width:100%; height:110px; object-fit:cover; border-radius:8px; margin-bottom:8px;">
    <div style="font-weight:800; font-size:14px; margin-bottom:4px;">Хаб «Київ-Поділ»</div>
    <div style="font-size:11px; color:#64748B; margin-bottom:10px;">вул. Сагайдачного, 12</div>
    <div style="background:#D1FAE5; color:#047857; font-weight:700; font-size:11px; padding:6px; border-radius:6px; text-align:center; margin-bottom:12px;">
      ● 2x CCS2 Вільні · 100% Живлення
    </div>
    <button style="width:100%; height:36px; background:#005EC9; color:#FFF; border:none; border-radius:8px; font-size:12px; font-weight:700;">Відкрити у Waze / Maps</button>
  </div>
</body></html>"""

# =============================================================================
# FIG 22: CARDS & NAVIGATION (NO BOOKING, BUTTON: ПРОКЛАСТИ МАРШРУТ)
# =============================================================================
html_fig22 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F8FAFC; padding: 25px; width: 1083px; }}
  .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 16px; }}
  .card {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 20px; }}
</style></head><body>
  <div style="font-size:22px; font-weight:800;">UI-компоненти: Картки станцій, відгуків, навігація та футер</div>
  <div class="grid">
    <div class="card">
      <div style="font-size:13px; font-weight:800; color:#005EC9; margin-bottom:12px; text-transform:uppercase;">Компонент Card / Station:</div>
      <div style="border:1.5px solid #E2E8F0; border-radius:10px; overflow:hidden;">
        <img src="file:///{HUB_KYIV_URL}" style="width:100%; height:110px; object-fit:cover;">
        <div style="padding:14px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
            <strong style="font-size:14px;">Хаб «Київ-Поділ»</strong>
            <span style="background:#D1FAE5; color:#047857; font-size:10.5px; font-weight:700; padding:2px 8px; border-radius:4px;">🔋 Генератор ON</span>
          </div>
          <div style="font-size:11.5px; color:#64748B; margin-bottom:12px;">вул. Сагайдачного, 12 · 14.50 ₴/кВт·год</div>
          <button style="width:100%; height:36px; background:#005EC9; color:#FFF; border:none; border-radius:6px; font-size:12px; font-weight:700;">Прокласти маршрут</button>
        </div>
      </div>
    </div>

    <div class="card">
      <div style="font-size:13px; font-weight:800; color:#005EC9; margin-bottom:12px; text-transform:uppercase;">Компонент Card / Review (З аватаром):</div>
      <div style="border:1.5px solid #E2E8F0; border-radius:10px; padding:16px; background:#F8FAFC;">
        <div style="color:#F59E0B; font-weight:800; margin-bottom:8px;">★★★★★</div>
        <p style="font-size:12.5px; line-height:1.5; color:#334155; margin-bottom:14px;">
          «Помічник ChargeUA буквально рятує під час блекаутів. В один клік знаходжу працюючу зарядку з генератором без затримок!»
        </p>
        <div style="display:flex; align-items:center; gap:10px;">
          <img src="file:///{AV1_URL}" style="width:40px; height:40px; border-radius:50%; object-fit:cover; border:2px solid #005EC9;">
          <div><strong style="font-size:13px;">Олексій Коваленко</strong><div style="font-size:11px; color:#64748B;">Tesla Model Y · Київ</div></div>
        </div>
      </div>
    </div>
  </div>
</body></html>"""

print("Rendering clean non-booking figures: 17, 18, 19, 22...")
render_figure("fig17_catalog_details_desktop", html_fig17, 1291, 520)
render_figure("fig18_catalog_details_mobile", html_fig18, 750, 420)
render_figure("fig19_overlays", html_fig19, 898, 420)
render_figure("fig22_cards_nav", html_fig22, 1083, 500)
print("Figures 17, 18, 19, 22 rendered cleanly and verified!")
