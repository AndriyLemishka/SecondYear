import os, subprocess

BASE_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4"
MAT_DIR = os.path.join(BASE_DIR, "materials")
HTML_DIR = os.path.join(BASE_DIR, "08_scratch")
SCR_DIR = os.path.join(BASE_DIR, "08_scratch")
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

logo_path = os.path.join(MAT_DIR, "Logo.svg").replace(os.sep, "/")
hero_path = os.path.join(MAT_DIR, "hero_bg.jpg").replace(os.sep, "/")

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Inter', sans-serif;
    background: #FFFFFF;
    color: #0F172A;
    width: 1440px;
    margin: 0;
  }}
  header {{
    height: 76px;
    padding: 0 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #E2E8F0;
  }}
  .hero-wrapper {{
    position: relative;
    width: 1440px;
    height: 520px;
    background: #FFFFFF;
    overflow: hidden;
  }}
  .hero-img {{
    position: absolute;
    right: 0;
    top: 0;
    width: 65%;
    height: 100%;
    object-fit: contain;
    object-position: right center;
    z-index: 1;
  }}
  .hero-content {{
    position: relative;
    z-index: 2;
    width: 50%;
    padding: 50px 0 50px 60px;
  }}
  .chip {{
    background: #F1F5F9;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 600;
    color: #334155;
    border: 1px solid #CBD5E1;
  }}
</style>
</head>
<body>
  <div style="background:#0F172A; color:#FFF; font-size:11px; padding:7px 60px; display:flex; justify-content:space-between;">
    <div>● Мережа ChargeUA: 480+ станцій онлайн по Україні | 100% телеметрія в реальному часі</div>
    <div>Гаряча лінія 24/7: 0 800 300 400 | UA</div>
  </div>
  <header>
    <div style="display:flex; align-items:center; gap:10px;">
      <img src="file:///{logo_path}" style="height:36px;">
      <span style="font-size:22px; font-weight:800; color:#005EC9;">ChargeUA</span>
    </div>
    <div style="display:flex; gap:28px; font-size:14px; font-weight:600; color:#334155;">
      <span style="color:#005EC9;">Головна</span>
      <span>Калькулятор</span>
      <span>Карта станцій</span>
      <span>Тарифи</span>
      <span>Для бізнесу</span>
    </div>
    <button style="background:#005EC9; color:#FFF; border:none; padding:10px 20px; border-radius:8px; font-weight:700;">Знайти зарядку</button>
  </header>
  <div class="hero-wrapper">
    <img src="file:///{hero_path}" class="hero-img">
    <div class="hero-content">
      <div style="background:#EFF6FF; color:#005EC9; border:1px solid #BFDBFE; display:inline-block; padding:4px 12px; border-radius:999px; font-size:11px; font-weight:700; margin-bottom:14px;">
        ⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР ЗАРЯДНИХ СТАНЦІЙ
      </div>
      <h1 style="font-size:40px; font-weight:800; line-height:1.15; margin-bottom:14px;">
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
        <span class="chip">Type 2 (22 кВт)</span>
        <span class="chip">CCS 2 (160 кВт)</span>
        <span class="chip">CHAdeMO</span>
        <span class="chip" style="background:#D1FAE5; color:#047857; font-weight:700; border-color:#A7F3D0;">🔋 З генератором</span>
      </div>
    </div>
  </div>
</body>
</html>"""

html_file = os.path.join(HTML_DIR, "test_hero.html")
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html)

out_png = os.path.join(SCR_DIR, "test_hero.png")
cmd = [
    CHROME_PATH,
    "--headless=new",
    "--window-size=1440,650",
    "--force-device-scale-factor=1.0",
    f"--screenshot={out_png}",
    f"file:///{html_file.replace(os.sep, '/')}"
]
subprocess.run(cmd, check=True)
print("Saved test_hero.png successfully")
