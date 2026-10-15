# -*- coding: utf-8 -*-
"""
Render perfect, professional figures for:
- fig14_desktop_bottom.png: Generator section, 3 Station cards, Clean Steps (NO video!), Reviews with avatars, B2B form, Footer
- fig15_tablet.png: 3 balanced tablet columns (no slicing cuts across titles, NO video!)
- fig16_mobile.png: 4 balanced mobile columns (no slicing cuts, NO video, bottom nav on col 4)
Matching the student reference report (ReadSpace) 100%.
"""

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
HERO_URL = p2u("hero_bg.jpg")
HUB_KYIV_URL = p2u("ai_hub_kyiv.jpg")
HUB_LVIV_URL = p2u("ai_hub_lviv.jpg")
GEN_URL = p2u("ai_generator_blackout.jpg")
CABLE_URL = p2u("ai_step_cable.jpg")
AV1_URL = p2u("ai_avatar_oleksiy.jpg")
AV2_URL = p2u("ai_avatar_olena.jpg")
AV3_URL = p2u("ai_avatar_sergiy.jpg")

COMMON_HEAD = """
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
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

# ==============================================================================
# 1. FIG 14: DESKTOP BOTTOM (NO VIDEO PLAYER BOX)
# ==============================================================================
html_fig14 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ width: 1440px; background: #FFFFFF; }}
  .sec-gen {{ padding: 30px 60px 30px; }}
  .banner-box {{ background: #0F172A; border-radius: 20px; padding: 40px 50px; display: grid; grid-template-columns: 1.1fr 1fr; gap: 40px; align-items: center; color: #FFF; }}
  .gen-h2 {{ font-size: 32px; font-weight: 800; line-height: 1.25; margin-bottom: 14px; }}
  .gen-p {{ font-size: 15px; line-height: 1.6; color: #CBD5E1; margin-bottom: 24px; }}
  .btn-gen {{ background: #00E5FF; color: #0F172A; border: none; padding: 13px 26px; border-radius: 8px; font-size: 14px; font-weight: 800; cursor: pointer; }}

  .hubs-sec {{ padding: 20px 60px 30px; }}
  .hubs-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 20px; }}
  .hub-card {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 16px; overflow: hidden; }}
  .hub-img {{ width: 100%; height: 180px; object-fit: cover; }}
  .hub-body {{ padding: 18px; }}
  .hub-title {{ font-size: 16px; font-weight: 800; color: #0F172A; }}
  .hub-addr {{ font-size: 13px; color: #64748B; margin: 4px 0 12px; }}
  .badge-status {{ display: inline-block; padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: 700; margin-bottom: 14px; }}
  .badge-green {{ background: #D1FAE5; color: #065F46; }}
  .btn-route {{ width: 100%; background: #005EC9; color: #FFF; border: none; padding: 11px; border-radius: 8px; font-size: 13px; font-weight: 700; cursor: pointer; }}

  .steps-sec {{ padding: 20px 60px 40px; }}
  .steps-box {{ background: #F8FAFC; border: 1.5px solid #E2E8F0; border-radius: 20px; padding: 36px 44px; }}
  .steps-grid {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px; margin-top: 28px; }}
  .step-card {{ background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 14px; padding: 24px 20px; }}
  .step-num {{ width: 36px; height: 36px; border-radius: 18px; background: #005EC9; color: #FFF; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 16px; margin-bottom: 14px; }}
  .step-title {{ font-size: 16px; font-weight: 800; color: #0F172A; margin-bottom: 8px; }}
  .step-desc {{ font-size: 13px; line-height: 1.5; color: #64748B; }}

  .reviews-sec {{ padding: 20px 60px 30px; }}
  .rev-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 20px; }}
  .rev-card {{ background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 14px; padding: 22px; display: flex; flex-direction: column; justify-content: space-between; }}
  .stars {{ color: #F59E0B; font-size: 16px; margin-bottom: 10px; }}
  .rev-text {{ font-size: 13px; line-height: 1.5; color: #334155; margin-bottom: 18px; }}
  .rev-author {{ display: flex; align-items: center; gap: 12px; }}
  .rev-avatar {{ width: 44px; height: 44px; border-radius: 50%; object-fit: cover; }}

  .form-sec {{ padding: 20px 60px 40px; }}
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
        <img src="{HUB_KYIV_URL}" class="hub-img">
        <div class="hub-body">
          <div class="hub-title">Хаб «Київ-Оболонь» · 120 кВт CCS2</div>
          <div class="hub-addr">просп. Оболонський, 1-Б · 4 порти</div>
          <div class="badge-status badge-green">⚡ Мережа онлайн · Вільний (2/4)</div>
          <button class="btn-route">Прокласти маршрут (Waze / Maps)</button>
        </div>
      </div>
    </div>
  </div>

  <!-- HOW IT WORKS (CLEAN STEPS - NO VIDEO!) -->
  <div class="steps-sec">
    <div class="steps-box">
      <div style="font-size:12px; font-weight:800; color:#005EC9; margin-bottom:6px;">ПРОСТИЙ АЛГОРИТМ</div>
      <h2 style="font-size:26px; font-weight:800; color:#0F172A;">Як зарядитися за 3 кроки: від пошуку до повної батареї</h2>
      <p style="font-size:14px; color:#64748B; margin-top:4px;">Зручний покроковий процес без складної реєстрації, передплат чи очікування в чергах.</p>
      
      <div class="steps-grid">
        <div class="step-card">
          <div class="step-num">1</div>
          <div class="step-title">Знайдіть вільну станцію</div>
          <div class="step-desc">Фільтруйте за потужністю, роз'ємом або наявністю генератора на живій карті ChargeUA.</div>
        </div>
        <div class="step-card">
          <div class="step-num">2</div>
          <div class="step-title">Підключіть конектор CCS2</div>
          <div class="step-desc">Вставте кабель у роз'єм електрокара — світловий смарт-індикатор спалахне зеленим.</div>
        </div>
        <div class="step-card">
          <div class="step-num">3</div>
          <div class="step-title">Оплатіть у 1 клік</div>
          <div class="step-desc">Apple Pay, Google Pay або банківська картка. Жодних обов'язкових депозитів.</div>
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
      <button style="background:#005EC9; color:#FFF; border:none; padding:14px 32px; font-size:14px; font-weight:700; border-radius:8px; cursor:pointer;">Подати заявку на монтаж</button>
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
</body></html>
"""

