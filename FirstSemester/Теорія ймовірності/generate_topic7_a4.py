# -*- coding: utf-8 -*-
"""
Генерація красивого опорного листа А4 по Темі 7: Дискретні випадкові величини (ДВВ).
Включає:
- Теорію: Ряд розподілу, властивості ймовірностей, F(x), M[X], D[X], сигма.
- [Пріоритет №1] Завдання 7 Варіанта 12 (РГР): ДВВ з двома значеннями, M=3.2, D=0.15.
- [Пріоритет №2] Завдання 7 з Типового білета ПК-1: Вибірка 2 кульок з 5, найменший номер, покрокова побудова F(x) з векторним графіком сходинок.
- [Пріоритет №2] Завдання 8 з Типового білета ПК-1: Обчислення M[X] за таблицею при k=0.
- Властивості математичного сподівання та дисперсії (M[C], D[C], M[CX], D[CX], M[X+Y], D[X+Y]).
"""

import subprocess
import os
import shutil
import pymupdf

html_content = r'''<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <title>Теорія Ймовірностей — Тема 7: Дискретні випадкові величини (ДВВ)</title>
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
      background: #0f766e;
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
      color: #ccfbf1;
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
      gap: 6px;
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
      border-bottom: 1.5px solid #0f766e;
      padding-bottom: 3px;
      margin-bottom: 4px;
    }
    .card-title {
      font-size: 9.2pt;
      font-weight: 900;
      color: #0f766e;
    }
    .card-tag {
      font-size: 7pt;
      font-weight: 800;
      background: #ccfbf1;
      color: #0f766e;
      padding: 1.5px 7px;
      border-radius: 3px;
      text-transform: uppercase;
    }

    .grid-2col {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 7px;
    }

    /* TABLES */
    .dist-table {
      width: 100%;
      border-collapse: collapse;
      margin: 3px 0;
      font-family: "Cambria Math", "Segoe UI", sans-serif;
      font-size: 7.8pt;
      text-align: center;
    }
    .dist-table th, .dist-table td {
      border: 1px solid #94a3b8;
      padding: 2.5px 4px;
    }
    .dist-table th {
      background: #f1f5f9;
      font-weight: 800;
      width: 16%;
    }

    /* CODE & MATH BOXES */
    .calc-row {
      font-family: "Cambria Math", "Segoe UI", sans-serif;
      font-size: 7.6pt;
      line-height: 1.35;
      padding: 4px 7px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 3.5px solid #0f766e;
      border-radius: 3px;
      margin: 2.5px 0;
    }
    .calc-row-blue {
      border-left-color: #0284c7;
      background: #f0f9ff;
    }
    .calc-row-purple {
      border-left-color: #7c3aed;
      background: #faf5ff;
    }
    .calc-row-amber {
      border-left-color: #d97706;
      background: #fffbeb;
    }

    .ans-tag {
      display: inline-block;
      font-weight: 800;
      color: #0f766e;
      background: #ccfbf1;
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
      <h1>Тема 7: Дискретні Випадкові Величини (ДВВ) • Опорний Конспект</h1>
      <p>НУ «Львівська політехніка» • Кафедра ОМП • Студент: Лемішка Андрій (ПП-24) • Варіант № 12</p>
    </div>
    <div class="badge">
      ТЕМА 7<br>
      Шпаргалка А4
    </div>
  </div>

  <div class="section-grid">

    <!-- BLOCK 1: CORE THEORY & FORMULAS -->
    <div class="card" style="border: 1.5px solid #0f766e;">
      <div class="card-title-row">
        <span class="card-title">1. Теорія ДВВ: Ряд розподілу, Функція накопичення F(x) та Характеристики</span>
        <span class="card-tag">Фундамент</span>
      </div>
      <div class="grid-2col">
        <div>
          <p style="font-size: 7.4pt; margin-bottom: 2px;">
            <b>Ряд розподілу:</b> Таблиця пар (x<sub>i</sub>, p<sub>i</sub>). Умова нормування: <b>∑ p<sub>i</sub> = 1</b>.<br>
            <b>Функція розподілу F(x) = P(X &lt; x):</b> неспадна, неперервна зліва, 0 ≤ F(x) ≤ 1.<br>
            • F(−∞) = 0, &nbsp; F(+∞) = 1, &nbsp; P(a ≤ X &lt; b) = F(b) − F(a).
          </p>
          <div class="calc-row">
            <b>Математичне сподівання (центр):</b> M[X] = ∑ x<sub>i</sub> · p<sub>i</sub><br>
            <b>Дисперсія (розкид):</b> D[X] = M[X<sup>2</sup>] − (M[X])<sup>2</sup> = ∑ x<sub>i</sub><sup>2</sup>·p<sub>i</sub> − (M[X])<sup>2</sup><br>
            <b>Середнє квадратичне відхилення:</b> σ<sub>X</sub> = √D[X]
          </div>
        </div>

        <div>
          <p style="font-size: 7.4pt; margin-bottom: 2px;">
            <b>Основні властивості математичного сподівання та дисперсії:</b>
          </p>
          <div class="calc-row calc-row-amber">
            • <b>M[C] = C</b>, &nbsp; <b>D[C] = 0</b> &nbsp; (для сталої C)<br>
            • <b>M[C · X] = C · M[X]</b>, &nbsp; <b>D[C · X] = C<sup>2</sup> · D[X]</b><br>
            • <b>M[X ± Y] = M[X] ± M[Y]</b> &nbsp; (завжди!)<br>
            • <b>D[X ± Y] = D[X] + D[Y]</b> &nbsp; (якщо X та Y <u>незалежні</u>)<br>
            • Для двох значень: <b>D[X] = p<sub>1</sub> · p<sub>2</sub> · (x<sub>2</sub> − x<sub>1</sub>)<sup>2</sup></b>
          </div>
        </div>
      </div>
    </div>

    <!-- BLOCK 2: VARIANT 12 TASK 7 (HERO TASK) -->
    <div class="card" style="border: 1.5px solid #0284c7;">
      <div class="card-title-row" style="border-bottom-color: #0284c7;">
        <span class="card-title" style="color: #0284c7;">★ [Пріоритет №1] Завдання 7 Варіанта 12 (РГР): ДВВ з двома значеннями</span>
        <span class="card-tag" style="background: #0284c7; color: #ffffff;">Варіант 12</span>
      </div>
      <p style="font-size: 7.6pt; margin-bottom: 3px;">
        <b>Умова:</b> Знайти закон розподілу випадкової величини ξ, яка набуває лише два значення: x<sub>1</sub> з імовірністю p<sub>1</sub> = 0,3 і x<sub>2</sub>, якщо x<sub>1</sub> &lt; x<sub>2</sub>, математичне сподівання <b>Mξ = 3,2</b>, а дисперсія <b>Dξ = 0,15</b>.
      </p>

      <div class="grid-2col">
        <div>
          <div class="calc-row calc-row-blue">
            <b>Крок 1. Знаходимо ймовірність p<sub>2</sub>:</b><br>
            p<sub>1</sub> + p<sub>2</sub> = 1 ⇒ p<sub>2</sub> = 1 − 0,3 = <b>0,7</b><br>
            <b>Крок 2. Рівняння сподівання:</b><br>
            Mξ = 0,3·x<sub>1</sub> + 0,7·x<sub>2</sub> = 3,2 &nbsp;— <i>(Рівняння 1)</i><br>
            <b>Крок 3. Формула дисперсії для двох значень:</b><br>
            Dξ = p<sub>1</sub> · p<sub>2</sub> · (x<sub>2</sub> − x<sub>1</sub>)<sup>2</sup><br>
            0,15 = 0,3 · 0,7 · (x<sub>2</sub> − x<sub>1</sub>)<sup>2</sup> = 0,21 · (x<sub>2</sub> − x<sub>1</sub>)<sup>2</sup><br>
            (x<sub>2</sub> − x<sub>1</sub>)<sup>2</sup> = <sup>0,15</sup>/<sub>0,21</sub> = <b><sup>5</sup>/<sub>7</sub></b> ⇒ x<sub>2</sub> − x<sub>1</sub> = √(5/7)
          </div>
        </div>

        <div>
          <div class="calc-row calc-row-blue">
            <b>Крок 4. Знаходимо значення x<sub>1</sub> та x<sub>2</sub>:</b><br>
            З кроку 3: x<sub>2</sub> = x<sub>1</sub> + √(5/7). Підставляємо в Рівняння 1:<br>
            0,3·x<sub>1</sub> + 0,7·(x<sub>1</sub> + √(5/7)) = 3,2<br>
            1·x<sub>1</sub> + 0,7·√(5/7) = 3,2 &nbsp; [0,7·√(5/7) = 0,7·0,84515 ≈ 0,5916]<br>
            <b>x<sub>1</sub> = 3,2 − 0,5916 = 2,6084 ≈ 2,61</b><br>
            <b>x<sub>2</sub> = 2,6084 + 0,8452 = 3,4536 ≈ 3,45</b><br>
            <i>Перевірка M: 0,3·2,6084 + 0,7·3,4536 = 0,7825 + 2,4175 = 3,2000!</i>
          </div>
        </div>
      </div>

      <div style="margin-top: 4px; display: flex; justify-content: space-between; align-items: center; background: #f0fdf4; padding: 4px 10px; border-radius: 4px; border: 1px solid #bbf7d0;">
        <span style="font-weight: 800; font-size: 7.8pt; color: #166534;">Шуканий ряд розподілу Варіанта 12:</span>
        <div style="width: 50%;">
          <table class="dist-table" style="margin: 0; background: white;">
            <tr><th>ξ</th><td>x<sub>1</sub> ≈ <b>2,61</b></td><td>x<sub>2</sub> ≈ <b>3,45</b></td></tr>
            <tr><th>p</th><td><b>0,3</b></td><td><b>0,7</b></td></tr>
          </table>
        </div>
      </div>
    </div>

    <!-- BLOCK 3: TICKET TASK 7 & TASK 8 -->
    <div class="grid-2col">
      
      <!-- Ticket Task 7 -->
      <div class="card" style="border-left: 4px solid #7c3aed;">
        <div class="card-title-row" style="border-bottom-color: #7c3aed;">
          <span class="card-title" style="color: #7c3aed;">★ [Пріоритет №2] Білет ПК-1 (№ 7): Функція F(x)</span>
          <span class="card-tag" style="background: #ede9fe; color: #7c3aed;">Білет ОМП</span>
        </div>
        <p style="font-size: 7.2pt; margin-bottom: 2px;">
          <b>Умова:</b> У скриньці 5 кульок з № 1..5. Виймають 2 кульки. X — <b>найменший номер</b>. Записати функцію розподілу F(x).
        </p>
        <div class="calc-row calc-row-purple" style="font-size: 7.3pt;">
          Всього пар: n = C<sub>5</sub><sup>2</sup> = 10. Можливі X ∈ {1, 2, 3, 4}:<br>
          • X = 1: пари {1,2},{1,3},{1,4},{1,5} (4 пари) ⇒ <b>p<sub>1</sub> = 4/10 = 0,4</b><br>
          • X = 2: пари {2,3},{2,4},{2,5} (3 пари) ⇒ <b>p<sub>2</sub> = 3/10 = 0,3</b><br>
          • X = 3: пари {3,4},{3,5} (2 пари) ⇒ <b>p<sub>3</sub> = 2/10 = 0,2</b><br>
          • X = 4: пара {4,5} (1 пара) ⇒ <b>p<sub>4</sub> = 1/10 = 0,1</b><br>
          <b>Накопичувальні сходинки F(x) = P(X &lt; x):</b><br>
          F(x) = <b>0</b> (x ≤ 1); &nbsp; <b>0,4</b> (1 &lt; x ≤ 2); &nbsp; <b>0,7</b> (2 &lt; x ≤ 3);<br>
          F(x) = <b>0,9</b> (3 &lt; x ≤ 4); &nbsp; <b>1</b> (x &gt; 4).
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 3px;">
          <!-- SVG Mini Step Chart -->
          <svg width="150" height="42" viewBox="0 0 150 42" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:3px;">
            <line x1="15" y1="36" x2="145" y2="36" stroke="#94a3b8" stroke-width="1"/>
            <line x1="20" y1="38" x2="20" y2="4" stroke="#94a3b8" stroke-width="1"/>
            <!-- steps -->
            <line x1="5" y1="36" x2="35" y2="36" stroke="#7c3aed" stroke-width="2"/>
            <line x1="35" y1="24" x2="65" y2="24" stroke="#7c3aed" stroke-width="2"/>
            <line x1="65" y1="15" x2="95" y2="15" stroke="#7c3aed" stroke-width="2"/>
            <line x1="95" y1="9" x2="125" y2="9" stroke="#7c3aed" stroke-width="2"/>
            <line x1="125" y1="6" x2="145" y2="6" stroke="#7c3aed" stroke-width="2"/>
            <!-- labels -->
            <text x="35" y="41" font-size="6" fill="#475569" text-anchor="middle">1</text>
            <text x="65" y="41" font-size="6" fill="#475569" text-anchor="middle">2</text>
            <text x="95" y="41" font-size="6" fill="#475569" text-anchor="middle">3</text>
            <text x="125" y="41" font-size="6" fill="#475569" text-anchor="middle">4</text>
            <text x="12" y="8" font-size="6" fill="#7c3aed">1.0</text>
          </svg>
          <span class="ans-tag" style="background:#ede9fe; color:#6d28d9;">Відповідь: Варіант В</span>
        </div>
      </div>

      <!-- Ticket Task 8 -->
      <div class="card" style="border-left: 4px solid #ea580c;">
        <div class="card-title-row" style="border-bottom-color: #ea580c;">
          <span class="card-title" style="color: #ea580c;">★ [Пріоритет №2] Білет ПК-1 (№ 8): Матсподівання M[X]</span>
          <span class="card-tag" style="background: #ffedd5; color: #ea580c;">Білет ОМП</span>
        </div>
        <p style="font-size: 7.2pt; margin-bottom: 2px;">
          <b>Умова:</b> Знайти M(X) для таблиці при <b>k = 0</b>:
        </p>
        <table class="dist-table" style="background: #fffaf5;">
          <tr><th>X</th><td>k − 4 = <b>−4</b></td><td>k − 2 = <b>−2</b></td><td>2 + k = <b>2</b></td><td>3 + k = <b>3</b></td></tr>
          <tr><th>P</th><td><b>0,1</b></td><td><b>0,2</b></td><td><b>0,4</b></td><td><b>0,3</b></td></tr>
        </table>
        <div class="calc-row" style="border-left-color: #ea580c; background: #fffaf5; font-size: 7.4pt; margin-top: 3px;">
          <b>Обчислення за формулою M[X] = ∑ x<sub>i</sub> · p<sub>i</sub>:</b><br>
          M[X] = (−4)·0,1 + (−2)·0,2 + 2·0,4 + 3·0,3<br>
          M[X] = −0,4 − 0,4 + 0,8 + 0,9 = <b>0,9</b><br>
          <span style="font-size: 6.8pt; color: #475569;">Перевірка дисперсії: M[X<sup>2</sup>] = 16·0,1 + 4·0,2 + 4·0,4 + 9·0,3 = 1,6+0,8+1,6+2,7 = 6,7 ⇒ D[X] = 6,7 − 0,9<sup>2</sup> = 5,89.</span>
        </div>
        <div style="text-align: right; margin-top: 2px;">
          <span class="ans-tag" style="background:#ffedd5; color:#c2410c;">Відповідь у білеті: Г) 0,9</span>
        </div>
      </div>

    </div>

    <!-- BLOCK 4: SPECIAL COMMON EXAM PROBLEM -->
    <div class="card" style="background: #f8fafc;">
      <div class="card-title-row">
        <span class="card-title">Типова задача захисту: Відновлення параметра «С» у законі розподілу</span>
        <span class="card-tag">Класика колоквіуму</span>
      </div>
      <div class="grid-2col" style="font-size: 7.3pt;">
        <div>
          <b>Умова:</b> Ряд розподілу містить невідому константу C: &nbsp; P(X = 1) = C, P(X = 2) = 2C, P(X = 3) = 0,4, P(X = 4) = 3C. Знайти C та M[X].<br>
          <b>Розв'язок:</b> За умовою нормування сума всіх ймовірностей рівна 1: &nbsp; C + 2C + 0,4 + 3C = 1 ⇒ 6C = 0,6 ⇒ <b>C = 0,1</b>.
        </div>
        <div>
          Ймовірності: p<sub>1</sub> = 0,1; p<sub>2</sub> = 0,2; p<sub>3</sub> = 0,4; p<sub>4</sub> = 0,3 (збігаються з Завданням 8!).<br>
          <b>M[X]</b> = 1·0,1 + 2·0,2 + 3·0,4 + 4·0,3 = 0,1 + 0,4 + 1,2 + 1,2 = <b>2,9</b>.
        </div>
      </div>
    </div>

  </div>

  <!-- FOOTER -->
  <div class="footer">
    <span>НУ «Львівська політехніка» • Інститут комп'ютерних наук (ІКНІ) • Кафедра ОМП</span>
    <span>Опорний лист Теми 7 (Дискретні випадкові величини) • Формат А4 • 300 DPI</span>
  </div>

</body>
</html>
'''

temp_html = os.path.join(os.environ.get('TEMP', '.'), 'topic7_showcase_a4.html')
temp_pdf = os.path.join(os.environ.get('TEMP', '.'), 'topic7_showcase_a4.pdf')
final_html = 'topic7_showcase_a4.html'
final_pdf = 'topic7_showcase_a4.pdf'
final_png = 'topic7_showcase_a4.png'

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
