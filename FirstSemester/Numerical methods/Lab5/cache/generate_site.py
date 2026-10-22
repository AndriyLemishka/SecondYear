import os

html_content = '''<!DOCTYPE html>
<html lang="uk" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Чисельні методи • Лабораторна робота №5 | Лемішка Андрій</title>
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

    /* Scrollbar */
    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }
    ::-webkit-scrollbar-track {
      background: var(--bg);
    }
    ::-webkit-scrollbar-thumb {
      background: var(--card-border);
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: var(--primary);
    }

    /* Navigation */
    nav {
      position: sticky;
      top: 0;
      z-index: 100;
      background: var(--nav-bg);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--card-border);
      padding: 0.75rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .nav-brand {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-weight: 700;
      font-size: 1.15rem;
      color: var(--text);
      text-decoration: none;
    }

    .nav-brand .badge {
      background: linear-gradient(135deg, var(--primary), var(--accent));
      color: #fff;
      font-size: 0.75rem;
      padding: 0.2rem 0.55rem;
      border-radius: 9999px;
      font-weight: 600;
    }

    .nav-links {
      display: flex;
      gap: 1.5rem;
      align-items: center;
      list-style: none;
    }

    .nav-links a {
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 500;
      transition: color 0.2s ease;
    }

    .nav-links a:hover {
      color: var(--primary);
    }

    .theme-toggle {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      color: var(--text);
      padding: 0.45rem 0.8rem;
      border-radius: 0.5rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.85rem;
      transition: all 0.2s ease;
    }

    .theme-toggle:hover {
      border-color: var(--primary);
    }

    /* Container */
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 2.5rem 1.5rem;
    }

    /* Hero Section */
    .hero {
      text-align: center;
      padding: 3rem 1rem 4rem;
      background: radial-gradient(circle at 50% 20%, var(--primary-glow), transparent 70%);
      border-radius: 1.5rem;
      margin-bottom: 3rem;
      border: 1px solid var(--card-border);
    }

    .hero-meta {
      display: inline-flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-bottom: 1.25rem;
      justify-content: center;
    }

    .pill {
      background: rgba(59, 130, 246, 0.12);
      border: 1px solid rgba(59, 130, 246, 0.3);
      color: var(--primary);
      padding: 0.3rem 0.75rem;
      border-radius: 9999px;
      font-size: 0.82rem;
      font-weight: 600;
    }

    .pill.green {
      background: rgba(16, 185, 129, 0.12);
      border-color: rgba(16, 185, 129, 0.3);
      color: var(--secondary);
    }

    .pill.purple {
      background: rgba(139, 92, 246, 0.12);
      border-color: rgba(139, 92, 246, 0.3);
      color: var(--accent);
    }

    h1 {
      font-size: 2.5rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      margin-bottom: 1rem;
      background: linear-gradient(135deg, var(--text) 40%, var(--primary));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
      font-size: 1.15rem;
      color: var(--text-muted);
      max-width: 750px;
      margin: 0 auto 2rem;
    }

    .equation-box {
      display: inline-block;
      background: var(--card-bg);
      border: 2px solid var(--primary);
      padding: 1.25rem 2.5rem;
      border-radius: 1rem;
      box-shadow: 0 10px 30px var(--primary-glow);
      margin-bottom: 2rem;
    }

    .equation-box .eq {
      font-size: 1.6rem;
      font-weight: 700;
      font-family: 'Cambria Math', 'KaTeX_Math', serif;
      letter-spacing: 0.05em;
    }

    .equation-box .target-root {
      font-size: 0.95rem;
      color: var(--secondary);
      margin-top: 0.5rem;
      font-weight: 600;
    }

    /* Grid Layouts */
    .grid-2 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1.75rem;
      margin-bottom: 2.5rem;
    }

    .grid-3 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1.5rem;
      margin-bottom: 2.5rem;
    }

    /* Cards */
    .card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 1rem;
      padding: 1.75rem;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
      transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .card:hover {
      border-color: rgba(59, 130, 246, 0.4);
      transform: translateY(-2px);
    }

    .card-title {
      font-size: 1.25rem;
      font-weight: 700;
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--text);
    }

    .card-title .icon {
      width: 1.75rem;
      height: 1.75rem;
      border-radius: 0.5rem;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.9rem;
      background: var(--primary-glow);
      color: var(--primary);
    }

    /* Sections */
    section {
      margin-bottom: 3.5rem;
    }

    .section-header {
      margin-bottom: 1.5rem;
    }

    .section-header h2 {
      font-size: 1.85rem;
      font-weight: 800;
      margin-bottom: 0.5rem;
    }

    .section-header p {
      color: var(--text-muted);
      font-size: 1rem;
    }

    /* Math steps & highlight */
    .math-step {
      background: var(--code-bg);
      border-left: 4px solid var(--primary);
      padding: 1rem 1.25rem;
      border-radius: 0 0.5rem 0.5rem 0;
      margin: 1rem 0;
      font-family: 'Cambria Math', 'Consolas', monospace;
      font-size: 0.95rem;
    }

    .callout {
      background: rgba(59, 130, 246, 0.08);
      border: 1px solid rgba(59, 130, 246, 0.25);
      border-radius: 0.75rem;
      padding: 1.25rem;
      margin: 1.25rem 0;
    }

    .callout.green {
      background: rgba(16, 185, 129, 0.08);
      border-color: rgba(16, 185, 129, 0.25);
    }

    .callout.amber {
      background: rgba(245, 158, 11, 0.08);
      border-color: rgba(245, 158, 11, 0.25);
    }

    .callout-title {
      font-weight: 700;
      font-size: 0.95rem;
      margin-bottom: 0.35rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    /* Simulator styling */
    .sim-container {
      background: var(--code-bg);
      border: 1px solid var(--card-border);
      border-radius: 1rem;
      padding: 1.5rem;
      margin-top: 1.5rem;
    }

    .sim-controls {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      align-items: center;
      margin-bottom: 1.25rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid var(--card-border);
    }

    .btn {
      background: var(--primary);
      color: #fff;
      border: none;
      padding: 0.6rem 1.2rem;
      border-radius: 0.5rem;
      font-weight: 600;
      font-size: 0.9rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: background 0.2s ease, transform 0.1s ease;
    }

    .btn:hover {
      background: var(--primary-hover);
    }

    .btn:active {
      transform: scale(0.98);
    }

    .btn.secondary {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      color: var(--text);
    }

    .btn.secondary:hover {
      border-color: var(--primary);
      color: var(--primary);
    }

    .canvas-wrapper {
      position: relative;
      width: 100%;
      height: 380px;
      background: var(--bg);
      border-radius: 0.75rem;
      border: 1px solid var(--card-border);
      overflow: hidden;
    }

    canvas {
      display: block;
      width: 100%;
      height: 100%;
    }

    .sim-info {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 1rem;
      margin-top: 1.25rem;
    }

    .stat-badge {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      padding: 0.85rem;
      border-radius: 0.5rem;
      text-align: center;
    }

    .stat-badge .label {
      font-size: 0.75rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.25rem;
    }

    .stat-badge .val {
      font-size: 1.1rem;
      font-weight: 700;
      font-family: monospace;
      color: var(--text);
    }

    /* Comparison Table */
    .table-container {
      overflow-x: auto;
      border-radius: 0.75rem;
      border: 1px solid var(--card-border);
      margin: 1.5rem 0;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.92rem;
    }

    th {
      background: rgba(59, 130, 246, 0.12);
      color: var(--text);
      font-weight: 700;
      padding: 0.85rem 1rem;
      border-bottom: 2px solid var(--card-border);
    }

    td {
      padding: 0.75rem 1rem;
      border-bottom: 1px solid var(--card-border);
      color: var(--text);
    }

    tr:nth-child(even) {
      background: var(--table-stripe);
    }

    tr:hover {
      background: rgba(59, 130, 246, 0.05);
    }

    /* Interactive Quiz */
    .quiz-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 1rem;
      padding: 1.75rem;
      margin-bottom: 1.5rem;
    }

    .quiz-q {
      font-weight: 700;
      font-size: 1.05rem;
      margin-bottom: 1rem;
      display: flex;
      gap: 0.5rem;
    }

    .quiz-options {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .quiz-option {
      background: var(--code-bg);
      border: 1px solid var(--card-border);
      padding: 0.75rem 1rem;
      border-radius: 0.5rem;
      cursor: pointer;
      transition: all 0.2s ease;
      font-size: 0.9rem;
    }

    .quiz-option:hover {
      border-color: var(--primary);
    }

    .quiz-option.correct {
      background: rgba(16, 185, 129, 0.15);
      border-color: var(--secondary);
      color: var(--secondary);
      font-weight: 600;
    }

    .quiz-option.wrong {
      background: rgba(239, 68, 68, 0.15);
      border-color: var(--danger);
      color: var(--danger);
    }

    .quiz-explanation {
      margin-top: 0.75rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      padding: 0.75rem;
      border-radius: 0.4rem;
      background: rgba(255, 255, 255, 0.03);
      display: none;
    }

    /* Accordion FAQ */
    .faq-item {
      border: 1px solid var(--card-border);
      border-radius: 0.6rem;
      margin-bottom: 0.75rem;
      overflow: hidden;
      background: var(--card-bg);
    }

    .faq-question {
      padding: 1rem 1.25rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: background 0.2s ease;
    }

    .faq-question:hover {
      background: rgba(59, 130, 246, 0.05);
    }

    .faq-answer {
      padding: 0 1.25rem;
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.3s ease, padding 0.3s ease;
      color: var(--text-muted);
      font-size: 0.92rem;
      border-top: 1px solid transparent;
    }

    .faq-item.open .faq-answer {
      padding: 1rem 1.25rem;
      max-height: 500px;
      border-top-color: var(--card-border);
    }

    /* Code Block */
    pre {
      background: var(--code-bg);
      border: 1px solid var(--card-border);
      border-radius: 0.75rem;
      padding: 1.25rem;
      overflow-x: auto;
      font-family: 'Consolas', 'Courier New', monospace;
      font-size: 0.88rem;
      line-height: 1.5;
    }

    /* Tabs */
    .tabs-header {
      display: flex;
      gap: 0.5rem;
      border-bottom: 1px solid var(--card-border);
      margin-bottom: 1.5rem;
    }

    .tab-btn {
      padding: 0.75rem 1.25rem;
      background: transparent;
      border: none;
      border-bottom: 2px solid transparent;
      color: var(--text-muted);
      font-weight: 600;
      font-size: 0.95rem;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .tab-btn.active {
      color: var(--primary);
      border-bottom-color: var(--primary);
    }

    .tab-pane {
      display: none;
    }

    .tab-pane.active {
      display: block;
    }

    footer {
      border-top: 1px solid var(--card-border);
      padding: 2.5rem 1.5rem;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.88rem;
    }

    @media (max-width: 768px) {
      nav {
        padding: 0.75rem 1rem;
      }
      .nav-links {
        display: none;
      }
      h1 {
        font-size: 1.85rem;
      }
      .equation-box {
        padding: 1rem 1.5rem;
      }
    }
  </style>
</head>
<body>

  <!-- Navigation -->
  <nav>
    <a href="#" class="nav-brand">
      <span>📐 Чисельні методи</span>
      <span class="badge">ЛР №5</span>
    </a>
    <ul class="nav-links">
      <li><a href="#overview">Варіант 12</a></li>
      <li><a href="#theory">Математичний апарат</a></li>
      <li><a href="#simulators">Інтерактивний симулятор</a></li>
      <li><a href="#comparison">Порівняння методів</a></li>
      <li><a href="#practicum">Практикум та захист</a></li>
      <li><a href="#code">Код і файли</a></li>
    </ul>
    <button class="theme-toggle" id="themeToggle" onclick="toggleTheme()">
      <span id="themeIcon">☀️</span>
      <span id="themeLabel">Тема</span>
    </button>
  </nav>

  <div class="container">

    <!-- Hero Section -->
    <div class="hero">
      <div class="hero-meta">
        <span class="pill">НУ «Львівська політехніка»</span>
        <span class="pill green">Кафедра САПР • ІКНІТ</span>
        <span class="pill purple">Група: ПП-24</span>
        <span class="pill">Студент: Лемішка Андрій</span>
        <span class="pill green">Викладач: Чумакевич В.В.</span>
      </div>
      <h1>Чисельне розв’язування нелінійного рівняння</h1>
      <p class="hero-subtitle">
        Інтерактивний посібник, покроковий практикум та тренажер для захисту лабораторної роботи № 5. Порівняння методу половинного ділення (дихотомії) та методу дотичних Ньютона.
      </p>

      <div class="equation-box">
        <div class="eq">f(x) = x² + 0,78x – 0,108 = 0</div>
        <div class="target-root">🎯 Ціль: знайти додатний корінь x* = 0,12 з точністю δ = 10⁻¹⁰</div>
      </div>

      <div class="grid-3" style="margin-top: 1.5rem;">
        <div class="stat-badge">
          <div class="label">Метод бісекції</div>
          <div class="val" style="color: #3b82f6;">33 ітерації</div>
          <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.2rem;">Лінійна збіжність O(n)</div>
        </div>
        <div class="stat-badge">
          <div class="label">Метод Ньютона</div>
          <div class="val" style="color: #10b981;">5 ітерацій</div>
          <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.2rem;">Квадратична збіжність O(n²)</div>
        </div>
        <div class="stat-badge">
          <div class="label">Прискорення Ньютона</div>
          <div class="val" style="color: #8b5cf6;">у 6,6 раза швидше</div>
          <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.2rem;">Похибка |f(x₅)| ~ 10⁻¹⁴</div>
        </div>
      </div>
    </div>

    <!-- Section 1: Overview & Math -->
    <section id="overview">
      <div class="section-header">
        <h2>1. Математична постановка задачі (Варіант 12)</h2>
        <p>Аналітичні викладки, дослідження функції та визначення точного розв’язку</p>
      </div>

      <div class="grid-2">
        <div class="card">
          <div class="card-title">
            <span class="icon">✏️</span>
            Аналітичний розв’язок через дискримінант
          </div>
          <p>Рівняння є квадратним $ax^2 + bx + c = 0$, де $a = 1$, $b = 0,78$, $c = -0,108$.</p>
          <div class="math-step">
            D = b² – 4ac<br>
            D = 0,78² – 4 · 1 · (–0,108) = 0,6084 + 0,4320 = 1,0404<br>
            √D = √1,0404 = 1,02
          </div>
          <p>Обчислюємо корені за класичною формулою Вієта / квадратного рівняння:</p>
          <div class="math-step">
            x₁ = (–0,78 – 1,02) / 2 = –1,80 / 2 = <strong>–0,9</strong><br>
            x₂ = (–0,78 + 1,02) / 2 = 0,24 / 2 = <strong>+0,12</strong>
          </div>
          <div class="callout green">
            <div class="callout-title">✅ Результат аналізу</div>
            У завданні потрібно знайти <strong>додатний корінь</strong>. Отже, точний шуканий розв'язок: <strong>x* = 0,12</strong>.
          </div>
        </div>

        <div class="card">
          <div class="card-title">
            <span class="icon">📈</span>
            Похідні та геометричні властивості
          </div>
          <p>Для методу Ньютона необхідний аналітичний вираз першої похідної:</p>
          <div class="math-step">
            f'(x) = d(x² + 0,78x – 0,108) / dx = <strong>2x + 0,78</strong><br>
            f''(x) = d²f / dx² = <strong>2 > 0</strong> (парабола напрямлена вітками вгору)
          </div>
          <p><strong>Вибір початкового інтервалу для бісекції [0; 0,35]:</strong></p>
          <div class="math-step">
            f(0) = 0² + 0,78(0) – 0,108 = <strong>–0,108 < 0</strong><br>
            f(0,35) = 0,35² + 0,78(0,35) – 0,108 = 0,1225 + 0,273 – 0,108 = <strong>+0,2875 > 0</strong>
          </div>
          <div class="callout">
            <div class="callout-title">💡 Теорема Больцано — Коші</div>
            Оскільки $f(0) \cdot f(0,35) < 0$ і функція неперервна, на відрізку $[0; 0,35]$ гарантовано існує хоча б один дійсний корінь (наш $x = 0,12$).
          </div>
        </div>
      </div>
    </section>

    <!-- Section 2: Theory of Methods -->
    <section id="theory">
      <div class="section-header">
        <h2>2. Теорія чисельних методів: Що і як відбувається</h2>
        <p>Детальний розбір механіки роботи кожного алгоритму з формулами та оцінками збіжності</p>
      </div>

      <div class="grid-2">
        <!-- Bisection -->
        <div class="card">
          <div class="card-title">
            <span class="icon">✂️</span>
            Метод половинного ділення (Бісекції)
          </div>
          <p><strong>Суть методу:</strong> послідовне ділення навпіл інтервалу $[a, b]$, на кінцях якого функція приймає протилежні знаки ($f(a) \cdot f(b) < 0$).</p>
          
          <h4 style="margin: 1rem 0 0.5rem; font-size: 0.95rem;">Алгоритм кроків:</h4>
          <ol style="margin-left: 1.25rem; font-size: 0.9rem; color: var(--text-muted); line-height: 1.7;">
            <li>Знаходимо середину інтервалу: $c_i = \frac{a_i + b_i}{2}$.</li>
            <li>Обчислюємо $f(c_i)$ та визначаємо його знак.</li>
            <li>Перевіряємо умову зупинки: якщо $|b_i - a_i| < \delta$, зупиняємось ($x^* \approx c_i$).</li>
            <li>Якщо $\text{sign}(f(b_i)) \cdot \text{sign}(f(c_i)) > 0$, корінь ліворуч, тому нова права межа $b_{i+1} = c_i$.</li>
            <li>Інакше корінь праворуч, тому нова ліва межа $a_{i+1} = c_i$.</li>
          </ol>

          <div class="callout amber">
            <div class="callout-title">📐 Апріорна оцінка кількості ітерацій N</div>
            Довжина інтервалу зменшується рівно в $2^N$ разів: $\frac{b - a}{2^N} \le \delta$.<br>
            Для нашого випадку:
            $$N \ge \log_2\left(\frac{0,35 - 0}{10^{-10}}\right) = \log_2(3,5 \times 10^9) \approx 31,7$$
            Округлення вгору дає <strong>32 кроки</strong>. Саме тому програма завершила роботу на 32-й ітерації (всього 33 кроки: 0..32)!
          </div>
        </div>

        <!-- Newton -->
        <div class="card">
          <div class="card-title">
            <span class="icon">⚡</span>
            Метод Ньютона (Дотичних)
          </div>
          <p><strong>Суть методу:</strong> заміна нелінійної функції її дотичною лінією в поточній точці $x_k$ за допомогою лінійного розкладу Тейлора.</p>
          
          <h4 style="margin: 1rem 0 0.5rem; font-size: 0.95rem;">Ітераційна формула:</h4>
          <div class="math-step">
            f(x) ≈ f(x_k) + f'(x_k) · (x – x_k) = 0<br>
            <strong>x_{k+1} = x_k – \frac{f(x_k)}{f'(x_k)}</strong>
          </div>

          <h4 style="margin: 1rem 0 0.5rem; font-size: 0.95rem;">Умова збіжності (Теорема Фур’є):</h4>
          <p style="font-size: 0.9rem; color: var(--text-muted);">
            Якщо на відрізку $[a, b]$ перша і друга похідні зберігають постійний знак, а початкове наближення $x_0$ вибрано так, що <strong>$f(x_0) \cdot f''(x_0) > 0$</strong>, то метод гарантовано і монотонно збігається.
          </p>

          <div class="callout green">
            <div class="callout-title">🚀 Чому така швидкість? (Квадратична збіжність)</div>
            Якщо похибка на кроці $k$ дорівнює $\varepsilon_k$, то на кроці $k+1$: $\varepsilon_{k+1} \approx C \cdot \varepsilon_k^2$.<br>
            Кількість вірних десяткових знаків <strong>подвоюється</strong> на кожній ітерації:<br>
            $k=1 \implies |x - x^*| \approx 1,8 \times 10^{-2}$<br>
            $k=2 \implies |x - x^*| \approx 3,2 \times 10^{-4}$<br>
            $k=3 \implies |x - x^*| \approx 1,0 \times 10^{-7}$<br>
            $k=4 \implies |x - x^*| \approx 1,0 \times 10^{-14}$ (машинна точність досягнута!).
          </div>
        </div>
      </div>
    </section>

    <!-- Section 3: Interactive Simulators -->
    <section id="simulators">
      <div class="section-header">
        <h2>3. Інтерактивний практикум: Живі симулятори на Canvas</h2>
        <p>Покроково спостерігайте, як алгоритми знаходять корінь $x = 0,12$ у реальному часі</p>
      </div>

      <!-- Simulator Tabs -->
      <div class="tabs-header">
        <button class="tab-btn active" onclick="switchSim('bisection')">Метод половинного ділення (Бісекція)</button>
        <button class="tab-btn" onclick="switchSim('newton')">Метод Ньютона (Дотичних)</button>
      </div>

      <!-- Bisection Simulator Pane -->
      <div id="sim-bisection-pane" class="tab-pane active">
        <div class="sim-container">
          <div class="sim-controls">
            <button class="btn" onclick="stepBisection()">▶ Наступний крок</button>
            <button class="btn secondary" onclick="autoRunBisection()" id="btnAutoBis">⏩ Автоматично</button>
            <button class="btn secondary" onclick="resetBisection()">↺ Скинути</button>
            <span style="font-size: 0.9rem; color: var(--text-muted); margin-left: auto;" id="bisStatus">
              Крок: 0 / 10 | Інтервал [0; 0.35]
            </span>
          </div>

          <div class="canvas-wrapper">
            <canvas id="bisectionCanvas"></canvas>
          </div>

          <div class="sim-info">
            <div class="stat-badge">
              <div class="label">Ліва межа (a)</div>
              <div class="val" id="valA">0.000000</div>
            </div>
            <div class="stat-badge">
              <div class="label">Середина (c) / Наближення</div>
              <div class="val" style="color: var(--primary);" id="valC">0.175000</div>
            </div>
            <div class="stat-badge">
              <div class="label">Права межа (b)</div>
              <div class="val" id="valB">0.350000</div>
            </div>
            <div class="stat-badge">
              <div class="label">Довжина відрізка (b - a)</div>
              <div class="val" style="color: var(--accent);" id="valWidth">0.350000</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Newton Simulator Pane -->
      <div id="sim-newton-pane" class="tab-pane">
        <div class="sim-container">
          <div class="sim-controls">
            <button class="btn" onclick="stepNewton()">▶ Наступний крок</button>
            <button class="btn secondary" onclick="autoRunNewton()" id="btnAutoNewt">⏩ Автоматично</button>
            <button class="btn secondary" onclick="resetNewton()">↺ Скинути</button>
            <span style="font-size: 0.9rem; color: var(--text-muted); margin-left: auto;" id="newtStatus">
              Крок: 0 / 5 | x₀ = 0.0
            </span>
          </div>

          <div class="canvas-wrapper">
            <canvas id="newtonCanvas"></canvas>
          </div>

          <div class="sim-info">
            <div class="stat-badge">
              <div class="label">Поточне x_k</div>
              <div class="val" id="valNewtX">0.000000</div>
            </div>
            <div class="stat-badge">
              <div class="label">Значення f(x_k)</div>
              <div class="val" id="valNewtF">-0.108000</div>
            </div>
            <div class="stat-badge">
              <div class="label">Похідна f'(x_k)</div>
              <div class="val" id="valNewtDF">0.780000</div>
            </div>
            <div class="stat-badge">
              <div class="label">Наступне x_{k+1}</div>
              <div class="val" style="color: var(--secondary);" id="valNewtNext">0.138462</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 4: Comparison Table & Analysis -->
    <section id="comparison">
      <div class="section-header">
        <h2>4. Порівняльний аналіз (Бісекція vs Ньютон)</h2>
        <p>Головні відмінності, переваги, недоліки та практичні висновки</p>
      </div>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Параметр / Характеристика</th>
              <th>Метод половинного ділення (Дихотомія)</th>
              <th>Метод Ньютона (Дотичних)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Швидкість збіжності</strong></td>
              <td>Лінійна (похибка зменшується в 2 рази за крок)</td>
              <td><span style="color: var(--secondary); font-weight: 700;">Квадратична</span> (похибка зводиться у квадрат)</td>
            </tr>
            <tr>
              <td><strong>Кількість ітерацій (δ = 10⁻¹⁰)</strong></td>
              <td>33 ітерації (кроки 0..32)</td>
              <td><span style="color: var(--secondary); font-weight: 700;">5 ітерацій</span> (у 6.6 разів швидше)</td>
            </tr>
            <tr>
              <td><strong>Необхідні вхідні дані</strong></td>
              <td>Відрізок $[a, b]$, де $f(a) \cdot f(b) < 0$</td>
              <td>Початкова точка $x_0$ та аналітична похідна $f'(x)$</td>
            </tr>
            <tr>
              <td><strong>Обчислювальна складність кроку</strong></td>
              <td>1 обчислення функції $f(c)$</td>
              <td>1 обчислення $f(x)$ та 1 обчислення похідної $f'(x)$</td>
            </tr>
            <tr>
              <td><strong>Гарантія збіжності</strong></td>
              <td><span style="color: var(--secondary); font-weight: 700;">100% гарантована</span> для будь-якої неперервної функції</td>
              <td>Лише при вдалому виборі $x_0$; може розходитися, якщо $f'(x) \approx 0$</td>
            </tr>
            <tr>
              <td><strong>Чутливість до локальних екстремумів</strong></td>
              <td>Не чутливий</td>
              <td>Висока (якщо потрапить у точку $f'(x)=0$, ділення на нуль)</td>
            </tr>
            <tr>
              <td><strong>Рекомендована сфера застосування</strong></td>
              <td>Груба початкова локалізація кореня (звуження інтервалу)</td>
              <td>Швидке уточнення кореня з екстремальною точністю</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout green">
        <div class="callout-title">💡 Ідеальна гібридна інженерна стратегія (Метод Брента)</div>
        На практиці в інженерних бібліотеках (наприклад, <code>scipy.optimize.brentq</code>) спочатку застосовують кілька кроків <strong>бісекції</strong> для надійної локалізації вузького околу кореня, а потім перемикаються на <strong>метод Ньютона</strong> для надшвидкого досягнення машинної точності.
      </div>
    </section>

    <!-- Section 5: Defense Preparation & Quiz -->
    <section id="practicum">
      <div class="section-header">
        <h2>5. Підготовка до захисту: Запитання викладача та тренажер (Quiz)</h2>
        <p>Розбір обов’язкових контрольних запитань та інтерактивний тест перед здачею лабораторної</p>
      </div>

      <h3 style="margin-bottom: 1rem; font-size: 1.25rem;">❓ Топ-5 підступних запитань викладача на захисті</h3>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          1. Чому метод Ньютона зійшовся за 5 ітерацій, а бісекція аж за 33?
          <span>▼</span>
        </div>
        <div class="faq-answer">
          <strong>Відповідь:</strong> Метод бісекції має лінійну швидкість збіжності — інтервал невизначеності ділиться навпіл на кожному кроці ($O(n)$), зменшуючи похибку за законом $\Delta_k = \frac{b-a}{2^k}$. Щоб зменшити похибку від $0,35$ до $10^{-10}$, потрібно $\approx 32$ поділи. Метод Ньютона має <strong>квадратичну збіжність</strong> ($O(n^2)$): на кожній ітерації подвоюється кількість вірних знаків після коми ($\varepsilon_{k+1} \approx C \cdot \varepsilon_k^2$). Тому він досягає похибки $\sim 10^{-14}$ усього за 5 кроків.
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          2. Що станеться в методі Ньютона, якщо в точці наближення похідна f'(x) = 0?
          <span>▼</span>
        </div>
        <div class="faq-answer">
          <strong>Відповідь:</strong> У формулі $x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$ відбудеться ділення на нуль (або отримаємо $\infty$). Геометрично це означає, що дотична паралельна осі абсцис $Ox$ і ніколи її не перетне. Алгоритм аварійно зупиниться або піде у нескінченність.
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          3. Чому для бісекції обов'язково f(a) · f(b) &lt; 0 і що буде, якщо там 2 корені?
          <span>▼</span>
        </div>
        <div class="faq-answer">
          <strong>Відповідь:</strong> Умова $f(a) \cdot f(b) < 0$ (за теоремою Больцано — Коші) гарантує, що неперервна крива перетинає вісь $Ox$ непарну кількість разів. Якщо на інтервалі 2 корені, то $f(a)$ і $f(b)$ мають однаковий знак ($f(a) \cdot f(b) > 0$), і класичний метод бісекції взагалі не зможе почати роботу, оскільки "не бачить" наявності коренів.
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          4. Чим відрізняється метод золотого перерізу від бісекції?
          <span>▼</span>
        </div>
        <div class="faq-answer">
          <strong>Відповідь:</strong> У методі бісекції інтервал ділиться рівно навпіл ($c = (a+b)/2$), що вимагає обчислення значення функції на кожному кроці. У методі золотого січення поділ здійснюється у пропорції золотого перерізу ($0,618$). Завдяки симетрії властивостей золотого перерізу одна з внутрішніх точок перевикористовується на наступній ітерації, що суттєво заощаджує час при обчисленні складних і ресурсомістких функцій.
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          5. Що таке трансцендентне рівняння і чим воно відрізняється від алгебраїчного?
          <span>▼</span>
        </div>
        <div class="faq-answer">
          <strong>Відповідь:</strong> Алгебраїчне рівняння містить лише поліноми (додавання, віднімання, множення та піднесення до цілого степеня, як наше $x^2 + 0,78x - 0,108 = 0$). Трансцендентне рівняння містить неалгебраїчні (трансцендентні) функції: $\sin x$, $\cos x$, $e^x$, $\ln x$, $\text{tg } x$. Його корені в загальному випадку неможливо виразити через скінченну комбінацію арифметичних операцій і радикалів, тому їх розв'язують виключно чисельними методами.
        </div>
      </div>

      <h3 style="margin: 2.5rem 0 1rem; font-size: 1.25rem;">🧠 Інтерактивний тест на самоперевірку (Quiz)</h3>

      <div id="quizContainer">
        <!-- Q1 -->
        <div class="quiz-card" data-correct="1">
          <div class="quiz-q">
            <span>1.</span> Який додатний корінь рівняння f(x) = x² + 0,78x – 0,108 = 0 у варіанті 12?
          </div>
          <div class="quiz-options">
            <div class="quiz-option" onclick="checkOption(this, 0)">x = 0,30</div>
            <div class="quiz-option" onclick="checkOption(this, 1)">x = 0,12</div>
            <div class="quiz-option" onclick="checkOption(this, 2)">x = 0,78</div>
            <div class="quiz-option" onclick="checkOption(this, 3)">x = -0,90</div>
          </div>
          <div class="quiz-explanation">
            <strong>Правильно!</strong> За дискримінантом $D = 1,0404$, $\sqrt{D} = 1,02$, додатний корінь $x_2 = (-0,78 + 1,02)/2 = 0,12$. Корінь -0,90 є від'ємним.
          </div>
        </div>

        <!-- Q2 -->
        <div class="quiz-card" data-correct="2">
          <div class="quiz-q">
            <span>2.</span> Яка швидкість збіжності характерна для методу Ньютона в околі простого кореня?
          </div>
          <div class="quiz-options">
            <div class="quiz-option" onclick="checkOption(this, 0)">Лінійна O(n)</div>
            <div class="quiz-option" onclick="checkOption(this, 1)">Логарифмічна O(log n)</div>
            <div class="quiz-option" onclick="checkOption(this, 2)">Квадратична O(n²)</div>
            <div class="quiz-option" onclick="checkOption(this, 3)">Кубічна O(n³)</div>
          </div>
          <div class="quiz-explanation">
            <strong>Правильно!</strong> Метод Ньютона має квадратичну швидкість збіжності ($\varepsilon_{k+1} \approx C \cdot \varepsilon_k^2$), тобто точність (кількість вірних десяткових знаків) подвоюється на кожному кроці.
          </div>
        </div>

        <!-- Q3 -->
        <div class="quiz-card" data-correct="0">
          <div class="quiz-q">
            <span>3.</span> Скільки ітерацій знадобилося методу бісекції для досягнення точності δ = 10⁻¹⁰ на відрізку [0; 0,35]?
          </div>
          <div class="quiz-options">
            <div class="quiz-option" onclick="checkOption(this, 0)">33 ітерації (кроки 0..32)</div>
            <div class="quiz-option" onclick="checkOption(this, 1)">5 ітерацій</div>
            <div class="quiz-option" onclick="checkOption(this, 2)">12 ітерацій</div>
            <div class="quiz-option" onclick="checkOption(this, 3)">60 ітерацій</div>
          </div>
          <div class="quiz-explanation">
            <strong>Правильно!</strong> Згідно з апріорною формулою $N \ge \log_2(0,35 / 10^{-10}) \approx 31,7$, знадобилося рівно 32 поділи (33 кроки: від 0 до 32).
          </div>
        </div>
      </div>
    </section>

    <!-- Section 6: Code & Files -->
    <section id="code">
      <div class="section-header">
        <h2>6. Програмний код та файли проекту</h2>
        <p>Готовий скрипт мовою Python та перелік згенерованих матеріалів</p>
      </div>

      <div class="grid-2">
        <div class="card">
          <div class="card-title">
            <span class="icon">🐍</span>
            main.py (Реалізація методів)
          </div>
          <pre><code>import math

def fun(x):
    return x**2 + 0.78 * x - 0.108

def dfun(x):
    return 2 * x + 0.78

def bisection(a, b, delta):
    fa = fun(a)
    signa = int(math.copysign(1, fa))
    fb = fun(b)
    signb = int(math.copysign(1, fb))
    
    for i in range(60):
        c = (a + b) / 2
        fc = fun(c)
        signc = int(math.copysign(1, fc))
        eps = abs(a - b)
        print(i, a, signa, b, signb, c, signc)
        
        if eps &lt; delta:
            break
        if signb * signc &gt; 0:
            b = c
            signb = signc
        else:
            a = c
            signa = signc

def newton(x, delta):
    print(0, x) 
    for i in range(1, 20):
        f = fun(x)
        df = dfun(x)
        x1 = x - f / df
        eps = abs(x1 - x)
        ksi = 2 * eps / (abs(x1) + delta)
        print(i, f, df, x1)
        
        if eps &lt; delta or ksi &lt; delta:
            break
        x = x1

bisection(0, 0.35, 1e-10)
print()
newton(0, 1e-10)</code></pre>
        </div>

        <div class="card">
          <div class="card-title">
            <span class="icon">📂</span>
            Файли лабораторної роботи
          </div>
          <p style="margin-bottom: 1rem; color: var(--text-muted);">Усі звіти та розрахунки сформовані у відповідних директоріях:</p>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.75rem;">
            <li style="padding: 0.6rem 0.8rem; background: var(--code-bg); border-radius: 0.5rem; border: 1px solid var(--card-border); display: flex; justify-content: space-between; align-items: center;">
              <span>📄 <strong>Лемішка_Андрій_ЛР5_ПП24.pdf</strong></span>
              <span class="pill green">Готовий звіт</span>
            </li>
            <li style="padding: 0.6rem 0.8rem; background: var(--code-bg); border-radius: 0.5rem; border: 1px solid var(--card-border); display: flex; justify-content: space-between; align-items: center;">
              <span>📝 <strong>Лемішка_Андрій_ЛР5_ПП24.docx</strong></span>
              <span class="pill">Документ Word</span>
            </li>
            <li style="padding: 0.6rem 0.8rem; background: var(--code-bg); border-radius: 0.5rem; border: 1px solid var(--card-border); display: flex; justify-content: space-between; align-items: center;">
              <span>📊 <strong>src/nonlinear_equation.xlsx</strong></span>
              <span class="pill purple">Таблиці та графіки</span>
            </li>
            <li style="padding: 0.6rem 0.8rem; background: var(--code-bg); border-radius: 0.5rem; border: 1px solid var(--card-border); display: flex; justify-content: space-between; align-items: center;">
              <span>🖼️ <strong>plots/bisection_plot.png</strong></span>
              <span class="pill">Графік бісекції</span>
            </li>
            <li style="padding: 0.6rem 0.8rem; background: var(--code-bg); border-radius: 0.5rem; border: 1px solid var(--card-border); display: flex; justify-content: space-between; align-items: center;">
              <span>🖼️ <strong>plots/newton_plot.png</strong></span>
              <span class="pill">Графік Ньютона</span>
            </li>
          </ul>
        </div>
      </div>
    </section>

  </div>

  <footer>
    <p>Національний університет «Львівська політехніка» • Кафедра систем автоматизованого проектування (САПР)</p>
    <p style="margin-top: 0.25rem;">Лабораторна робота № 5 • Студент: Лемішка Андрій (ПП-24) • Варіант 12 • Викладач: Чумакевич В.В.</p>
  </footer>

  <!-- JavaScript for Interactive Simulators & Logic -->
  <script>
    // Theme toggle
    function toggleTheme() {
      const html = document.documentElement;
      if (html.classList.contains('dark')) {
        html.classList.remove('dark');
        html.classList.add('light');
        document.getElementById('themeIcon').textContent = '🌙';
      } else {
        html.classList.remove('light');
        html.classList.add('dark');
        document.getElementById('themeIcon').textContent = '☀️';
      }
      drawBisection();
      drawNewton();
    }

    // Function definition: f(x) = x^2 + 0.78x - 0.108
    function f(x) {
      return x * x + 0.78 * x - 0.108;
    }
    function df(x) {
      return 2 * x + 0.78;
    }

    // Tab Switcher
    function switchSim(simName) {
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
      
      if (simName === 'bisection') {
        event.currentTarget.classList.add('active');
        document.getElementById('sim-bisection-pane').classList.add('active');
        setTimeout(drawBisection, 50);
      } else {
        event.currentTarget.classList.add('active');
        document.getElementById('sim-newton-pane').classList.add('active');
        setTimeout(drawNewton, 50);
      }
    }

    // Accordion Toggle
    function toggleFaq(el) {
      const parent = el.parentElement;
      parent.classList.toggle('open');
      const arrow = el.querySelector('span');
      if (parent.classList.contains('open')) {
        arrow.textContent = '▲';
      } else {
        arrow.textContent = '▼';
      }
    }

    // Quiz checker
    function checkOption(el, chosenIndex) {
      const card = el.closest('.quiz-card');
      const correctIndex = parseInt(card.dataset.correct);
      const options = card.querySelectorAll('.quiz-option');
      
      options.forEach(opt => {
        opt.onclick = null; // disable further clicks
        opt.style.cursor = 'default';
      });

      if (chosenIndex === correctIndex) {
        el.classList.add('correct');
      } else {
        el.classList.add('wrong');
        options[correctIndex].classList.add('correct');
      }

      const explanation = card.querySelector('.quiz-explanation');
      if (explanation) explanation.style.display = 'block';
    }

    // ==========================================
    // 1. BISECTION SIMULATOR ENGINE
    // ==========================================
    const bisSteps = [
      { i: 0, a: 0.0, b: 0.35, c: 0.175, fa: -0.108, fb: 0.2875, fc: 0.0591 },
      { i: 1, a: 0.0, b: 0.175, c: 0.0875, fa: -0.108, fb: 0.0591, fc: -0.0321 },
      { i: 2, a: 0.0875, b: 0.175, c: 0.13125, fa: -0.0321, fb: 0.0591, fc: 0.0116 },
      { i: 3, a: 0.0875, b: 0.13125, c: 0.109375, fa: -0.0321, fb: 0.0116, fc: -0.0107 },
      { i: 4, a: 0.109375, b: 0.13125, c: 0.1203125, fa: -0.0107, fb: 0.0116, fc: 0.00032 },
      { i: 5, a: 0.109375, b: 0.1203125, c: 0.11484375, fa: -0.0107, fb: 0.00032, fc: -0.0052 },
      { i: 6, a: 0.11484375, b: 0.1203125, c: 0.117578125, fa: -0.0052, fb: 0.00032, fc: -0.0024 },
      { i: 7, a: 0.117578125, b: 0.1203125, c: 0.1189453125, fa: -0.0024, fb: 0.00032, fc: -0.0011 },
      { i: 8, a: 0.1189453125, b: 0.1203125, c: 0.11962890625, fa: -0.0011, fb: 0.00032, fc: -0.00038 },
      { i: 9, a: 0.11962890625, b: 0.1203125, c: 0.119970703125, fa: -0.00038, fb: 0.00032, fc: -0.00003 },
      { i: 10, a: 0.119970703125, b: 0.1203125, c: 0.1201416015625, fa: -0.00003, fb: 0.00032, fc: 0.00014 }
    ];

    let currentBisStep = 0;
    let bisAutoInterval = null;

    function drawBisection() {
      const canvas = document.getElementById('bisectionCanvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const rect = canvas.getBoundingClientRect();
      canvas.width = rect.width * window.devicePixelRatio;
      canvas.height = rect.height * window.devicePixelRatio;
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);

      const w = rect.width;
      const h = rect.height;
      const isDark = document.documentElement.classList.contains('dark');

      ctx.clearRect(0, 0, w, h);

      // Coordinate mapping
      const xMin = -0.05, xMax = 0.40;
      const yMin = -0.15, yMax = 0.35;

      function toScreenX(x) {
        return ((x - xMin) / (xMax - xMin)) * (w - 100) + 60;
      }
      function toScreenY(y) {
        return h - 40 - ((y - yMin) / (yMax - yMin)) * (h - 80);
      }

      // Draw Grid & Axes
      ctx.strokeStyle = isDark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.06)';
      ctx.lineWidth = 1;

      // Axis Ox
      ctx.beginPath();
      ctx.moveTo(0, toScreenY(0));
      ctx.lineTo(w, toScreenY(0));
      ctx.strokeStyle = isDark ? '#4b5563' : '#cbd5e1';
      ctx.lineWidth = 1.5;
      ctx.stroke();

      // Axis Oy
      ctx.beginPath();
      ctx.moveTo(toScreenX(0), 0);
      ctx.lineTo(toScreenX(0), h);
      ctx.stroke();

      // Labels
      ctx.fillStyle = isDark ? '#9ca3af' : '#64748b';
      ctx.font = '11px sans-serif';
      ctx.fillText('0', toScreenX(0) - 12, toScreenY(0) + 15);
      ctx.fillText('0.12 (корінь)', toScreenX(0.12) - 30, toScreenY(0) + 20);
      ctx.fillText('Ox', w - 25, toScreenY(0) - 8);
      ctx.fillText('Oy', toScreenX(0) + 8, 20);

      // Draw Curve f(x)
      ctx.beginPath();
      ctx.strokeStyle = '#3b82f6';
      ctx.lineWidth = 2.5;
      for (let px = 0; px <= w; px += 2) {
        const x = xMin + (px / w) * (xMax - xMin);
        const y = f(x);
        const py = toScreenY(y);
        if (px === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Get current step data
      const step = bisSteps[currentBisStep];
      const ax = toScreenX(step.a);
      const bx = toScreenX(step.b);
      const cx = toScreenX(step.c);
      const y0 = toScreenY(0);

      // Highlight Interval [a, b]
      ctx.fillStyle = isDark ? 'rgba(59, 130, 246, 0.15)' : 'rgba(59, 130, 246, 0.2)';
      ctx.fillRect(ax, 30, bx - ax, h - 70);

      // Draw vertical lines for a, b, c
      function drawBound(xPos, color, label, yVal) {
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(xPos, 30);
        ctx.lineTo(xPos, h - 40);
        ctx.stroke();
        ctx.setLineDash([]);

        // point on curve
        const py = toScreenY(yVal);
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.arc(xPos, py, 5, 0, Math.PI * 2);
        ctx.fill();

        // Label
        ctx.fillStyle = color;
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText(label, xPos - 5, h - 22);
      }

      drawBound(ax, '#ef4444', `a=${step.a.toFixed(3)}`, step.fa);
      drawBound(bx, '#10b981', `b=${step.b.toFixed(3)}`, step.fb);
      drawBound(cx, '#3b82f6', `c=${step.c.toFixed(3)}`, step.fc);

      // Exact root marker
      const rx = toScreenX(0.12);
      ctx.fillStyle = '#f59e0b';
      ctx.beginPath();
      ctx.arc(rx, y0, 6, 0, Math.PI * 2);
      ctx.fill();

      // Update UI stats
      document.getElementById('valA').textContent = step.a.toFixed(6);
      document.getElementById('valB').textContent = step.b.toFixed(6);
      document.getElementById('valC').textContent = step.c.toFixed(6);
      document.getElementById('valWidth').textContent = (step.b - step.a).toFixed(6);
      document.getElementById('bisStatus').textContent = `Крок: ${step.i} / ${bisSteps.length - 1} | Ширина: ${(step.b - step.a).toFixed(6)}`;
    }

    function stepBisection() {
      if (currentBisStep < bisSteps.length - 1) {
        currentBisStep++;
      } else {
        currentBisStep = 0;
      }
      drawBisection();
    }

    function resetBisection() {
      clearInterval(bisAutoInterval);
      bisAutoInterval = null;
      document.getElementById('btnAutoBis').textContent = '⏩ Автоматично';
      currentBisStep = 0;
      drawBisection();
    }

    function autoRunBisection() {
      if (bisAutoInterval) {
        clearInterval(bisAutoInterval);
        bisAutoInterval = null;
        document.getElementById('btnAutoBis').textContent = '⏩ Автоматично';
      } else {
        document.getElementById('btnAutoBis').textContent = '⏸ Пауза';
        bisAutoInterval = setInterval(() => {
          if (currentBisStep < bisSteps.length - 1) {
            currentBisStep++;
            drawBisection();
          } else {
            clearInterval(bisAutoInterval);
            bisAutoInterval = null;
            document.getElementById('btnAutoBis').textContent = '⏩ Автоматично';
          }
        }, 1200);
      }
    }

    // ==========================================
    // 2. NEWTON SIMULATOR ENGINE
    // ==========================================
    const newtSteps = [
      { i: 0, x: 0.0, f: -0.108, df: 0.78, nextX: 0.138461538 },
      { i: 1, x: 0.138461538, f: 0.0191716, df: 1.056923, nextX: 0.120322472 },
      { i: 2, x: 0.120322472, f: 0.0003290, df: 1.020645, nextX: 0.120000102 },
      { i: 3, x: 0.120000102, f: 1.039e-7, df: 1.020000, nextX: 0.120000000 },
      { i: 4, x: 0.120000000, f: 1.038e-14, df: 1.020000, nextX: 0.120000000 }
    ];

    let currentNewtStep = 0;
    let newtAutoInterval = null;

    function drawNewton() {
      const canvas = document.getElementById('newtonCanvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const rect = canvas.getBoundingClientRect();
      canvas.width = rect.width * window.devicePixelRatio;
      canvas.height = rect.height * window.devicePixelRatio;
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);

      const w = rect.width;
      const h = rect.height;
      const isDark = document.documentElement.classList.contains('dark');

      ctx.clearRect(0, 0, w, h);

      // Coordinate mapping
      const xMin = -0.05, xMax = 0.25;
      const yMin = -0.15, yMax = 0.15;

      function toScreenX(x) {
        return ((x - xMin) / (xMax - xMin)) * (w - 100) + 60;
      }
      function toScreenY(y) {
        return h - 40 - ((y - yMin) / (yMax - yMin)) * (h - 80);
      }

      // Axis Ox & Oy
      ctx.beginPath();
      ctx.moveTo(0, toScreenY(0));
      ctx.lineTo(w, toScreenY(0));
      ctx.strokeStyle = isDark ? '#4b5563' : '#cbd5e1';
      ctx.lineWidth = 1.5;
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(toScreenX(0), 0);
      ctx.lineTo(toScreenX(0), h);
      ctx.stroke();

      // Labels
      ctx.fillStyle = isDark ? '#9ca3af' : '#64748b';
      ctx.font = '11px sans-serif';
      ctx.fillText('0', toScreenX(0) - 12, toScreenY(0) + 15);
      ctx.fillText('x*=0.12', toScreenX(0.12) - 20, toScreenY(0) + 20);

      // Curve f(x)
      ctx.beginPath();
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 2.5;
      for (let px = 0; px <= w; px += 2) {
        const x = xMin + (px / w) * (xMax - xMin);
        const y = f(x);
        const py = toScreenY(y);
        if (px === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current step
      const step = newtSteps[currentNewtStep];
      const curX = step.x;
      const curY = step.f;
      const slope = step.df;
      const nextX = step.nextX;

      const sx = toScreenX(curX);
      const sy = toScreenY(curY);
      const sNextX = toScreenX(nextX);
      const y0 = toScreenY(0);

      // Tangent line: y - curY = slope * (x - curX)
      // Pass through (curX, curY) and (nextX, 0)
      ctx.beginPath();
      ctx.strokeStyle = '#ef4444';
      ctx.lineWidth = 2;
      const tangX1 = curX - 0.08;
      const tangY1 = curY + slope * (tangX1 - curX);
      const tangX2 = nextX + 0.05;
      const tangY2 = slope * (tangX2 - nextX);

      ctx.moveTo(toScreenX(tangX1), toScreenY(tangY1));
      ctx.lineTo(toScreenX(tangX2), toScreenY(tangY2));
      ctx.stroke();

      // Vertical drop line to curve
      ctx.strokeStyle = '#8b5cf6';
      ctx.lineWidth = 1.5;
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(sx, y0);
      ctx.lineTo(sx, sy);
      ctx.stroke();
      ctx.setLineDash([]);

      // Point on Curve
      ctx.fillStyle = '#ef4444';
      ctx.beginPath();
      ctx.arc(sx, sy, 6, 0, Math.PI * 2);
      ctx.fill();

      // New calculated root point on axis
      ctx.fillStyle = '#3b82f6';
      ctx.beginPath();
      ctx.arc(sNextX, y0, 6, 0, Math.PI * 2);
      ctx.fill();

      // Text labels on canvas
      ctx.font = 'bold 12px sans-serif';
      ctx.fillStyle = '#ef4444';
      ctx.fillText(`(x${step.i}, f(x${step.i}))`, sx + 8, sy - 8);

      ctx.fillStyle = '#3b82f6';
      ctx.fillText(`x${step.i+1}`, sNextX - 10, y0 + 18);

      // Update UI stats
      document.getElementById('valNewtX').textContent = step.x.toFixed(6);
      document.getElementById('valNewtF').textContent = step.f.toFixed(8);
      document.getElementById('valNewtDF').textContent = step.df.toFixed(6);
      document.getElementById('valNewtNext').textContent = step.nextX.toFixed(8);
      document.getElementById('newtStatus').textContent = `Крок: ${step.i} / ${newtSteps.length - 1} | x_${step.i} = ${step.x.toFixed(6)}`;
    }

    function stepNewton() {
      if (currentNewtStep < newtSteps.length - 1) {
        currentNewtStep++;
      } else {
        currentNewtStep = 0;
      }
      drawNewton();
    }

    function resetNewton() {
      clearInterval(newtAutoInterval);
      newtAutoInterval = null;
      document.getElementById('btnAutoNewt').textContent = '⏩ Автоматично';
      currentNewtStep = 0;
      drawNewton();
    }

    function autoRunNewton() {
      if (newtAutoInterval) {
        clearInterval(newtAutoInterval);
        newtAutoInterval = null;
        document.getElementById('btnAutoNewt').textContent = '⏩ Автоматично';
      } else {
        document.getElementById('btnAutoNewt').textContent = '⏸ Пауза';
        newtAutoInterval = setInterval(() => {
          if (currentNewtStep < newtSteps.length - 1) {
            currentNewtStep++;
            drawNewton();
          } else {
            clearInterval(newtAutoInterval);
            newtAutoInterval = null;
            document.getElementById('btnAutoNewt').textContent = '⏩ Автоматично';
          }
        }, 1500);
      }
    }

    // Initial trigger
    window.addEventListener('resize', () => {
      drawBisection();
      drawNewton();
    });
    window.addEventListener('DOMContentLoaded', () => {
      drawBisection();
    });
  </script>
</body>
</html>
'''

with open('Lab5/site/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Saved Lab5/site/index.html, length:", len(html_content))
