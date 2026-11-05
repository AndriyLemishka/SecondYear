# -*- coding: utf-8 -*-
"""
Генерація детального розв'язку Завдання 6 Варіанта 12 БЕЗ ЖОДНОГО СПРОЩЕННЯ.
Кожен доданок розписується повністю за канонічною формулою Бернуллі:
P_n(k) = C_n^k * p^k * q^(n-k)
з усіма дробами (1/2)^k * (1/2)^(n-k).
"""

import subprocess
import os
import shutil
import pymupdf

html_content = r'''<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <title>Тема 6 — Завдання 6 Варіанта 12: Розв'язок БЕЗ спрощення формули</title>
  <style>
    @page {
      size: 210mm 297mm;
      margin: 0;
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      width: 210mm;
      height: 297mm;
      max-height: 297mm;
      overflow: hidden;
      background: #f8fafc;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      color: #0f172a;
      padding: 7mm 8.5mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    /* HEADER */
    .header {
      background: #0284c7;
      color: #ffffff;
      border-radius: 6px;
      padding: 8px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }
    .header h1 {
      font-size: 13pt;
      font-weight: 900;
      text-transform: uppercase;
      line-height: 1.15;
    }
    .header p {
      font-size: 8.2pt;
      color: #e0f2fe;
      margin-top: 2px;
    }
    .header .badge {
      background: rgba(255, 255, 255, 0.2);
      border: 1px solid rgba(255, 255, 255, 0.4);
      border-radius: 4px;
      padding: 4px 10px;
      font-size: 8.5pt;
      font-weight: 800;
      text-align: right;
    }

    .section-grid {
      display: flex;
      flex-direction: column;
      gap: 6.5px;
      flex: 1;
    }

    .card {
      background: #ffffff;
      border: 1.2px solid #cbd5e1;
      border-radius: 6px;
      padding: 7px 10px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.02);
    }

    .card-title-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1.5px solid #0284c7;
      padding-bottom: 3px;
      margin-bottom: 4px;
    }
    .card-title {
      font-size: 9.5pt;
      font-weight: 900;
      color: #0369a1;
    }
    .card-tag {
      font-size: 7.2pt;
      font-weight: 800;
      background: #e0f2fe;
      color: #0284c7;
      padding: 2px 7px;
      border-radius: 3px;
      text-transform: uppercase;
    }

    /* FULL EXPANDED STEP BOX */
    .step-box {
      background: #f8fafc;
      border: 1.2px solid #e2e8f0;
      border-radius: 5px;
      padding: 6px 9px;
      margin-bottom: 4px;
    }
    .step-head {
      font-weight: 800;
      font-size: 8.2pt;
      color: #0f172a;
      display: flex;
      justify-content: space-between;
      margin-bottom: 3px;
      border-bottom: 1px dashed #cbd5e1;
      padding-bottom: 2px;
    }

    .calc-row {
      font-family: "Cambria Math", "Segoe UI", sans-serif;
      font-size: 8pt;
      line-height: 1.5;
      padding: 3px 6px;
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-left: 3.5px solid #0284c7;
      border-radius: 3px;
      margin: 3px 0;
    }
    .calc-row-green {
      border-left-color: #16a34a;
      background: #f0fdf4;
    }

    .sub-expl {
      font-size: 7.2pt;
      color: #475569;
      margin-top: 1px;
    }

    .grid-2col {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 7px;
    }

    .ans-tag {
      display: inline-block;
      font-weight: 800;
      color: #15803d;
      background: #dcfce7;
      padding: 3px 9px;
      border-radius: 4px;
      font-size: 8.2pt;
    }

    .footer {
      border-top: 1px solid #cbd5e1;
      padding-top: 3px;
      display: flex;
      justify-content: space-between;
      font-size: 7pt;
      color: #64748b;
      margin-top: 3px;
    }
  </style>
</head>
<body>

  <!-- HEADER -->
  <div class="header">
    <div>
      <h1>Завдання 6 Варіанта 12 • Повний розв'язок БЕЗ скорочень</h1>
      <p>НУ «Львівська політехніка» • Теорія ймовірностей • Схема Бернуллі з повною підстановкою в P<sub>n</sub>(k) = C<sub>n</sub><sup>k</sup> · p<sup>k</sup> · q<sup>n−k</sup></p>
    </div>
    <div class="badge">
      ВАРІАНТ № 12<br>
      Покроковий вивід
    </div>
  </div>

  <div class="section-grid">

    <!-- BLOCK 1: CANONICAL FORMULA & PARAMETERS -->
    <div class="card" style="background: #eff6ff; border-color: #3b82f6;">
      <div class="card-title-row" style="border-bottom-color: #3b82f6;">
        <span class="card-title" style="color: #1d4ed8;">Базові дані та канонічна формула Бернуллі (Без жодних трюків)</span>
        <span class="card-tag" style="background: #dbeafe; color: #1d4ed8;">Еталон</span>
      </div>
      <p style="font-size: 7.8pt; line-height: 1.4;">
        <b>Умова:</b> Підкидається гральна кістка. Що ймовірніше: з <b>5 підкидань не більше 2 разів</b> випаде парне число чи з <b>7 підкидань не менше 3 разів</b> випаде парне число?<br>
        <b>Окремий дослід:</b> Кістка має грані {1, 2, 3, 4, 5, 6}. Парні: {2, 4, 6} (3 успішні грані з 6).<br>
        • Ймовірність успіху: <b>p = 3/6 = 1/2</b>.<br>
        • Ймовірність невдачі (непарне): <b>q = 1 − p = 1 − 1/2 = 1/2</b>.<br>
        <b>Канонічна формула Бернуллі:</b> &nbsp; <b style="font-size: 8.8pt; color: #1d4ed8;">P<sub>n</sub>(k) = C<sub>n</sub><sup>k</sup> · p<sup>k</sup> · q<sup>n−k</sup> = C<sub>n</sub><sup>k</sup> · (1/2)<sup>k</sup> · (1/2)<sup>n−k</sup></b>
      </p>
    </div>

    <!-- BLOCK 2: SCENARIO 1 (n = 5) STEP BY STEP -->
    <div class="card">
      <div class="card-title-row">
        <span class="card-title">Сценарій 1: n = 5 підкидань, подія A = «не більше 2 разів» (k = 0, k = 1 або k = 2)</span>
        <span class="card-tag">n = 5, k ≤ 2</span>
      </div>
      <p style="font-size: 7.5pt; margin-bottom: 3px;">
        Рахуємо <b>кожен доданок окремо</b> за повною формулою Бернуллі: P(A) = P<sub>5</sub>(0) + P<sub>5</sub>(1) + P<sub>5</sub>(2).
      </p>

      <div class="calc-row">
        <b>1) Рівно 0 разів (k = 0):</b><br>
        P<sub>5</sub>(0) = C<sub>5</sub><sup>0</sup> · (1/2)<sup>0</sup> · (1/2)<sup>5−0</sup> = 1 · 1 · (1/2)<sup>5</sup> = 1 · 1 · <sup>1</sup>/<sub>32</sub> = <b><sup>1</sup>/<sub>32</sub></b>
      </div>

      <div class="calc-row">
        <b>2) Рівно 1 раз (k = 1):</b><br>
        P<sub>5</sub>(1) = C<sub>5</sub><sup>1</sup> · (1/2)<sup>1</sup> · (1/2)<sup>5−1</sup> = 5 · (1/2) · (1/2)<sup>4</sup> = 5 · <sup>1</sup>/<sub>2</sub> · <sup>1</sup>/<sub>16</sub> = 5 · <sup>1</sup>/<sub>32</sub> = <b><sup>5</sup>/<sub>32</sub></b>
      </div>

      <div class="calc-row">
        <b>3) Рівно 2 рази (k = 2):</b><br>
        P<sub>5</sub>(2) = C<sub>5</sub><sup>2</sup> · (1/2)<sup>2</sup> · (1/2)<sup>5−2</sup> = <sup>(5 · 4)</sup>/<sub>2</sub> · (1/2)<sup>2</sup> · (1/2)<sup>3</sup> = 10 · <sup>1</sup>/<sub>4</sub> · <sup>1</sup>/<sub>8</sub> = 10 · <sup>1</sup>/<sub>32</sub> = <b><sup>10</sup>/<sub>32</sub></b>
      </div>

      <div class="calc-row" style="background: #f0fdf4; border-left-color: #16a34a; font-weight: 700;">
        Сума ймовірностей для Сценарію 1:<br>
        P(A) = <sup>1</sup>/<sub>32</sub> + <sup>5</sup>/<sub>32</sub> + <sup>10</sup>/<sub>32</sub> = <sup>(1 + 5 + 10)</sup>/<sub>32</sub> = <sup>16</sup>/<sub>32</sub> = <b>0,50 &nbsp; (50%)</b>
      </div>
    </div>

    <!-- BLOCK 3: SCENARIO 2 (n = 7) STEP BY STEP -->
    <div class="card">
      <div class="card-title-row">
        <span class="card-title">Сценарій 2: n = 7 підкидань, подія B = «не менше 3 разів» (k ≥ 3)</span>
        <span class="card-tag" style="background: #dcfce7; color: #15803d;">n = 7, k ≥ 3</span>
      </div>
      <p style="font-size: 7.5pt; margin-bottom: 3px;">
        Подія B означає k ∈ {3, 4, 5, 6, 7}. Щоб не рахувати 5 довгих формул, беремо протилежну подію B̄ = «не більше 2 разів» (k = 0, 1, 2):
      </p>

      <div class="calc-row">
        <b>1) Рівно 0 разів (k = 0):</b><br>
        P<sub>7</sub>(0) = C<sub>7</sub><sup>0</sup> · (1/2)<sup>0</sup> · (1/2)<sup>7−0</sup> = 1 · 1 · (1/2)<sup>7</sup> = 1 · 1 · <sup>1</sup>/<sub>128</sub> = <b><sup>1</sup>/<sub>128</sub></b>
      </div>

      <div class="calc-row">
        <b>2) Рівно 1 раз (k = 1):</b><br>
        P<sub>7</sub>(1) = C<sub>7</sub><sup>1</sup> · (1/2)<sup>1</sup> · (1/2)<sup>7−1</sup> = 7 · (1/2) · (1/2)<sup>6</sup> = 7 · <sup>1</sup>/<sub>2</sub> · <sup>1</sup>/<sub>64</sub> = 7 · <sup>1</sup>/<sub>128</sub> = <b><sup>7</sup>/<sub>128</sub></b>
      </div>

      <div class="calc-row">
        <b>3) Рівно 2 рази (k = 2):</b><br>
        P<sub>7</sub>(2) = C<sub>7</sub><sup>2</sup> · (1/2)<sup>2</sup> · (1/2)<sup>7−2</sup> = <sup>(7 · 6)</sup>/<sub>2</sub> · (1/2)<sup>2</sup> · (1/2)<sup>5</sup> = 21 · <sup>1</sup>/<sub>4</sub> · <sup>1</sup>/<sub>32</sub> = 21 · <sup>1</sup>/<sub>128</sub> = <b><sup>21</sup>/<sub>128</sub></b>
      </div>

      <div class="calc-row" style="background: #fef2f2; border-left-color: #dc2626;">
        Сума протилежної події B̄:<br>
        P(B̄) = P<sub>7</sub>(0) + P<sub>7</sub>(1) + P<sub>7</sub>(2) = <sup>1</sup>/<sub>128</sub> + <sup>7</sup>/<sub>128</sub> + <sup>21</sup>/<sub>128</sub> = <sup>(1 + 7 + 21)</sup>/<sub>128</sub> = <b><sup>29</sup>/<sub>128</sub></b>
      </div>

      <div class="calc-row calc-row-green" style="font-weight: 700;">
        Шукана ймовірність події B (через 1 − P(B̄)):<br>
        P(B) = 1 − P(B̄) = 1 − <sup>29</sup>/<sub>128</sub> = <sup>(128 − 29)</sup>/<sub>128</sub> = <b><sup>99</sup>/<sub>128</sub> ≈ 0,7734 &nbsp; (77,34%)</b>
      </div>
    </div>

    <!-- BLOCK 4: DIRECT COMPARISON -->
    <div class="card" style="background: #ecfdf5; border: 1.5px solid #16a34a;">
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
          <b style="color: #166534; font-size: 8.5pt;">Остаточне порівняння та висновок:</b><br>
          <span style="font-size: 8pt; color: #1e293b;">
            Ймовірність 1-го варіанта: <b>P(A) = 16/32 = 0,50</b> (50%)<br>
            Ймовірність 2-го варіанта: <b>P(B) = 99/128 ≈ 0,7734</b> (77,34%)
          </span>
        </div>
        <div>
          <span class="ans-tag" style="font-size: 9pt;">P(B) = 0,7734 &gt; P(A) = 0,50 ⇒ Ймовірніше з 7 підкидань не менше 3 разів!</span>
        </div>
      </div>
    </div>

  </div>

  <!-- FOOTER -->
  <div class="footer">
    <span>НУ «Львівська політехніка» • Кафедра ОМП • Студент: Лемішка Андрій (ПП-24)</span>
    <span>Опорний лист: Тема 6 (Схема Бернуллі без скорочень) • Формат А4 • 300 DPI</span>
  </div>

</body>
</html>
'''

temp_html = os.path.join(os.environ.get('TEMP', '.'), 'task6_no_simplification_a4.html')
temp_pdf = os.path.join(os.environ.get('TEMP', '.'), 'task6_no_simplification_a4.pdf')
final_html = 'task6_no_simplification_a4.html'
final_pdf = 'task6_no_simplification_a4.pdf'
final_png = 'task6_no_simplification_a4.png'

with open(temp_html, 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(final_html, 'w', encoding='utf-8') as f:
    f.write(html_content)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

cmd_pdf = [
    chrome_path,
    '--headless',
    '--disable-gpu',
    '--no-pdf-header-footer',
    f'--print-to-pdf={temp_pdf}',
    '--virtual-time-budget=9000',
    temp_html
]
subprocess.run(cmd_pdf, check=True)

shutil.copy(temp_pdf, final_pdf)

doc = pymupdf.open(temp_pdf)
page = doc[0]
zoom = 300 / 72  # 300 DPI
mat = pymupdf.Matrix(zoom, zoom)
pix = page.get_pixmap(matrix=mat, alpha=False)
pix.save(final_png)
print(f"Clean PNG rendered: {final_png} ({pix.width}x{pix.height})")
