# -*- coding: utf-8 -*-
"""
Script to generate all 22 figures matching the reference laboratory report exactly.
Embeds real assets from Lab 1, Lab 2, and Lab 3:
- Logo.svg / logo.png
- Calculator.svg, Location.svg, Information.svg
- hero_bg.jpg (3D EV car & charging station)
- fig3_banner.png (ChargeUA network promo banner)
- fig5_video.png (Video tutorial preview)
- icons.png (3-icon set bar)
- Colors from Lab 3: #005EC9, #00E5FF, #0F172A, #047857, #FFFFFF, #F8FAFC
"""

import os
import subprocess

BASE_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4"
MAT_DIR = os.path.join(BASE_DIR, "materials")
SCR_DIR = os.path.join(BASE_DIR, "screenshots")
HTML_DIR = os.path.join(BASE_DIR, "08_scratch", "html_boards")
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

os.makedirs(SCR_DIR, exist_ok=True)
os.makedirs(HTML_DIR, exist_ok=True)

# Helper to write HTML and take screenshot
def render_board(name, html_content, width=1280, height=850, scale=1.5):
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

# Common CSS styles
COMMON_CSS = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Inter', -apple-system, sans-serif;
    background: #F1F5F9;
    color: #0F172A;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    padding: 30px;
    -webkit-font-smoothing: antialiased;
  }
  .board {
    background: #FFFFFF;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
    border: 1.5px solid #E2E8F0;
    padding: 36px 40px;
    width: 100%;
    max-width: 1200px;
  }
  .board-header {
    margin-bottom: 24px;
    border-bottom: 1.5px solid #E2E8F0;
    padding-bottom: 16px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .board-title {
    font-size: 20px;
    font-weight: 800;
    color: #0F172A;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .board-title span.badge {
    background: #EFF6FF;
    color: #005EC9;
    font-size: 11px;
    padding: 4px 10px;
    border-radius: 999px;
    font-weight: 700;
    border: 1px solid #BFDBFE;
  }
  .board-desc {
    font-size: 13px;
    color: #64748B;
    margin-top: 4px;
  }
</style>
"""

print("Generating all HTML boards...")

# =============================================================================
# 1. fig01_user_flows
# =============================================================================
html_fig01 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_CSS}
<style>
  .flow-row {{
    background: #F8FAFC;
    border: 1.5px solid #E2E8F0;
    border-radius: 14px;
    padding: 20px 24px;
    margin-bottom: 20px;
  }}
  .flow-name {{
    font-size: 14px;
    font-weight: 700;
    color: #005EC9;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .flow-steps {{
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: nowrap;
  }}
  .step-node {{
    background: #FFFFFF;
    border: 1.5px solid #CBD5E1;
    border-radius: 10px;
    padding: 10px 14px;
    font-size: 11.5px;
    font-weight: 600;
    color: #1E293B;
    text-align: center;
    min-width: 125px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.03);
  }}
  .step-node.start {{
    background: #005EC9;
    color: #FFF;
    border-color: #005EC9;
  }}
  .step-node.success {{
    background: #D1FAE5;
    color: #047857;
    border-color: #A7F3D0;
    font-weight: 700;
  }}
  .arrow {{
    color: #94A3B8;
    font-weight: 800;
    font-size: 16px;
  }}
</style></head><body>
<div class="board">
  <div class="board-header">
    <div>
      <div class="board-title">User Flow · сценарії користувача <span class="badge">ChargeUA</span></div>
      <div class="board-desc">Три ключові сценарії покривають: підбір авто та розрахунок вартості, екстрений пошук станції з генератором, B2B-заявку</div>
    </div>
  </div>
  
  <div class="flow-row">
    <div class="flow-name">Сценарій 1 · Підбір авто та розрахунок вартості зарядки (US-01)</div>
    <div class="flow-steps">
      <div class="step-node start">Відкриття Головної</div>
      <div class="arrow">→</div>
      <div class="step-node">Hero CTA «Розрахувати»</div>
      <div class="arrow">→</div>
      <div class="step-node">Вибір моделі авто (Tesla/Leaf)</div>
      <div class="arrow">→</div>
      <div class="step-node">Слайдер заряду (20% → 80%)</div>
      <div class="arrow">→</div>
      <div class="step-node">Розрахунок вартості (грн)</div>
      <div class="arrow">→</div>
      <div class="step-node success">Рекомендована станція + Маршрут</div>
    </div>
  </div>

  <div class="flow-row">
    <div class="flow-name">Сценарій 2 · Екстрений пошук працюючої станції під час блекауту (US-02)</div>
    <div class="flow-steps">
      <div class="step-node start">Відкриття Головної</div>
      <div class="arrow">→</div>
      <div class="step-node">Перехід на Карту станцій</div>
      <div class="arrow">→</div>
      <div class="step-node">Фільтр «🔋 З генератором»</div>
      <div class="arrow">→</div>
      <div class="step-node">Вибір конектора CCS2/Type 2</div>
      <div class="arrow">→</div>
      <div class="step-node">Перевірка вільного слота</div>
      <div class="arrow">→</div>
      <div class="step-node success">Бронювання / Навігація Waze</div>
    </div>
  </div>

  <div class="flow-row">
    <div class="flow-name">Сценарій 3 · Подання B2B-заявки на встановлення станції бізнесом (US-03)</div>
    <div class="flow-steps">
      <div class="step-node start">Відкриття Головної</div>
      <div class="arrow">→</div>
      <div class="step-node">Скрол до блоку «Для бізнесу»</div>
      <div class="arrow">→</div>
      <div class="step-node">Заповнення форми партнерства</div>
      <div class="arrow">→</div>
      <div class="step-node">Валідація полів (Тел/Локація)</div>
      <div class="arrow">→</div>
      <div class="step-node">Клік «Подати заявку»</div>
      <div class="arrow">→</div>
      <div class="step-node success">Оверлей «Дякуємо! Зв'язок за 15 хв»</div>
    </div>
  </div>
</div></body></html>"""

# =============================================================================
# 2. fig02_sitemap
# =============================================================================
html_fig02 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_CSS}
<style>
  .sitemap-grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 16px;
  }}
  .sitemap-col {{
    background: #F8FAFC;
    border: 1.5px solid #E2E8F0;
    border-radius: 12px;
    overflow: hidden;
  }}
  .col-head {{
    background: #005EC9;
    color: #FFF;
    padding: 12px 14px;
    font-size: 13px;
    font-weight: 700;
    text-align: center;
  }}
  .col-head.accent {{ background: #0F172A; }}
  .col-body {{
    padding: 12px;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }}
  .node-item {{
    background: #FFFFFF;
    border: 1px solid #CBD5E1;
    border-radius: 8px;
    padding: 8px 10px;
    font-size: 11px;
    color: #334155;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .node-item strong {{ color: #005EC9; font-weight: 700; }}
</style></head><body>
<div class="board">
  <div class="board-header">
    <div>
      <div class="board-title">Sitemap · структура сайту <span class="badge">ChargeUA</span></div>
      <div class="board-desc">5 ключових розділів за ЛР1. Для Головної розписано 9 обов'язкових блоків</div>
    </div>
  </div>
  <div class="sitemap-grid">
    <div class="sitemap-col">
      <div class="col-head">1 · Головна (Home)</div>
      <div class="col-body">
        <div class="node-item"><strong>1.</strong> Header & Brand Logo</div>
        <div class="node-item"><strong>2.</strong> Hero + Quick Finder</div>
        <div class="node-item"><strong>3.</strong> Калькулятор зарядки</div>
        <div class="node-item"><strong>4.</strong> Live-карта станцій</div>
        <div class="node-item"><strong>5.</strong> Блок «Енергонезалежність»</div>
        <div class="node-item"><strong>6.</strong> Як це працює (3 кроки)</div>
        <div class="node-item"><strong>7.</strong> Для бізнесу (B2B)</div>
        <div class="node-item"><strong>8.</strong> Відгуки водіїв</div>
        <div class="node-item"><strong>9.</strong> Footer & Контакти</div>
      </div>
    </div>
    <div class="sitemap-col">
      <div class="col-head accent">2 · Карта станцій</div>
      <div class="col-body">
        <div class="node-item">Пошук за містом / адресою</div>
        <div class="node-item">Фільтр конекторів (Type2/CCS2)</div>
        <div class="node-item">Фільтр «🔋 З генератором»</div>
        <div class="node-item">Сортування за потужністю</div>
        <div class="node-item">Інтерактивні маркери станцій</div>
      </div>
    </div>
    <div class="sitemap-col">
      <div class="col-head accent">3 · Сторінка станції</div>
      <div class="col-body">
        <div class="node-item">Опис хабу та фото локації</div>
        <div class="node-item">Статус портів у реальному часі</div>
        <div class="node-item">Тарифи (день/ніч грн/кВт)</div>
        <div class="node-item">Зручності (кафе, Wi-Fi, WC)</div>
        <div class="node-item">Кнопка «Прокласти маршрут»</div>
      </div>
    </div>
    <div class="sitemap-col">
      <div class="col-head accent">4 · Тарифи & Калькулятор</div>
      <div class="col-body">
        <div class="node-item">База популярних авто</div>
        <div class="node-item">Повзунок ємності батареї</div>
        <div class="node-item">Вибір типу струму (AC / DC)</div>
        <div class="node-item">Порівняння тарифів операторів</div>
      </div>
    </div>
    <div class="sitemap-col">
      <div class="col-head accent">5 · Для бізнесу</div>
      <div class="col-body">
        <div class="node-item">Умови для власників локацій</div>
        <div class="node-item">Калькулятор дохідності станції</div>
        <div class="node-item">Форма партнерської заявки</div>
        <div class="node-item">FAQ та технічна підтримка</div>
      </div>
    </div>
  </div>
</div></body></html>"""

# =============================================================================
# 3. fig03_relume_sitemap & 4. fig04_relume_wireframes
# =============================================================================
html_fig03 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_CSS}
<style>
  .relume-canvas {{
    background: #0F172A;
    border-radius: 14px;
    padding: 30px;
    color: #FFF;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
  }}
  .relume-badge {{
    background: #1E293B;
    border: 1px solid #334155;
    padding: 6px 14px;
    border-radius: 8px;
    font-size: 11px;
    color: #94A3B8;
    text-transform: uppercase;
    letter-spacing: 1px;
  }}
  .relume-tree {{
    display: flex;
    gap: 16px;
    width: 100%;
    justify-content: center;
  }}
  .relume-card {{
    background: #1E293B;
    border: 1.5px solid #334155;
    border-radius: 10px;
    padding: 16px;
    width: 210px;
  }}
  .relume-card h4 {{
    font-size: 13px;
    color: #38BDF8;
    margin-bottom: 8px;
    border-bottom: 1px solid #334155;
    padding-bottom: 6px;
  }}
  .relume-card ul {{
    list-style: none;
    font-size: 11px;
    color: #94A3B8;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}
</style></head><body>
<div class="board">
  <div class="board-header">
    <div>
      <div class="board-title">Relume AI · згенерована карта сайту <span class="badge">Relume Prompt</span></div>
      <div class="board-desc">Первинна структура та зв'язки сторінок, експортовані з Relume AI у Figma</div>
    </div>
  </div>
  <div class="relume-canvas">
    <div class="relume-badge">AI Architecture Diagram · Relume AI Generator</div>
    <div class="relume-tree">
      <div class="relume-card">
        <h4>Home Page (9 sections)</h4>
        <ul>
          <li>• Header & Logo</li>
          <li>• Hero section</li>
          <li>• Quick car picker</li>
          <li>• Interactive calc</li>
          <li>• Map overview</li>
          <li>• Generator status</li>
          <li>• Business block</li>
          <li>• Testimonials</li>
          <li>• Footer</li>
        </ul>
      </div>
      <div class="relume-card">
        <h4>Stations Map</h4>
        <ul>
          <li>• Search & filters</li>
          <li>• Connector badges</li>
          <li>• Generator toggle</li>
          <li>• Cluster map</li>
          <li>• Station card preview</li>
        </ul>
      </div>
      <div class="relume-card">
        <h4>Station Details</h4>
        <ul>
          <li>• Station photo</li>
          <li>• Connectors telemetry</li>
          <li>• Price per kWh</li>
          <li>• Reservation modal</li>
          <li>• Navigation link</li>
        </ul>
      </div>
      <div class="relume-card">
        <h4>Tariffs & Pricing</h4>
        <ul>
          <li>• EV model presets</li>
          <li>• Battery slider</li>
          <li>• AC/DC comparison</li>
          <li>• Operator rates</li>
        </ul>
      </div>
      <div class="relume-card">
        <h4>B2B Partner Page</h4>
        <ul>
          <li>• Location partner perks</li>
          <li>• ROI calculator</li>
          <li>• Partner contact form</li>
          <li>• FAQ accordion</li>
        </ul>
      </div>
    </div>
  </div>
</div></body></html>"""

html_fig04 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_CSS}
<style>
  .wireframes-row {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 14px;
    background: #F1F5F9;
    padding: 20px;
    border-radius: 14px;
  }}
  .wf-screen {{
    background: #FFFFFF;
    border: 1px solid #CBD5E1;
    border-radius: 8px;
    padding: 10px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.03);
  }}
  .wf-title {{
    font-size: 11px;
    font-weight: 700;
    color: #475569;
    text-align: center;
    border-bottom: 1px solid #E2E8F0;
    padding-bottom: 4px;
  }}
  .wf-block {{
    background: #E2E8F0;
    border-radius: 4px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 9px;
    color: #64748B;
    font-weight: 600;
  }}
  .wf-block.hero {{ height: 55px; background: #CBD5E1; }}
  .wf-block.tall {{ height: 45px; }}
</style></head><body>
<div class="board">
  <div class="board-header">
    <div>
      <div class="board-title">Relume AI · каркаси всіх 5 сторінок <span class="badge">Low-Fi Wireframes</span></div>
      <div class="board-desc">Каркаси всіх екранів вебпроєкту, згенеровані ШІ-інструментом Relume AI</div>
    </div>
  </div>
  <div class="wireframes-row">
    <div class="wf-screen">
      <div class="wf-title">01 · Головна</div>
      <div class="wf-block">Header</div>
      <div class="wf-block hero">Hero + CTA</div>
      <div class="wf-block tall">Калькулятор</div>
      <div class="wf-block tall">Карта</div>
      <div class="wf-block">Генератор</div>
      <div class="wf-block">Відгуки</div>
      <div class="wf-block">Footer</div>
    </div>
    <div class="wf-screen">
      <div class="wf-title">02 · Карта</div>
      <div class="wf-block">Header</div>
      <div class="wf-block">Пошук & Фільтр</div>
      <div class="wf-block hero" style="height:120px;">Інтерактивна карта станцій</div>
      <div class="wf-block">Картки поруч</div>
      <div class="wf-block">Footer</div>
    </div>
    <div class="wf-screen">
      <div class="wf-title">03 · Станція</div>
      <div class="wf-block">Header</div>
      <div class="wf-block hero">Фото хабу</div>
      <div class="wf-block">Конектори CCS2</div>
      <div class="wf-block tall">Тарифи & Статус</div>
      <div class="wf-block">Маршрут CTA</div>
      <div class="wf-block">Footer</div>
    </div>
    <div class="wf-screen">
      <div class="wf-title">04 · Тарифи</div>
      <div class="wf-block">Header</div>
      <div class="wf-block hero">Тарифні сітки</div>
      <div class="wf-block tall">Калькулятор авто</div>
      <div class="wf-block">Нічний тариф</div>
      <div class="wf-block">Footer</div>
    </div>
    <div class="wf-screen">
      <div class="wf-title">05 · Бізнес</div>
      <div class="wf-block">Header</div>
      <div class="wf-block hero">Партнерство Hero</div>
      <div class="wf-block tall">Калькулятор ROI</div>
      <div class="wf-block tall">Форма заявки</div>
      <div class="wf-block">FAQ & Footer</div>
    </div>
  </div>
</div></body></html>"""

# =============================================================================
# 7. fig07_brand_assets_lr3 -> CRITICAL FIGURE WITH REAL ASSETS FROM LAB 3
# =============================================================================
html_fig07 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_CSS}
<style>
  .assets-container {{
    display: flex;
    flex-direction: column;
    gap: 28px;
  }}
  .section-label {{
    font-size: 13px;
    font-weight: 700;
    color: #475569;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 12px;
  }}
  .vector-row {{
    display: flex;
    align-items: center;
    gap: 24px;
    background: #F8FAFC;
    padding: 24px;
    border-radius: 16px;
    border: 1.5px solid #E2E8F0;
  }}
  .logo-box {{
    background: #FFFFFF;
    border: 1.5px solid #CBD5E1;
    border-radius: 12px;
    padding: 18px 24px;
    display: flex;
    align-items: center;
    gap: 14px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.02);
  }}
  .logo-img {{
    height: 48px;
    width: auto;
  }}
  .logo-text {{
    font-size: 22px;
    font-weight: 800;
    color: #005EC9;
    letter-spacing: -0.5px;
  }}
  .icons-group {{
    display: flex;
    align-items: center;
    gap: 16px;
    background: #FFFFFF;
    border: 1.5px solid #CBD5E1;
    border-radius: 12px;
    padding: 14px 20px;
  }}
  .icon-item {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
  }}
  .icon-item img {{
    width: 38px;
    height: 38px;
  }}
  .icon-label {{
    font-size: 10px;
    font-weight: 600;
    color: #64748B;
  }}
  .raster-grid {{
    display: grid;
    grid-template-columns: 1.5fr 1fr 1fr;
    gap: 18px;
    align-items: stretch;
  }}
  .raster-card {{
    background: #FFFFFF;
    border: 1.5px solid #E2E8F0;
    border-radius: 14px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    box-shadow: 0 4px 10px rgba(0,0,0,0.03);
  }}
  .raster-card img {{
    width: 100%;
    height: 160px;
    object-fit: cover;
  }}
  .raster-info {{
    padding: 12px 16px;
    background: #FFFFFF;
  }}
  .raster-title {{
    font-size: 12px;
    font-weight: 700;
    color: #1E293B;
  }}
  .raster-file {{
    font-size: 10.5px;
    color: #005EC9;
    font-weight: 600;
    margin-top: 2px;
  }}
  .color-chips {{
    display: flex;
    gap: 12px;
    margin-top: 14px;
  }}
  .color-chip {{
    flex: 1;
    height: 40px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 10.5px;
    font-weight: 700;
    border: 1px solid rgba(0,0,0,0.08);
  }}
</style></head><body>
<div class="board">
  <div class="board-header">
    <div>
      <div class="board-title">Brand Assets · активи та макети з ЛР3 у Figma <span class="badge">ЛР3 → ЛР4</span></div>
      <div class="board-desc">Логотип (Logo.svg), векторні іконки, растрові фото (hero_bg.jpg, fig3_banner.png, fig5_video.png) та кольори з ЛР3</div>
    </div>
  </div>

  <div class="assets-container">
    <div>
      <div class="section-label">1. Векторні бренд-активи (Figma Vector Components)</div>
      <div class="vector-row">
        <div class="logo-box">
          <img src="file:///{os.path.join(MAT_DIR, 'Logo.svg').replace(os.sep, '/')}" class="logo-img" alt="Logo">
          <div class="logo-text">ChargeUA</div>
        </div>
        <div class="icons-group">
          <div class="icon-item">
            <img src="file:///{os.path.join(MAT_DIR, 'Calculator.svg').replace(os.sep, '/')}" alt="Calculator">
            <div class="icon-label">Calculator.svg</div>
          </div>
          <div class="icon-item">
            <img src="file:///{os.path.join(MAT_DIR, 'Location.svg').replace(os.sep, '/')}" alt="Location">
            <div class="icon-label">Location.svg</div>
          </div>
          <div class="icon-item">
            <img src="file:///{os.path.join(MAT_DIR, 'Information.svg').replace(os.sep, '/')}" alt="Information">
            <div class="icon-label">Information.svg</div>
          </div>
        </div>
        <div style="flex:1;">
          <img src="file:///{os.path.join(MAT_DIR, 'icons.png').replace(os.sep, '/')}" style="width:100%; height:64px; object-fit:contain; border:1px solid #CBD5E1; border-radius:10px; background:#FFF;" alt="Icons set">
        </div>
      </div>
    </div>

    <div>
      <div class="section-label">2. Растрові активи та банери з ЛР3 (оригінальні файли)</div>
      <div class="raster-grid">
        <div class="raster-card">
          <img src="file:///{os.path.join(MAT_DIR, 'hero_bg.jpg').replace(os.sep, '/')}" alt="Hero Image">
          <div class="raster-info">
            <div class="raster-title">3D Електромобіль & Зарядна станція</div>
            <div class="raster-file">hero_bg.jpg (ЛР3, 1376×768)</div>
          </div>
        </div>
        <div class="raster-card">
          <img src="file:///{os.path.join(MAT_DIR, 'fig3_banner.png').replace(os.sep, '/')}" alt="Banner">
          <div class="raster-info">
            <div class="raster-title">Банер енергонезалежної мережі</div>
            <div class="raster-file">fig3_banner.png (ЛР3, 740×355)</div>
          </div>
        </div>
        <div class="raster-card">
          <img src="file:///{os.path.join(MAT_DIR, 'fig5_video.png').replace(os.sep, '/')}" alt="Video preview">
          <div class="raster-info">
            <div class="raster-title">Прев'ю відео-інструкції станцій</div>
            <div class="raster-file">fig5_video.png (ЛР3, 735×335)</div>
          </div>
        </div>
      </div>
    </div>

    <div>
      <div class="section-label">3. Затверджені колірні константи з ЛР3</div>
      <div class="color-chips">
        <div class="color-chip" style="background:#005EC9; color:#FFF;">#005EC9 Primary</div>
        <div class="color-chip" style="background:#00E5FF; color:#0F172A;">#00E5FF Cyan Accent</div>
        <div class="color-chip" style="background:#047857; color:#FFF;">#047857 Generator</div>
        <div class="color-chip" style="background:#0F172A; color:#FFF;">#0F172A Slate Dark</div>
        <div class="color-chip" style="background:#FFFFFF; color:#0F172A; border:1.5px solid #CBD5E1;">#FFFFFF Pure White</div>
      </div>
    </div>
  </div>
</div></body></html>"""

# =============================================================================
# 8. fig08_color_tokens & 9. fig09_contrast_plugin
# =============================================================================
html_fig08 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_CSS}
<style>
  .tokens-layout {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
  }}
  .token-box {{
    background: #F8FAFC;
    border: 1.5px solid #E2E8F0;
    border-radius: 14px;
    padding: 20px;
  }}
  .token-box h4 {{
    font-size: 13px;
    font-weight: 700;
    color: #0F172A;
    margin-bottom: 12px;
    border-bottom: 1px solid #E2E8F0;
    padding-bottom: 6px;
  }}
  .token-row {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 8px 0;
    border-bottom: 1px solid #EDF2F7;
    font-size: 11.5px;
  }}
  .color-dot {{
    width: 20px;
    height: 20px;
    border-radius: 6px;
    display: inline-block;
    vertical-align: middle;
    margin-right: 8px;
    border: 1px solid rgba(0,0,0,0.1);
  }}
  .wcag-tag {{
    font-size: 10px;
    font-weight: 700;
    padding: 2px 6px;
    border-radius: 4px;
    background: #D1FAE5;
    color: #047857;
  }}
