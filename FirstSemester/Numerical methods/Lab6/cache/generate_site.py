import os

def generate_site():
    html_content = '''<!DOCTYPE html>
<html lang="uk" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Чисельні методи • Лабораторна робота №6 | Лемішка Андрій (ПП-24)</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root {
      --bg: #0b0f19;
      --card-bg: rgba(17, 24, 39, 0.85);
      --card-border: rgba(255, 255, 255, 0.1);
      --text: #f3f4f6;
      --text-muted: #9ca3af;
      --primary: #3b82f6;
      --primary-hover: #2563eb;
      --primary-glow: rgba(59, 130, 246, 0.25);
      --secondary: #10b981;
      --accent: #8b5cf6;
      --danger: #ef4444;
      --warning: #f59e0b;
      --code-bg: #030712;
      --nav-bg: rgba(11, 15, 25, 0.9);
      --table-stripe: rgba(255, 255, 255, 0.02);
    }

    html.light {
      --bg: #f8fafc;
      --card-bg: rgba(255, 255, 255, 0.95);
      --card-border: rgba(0, 0, 0, 0.08);
      --text: #0f172a;
      --text-muted: #64748b;
      --primary: #2563eb;
      --primary-hover: #1d4ed8;
      --primary-glow: rgba(37, 99, 235, 0.15);
      --secondary: #059669;
      --accent: #7c3aed;
      --danger: #dc2626;
      --warning: #d97706;
      --code-bg: #f1f5f9;
      --nav-bg: rgba(248, 250, 252, 0.92);
      --table-stripe: rgba(0, 0, 0, 0.02);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    }

    body {
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.6;
      transition: background-color 0.3s ease, color 0.3s ease;
      overflow-x: hidden;
    }

    header {
      position: sticky;
      top: 0;
      z-index: 50;
      backdrop-filter: blur(12px);
      background: var(--nav-bg);
      border-bottom: 1px solid var(--card-border);
      padding: 1rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-weight: 700;
      font-size: 1.25rem;
      color: var(--primary);
    }

    .brand i { font-size: 1.5rem; }

    .nav-actions { display: flex; align-items: center; gap: 1rem; }

    .theme-toggle {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      color: var(--text);
      padding: 0.5rem 1rem;
      border-radius: 0.5rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.9rem;
      transition: all 0.2s;
    }

    .theme-toggle:hover {
      border-color: var(--primary);
      box-shadow: 0 0 10px var(--primary-glow);
    }

    .hero {
      padding: 3rem 2rem 2rem;
      text-align: center;
      max-width: 900px;
      margin: 0 auto;
    }

    .badge {
      display: inline-block;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 600;
      background: rgba(59, 130, 246, 0.15);
      color: var(--primary);
      border: 1px solid rgba(59, 130, 246, 0.3);
      margin-bottom: 1rem;
    }

    h1 {
      font-size: 2.25rem;
      font-weight: 800;
      margin-bottom: 1rem;
      background: linear-gradient(135deg, var(--text) 0%, var(--primary) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .subtitle {
      color: var(--text-muted);
      font-size: 1.1rem;
      margin-bottom: 2rem;
    }

    .meta-cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1rem;
      margin-bottom: 2rem;
    }

    .meta-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 0.75rem;
      padding: 1.25rem;
      text-align: left;
    }

    .meta-card .label {
      font-size: 0.8rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.25rem;
    }

    .meta-card .value {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text);
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 1.5rem 4rem;
    }

    .tabs {
      display: flex;
      gap: 0.5rem;
      border-bottom: 1px solid var(--card-border);
      margin-bottom: 2rem;
      overflow-x: auto;
      padding-bottom: 0.5rem;
    }

    .tab-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 0.75rem 1.25rem;
      font-size: 0.95rem;
      font-weight: 600;
      border-radius: 0.5rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s;
      white-space: nowrap;
    }

    .tab-btn:hover {
      color: var(--text);
      background: rgba(255, 255, 255, 0.04);
    }

    .tab-btn.active {
      color: var(--primary);
      background: rgba(59, 130, 246, 0.1);
      border-bottom: 2px solid var(--primary);
    }

    .tab-content { display: none; }
    .tab-content.active { display: block; animation: fadeIn 0.3s ease; }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 1rem;
      padding: 2rem;
      margin-bottom: 2rem;
      backdrop-filter: blur(10px);
    }

    .card-title {
      font-size: 1.35rem;
      font-weight: 700;
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      color: var(--text);
    }

    .formula-box {
      background: var(--code-bg);
      border: 1px solid var(--card-border);
      border-left: 4px solid var(--primary);
      border-radius: 0.5rem;
      padding: 1.25rem;
      margin: 1rem 0;
      font-family: 'Courier New', Courier, monospace;
      font-size: 1.05rem;
    }

    .charts-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
      gap: 1.5rem;
      margin-bottom: 2rem;
    }

    .chart-container {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 1rem;
      padding: 1.5rem;
      position: relative;
    }

    .table-wrapper {
      overflow-x: auto;
      border-radius: 0.75rem;
      border: 1px solid var(--card-border);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      text-align: right;
      font-size: 0.9rem;
    }

    th {
      background: rgba(59, 130, 246, 0.15);
      color: var(--primary);
      padding: 0.75rem 1rem;
      font-weight: 700;
      border-bottom: 1px solid var(--card-border);
      white-space: nowrap;
    }

    th:first-child, td:first-child { text-align: center; }

    td {
      padding: 0.65rem 1rem;
      border-bottom: 1px solid var(--card-border);
    }

    tr:nth-child(even) { background-color: var(--table-stripe); }
    tr:hover { background-color: rgba(59, 130, 246, 0.05); }

    .accordion-item {
      border: 1px solid var(--card-border);
      border-radius: 0.5rem;
      margin-bottom: 0.75rem;
      overflow: hidden;
    }

    .accordion-header {
      background: var(--card-bg);
      padding: 0.9rem 1.25rem;
      font-weight: 600;
      font-size: 1rem;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: background 0.2s;
    }

    .accordion-header:hover { background: rgba(59, 130, 246, 0.05); }

    .accordion-body {
      padding: 1rem 1.25rem;
      background: rgba(0, 0, 0, 0.1);
      display: none;
      border-top: 1px solid var(--card-border);
      line-height: 1.7;
      font-size: 0.95rem;
      color: var(--text);
    }

    .accordion-item.open .accordion-body { display: block; }
    .accordion-item.open .accordion-header i { transform: rotate(180deg); }

    pre code {
      display: block;
      background: var(--code-bg);
      padding: 1.25rem;
      border-radius: 0.5rem;
      border: 1px solid var(--card-border);
      overflow-x: auto;
      font-family: Consolas, 'Fira Code', monospace;
      font-size: 0.9rem;
      color: #38bdf8;
    }

    footer {
      text-align: center;
      padding: 2rem;
      color: var(--text-muted);
      border-top: 1px solid var(--card-border);
      font-size: 0.9rem;
    }
  </style>
</head>
<body>

  <header>
    <div class="brand">
      <i class="fa-solid fa-square-root-variable"></i>
      <span>ЧМ • Лабораторна №6</span>
    </div>
    <div class="nav-actions">
      <button class="theme-toggle" onclick="toggleTheme()">
        <i class="fa-solid fa-moon" id="themeIcon"></i>
        <span id="themeText">Темна</span>
      </button>
    </div>
  </header>

  <section class="hero">
    <div class="badge">Варіант № 12 • Група ПП-24</div>
    <h1>Чисельне розв’язування диференціальних рівнянь</h1>
    <p class="subtitle">Методи Ейлера, Гюна та Рунге – Кутта 4-го порядку для dy/dx = –0.9 y, y(0) = 0.12</p>

    <div class="meta-cards">
      <div class="meta-card">
        <div class="label">Студент</div>
        <div class="value">Лемішка Андрій</div>
      </div>
      <div class="meta-card">
        <div class="label">Викладач</div>
        <div class="value">Чумакевич В.В.</div>
      </div>
      <div class="meta-card">
        <div class="label">Рівняння</div>
        <div class="value">dy/dx = –0.9 y</div>
      </div>
      <div class="meta-card">
        <div class="label">Параметри</div>
        <div class="value">y(0) = 0.12, N = 20</div>
      </div>
    </div>
  </section>

  <main class="container">
    <div class="tabs">
      <button class="tab-btn active" onclick="switchTab('tab-charts')"><i class="fa-solid fa-chart-line"></i> Графіки</button>
      <button class="tab-btn" onclick="switchTab('tab-tables')"><i class="fa-solid fa-table"></i> Таблиці результатів</button>
      <button class="tab-btn" onclick="switchTab('tab-theory')"><i class="fa-solid fa-book"></i> Теорія та висновок</button>
      <button class="tab-btn" onclick="switchTab('tab-code')"><i class="fa-solid fa-code"></i> Код програми</button>
      <button class="tab-btn" onclick="switchTab('tab-questions')"><i class="fa-solid fa-circle-question"></i> Контрольні запитання (18)</button>
    </div>

    <!-- TAB 1: CHARTS -->
    <div id="tab-charts" class="tab-content active">
      <div class="charts-grid">
        <div class="chart-container">
          <h3 class="card-title"><i class="fa-solid fa-wave-square" style="color: var(--primary);"></i> Порівняння функцій y(x)</h3>
          <canvas id="functionChart" height="260"></canvas>
        </div>
        <div class="chart-container">
          <h3 class="card-title"><i class="fa-solid fa-chart-area" style="color: var(--danger);"></i> Абсолютна похибка Δ (Log Scale)</h3>
          <canvas id="errorChart" height="260"></canvas>
        </div>
      </div>

      <div class="card">
        <h2 class="card-title"><i class="fa-solid fa-clipboard-check" style="color: var(--secondary);"></i> Порівняння точності методів у точці x = 1.0</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem;">
          <div style="padding: 1rem; border-radius: 0.5rem; background: rgba(239, 68, 68, 0.1); border: 1px solid var(--danger);">
            <div style="font-weight: 700; color: var(--danger); margin-bottom: 0.5rem;">Метод Ейлера (1-й порядок)</div>
            <div>y₁(1.0) = 0.047780</div>
            <div>Похибка Δ₁ = 1.0081 · 10⁻³</div>
          </div>
          <div style="padding: 1rem; border-radius: 0.5rem; background: rgba(245, 158, 11, 0.1); border: 1px solid var(--warning);">
            <div style="font-weight: 700; color: var(--warning); margin-bottom: 0.5rem;">Метод Гюна (2-й порядок)</div>
            <div>y₂(1.0) = 0.048804</div>
            <div>Похибка Δ₂ = 1.5331 · 10⁻⁵</div>
          </div>
          <div style="padding: 1rem; border-radius: 0.5rem; background: rgba(59, 130, 246, 0.1); border: 1px solid var(--primary);">
            <div style="font-weight: 700; color: var(--primary); margin-bottom: 0.5rem;">Метод Рунге – Кутта (4-й порядок)</div>
            <div>y₄(1.0) = 0.04878836</div>
            <div>Похибка Δ₄ = 1.5578 · 10⁻⁹ (у 640 000 разів точніший!)</div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 2: TABLES -->
    <div id="tab-tables" class="tab-content">
      <div class="card">
        <h2 class="card-title"><i class="fa-solid fa-table-cells"></i> Зведена таблиця результатів (i = 0 .. 20)</h2>
        <div class="table-wrapper">
          <table id="summaryTable">
            <thead>
              <tr>
                <th>i</th>
                <th>x</th>
                <th>y (точний)</th>
                <th>y1 (Ейлер)</th>
                <th>Δ1</th>
                <th>y2 (Гюн)</th>
                <th>Δ2</th>
                <th>y4 (РК4)</th>
                <th>Δ4</th>
              </tr>
            </thead>
            <tbody></tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- TAB 3: THEORY & CONCLUSION -->
    <div id="tab-theory" class="tab-content">
      <div class="card">
        <h2 class="card-title"><i class="fa-solid fa-calculator"></i> Аналітичний розв’язок</h2>
        <div class="formula-box">
          dy(x)/dx = –0.9 y, &nbsp; y(0) = 0.12<br>
          dy / y = –0.9 dx &nbsp;⇒&nbsp; ln|y| = –0.9 x + C₁<br>
          y(x) = C · exp(–0.9 x)<br>
          y(0) = C = 0.12 &nbsp;⇒&nbsp; <strong>y(x) = 0.12 · exp(–0.9 x)</strong>
        </div>
      </div>

      <div class="card">
        <h2 class="card-title"><i class="fa-solid fa-flag-checkered"></i> Висновок</h2>
        <p style="font-size: 1.05rem; line-height: 1.8;">
          У лабораторній роботі розв’язано задачу Коші для диференціального рівняння dy(x)/dx = –0,9 y з початковою умовою y(0) = 0,12 (Варіант 12, група ПП-24). Обчислення виконано на відрізку x ∈ [0; 1] при N = 20 кроках (h = 0,05) трьома методами: Ейлера, Гюна та Рунге – Кутта 4-го порядку. Програму складено мовою Python, аналітичний розв’язок y(x) = 0,12 exp(–0,9 x), похибки та графіки побудовано в MS Excel та за допомогою Matplotlib.<br><br>
          Порівняльний аналіз показав, що у кінцевій точці x = 1 абсолютна похибка для методу Ейлера склала Δ₁ ≈ 1,01·10⁻³ (1-й порядок точності), для методу Гюна — Δ₂ ≈ 1,53·10⁻⁵ (2-й порядок), а для методу Рунге – Кутта — Δ₄ ≈ 1,56·10⁻⁹ (4-й порядок). Отже, найменшу похибку та найвищу точність забезпечив метод Рунге – Кутта 4-го порядку, який перевершив метод Ейлера за точністю у понад 640 000 разів.
        </p>
      </div>
    </div>

    <!-- TAB 4: CODE -->
    <div id="tab-code" class="tab-content">
      <div class="card">
        <h2 class="card-title"><i class="fa-brands fa-python"></i> Код програми (main.py)</h2>
        <pre><code>def fun(x, y):
    return -0.9 * y


def euler(y0, x0, x1, n):
    y = y0
    x = x0
    h = (x1 - x0) / n
    print(0, y, x)
    for i in range(1, n + 1):
        k1 = fun(x, y)
        y = y + k1 * h
        x = x + h
        print(i, k1, y, x)


def heun(y0, x0, x1, n):
    y = y0
    x = x0
    h = (x1 - x0) / n
    print(0, y, x)

    for i in range(1, n + 1):
        k1 = fun(x, y)
        k2 = fun(x + h, y + h * k1)
        y = y + (k1 + k2) * h / 2
        x = x + h
        print(i, k1, k2, y, x)


def runge_kutta4(y0, x0, x1, n):
    y = y0
    x = x0
    h = (x1 - x0) / n
    print(0, y, x)

    for i in range(1, n + 1):
        k1 = fun(x, y)
        k2 = fun(x + h / 2, y + k1 * h / 2)
        k3 = fun(x + h / 2, y + k2 * h / 2)
        k4 = fun(x + h, y + k3 * h)
        y = y + (k1 + 2 * k2 + 2 * k3 + k4) * h / 6
        x = x + h
        print(i, k1, k2, k3, k4, y, x)


euler(0.12, 0, 1, 20)
print()
heun(0.12, 0, 1, 20)
print()
runge_kutta4(0.12, 0, 1, 20)
print()</code></pre>
      </div>
    </div>

    <!-- TAB 5: QUESTIONS -->
    <div id="tab-questions" class="tab-content">
      <div class="card">
        <h2 class="card-title"><i class="fa-solid fa-graduation-cap"></i> Контрольні запитання та відповіді (18 питань)</h2>
        <div id="questionsContainer"></div>
      </div>
    </div>

  </main>

  <footer>
    <p>Національний університет «Львівська політехніка» • Кафедра САПР • 2026/2027</p>
    <p>Студент: Лемішка Андрій • Група ПП-24 • Варіант 12 • Викладач: Чумакевич В.В.</p>
  </footer>

  <script>
    function toggleTheme() {
      const html = document.documentElement;
      const isDark = html.classList.toggle('dark');
      html.classList.toggle('light', !isDark);
      document.getElementById('themeIcon').className = isDark ? 'fa-solid fa-moon' : 'fa-solid fa-sun';
      document.getElementById('themeText').innerText = isDark ? 'Темна' : 'Світла';
    }

    function switchTab(tabId) {
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
      event.currentTarget.classList.add('active');
      document.getElementById(tabId).classList.add('active');
    }

    // Computation
    const y0 = 0.12, x0 = 0.0, x1 = 1.0, n = 20, h = (x1 - x0) / n;
    const fun = (x, y) => -0.9 * y;
    const analytical = (x) => 0.12 * Math.exp(-0.9 * x);

    const xVals = [], yExact = [], yEuler = [], yHeun = [], yRK4 = [];
    const deltaEuler = [], deltaHeun = [], deltaRK4 = [];

    let ye = y0, yh = y0, yr = y0, curX = x0;
    xVals.push(0); yExact.push(analytical(0));
    yEuler.push(y0); yHeun.push(y0); yRK4.push(y0);
    deltaEuler.push(0); deltaHeun.push(0); deltaRK4.push(0);

    for (let i = 1; i <= n; i++) {
      let k1_e = fun(curX, ye);
      ye = ye + k1_e * h;

      let k1_h = fun(curX, yh);
      let k2_h = fun(curX + h, yh + h * k1_h);
      yh = yh + (k1_h + k2_h) * h / 2;

      let k1_r = fun(curX, yr);
      let k2_r = fun(curX + h/2, yr + k1_r * h / 2);
      let k3_r = fun(curX + h/2, yr + k2_r * h / 2);
      let k4_r = fun(curX + h, yr + k3_r * h);
      yr = yr + (k1_r + 2*k2_r + 2*k3_r + k4_r) * h / 6;

      curX = x0 + i * h;
      let ex = analytical(curX);

      xVals.push(parseFloat(curX.toFixed(2)));
      yExact.push(ex);
      yEuler.push(ye);
      yHeun.push(yh);
      yRK4.push(yr);

      deltaEuler.push(Math.abs(ex - ye));
      deltaHeun.push(Math.abs(ex - yh));
      deltaRK4.push(Math.abs(ex - yr));
    }

    const tbody = document.querySelector('#summaryTable tbody');
    for (let i = 0; i <= n; i++) {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td>${i}</td>
        <td>${xVals[i].toFixed(2)}</td>
        <td>${yExact[i].toFixed(6)}</td>
        <td>${yEuler[i].toFixed(6)}</td>
        <td style="color: var(--danger);">${deltaEuler[i].toExponential(3)}</td>
        <td>${yHeun[i].toFixed(6)}</td>
        <td style="color: var(--warning);">${deltaHeun[i].toExponential(3)}</td>
        <td>${yRK4[i].toFixed(6)}</td>
        <td style="color: var(--primary); font-weight: 600;">${deltaRK4[i] === 0 ? '0' : deltaRK4[i].toExponential(3)}</td>
      `;
      tbody.appendChild(tr);
    }

    const ctx1 = document.getElementById('functionChart').getContext('2d');
    new Chart(ctx1, {
      type: 'line',
      data: {
        labels: xVals,
        datasets: [
          { label: 'Аналітичний y(x)', data: yExact, borderColor: '#10b981', borderWidth: 3, pointRadius: 0 },
          { label: 'Ейлер (y1)', data: yEuler, borderColor: '#ef4444', borderWidth: 2, borderDash: [4, 4], pointRadius: 4 },
          { label: 'Гюн (y2)', data: yHeun, borderColor: '#f59e0b', borderWidth: 2, borderDash: [2, 2], pointRadius: 4 },
          { label: 'Рунге-Кутта (y4)', data: yRK4, borderColor: '#3b82f6', borderWidth: 2, pointRadius: 4 }
        ]
      },
      options: {
        responsive: true,
        plugins: { legend: { labels: { color: '#9ca3af' } } },
        scales: {
          x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#9ca3af' } },
          y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#9ca3af' } }
        }
      }
    });

    const ctx2 = document.getElementById('errorChart').getContext('2d');
    new Chart(ctx2, {
      type: 'line',
      data: {
        labels: xVals.slice(1),
        datasets: [
          { label: 'Похибка Ейлера (Δ1)', data: deltaEuler.slice(1), borderColor: '#ef4444', borderWidth: 2, pointRadius: 4 },
          { label: 'Похибка Гюна (Δ2)', data: deltaHeun.slice(1), borderColor: '#f59e0b', borderWidth: 2, pointRadius: 4 },
          { label: 'Похибка Рунге-Кутта (Δ4)', data: deltaRK4.slice(1), borderColor: '#3b82f6', borderWidth: 2, pointRadius: 4 }
        ]
      },
      options: {
        responsive: true,
        plugins: { legend: { labels: { color: '#9ca3af' } } },
        scales: {
          x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#9ca3af' } },
          y: { type: 'logarithmic', grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#9ca3af' } }
        }
      }
    });

    const questions = [
      ["1. Як ставиться задача Коші?", "Необхідно знайти розв'язок рівняння dy/dx = f(x, y) на заданому відрізку, який задовольняє початкову умову y(x₀) = y₀. Геометрично це пошук інтегральної кривої, яка проходить через фіксовану точку (x₀; y₀)."],
      ["2. Як класифікуються методи розв'язування задачі Коші?", "Методи діляться на: 1) Аналітичні наближені (формули/ряди: розклад у ряд Тейлора, метод Пікара); 2) Чисельні (таблиця значень у вузлах: Ейлера, Гюна, Рунге-Кутта). Чисельні методи також бувають однокроковими і багатокроковими, явними та неявними."],
      ["3. Які методи відносяться до аналітичних методів розв'язування задачі Коші?", "Метод послідовних наближень (ітерацій) Пікара, метод розкладу в степеневий ряд Тейлора та асимптотичні методи збурень."],
      ["4. Які методи відносяться до чисельних методів розв'язування задачі Коші?", "Однокрокові (Ейлера, Гюна, Рунге-Кутта 2-го..4-го порядків), багатокрокові (Адамса-Башфорта, Адамса-Моултона, Мілна) та неявні методи для жорстких задач (неявний Ейлер, метод Гіра / BDF)."],
      ["5. Які методи відносяться до методів типу Ейлера?", "1) Звичайний явний метод Ейлера (1-й порядок O(h)); 2) Модифікований метод Ейлера (з перерахунком у середній точці h/2, O(h²)); 3) Метод Ейлера-Коші / Гюна (предиктор-коректор, O(h²)); 4) Неявний метод Ейлера (A-стійкий)."],
      ["6. Як розв'язується задача Коші по формулі Ейлера?", "За рекурентною формулою: y_{i+1} = y_i + h · f(x_i, y_i). Функція на кожному кроці наближається дотичною на початку відрізка. Похибка на кроці має порядок O(h)."],
      ["7. Як побудований модифікований метод Ейлера?", "1) Знаходиться значення посередині кроку: y_{i+1/2} = y_i + (h/2)·f(x_i, y_i); 2) Остаточне значення в точці x_{i+1} знаходиться через похідну в середині: y_{i+1} = y_i + h · f(x_i + h/2, y_{i+1/2}). Порядок похибки — O(h²)."],
      ["8. Як розв'язується задача Коші по методу Ейлера-Коші?", "За схемою предиктора-коректора: 1) Прогноз за Ейлером: ỹ_{i+1} = y_i + h · f(x_i, y_i); 2) Корекція через середнє арифметичне похідних на кінцях кроку: y_{i+1} = y_i + (h/2) · [f(x_i, y_i) + f(x_{i+1}, ỹ_{i+1})]. Порядок похибки — O(h²)."],
      ["9. Як розв'язується задача Коші по методу Рунге-Кутта?", "На кожному кроці обчислюють 4 коефіцієнти: k₁ (початок кроку), k₂ і k₃ (два наближення в середині h/2), та k₄ (кінець кроку). Остаточне значення: y_{i+1} = y_i + (h/6)·(k₁ + 2k₂ + 2k₃ + k₄). Метод має 4-й порядок точності O(h⁴)."],
      ["10. Що таке ”жорстке” диференціальне рівняння?", "Це рівняння або система, розв'язок якої містить процеси, що протікають з дуже різними швидкостями (постійні часу відрізняються в сотні або тисячі разів). Швидкі складові швидко затухають, але змушують брати крихітний крок у звичайних методах."],
      ["11. Які задачі зводяться до ”жорстких”?", "Задачі хімічної кінетики (швидкі та повільні реакції), електронні схеми, робототехніка (швидкі струми двигунів і повільний рух маніпулятора) та задачі теплопровідності."],
      ["12. Які методи використовуються для розв'язування ”жорстких” задач?", "Спеціальні стійкі методи: неявний метод Ейлера, неявні методи Рунге-Кутта (Радо, Розенброка) та методи диференціювання назад (методи Гіра / BDF)."],
      ["13. Як побудований неявний метод Ейлера?", "За формулою y_{i+1} = y_i + h · f(x_{i+1}, y_{i+1}). Оскільки y_{i+1} входить у праву частину, на кожному кроці розв'язується алгебраїчне рівняння відносно y_{i+1}. Метод абсолютно стійкий при будь-якому кроці h."],
      ["14. Як будуються неявні схеми методу Рунге-Кутта?", "У неявних схемах коефіцієнти k_j залежать від усіх коефіцієнтів k, тому на кожному кроці розв'язується система рівнянь відносно k₁, ..., k_s."],
      ["15. Яка схема неявного методу Рунге-Кутта другого порядку?", "1) Неявний метод середньої точки: k₁ = f(x_i + h/2, y_i + (h/2)k₁), y_{i+1} = y_i + h·k₁; 2) Неявний метод трапецій: y_{i+1} = y_i + (h/2)[f(x_i, y_i) + f(x_{i+1}, y_{i+1})]. Обидва методи є A-стійкими."],
      ["16. Як побудована схема неявного методу Рунге-Кутта четвертого порядку?", "Це двоетапний метод Гауса-Лежандра: внутрішні точки вибираються на коренях полінома Лежандра, k₁ і k₂ знаходяться із системи двох зв'язаних неявних рівнянь, а крок робиться за формулою y_{i+1} = y_i + (h/2)(k₁ + k₂)."],
      ["17. Який порядок вибору методу розв'язування задачі Коші?", "1) Оцінюють необхідну точність; 2) Перевіряють рівняння на жорсткість; 3) Для звичайних задач беруть класичний метод Рунге-Кутта 4-го порядку; 4) Для тривалого інтегрування — методи Адамса; 5) Для жорстких задач — неявні методи або метод Гіра."],
      ["18. Який із неявних методів забезпечує найвищу точність?", "Неявні методи Рунге-Кутта типу Гауса (Гауса-Лежандра): при s стадіях вони забезпечують максимально можливий порядок точності 2s (наприклад, 2-стадійний дає 4-й порядок, а 3-стадійний — 6-й порядок)."]
    ];

    const qContainer = document.getElementById('questionsContainer');
    questions.forEach(([q, a], idx) => {
      const item = document.createElement('div');
      item.className = 'accordion-item' + (idx === 0 ? ' open' : '');
      item.innerHTML = `
        <div class="accordion-header" onclick="this.parentElement.classList.toggle('open')">
          <span>${q}</span>
          <i class="fa-solid fa-chevron-down"></i>
        </div>
        <div class="accordion-body">
          <p>${a}</p>
        </div>
      `;
      qContainer.appendChild(item);
    });
  </script>
</body>
</html>
'''
    site_path = os.path.join("Lab6", "site", "index.html")
    with open(site_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Updated site: {site_path}")

if __name__ == "__main__":
    generate_site()
