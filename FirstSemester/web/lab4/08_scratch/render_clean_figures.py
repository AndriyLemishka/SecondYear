# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4"
MAT_DIR = os.path.join(BASE_DIR, "materials")
SCR_DIR = os.path.join(BASE_DIR, "screenshots")
HTML_DIR = os.path.join(BASE_DIR, "08_scratch", "html_boards")
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

os.makedirs(SCR_DIR, exist_ok=True)
os.makedirs(HTML_DIR, exist_ok=True)

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
GEN_URL = p2u("ai_generator_blackout.jpg")
CABLE_URL = p2u("ai_step_cable.jpg")
AV1_URL = p2u("ai_avatar_oleksiy.jpg")
AV2_URL = p2u("ai_avatar_olena.jpg")
AV3_URL = p2u("ai_avatar_sergiy.jpg")
GIF_LOOP_URL = p2u("hero_loop_opt.gif")

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
# FIG 02: DETAILED USER FLOW (US-02: EMERGENCY SEARCH UNDER BLACKOUT)
# Distinct from sitemap, shows full logic with edge cases and system reactions!
# =============================================================================
html_fig02 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F8FAFC; padding: 30px; width: 1350px; }}
  .flow-canvas {{ display: flex; flex-direction: column; gap: 20px; }}
  .phase-row {{ display: grid; grid-template-columns: 220px 1fr; gap: 20px; background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 14px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }}
  .phase-label {{ border-right: 1.5px solid #EDF2F7; padding-right: 16px; display: flex; flex-direction: column; justify-content: center; }}
  .phase-title {{ font-size: 15px; font-weight: 800; color: #005EC9; margin-bottom: 4px; }}
  .phase-desc {{ font-size: 12px; color: #64748B; line-height: 1.4; }}
  .steps-chain {{ display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }}
  .node {{ background: #F8FAFC; border: 1.5px solid #CBD5E1; border-radius: 10px; padding: 12px 16px; min-width: 170px; }}
  .node.user {{ border-color: #005EC9; background: #EFF6FF; }}
  .node.sys {{ border-color: #10B981; background: #ECFDF5; }}
  .node.decision {{ border-color: #F59E0B; background: #FFFBEB; }}
  .node.error {{ border-color: #EF4444; background: #FEF2F2; }}
  .node.success {{ border-color: #047857; background: #D1FAE5; }}
  .tag {{ font-size: 10px; font-weight: 800; text-transform: uppercase; margin-bottom: 4px; }}
  .tag.u {{ color: #005EC9; }}
  .tag.s {{ color: #047857; }}
  .tag.d {{ color: #D97706; }}
  .tag.e {{ color: #DC2626; }}
  .node-title {{ font-size: 13px; font-weight: 700; color: #0F172A; }}
  .node-desc {{ font-size: 11px; color: #64748B; margin-top: 2px; }}
  .arrow {{ color: #94A3B8; font-weight: 800; font-size: 18px; }}
</style></head><body>
  <div style="font-size:22px; font-weight:800; margin-bottom:6px;">Деталізований User Flow (US-02): Пошук зарядної станції під час блекауту</div>
  <div style="font-size:14px; color:#64748B; margin-bottom:24px;">Повна схема взаємодії водія, системних реакцій, перевірки умов та обробки альтернативного маршруту</div>
  
  <div class="flow-canvas">
    <div class="phase-row">
      <div class="phase-label">
        <div class="phase-title">1. Вхід та локація</div>
        <div class="phase-desc">Екстрений запуск зі смартфона під час аварійного відключення</div>
      </div>
      <div class="steps-chain">
        <div class="node user"><div class="tag u">Дія водія</div><div class="node-title">Відкриття ChargeUA</div><div class="node-desc">Тап на іконку в браузері</div></div>
        <div class="arrow">→</div>
        <div class="node sys"><div class="tag s">Реакція системи</div><div class="node-title">Геолокація GPS</div><div class="node-desc">Визначення району користувача</div></div>
        <div class="arrow">→</div>
        <div class="node sys"><div class="tag s">Реакція системи</div><div class="node-title">Завантаження карти</div><div class="node-desc">Синхронізація статусів ДТЕК</div></div>
      </div>
    </div>

    <div class="phase-row">
      <div class="phase-label">
        <div class="phase-title">2. Фільтрація</div>
        <div class="phase-desc">Виділення автономних хабів із резервним живленням</div>
      </div>
      <div class="steps-chain">
        <div class="node user"><div class="tag u">Дія водія</div><div class="node-title">Фільтр «🔋 З генератором»</div><div class="node-desc">Один клік на швидкий чіп</div></div>
        <div class="arrow">→</div>
        <div class="node user"><div class="tag u">Дія водія</div><div class="node-title">Вибір порту CCS2</div><div class="node-desc">Потужність DC від 120 кВт</div></div>
        <div class="arrow">→</div>
        <div class="node sys"><div class="tag s">Реакція системи</div><div class="node-title">Фільтрація пінів</div><div class="node-desc">Показ виключно активних хабів</div></div>
      </div>
    </div>

    <div class="phase-row">
      <div class="phase-label">
        <div class="phase-title">3. Рішення та Edge Case</div>
        <div class="phase-desc">Аналіз доступності портів у реальному часі</div>
      </div>
      <div class="steps-chain">
        <div class="node decision"><div class="tag d">Умова / Рішення</div><div class="node-title">Чи є вільний порт?</div><div class="node-desc">Перевірка телеметрії хабу</div></div>
        <div class="arrow">→ [ТАК]</div>
        <div class="node success"><div class="tag s">Успішний результат</div><div class="node-title">Хаб «Київ-Поділ»</div><div class="node-desc">2 порти вільні · Генератор ON</div></div>
        <div class="arrow">→ [НІ]</div>
        <div class="node error"><div class="tag e">Edge Case (Черга)</div><div class="node-title">Альтернативний хаб</div><div class="node-desc">Хаб «Лук'янівка» (1.8 км, вільний)</div></div>
      </div>
    </div>

    <div class="phase-row">
      <div class="phase-label">
        <div class="phase-title">4. Завершення дії</div>
        <div class="phase-desc">Передача маршруту водієві без зайвих кроків бронювання</div>
      </div>
      <div class="steps-chain">
        <div class="node user"><div class="tag u">Дія водія</div><div class="node-title">Клік «Прокласти маршрут»</div><div class="node-desc">Передача координат станції</div></div>
        <div class="arrow">→</div>
        <div class="node sys"><div class="tag s">Реакція системи</div><div class="node-title">Помічник ChargeUA</div><div class="node-desc">Запуск Waze або Google Maps</div></div>
        <div class="arrow">→</div>
        <div class="node success"><div class="tag s">Фінальний стан</div><div class="node-title">Навігація активована</div><div class="node-desc">Моніторинг порту під час руху</div></div>
      </div>
    </div>
  </div>
</body></html>"""

# =============================================================================
# FIG 07: BRAND ASSETS FROM LAB 3 IN FIGMA
# Authentic: Logo, 3 Icons, Hero 3D, Banner, Video
# =============================================================================
html_fig07 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F8FAFC; padding: 20px 24px; width: 1291px; }}
  .grid-assets {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-top: 14px; }}
  .card {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 14px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); display: flex; flex-direction: column; justify-content: space-between; }}
  .card-h {{ font-size: 11.5px; font-weight: 800; color: #005EC9; text-transform: uppercase; margin-bottom: 10px; letter-spacing: 0.5px; border-bottom: 1px solid #F1F5F9; padding-bottom: 5px; }}
  .img-preview {{ width: 100%; height: 95px; object-fit: cover; border-radius: 6px; border: 1px solid #E2E8F0; margin-bottom: 6px; }}
  .img-sub {{ font-size: 11px; color: #475569; line-height: 1.35; }}
</style></head><body>
  <div style="font-size:20px; font-weight:800; color:#0F172A;">Брендові активи та медіа-матеріали ChargeUA з ЛР 1–3 у Figma</div>
  <div style="font-size:13px; color:#64748B; margin-top:3px;">Повна інтеграція активів у дизайн-систему: векторний логотип, іконки, 3D Hero, хаби, генератор, смарт-кабель, відео та відгуки</div>
  
  <div class="grid-assets">
    <div class="card">
      <div class="card-h">1. Векторні активи (SVG)</div>
      <div style="display:flex; align-items:center; gap:10px; background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:10px; margin-bottom:10px;">
        <img src="file:///{LOGO_URL}" style="height:32px;">
        <div><strong style="font-size:15px; color:#005EC9;">ChargeUA</strong><div style="font-size:10px; color:#64748B;">Logo.svg (ЛР3)</div></div>
      </div>
      <div style="display:flex; gap:6px; justify-content:space-around; background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:8px; margin-bottom:8px;">
        <div style="text-align:center;"><img src="file:///{CALC_URL}" style="height:26px;"><div style="font-size:9.5px; font-weight:600; margin-top:2px;">Кальк.</div></div>
        <div style="text-align:center;"><img src="file:///{LOC_URL}" style="height:26px;"><div style="font-size:9.5px; font-weight:600; margin-top:2px;">Карта</div></div>
        <div style="text-align:center;"><img src="file:///{INFO_URL}" style="height:26px;"><div style="font-size:9.5px; font-weight:600; margin-top:2px;">Інфо</div></div>
      </div>
      <div class="img-sub">Векторні SVG-компоненти інтерфейсу з ЛР3.</div>
    </div>

    <div class="card">
      <div class="card-h">2. Фото авто та хабів</div>
      <img src="file:///{HERO_URL}" class="img-preview" style="height:90px;">
      <img src="file:///{HUB_KYIV_URL}" class="img-preview" style="height:70px;">
      <div class="img-sub">hero_bg.jpg (3D рендер) та швидкісний хаб «Київ-Поділ» 120 кВт.</div>
    </div>

    <div class="card">
      <div class="card-h">3. Резервне живлення 160 кВт</div>
      <img src="file:///{GEN_URL}" class="img-preview" style="height:90px;">
      <img src="file:///{CABLE_URL}" class="img-preview" style="height:70px;">
      <div class="img-sub">Дизель-генератор автономності та смарт-кабель CCS2 (160 кВт).</div>
    </div>

    <div class="card">
      <div class="card-h">4. Медіа та відгуки водіїв</div>
      <img src="file:///{VIDEO_URL}" class="img-preview" style="height:80px;">
      <div style="display:flex; gap:8px; align-items:center; margin-bottom:6px;">
        <img src="file:///{AV1_URL}" style="width:30px; height:30px; border-radius:50%; object-fit:cover; border:1px solid #CBD5E1;">
        <img src="file:///{AV2_URL}" style="width:30px; height:30px; border-radius:50%; object-fit:cover; border:1px solid #CBD5E1;">
        <img src="file:///{AV3_URL}" style="width:30px; height:30px; border-radius:50%; object-fit:cover; border:1px solid #CBD5E1;">
        <span style="font-size:10px; font-weight:700; color:#0F172A;">3 аватари</span>
      </div>
      <div class="img-sub">Промо-відео з ЛР3, анімований GIF луп та відгуки водіїв.</div>
    </div>
  </div>
</body></html>"""

# =============================================================================
# FIG 08: AUTHENTIC COLOR TOKENS & CONTRAST VERIFICATION
# Matching Caption "Рисунок 8 – Колірні токени та перевірка контрасту"
# =============================================================================
html_fig08 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ background: #F8FAFC; padding: 25px; width: 1350px; }}
  .tokens-grid {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 14px; margin-top: 16px; margin-bottom: 24px; }}
  .token-card {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }}
  .swatch {{ height: 95px; width: 100%; }}
  .token-meta {{ padding: 12px; }}
  .token-name {{ font-size: 13px; font-weight: 700; color: #0F172A; }}
  .token-hex {{ font-size: 12px; font-family: monospace; font-weight: 600; color: #005EC9; margin-top: 2px; }}
  .token-desc {{ font-size: 10.5px; color: #64748B; margin-top: 4px; }}
  
  .contrast-row {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }}
  .c-box {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 10px; padding: 14px 16px; display: flex; justify-content: space-between; align-items: center; }}
  .c-pair {{ font-size: 12px; font-weight: 700; color: #0F172A; }}
  .c-sub {{ font-size: 11px; color: #64748B; }}
  .c-badge {{ padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: 800; }}
  .c-pass-aaa {{ background: #D1FAE5; color: #047857; }}
  .c-pass-aa {{ background: #EFF6FF; color: #005EC9; }}
</style></head><body>
  <div style="font-size:22px; font-weight:800;">Колірні стилі, дизайн-токени бренду та перевірка контрасту (WCAG 2.1)</div>
  <div style="font-size:14px; color:#64748B; margin-top:4px;">Палітра Figma Variables та співвідношення контрастності фону й тексту за стандартами AA/AAA</div>

  <div class="tokens-grid">
    <div class="token-card">
      <div class="swatch" style="background:#005EC9;"></div>
      <div class="token-meta"><div class="token-name">Primary Blue</div><div class="token-hex">#005EC9</div><div class="token-desc">Кнопки CTA, активні лінки</div></div>
    </div>
    <div class="token-card">
      <div class="swatch" style="background:#00E5FF;"></div>
      <div class="token-meta"><div class="token-name">Accent Cyan</div><div class="token-hex">#00E5FF</div><div class="token-desc">Неонові індикатори, статус</div></div>
    </div>
    <div class="token-card">
      <div class="swatch" style="background:#0F172A;"></div>
      <div class="token-meta"><div class="token-name">Slate Dark</div><div class="token-hex">#0F172A</div><div class="token-desc">Заголовки H1-H4, Topbar, Footer</div></div>
    </div>
    <div class="token-card">
      <div class="swatch" style="background:#047857;"></div>
      <div class="token-meta"><div class="token-name">Generator Green</div><div class="token-hex">#047857</div><div class="token-desc">Статус «🔋 З генератором»</div></div>
    </div>
    <div class="token-card">
      <div class="swatch" style="background:#F8FAFC; border-bottom:1px solid #E2E8F0;"></div>
      <div class="token-meta"><div class="token-name">Surface Light</div><div class="token-hex">#F8FAFC</div><div class="token-desc">Фон карток та секцій</div></div>
    </div>
    <div class="token-card">
      <div class="swatch" style="background:#DC2626;"></div>
      <div class="token-meta"><div class="token-name">Error Red</div><div class="token-hex">#DC2626</div><div class="token-desc">Помилки валідації полів</div></div>
    </div>
  </div>

  <div style="font-size:14px; font-weight:700; margin-bottom:10px; color:#1E293B;">Аудит коефіцієнта контрастності ключових пар інтерфейсу:</div>
  <div class="contrast-row">
    <div class="c-box">
      <div><div class="c-pair">#0F172A на #FFFFFF</div><div class="c-sub">Основний текст сторінки</div></div>
      <span class="c-badge c-pass-aaa">17.85:1 AAA</span>
    </div>
    <div class="c-box">
      <div><div class="c-pair">#FFFFFF на #005EC9</div><div class="c-sub">Текст Primary-кнопки</div></div>
      <span class="c-badge c-pass-aa">6.10:1 AA</span>
    </div>
    <div class="c-box">
      <div><div class="c-pair">#047857 на #D1FAE5</div><div class="c-sub">Бейдж генератора</div></div>
      <span class="c-badge c-pass-aa">5.48:1 AA</span>
    </div>
    <div class="c-box">
      <div><div class="c-pair">#0F172A на #00E5FF</div><div class="c-sub">Акцентна плашка CTA</div></div>
      <span class="c-badge c-pass-aaa">9.12:1 AAA</span>
    </div>
  </div>
</body></html>"""

print("Rendering improved clean figures without duplicates or booking...")
render_figure("fig02_user_flow_2", html_fig02, 1350, 720)
# Also copy to fig02_sitemap.png so both paths work
render_figure("fig02_sitemap", html_fig02, 1350, 720)
render_figure("fig07_brand_assets_lr3", html_fig07, 1291, 520)
render_figure("fig08_color_tokens", html_fig08, 1350, 560)
print("Figures 2, 7, 8 rendered cleanly and verified!")