# ==============================================================================
# 2. FIG 15: TABLET (3 LOGICAL CLEAN COLUMNS MATCHING READSPACE REFERENCE)
# ==============================================================================
html_fig15 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ width: 1250px; background: #F1F5F9; padding: 20px; }}
  .board-cols {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; align-items: start; }}
  .col-frame {{ background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 14px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.04); }}
  
  .t-head {{ padding: 14px 18px; border-bottom: 1px solid #E2E8F0; display: flex; align-items: center; justify-content: space-between; }}
  .t-hero {{ padding: 20px 18px; }}
  .t-h1 {{ font-size: 22px; font-weight: 800; line-height: 1.25; margin: 10px 0 8px; color: #0F172A; }}
  .t-p {{ font-size: 13px; color: #64748B; line-height: 1.45; margin-bottom: 14px; }}
  .t-btn-blue {{ background: #005EC9; color: #FFF; border: none; padding: 10px 18px; border-radius: 7px; font-size: 12px; font-weight: 700; cursor: pointer; }}
  
  .t-strip {{ padding: 12px 18px; background: #F8FAFC; border-top: 1px solid #E2E8F0; border-bottom: 1px solid #E2E8F0; font-size: 12px; font-weight: 600; display: flex; justify-content: space-between; }}
  .t-calc {{ padding: 18px; }}
  .t-calc-res {{ background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; padding: 14px; margin-top: 12px; }}

  .hub-item {{ padding: 16px 18px; border-bottom: 1px solid #E2E8F0; }}
  .hub-item:last-child {{ border-bottom: none; }}
  .hub-img-t {{ width: 100%; height: 160px; object-fit: cover; border-radius: 10px; margin-bottom: 10px; }}
  
  .gen-box-t {{ padding: 20px 18px; background: #0F172A; color: #FFF; }}
  .step-box-t {{ padding: 12px 14px; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; margin-bottom: 10px; }}
  .rev-box-t {{ padding: 14px 16px; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; margin-bottom: 12px; }}
  
  .footer-t {{ background: #0F172A; color: #FFF; padding: 24px 18px; font-size: 11px; }}
</style></head><body>
<div class="board-cols">
  <!-- COL 1: HEADER + HERO + STRIP + CALCULATOR -->
  <div class="col-frame">
    <div class="t-head">
      <div style="display:flex; align-items:center; gap:8px;">
        <img src="{LOGO_URL}" style="width:24px; height:24px;">
        <span style="font-weight:800; font-size:16px; color:#005EC9;">ChargeUA</span>
      </div>
      <div style="font-size:12px; color:#64748B;">Головна · Калькулятор · Карта</div>
      <button class="t-btn-blue">Знайти</button>
    </div>
    
    <div class="t-hero">
      <div style="font-size:10px; font-weight:800; color:#005EC9;">⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР</div>
      <div class="t-h1">Швидка зарядка по всій Україні</div>
      <div class="t-p">Знаходьте станції, розраховуйте вартість за секунди та подорожуйте без хвилювань у блекаути.</div>
      <button class="t-btn-blue" style="margin-bottom:14px;">Розрахувати зарядку →</button>
      <img src="{HERO_URL}" style="width:100%; height:180px; object-fit:cover; border-radius:10px;">
    </div>

    <div class="t-strip">
      <span>⚡ 480+ станцій</span>
      <span style="color:#16A34A;">🔋 100% у блекаути</span>
      <span style="color:#005EC9;">⏱ 3 сек розрахунок</span>
    </div>

    <div class="t-calc">
      <div style="font-size:15px; font-weight:800; color:#0F172A;">Калькулятор зарядки</div>
      <div style="font-size:12px; color:#005EC9; font-weight:600; margin:4px 0 10px;">Volkswagen ID.4 · 20% → 80%</div>
      <div class="t-calc-res">
        <div style="font-size:20px; font-weight:800; color:#005EC9;">652.50 ₴</div>
        <div style="font-size:11px; color:#64748B; margin-top:2px;">~28 хв на DC 120 кВт · 46.2 кВт·год</div>
      </div>
      <button class="t-btn-blue" style="width:100%; margin-top:12px;">Знайти вільну станцію</button>
    </div>
  </div>

  <!-- COL 2: POPULAR HUBS + GENERATOR BLACKOUT -->
  <div class="col-frame">
    <div style="padding:14px 18px; border-bottom:1px solid #E2E8F0; font-weight:800; font-size:15px;">
      Популярні зарядні хаби
    </div>

    <div class="hub-item">
      <img src="{HUB_KYIV_URL}" class="hub-img-t">
      <div style="font-weight:800; font-size:15px;">Хаб «Київ-Поділ» · 120 кВт CCS2</div>
      <div style="font-size:12px; color:#64748B; margin:3px 0 8px;">вул. Сагайдачного, 12 · 4 порти</div>
      <div style="display:inline-block; padding:3px 8px; border-radius:5px; font-size:10px; font-weight:700; background:#D1FAE5; color:#065F46; margin-bottom:10px;">🔋 Працює від генератора</div>
      <button class="t-btn-blue" style="width:100%;">Прокласти маршрут</button>
    </div>

    <div class="hub-item">
      <img src="{HUB_LVIV_URL}" class="hub-img-t">
      <div style="font-weight:800; font-size:15px;">Хаб «Арена Львів» · 160 кВт CCS2</div>
      <div style="font-size:12px; color:#64748B; margin:3px 0 8px;">вул. Стрийська, 199 · 6 портів</div>
      <div style="display:inline-block; padding:3px 8px; border-radius:5px; font-size:10px; font-weight:700; background:#D1FAE5; color:#065F46; margin-bottom:10px;">🔋 Працює від генератора</div>
      <button class="t-btn-blue" style="width:100%;">Прокласти маршрут</button>
    </div>

    <div class="gen-box-t">
      <div style="font-size:10px; font-weight:800; color:#00E5FF; margin-bottom:4px;">ЕНЕРГОНЕЗАЛЕЖНІСТЬ 100%</div>
      <div style="font-size:16px; font-weight:800; margin-bottom:8px;">Зарядка у повні блекаути</div>
      <div style="font-size:12px; color:#CBD5E1; line-height:1.45; margin-bottom:12px;">180+ хабів мережі обладнані потужними генераторами 160 кВт для безперебійного живлення.</div>
      <img src="{GEN_URL}" style="width:100%; height:130px; object-fit:cover; border-radius:8px;">
    </div>
  </div>

  <!-- COL 3: STEPS + REVIEWS + FORM + FOOTER -->
  <div class="col-frame">
    <div style="padding:16px 18px;">
      <div style="font-weight:800; font-size:15px; margin-bottom:12px;">Як зарядитися за 3 кроки</div>
      
      <div class="step-box-t">
        <div style="font-weight:800; font-size:13px; color:#005EC9;">1. Знайдіть вільну станцію</div>
        <div style="font-size:11px; color:#64748B; margin-top:2px;">Фільтруйте за потужністю або наявністю генератора на карті.</div>
      </div>
      <div class="step-box-t">
        <div style="font-weight:800; font-size:13px; color:#005EC9;">2. Підключіть конектор CCS2</div>
        <div style="font-size:11px; color:#64748B; margin-top:2px;">Вставте кабель — індикатор спалахне зеленим кольором.</div>
      </div>
      <div class="step-box-t">
        <div style="font-weight:800; font-size:13px; color:#005EC9;">3. Оплатіть у 1 клік</div>
        <div style="font-size:11px; color:#64748B; margin-top:2px;">Apple Pay або картка без жодних передплат та комісій.</div>
      </div>

      <div style="font-weight:800; font-size:15px; margin:16px 0 10px;">Відгуки водіїв</div>
      <div class="rev-box-t">
        <div style="color:#F59E0B; font-size:12px; margin-bottom:4px;">★★★★★</div>
        <div style="font-size:11px; color:#334155; line-height:1.4;">«Під час блекауту зарядився за 25 хв на Подолі. Генератор гуде, все супер!»</div>
        <div style="display:flex; align-items:center; gap:8px; margin-top:8px;">
          <img src="{AV1_URL}" style="width:26px; height:26px; border-radius:13px; object-fit:cover;">
          <div style="font-size:11px; font-weight:700;">Олексій К. (Tesla Y)</div>
        </div>
      </div>

      <div style="font-weight:800; font-size:14px; margin:14px 0 8px;">Встановіть станцію ChargeUA</div>
      <input type="text" placeholder="Ваш телефон (+380...)" style="width:100%; height:34px; border:1px solid #CBD5E1; border-radius:6px; padding:0 10px; font-size:12px; margin-bottom:8px;">
      <button class="t-btn-blue" style="width:100%; margin-bottom:16px;">Подати заявку на монтаж</button>
    </div>

    <div class="footer-t">
      <div style="display:flex; align-items:center; gap:6px; margin-bottom:8px;">
        <img src="{LOGO_URL}" style="width:20px; height:20px; filter:brightness(0) invert(1);">
        <span style="font-weight:800; font-size:14px;">ChargeUA</span>
      </div>
      <div style="color:#94A3B8; line-height:1.4; margin-bottom:10px;">Національний агрегатор зарядної інфраструктури України.</div>
      <div style="color:#64748B; border-top:1px solid #1E293B; padding-top:8px;">© 2026 ChargeUA · Лемішка Андрій, ПП-24</div>
    </div>
  </div>
</div>
</body></html>
"""

# ==============================================================================
# 3. FIG 16: MOBILE (4 LOGICAL CLEAN COLUMNS MATCHING READSPACE REFERENCE)
# ==============================================================================
html_fig16 = f"""<!DOCTYPE html><html><head>{COMMON_HEAD}
<style>
  body {{ width: 1600px; background: #F1F5F9; padding: 20px; }}
  .board-cols {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; align-items: start; }}
  .col-frame {{ background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 14px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.04); }}
  
  .m-topbar {{ background: #0F172A; color: #FFF; padding: 6px 14px; font-size: 10px; font-weight: 500; display: flex; justify-content: space-between; }}
  .m-head {{ padding: 12px 14px; border-bottom: 1px solid #E2E8F0; display: flex; align-items: center; justify-content: space-between; }}
  .m-hero {{ padding: 16px 14px; }}
  .m-h1 {{ font-size: 20px; font-weight: 800; line-height: 1.25; margin: 8px 0 6px; color: #0F172A; }}
  .m-p {{ font-size: 12px; color: #64748B; line-height: 1.45; margin-bottom: 12px; }}
  .m-btn-blue {{ background: #005EC9; color: #FFF; border: none; padding: 9px 14px; border-radius: 7px; font-size: 12px; font-weight: 700; cursor: pointer; width: 100%; }}
  
  .m-calc-box {{ background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; padding: 12px; margin: 12px 14px; }}
  .m-step {{ padding: 10px 12px; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; margin-bottom: 8px; }}
  .m-hub {{ padding: 12px 14px; border-bottom: 1px solid #E2E8F0; }}
  .m-hub-img {{ width: 100%; height: 130px; object-fit: cover; border-radius: 8px; margin-bottom: 8px; }}
  .m-gen {{ background: #0F172A; color: #FFF; padding: 14px; }}
  .m-rev {{ background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 10px 12px; margin-bottom: 8px; }}
  .m-footer {{ background: #0F172A; color: #FFF; padding: 18px 14px; font-size: 10px; }}
  
  .m-botnav {{ background: #FFFFFF; border-top: 1px solid #E2E8F0; padding: 10px 14px; display: flex; justify-content: space-around; font-size: 11px; font-weight: 700; }}
</style></head><body>
<div class="board-cols">
  <!-- COL 1: TOPBAR + HEADER + HERO + BENEFITS -->
  <div class="col-frame">
    <div class="m-topbar">
      <span>● 480+ станцій онлайн</span>
      <span>0 800 300 400</span>
    </div>
    <div class="m-head">
      <div style="display:flex; align-items:center; gap:6px;">
        <img src="{LOGO_URL}" style="width:20px; height:20px;">
        <span style="font-weight:800; font-size:15px; color:#005EC9;">ChargeUA</span>
      </div>
      <div style="font-size:18px; font-weight:700;">☰</div>
    </div>
    <div class="m-hero">
      <div style="font-size:9px; font-weight:800; color:#005EC9;">⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР</div>
      <div class="m-h1">Заряджайте авто без стресу</div>
      <div class="m-p">Усі мережі України на одній карті з фільтром генераторів у блекаути.</div>
      <button class="m-btn-blue" style="margin-bottom:12px;">Розрахувати зарядку →</button>
      <img src="{HERO_URL}" style="width:100%; height:150px; object-fit:cover; border-radius:8px;">
    </div>
    <div style="padding:12px 14px; border-top:1px solid #E2E8F0; font-size:11px; line-height:1.6; color:#334155;">
      <div>✓ Точний калькулятор витрат</div>
      <div>✓ Live-карта 480+ станцій зі статусом</div>
      <div>✓ 100% захист генераторами у блекаути</div>
    </div>
  </div>

  <!-- COL 2: CALCULATOR + STEPS -->
  <div class="col-frame">
    <div style="padding:12px 14px; border-bottom:1px solid #E2E8F0; font-weight:800; font-size:14px;">
      Калькулятор вартості
    </div>
    <div class="m-calc-box">
      <div style="font-size:12px; font-weight:700; color:#005EC9;">VW ID.4 (77 кВт·год) · 20% → 80%</div>
      <div style="font-size:20px; font-weight:800; color:#0F172A; margin:6px 0;">652.50 ₴</div>
      <div style="font-size:11px; color:#64748B; margin-bottom:10px;">~28 хв на DC 120 кВт · 46.2 кВт·год</div>
      <button class="m-btn-blue">Знайти найближчий хаб</button>
    </div>

    <div style="padding:0 14px 14px;">
      <div style="font-weight:800; font-size:14px; margin-bottom:10px;">Як зарядитися за 3 кроки:</div>
      <div class="m-step">
        <div style="font-weight:800; font-size:12px; color:#005EC9;">1. Знайдіть станцію на карті</div>
        <div style="font-size:10px; color:#64748B;">Фільтр за потужністю та світлом.</div>
      </div>
      <div class="m-step">
        <div style="font-weight:800; font-size:12px; color:#005EC9;">2. Підключіть конектор CCS2</div>
        <div style="font-size:10px; color:#64748B;">Вставте кабель у порт електромобіля.</div>
      </div>
      <div class="m-step">
        <div style="font-weight:800; font-size:12px; color:#005EC9;">3. Оплатіть у 1 клік</div>
        <div style="font-size:10px; color:#64748B;">Apple Pay або банківська картка.</div>
      </div>
      <img src="{CABLE_URL}" style="width:100%; height:120px; object-fit:cover; border-radius:8px; margin-top:4px;">
    </div>
  </div>

  <!-- COL 3: POPULAR HUBS + GENERATOR -->
  <div class="col-frame">
    <div style="padding:12px 14px; border-bottom:1px solid #E2E8F0; font-weight:800; font-size:14px;">
      Популярні хаби мережі:
    </div>

    <div class="m-hub">
      <img src="{HUB_KYIV_URL}" class="m-hub-img">
      <div style="font-weight:800; font-size:13px;">Хаб «Київ-Поділ» · 120 кВт</div>
      <div style="font-size:11px; color:#64748B; margin:2px 0 6px;">вул. Сагайдачного, 12 · 14.50 ₴</div>
      <div style="display:inline-block; padding:2px 6px; border-radius:4px; font-size:9px; font-weight:700; background:#D1FAE5; color:#065F46; margin-bottom:8px;">🔋 Генератор ON · Вільний (3/4)</div>
      <button class="m-btn-blue">Прокласти маршрут</button>
    </div>

    <div class="m-hub">
      <img src="{HUB_LVIV_URL}" class="m-hub-img">
      <div style="font-weight:800; font-size:13px;">Хаб «Арена Львів» · 160 кВт</div>
      <div style="font-size:11px; color:#64748B; margin:2px 0 6px;">вул. Стрийська, 199 · 15.00 ₴</div>
      <div style="display:inline-block; padding:2px 6px; border-radius:4px; font-size:9px; font-weight:700; background:#D1FAE5; color:#065F46; margin-bottom:8px;">🔋 Сонячний навіс + Дизель</div>
      <button class="m-btn-blue">Прокласти маршрут</button>
    </div>

    <div class="m-gen">
      <div style="font-size:9px; font-weight:800; color:#00E5FF; margin-bottom:2px;">ЕНЕРГОНЕЗАЛЕЖНІСТЬ 100%</div>
      <div style="font-size:14px; font-weight:800; margin-bottom:6px;">Зарядка у повні блекаути</div>
      <div style="font-size:11px; color:#CBD5E1; line-height:1.4; margin-bottom:8px;">Промислові дизель-генератори 160 кВт гарантують живлення.</div>
      <img src="{GEN_URL}" style="width:100%; height:110px; object-fit:cover; border-radius:6px;">
    </div>
  </div>

  <!-- COL 4: REVIEWS + FORM + FOOTER + BOTTOM NAV -->
  <div class="col-frame">
    <div style="padding:12px 14px;">
      <div style="font-weight:800; font-size:14px; margin-bottom:8px;">Відгуки водіїв:</div>
      <div class="m-rev">
        <div style="color:#F59E0B; font-size:11px; margin-bottom:2px;">★★★★★</div>
        <div style="font-size:10px; color:#334155;">«Під час блекауту зарядився за 25 хв на Подолі! Все супер!»</div>
        <div style="display:flex; align-items:center; gap:6px; margin-top:6px;">
          <img src="{AV1_URL}" style="width:22px; height:22px; border-radius:11px; object-fit:cover;">
          <span style="font-size:10px; font-weight:700;">Олексій (Tesla Y)</span>
        </div>
      </div>
      <div class="m-rev">
        <div style="color:#F59E0B; font-size:11px; margin-bottom:2px;">★★★★★</div>
        <div style="font-size:10px; color:#334155;">«Зручний калькулятор витрат і точний кілометраж.»</div>
        <div style="display:flex; align-items:center; gap:6px; margin-top:6px;">
          <img src="{AV2_URL}" style="width:22px; height:22px; border-radius:11px; object-fit:cover;">
          <span style="font-size:10px; font-weight:700;">Олена (Nissan Leaf)</span>
        </div>
      </div>

      <div style="font-weight:800; font-size:13px; margin:12px 0 6px;">Встановіть станцію:</div>
      <input type="text" placeholder="Ім'я та номер телефону" style="width:100%; height:32px; border:1px solid #CBD5E1; border-radius:6px; padding:0 8px; font-size:11px; margin-bottom:6px;">
      <button class="m-btn-blue" style="margin-bottom:12px;">Подати заявку</button>
    </div>

    <div class="m-footer">
      <div style="display:flex; align-items:center; gap:6px; margin-bottom:6px;">
        <img src="{LOGO_URL}" style="width:16px; height:16px; filter:brightness(0) invert(1);">
        <span style="font-weight:800; font-size:13px;">ChargeUA</span>
      </div>
      <div style="color:#94A3B8; margin-bottom:6px;">Національний веб-помічник зарядної інфраструктури.</div>
      <div style="color:#64748B;">© 2026 ChargeUA · ПП-24</div>
    </div>

    <!-- STICKY BOTTOM NAV BAR -->
    <div class="m-botnav">
      <span style="color:#005EC9;">⌂ Головна</span>
      <span style="color:#64748B;">⚲ Карта</span>
      <span style="color:#64748B;">🖩 Калькулятор</span>
      <span style="color:#64748B;">👤 Профіль</span>
    </div>
  </div>
</div>
</body></html>
"""

print("Writing HTML boards...")
p_f14_html = os.path.join(HTML_DIR, "fig14_desktop_bottom.html")
p_f15_html = os.path.join(HTML_DIR, "fig15_tablet.html")
p_f16_html = os.path.join(HTML_DIR, "fig16_mobile.html")

with open(p_f14_html, "w", encoding="utf-8") as f:
    f.write(html_fig14)
with open(p_f15_html, "w", encoding="utf-8") as f:
    f.write(html_fig15)
with open(p_f16_html, "w", encoding="utf-8") as f:
    f.write(html_fig16)

print("Rendering figures with Chrome Headless...")
p_f14_png = os.path.join(SCR_DIR, "fig14_desktop_bottom.png")
p_f15_png = os.path.join(SCR_DIR, "fig15_tablet.png")
p_f16_png = os.path.join(SCR_DIR, "fig16_mobile.png")

render_chrome(p_f14_html, p_f14_png, 1440, 2300, scale=1.5)
print("Rendered fig14_desktop_bottom.png")

render_chrome(p_f15_html, p_f15_png, 1250, 1260, scale=1.5)
print("Rendered fig15_tablet.png (Clean 3 columns, no cuts, no video)")

render_chrome(p_f16_html, p_f16_png, 1600, 1280, scale=1.5)
print("Rendered fig16_mobile.png (Clean 4 columns, no cuts, no video, bottom nav)")

print("ALL FIGURES RENDERED PERFECTLY!")