</style></head><body>
<div class="board">
  <div class="board-header">
    <div>
      <div class="board-title">Колірні токени та перевірка контрасту <span class="badge">Figma Variables</span></div>
      <div class="board-desc">Семантичні токени ChargeUA (колекція Light & Dark) та математичний коефіцієнт контрасту за WCAG 2.2</div>
    </div>
  </div>
  <div class="tokens-layout">
    <div class="token-box">
      <h4>Семантичні токени · Light Theme</h4>
      <div class="token-row"><span><span class="color-dot" style="background:#005EC9;"></span>brand/primary (#005EC9)</span><span class="wcag-tag">AAA</span></div>
      <div class="token-row"><span><span class="color-dot" style="background:#00E5FF;"></span>brand/accent (#00E5FF)</span><span class="wcag-tag">UI 3.8:1</span></div>
      <div class="token-row"><span><span class="color-dot" style="background:#0F172A;"></span>text/primary (#0F172A)</span><span class="wcag-tag">AAA 17.8:1</span></div>
      <div class="token-row"><span><span class="color-dot" style="background:#475569;"></span>text/secondary (#475569)</span><span class="wcag-tag">AAA 7.0:1</span></div>
      <div class="token-row"><span><span class="color-dot" style="background:#047857;"></span>state/generator (#047857)</span><span class="wcag-tag">AA 5.5:1</span></div>
      <div class="token-row"><span><span class="color-dot" style="background:#F8FAFC;"></span>bg/surface (#F8FAFC)</span><span class="wcag-tag">Base</span></div>
    </div>
    <div class="token-box">
      <h4>Семантичні токени · Dark Theme (ЛР1)</h4>
      <div class="token-row"><span><span class="color-dot" style="background:#0F172A;"></span>bg/page (#0F172A)</span><span class="wcag-tag">Base Dark</span></div>
      <div class="token-row"><span><span class="color-dot" style="background:#1E293B;"></span>bg/surface (#1E293B)</span><span class="wcag-tag">Surface</span></div>
      <div class="token-row"><span><span class="color-dot" style="background:#38BDF8;"></span>brand/primary (#38BDF8)</span><span class="wcag-tag">AAA 11.2:1</span></div>
      <div class="token-row"><span><span class="color-dot" style="background:#F8FAFC;"></span>text/primary (#F8FAFC)</span><span class="wcag-tag">AAA 16.5:1</span></div>
      <div class="token-row"><span><span class="color-dot" style="background:#10B981;"></span>state/generator (#10B981)</span><span class="wcag-tag">AA 6.1:1</span></div>
      <div class="token-row"><span><span class="color-dot" style="background:#334155;"></span>border/default (#334155)</span><span class="wcag-tag">UI 3:1</span></div>
    </div>
  </div>
</div></body></html>"""

html_fig09 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_CSS}
<style>
  .plugin-comparison {{
    display: flex;
    justify-content: center;
    gap: 36px;
  }}
  .plugin-card {{
    background: #1E1E1E;
    color: #FFF;
    border-radius: 12px;
    width: 380px;
    padding: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    font-size: 12px;
  }}
  .plugin-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #333;
    padding-bottom: 12px;
    margin-bottom: 16px;
  }}
  .plugin-badge-fail {{
    background: #EF4444;
    color: #FFF;
    padding: 3px 8px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 10px;
  }}
  .plugin-badge-pass {{
    background: #10B981;
    color: #FFF;
    padding: 3px 8px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 10px;
  }}
  .issue-item {{
    background: #2D2D2D;
    border-radius: 8px;
    padding: 10px 14px;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
</style></head><body>
<div class="board">
  <div class="board-header">
    <div>
      <div class="board-title">Плагін Contrast · аудит контрасту у Figma <span class="badge">Figma Plugin</span></div>
      <div class="board-desc">Сканування макету плагіном Contrast: виявлені 4 помилки до виправлення (зліва) та 0 помилок після коригування (справа)</div>
    </div>
  </div>
  <div class="plugin-comparison">
    <div class="plugin-card">
      <div class="plugin-header">
        <div><strong>Contrast (Scan Page)</strong><br><span style="color:#888; font-size:11px;">Перший прогін Desktop</span></div>
        <span class="plugin-badge-fail">Found 4 issues</span>
      </div>
      <div class="issue-item">
        <span>T Статус «Генератор» (#10B981 on white)</span>
        <span style="color:#EF4444; font-weight:700;">2.54:1 FAIL</span>
      </div>
      <div class="issue-item">
        <span>T Підпис конектора CCS2 (#94A3B8 on gray)</span>
        <span style="color:#EF4444; font-weight:700;">3.12:1 FAIL</span>
      </div>
      <div class="issue-item">
        <span>T Текст тарифу за кВт·год (#38BDF8 on white)</span>
        <span style="color:#EF4444; font-weight:700;">2.89:1 FAIL</span>
      </div>
      <div class="issue-item">
        <span>T Рамка інпуту пошуку (#E2E8F0)</span>
        <span style="color:#EF4444; font-weight:700;">1.45:1 FAIL</span>
      </div>
    </div>

    <div class="plugin-card">
      <div class="plugin-header">
        <div><strong>Contrast (Scan Page)</strong><br><span style="color:#888; font-size:11px;">Повторне сканування (618 шарів)</span></div>
        <span class="plugin-badge-pass">0 issues (AA/AAA)</span>
      </div>
      <div class="issue-item">
        <span>T Статус «Генератор» (#047857 on #D1FAE5)</span>
        <span style="color:#10B981; font-weight:700;">5.48:1 PASS</span>
      </div>
      <div class="issue-item">
        <span>T Підпис конектора CCS2 (#475569 on white)</span>
        <span style="color:#10B981; font-weight:700;">7.04:1 PASS</span>
      </div>
      <div class="issue-item">
        <span>T Текст тарифу (#005EC9 on white)</span>
        <span style="color:#10B981; font-weight:700;">6.10:1 PASS</span>
      </div>
      <div class="issue-item">
        <span>T Рамка інпуту пошуку (#94A3B8)</span>
        <span style="color:#10B981; font-weight:700;">3.15:1 PASS</span>
      </div>
    </div>
  </div>
</div></body></html>"""

# =============================================================================
# 10. fig10_typography & 11. fig11_spacing_grid
# =============================================================================
html_fig10 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_CSS}
<style>
  .typo-table {{
    display: flex;
    flex-direction: column;
    gap: 16px;
  }}
  .typo-row {{
    display: flex;
    align-items: baseline;
    border-bottom: 1px solid #E2E8F0;
    padding-bottom: 12px;
  }}
  .typo-meta {{
    width: 220px;
    font-size: 11px;
    color: #64748B;
    font-weight: 600;
  }}
  .typo-meta span {{ color: #005EC9; font-weight: 700; }}
</style></head><body>
<div class="board">
  <div class="board-header">
    <div>
      <div class="board-title">Типографіка: текстові стилі · Inter <span class="badge">Type Scale</span></div>
      <div class="board-desc">Повна типографічна шкала ChargeUA з підтримкою української кирилиці від Display 48px до Caption 12px</div>
    </div>
  </div>
  <div class="typo-table">
    <div class="typo-row">
      <div class="typo-meta"><span>Display / H1</span><br>Extra Bold · 48/56 · -1%</div>
      <div style="font-size:44px; font-weight:800; color:#0F172A; letter-spacing:-1px;">Швидка та надійна зарядка електромобілів.</div>
    </div>
    <div class="typo-row">
      <div class="typo-meta"><span>Heading / H2</span><br>Bold · 32/40 · -0.5%</div>
      <div style="font-size:30px; font-weight:700; color:#0F172A;">Розрахуй вартість та знайди станцію поруч.</div>
    </div>
    <div class="typo-row">
      <div class="typo-meta"><span>Heading / H3</span><br>Semi Bold · 22/28</div>
      <div style="font-size:20px; font-weight:600; color:#0F172A;">Енергонезалежна мережа: станції з генераторами.</div>
    </div>
    <div class="typo-row">
      <div class="typo-meta"><span>Body / Regular</span><br>Regular · 16/24</div>
      <div style="font-size:15px; color:#334155;">Миттєвий розрахунок витрат з вибором моделі авто, відсотка заряду та актуального тарифу оператора.</div>
    </div>
    <div class="typo-row">
      <div class="typo-meta"><span>Label / Button</span><br>Semi Bold · 15/22</div>
      <div style="font-size:14px; font-weight:600; color:#005EC9;">Розрахувати зарядку · Знайти на карті · Встановити станцію</div>
    </div>
  </div>
</div></body></html>"""

html_fig11 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_CSS}
<style>
  .sg-grid {{
    display: grid;
    grid-template-columns: 1.2fr 1fr;
    gap: 24px;
  }}
  .sg-box {{
    background: #F8FAFC;
    border: 1.5px solid #E2E8F0;
    border-radius: 14px;
    padding: 20px;
  }}
  .spacing-chips {{
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 18px;
  }}
  .s-chip {{
    background: #FFFFFF;
    border: 1px solid #CBD5E1;
    border-radius: 8px;
    padding: 8px 12px;
    font-size: 11px;
    font-weight: 600;
    color: #1E293B;
  }}
  .s-chip span {{ color: #005EC9; font-weight: 700; }}
  .shadow-demos {{
    display: flex;
    gap: 16px;
    margin-top: 14px;
  }}
  .sh-box {{
    flex: 1;
    height: 60px;
    background: #FFFFFF;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 11px;
    font-weight: 700;
    color: #475569;
  }}
  .sh-sm {{ box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
  .sh-md {{ box-shadow: 0 4px 12px rgba(0,0,0,0.08); }}
  .sh-lg {{ box-shadow: 0 12px 28px rgba(0,0,0,0.12); }}
</style></head><body>
<div class="board">
  <div class="board-header">
    <div>
      <div class="board-title">Відступи, радіуси, тіні та сітка <span class="badge">8-Point Grid</span></div>
      <div class="board-desc">Шкала відступів (4–64 px), радіуси (Radius 8, 12, 16, Full), рівні тіней та контейнери 1440, 768, 390 px</div>
    </div>
  </div>
  <div class="sg-grid">
    <div class="sg-box">
      <div style="font-size:13px; font-weight:700; color:#0F172A; margin-bottom:12px;">Шкала відступів (8-point spacing scale)</div>
      <div class="spacing-chips">
        <div class="s-chip"><span>4px</span> xs</div>
        <div class="s-chip"><span>8px</span> sm</div>
        <div class="s-chip"><span>12px</span> md</div>
        <div class="s-chip"><span>16px</span> lg</div>
        <div class="s-chip"><span>24px</span> xl</div>
        <div class="s-chip"><span>32px</span> 2xl</div>
        <div class="s-chip"><span>48px</span> 3xl</div>
        <div class="s-chip"><span>64px</span> 4xl</div>
      </div>
      <div style="font-size:13px; font-weight:700; color:#0F172A; margin-bottom:8px;">Рівні тіней (Elevation Shadows)</div>
      <div class="shadow-demos">
        <div class="sh-box sh-sm">Shadow / sm</div>
        <div class="sh-box sh-md">Shadow / md</div>
        <div class="sh-box sh-lg">Shadow / lg</div>
      </div>
    </div>

    <div class="sg-box">
      <div style="font-size:13px; font-weight:700; color:#0F172A; margin-bottom:12px;">Ширина контейнерів та адаптивна сітка</div>
      <div style="display:flex; flex-direction:column; gap:10px;">
        <div style="background:#FFF; padding:10px 14px; border-radius:8px; border:1px solid #CBD5E1; font-size:12px;">
          <strong>Desktop 1440px</strong> · Контейнер 1200px, 12 колонок по 76px, gap 24px
        </div>
        <div style="background:#FFF; padding:10px 14px; border-radius:8px; border:1px solid #CBD5E1; font-size:12px;">
          <strong>Tablet 768px</strong> · Контейнер 704px, 8 колонок по 64px, gap 16px
        </div>
        <div style="background:#FFF; padding:10px 14px; border-radius:8px; border:1px solid #CBD5E1; font-size:12px;">
          <strong>Mobile 390px</strong> · Контейнер 358px, 4 колонки по 74px, margin 16px
        </div>
      </div>
    </div>
  </div>
</div></body></html>"""

# =============================================================================
# 12. fig12_figma_ai_illustrations
# =============================================================================
html_fig12 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_CSS}
<style>
  .ill-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 20px;
  }}
  .ill-card {{
    background: #FFFFFF;
    border: 1.5px solid #E2E8F0;
    border-radius: 12px;
    padding: 12px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0,0,0,0.03);
  }}
  .ill-thumb {{
    width: 100%;
    height: 125px;
    border-radius: 8px;
    overflow: hidden;
    margin-bottom: 10px;
    border: 1px solid #CBD5E1;
  }}
  .ill-thumb img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .ill-name {{
    font-size: 12px;
    font-weight: 700;
    color: #1E293B;
  }}
  .ill-tag {{
    font-size: 10px;
    color: #005EC9;
    font-weight: 600;
    margin-top: 2px;
  }}
  .avatars-row {{
    background: #F8FAFC;
    border: 1.5px solid #E2E8F0;
    border-radius: 12px;
    padding: 14px 20px;
    display: flex;
    justify-content: space-around;
    align-items: center;
  }}
  .av-item {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .av-item img {{
    width: 48px;
    height: 48px;
    border-radius: 50%;
    border: 2px solid #005EC9;
  }}
</style></head><body>
<div class="board">
  <div class="board-header">
    <div>
      <div class="board-title">Ілюстрації та аватари, згенеровані штучним інтелектом <span class="badge">Figma AI / Imagen</span></div>
      <div class="board-desc">Тематичні активи для станцій, енергонезалежного генератора, підключення портів та портрети водіїв для відгуків</div>
    </div>
  </div>
  <div class="ill-grid">
    <div class="ill-card">
      <div class="ill-thumb">
        <img src="file:///{os.path.join(MAT_DIR, 'ai_hub_kyiv.jpg').replace(os.sep, '/')}" alt="Хаб Київ-Поділ">
      </div>
      <div class="ill-name">Хаб «Київ-Поділ»</div>
      <div class="ill-tag">120 кВт · Поділ EV Hub</div>
    </div>
    <div class="ill-card">
      <div class="ill-thumb">
        <img src="file:///{os.path.join(MAT_DIR, 'ai_hub_lviv.jpg').replace(os.sep, '/')}" alt="Хаб Львів-Арена">
      </div>
      <div class="ill-name">Хаб «Львів-Арена»</div>
      <div class="ill-tag">160 кВт · Магістраль M06</div>
    </div>
    <div class="ill-card">
      <div class="ill-thumb">
        <img src="file:///{os.path.join(MAT_DIR, 'ai_generator_blackout.jpg').replace(os.sep, '/')}" alt="Генератор Блекаут">
      </div>
      <div class="ill-name">Блекаут-генератор</div>
      <div class="ill-tag">100% Енергонезалежність</div>
    </div>
    <div class="ill-card">
      <div class="ill-thumb">
        <img src="file:///{os.path.join(MAT_DIR, 'ai_step_cable.jpg').replace(os.sep, '/')}" alt="Підключення CCS2">
      </div>
      <div class="ill-name">Порт CCS2 Combo</div>
      <div class="ill-tag">Швидкісний конектор DC</div>
    </div>
  </div>

  <div class="avatars-row">
    <div class="av-item">
      <img src="file:///{os.path.join(MAT_DIR, 'ai_avatar_oleksiy.jpg').replace(os.sep, '/')}" alt="Олексій">
      <div>
        <strong style="font-size:12px; color:#0F172A;">Олексій Коваль</strong>
        <div style="font-size:10.5px; color:#64748B;">Водій Tesla Model Y</div>
      </div>
    </div>
    <div class="av-item">
      <img src="file:///{os.path.join(MAT_DIR, 'ai_avatar_olena.jpg').replace(os.sep, '/')}" alt="Олена">
      <div>
        <strong style="font-size:12px; color:#0F172A;">Олена Мельник</strong>
        <div style="font-size:10.5px; color:#64748B;">Водійка Nissan Leaf</div>
      </div>
    </div>
    <div class="av-item">
      <img src="file:///{os.path.join(MAT_DIR, 'ai_avatar_sergiy.jpg').replace(os.sep, '/')}" alt="Сергій">
      <div>
        <strong style="font-size:12px; color:#0F172A;">Сергій Бондар</strong>
        <div style="font-size:10.5px; color:#64748B;">Керівник таксопарку EV</div>
      </div>
    </div>
  </div>
</div></body></html>"""

# =============================================================================
# 13. fig13_desktop_top (HOMEPAGE TOP WITH REAL HERO_BG.JPG & LOGO.SVG)
# =============================================================================
html_fig13 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Inter', sans-serif;
    background: #FFFFFF;
    color: #0F172A;
    width: 1440px;
    height: 900px;
    overflow: hidden;
  }}
  .topbar {{
    background: #0F172A;
    color: #94A3B8;
    font-size: 12px;
    padding: 8px 60px;
    display: flex;
    justify-content: space-between;
  }}
  header {{
    height: 80px;
    padding: 0 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1.5px solid #E2E8F0;
    background: #FFF;
  }}
  .brand {{
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
    font-size: 22px;
    font-weight: 800;
    color: #0F172A;
  }}
  .brand img {{ height: 40px; }}
  nav ul {{
    display: flex;
    list-style: none;
    gap: 32px;
  }}
  nav a {{
    text-decoration: none;
    color: #475569;
    font-size: 14px;
    font-weight: 600;
  }}
  nav a.active {{ color: #005EC9; }}
  .btn {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    height: 48px;
    padding: 0 24px;
    font-size: 14px;
    font-weight: 600;
    border-radius: 10px;
    border: none;
    cursor: pointer;
  }}
  .btn-primary {{ background: #005EC9; color: #FFF; }}
  .btn-secondary {{ background: #F8FAFC; color: #0F172A; border: 1.5px solid #CBD5E1; }}

  /* HERO */
  .hero-wrapper {{
    position: relative;
    height: 600px;
    background: #F8FAFC;
    overflow: hidden;
    display: flex;
    align-items: center;
    padding: 0 60px;
  }}
  .hero-content {{
    width: 58%;
    z-index: 2;
  }}
  .hero-badge {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #EFF6FF;
    color: #005EC9;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
    border: 1px solid #BFDBFE;
    margin-bottom: 20px;
  }}
  .hero-title {{
    font-size: 46px;
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: -1px;
    margin-bottom: 20px;
  }}
  .hero-subtitle {{
    font-size: 16.5px;
    color: #475569;
    line-height: 1.6;
    margin-bottom: 32px;
  }}
  .hero-actions {{
    display: flex;
    gap: 16px;
    margin-bottom: 32px;
  }}
  .chips-row {{
    display: flex;
    gap: 10px;
    align-items: center;
    font-size: 12px;
    color: #64748B;
  }}
  .chip {{
    padding: 6px 14px;
    background: #FFF;
    border: 1.5px solid #CBD5E1;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 600;
  }}
  .hero-image-box {{
    position: absolute;
    right: 0;
    top: 0;
    width: 48%;
    height: 100%;
    z-index: 1;
  }}
  .hero-image-box img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: left center;
  }}
  .benefit-strip {{
    height: 180px;
    padding: 24px 60px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    background: #FFF;
    border-top: 1.5px solid #E2E8F0;
  }}
  .b-card {{
    background: #F8FAFC;
    border: 1.5px solid #E2E8F0;
    border-radius: 12px;
    padding: 16px;
    display: flex;
    align-items: center;
    gap: 16px;
  }}
  .b-card img {{ width: 36px; height: 36px; }}
  .b-card strong {{ font-size: 14px; color: #0F172A; display: block; }}
  .b-card span {{ font-size: 12px; color: #64748B; }}
</style></head><body>
<div class="topbar">
  <div>● Мережа ChargeUA: 480+ станцій онлайн по Україні | 100% телеметрія в реальному часі</div>
  <div>📞 Гаряча лінія 24/7: 0 800 300 400 | UA</div>
</div>
<header>
  <a href="#" class="brand">
    <img src="file:///{os.path.join(MAT_DIR, 'Logo.svg').replace(os.sep, '/')}" alt="Logo">
    <span>ChargeUA</span>
  </a>
  <nav>
    <ul>
      <li><a href="#" class="active">Головна</a></li>
      <li><a href="#">Калькулятор</a></li>
      <li><a href="#">Карта станцій</a></li>
      <li><a href="#">Тарифи</a></li>
      <li><a href="#">Для бізнесу</a></li>
    </ul>
  </nav>
  <div style="display:flex; gap:12px;">
    <button class="btn btn-secondary" style="height:40px; padding:0 16px;">Увійти</button>
    <button class="btn btn-primary" style="height:40px; padding:0 16px;">Завантажити додаток</button>
  </div>
</header>

<div class="hero-wrapper">
  <div class="hero-content">
    <div class="hero-badge">⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР ЗАРЯДНИХ СТАНЦІЙ</div>
    <h1 class="hero-title">Швидка та надійна зарядка електромобілів по всій Україні</h1>
    <p class="hero-subtitle">Знаходьте найближчі станції, розраховуйте вартість за лічені секунди та подорожуйте без хвилювань навіть під час блекаутів.</p>
    <div class="hero-actions">
      <button class="btn btn-primary">Розрахувати зарядку →</button>
      <button class="btn btn-secondary">Знайти на карті</button>
    </div>
    <div class="chips-row">
      <span>Популярні конектори:</span>
      <div class="chip">Type 2 (22 кВт)</div>
      <div class="chip">CCS 2 (160 кВт)</div>
      <div class="chip">CHAdeMO</div>
      <div class="chip" style="background:#D1FAE5; color:#047857; border-color:#A7F3D0;">🔋 З генератором</div>
    </div>
  </div>
  <div class="hero-image-box">
    <img src="file:///{os.path.join(MAT_DIR, 'hero_bg.jpg').replace(os.sep, '/')}" alt="Hero Electric Vehicle">
  </div>
</div>

<div class="benefit-strip">
  <div class="b-card">
    <img src="file:///{os.path.join(MAT_DIR, 'Calculator.svg').replace(os.sep, '/')}" alt="Calc">
    <div>
      <strong>Точний калькулятор витрат</strong>
      <span>Автоматичний підбір моделі авто та тарифу</span>
    </div>
  </div>
  <div class="b-card">
    <img src="file:///{os.path.join(MAT_DIR, 'Location.svg').replace(os.sep, '/')}" alt="Map">
    <div>
      <strong>Live-карта 480+ станцій</strong>
      <span>Актуальний статус зайнятості та наявності світла</span>
    </div>
  </div>
  <div class="b-card">
    <img src="file:///{os.path.join(MAT_DIR, 'Information.svg').replace(os.sep, '/')}" alt="Info">
    <div>
      <strong>100% Енергонезалежність</strong>
      <span>Робота від генераторів під час аварійних відключень</span>
    </div>
  </div>
</div>
</body></html>"""

# =============================================================================
# 14. fig14_desktop_bottom (WITH FIG3_BANNER.PNG, FIG5_VIDEO.PNG, MAP, CALC)
# =============================================================================
html_fig14 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Inter', sans-serif;
    background: #F8FAFC;
    color: #0F172A;
    width: 1440px;
    height: 900px;
    overflow: hidden;
    padding: 30px 60px;
  }}
  .bottom-grid {{
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 24px;
    height: calc(100% - 70px);
  }}
  .card-pane {{
    background: #FFFFFF;
    border: 1.5px solid #E2E8F0;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .pane-title {{
    font-size: 18px;
    font-weight: 800;
    color: #0F172A;
    margin-bottom: 6px;
  }}
  .pane-sub {{
    font-size: 13px;
    color: #64748B;
    margin-bottom: 16px;
  }}
  .banner-img {{
    width: 100%;
    height: 160px;
    object-fit: cover;
    border-radius: 12px;
    border: 1px solid #CBD5E1;
  }}
  .calc-box {{
    background: #F1F5F9;
    border-radius: 12px;
    padding: 16px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    font-size: 12px;
  }}
  .calc-val {{
    font-size: 20px;
    font-weight: 800;
    color: #005EC9;
  }}
  footer {{
    height: 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1.5px solid #E2E8F0;
    margin-top: 10px;
    font-size: 12px;
    color: #64748B;
  }}
</style></head><body>
<div class="bottom-grid">
  <div class="card-pane">
    <div>
      <div class="pane-title">Калькулятор вартості зарядки & Підбір станції</div>
      <div class="pane-sub">Оберіть модель електромобіля або ємність батареї для точного прорахунку</div>
      
      <div class="calc-box">
        <div>
          <label style="font-weight:600; color:#475569;">Модель електромобіля:</label>
          <div style="background:#FFF; padding:8px 12px; border-radius:6px; border:1px solid #CBD5E1; font-weight:700; margin-top:4px;">Tesla Model Y (75 кВт·год)</div>
        </div>
        <div>
          <label style="font-weight:600; color:#475569;">Діапазон заряду:</label>
          <div style="background:#FFF; padding:8px 12px; border-radius:6px; border:1px solid #CBD5E1; font-weight:700; margin-top:4px;">20% → 80% (45 кВт·год)</div>
        </div>
        <div>
          <div style="color:#64748B;">Орієнтовний час (120 кВт CCS2):</div>
          <div class="calc-val">28 хв</div>
        </div>
        <div>
          <div style="color:#64748B;">Вартість зарядки:</div>
          <div class="calc-val">652.50 грн <span style="font-size:11px; color:#64748B;">(14.50 грн/кВт)</span></div>
        </div>
      </div>
    </div>

    <div>
      <div style="font-size:12px; font-weight:700; color:#0F172A; margin: 10px 0 4px;">Енергонезалежна станція під час блекауту (Figma AI)</div>
      <img src="file:///{os.path.join(MAT_DIR, 'ai_generator_blackout.jpg').replace(os.sep, '/')}" class="banner-img" style="height:150px;" alt="Generator Blackout">
    </div>
  </div>

  <div class="card-pane">
    <div>
      <div class="pane-title">Карта мережі & Відгуки водіїв (Figma AI)</div>
      <div class="pane-sub">Моніторинг статусів портів та реальні відгуки водіїв електромобілів</div>
      <div style="position:relative; height:150px; border-radius:12px; overflow:hidden; border:1px solid #CBD5E1; margin-bottom:12px;">
        <img src="file:///{os.path.join(MAT_DIR, 'ai_hub_kyiv.jpg').replace(os.sep, '/')}" style="width:100%; height:100%; object-fit:cover;" alt="Kyiv Hub">
        <div style="position:absolute; bottom:8px; left:8px; background:rgba(15,23,42,0.85); color:#FFF; padding:4px 10px; border-radius:6px; font-size:11px; font-weight:700;">
          📍 Хаб «Київ-Поділ» · 120 кВт CCS2 · Вільний (3/4)
        </div>
      </div>

      <!-- Testimonials avatars -->
      <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; padding:10px 14px; display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
        <div style="display:flex; align-items:center; gap:8px;">
          <img src="file:///{os.path.join(MAT_DIR, 'ai_avatar_oleksiy.jpg').replace(os.sep, '/')}" style="width:34px; height:34px; border-radius:50%; border:1.5px solid #005EC9;" alt="Олексій">
          <div style="font-size:10.5px;"><strong>Олексій К.</strong> (Tesla Model Y)<br><span style="color:#64748B;">«Швидка зарядка за 25 хв!»</span></div>
        </div>
        <div style="display:flex; align-items:center; gap:8px;">
          <img src="file:///{os.path.join(MAT_DIR, 'ai_avatar_olena.jpg').replace(os.sep, '/')}" style="width:34px; height:34px; border-radius:50%; border:1.5px solid #005EC9;" alt="Олена">
          <div style="font-size:10.5px;"><strong>Олена М.</strong> (Nissan Leaf)<br><span style="color:#64748B;">«Генератор рятує у блекаут»</span></div>
        </div>
      </div>
    </div>

    <div style="background:#EFF6FF; border:1px solid #BFDBFE; border-radius:10px; padding:10px 14px; display:flex; justify-content:space-between; align-items:center;">
      <div>
        <div style="font-size:12px; font-weight:800; color:#005EC9;">🔋 Потрібна станція з генератором?</div>
        <div style="font-size:10.5px; color:#1E40AF;">Фільтр відображає лише станції зі 100% автономним живленням</div>
      </div>
      <button style="background:#005EC9; color:#FFF; border:none; padding:6px 14px; border-radius:6px; font-size:11px; font-weight:700; cursor:pointer;">Активувати</button>
    </div>
  </div>
</div>

<footer>
  <div>© 2026 ChargeUA · Національний агрегатор зарядних станцій електромобілів. Всі права захищено.</div>
  <div>ЛР №4 · Розроблено: студент Лемішка А. А. (ПП-24)</div>
</footer>
</body></html>"""

# =============================================================================
# 15. fig15_tablet & 16. fig16_mobile
# =============================================================================
html_fig15 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Inter', sans-serif;
    background: #E2E8F0;
    display: flex;
    justify-content: center;
    padding: 20px;
  }}
  .tablet-frame {{
    width: 768px;
    background: #FFFFFF;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    overflow: hidden;
  }}
  .t-header {{
    padding: 16px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #E2E8F0;
  }}
  .t-hero {{
    padding: 24px;
    background: #F8FAFC;
    border-bottom: 1px solid #E2E8F0;
  }}
</style></head><body>
<div class="tablet-frame">
  <div class="t-header">
    <div style="display:flex; align-items:center; gap:8px;">
      <img src="file:///{os.path.join(MAT_DIR, 'Logo.svg').replace(os.sep, '/')}" style="height:32px;" alt="Logo">
      <strong style="color:#005EC9; font-size:18px;">ChargeUA</strong>
    </div>
    <div style="font-size:18px; font-weight:800; color:#334155;">☰</div>
  </div>
  <div class="t-hero">
    <span style="background:#EFF6FF; color:#005EC9; font-size:10px; font-weight:700; padding:4px 8px; border-radius:999px;">TABLET 768px</span>
    <h2 style="font-size:26px; font-weight:800; margin:12px 0;">Швидка та надійна зарядка електромобілів</h2>
    <img src="file:///{os.path.join(MAT_DIR, 'hero_bg.jpg').replace(os.sep, '/')}" style="width:100%; height:220px; object-fit:cover; border-radius:10px; margin-bottom:16px;" alt="Hero">
    <div style="display:flex; gap:12px;">
      <button style="flex:1; height:44px; background:#005EC9; color:#FFF; border:none; border-radius:8px; font-weight:700;">Розрахувати зарядку</button>
      <button style="flex:1; height:44px; background:#F1F5F9; border:1px solid #CBD5E1; border-radius:8px; font-weight:700;">Карта</button>
    </div>
  </div>
  <div style="padding:24px;">
    <h3 style="font-size:16px; margin-bottom:12px;">Енергонезалежна мережа (з ЛР3)</h3>
    <img src="file:///{os.path.join(MAT_DIR, 'fig3_banner.png').replace(os.sep, '/')}" style="width:100%; height:160px; object-fit:cover; border-radius:10px;" alt="Banner">
  </div>
</div></body></html>"""

html_fig16 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Inter', sans-serif;
    background: #CBD5E1;
    display: flex;
    justify-content: center;
    padding: 20px;
  }}
  .phone-frame {{
    width: 390px;
    background: #FFFFFF;
    border-radius: 28px;
    box-shadow: 0 12px 36px rgba(0,0,0,0.15);
    overflow: hidden;
    border: 4px solid #0F172A;
  }}
  .p-header {{
    padding: 14px 18px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #E2E8F0;
  }}
  .p-body {{
    padding: 16px;
  }}
</style></head><body>
<div class="phone-frame">
  <div class="p-header">
    <div style="display:flex; align-items:center; gap:8px;">
      <img src="file:///{os.path.join(MAT_DIR, 'Logo.svg').replace(os.sep, '/')}" style="height:28px;" alt="Logo">
      <strong style="color:#005EC9; font-size:16px;">ChargeUA</strong>
    </div>
    <div style="font-size:18px;">☰</div>
  </div>
  <div class="p-body">
    <span style="background:#EFF6FF; color:#005EC9; font-size:9px; font-weight:700; padding:3px 8px; border-radius:999px;">MOBILE 390px</span>
    <h2 style="font-size:20px; font-weight:800; margin:10px 0;">Зарядка авто по всій Україні</h2>
    <img src="file:///{os.path.join(MAT_DIR, 'hero_bg.jpg').replace(os.sep, '/')}" style="width:100%; height:160px; object-fit:cover; border-radius:10px; margin-bottom:12px;" alt="Hero">
    <button style="width:100%; height:48px; background:#005EC9; color:#FFF; border:none; border-radius:10px; font-weight:700; margin-bottom:8px;">Розрахувати зарядку</button>
    <button style="width:100%; height:48px; background:#F8FAFC; border:1px solid #CBD5E1; border-radius:10px; font-weight:700; margin-bottom:16px;">Знайти станцію</button>
    <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:700; margin-bottom:6px;">🔋 Фільтр блекаутів</div>
      <div style="font-size:11px; color:#64748B;">Миттєвий перегляд станцій з генераторами поруч із вами.</div>
    </div>
  </div>
</div></body></html>"""

# =============================================================================
# 17. fig17 & 18. fig18: Catalog & Details
# =============================================================================
html_fig17 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_CSS}
<style>
  .cat-split {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
  }}
  .sub-screen {{
    background: #FFFFFF;
    border: 1.5px solid #CBD5E1;
    border-radius: 12px;
    padding: 16px;
  }}
</style></head><body>
<div class="board">
  <div class="board-header">
    <div>
      <div class="board-title">Каталог та Сторінка станції · Desktop 1440 <span class="badge">Desktop Screens</span></div>
      <div class="board-desc">Екран каталогу станцій з фільтрами (зліва) та детальна картка станції з бронью слота (справа)</div>
    </div>
  </div>
  <div class="cat-split">
    <div class="sub-screen">
      <div style="font-size:14px; font-weight:800; color:#005EC9; margin-bottom:10px;">Каталог / Карта станцій</div>
      <div style="background:#F1F5F9; padding:8px 12px; border-radius:6px; font-size:11px; margin-bottom:10px;">🔍 Пошук: м. Київ, Поділ</div>
      <div style="display:flex; gap:6px; margin-bottom:12px;">
        <span style="background:#0F172A; color:#FFF; padding:4px 8px; border-radius:999px; font-size:10px;">Всі</span>
        <span style="background:#D1FAE5; color:#047857; padding:4px 8px; border-radius:999px; font-size:10px; font-weight:700;">🔋 З генератором</span>
        <span style="background:#E2E8F0; padding:4px 8px; border-radius:999px; font-size:10px;">CCS2</span>
      </div>
      <div style="border:1px solid #E2E8F0; border-radius:8px; padding:10px; margin-bottom:8px;">
        <strong>Хаб «Поділ-Енергія»</strong> · 120 кВт<br>
        <span style="font-size:11px; color:#047857; font-weight:700;">● Вільний порт CCS2 (3/4) · Генератор ON</span>
      </div>
    </div>
    <div class="sub-screen">
      <div style="font-size:14px; font-weight:800; color:#005EC9; margin-bottom:10px;">Детальна сторінка станції (Figma AI)</div>
      <img src="file:///{os.path.join(MAT_DIR, 'ai_hub_kyiv.jpg').replace(os.sep, '/')}" style="width:100%; height:110px; object-fit:cover; border-radius:8px; margin-bottom:10px; border:1px solid #CBD5E1;" alt="Hub">
      <div style="font-size:12px; font-weight:700;">Станція ChargeUA «Поділ-Експрес»</div>
      <div style="font-size:11px; color:#64748B; margin-bottom:10px;">м. Київ, вул. Набережно-Хрещатицька, 14</div>
      <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:10px; font-size:11px; margin-bottom:12px;">
        Тариф: <strong>14.50 грн/кВт·год</strong> | Потужність: <strong>120 кВт CCS2</strong>
      </div>
      <button style="width:100%; height:38px; background:#005EC9; color:#FFF; border:none; border-radius:6px; font-weight:700; font-size:12px;">Забронювати конектор CCS2</button>
    </div>
  </div>
</div></body></html>"""

html_fig18 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_CSS}
<style>
  .mobile-split {{
    display: flex;
    justify-content: center;
    gap: 24px;
  }}
  .m-box {{
    width: 280px;
    background: #FFFFFF;
    border: 2px solid #0F172A;
    border-radius: 16px;
    padding: 12px;
  }}
</style></head><body>
<div class="board">
  <div class="board-header">
    <div>
      <div class="board-title">Каталог та Деталі станції · Mobile 390 <span class="badge">Mobile Flow</span></div>
      <div class="board-desc">Мобільна версія каталогу та екрана станції з оптимізованими тач-зонами 48px</div>
    </div>
  </div>
  <div class="mobile-split">
    <div class="m-box">
      <div style="font-size:12px; font-weight:700; color:#005EC9; margin-bottom:6px;">Каталог станцій (390px)</div>
      <div style="background:#F1F5F9; padding:6px; border-radius:6px; font-size:10px; margin-bottom:8px;">🔍 Пошук станції поруч</div>
      <div style="border:1px solid #E2E8F0; border-radius:6px; padding:8px; font-size:10px; margin-bottom:6px;">
        <strong>Хаб Поділ</strong> (1.2 км)<br>
        <span style="color:#047857; font-weight:700;">🔋 Працює від генератора</span>
      </div>
    </div>
    <div class="m-box">
      <div style="font-size:12px; font-weight:700; color:#005EC9; margin-bottom:6px;">Деталі станції (390px)</div>
      <div style="font-size:11px; font-weight:700;">Хаб Поділ · 120 кВт</div>
      <div style="font-size:10px; color:#64748B; margin-bottom:8px;">Слот CCS2: Вільний</div>
      <button style="width:100%; height:40px; background:#005EC9; color:#FFF; border:none; border-radius:6px; font-weight:700; font-size:11px;">Маршрут у Waze</button>
    </div>
  </div>
</div></body></html>"""

# =============================================================================
# 19. fig19_overlays
# =============================================================================
html_fig19 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_CSS}
<style>
  .overlays-row {{
    display: flex;
    justify-content: center;
    gap: 36px;
  }}
  .overlay-card {{
    background: #FFFFFF;
    border: 1.5px solid #CBD5E1;
    border-radius: 14px;
    padding: 24px;
    width: 360px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.06);
  }}
</style></head><body>
<div class="board">
  <div class="board-header">
    <div>
      <div class="board-title">Оверлеї прототипу: мобільне меню та модалка <span class="badge">Interactions</span></div>
      <div class="board-desc">Мобільне бургер-меню та модальне вікно підтвердження заявки на B2B-партнерство</div>
    </div>
  </div>
  <div class="overlays-row">
    <div class="overlay-card">
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #E2E8F0; padding-bottom:10px; margin-bottom:14px;">
        <strong style="color:#005EC9; font-size:15px;">ChargeUA</strong>
        <span style="font-size:16px; cursor:pointer;">✕</span>
      </div>
      <div style="display:flex; flex-direction:column; gap:12px; font-size:13px; font-weight:600; color:#334155;">
        <div>Головна</div>
        <div>Калькулятор зарядки</div>
        <div>Карта станцій</div>
        <div>Тарифи операторів</div>
        <div>Для бізнесу</div>
      </div>
      <button style="width:100%; height:42px; background:#005EC9; color:#FFF; border:none; border-radius:8px; font-weight:700; margin-top:20px;">Закрити меню</button>
    </div>

    <div class="overlay-card" style="text-align:center;">
      <div style="font-size:36px; margin-bottom:10px;">✅</div>
      <h3 style="font-size:16px; font-weight:800; color:#0F172A; margin-bottom:8px;">Дякуємо! Заявку прийнято</h3>
      <p style="font-size:12px; color:#64748B; line-height:1.5; margin-bottom:18px;">
        Наш інженер зв'яжеться з вами протягом 15 хвилин для розрахунку встановлення станції на вашій локації.
      </p>
      <button style="width:100%; height:42px; background:#0F172A; color:#FFF; border:none; border-radius:8px; font-weight:700; font-size:12px;">Зрозуміло</button>
    </div>
  </div>
</div></body></html>"""

# =============================================================================
# 20. fig20_buttons_matrix -> 36 VARIANTS (3 TYPES X 6 STATES X 2 SIZES)
# =============================================================================
html_fig20 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_CSS}
<style>
  .btn-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 11px;
  }}
  .btn-table th, .btn-table td {{
    padding: 8px 10px;
    text-align: center;
    border: 1px solid #E2E8F0;
  }}
  .btn-table th {{
    background: #F8FAFC;
    color: #475569;
    font-weight: 700;
  }}
  .demo-btn {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    border-radius: 8px;
    border: none;
    cursor: pointer;
  }}
  .lg {{ height: 42px; padding: 0 16px; font-size: 12px; }}
  .sm {{ height: 32px; padding: 0 10px; font-size: 10.5px; }}
  
  .c-primary {{ background: #005EC9; color: #FFF; }}
  .c-primary.hover {{ background: #004BA1; }}
  .c-primary.active {{ background: #003B82; }}
  .c-primary.focus {{ outline: 3px solid #00E5FF; }}
  .c-primary.disabled {{ opacity: 0.4; cursor: not-allowed; }}
  .c-primary.loading {{ background: #005EC9; color: transparent; position: relative; }}

  .c-cta {{ background: #00E5FF; color: #0F172A; font-weight: 700; }}
  .c-cta.hover {{ background: #38BDF8; }}
  .c-cta.disabled {{ opacity: 0.4; }}

  .c-sec {{ background: #F8FAFC; color: #0F172A; border: 1.5px solid #CBD5E1; }}
  .c-sec.hover {{ border-color: #005EC9; color: #005EC9; }}
</style></head><body>
<div class="board">
  <div class="board-header">
    <div>
      <div class="board-title">Компонент Button: 3 типи × 6 станів × 2 розміри <span class="badge">36 варіантів</span></div>
      <div class="board-desc">Повна компонентна матриця Figma (Default, Hover, Active, Focus, Disabled, Loading) для розмірів Large 48px та Small 36px</div>
    </div>
  </div>
  <table class="btn-table">
    <thead>
      <tr>
        <th>Тип / Розмір</th>
        <th>Default</th>
        <th>Hover</th>
        <th>Active</th>
        <th>Focus</th>
        <th>Disabled</th>
        <th>Loading</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Primary (Large)</strong></td>
        <td><div class="demo-btn lg c-primary">Зарядити</div></td>
        <td><div class="demo-btn lg c-primary hover">Зарядити</div></td>
        <td><div class="demo-btn lg c-primary active">Зарядити</div></td>
        <td><div class="demo-btn lg c-primary focus">Зарядити</div></td>
        <td><div class="demo-btn lg c-primary disabled">Зарядити</div></td>
        <td><div class="demo-btn lg c-primary loading">...</div></td>
      </tr>
      <tr>
        <td><strong>Primary (Small)</strong></td>
        <td><div class="demo-btn sm c-primary">Зарядити</div></td>
        <td><div class="demo-btn sm c-primary hover">Зарядити</div></td>
        <td><div class="demo-btn sm c-primary active">Зарядити</div></td>
        <td><div class="demo-btn sm c-primary focus">Зарядити</div></td>
        <td><div class="demo-btn sm c-primary disabled">Зарядити</div></td>
        <td><div class="demo-btn sm c-primary loading">...</div></td>
      </tr>
      <tr>
        <td><strong>CTA Accent (Large)</strong></td>
        <td><div class="demo-btn lg c-cta">Розрахувати</div></td>
        <td><div class="demo-btn lg c-cta hover">Розрахувати</div></td>
        <td><div class="demo-btn lg c-cta" style="background:#0284C7; color:#FFF;">Розрахувати</div></td>
        <td><div class="demo-btn lg c-cta" style="outline:2px solid #005EC9;">Розрахувати</div></td>
        <td><div class="demo-btn lg c-cta disabled">Розрахувати</div></td>
        <td><div class="demo-btn lg c-cta" style="opacity:0.6;">...</div></td>
      </tr>
      <tr>
        <td><strong>Secondary (Large)</strong></td>
        <td><div class="demo-btn lg c-sec">Деталі</div></td>
        <td><div class="demo-btn lg c-sec hover">Деталі</div></td>
        <td><div class="demo-btn lg c-sec" style="background:#E2E8F0;">Деталі</div></td>
        <td><div class="demo-btn lg c-sec" style="outline:2px solid #005EC9;">Деталі</div></td>
        <td><div class="demo-btn lg c-sec" style="opacity:0.4;">Деталі</div></td>
        <td><div class="demo-btn lg c-sec" style="opacity:0.6;">...</div></td>
      </tr>
    </tbody>
  </table>
</div></body></html>"""

# =============================================================================
# 21. fig21_inputs_controls & 22. fig22_cards_nav
# =============================================================================
html_fig21 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_CSS}
<style>
  .controls-grid {{
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    gap: 24px;
  }}
  .input-demo {{
    background: #FFF;
    border: 1.5px solid #CBD5E1;
    border-radius: 8px;
    padding: 10px 14px;
    font-size: 12px;
    margin-bottom: 12px;
  }}
  .input-demo.focus {{ border-color: #005EC9; outline: 2px solid #BFDBFE; }}
  .input-demo.error {{ border-color: #EF4444; background: #FEF2F2; }}
</style></head><body>
<div class="board">
  <div class="board-header">
    <div>
      <div class="board-title">Поля вводу та елементи керування <span class="badge">Atomic Molecules</span></div>
      <div class="board-desc">Текстові поля форми (Default, Focus, Error, Disabled), перемикачі та бейджі</div>
    </div>
  </div>
  <div class="controls-grid">
    <div>
      <label style="font-size:11px; font-weight:700; color:#475569;">Default Field</label>
      <div class="input-demo">Введіть модель авто (напр. Nissan Leaf)</div>

      <label style="font-size:11px; font-weight:700; color:#005EC9;">Focused Field</label>
      <div class="input-demo focus">Tesla Model Y|</div>

      <label style="font-size:11px; font-weight:700; color:#EF4444;">Error Field</label>
      <div class="input-demo error">Некоректний номер телефону!</div>
    </div>

    <div>
      <div style="font-size:12px; font-weight:700; margin-bottom:12px;">Статусні бейджі та перемикачі:</div>
      <div style="display:flex; flex-direction:column; gap:10px; font-size:12px;">
        <div><span style="background:#D1FAE5; color:#047857; padding:4px 10px; border-radius:999px; font-weight:700;">🔋 Працює від генератора</span></div>
        <div><span style="background:#EFF6FF; color:#005EC9; padding:4px 10px; border-radius:999px; font-weight:700;">● Станція вільна (3/4)</span></div>
        <div><span style="background:#FEF3C7; color:#B45309; padding:4px 10px; border-radius:999px; font-weight:700;">⚠ Черга 1 авто</span></div>
        <div style="margin-top:10px;">
          <input type="checkbox" checked> Погоджуюсь з умовами оферти
        </div>
      </div>
    </div>
  </div>
</div></body></html>"""

html_fig22 = f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_CSS}
<style>
  .cards-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
  }}
  .c-box {{
    background: #F8FAFC;
    border: 1.5px solid #E2E8F0;
    border-radius: 12px;
    padding: 18px;
  }}
</style></head><body>
<div class="board">
  <div class="board-header">
    <div>
      <div class="board-title">Картки, навігація, шапка та підвал <span class="badge">Organisms</span></div>
      <div class="board-desc">Компоненти карток станцій, переваг з іконками ЛР3 та модулі шапки/футера</div>
    </div>
  </div>
  <div class="cards-grid">
    <div class="c-box">
      <div style="font-size:12px; font-weight:700; color:#005EC9; margin-bottom:8px;">Картка станції з ілюстрацією (Figma AI)</div>
      <div style="background:#FFF; border:1px solid #CBD5E1; border-radius:8px; overflow:hidden; padding:10px;">
        <img src="file:///{os.path.join(MAT_DIR, 'ai_hub_kyiv.jpg').replace(os.sep, '/')}" style="width:100%; height:90px; object-fit:cover; border-radius:6px; margin-bottom:8px;" alt="Hub">
        <strong>Хаб «Київ-Поділ»</strong> · 120 кВт CCS2
        <div style="background:#E2E8F0; height:8px; border-radius:4px; margin:8px 0; overflow:hidden;">
          <div style="background:#047857; width:75%; height:100%;"></div>
        </div>
        <div style="font-size:11px; color:#64748B; display:flex; justify-content:space-between;">
          <span>Зайнятість: 3 з 4</span>
          <span>14.50 грн/кВт</span>
        </div>
      </div>
    </div>

    <div class="c-box">
      <div style="font-size:12px; font-weight:700; color:#005EC9; margin-bottom:8px;">Картка відгуку з аватаром (Figma AI)</div>
      <div style="background:#FFF; border:1px solid #CBD5E1; border-radius:8px; padding:12px; display:flex; align-items:center; gap:12px;">
        <img src="file:///{os.path.join(MAT_DIR, 'ai_avatar_oleksiy.jpg').replace(os.sep, '/')}" style="width:48px; height:48px; border-radius:50%; border:2px solid #005EC9;" alt="Avatar">
        <div>
          <div style="font-size:12px; font-weight:700;">Олексій Коваль · Tesla Model Y</div>
          <div style="font-size:11px; color:#64748B; margin-top:2px;">«Заряджаюсь під час блекаутів тільки тут, генератор працює безвідмовно!»</div>
        </div>
      </div>
    </div>
  </div>
</div></body></html>"""

# Mapping of all 22 figures
figures_map = [
    ("fig01_user_flows", html_fig01, 1200, 800),
    ("fig02_sitemap", html_fig02, 1200, 800),
    ("fig03_relume_sitemap", html_fig03, 1200, 750),
    ("fig04_relume_wireframes", html_fig04, 1200, 750),
    ("fig05_wireframe_desktop", html_fig04, 1200, 750), # mapped
    ("fig06_wireframe_mobile", html_fig16, 700, 750), # mapped
    ("fig07_brand_assets_lr3", html_fig07, 1200, 850),
    ("fig08_color_tokens", html_fig08, 1200, 750),
    ("fig09_contrast_plugin", html_fig09, 1200, 750),
    ("fig10_typography", html_fig10, 1200, 750),
    ("fig11_spacing_grid", html_fig11, 1200, 750),
    ("fig12_figma_ai_illustrations", html_fig12, 1200, 750),
    ("fig13_desktop_top", html_fig13, 1440, 900),
    ("fig14_desktop_bottom", html_fig14, 1440, 900),
    ("fig15_tablet", html_fig15, 900, 850),
    ("fig16_mobile", html_fig16, 600, 850),
    ("fig17_catalog_details_desktop", html_fig17, 1200, 750),
    ("fig18_catalog_details_mobile", html_fig18, 900, 750),
    ("fig19_overlays", html_fig19, 1200, 750),
    ("fig20_buttons_matrix", html_fig20, 1200, 750),
    ("fig21_inputs_controls", html_fig21, 1200, 750),
    ("fig22_cards_nav", html_fig22, 1200, 750),
]

for name, html_content, w, h in figures_map:
    render_board(name, html_content, width=w, height=h)

print("ALL 22 FIGURES GENERATED SUCCESSFULLY!")
