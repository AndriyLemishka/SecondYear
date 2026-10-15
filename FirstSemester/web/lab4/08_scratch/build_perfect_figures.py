# -*- coding: utf-8 -*-
"""
Full implementation of perfect figure generation matching student reference (ReadSpace, Кобрак Ярослав).
"""

import os, subprocess
from PIL import Image

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
  body {{ background: #FFFFFF; color: #0F172A; -webkit-font-smoothing: antialiased; }}
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

# ==============================================================================
# 1. FIG 13 & FIG 14: DESKTOP 1440 (TOP & BOTTOM)
# ==============================================================================

html_fig13 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ width: 1440px; background: #FFFFFF; }}
  .top-strip {{ background: #0F172A; color: #E2E8F0; padding: 10px 60px; display: flex; justify-content: space-between; font-size: 13px; font-weight: 500; }}
  .navbar {{ height: 76px; padding: 0 60px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #E2E8F0; }}
  .nav-links {{ display: flex; gap: 32px; font-size: 15px; font-weight: 600; color: #334155; }}
  .nav-btn {{ padding: 10px 22px; border-radius: 8px; font-size: 14px; font-weight: 700; cursor: pointer; }}
  .btn-outline {{ border: 1.5px solid #E2E8F0; background: #FFF; color: #0F172A; }}
  .btn-primary {{ background: #005EC9; color: #FFF; border: none; }}

  .hero-sec {{ padding: 60px 60px 40px; display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; position: relative; }}
  .badge-hero {{ display: inline-flex; align-items: center; gap: 6px; padding: 6px 14px; border-radius: 20px; background: #EFF6FF; color: #005EC9; font-size: 12px; font-weight: 700; margin-bottom: 18px; }}
  .hero-h1 {{ font-size: 44px; font-weight: 800; line-height: 1.2; color: #0F172A; margin-bottom: 18px; }}
  .hero-p {{ font-size: 16px; line-height: 1.6; color: #64748B; margin-bottom: 28px; }}
  .hero-btns {{ display: flex; gap: 16px; margin-bottom: 30px; }}
  .hero-chips {{ display: flex; gap: 10px; font-size: 13px; align-items: center; color: #64748B; }}
  .chip {{ padding: 6px 14px; border-radius: 20px; border: 1px solid #CBD5E1; font-weight: 600; color: #1E293B; }}
  .chip-green {{ background: #D1FAE5; border-color: #34D399; color: #065F46; font-weight: 700; }}
  .hero-img {{ width: 100%; border-radius: 18px; object-fit: cover; box-shadow: 0 10px 30px rgba(0,94,201,0.08); }}

  .features-strip {{ padding: 20px 60px 50px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }}
  .feat-card {{ background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 14px; padding: 22px; display: flex; gap: 18px; align-items: center; }}
  .feat-icon {{ width: 48px; height: 48px; flex-shrink: 0; }}

  .calc-sec {{ padding: 10px 60px 60px; }}
  .calc-box {{ background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 18px; padding: 36px; box-shadow: 0 4px 20px rgba(0,0,0,0.04); display: grid; grid-template-columns: 1.2fr 1fr; gap: 40px; }}
  .model-pills {{ display: flex; gap: 10px; margin: 16px 0 24px; }}
  .pill {{ padding: 10px 18px; border-radius: 8px; border: 1.5px solid #CBD5E1; font-size: 14px; font-weight: 600; cursor: pointer; }}
  .pill.active {{ background: #005EC9; color: #FFF; border-color: #005EC9; }}
  .slider-bar {{ height: 10px; background: #E2E8F0; border-radius: 5px; position: relative; margin: 20px 0 10px; }}
  .slider-fill {{ width: 75%; height: 100%; background: #005EC9; border-radius: 5px; }}
  .calc-res-card {{ background: #F8FAFC; border: 1.5px solid #005EC9; border-radius: 14px; padding: 28px; display: flex; flex-direction: column; justify-content: space-between; }}
  .res-price {{ font-size: 34px; font-weight: 800; color: #0F172A; margin: 8px 0 14px; }}
  .btn-calc {{ background: #005EC9; color: #FFF; padding: 14px; border-radius: 10px; border: none; font-size: 15px; font-weight: 700; width: 100%; cursor: pointer; }}
</style></head><body>
  <div class="top-strip">
    <div>● Мережа ChargeUA: 480+ станцій онлайн по Україні | 100% телеметрія в реальному часі</div>
    <div>Гаряча лінія 24/7: 0 800 300 400 | UA</div>
  </div>
  <div class="navbar">
    <div style="display:flex; align-items:center; gap:12px;">
      <img src="{LOGO_URL}" style="width:38px; height:38px;">
      <span style="font-size:24px; font-weight:800; color:#005EC9;">ChargeUA</span>
    </div>
    <div class="nav-links">
      <span style="color:#005EC9;">Головна</span>
      <span>Калькулятор</span>
      <span>Карта станцій</span>
      <span>Тарифи</span>
      <span>Для бізнесу</span>
    </div>
    <div style="display:flex; gap:12px;">
      <button class="nav-btn btn-outline">Увійти</button>
      <button class="nav-btn btn-primary">Завантажити додаток</button>
    </div>
  </div>

  <div class="hero-sec">
    <div>
      <div class="badge-hero">⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР ЗАРЯДНИХ СТАНЦІЙ</div>
      <h1 class="hero-h1">Швидка та надійна зарядка електромобілів по всій Україні</h1>
      <p class="hero-p">Знаходьте найближчі станції, розраховуйте вартість за лічені секунди та подорожуйте без хвилювань навіть під час блекаутів.</p>
      <div class="hero-btns">
        <button class="nav-btn btn-primary" style="padding:14px 28px; font-size:15px;">Розрахувати зарядку →</button>
        <button class="nav-btn btn-outline" style="padding:14px 28px; font-size:15px;">Знайти на карті</button>
      </div>
      <div class="hero-chips">
        <span>Популярні конектори:</span>
        <span class="chip">Type 2 (22 кВт)</span>
        <span class="chip">CCS 2 (160 кВт)</span>
        <span class="chip chip-green">🔋 З генератором</span>
      </div>
    </div>
    <div>
      <img src="{HERO_URL}" class="hero-img">
    </div>
  </div>

  <div class="features-strip">
    <div class="feat-card">
      <img src="{CALC_URL}" class="feat-icon">
      <div>
        <div style="font-weight:700; font-size:15px; margin-bottom:4px;">Точний калькулятор витрат</div>
        <div style="font-size:13px; color:#64748B;">Автоматичний підбір моделі авто та тарифу</div>
      </div>
    </div>
    <div class="feat-card">
      <img src="{LOC_URL}" class="feat-icon">
      <div>
        <div style="font-weight:700; font-size:15px; margin-bottom:4px;">Live-карта 480+ станцій</div>
        <div style="font-size:13px; color:#64748B;">Актуальний статус зайнятості та світла онлайн</div>
      </div>
    </div>
    <div class="feat-card">
      <img src="{INFO_URL}" class="feat-icon">
      <div>
        <div style="font-weight:700; font-size:15px; margin-bottom:4px;">100% Енергонезалежність</div>
        <div style="font-size:13px; color:#64748B;">Робота від потужних генераторів у блекаути</div>
      </div>
    </div>
  </div>

  <div class="calc-sec">
    <div style="margin-bottom:20px;">
      <h2 style="font-size:28px; font-weight:800; color:#0F172A;">Інтерактивний калькулятор зарядки ChargeUA</h2>
      <p style="font-size:15px; color:#64748B; margin-top:4px;">Оберіть модель електрокара та розрахуйте тривалість сесії й вартість</p>
    </div>
    <div class="calc-box">
      <div>
        <div style="font-weight:700; font-size:14px;">Модель автомобіля:</div>
        <div class="model-pills">
          <div class="pill active">Volkswagen ID.4 (77 кВт·год)</div>
          <div class="pill">Tesla Model Y</div>
          <div class="pill">Nissan Leaf</div>
        </div>
        <div style="font-weight:700; font-size:14px; margin-top:20px;">Рівень заряду батареї (20% → 80%):</div>
        <div class="slider-bar"><div class="slider-fill"></div></div>
        <div style="display:flex; justify-content:space-between; font-size:12px; color:#64748B;">
          <span>20% (15.4 кВт·год)</span>
          <span>80% (61.6 кВт·год)</span>
        </div>
      </div>
      <div class="calc-res-card">
        <div>
          <div style="font-size:13px; color:#64748B; font-weight:600;">Орієнтовна вартість сесії:</div>
          <div class="res-price">652.50 ₴ <span style="font-size:15px; font-weight:500; color:#64748B;">(14.50 ₴/кВт·год)</span></div>
          <div style="font-size:13px; font-weight:700; color:#005EC9; margin-bottom:6px;">● Час на 120 кВт DC: ~28 хв | Економія vs Бензин: ~1 420 ₴</div>
        </div>
        <button class="btn-calc">Знайти найближчу вільну станцію</button>
      </div>
    </div>
  </div>
</body></html>"""

html_fig14 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ width: 1440px; background: #FFFFFF; }}
  .sec-gen {{ padding: 30px 60px 40px; }}
  .banner-box {{ background: #0F172A; border-radius: 20px; padding: 40px 50px; display: grid; grid-template-columns: 1.1fr 1fr; gap: 40px; align-items: center; color: #FFF; }}
  .gen-h2 {{ font-size: 32px; font-weight: 800; line-height: 1.25; margin-bottom: 14px; }}
  .gen-p {{ font-size: 15px; line-height: 1.6; color: #CBD5E1; margin-bottom: 24px; }}
  .btn-gen {{ background: #00E5FF; color: #0F172A; border: none; padding: 13px 26px; border-radius: 8px; font-size: 14px; font-weight: 800; cursor: pointer; }}

  .hubs-sec {{ padding: 20px 60px 40px; }}
  .hubs-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 20px; }}
  .hub-card {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 16px; overflow: hidden; }}
  .hub-img {{ width: 100%; height: 180px; object-fit: cover; }}
  .hub-body {{ padding: 18px; }}
  .hub-title {{ font-size: 16px; font-weight: 800; color: #0F172A; }}
  .hub-addr {{ font-size: 13px; color: #64748B; margin: 4px 0 12px; }}
  .badge-status {{ display: inline-block; padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: 700; margin-bottom: 14px; }}
  .badge-green {{ background: #D1FAE5; color: #065F46; }}
  .btn-route {{ width: 100%; background: #005EC9; color: #FFF; border: none; padding: 11px; border-radius: 8px; font-size: 13px; font-weight: 700; cursor: pointer; }}

  .reviews-sec {{ padding: 20px 60px 40px; }}
  .rev-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 20px; }}
  .rev-card {{ background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 14px; padding: 22px; display: flex; flex-direction: column; justify-content: space-between; }}
  .stars {{ color: #F59E0B; font-size: 16px; margin-bottom: 10px; }}
  .rev-text {{ font-size: 13px; line-height: 1.5; color: #334155; margin-bottom: 18px; }}
  .rev-author {{ display: flex; align-items: center; gap: 12px; }}
  .rev-avatar {{ width: 44px; height: 44px; border-radius: 50%; object-fit: cover; }}

  .form-sec {{ padding: 20px 60px 50px; }}
  .form-box {{ background: #F8FAFC; border: 1.5px solid #E2E8F0; border-radius: 18px; padding: 36px 44px; }}
  .form-row {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin: 20px 0 24px; }}
  .form-input {{ width: 100%; height: 46px; border: 1.5px solid #CBD5E1; border-radius: 8px; padding: 0 14px; font-size: 14px; background: #FFF; }}

  .footer {{ background: #0F172A; color: #FFF; padding: 50px 60px 30px; }}
  .footer-grid {{ display: grid; grid-template-columns: 1.4fr 1fr 1fr 1fr; gap: 40px; margin-bottom: 40px; }}
  .f-col-title {{ font-size: 15px; font-weight: 700; margin-bottom: 16px; color: #FFF; }}
  .f-col-links {{ display: flex; flex-direction: column; gap: 10px; font-size: 13px; color: #94A3B8; }}
  .f-bottom {{ border-top: 1px solid #1E293B; padding-top: 24px; display: flex; justify-content: space-between; font-size: 12px; color: #64748B; }}
</style></head><body>
  <div class="sec-gen">
    <div class="banner-box">
      <div>
        <div style="font-size:12px; font-weight:800; color:#00E5FF; margin-bottom:10px;">ЕНЕРГОНЕЗАЛЕЖНІСТЬ 24/7</div>
        <h2 class="gen-h2">Заряджайте авто навіть під час повних блекаутів</h2>
        <p class="gen-p">Ключові хаби ChargeUA обладнано промисловими дизель-генераторами 160–250 кВт. Автоматичний перехід на резервне живлення за 8 секунд гарантує 100% Uptime зарядної мережі.</p>
        <button class="btn-gen">Показати станції зі світлом</button>
      </div>
      <div>
        <img src="{GEN_URL}" style="width:100%; border-radius:14px; object-fit:cover;">
      </div>
    </div>
  </div>

  <div class="hubs-sec">
    <h2 style="font-size:26px; font-weight:800;">Популярні зарядні хаби мережі</h2>
    <p style="font-size:14px; color:#64748B; margin-top:4px;">Швидкісні станції з гарантованим живленням та живою телеметрією</p>
    <div class="hubs-grid">
      <div class="hub-card">
        <img src="{HUB_KYIV_URL}" class="hub-img">
        <div class="hub-body">
          <div class="hub-title">Хаб «Київ-Поділ» · 120 кВт CCS2</div>
          <div class="hub-addr">м. Київ, вул. Сагайдачного, 12</div>
          <div class="badge-status badge-green">🔋 Генератор ON · Вільний (3/4)</div>
          <button class="btn-route">Прокласти маршрут (Waze / Maps)</button>
        </div>
      </div>
      <div class="hub-card">
        <img src="{HUB_LVIV_URL}" class="hub-img">
        <div class="hub-body">
          <div class="hub-title">Хаб «Арена Львів» · 160 кВт CCS2</div>
          <div class="hub-addr">м. Львів, вул. Стрийська, 199</div>
          <div class="badge-status badge-green">🔋 Сонячний навіс + Дизель</div>
          <button class="btn-route">Прокласти маршрут (Waze / Maps)</button>
        </div>
      </div>
      <div class="hub-card">
        <img src="{VIDEO_URL}" class="hub-img">
        <div class="hub-body">
          <div class="hub-title">Відеогайд: як зарядитися за 3 кроки</div>
          <div class="hub-addr">Покрокова інструкція підключення кабелю CCS2</div>
          <div class="badge-status" style="background:#EFF6FF; color:#005EC9;">▶ Відеоінструкція (0:45)</div>
          <button class="btn-route" style="background:#F1F5F9; color:#0F172A; border:1px solid #CBD5E1;">Переглянути відеодемо</button>
        </div>
      </div>
    </div>
  </div>

  <div class="reviews-sec">
    <h2 style="font-size:26px; font-weight:800;">Відгуки реальних водіїв</h2>
    <p style="font-size:14px; color:#64748B; margin-top:4px;">Що кажуть власники електрокарів про сервіс ChargeUA</p>
    <div class="rev-grid">
      <div class="rev-card">
        <div>
          <div class="stars">★★★★★</div>
          <div class="rev-text">«Під час блекауту на Подолі зарядився за 25 хвилин. Генератор гуде, станція стабільна, кава поруч. Найкращий сервіс!»</div>
        </div>
        <div class="rev-author">
          <img src="{AV1_URL}" class="rev-avatar">
          <div>
            <div style="font-size:14px; font-weight:700;">Олексій К.</div>
            <div style="font-size:12px; color:#64748B;">Водій Tesla Model Y · Київ</div>
          </div>
        </div>
      </div>
      <div class="rev-card">
        <div>
          <div class="stars">★★★★★</div>
          <div class="rev-text">«Дуже зручний калькулятор. Одразу видно скільки кіловат потрібно і яка буде фінальна вартість без прихованих платежів.»</div>
        </div>
        <div class="rev-author">
          <img src="{AV2_URL}" class="rev-avatar">
          <div>
            <div style="font-size:14px; font-weight:700;">Олена М.</div>
            <div style="font-size:12px; color:#64748B;">Водійка Nissan Leaf · Львів</div>
          </div>
        </div>
      </div>
      <div class="rev-card">
        <div>
          <div class="stars">★★★★★</div>
          <div class="rev-text">«Для комерційного автопарку зручний моніторинг вільних станцій — це знахідка. Жодних простоїв та черг на трасі Київ-Львів.»</div>
        </div>
        <div class="rev-author">
          <img src="{AV3_URL}" class="rev-avatar">
          <div>
            <div style="font-size:14px; font-weight:700;">Сергій В.</div>
            <div style="font-size:12px; color:#64748B;">Керівник автопарку електробусів</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="form-sec">
    <div class="form-box">
      <h3 style="font-size:22px; font-weight:800; color:#0F172A;">Маєте локацію? Встановіть станцію ChargeUA</h3>
      <p style="font-size:14px; color:#64748B; margin-top:4px;">Отримуйте стабільний пасивний дохід від зарядки авто ваших клієнтів</p>
      <div class="form-row">
        <input type="text" placeholder="Ваше ім'я" class="form-input">
        <input type="text" placeholder="Номер телефону (+380...)" class="form-input">
        <input type="text" placeholder="Місто та адреса об'єкта" class="form-input">
      </div>
      <button class="nav-btn btn-primary" style="padding:14px 32px; font-size:14px;">Подати заявку на монтаж</button>
    </div>
  </div>

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
          <span>Тарифи</span>
        </div>
      </div>
      <div>
        <div class="f-col-title">Для бізнесу</div>
        <div class="f-col-links">
          <span>Встановити хаб</span>
          <span>B2B-калькулятор</span>
          <span>Партнерство</span>
          <span>Резервне живлення</span>
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
</body></html>"""

# Write HTML for Fig 13 & 14
with open(os.path.join(HTML_DIR, "fig13_desktop_top.html"), "w", encoding="utf-8") as f:
    f.write(html_fig13)
with open(os.path.join(HTML_DIR, "fig14_desktop_bottom.html"), "w", encoding="utf-8") as f:
    f.write(html_fig14)

print("Fig 13 & 14 HTML generated.")

# ==============================================================================
# 2. FIG 15: TABLET 768 (SEAMLESS 3-COLUMN VERTICAL SLICE)
# ==============================================================================

html_tablet_full = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ width: 768px; background: #FFFFFF; border: 1px solid #E2E8F0; }}
  .top-strip {{ background: #0F172A; color: #E2E8F0; padding: 8px 24px; display: flex; justify-content: space-between; font-size: 11px; font-weight: 500; }}
  .navbar {{ height: 64px; padding: 0 24px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #E2E8F0; }}
  .hero-sec {{ padding: 32px 24px 20px; }}
  .hero-h1 {{ font-size: 32px; font-weight: 800; line-height: 1.25; color: #0F172A; margin-bottom: 12px; }}
  .hero-p {{ font-size: 14px; line-height: 1.5; color: #64748B; margin-bottom: 20px; }}
  .hero-btns {{ display: flex; gap: 12px; margin-bottom: 20px; }}
  .nav-btn {{ padding: 10px 18px; border-radius: 8px; font-size: 13px; font-weight: 700; }}
  .btn-primary {{ background: #005EC9; color: #FFF; border: none; }}
  .btn-outline {{ border: 1.5px solid #CBD5E1; background: #FFF; color: #0F172A; }}
  .hero-chips {{ display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 24px; }}
  .chip {{ padding: 5px 12px; border-radius: 16px; border: 1px solid #CBD5E1; font-size: 12px; font-weight: 600; }}
  .hero-img {{ width: 100%; border-radius: 14px; object-fit: cover; }}

  .feat-sec {{ padding: 20px 24px; display: flex; flex-direction: column; gap: 12px; }}
  .feat-card {{ background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 14px 18px; display: flex; gap: 14px; align-items: center; }}
  .feat-icon {{ width: 36px; height: 36px; flex-shrink: 0; }}

  .calc-sec {{ padding: 24px; }}
  .calc-box {{ background: #F8FAFC; border: 1.5px solid #CBD5E1; border-radius: 16px; padding: 24px; }}
  .pills {{ display: flex; gap: 8px; margin: 12px 0 18px; }}
  .pill {{ padding: 8px 14px; border-radius: 8px; border: 1.5px solid #CBD5E1; font-size: 12px; font-weight: 700; background: #FFF; }}
  .pill.active {{ background: #005EC9; color: #FFF; border-color: #005EC9; }}
  .slider-bar {{ height: 8px; background: #E2E8F0; border-radius: 4px; margin: 16px 0 8px; }}
  .slider-fill {{ width: 75%; height: 100%; background: #005EC9; border-radius: 4px; }}
  .calc-res {{ background: #FFF; border: 1.5px solid #005EC9; border-radius: 12px; padding: 18px; margin-top: 18px; }}

  .gen-sec {{ padding: 24px; }}
  .gen-box {{ background: #0F172A; border-radius: 16px; padding: 28px; color: #FFF; }}
  .gen-img {{ width: 100%; border-radius: 12px; margin-top: 18px; object-fit: cover; }}

  .hubs-sec {{ padding: 24px; }}
  .hub-card {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 14px; overflow: hidden; margin-bottom: 18px; }}
  .hub-img {{ width: 100%; height: 180px; object-fit: cover; }}
  .hub-body {{ padding: 16px; }}

  .video-sec {{ padding: 24px; background: #F8FAFC; }}
  .steps-sec {{ padding: 24px; }}
  .step-row {{ display: flex; gap: 14px; margin-bottom: 16px; align-items: flex-start; }}
  .step-num {{ width: 32px; height: 32px; border-radius: 50%; background: #005EC9; color: #FFF; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 14px; flex-shrink: 0; }}

  .reviews-sec {{ padding: 24px; }}
  .rev-card {{ background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; }}

  .form-sec {{ padding: 24px; }}
  .form-box {{ background: #F8FAFC; border: 1.5px solid #E2E8F0; border-radius: 14px; padding: 22px; }}
  .form-input {{ width: 100%; height: 42px; border: 1.5px solid #CBD5E1; border-radius: 8px; padding: 0 12px; font-size: 13px; background: #FFF; margin-bottom: 12px; }}

  .footer {{ background: #0F172A; color: #FFF; padding: 36px 24px 24px; }}
</style></head><body>
  <div class="top-strip">
    <div>● Мережа ChargeUA: 480+ станцій онлайн</div>
    <div>0 800 300 400 | UA</div>
  </div>
  <div class="navbar">
    <div style="display:flex; align-items:center; gap:10px;">
      <img src="{LOGO_URL}" style="width:30px; height:30px;">
      <span style="font-size:20px; font-weight:800; color:#005EC9;">ChargeUA</span>
    </div>
    <div style="font-size:22px; font-weight:800; color:#0F172A;">☰</div>
  </div>

  <div class="hero-sec">
    <div style="font-size:11px; font-weight:800; color:#005EC9; margin-bottom:8px;">⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР</div>
    <h1 class="hero-h1">Швидка зарядка по всій Україні</h1>
    <p class="hero-p">Знаходьте вільну станцію навіть під час блекаутів із гарантованим резервним живленням.</p>
    <div class="hero-btns">
      <button class="nav-btn btn-primary">Розрахувати →</button>
      <button class="nav-btn btn-outline">Карта хабів</button>
    </div>
    <div class="hero-chips">
      <span class="chip">Type 2 (22 кВт)</span>
      <span class="chip">CCS 2 (160 кВт)</span>
      <span class="chip" style="background:#D1FAE5; color:#065F46; font-weight:700;">🔋 З генератором</span>
    </div>
    <img src="{HERO_URL}" class="hero-img">
  </div>

  <div class="feat-sec">
    <div class="feat-card">
      <img src="{CALC_URL}" class="feat-icon">
      <div>
        <div style="font-weight:700; font-size:14px;">Точний калькулятор витрат</div>
        <div style="font-size:12px; color:#64748B;">Автоматичний підбір моделі авто та тарифу</div>
      </div>
    </div>
    <div class="feat-card">
      <img src="{LOC_URL}" class="feat-icon">
      <div>
        <div style="font-weight:700; font-size:14px;">Live-карта 480+ станцій</div>
        <div style="font-size:12px; color:#64748B;">Актуальний статус зайнятості та світла онлайн</div>
      </div>
    </div>
    <div class="feat-card">
      <img src="{INFO_URL}" class="feat-icon">
      <div>
        <div style="font-weight:700; font-size:14px;">100% Енергонезалежність</div>
        <div style="font-size:12px; color:#64748B;">Робота від генераторів під час блекаутів</div>
      </div>
    </div>
  </div>

  <div class="calc-sec">
    <div class="calc-box">
      <h2 style="font-size:20px; font-weight:800;">Калькулятор зарядки</h2>
      <div class="pills">
        <div class="pill active">VW ID.4</div>
        <div class="pill">Tesla Model Y</div>
        <div class="pill">Nissan Leaf</div>
      </div>
      <div style="font-size:13px; font-weight:600;">Рівень батареї: 20% → 80%</div>
      <div class="slider-bar"><div class="slider-fill"></div></div>
      <div class="calc-res">
        <div style="font-size:24px; font-weight:800; color:#0F172A;">652.50 ₴</div>
        <div style="font-size:12px; font-weight:700; color:#005EC9; margin:4px 0 12px;">● Час на 120 кВт DC: ~28 хв | Економія: ~1 420 ₴</div>
        <button class="nav-btn btn-primary" style="width:100%;">Знайти найближчий хаб</button>
      </div>
    </div>
  </div>

  <div class="gen-sec">
    <div class="gen-box">
      <div style="font-size:11px; font-weight:800; color:#00E5FF; margin-bottom:8px;">ЕНЕРГОНЕЗАЛЕЖНІСТЬ 24/7</div>
      <h2 style="font-size:24px; font-weight:800; line-height:1.3;">Заряджайтеся у блекаути</h2>
      <p style="font-size:13px; color:#CBD5E1; line-height:1.5; margin-top:8px;">Дизель-генератори 160–250 кВт гарантують 100% працездатність мережі.</p>
      <img src="{GEN_URL}" class="gen-img">
    </div>
  </div>

  <div class="hubs-sec">
    <h2 style="font-size:22px; font-weight:800; margin-bottom:16px;">Популярні хаби</h2>
    <div class="hub-card">
      <img src="{HUB_KYIV_URL}" class="hub-img">
      <div class="hub-body">
        <div style="font-weight:800; font-size:15px;">Хаб «Київ-Поділ» · 120 кВт CCS2</div>
        <div style="font-size:12px; color:#64748B; margin:4px 0 10px;">вул. Сагайдачного, 12 · 14.50 ₴/кВт·год</div>
        <div style="font-size:11px; font-weight:700; color:#065F46; background:#D1FAE5; display:inline-block; padding:4px 8px; border-radius:6px; margin-bottom:10px;">🔋 Генератор ON · Вільний (3/4)</div>
        <button class="nav-btn btn-primary" style="width:100%;">Прокласти маршрут (Waze / Maps)</button>
      </div>
    </div>
    <div class="hub-card">
      <img src="{HUB_LVIV_URL}" class="hub-img">
      <div class="hub-body">
        <div style="font-weight:800; font-size:15px;">Хаб «Арена Львів» · 160 кВт CCS2</div>
        <div style="font-size:12px; color:#64748B; margin:4px 0 10px;">вул. Стрийська, 199 · 15.00 ₴/кВт·год</div>
        <div style="font-size:11px; font-weight:700; color:#065F46; background:#D1FAE5; display:inline-block; padding:4px 8px; border-radius:6px; margin-bottom:10px;">🔋 Сонячний навіс + Дизель</div>
        <button class="nav-btn btn-primary" style="width:100%;">Прокласти маршрут (Waze / Maps)</button>
      </div>
    </div>
  </div>

  <div class="video-sec">
    <h2 style="font-size:20px; font-weight:800; margin-bottom:12px;">Відеоінструкція</h2>
    <img src="{VIDEO_URL}" style="width:100%; border-radius:12px; object-fit:cover; margin-bottom:14px;">
    <p style="font-size:13px; color:#64748B;">Як підключити конектор CCS2 та розпочати зарядку за 3 кроки.</p>
  </div>

  <div class="steps-sec">
    <h2 style="font-size:20px; font-weight:800; margin-bottom:16px;">Як зарядитися за 3 кроки</h2>
    <div class="step-row">
      <div class="step-num">1</div>
      <div>
        <div style="font-weight:700; font-size:14px;">Знайдіть вільну станцію</div>
        <div style="font-size:12px; color:#64748B;">Фільтруйте за потужністю або генератором.</div>
      </div>
    </div>
    <div class="step-row">
      <div class="step-num">2</div>
      <div>
        <div style="font-weight:700; font-size:14px;">Підключіть конектор CCS2</div>
        <div style="font-size:12px; color:#64748B;">Вставте кабель у порт авто.</div>
      </div>
    </div>
    <div class="step-row">
      <div class="step-num">3</div>
      <div>
        <div style="font-weight:700; font-size:14px;">Оплатіть у 1 клік</div>
        <div style="font-size:12px; color:#64748B;">Apple Pay або Google Pay без переплат.</div>
      </div>
    </div>
  </div>

  <div class="reviews-sec">
    <h2 style="font-size:20px; font-weight:800; margin-bottom:14px;">Відгуки водіїв</h2>
    <div class="rev-card">
      <div style="color:#F59E0B; margin-bottom:6px;">★★★★★</div>
      <div style="font-size:12px; color:#334155; margin-bottom:10px;">«Під час блекауту на Подолі зарядився за 25 хв! Все супер!»</div>
      <div style="display:flex; align-items:center; gap:8px;">
        <img src="{AV1_URL}" style="width:32px; height:32px; border-radius:50%; object-fit:cover;">
        <span style="font-size:12px; font-weight:700;">Олексій (Tesla Y)</span>
      </div>
    </div>
    <div class="rev-card">
      <div style="color:#F59E0B; margin-bottom:6px;">★★★★★</div>
      <div style="font-size:12px; color:#334155; margin-bottom:10px;">«Калькулятор дуже виручає при плануванні поїздки.»</div>
      <div style="display:flex; align-items:center; gap:8px;">
        <img src="{AV2_URL}" style="width:32px; height:32px; border-radius:50%; object-fit:cover;">
        <span style="font-size:12px; font-weight:700;">Олена (Leaf)</span>
      </div>
    </div>
  </div>

  <div class="form-sec">
    <div class="form-box">
      <h3 style="font-size:18px; font-weight:800; margin-bottom:6px;">Маєте локацію?</h3>
      <p style="font-size:12px; color:#64748B; margin-bottom:14px;">Встановіть зарядну станцію ChargeUA</p>
      <input type="text" placeholder="Ваше ім'я" class="form-input">
      <input type="text" placeholder="Телефон (+380...)" class="form-input">
      <button class="nav-btn btn-primary" style="width:100%;">Подати заявку</button>
    </div>
  </div>

  <div class="footer">
    <div style="display:flex; align-items:center; gap:8px; margin-bottom:12px;">
      <img src="{LOGO_URL}" style="width:24px; height:24px; filter:brightness(0) invert(1);">
      <span style="font-size:18px; font-weight:800; color:#FFF;">ChargeUA</span>
    </div>
    <p style="font-size:12px; color:#94A3B8; margin-bottom:16px;">Агрегатор електрозарядок України.</p>
    <div style="font-size:11px; color:#64748B; border-top:1px solid #1E293B; padding-top:14px;">
      © 2026 ChargeUA · ПП-24 · САПР
    </div>
  </div>
</body></html>"""

with open(os.path.join(HTML_DIR, "tablet_full.html"), "w", encoding="utf-8") as f:
    f.write(html_tablet_full)

print("Tablet HTML generated.")

# ==============================================================================
# 3. FIG 16: MOBILE 390 (SEAMLESS 4-COLUMN VERTICAL SLICE)
# ==============================================================================

html_mobile_full = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ width: 390px; background: #FFFFFF; border: 1px solid #E2E8F0; padding-bottom: 60px; }}
  .top-strip {{ background: #0F172A; color: #E2E8F0; padding: 6px 16px; display: flex; justify-content: space-between; font-size: 10px; font-weight: 500; }}
  .navbar {{ height: 56px; padding: 0 16px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #E2E8F0; }}
  .hero-sec {{ padding: 22px 16px 16px; }}
  .hero-h1 {{ font-size: 24px; font-weight: 800; line-height: 1.25; color: #0F172A; margin-bottom: 10px; }}
  .hero-p {{ font-size: 13px; line-height: 1.5; color: #64748B; margin-bottom: 16px; }}
  .btn-primary {{ background: #005EC9; color: #FFF; border: none; padding: 11px 18px; border-radius: 8px; font-size: 13px; font-weight: 700; width: 100%; cursor: pointer; }}
  .hero-img {{ width: 100%; border-radius: 12px; margin-top: 14px; object-fit: cover; }}

  .calc-sec {{ padding: 16px; }}
  .calc-box {{ background: #F8FAFC; border: 1.5px solid #CBD5E1; border-radius: 14px; padding: 16px; }}
  .slider-bar {{ height: 6px; background: #E2E8F0; border-radius: 3px; margin: 12px 0 6px; }}
  .slider-fill {{ width: 75%; height: 100%; background: #005EC9; border-radius: 3px; }}

  .step-sec {{ padding: 16px; }}
  .cable-img {{ width: 100%; border-radius: 12px; margin-bottom: 12px; object-fit: cover; }}

  .gen-sec {{ padding: 16px; }}
  .gen-box {{ background: #0F172A; border-radius: 14px; padding: 18px; color: #FFF; }}
  .gen-img {{ width: 100%; border-radius: 10px; margin-top: 12px; object-fit: cover; }}

  .hubs-sec {{ padding: 16px; }}
  .hub-card {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 12px; overflow: hidden; margin-bottom: 14px; }}
  .hub-img {{ width: 100%; height: 150px; object-fit: cover; }}
  .hub-body {{ padding: 14px; }}

  .reviews-sec {{ padding: 16px; }}
  .rev-card {{ background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; padding: 12px; margin-bottom: 10px; }}

  .footer {{ background: #0F172A; color: #FFF; padding: 24px 16px 18px; }}
  .bottom-nav {{ position: fixed; bottom: 0; left: 0; width: 390px; height: 54px; background: #FFF; border-top: 1px solid #E2E8F0; display: flex; justify-content: space-around; align-items: center; font-size: 10px; font-weight: 700; color: #64748B; z-index: 99; }}
  .nav-item.active {{ color: #005EC9; }}
</style></head><body>
  <div class="top-strip">
    <div>● 480+ станцій онлайн | Генератори ON</div>
    <div>UA</div>
  </div>
  <div class="navbar">
    <div style="display:flex; align-items:center; gap:8px;">
      <img src="{LOGO_URL}" style="width:26px; height:26px;">
      <span style="font-size:18px; font-weight:800; color:#005EC9;">ChargeUA</span>
    </div>
    <div style="font-size:20px; font-weight:800;">☰</div>
  </div>

  <div class="hero-sec">
    <div style="font-size:10px; font-weight:800; color:#005EC9; margin-bottom:6px;">⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР</div>
    <h1 class="hero-h1">Заряджайте авто без стресу</h1>
    <p class="hero-p">Усі перевірені мережі електрозарядок України з онлайн-статусом світла та генераторів.</p>
    <button class="btn-primary">Розрахувати зарядку →</button>
    <img src="{HERO_URL}" class="hero-img">
    <div style="font-size:12px; color:#475569; margin-top:14px; line-height:1.6;">
      <div>✓ Точний калькулятор витрат батареї</div>
      <div>✓ Жива карта 480+ станцій онлайн</div>
      <div>✓ 100% захист генераторами в блекаут</div>
    </div>
  </div>

  <div class="calc-sec">
    <div class="calc-box">
      <div style="font-weight:800; font-size:16px;">Калькулятор вартості</div>
      <div style="font-size:12px; color:#64748B; margin-top:4px;">VW ID.4 (77 кВт·год) · 20% → 80%</div>
      <div class="slider-bar"><div class="slider-fill"></div></div>
      <div style="font-size:22px; font-weight:800; color:#0F172A; margin-top:8px;">652.50 ₴</div>
      <div style="font-size:11px; font-weight:700; color:#005EC9; margin:4px 0 12px;">● Час DC 120 кВт: ~28 хв</div>
      <button class="btn-primary" style="background:#0F172A;">Знайти хаб зі світлом</button>
    </div>
  </div>

  <div class="step-sec">
    <div style="font-weight:800; font-size:16px; margin-bottom:10px;">Як зарядитися за 3 кроки:</div>
    <img src="{CABLE_URL}" class="cable-img">
    <div style="font-size:12px; color:#475569; line-height:1.6;">
      <div>1. Знайдіть вільну станцію на карті</div>
      <div>2. Підключіть конектор CCS2</div>
      <div>3. Оплатіть в 1 клік Apple Pay</div>
    </div>
  </div>

  <div class="hubs-sec">
    <div style="font-weight:800; font-size:16px; margin-bottom:12px;">Хаб «Київ-Поділ» · 120 кВт</div>
    <div class="hub-card">
      <img src="{HUB_KYIV_URL}" class="hub-img">
      <div class="hub-body">
        <div style="font-size:11px; font-weight:700; color:#065F46; background:#D1FAE5; display:inline-block; padding:4px 8px; border-radius:6px; margin-bottom:10px;">🔋 Генератор ON · Вільний (3/4)</div>
        <button class="btn-primary">Прокласти маршрут (Waze / Maps)</button>
      </div>
    </div>
  </div>

  <div class="gen-sec">
    <div class="gen-box">
      <div style="font-size:10px; font-weight:800; color:#00E5FF;">ЗАХИСТ ВІД БЛЕКАУТІВ</div>
      <div style="font-size:18px; font-weight:800; margin-top:4px;">100% Енергонезалежність</div>
      <img src="{GEN_URL}" class="gen-img">
      <p style="font-size:11px; color:#CBD5E1; margin-top:8px;">Дизель-генератори 160 кВт на кожному опорному хабі мережі.</p>
    </div>
  </div>

  <div class="reviews-sec">
    <div style="font-weight:800; font-size:16px; margin-bottom:10px;">Відгуки водіїв:</div>
    <div class="rev-card">
      <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
        <img src="{AV1_URL}" style="width:28px; height:28px; border-radius:50%; object-fit:cover;">
        <span style="font-size:12px; font-weight:700;">Олексій (Tesla): «Зарядився в блекаут за 25 хв!»</span>
      </div>
    </div>
    <div class="rev-card">
      <div style="display:flex; align-items:center; gap:8px;">
        <img src="{AV2_URL}" style="width:28px; height:28px; border-radius:50%; object-fit:cover;">
        <span style="font-size:12px; font-weight:700;">Олена (Leaf): «Зручний калькулятор.»</span>
      </div>
    </div>
  </div>

  <div class="footer">
    <div style="display:flex; align-items:center; gap:8px; margin-bottom:8px;">
      <img src="{LOGO_URL}" style="width:20px; height:20px; filter:brightness(0) invert(1);">
      <span style="font-size:16px; font-weight:800;">ChargeUA</span>
    </div>
    <p style="font-size:11px; color:#94A3B8;">Агрегатор електрозарядок.<br>© 2026 ChargeUA · ПП-24</p>
  </div>

  <div class="bottom-nav">
    <div class="nav-item active">🏠 Головна</div>
    <div class="nav-item">🗺️ Карта</div>
    <div class="nav-item">⚡ Кальк</div>
    <div class="nav-item">👤 Профіль</div>
  </div>
</body></html>"""

with open(os.path.join(HTML_DIR, "mobile_full.html"), "w", encoding="utf-8") as f:
    f.write(html_mobile_full)

print("Mobile HTML generated.")

# ==============================================================================
# 4. FIG 17: DESKTOP 1440 CATALOG & DETAILS (AUTHENTIC SIDE-BY-SIDE)
# ==============================================================================

html_fig17 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ width: 1440px; background: #FFFFFF; padding: 10px; display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }}
  .page-box {{ background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 14px rgba(0,0,0,0.06); }}
  .navbar {{ height: 50px; padding: 0 24px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #E2E8F0; background: #FFF; }}
  .nav-links {{ display: flex; gap: 18px; font-size: 11px; font-weight: 600; color: #475569; }}
  .btn-sm {{ padding: 6px 12px; border-radius: 6px; font-size: 11px; font-weight: 700; cursor: pointer; }}
  .btn-pri {{ background: #005EC9; color: #FFF; border: none; }}
  .btn-out {{ border: 1px solid #CBD5E1; background: #FFF; }}

  .bread {{ font-size: 11px; color: #94A3B8; margin-bottom: 12px; }}
  .title-h1 {{ font-size: 22px; font-weight: 800; color: #0F172A; margin-bottom: 4px; }}
  .sub-p {{ font-size: 12px; color: #64748B; margin-bottom: 16px; }}

  .search-row {{ display: flex; gap: 10px; margin-bottom: 14px; }}
  .search-in {{ flex: 1; height: 36px; border: 1.5px solid #CBD5E1; border-radius: 6px; padding: 0 12px; font-size: 12px; }}
  .chips-row {{ display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 16px; }}
  .chip {{ padding: 4px 10px; border-radius: 12px; border: 1px solid #CBD5E1; font-size: 10px; font-weight: 600; background: #FFF; }}
  .chip.active {{ background: #005EC9; color: #FFF; border-color: #005EC9; }}
  .chip-grn {{ background: #D1FAE5; color: #065F46; font-weight: 700; border-color: #34D399; }}

  .grid-8 {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 18px; }}
  .card-st {{ background: #FFF; border: 1px solid #E2E8F0; border-radius: 8px; overflow: hidden; font-size: 10px; }}
  .st-img {{ width: 100%; height: 75px; object-fit: cover; }}
  .st-body {{ padding: 8px; }}
  .st-title {{ font-weight: 800; color: #0F172A; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
  .st-addr {{ color: #64748B; font-size: 9px; margin: 2px 0 6px; }}
  .st-badge {{ display: inline-block; padding: 2px 5px; border-radius: 4px; font-weight: 700; font-size: 9px; }}
  .badge-g {{ background: #D1FAE5; color: #065F46; }}

  .pag-bar {{ display: flex; justify-content: center; gap: 6px; margin: 14px 0 20px; font-size: 11px; font-weight: 600; align-items: center; }}
  .pag-btn {{ width: 24px; height: 24px; border: 1px solid #CBD5E1; border-radius: 4px; display: flex; align-items: center; justify-content: center; }}

  .footer-mini {{ background: #0F172A; color: #FFF; padding: 20px 24px 14px; font-size: 10px; }}
  .f-row {{ display: flex; justify-content: space-between; margin-bottom: 14px; }}
  .f-cols {{ display: flex; gap: 30px; }}
  .f-col div:first-child {{ font-weight: 700; color: #FFF; margin-bottom: 6px; }}
  .f-col div {{ color: #94A3B8; margin-bottom: 3px; font-size: 9px; }}
  .f-bot {{ border-top: 1px solid #1E293B; padding-top: 8px; font-size: 9px; color: #64748B; }}

  /* DETAILS SPECIFIC */
  .det-hero {{ display: grid; grid-template-columns: 1.1fr 1fr; gap: 18px; margin-bottom: 22px; }}
  .det-img {{ width: 100%; height: 210px; border-radius: 10px; object-fit: cover; }}
  .spec-box {{ background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 10px; margin: 10px 0; font-size: 11px; }}
  .spec-row {{ display: flex; justify-content: space-between; margin-bottom: 4px; }}
  .btn-full {{ width: 100%; padding: 10px; border-radius: 6px; font-weight: 700; font-size: 12px; cursor: pointer; text-align: center; }}
</style></head><body>

  <!-- LEFT: CATALOG DESKTOP 1440 -->
  <div class="page-box">
    <div class="navbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <img src="{LOGO_URL}" style="width:24px; height:24px;">
        <span style="font-size:16px; font-weight:800; color:#005EC9;">ChargeUA</span>
      </div>
      <div class="nav-links">
        <span style="color:#005EC9;">Каталог</span>
        <span>Калькулятор</span>
        <span>Карта станцій</span>
        <span>Тарифи</span>
        <span>Для бізнесу</span>
      </div>
      <button class="btn-sm btn-pri">Увійти</button>
    </div>

    <div style="padding:20px 24px;">
      <div class="bread">Головна / Каталог станцій</div>
      <h1 class="title-h1">Каталог зарядних станцій ChargeUA</h1>
      <p class="sub-p">480+ станцій онлайн по Україні з живою телеметрією та захистом від блекаутів</p>

      <div class="search-row">
        <input type="text" placeholder="Пошук станції за містом, адресою чи трасою (напр. Київ, Поділ)..." class="search-in" value="Київ, Поділ">
        <button class="btn-sm btn-pri" style="padding:0 16px;">Знайти</button>
      </div>

      <div class="chips-row">
        <span class="chip active">Всі типи</span>
        <span class="chip">Швидкісні CCS2 (>100 кВт)</span>
        <span class="chip">Type 2 (22 кВт)</span>
        <span class="chip chip-grn">🔋 З генератором</span>
        <span class="chip">Вільні зараз</span>
      </div>

      <div class="grid-8">
        <div class="card-st">
          <img src="{HUB_KYIV_URL}" class="st-img">
          <div class="st-body">
            <div class="st-title">Хаб «Київ-Поділ»</div>
            <div class="st-addr">120 кВт CCS2 · 14.50 ₴</div>
            <div class="st-badge badge-g">● Вільний (3/4)</div>
          </div>
        </div>
        <div class="card-st">
          <img src="{HUB_LVIV_URL}" class="st-img">
          <div class="st-body">
            <div class="st-title">Хаб «Арена Львів»</div>
            <div class="st-addr">160 кВт CCS2 · 15.00 ₴</div>
            <div class="st-badge badge-g">🔋 Генератор ON</div>
          </div>
        </div>
        <div class="card-st">
          <img src="{GEN_URL}" class="st-img">
          <div class="st-body">
            <div class="st-title">ЕкоХаб «Тернопіль»</div>
            <div class="st-addr">75 кВт CCS2 · 13.80 ₴</div>
            <div class="st-badge badge-g">● Вільний (2/2)</div>
          </div>
        </div>
        <div class="card-st">
          <img src="{HUB_KYIV_URL}" class="st-img">
          <div class="st-body">
            <div class="st-title">Хаб «Одеса-Аркадія»</div>
            <div class="st-addr">120 кВт CCS2 · 14.80 ₴</div>
            <div class="st-badge badge-g">● Вільний (4/4)</div>
          </div>
        </div>
        <div class="card-st">
          <img src="{HUB_LVIV_URL}" class="st-img">
          <div class="st-body">
            <div class="st-title">Хаб «Дніпро-Центр»</div>
            <div class="st-addr">160 кВт CCS2 · 15.20 ₴</div>
            <div class="st-badge badge-g">🔋 Генератор ON</div>
          </div>
        </div>
        <div class="card-st">
          <img src="{HUB_KYIV_URL}" class="st-img">
          <div class="st-body">
            <div class="st-title">Хаб «Вінниця»</div>
            <div class="st-addr">80 кВт CCS2 · 14.00 ₴</div>
            <div class="st-badge badge-g">● Вільний (2/3)</div>
          </div>
        </div>
        <div class="card-st">
          <img src="{HUB_LVIV_URL}" class="st-img">
          <div class="st-body">
            <div class="st-title">Хаб «Івано-Франківськ»</div>
            <div class="st-addr">120 кВт CCS2 · 14.50 ₴</div>
            <div class="st-badge badge-g">● Вільний (3/4)</div>
          </div>
        </div>
        <div class="card-st">
          <img src="{GEN_URL}" class="st-img">
          <div class="st-body">
            <div class="st-title">Хаб «Житомир-Траса»</div>
            <div class="st-addr">160 кВт CCS2 · 14.90 ₴</div>
            <div class="st-badge badge-g">🔋 Генератор ON</div>
          </div>
        </div>
      </div>

      <div class="pag-bar">
        <div class="pag-btn">&lt;</div>
        <div class="pag-btn" style="background:#005EC9; color:#FFF;">1</div>
        <div class="pag-btn">2</div>
        <div class="pag-btn">3</div>
        <div class="pag-btn">&gt;</div>
        <span style="color:#64748B; margin-left:10px;">Сторінка 1 з 12</span>
      </div>
    </div>

    <div class="footer-mini">
      <div class="f-row">
        <div>
          <div style="font-weight:800; font-size:13px; color:#FFF; margin-bottom:4px;">ChargeUA</div>
          <div style="color:#94A3B8;">Національний агрегатор зарядних станцій</div>
        </div>
        <div class="f-cols">
          <div class="f-col"><div>Платформа</div><div>Про нас</div><div>Тарифи</div></div>
          <div class="f-col"><div>Підтримка</div><div>Відгуки</div><div>Контакти</div></div>
        </div>
      </div>
      <div class="f-bot">© 2026 ChargeUA · Лемішка Андрій, ПП-24</div>
    </div>
  </div>

  <!-- RIGHT: STATION DETAILS DESKTOP 1440 -->
  <div class="page-box">
    <div class="navbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <img src="{LOGO_URL}" style="width:24px; height:24px;">
        <span style="font-size:16px; font-weight:800; color:#005EC9;">ChargeUA</span>
      </div>
      <div class="nav-links">
        <span>Каталог</span>
        <span>Калькулятор</span>
        <span>Карта станцій</span>
        <span>Тарифи</span>
        <span>Для бізнесу</span>
      </div>
      <button class="btn-sm btn-pri">Увійти</button>
    </div>

    <div style="padding:20px 24px;">
      <div class="bread">Головна / Каталог станцій / Хаб «Київ-Поділ»</div>

      <div class="det-hero">
        <img src="{HUB_KYIV_URL}" class="det-img">
        <div>
          <h1 style="font-size:20px; font-weight:800; color:#0F172A; margin-bottom:4px;">Хаб «Київ-Поділ» · 120 кВт CCS2</h1>
          <div style="font-size:11px; color:#64748B; margin-bottom:8px;">м. Київ, вул. Петра Сагайдачного, 12 · EcoFactor Network</div>
          <div style="display:flex; gap:6px; margin-bottom:10px;">
            <span class="st-badge badge-g">● В мережі (Онлайн)</span>
            <span class="st-badge badge-g">🔋 Дизель-генератор 160 кВА активний</span>
          </div>
          <div class="spec-box">
            <div class="spec-row"><span>Вільні роз'єми:</span><strong style="color:#005EC9;">3 з 4 (2x CCS2, 1x Type 2)</strong></div>
            <div class="spec-row"><span>Тариф:</span><strong>14.50 ₴/кВт·год</strong></div>
            <div class="spec-row"><span>Потужність DC:</span><strong>120 кВт (до 300А)</strong></div>
          </div>
          <button class="btn-full btn-pri" style="margin-bottom:8px;">Прокласти маршрут (Waze / Google Maps)</button>
          <button class="btn-full btn-out" style="color:#0F172A;">Помічник ChargeUA: розрахувати час</button>
        </div>
      </div>

      <div style="margin-bottom:18px;">
        <div style="font-weight:800; font-size:14px; color:#0F172A; margin-bottom:10px;">Схожі швидкісні станції поруч</div>
        <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:8px;">
          <div class="card-st">
            <img src="{HUB_LVIV_URL}" class="st-img" style="height:60px;">
            <div class="st-body">
              <div class="st-title">Хаб «Арена»</div>
              <div class="st-addr">160 кВт · 15.00 ₴</div>
            </div>
          </div>
          <div class="card-st">
            <img src="{GEN_URL}" class="st-img" style="height:60px;">
            <div class="st-body">
              <div class="st-title">ЕкоХаб «Тернопіль»</div>
              <div class="st-addr">75 кВт · 13.80 ₴</div>
            </div>
          </div>
          <div class="card-st">
            <img src="{HUB_KYIV_URL}" class="st-img" style="height:60px;">
            <div class="st-body">
              <div class="st-title">Хаб «Одеса»</div>
              <div class="st-addr">120 кВт · 14.80 ₴</div>
            </div>
          </div>
          <div class="card-st">
            <img src="{HUB_LVIV_URL}" class="st-img" style="height:60px;">
            <div class="st-body">
              <div class="st-title">Хаб «Дніпро»</div>
              <div class="st-addr">160 кВт · 15.20 ₴</div>
            </div>
          </div>
        </div>
      </div>

      <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:12px; margin-bottom:18px;">
        <div style="font-weight:700; font-size:12px; color:#0F172A; margin-bottom:4px;">Питання щодо станції?</div>
        <div style="font-size:10px; color:#64748B; margin-bottom:8px;">Диспетчер підтримки відповість протягом 2 хвилин</div>
        <div style="display:flex; gap:8px;">
          <input type="text" placeholder="Ваш номер телефону або запитання..." style="flex:1; height:32px; border:1px solid #CBD5E1; border-radius:6px; padding:0 10px; font-size:11px;">
          <button class="btn-sm btn-pri">Надіслати</button>
        </div>
      </div>
    </div>

    <div class="footer-mini">
      <div class="f-row">
        <div>
          <div style="font-weight:800; font-size:13px; color:#FFF; margin-bottom:4px;">ChargeUA</div>
          <div style="color:#94A3B8;">Національний агрегатор зарядних станцій</div>
        </div>
        <div class="f-cols">
          <div class="f-col"><div>Платформа</div><div>Про нас</div><div>Тарифи</div></div>
          <div class="f-col"><div>Підтримка</div><div>Відгуки</div><div>Контакти</div></div>
        </div>
      </div>
      <div class="f-bot">© 2026 ChargeUA · Лемішка Андрій, ПП-24</div>
    </div>
  </div>

</body></html>"""

with open(os.path.join(HTML_DIR, "fig17_catalog_details_desktop.html"), "w", encoding="utf-8") as f:
    f.write(html_fig17)

print("Fig 17 HTML generated.")

# ==============================================================================
# 5. FIG 18: MOBILE 390 CATALOG & DETAILS (AUTHENTIC SIDE-BY-SIDE)
# ==============================================================================

html_fig18 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ width: 800px; background: #FFFFFF; padding: 10px; display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
  .m-phone {{ background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.06); }}
  .m-top {{ background: #0F172A; color: #FFF; padding: 6px 12px; font-size: 9px; display: flex; justify-content: space-between; }}
  .m-head {{ height: 48px; padding: 0 14px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #E2E8F0; background: #FFF; }}
  .m-body {{ padding: 14px; }}
  .bread {{ font-size: 10px; color: #94A3B8; margin-bottom: 8px; }}
  .m-h1 {{ font-size: 18px; font-weight: 800; color: #0F172A; margin-bottom: 4px; }}
  .m-in {{ width: 100%; height: 34px; border: 1.5px solid #CBD5E1; border-radius: 6px; padding: 0 10px; font-size: 11px; margin: 10px 0; }}
  .chips {{ display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 12px; }}
  .chip {{ padding: 3px 8px; border-radius: 10px; border: 1px solid #CBD5E1; font-size: 9px; font-weight: 600; background: #FFF; }}
  .chip.act {{ background: #005EC9; color: #FFF; border-color: #005EC9; }}
  .st-card {{ background: #FFF; border: 1px solid #E2E8F0; border-radius: 8px; overflow: hidden; margin-bottom: 10px; }}
  .st-img {{ width: 100%; height: 110px; object-fit: cover; }}
  .st-pad {{ padding: 10px; }}
  .btn-m {{ width: 100%; padding: 8px; border-radius: 6px; font-size: 11px; font-weight: 700; cursor: pointer; text-align: center; border: none; }}
  .btn-pri {{ background: #005EC9; color: #FFF; }}
  .btn-sec {{ background: #F1F5F9; color: #0F172A; border: 1px solid #CBD5E1; }}
  .m-foot {{ background: #0F172A; color: #FFF; padding: 14px; font-size: 9px; }}
  .b-nav {{ height: 42px; background: #FFF; border-top: 1px solid #E2E8F0; display: flex; justify-content: space-around; align-items: center; font-size: 9px; font-weight: 700; color: #64748B; }}
</style></head><body>

  <!-- LEFT: MOBILE CATALOG -->
  <div class="m-phone">
    <div class="m-top"><span>● 480+ станцій</span><span>UA</span></div>
    <div class="m-head">
      <div style="display:flex; align-items:center; gap:6px;">
        <img src="{LOGO_URL}" style="width:20px; height:20px;">
        <span style="font-size:15px; font-weight:800; color:#005EC9;">ChargeUA</span>
      </div>
      <div style="font-size:18px;">☰</div>
    </div>
    <div class="m-body">
      <div class="bread">Головна / Каталог</div>
      <h1 class="m-h1">Каталог станцій</h1>
      <input type="text" placeholder="Пошук (Київ, Поділ...)" class="m-in" value="Київ, Поділ">
      <div class="chips">
        <span class="chip act">Всі</span>
        <span class="chip">Швидкісні CCS2</span>
        <span class="chip" style="background:#D1FAE5; color:#065F46;">🔋 Генератор ON</span>
      </div>

      <div class="st-card">
        <img src="{HUB_KYIV_URL}" class="st-img">
        <div class="st-pad">
          <div style="font-weight:800; font-size:13px;">Хаб «Київ-Поділ» · 120 кВт</div>
          <div style="font-size:10px; color:#64748B; margin:2px 0 6px;">вул. Сагайдачного, 12 · 14.50 ₴</div>
          <div style="font-size:9px; font-weight:700; color:#065F46; background:#D1FAE5; display:inline-block; padding:3px 6px; border-radius:4px; margin-bottom:8px;">🔋 Генератор ON · Вільний (3/4)</div>
          <button class="btn-m btn-pri">Прокласти маршрут</button>
        </div>
      </div>

      <div class="st-card">
        <img src="{HUB_LVIV_URL}" class="st-img">
        <div class="st-pad">
          <div style="font-weight:800; font-size:13px;">Хаб «Арена Львів» · 160 кВт</div>
          <div style="font-size:10px; color:#64748B; margin:2px 0 6px;">вул. Стрийська, 199 · 15.00 ₴</div>
          <div style="font-size:9px; font-weight:700; color:#065F46; background:#D1FAE5; display:inline-block; padding:3px 6px; border-radius:4px; margin-bottom:8px;">🔋 Сонячний навіс + Дизель</div>
          <button class="btn-m btn-pri">Прокласти маршрут</button>
        </div>
      </div>
    </div>
    <div class="m-foot">
      <div>ChargeUA · Мережа електрозарядок</div>
      <div style="color:#64748B; margin-top:4px;">© 2026 ChargeUA · ПП-24</div>
    </div>
    <div class="b-nav">
      <span>🏠 Головна</span>
      <span style="color:#005EC9;">🗺️ Картка</span>
      <span>⚡ Кальк</span>
      <span>👤 Профіль</span>
    </div>
  </div>

  <!-- RIGHT: MOBILE DETAILS -->
  <div class="m-phone">
    <div class="m-top"><span>● 480+ станцій</span><span>UA</span></div>
    <div class="m-head">
      <div style="display:flex; align-items:center; gap:6px;">
        <img src="{LOGO_URL}" style="width:20px; height:20px;">
        <span style="font-size:15px; font-weight:800; color:#005EC9;">ChargeUA</span>
      </div>
      <div style="font-size:18px;">☰</div>
    </div>
    <div class="m-body">
      <div class="bread">Головна / Каталог / Деталі</div>
      <img src="{HUB_KYIV_URL}" style="width:100%; height:130px; border-radius:8px; object-fit:cover; margin-bottom:10px;">
      <h1 class="m-h1">Хаб «Київ-Поділ»</h1>
      <div style="font-size:10px; color:#64748B; margin-bottom:6px;">вул. Сагайдачного, 12 · EcoFactor</div>
      <div style="font-size:9px; font-weight:700; color:#065F46; background:#D1FAE5; display:inline-block; padding:3px 6px; border-radius:4px; margin-bottom:10px;">🔋 Генератор 160 кВА активний</div>

      <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:10px; margin-bottom:10px; font-size:10px;">
        <div style="display:flex; justify-content:space-between; margin-bottom:4px;"><span>Вільні роз'єми:</span><strong style="color:#005EC9;">3 з 4 (2x CCS2)</strong></div>
        <div style="display:flex; justify-content:space-between; margin-bottom:4px;"><span>Тариф:</span><strong>14.50 ₴/кВт·год</strong></div>
        <div style="display:flex; justify-content:space-between;"><span>Потужність DC:</span><strong>120 кВт</strong></div>
      </div>

      <button class="btn-m btn-pri" style="margin-bottom:6px;">Прокласти маршрут (Waze / Maps)</button>
      <button class="btn-m btn-sec" style="margin-bottom:12px;">Помічник ChargeUA</button>

      <div style="font-weight:700; font-size:11px; margin-bottom:6px;">Альтернативні хаби поруч:</div>
      <div style="border:1px solid #E2E8F0; border-radius:6px; padding:6px; display:flex; gap:8px; align-items:center; margin-bottom:8px;">
        <img src="{HUB_LVIV_URL}" style="width:40px; height:40px; border-radius:4px; object-fit:cover;">
        <div>
          <div style="font-weight:700; font-size:10px;">Хаб «Арена» · 160 кВт</div>
          <div style="font-size:9px; color:#64748B;">15.00 ₴ · 2x CCS2 вільні</div>
        </div>
      </div>
    </div>
    <div class="m-foot">
      <div>ChargeUA · Мережа електрозарядок</div>
      <div style="color:#64748B; margin-top:4px;">© 2026 ChargeUA · ПП-24</div>
    </div>
    <div class="b-nav">
      <span>🏠 Головна</span>
      <span style="color:#005EC9;">🗺️ Картка</span>
      <span>⚡ Кальк</span>
      <span>👤 Профіль</span>
    </div>
  </div>

</body></html>"""

with open(os.path.join(HTML_DIR, "fig18_catalog_details_mobile.html"), "w", encoding="utf-8") as f:
    f.write(html_fig18)

print("Fig 18 HTML generated.")

# ==============================================================================
# RENDERING & SLICING EXECUTION
# ==============================================================================

print("Starting figure renders...")

# 1. Desktop Top & Bottom
p_fig13_html = os.path.join(HTML_DIR, "fig13_desktop_top.html")
p_fig13_png = os.path.join(SCR_DIR, "fig13_desktop_top.png")
render_chrome(p_fig13_html, p_fig13_png, 1440, 1850, scale=1.5)
print("Rendered fig13_desktop_top.png")

p_fig14_html = os.path.join(HTML_DIR, "fig14_desktop_bottom.html")
p_fig14_png = os.path.join(SCR_DIR, "fig14_desktop_bottom.png")
render_chrome(p_fig14_html, p_fig14_png, 1440, 1850, scale=1.5)
print("Rendered fig14_desktop_bottom.png")

# 2. Tablet 768: Tall render + 3-column slicing
p_tab_html = os.path.join(HTML_DIR, "tablet_full.html")
p_tab_tall = os.path.join(HTML_DIR, "tablet_tall.png")
render_chrome(p_tab_html, p_tab_tall, 768, 3350, scale=1.5)

im_tab = Image.open(p_tab_tall)
tw, th = im_tab.size
sh = th // 3

s1 = im_tab.crop((0, 0, tw, sh))
s2 = im_tab.crop((0, sh, tw, 2 * sh))
s3 = im_tab.crop((0, 2 * sh, tw, th))
if s3.size[1] != sh:
    s3 = s3.resize((tw, sh))

gap = 20
comp_w = tw * 3 + gap * 2
comp_tab = Image.new("RGB", (comp_w, sh), (255, 255, 255))
comp_tab.paste(s1, (0, 0))
comp_tab.paste(s2, (tw + gap, 0))
comp_tab.paste(s3, (2 * (tw + gap), 0))
comp_tab.save(os.path.join(SCR_DIR, "fig15_tablet.png"))
print("Rendered and sliced fig15_tablet.png (3 columns)")

# 3. Mobile 390: Tall render + 4-column slicing
p_mob_html = os.path.join(HTML_DIR, "mobile_full.html")
p_mob_tall = os.path.join(HTML_DIR, "mobile_tall.png")
render_chrome(p_mob_html, p_mob_tall, 390, 3100, scale=1.5)

im_mob = Image.open(p_mob_tall)
mw, mh = im_mob.size
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
print("Rendered and sliced fig16_mobile.png (4 columns)")

# 4. Fig 17: Desktop Catalog & Details Side by Side
p_fig17_html = os.path.join(HTML_DIR, "fig17_catalog_details_desktop.html")
p_fig17_png = os.path.join(SCR_DIR, "fig17_catalog_details_desktop.png")
render_chrome(p_fig17_html, p_fig17_png, 1440, 1050, scale=1.5)
print("Rendered fig17_catalog_details_desktop.png")

# 5. Fig 18: Mobile Catalog & Details Side by Side
p_fig18_html = os.path.join(HTML_DIR, "fig18_catalog_details_mobile.html")
p_fig18_png = os.path.join(SCR_DIR, "fig18_catalog_details_mobile.png")
render_chrome(p_fig18_html, p_fig18_png, 800, 950, scale=1.5)
print("Rendered fig18_catalog_details_mobile.png")

print("All targeted figures rendered successfully!")
