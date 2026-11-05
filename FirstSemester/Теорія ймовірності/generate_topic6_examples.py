# -*- coding: utf-8 -*-
"""
Генерація ідеального опорного листа А4 по Темі 6: Схема Бернуллі.
Використовує чистий HTML/CSS без KaTeX escape-проблем для 100% чіткого рендеру.
"""

import subprocess
import os
import shutil
import pymupdf

html_content = r'''<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <title>Теорія Ймовірностей — Тема 6: Схема Бернуллі та Анатомія Формули</title>
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
      background: #0369a1;
      color: #ffffff;
      border-radius: 6px;
      padding: 8px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }
    .header h1 {
      font-size: 13.5pt;
      font-weight: 900;
      letter-spacing: -0.2px;
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

    /* GRID SECTIONS */
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
      font-size: 9.2pt;
      font-weight: 900;
      color: #0369a1;
    }
    .card-tag {
      font-size: 7pt;
      font-weight: 800;
      background: #e0f2fe;
      color: #0284c7;
      padding: 1.5px 7px;
      border-radius: 3px;
      text-transform: uppercase;
    }

    /* FORMULA BREAKDOWN BANNER */
    .anatomy-box {
      background: #f0fdf4;
      border: 1.5px solid #16a34a;
      border-radius: 6px;
      padding: 7px 12px;
    }
    .anatomy-formula {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 12px;
      margin: 5px 0;
      background: #ffffff;
      border-radius: 5px;
      padding: 6px 10px;
      border: 1px dashed #86efac;
    }
    .part-box {
      text-align: center;
      padding: 3px 8px;
      border-radius: 4px;
    }
    .part-math {
      font-size: 13pt;
      font-weight: 900;
      font-family: "Cambria Math", "Times New Roman", serif;
    }
    .part-label {
      font-size: 7.2pt;
      font-weight: 700;
      margin-top: 1px;
    }
    .part-c { color: #2563eb; background: #eff6ff; }
    .part-p { color: #16a34a; background: #f0fdf4; }
    .part-q { color: #dc2626; background: #fef2f2; }
    .part-res { color: #0f172a; background: #f1f5f9; }

    .read-aloud {
      background: #f8fafc;
      border-left: 4px solid #0284c7;
      padding: 5px 9px;
      font-size: 8pt;
      line-height: 1.4;
      color: #1e293b;
      margin-top: 4px;
      border-radius: 0 4px 4px 0;
    }
    .read-aloud b { color: #0369a1; }

    /* TWO COLUMNS CARDS */
    .grid-2col {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 7px;
    }

    /* MINI EXAMPLES */
    .example-title {
      font-size: 8pt;
      font-weight: 800;
      color: #0f172a;
      display: flex;
      justify-content: space-between;
      margin-bottom: 2px;
    }
    .formula-row {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 3.5px solid #0284c7;
      border-radius: 3px;
      padding: 4px 7px;
      margin: 3px 0;
      font-size: 7.6pt;
      line-height: 1.35;
      font-family: "Cambria Math", "Segoe UI", sans-serif;
    }
    .formula-row-green {
      border-left-color: #16a34a;
      background: #f0fdf4;
    }
    .formula-row-purple {
      border-left-color: #7c3aed;
      background: #faf5ff;
    }

    .ans-tag {
      display: inline-block;
      font-weight: 800;
      color: #15803d;
      background: #dcfce7;
      padding: 2px 7px;
      border-radius: 3px;
      font-size: 7.6pt;
    }

    /* FOOTER */
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
      <h1>Схема Бернуллі • Анатомія Формули та Практичні Приклади</h1>
      <p>НУ «Львівська політехніка» • Кафедра ОМП • Студент: Лемішка Андрій (ПП-24) • Варіант № 12</p>
    </div>
    <div class="badge">
      ТЕМА 6<br>
      Шпаргалка А4
    </div>
  </div>

  <div class="section-grid">

    <!-- BLOCK 1: ANATOMY & HOW TO READ ALOUD -->
    <div class="card anatomy-box">
      <div class="card-title-row" style="border-bottom-color: #16a34a;">
        <span class="card-title" style="color: #15803d; font-size: 10pt;">1. Як правильно читається та розбирається формула Бернуллі</span>
        <span class="card-tag" style="background: #dcfce7; color: #16a34a;">Анатомія формули</span>
      </div>

      <div class="anatomy-formula">
        <div class="part-box part-res">
          <div class="part-math">P<sub>n</sub>(k)</div>
          <div class="part-label">Шанс k успіхів</div>
        </div>
        <div style="font-weight:900; font-size:14pt; color:#64748b;">=</div>
        <div class="part-box part-c">
          <div class="part-math">C<sub>n</sub><sup>k</sup></div>
          <div class="part-label">Комбінації чергування</div>
        </div>
        <div style="font-weight:900; font-size:14pt; color:#64748b;">·</div>
        <div class="part-box part-p">
          <div class="part-math">p<sup>k</sup></div>
          <div class="part-label">Ймовірність k успіхів</div>
        </div>
        <div style="font-weight:900; font-size:14pt; color:#64748b;">·</div>
        <div class="part-box part-q">
          <div class="part-math">q<sup>n−k</sup></div>
          <div class="part-label">Ймовірність (n−k) невдач</div>
        </div>
      </div>

      <div class="read-aloud">
        📢 <b>Як читати вголос викладачеві:</b><br>
        «Ймовірність того, що в <b>n</b> незалежних випробуваннях подія настане рівно <b>k</b> разів, дорівнює: 
        <b>числу сполучень (комбінацій) з n елементів по k</b>, 
        помноженому на <b>ймовірність успіху p у степені k</b>, 
        і помноженому на <b>ймовірність невдачі q у степені (n − k)</b>».<br>
        <i>(Зверніть увагу: після C<sub>n</sub><sup>k</sup> стоїть <u>не друга комбінація</u>, а <u>добуток імовірностей у відповідних степенях</u>!)</i>
      </div>
    </div>

    <!-- BLOCK 2: VARIANT 12 TASK 6 (HERO TASK) -->
    <div class="card" style="border: 1.5px solid #0284c7;">
      <div class="card-title-row">
        <span class="card-title" style="font-size: 9.8pt;">★ [Пріоритет №1] Завдання 6 Варіанта 12 (РГР): Гральна кістка</span>
        <span class="card-tag" style="background: #0284c7; color: #ffffff;">Варіант 12</span>
      </div>
      <p style="font-size: 7.7pt; margin-bottom: 3px;">
        <b>Умова:</b> Підкидається гральна кістка. Що ймовірніше: з <b>5 підкидань не більше 2 разів</b> випаде парне число, чи з <b>7 підкидань не менше 3 разів</b> випаде парне число?
      </p>
      <div style="font-size: 7.4pt; color: #475569; margin-bottom: 4px;">
        Базові параметри: парні {2, 4, 6} ⇒ <b>p = 3/6 = 1/2</b>, невдача <b>q = 1 − 1/2 = 1/2</b>. Оскільки p = q = 1/2, формула спрощується: <b>P<sub>n</sub>(k) = C<sub>n</sub><sup>k</sup> / 2<sup>n</sup></b>.
      </div>

      <div class="grid-2col">
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; padding: 5px 8px;">
          <div class="example-title">
            <span style="color:#0284c7;">Сценарій 1: n = 5, подія A (k ≤ 2)</span>
            <span>k ∈ {0, 1, 2}</span>
          </div>
          <div class="formula-row">
            C<sub>5</sub><sup>0</sup> = 1, &nbsp; C<sub>5</sub><sup>1</sup> = 5, &nbsp; C<sub>5</sub><sup>2</sup> = (5 · 4) / 2 = 10<br>
            P(A) = P<sub>5</sub>(0) + P<sub>5</sub>(1) + P<sub>5</sub>(2) = (1 + 5 + 10) / 2<sup>5</sup> = <b>16 / 32 = 0,50 (50%)</b>
          </div>
        </div>

        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; padding: 5px 8px;">
          <div class="example-title">
            <span style="color:#16a34a;">Сценарій 2: n = 7, подія B (k ≥ 3)</span>
            <span>k ∈ {3, 4, 5, 6, 7}</span>
          </div>
          <div class="formula-row formula-row-green">
            Протилежна подія B̄ (k ≤ 2): C<sub>7</sub><sup>0</sup> = 1, C<sub>7</sub><sup>1</sup> = 7, C<sub>7</sub><sup>2</sup> = (7 · 6) / 2 = 21<br>
            P(B̄) = (1 + 7 + 21) / 2<sup>7</sup> = 29 / 128 ⇒ <b>P(B) = 1 − 29/128 = 99/128 ≈ 0,7734 (77,34%)</b>
          </div>
        </div>
      </div>
      <div style="margin-top: 4px; font-size: 7.7pt; display: flex; justify-content: space-between; align-items: center; background: #ecfdf5; padding: 3px 8px; border-radius: 3px;">
        <span style="font-weight: 700; color: #166534;">Порівняння та висновок:</span>
        <span class="ans-tag">P(B) = 99/128 (≈77,34%) &gt; P(A) = 1/2 (50%) ⇒ Ймовірніше з 7 підкидань не менше 3 разів!</span>
      </div>
    </div>

    <!-- BLOCK 3: TICKET TASK 6 & MODE CALCULATION -->
    <div class="grid-2col">
      
      <!-- Ticket 6 -->
      <div class="card" style="border-left: 4px solid #7c3aed;">
        <div class="card-title-row" style="border-bottom-color: #7c3aed;">
          <span class="card-title" style="color: #7c3aed;">★ [Пріоритет №2] Типовий білет ПК-1 (№ 6)</span>
          <span class="card-tag" style="background: #ede9fe; color: #7c3aed;">Білет ОМП</span>
        </div>
        <p style="font-size: 7.4pt; margin-bottom: 2px;">
          <b>Умова:</b> Ймовірність появи події хоч би один раз у 4 незалежних дослідах дорівнює <b>0,8704</b>. Знайти ймовірність <i>p</i> в 1 досліді.
        </p>
        <div class="formula-row formula-row-purple">
          Формула «хоча б 1 раз»: P<sub>4</sub>(k ≥ 1) = 1 − q<sup>4</sup><br>
          1 − q<sup>4</sup> = 0,8704 &nbsp;⇒&nbsp; q<sup>4</sup> = 0,1296<br>
          q = <sup>4</sup>√0,1296 = 0,6 &nbsp;⇒&nbsp; <b>p = 1 − 0,6 = 0,4</b>
        </div>
        <div style="text-align: right; margin-top: 2px;">
          <span class="ans-tag" style="background:#ede9fe; color:#6d28d9;">Правильна відповідь у білеті: Д) 0,4</span>
        </div>
      </div>

      <!-- Mode Calculation k0 -->
      <div class="card" style="border-left: 4px solid #f59e0b;">
        <div class="card-title-row" style="border-bottom-color: #f59e0b;">
          <span class="card-title" style="color: #d97706;">Найімовірніше число успіхів k₀ (Мода)</span>
          <span class="card-tag" style="background: #fef3c7; color: #b45309;">Теорія + Приклад</span>
        </div>
        <p style="font-size: 7.4pt; margin-bottom: 2px;">
          <b>Подвійна нерівність:</b> n·p − q ≤ k₀ ≤ n·p + p &nbsp;(довжина інтервалу = 1).
        </p>
        <div class="formula-row" style="border-left-color: #f59e0b; background: #fffbeb;">
          <b>Приклад:</b> Монету кидають n = 15 разів (p = 0,5, q = 0,5):<br>
          15·0,5 − 0,5 ≤ k₀ ≤ 15·0,5 + 0,5 &nbsp;⇒&nbsp; <b>7 ≤ k₀ ≤ 8</b><br>
          Оскільки обидва числа цілі: <b>два значення k₀ = 7 та k₀ = 8</b>.
        </div>
        <div style="text-align: right; margin-top: 2px;">
          <span class="ans-tag" style="background:#fef3c7; color:#b45309;">Шанс P₁₅(7) = P₁₅(8) = 19,64%</span>
        </div>
      </div>

    </div>

    <!-- BLOCK 4: TWO REAL LIFE APPLIED EXAMPLES (PRODUCTION & ACCURACY) -->
    <div class="grid-2col">
      
      <!-- Example A: Factory Defect -->
      <div class="card">
        <div class="card-title-row">
          <span class="card-title">Приклад А: Контроль якості (Брак деталей)</span>
          <span class="card-tag">Виробництво</span>
        </div>
        <p style="font-size: 7.4pt; margin-bottom: 2px;">
          <b>Задача:</b> Ймовірність бракованої деталі p = 0,1 (10%). Навмання взято n = 4 деталі. Яка ймовірність, що бракована рівно k = 1 деталь?
        </p>
        <div class="formula-row">
          n = 4, k = 1, p = 0,1, q = 0,9<br>
          P<sub>4</sub>(1) = C<sub>4</sub><sup>1</sup> · (0,1)<sup>1</sup> · (0,9)<sup>4−1</sup> = 4 · 0,1 · 0,729 = <b>0,2916 (29,16%)</b>
        </div>
        <div style="font-size: 7pt; color: #475569;">
          Пояснення: C<sub>4</sub><sup>1</sup> = 4 варіанти чергування (БССС, СБСС, ССБС, СССБ), кожен з шансом 0,1·0,9<sup>3</sup>.
        </div>
      </div>

      <!-- Example B: Target Shooting -->
      <div class="card">
        <div class="card-title-row">
          <span class="card-title">Приклад Б: Стрільба по мішені (Влучність)</span>
          <span class="card-tag">Стрільба</span>
        </div>
        <p style="font-size: 7.4pt; margin-bottom: 2px;">
          <b>Задача:</b> Стрілець влучає в мішень з шансом p = 0,8 (80%). Зроблено n = 5 пострілів. Яка ймовірність влучити рівно k = 4 рази?
        </p>
        <div class="formula-row formula-row-green">
          n = 5, k = 4, p = 0,8, q = 0,2<br>
          P<sub>5</sub>(4) = C<sub>5</sub><sup>4</sup> · (0,8)<sup>4</sup> · (0,2)<sup>1</sup> = 5 · 0,4096 · 0,2 = <b>0,4096 (40,96%)</b>
        </div>
        <div style="font-size: 7pt; color: #475569;">
          Пояснення: C<sub>5</sub><sup>4</sup> = 5 способів розташувати 1 єдиний промах серед 5 здійснених пострілів.
        </div>
      </div>

    </div>

  </div>

  <!-- FOOTER -->
  <div class="footer">
    <span>НУ «Львівська політехніка» • Інститут комп'ютерних наук (ІКНІ) • Кафедра ОМП</span>
    <span>Опорний лист Теми 6 (Схема Бернуллі) • Формат А4 • 300 DPI</span>
  </div>

</body>
</html>
'''

temp_html = os.path.join(os.environ.get('TEMP', '.'), 'topic6_examples_a4.html')
temp_pdf = os.path.join(os.environ.get('TEMP', '.'), 'topic6_examples_a4.pdf')
final_html = 'topic6_examples_a4.html'
final_pdf = 'topic6_examples_a4.pdf'
final_png = 'topic6_examples_a4.png'

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
