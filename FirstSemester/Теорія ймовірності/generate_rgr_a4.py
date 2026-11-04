import base64
import subprocess
import pymupdf

with open(r'D:\Studings\SecondYear\FirstSemester\Теорія ймовірності\task5_clean.png', 'rb') as f:
    img_b64 = base64.b64encode(f.read()).decode()

html_template = r"""<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<title>РГР з теорії ймовірностей — Варіант 12 (Завдання 1–12)</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>
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
  html, body {
    width: 210mm;
    height: 297mm;
    max-height: 297mm;
    overflow: hidden;
    background: #ffffff;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #0f172a;
  }
  body {
    padding: 5mm 6mm 4mm 6mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  /* Top Banner */
  .header {
    background: linear-gradient(135deg, #1e3a8a 0%, #0369a1 100%);
    color: #ffffff;
    padding: 2mm 4mm;
    border-radius: 4px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2mm;
    flex-shrink: 0;
  }
  .header h1 {
    font-size: 13pt;
    font-weight: 900;
    letter-spacing: -0.2px;
    text-transform: uppercase;
  }
  .header p {
    font-size: 7.5pt;
    color: #e0f2fe;
    margin-top: 1px;
  }
  .badge {
    background: rgba(255, 255, 255, 0.25);
    border: 1px solid rgba(255, 255, 255, 0.6);
    padding: 1.5mm 3.5mm;
    border-radius: 3px;
    font-weight: 900;
    font-size: 8.5pt;
    letter-spacing: 0.5px;
    white-space: nowrap;
  }

  /* Grid: 3 columns x 4 rows */
  .grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(4, 1fr);
    gap: 2mm;
    flex: 1;
    min-height: 0;
  }

  .card {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 1.5mm 2.2mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    font-size: 6.8pt;
    line-height: 1.25;
    overflow: hidden;
  }
  .card-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1.5px solid #0284c7;
    padding-bottom: 1px;
    margin-bottom: 1px;
  }
  .card-title {
    font-size: 8pt;
    font-weight: 900;
    color: #1e3a8a;
  }
  .card-topic {
    font-size: 6pt;
    font-weight: 800;
    color: #0369a1;
    background: #e0f2fe;
    padding: 1px 4px;
    border-radius: 3px;
  }

  .umova {
    background: #f8fafc;
    border-left: 2px solid #64748b;
    padding: 1px 3px;
    font-size: 6.4pt;
    color: #334155;
    margin-bottom: 1.5px;
    font-style: italic;
    line-height: 1.2;
  }
  .umova b {
    font-style: normal;
    color: #0f172a;
  }

  .solution {
    display: flex;
    flex-direction: column;
    gap: 1px;
    font-size: 6.7pt;
    color: #0f172a;
  }
  .solution p {
    margin: 0;
  }

  .graph-box {
    display: flex;
    justify-content: center;
    align-items: center;
    background: #ffffff;
    border: 0.8px dashed #cbd5e1;
    border-radius: 3px;
    padding: 1px;
    margin: 1px 0;
  }
  .graph-box img {
    max-height: 15mm;
    max-width: 100%;
    object-fit: contain;
  }
  .graph-box svg {
    max-height: 15mm;
    width: auto;
  }

  .ans {
    background: #f0fdf4;
    border: 0.8px solid #86efac;
    border-radius: 3px;
    padding: 1px 4px;
    font-weight: 800;
    color: #166534;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 1px;
    font-size: 6.7pt;
  }
  .ans-val {
    color: #15803d;
  }

  .katex {
    font-size: 1em !important;
  }
  .katex-display {
    margin: 0.5px 0 !important;
  }

  /* Footer */
  .footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 0.8px solid #cbd5e1;
    padding-top: 1mm;
    font-size: 6pt;
    color: #64748b;
    font-weight: 600;
    margin-top: 1.5mm;
    flex-shrink: 0;
  }
</style>
</head>
<body>

<div class="header">
  <div>
    <h1>РОЗРАХУНКОВА РОБОТА: ТЕОРІЯ ЙМОВІРНОСТЕЙ — ВАРІАНТ № 12</h1>
    <p>НУ «Львівська політехніка» | Кафедра ОМП | Студент: Лемішка Андрій (ПП-24) | Завдання 1–12 (A4 Cheatsheet)</p>
  </div>
  <div class="badge">ВАРІАНТ 12</div>
</div>

<div class="grid">

  <!-- 1 -->
  <div class="card">
    <div>
      <div class="card-top">
        <span class="card-title">Завдання 1</span>
        <span class="card-topic">Комбінаторика</span>
      </div>
      <div class="umova">
        <b>Умова:</b> Скількома способами можна впорядкувати множину {1, 2, ..., n} так, щоб числа 1, 2, 3 стояли поруч і в порядку зростання?
      </div>
      <div class="solution">
        <p>• <b>Метод «блоку»:</b> числа 1, 2, 3 утворюють єдиний блок $X = (1, 2, 3)$.</p>
        <p>• Порядок всередині $X$ фіксований: лише $1$ спосіб.</p>
        <p>• Кількість елементів: $(n - 3)$ чисел + $1$ блок $X = (n - 2)$ об'єкти.</p>
        <p>• Кількість перестановок: $N = P_{n-2} = (n-2)!$</p>
      </div>
    </div>
    <div class="ans">
      <span>Відповідь:</span>
      <span class="ans-val">$N = (n - 2)!$</span>
    </div>
  </div>

  <!-- 2 -->
  <div class="card">
    <div>
      <div class="card-top">
        <span class="card-title">Завдання 2</span>
        <span class="card-topic">Алгебра подій</span>
      </div>
      <div class="umova">
        <b>Умова:</b> Гральну кістку підкидають 1 раз. $M$: число $\ge 3$; $N$: $< 4$; $K$: парне. Сумісність та опис операцій.
      </div>
      <div class="solution">
        <p>• $\Omega = \{1,2,3,4,5,6\}$. $M=\{3,4,5,6\}, N=\{1,2,3\}, K=\{2,4,6\}$.</p>
        <p>• $M \cap N = \{3\} \neq \varnothing$; $M \cap K = \{4, 6\} \neq \varnothing$; $N \cap K = \{2\} \neq \varnothing$ (усі пари <b>сумісні</b>).</p>
        <p>• $M \cap N = \{3\}$, $M \cup N = \Omega$, $N \cap K = \{2\}$.</p>
        <p>• $\bar{N} = \{4, 5, 6\}$, $\bar{K} = \{1, 3, 5\}$, $N \setminus K = \{1, 3\}$.</p>
        <p>• $M \cap N \cap K = \varnothing$ (неможлива), $M \cup N \cup K = \Omega$ (достовірна).</p>
      </div>
    </div>
    <div class="ans">
      <span>Відповідь:</span>
      <span class="ans-val">Усі пари сумісні</span>
    </div>
  </div>

  <!-- 3 -->
  <div class="card">
    <div>
      <div class="card-top">
        <span class="card-title">Завдання 3</span>
        <span class="card-topic">Класична ймовірність</span>
      </div>
      <div class="umova">
        <b>Умова:</b> Студент знає 40 з 60 питань. Іспит: відповісти принаймні на 4 з 5 у білеті. Яка ймовірність скласти?
      </div>
      <div class="solution">
        <p>• $N = 60, K = 40, N-K = 20, n = 5$.</p>
        <p>• $n_{\text{заг}} = C_{60}^5 = 5\,461\,512$.</p>
        <p>• <b>«Принаймні 4 з 5»:</b> рівно 4 або всі 5 відомих:</p>
        <p>$$m_1 = C_{40}^4 C_{20}^1 = 91\,390 \cdot 20 = 1\,827\,800$$</p>
        <p>$$m_2 = C_{40}^5 C_{20}^0 = 658\,008 \cdot 1 = 658\,008$$</p>
        <p>$$P = \frac{1\,827\,800 + 658\,008}{5\,461\,512} = \frac{2\,485\,808}{5\,461\,512} \approx 0{,}4551$$</p>
      </div>
    </div>
    <div class="ans">
      <span>Відповідь:</span>
      <span class="ans-val">$P \approx 0{,}4551 \ (45{,}51\%)$</span>
    </div>
  </div>

  <!-- 4 -->
  <div class="card">
    <div>
      <div class="card-top">
        <span class="card-title">Завдання 4</span>
        <span class="card-topic">Геометрична ймовірність</span>
      </div>
      <div class="umova">
        <b>Умова:</b> Точка круга радіуса $R$ попаде у вписаний трикутник $ABC$ ($AB = 2R, AC = CB = R\sqrt{2}$).
      </div>
      <div class="solution">
        <div class="graph-box">
          <svg width="120" height="48" viewBox="0 0 120 48">
            <circle cx="60" cy="25" r="21" fill="#f8fafc" stroke="#0284c7" stroke-width="1.3" />
            <polygon points="39,25 81,25 60,4" fill="#bae6fd" stroke="#0369a1" stroke-width="1.4" />
            <line x1="39" y1="25" x2="81" y2="25" stroke="#1e293b" stroke-width="1.3" />
            <circle cx="60" cy="25" r="1.5" fill="#ef4444" />
            <text x="32" y="27" font-size="7" font-weight="bold">A</text>
            <text x="83" y="27" font-size="7" font-weight="bold">B</text>
            <text x="58" y="3.5" font-size="7" font-weight="bold">C</text>
            <text x="58" y="32" font-size="6.5" fill="#ef4444">O</text>
            <text x="43" y="13" font-size="6.5" fill="#0369a1">R√2</text>
          </svg>
        </div>
        <p>• $AB = 2R$ — діаметр $\implies \angle C = 90^\circ$ (прямокутний $\triangle$).</p>
        <p>• $S_D = \pi R^2$; $S_d = \frac{1}{2} (R\sqrt{2})^2 = R^2$.</p>
        <p>• $P = \frac{S_d}{S_D} = \frac{R^2}{\pi R^2} = \frac{1}{\pi} \approx 0{,}3183$.</p>
      </div>
    </div>
    <div class="ans">
      <span>Відповідь:</span>
      <span class="ans-val">$P = \frac{1}{\pi} \approx 0{,}3183$</span>
    </div>
  </div>

  <!-- 5 -->
  <div class="card">
    <div>
      <div class="card-top">
        <span class="card-title">Завдання 5</span>
        <span class="card-topic">Повна ймовірність</span>
      </div>
      <div class="umova">
        <b>Умова:</b> Мандрівник виходить з $A$, на кожному роздоріжжі вибирає напрям навмання (не повертаючись). Ймовірність потрапити в $B$?
      </div>
      <div class="solution">
        <div class="graph-box">
          <img src="data:image/png;base64,__IMG_B64_PLACEHOLDER__" alt="Схема роздоріжжя A -> B">
        </div>
        <p>• З $A$ є рівноможливі напрями розгалуження.</p>
        <p>• За формулою повної ймовірності підсумовуються ймовірності всіх допустимих шляхів від $A$ до $B$:</p>
        <p>$$P(B) = \sum_{\text{ланцюжки}} P(\text{шлях}_{A \to B})$$</p>
      </div>
    </div>
    <div class="ans">
      <span>Результат:</span>
      <span class="ans-val">$P(B)$ через суму шляхів</span>
    </div>
  </div>

  <!-- 6 -->
  <div class="card">
    <div>
      <div class="card-top">
        <span class="card-title">Завдання 6</span>
        <span class="card-topic">Схема Бернуллі</span>
      </div>
      <div class="umova">
        <b>Умова:</b> Кубик: що ймовірніше — з 5 кидків $\le 2$ разів парне, чи з 7 кидків $\ge 3$ разів парне?
      </div>
      <div class="solution">
        <p>• $p = q = 0{,}5$ (парне очко: $2, 4, 6$).</p>
        <p>• <b>1 випадок ($n=5, k \le 2$):</b></p>
        <p>$$P_5(k \le 2) = \frac{C_5^0 + C_5^1 + C_5^2}{2^5} = \frac{16}{32} = 0{,}5000$$</p>
        <p>• <b>2 випадок ($n=7, k \ge 3$):</b></p>
        <p>$$P_7(k \ge 3) = 1 - \frac{C_7^0 + C_7^1 + C_7^2}{2^7} = 1 - \frac{29}{128} = \frac{99}{128} \approx 0{,}7734$$</p>
        <p>• $0{,}7734 > 0{,}5000$.</p>
      </div>
    </div>
    <div class="ans">
      <span>Відповідь:</span>
      <span class="ans-val">З 7 кидків $\ge 3$ ($77{,}34\%$)</span>
    </div>
  </div>

  <!-- 7 -->
  <div class="card">
    <div>
      <div class="card-top">
        <span class="card-title">Завдання 7</span>
        <span class="card-topic">Дискретна ВВ</span>
      </div>
      <div class="umova">
        <b>Умова:</b> ВВ $\xi$ має 2 значення: $x_1 < x_2$, $p_1 = 0{,}3$, $M\xi = 3{,}2$, $D\xi = 0{,}15$. Знайти ряд розподілу.
      </div>
      <div class="solution">
        <p>• $p_2 = 1 - 0{,}3 = 0{,}7$.</p>
        <p>• $M\xi = 0{,}3 x_1 + 0{,}7 x_2 = 3{,}2$.</p>
        <p>• $D\xi = p_1 p_2 (x_2 - x_1)^2 = 0{,}21 (x_2 - x_1)^2 = 0{,}15$.</p>
        <p>• $(x_2 - x_1)^2 = \frac{0{,}15}{0{,}21} = \frac{5}{7} \implies x_2 - x_1 = \sqrt{5/7} \approx 0{,}845$.</p>
        <p>• $x_1 = 3{,}2 - 0{,}7 \sqrt{5/7} \approx 2{,}608$; $x_2 = 3{,}2 + 0{,}3 \sqrt{5/7} \approx 3{,}454$.</p>
      </div>
    </div>
    <div class="ans">
      <span>Ряд розподілу:</span>
      <span class="ans-val">$x_1 \approx 2{,}61; \ x_2 \approx 3{,}45$</span>
    </div>
  </div>

  <!-- 8 -->
  <div class="card">
    <div>
      <div class="card-top">
        <span class="card-title">Завдання 8</span>
        <span class="card-topic">Муавр-Лаплас</span>
      </div>
      <div class="umova">
        <b>Умова:</b> 9% телевізорів з браком. Яка ймовірність, що серед 180 телевізорів від 15 до 30 бракованих?
      </div>
      <div class="solution">
        <p>• $n = 180, p = 0{,}09, q = 0{,}91$.</p>
        <p>• $np = 16{,}2$, $\sqrt{npq} = \sqrt{180 \cdot 0{,}09 \cdot 0{,}91} \approx 3{,}84$.</p>
        <p>• Інтегральна теорема: $P(15 \le k \le 30) \approx \Phi_0(x_2) - \Phi_0(x_1)$.</p>
        <p>$$x_1 = \frac{15 - 16{,}2}{3{,}84} = -0{,}31; \quad x_2 = \frac{30 - 16{,}2}{3{,}84} = 3{,}59$$</p>
        <p>$$P \approx \Phi_0(3{,}59) + \Phi_0(0{,}31) = 0{,}4998 + 0{,}1217 = 0{,}6215$$</p>
      </div>
    </div>
    <div class="ans">
      <span>Відповідь:</span>
      <span class="ans-val">$P \approx 0{,}6215 \ (62{,}15\%)$</span>
    </div>
  </div>

  <!-- 9 -->
  <div class="card">
    <div>
      <div class="card-top">
        <span class="card-title">Завдання 9</span>
        <span class="card-topic">Ряд і многокутник ВВ</span>
      </div>
      <div class="umova">
        <b>Умова:</b> З урни (7 білих, 3 чорні) виймають 2. $\xi$ — число білих. Побудувати многокутник, знайти $M, D, \sigma$.
      </div>
      <div class="solution">
        <p>• $\xi \in \{0, 1, 2\}$. $C_{10}^2 = 45$.</p>
        <p>• $p_0 = \frac{C_3^2}{45} = \frac{1}{15}$; $p_1 = \frac{C_7^1 C_3^1}{45} = \frac{7}{15}$; $p_2 = \frac{C_7^2}{45} = \frac{7}{15}$.</p>
        <div class="graph-box">
          <svg width="120" height="42" viewBox="0 0 120 42">
            <line x1="18" y1="35" x2="110" y2="35" stroke="#64748b" stroke-width="1.2" />
            <line x1="18" y1="35" x2="18" y2="4" stroke="#64748b" stroke-width="1.2" />
            <polyline points="28,30 60,10 98,10" fill="none" stroke="#0284c7" stroke-width="1.5" />
            <circle cx="28" cy="30" r="2" fill="#1e3a8a" />
            <circle cx="60" cy="10" r="2" fill="#1e3a8a" />
            <circle cx="98" cy="10" r="2" fill="#1e3a8a" />
            <text x="26" y="41" font-size="6.5">0</text>
            <text x="58" y="41" font-size="6.5">1</text>
            <text x="96" y="41" font-size="6.5">2</text>
            <text x="5" y="12" font-size="6">7/15</text>
            <text x="5" y="32" font-size="6">1/15</text>
          </svg>
        </div>
        <p>• $M\xi = 1{,}4$; $D\xi = \frac{7}{3} - 1{,}4^2 \approx 0{,}373$; $\sigma \approx 0{,}611$.</p>
      </div>
    </div>
    <div class="ans">
      <span>Числові хар-ки:</span>
      <span class="ans-val">$M = 1{,}4; D = 0{,}37; \sigma = 0{,}61$</span>
    </div>
  </div>

  <!-- 10 -->
  <div class="card">
    <div>
      <div class="card-top">
        <span class="card-title">Завдання 10</span>
        <span class="card-topic">Неперервна ВВ</span>
      </div>
      <div class="umova">
        <b>Умова:</b> $f(x) = \frac{4-x}{8}$ на $(0; 4)$. Знайти $F(x), P(x \in [2; 3]), Mo, Me, M\xi, D\xi$.
      </div>
      <div class="solution">
        <div class="graph-box">
          <svg width="120" height="42" viewBox="0 0 120 42">
            <line x1="18" y1="35" x2="110" y2="35" stroke="#64748b" stroke-width="1.2" />
            <line x1="18" y1="35" x2="18" y2="4" stroke="#64748b" stroke-width="1.2" />
            <polygon points="60,35 60,21 80,15 80,35" fill="#bae6fd" />
            <line x1="18" y1="8" x2="100" y2="35" stroke="#0284c7" stroke-width="1.5" />
            <text x="15" y="41" font-size="6.5">0</text>
            <text x="58" y="41" font-size="6.5">2</text>
            <text x="78" y="41" font-size="6.5">3</text>
            <text x="98" y="41" font-size="6.5">4</text>
            <text x="5" y="10" font-size="6">1/2</text>
          </svg>
        </div>
        <p>• $F(x) = \frac{x}{2} - \frac{x^2}{16}$; $P(2 \le x \le 3) = F(3) - F(2) = \frac{3}{16} = 0{,}1875$.</p>
        <p>• $Mo = 0$; $Me = 4 - 2\sqrt{2} \approx 1{,}172$.</p>
        <p>• $M\xi = \int_0^4 x \frac{4-x}{8} dx = \frac{4}{3}$; $D\xi = \frac{8}{9} \approx 0{,}889$.</p>
      </div>
    </div>
    <div class="ans">
      <span>Параметри:</span>
      <span class="ans-val">$P = \frac{3}{16}; M = \frac{4}{3}; D = \frac{8}{9}$</span>
    </div>
  </div>

  <!-- 11 -->
  <div class="card">
    <div>
      <div class="card-top">
        <span class="card-title">Завдання 11</span>
        <span class="card-topic">Функція від ВВ</span>
      </div>
      <div class="umova">
        <b>Умова:</b> $f(x) = A(x^2 + 2x)$ на $(0; 1)$. Знайти $A$, $M\eta, D\eta$ для $\eta = 2\xi$.
      </div>
      <div class="solution">
        <p>• <b>Нормування:</b> $\int_0^1 A(x^2 + 2x) dx = A \frac{4}{3} = 1 \implies A = \frac{3}{4}$.</p>
        <p>• $M\xi = \frac{3}{4} \int_0^1 (x^3 + 2x^2) dx = \frac{11}{16} = 0{,}6875$.</p>
        <p>• $M\eta = M(2\xi) = 2 M\xi = \frac{11}{8} = 1{,}375$.</p>
        <p>• $M\xi^2 = \frac{3}{4} \int_0^1 (x^4 + 2x^3) dx = \frac{21}{40} = 0{,}525$.</p>
        <p>• $D\xi = \frac{21}{40} - (\frac{11}{16})^2 \approx 0{,}05234 \implies D\eta = 4 D\xi \approx 0{,}2094$.</p>
      </div>
    </div>
    <div class="ans">
      <span>Відповідь:</span>
      <span class="ans-val">$A = \frac{3}{4}; M\eta = 1{,}375; D\eta \approx 0{,}209$</span>
    </div>
  </div>

  <!-- 12 -->
  <div class="card">
    <div>
      <div class="card-top">
        <span class="card-title">Завдання 12</span>
        <span class="card-topic">Характеристична ф-я</span>
      </div>
      <div class="umova">
        <b>Умова:</b> Знайти характеристичну функцію для $f(x) = 3x^2$ на $[0; 1]$. За нею знайти $M\xi$ та $D\xi$.
      </div>
      <div class="solution">
        <p>• $\varphi_\xi(t) = \int_0^1 e^{itx} 3x^2 dx$.</p>
        <p>• Інтегруванням частинами:</p>
        <p>$$\varphi_\xi(t) = \frac{3}{it} e^{it} + \frac{6}{(it)^2} e^{it} - \frac{6}{(it)^3} (e^{it} - 1)$$</p>
        <p>• $M\xi = \frac{1}{i} \varphi'(0) = \int_0^1 3x^3 dx = \frac{3}{4} = 0{,}75$.</p>
        <p>• $M\xi^2 = -\varphi''(0) = \int_0^1 3x^4 dx = \frac{3}{5} = 0{,}6$.</p>
        <p>• $D\xi = M\xi^2 - (M\xi)^2 = \frac{3}{5} - \frac{9}{16} = \frac{3}{80} = 0{,}0375$.</p>
      </div>
    </div>
    <div class="ans">
      <span>Відповідь:</span>
      <span class="ans-val">$M\xi = \frac{3}{4}; \ D\xi = \frac{3}{80} = 0{,}0375$</span>
    </div>
  </div>

</div>

<div class="footer">
  <span>НУ «Львівська політехніка» • Інститут прикладної математики та фундаментальних наук • Кафедра ОМП</span>
  <span>Розрахункова графічна робота (РГР) — Варіант 12 • Повний огляд завдань 1–12 на форматі A4</span>
</div>

</body>
</html>"""

html = html_template.replace('__IMG_B64_PLACEHOLDER__', img_b64)

path_html = r'D:\Studings\SecondYear\FirstSemester\Теорія ймовірності\rgr_var12_tasks1_12_a4.html'
path_pdf = r'D:\Studings\SecondYear\FirstSemester\Теорія ймовірності\rgr_var12_tasks1_12_a4.pdf'
path_png = r'D:\Studings\SecondYear\FirstSemester\Теорія ймовірності\rgr_var12_tasks1_12_a4.png'

with open(path_html, 'w', encoding='utf-8') as f:
    f.write(html)
print('HTML written!')

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
cmd_pdf = [chrome, '--headless=new', '--disable-gpu', f'--print-to-pdf={path_pdf}', '--no-pdf-header-footer', path_html]
subprocess.run(cmd_pdf, check=True)
print('PDF printed!')

doc = pymupdf.open(path_pdf)
print('PDF pages count:', len(doc))
page = doc[0]
pix = page.get_pixmap(dpi=300)
pix.save(path_png)
print('PNG rendered at 300 DPI successfully! Size:', pix.width, 'x', pix.height)
