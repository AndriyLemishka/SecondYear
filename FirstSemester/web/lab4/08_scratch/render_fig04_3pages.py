# -*- coding: utf-8 -*-
import os
import subprocess
from PIL import Image

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SCR_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4\screenshots"
HTML_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4\08_scratch\html_boards"

html_fig04 = """<!DOCTYPE html><html><head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, sans-serif; }
  body { background: #F8FAFC; padding: 25px 30px; width: 1040px; -webkit-font-smoothing: antialiased; }
  .title { font-size: 16px; font-weight: 800; color: #0F172A; margin-bottom: 4px; text-align: center; }
  .subtitle { font-size: 11px; color: #64748B; margin-bottom: 16px; text-align: center; }
  .pages-row { display: flex; gap: 20px; justify-content: center; }
  .wire-col { background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 10px; width: 310px; padding: 14px; display: flex; flex-direction: column; gap: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); }
  .wire-head { font-size: 12px; font-weight: 800; color: #0F172A; border-bottom: 1.5px solid #E2E8F0; padding-bottom: 8px; text-align: center; }
  .wire-block { background: #F8FAFC; border: 1px dashed #CBD5E1; border-radius: 6px; padding: 8px 10px; font-size: 10px; color: #64748B; text-align: center; }
  .wire-block.main { background: #F1F5F9; border-style: solid; font-weight: 700; color: #0F172A; }
  .wire-block.accent { background: #EFF6FF; border-color: #93C5FD; border-style: solid; font-weight: 700; color: #005EC9; }
</style></head><body>
  <div class="title">Relume AI · Згенеровані низькодеталізовані каркаси (3 фізичні сторінки сервісу)</div>
  <div class="subtitle">Інформаційна архітектура затверджених екранів веб-платформи для водіїв електромобілів ChargeUA</div>
  <div class="pages-row">
    <!-- 01. Home Page -->
    <div class="wire-col">
      <div class="wire-head">01 · Головна сторінка (Home Page)</div>
      <div class="wire-block">Header [Logo | Nav 5 розділів | CTA]</div>
      <div class="wire-block main" style="height:65px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:3px;">
        <div>Hero Section [H1 | Copy | CTA]</div>
        <div style="font-size:8.5px; color:#64748B; font-weight:500;">Візуальний блок: Авто + Хаб + Video Loop</div>
      </div>
      <div class="wire-block">3 Benefits Strip [Калькулятор | Карта | Генератор]</div>
      <div class="wire-block accent">Interactive Calculator [Слайдер 20% → 80% | Вартість]</div>
      <div class="wire-block accent">Live Map [Онлайн-карта мережі одразу після розрахунку]</div>
      <div class="wire-block main">Popular Stations Grid [Картки хабів з телеметрією]</div>
      <div class="wire-block">Blackout Protection [Генератори 160 кВт Cummins]</div>
      <div class="wire-block">3 Steps Guide &amp; Driver Reviews [Відгуки водіїв]</div>
      <div class="wire-block">Footer [Навігація | Статус 24/7 | Копірайт]</div>
    </div>

    <!-- 02. Stations Map & Catalog -->
    <div class="wire-col">
      <div class="wire-head">02 · Карта та каталог станцій (Stations Map)</div>
      <div class="wire-block">Header [Logo | Nav | Швидкий пошук]</div>
      <div class="wire-block main" style="padding:10px 8px;">
        <div>Search &amp; Filters Bar</div>
        <div style="font-size:8.5px; color:#64748B; font-weight:500; margin-top:2px;">[Пошук за адресою | Тільки вільні | 🔋 Генератор ON]</div>
      </div>
      <div class="wire-block accent" style="height:140px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:6px;">
        <div style="font-size:11px;">🗺 Interactive Map Container</div>
        <div style="font-size:9px; color:#64748B; font-weight:500;">Кластеризація та статусні маркери міст</div>
        <div style="font-size:8.5px; color:#005EC9;">(480+ станцій онлайн по Україні)</div>
      </div>
      <div class="wire-block main">Station Cards List [Фільтрований перелік хабів]</div>
      <div class="wire-block">Quick Route Action [Прямий запуск навігатора]</div>
      <div class="wire-block">Footer [Підтримка водіїв | Контакти]</div>
    </div>

    <!-- 03. Station Details -->
    <div class="wire-col">
      <div class="wire-head">03 · Деталі зарядної станції (Station Details)</div>
      <div class="wire-block">Header [Навігація повернення ← На карту]</div>
      <div class="wire-block main" style="height:75px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:3px;">
        <div>Station Photo Hero</div>
        <div style="font-size:8.5px; color:#64748B; font-weight:500;">Панорамне фото локації та статус потужності (160 кВт)</div>
      </div>
      <div class="wire-block accent">Live Telemetry &amp; Port Statuses [Зайнятість портів]</div>
      <div class="wire-block main">Tariffs Breakdown [DC Ultra / AC тарифи без прихованих оплат]</div>
      <div class="wire-block accent" style="padding:10px 8px;">
        <div>Route Navigation Assistant</div>
        <div style="font-size:8.5px; color:#005EC9; font-weight:500;">(Без бронювань та депозитів — вільний доїзд)</div>
      </div>
      <div class="wire-block">Nearby Amenities [Кав'ярня | Wi-Fi | Вбиральня | Паркінг]</div>
      <div class="wire-block">Footer [Оновлення даних за стандартом OCPP 2.0.1]</div>
    </div>
  </div>
</body></html>"""

html_path = os.path.join(HTML_DIR, "fig04_relume_wireframes_3pages.html")
out_png = os.path.join(SCR_DIR, "fig04_relume_wireframes.png")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_fig04)

cmd = [
    CHROME_PATH,
    "--headless=new",
    "--window-size=1040,640",
    "--hide-scrollbars",
    "--force-device-scale-factor=2",
    f"--screenshot={out_png}",
    f"file:///{html_path.replace(os.sep, '/')}"
]
subprocess.run(cmd, check=True)

im = Image.open(out_png)
print(f"Generated fig04_relume_wireframes (3 pages): {im.size}")
