# -*- coding: utf-8 -*-
import subprocess
import os
import shutil
import pymupdf

html_content = '''<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <title>Теорія Ймовірностей — Тема 6: Схема Бернуллі</title>
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
      padding: 7mm 8mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    /* HEADER */
    .header {
      border-bottom: 2px solid #0284c7;
      padding-bottom: 4px;
      margin-bottom: 6px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }
    .header-left h1 {
      font-size: 13.5pt;
      font-weight: 900;
      letter-spacing: -0.3px;
      color: #0f172a;
      text-transform: uppercase;
      line-height: 1.1;
    }
    .header-left .sub {
      font-size: 8.5pt;
      font-weight: 700;
      color: #0284c7;
      margin-top: 2px;
    }
    .header-right {
      text-align: right;
      font-size: 7.5pt;
      color: #475569;
      line-height: 1.25;
    }
    .badge-var {
      display: inline-block;
      background: #0284c7;
      color: white;
      font-weight: 800;
      font-size: 7.5pt;
      padding: 2px 7px;
      border-radius: 4px;
    }

    /* GRID LAYOUTS */
    .grid-top {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
      margin-bottom: 6px;
    }
    .grid-bottom {
      display: grid;
      grid-template-columns: 1.1fr 1fr 0.9fr;
      gap: 6px;
    }

    /* CARDS */
    .card {
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 6px 8px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }
    .card-hero {
      border: 1.5px solid #0284c7;
      background: #ffffff;
      margin-bottom: 6px;
      padding: 7px 9px;
    }
    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 4px;
      border-bottom: 1px solid #f1f5f9;
      padding-bottom: 3px;
    }
    .card-title {
      font-size: 8.5pt;
      font-weight: 800;
      color: #0f172a;
    }
    .card-pill {
      font-size: 6.5pt;
      font-weight: 800;
      text-transform: uppercase;
      padding: 1px 5px;
      border-radius: 3px;
      background: #e2e8f0;
      color: #334155;
    }
    .pill-hero {
      background: #0284c7;
      color: #ffffff;
    }
    .pill-purple {
      background: #ede9fe;
      color: #6d28d9;
    }
    .pill-amber {
      background: #fef3c7;
      color: #b45309;
    }
    .pill-emerald {
      background: #dcfce7;
      color: #15803d;
    }
    .pill-rose {
      background: #ffe4e6;
      color: #be123c;
    }

    .card-body {
      font-size: 7.2pt;
      line-height: 1.35;
      color: #334155;
    }
    .card-body p {
      margin-bottom: 3px;
    }

    /* FORMULAS */
    .formula-box {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 3px solid #0284c7;
      border-radius: 4px;
      padding: 3px 6px;
      margin: 3px 0;
      font-family: "Cambria Math", "Times New Roman", serif;
      font-size: 7.8pt;
      color: #0f172a;
    }
    .formula-highlight {
      background: #eff6ff;
      border-left-color: #2563eb;
      font-weight: 700;
    }

    /* HERO SPLIT */
    .hero-split {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
    }
    .subcard {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 5px;
      padding: 5px 7px;
    }
    .subcard-title {
      font-weight: 800;
      font-size: 7.5pt;
      color: #0f172a;
      margin-bottom: 3px;
      display: flex;
      justify-content: space-between;
    }

    /* RESULT CALLOUT */
    .ans-box {
      margin-top: 4px;
      padding: 3px 6px;
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      border-radius: 4px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 7.5pt;
    }
    .ans-box .label {
      font-weight: 700;
      color: #166534;
    }
    .ans-box .val {
      font-weight: 900;
      color: #15803d;
      font-size: 8.5pt;
    }

    /* FOOTER */
    .footer {
      border-top: 1px solid #cbd5e1;
      padding-top: 3px;
      display: flex;
      justify-content: space-between;
      font-size: 6.8pt;
      color: #64748b;
      margin-top: 4px;
    }
  </style>
</head>
<body>

  <!-- HEADER -->
  <div class="header">
    <div class="header-left">
      <h1>Теорія Ймовірностей • Тема 6</h1>
      <div class="sub">Повторні незалежні випробування • Схема Бернуллі та її властивості</div>
    </div>
    <div class="header-right">
      <span class="badge-var">ВАРІАНТ № 12</span><br>
      Студент: <b>Лемішка Андрій (ПП-24)</b> • НУ «Львівська політехніка»
    </div>
  </div>

  <!-- TOP ROW: THEORETICAL FOUNDATION -->
  <div class="grid-top">
    <!-- Top 1: Bernoulli Scheme Definition -->
    <div class="card">
      <div class="card-header">
        <span class="card-title">1. Схема випробувань Бернуллі</span>
        <span class="card-pill pill-purple">Означення</span>
      </div>
      <div class="card-body">
        <p><b>Три необхідні умови схеми Бернуллі:</b></p>
        <p>1. Проводиться фіксована серія з <i>n</i> <b>незалежних</b> дослідів.<br>
        2. Кожен дослід має рівно <b>два наслідки</b>: «успіх» (<i>A</i>) або «невдача» (<i>Ā</i>).<br>
        3. Ймовірність успіху <b>p = P(A)</b> є <b>сталою</b> для всіх дослідів (<i>q = 1 − p</i>).</p>
        <div class="formula-box formula-highlight">
          <b>Формула Бернуллі (рівно k успіхів у n випробуваннях):</b><br>
          P<sub>n</sub>(k) = C<sub>n</sub><sup>k</sup> · p<sup>k</sup> · q<sup>n−k</sup> = [ n! / (k!(n−k)!) ] · p<sup>k</sup> · q<sup>n−k</sup>
        </div>
        <p style="font-size: 6.8pt; color: #64748b;">Сума всіх ймовірностей: ∑<sub>k=0</sub><sup>n</sup> P<sub>n</sub>(k) = (p + q)<sup>n</sup> = 1<sup>n</sup> = 1 (Біном Ньютона).</p>
      </div>
    </div>

    <!-- Top 2: Special Cases & Mode -->
    <div class="card">
      <div class="card-header">
        <span class="card-title">2. Спеціальні випадки та Мода (k₀)</span>
        <span class="card-pill pill-amber">Властивості</span>
      </div>
      <div class="card-body">
        <p><b>1. Ймовірність «хоча б одного успіху» (k ≥ 1):</b></p>
        <div class="formula-box">
          P<sub>n</sub>(k ≥ 1) = 1 − P<sub>n</sub>(0) = <b>1 − q<sup>n</sup></b> &nbsp; (через протилежну подію)
        </div>
        <p><b>2. Найімовірніша кількість успіхів k₀ (мода біноміального розподілу):</b></p>
        <p>Число <i>k₀</i>, при якому ймовірність <i>P<sub>n</sub>(k₀)</i> є найбільшою серед усіх:</p>
        <div class="formula-box formula-highlight">
          <b>n·p − q ≤ k₀ ≤ n·p + p</b>
        </div>
        <p style="font-size: 6.8pt; color: #64748b;">Довжина інтервалу = (np+p) − (np−q) = p+q = 1. Якщо межі дробові — єдине ціле <i>k₀</i>; якщо цілі — два рівноймовірні <i>k₀</i>.</p>
      </div>
    </div>
  </div>

  <!-- MIDDLE ROW (HERO): VARIANT 12 TASK 6 -->
  <div class="card card-hero">
    <div class="card-header">
      <span class="card-title" style="color: #0284c7; font-size: 9.5pt;">★ [Обов'язково №1] Завдання 6 Варіанта 12: Порівняння двох серій підкидань кістки</span>
      <span class="card-pill pill-hero">Варіант 12 • РГР</span>
    </div>
    <div class="card-body">
      <p><b>Умова:</b> Підкидається гральна кістка. Що ймовірніше: з <b>5 підкидань не більше 2 разів</b> випаде парна кількість очок чи з <b>7 підкидань випаде не менше 3 разів</b> парна кількість очок?</p>
      
      <p><b>Базові параметри одного підкидання:</b> Подія <i>A</i> = {випало 2, 4 або 6} ⇒ <b>p = 3/6 = 1/2</b>, &nbsp; <b>q = 1 − 1/2 = 1/2</b>. Оскільки <i>p = q = 1/2</i>, то <i>P<sub>n</sub>(k) = C<sub>n</sub><sup>k</sup> / 2<sup>n</sup></i>.</p>

      <div class="hero-split">
        <!-- Subcard 1: n = 5 -->
        <div class="subcard">
          <div class="subcard-title">
            <span>Сценарій 1: n = 5, подія A {k ≤ 2}</span>
            <span style="color:#0284c7;">k ∈ {0, 1, 2}</span>
          </div>
          <p>Рахуємо безпосередньо суму трьох значень:</p>
          <div class="formula-box">
            P(A) = P₅(0) + P₅(1) + P₅(2) = (C₅⁰ + C₅¹ + C₅²) / 2⁵<br>
            • C₅⁰ = 1<br>
            • C₅¹ = 5<br>
            • C₅² = (5 · 4) / 2 = 10<br>
            <b>P(A) = (1 + 5 + 10) / 32 = 16 / 32 = 0,50 (50%)</b>
          </div>
        </div>

        <!-- Subcard 2: n = 7 -->
        <div class="subcard">
          <div class="subcard-title">
            <span>Сценарій 2: n = 7, подія B {k ≥ 3}</span>
            <span style="color:#16a34a;">k ∈ {3, 4, 5, 6, 7}</span>
          </div>
          <p>Застосовуємо метод протилежної події B̄ {k ≤ 2}:</p>
          <div class="formula-box">
            P(B̄) = P₇(0) + P₇(1) + P₇(2) = (C₇⁰ + C₇¹ + C₇²) / 2⁷<br>
            • C₇⁰ = 1; &nbsp; C₇¹ = 7; &nbsp; C₇² = (7 · 6) / 2 = 21<br>
            • P(B̄) = (1 + 7 + 21) / 128 = 29 / 128<br>
            <b>P(B) = 1 − 29/128 = 99/128 ≈ 0,7734 (77,34%)</b>
          </div>
        </div>
      </div>

      <div class="ans-box" style="margin-top: 5px;">
        <span class="label">Висновок та порівняння для Варіанта 12:</span>
        <span class="val">P(B) = 99/128 (≈77,34%) &gt; P(A) = 1/2 (50%) ⇒ Ймовірніше з 7 підкидань ≥ 3 разів!</span>
      </div>
    </div>
  </div>

  <!-- BOTTOM ROW: TICKET TASK 6 + MODE + POISSON APPROX -->
  <div class="grid-bottom">
    
    <!-- Bottom 1: Typical Ticket Task 6 -->
    <div class="card" style="border: 1.5px solid #6d28d9;">
      <div class="card-header">
        <span class="card-title" style="color: #6d28d9;">★ [Обов'язково №2] Типовий білет ПК-1 (№ 6)</span>
        <span class="card-pill pill-purple">Білет ОМП</span>
      </div>
      <div class="card-body">
        <p><b>Умова:</b> Ймовірність появи події хоч би один раз у 4 незалежних дослідах дорівнює <b>0,8704</b>. Яка ймовірність появи події в 1 досліді (p = const)?</p>
        <p style="font-size: 6.8pt; color: #64748b;">Варіанти: А) 0,6; Б) 0,7; В) 0,5; Г) 0,3; Д) 0,4.</p>
        <div class="formula-box">
          P₄(k ≥ 1) = 1 − q⁴ = 0,8704<br>
          q⁴ = 1 − 0,8704 = 0,1296<br>
          q = ⁴√0,1296 = 0,6<br>
          <b>p = 1 − q = 1 − 0,6 = 0,4</b>
        </div>
        <div class="ans-box">
          <span class="label">Правильна відповідь:</span>
          <span class="val" style="color: #6d28d9;">Варіант Д) 0,4</span>
        </div>
      </div>
    </div>

    <!-- Bottom 2: Mode Calculation Example -->
    <div class="card">
      <div class="card-header">
        <span class="card-title">Найімовірніше число успіхів (k₀)</span>
        <span class="card-pill pill-amber">Приклад розрахунку</span>
      </div>
      <div class="card-body">
        <p><b>Задача:</b> Монету кидають <i>n = 15</i> разів. <i>p = 0,5</i>; <i>q = 0,5</i>. Знайти <i>k₀</i>.</p>
        <div class="formula-box">
          np − q ≤ k₀ ≤ np + p<br>
          15·0,5 − 0,5 ≤ k₀ ≤ 15·0,5 + 0,5<br>
          7,5 − 0,5 ≤ k₀ ≤ 7,5 + 0,5<br>
          <b>7 ≤ k₀ ≤ 8</b>
        </div>
        <p>Оскільки обидві межі цілі числа, є <b>два найімовірніших значення</b>:</p>
        <div class="ans-box">
          <span class="label">Відповідь:</span>
          <span class="val">k₀ = 7 та k₀ = 8</span>
        </div>
      </div>
    </div>

    <!-- Bottom 3: Boundary Transitions (Preview of Topic 8) -->
    <div class="card">
      <div class="card-header">
        <span class="card-title">Граничні теореми (n → ∞)</span>
        <span class="card-pill pill-rose">Місток до Теми 8</span>
      </div>
      <div class="card-body">
        <p>Коли кількість дослідів <i>n</i> велика, прямий підрахунок <i>C<sub>n</sub><sup>k</sup></i> складний. Застосовують наближення:</p>
        <div class="formula-box" style="font-size: 7pt;">
          • <b>Пуассон</b> (рідкісні події: <i>n &gt; 100</i>, <i>p &lt; 0,01</i>, <i>λ = np</i>):<br>
          &nbsp;&nbsp;P<sub>n</sub>(k) ≈ (λ<sup>k</sup> / k!) · e<sup>−λ</sup><br>
          • <b>Муавр-Лаплас</b> (<i>npq &gt; 9</i>):<br>
          &nbsp;&nbsp;P<sub>n</sub>(k) ≈ [ 1 / √(npq) ] · φ(x)
        </div>
        <p style="font-size: 6.8pt; color: #64748b;">Детально розберемо в Завданні 8 РГР!</p>
      </div>
    </div>

  </div>

  <!-- FOOTER -->
  <div class="footer">
    <span>НУ «Львівська політехніка» • Кафедра ОМП • Курс: Теорія ймовірностей та математична статистика</span>
    <span>Опорний лист Теми 6 • Формат A4 (300 DPI) • Схема Бернуллі</span>
  </div>

</body>
</html>
'''

output_dir = r"D:\Studings\SecondYear\FirstSemester\Теорія ймовірності"
html_path = os.path.join(output_dir, "topic6_showcase_a4.html")
pdf_path = os.path.join(output_dir, "topic6_showcase_a4.pdf")
png_path = os.path.join(output_dir, "topic6_showcase_a4.png")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)
print("HTML saved!")

# Render to PDF via headless chrome
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    f"--print-to-pdf={pdf_path}",
    "--no-pdf-header-footer",
    html_path
]
subprocess.run(cmd, check=True)
print("PDF printed!")

# Render PDF page 0 to PNG at 300 DPI via pymupdf
doc = pymupdf.open(pdf_path)
print("PDF pages count:", len(doc))
page = doc[0]
pix = page.get_pixmap(dpi=300)
pix.save(png_path)
print(f"PNG saved at 300 DPI! Dimensions: {pix.width} x {pix.height}")

# Copy to brain artifact directory
brain_dir = r"C:\Users\andri\.gemini\antigravity\brain\dc20fa28-3959-4990-8c43-347402ae19ad"
shutil.copy(png_path, os.path.join(brain_dir, "topic6_showcase_a4.png"))
print("Copied to brain directory!")
