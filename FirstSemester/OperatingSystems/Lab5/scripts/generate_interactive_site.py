# -*- coding: utf-8 -*-
import os

TARGET_DIR = r"D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\Explenation material"
os.makedirs(TARGET_DIR, exist_ok=True)
html_file = os.path.join(TARGET_DIR, "index.html")

# We build the HTML file with complete CSS, HTML and JS
html_content = """<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Інтерактивна теорія та архітектура: Лабораторна робота №5 | Windows Server, AD DS, DNS, DHCP, GPO</title>
  <style>
    :root {
      --bg-primary: #0b1120;
      --bg-secondary: #111827;
      --bg-tertiary: #1e293b;
      --bg-card: rgba(30, 41, 59, 0.7);
      --border-color: #334155;
      --text-primary: #f8fafc;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      --accent-blue: #0284c7;
      --accent-cyan: #38bdf8;
      --accent-green: #10b981;
      --accent-purple: #8b5cf6;
      --accent-amber: #f59e0b;
      --accent-red: #ef4444;
      --shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4), 0 8px 10px -6px rgba(0, 0, 0, 0.3);
      --font: 'Segoe UI', system-ui, -apple-system, sans-serif;
      --code-font: 'Cascadia Code', 'Consolas', 'Courier New', monospace;
    }

    [data-theme="light"] {
      --bg-primary: #f8fafc;
      --bg-secondary: #ffffff;
      --bg-tertiary: #f1f5f9;
      --bg-card: rgba(255, 255, 255, 0.9);
      --border-color: #e2e8f0;
      --text-primary: #0f172a;
      --text-secondary: #475569;
      --text-muted: #94a3b8;
      --shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: var(--font);
      background-color: var(--bg-primary);
      color: var(--text-primary);
      line-height: 1.6;
      overflow-x: hidden;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    /* Header */
    header {
      background: var(--bg-secondary);
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(12px);
    }
    .header-container {
      max-width: 1440px;
      margin: 0 auto;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }
    .brand-group {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .logo-badge {
      background: linear-gradient(135deg, var(--accent-blue), var(--accent-cyan));
      color: white;
      font-weight: 800;
      font-size: 14px;
      padding: 8px 12px;
      border-radius: 8px;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .brand-titles h1 {
      font-size: 16px;
      font-weight: 700;
      color: var(--text-primary);
      line-height: 1.2;
    }
    .brand-titles p {
      font-size: 12px;
      color: var(--text-secondary);
    }
    .header-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .search-box {
      position: relative;
      display: flex;
      align-items: center;
    }
    .search-input {
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      border-radius: 20px;
      padding: 8px 16px 8px 36px;
      color: var(--text-primary);
      font-size: 13px;
      outline: none;
      width: 240px;
      transition: all 0.25s ease;
    }
    .search-input:focus {
      width: 320px;
      border-color: var(--accent-cyan);
      box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2);
    }
    .search-icon {
      position: absolute;
      left: 12px;
      font-size: 14px;
      color: var(--text-muted);
    }
    .theme-toggle-btn {
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      color: var(--text-primary);
      padding: 8px 12px;
      border-radius: 20px;
      cursor: pointer;
      font-size: 13px;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }
    .theme-toggle-btn:hover {
      background: var(--border-color);
    }

    /* Main Container */
    .app-layout {
      max-width: 1440px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 280px 1fr;
      min-height: calc(100vh - 65px);
    }

    /* Sidebar Navigation */
    .sidebar {
      background: var(--bg-secondary);
      border-right: 1px solid var(--border-color);
      padding: 24px 16px;
      position: sticky;
      top: 65px;
      height: calc(100vh - 65px);
      overflow-y: auto;
    }
    .nav-section-title {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--text-muted);
      font-weight: 700;
      margin: 16px 8px 8px;
    }
    .nav-btn {
      display: flex;
      align-items: center;
      gap: 12px;
      width: 100%;
      text-align: left;
      padding: 10px 14px;
      background: transparent;
      border: none;
      color: var(--text-secondary);
      border-radius: 8px;
      font-size: 13.5px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s ease;
      margin-bottom: 3px;
    }
    .nav-btn:hover {
      background: var(--bg-tertiary);
      color: var(--text-primary);
    }
    .nav-btn.active {
      background: linear-gradient(90deg, rgba(2, 132, 199, 0.15), rgba(56, 189, 248, 0.05));
      color: var(--accent-cyan);
      font-weight: 600;
      border-left: 3px solid var(--accent-cyan);
    }
    .nav-icon {
      font-size: 16px;
    }

    /* Main Content Area */
    main {
      padding: 32px 40px;
      max-width: 1120px;
    }

    /* Hero Banner */
    .hero-banner {
      background: linear-gradient(135deg, rgba(2, 132, 199, 0.2), rgba(139, 92, 246, 0.15));
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 16px;
      padding: 28px 32px;
      margin-bottom: 32px;
      position: relative;
      overflow: hidden;
    }
    .hero-banner h2 {
      font-size: 26px;
      font-weight: 800;
      color: var(--text-primary);
      margin-bottom: 8px;
    }
    .hero-banner p {
      color: var(--text-secondary);
      font-size: 14.5px;
      max-width: 820px;
      margin-bottom: 16px;
    }
    .hero-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    .hero-tag {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--accent-cyan);
      font-size: 12px;
      font-weight: 600;
      padding: 4px 10px;
      border-radius: 6px;
    }

    /* Tab Modules */
    .tab-module {
      display: none;
    }
    .tab-module.active {
      display: block;
      animation: fadeIn 0.3s ease;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Section Styles */
    .section-header {
      margin-bottom: 24px;
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 12px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }
    .section-title {
      font-size: 22px;
      font-weight: 800;
      color: var(--text-primary);
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .section-badge {
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      color: var(--accent-cyan);
      font-size: 12px;
      padding: 3px 8px;
      border-radius: 4px;
      font-weight: 600;
    }

    /* Cards & Grids */
    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 24px;
    }
    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin-bottom: 24px;
    }
    .card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 20px;
      box-shadow: var(--shadow);
      transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .card:hover {
      border-color: var(--accent-blue);
      transform: translateY(-2px);
    }
    .card-title {
      font-size: 16px;
      font-weight: 700;
      margin-bottom: 10px;
      color: var(--text-primary);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .card-title span.icon {
      font-size: 18px;
    }
    .card p {
      font-size: 13.5px;
      color: var(--text-secondary);
      margin-bottom: 12px;
    }

    /* Architectural Deep-Dives / Callouts */
    .callout {
      background: linear-gradient(90deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.9));
      border-left: 4px solid var(--accent-cyan);
      border-radius: 0 10px 10px 0;
      padding: 16px 20px;
      margin: 20px 0;
    }
    .callout-title {
      font-weight: 700;
      color: var(--accent-cyan);
      font-size: 14px;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .callout p {
      font-size: 13px;
      color: var(--text-secondary);
    }

    /* Tables */
    .table-container {
      overflow-x: auto;
      margin: 20px 0 28px;
      border: 1px solid var(--border-color);
      border-radius: 10px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13.5px;
      text-align: left;
    }
    th {
      background: var(--bg-secondary);
      color: var(--accent-cyan);
      font-weight: 700;
      padding: 12px 16px;
      border-bottom: 1px solid var(--border-color);
    }
    td {
      padding: 12px 16px;
      border-bottom: 1px solid var(--border-color);
      color: var(--text-secondary);
    }
    tr:last-child td { border-bottom: none; }
    tr:hover td { background: var(--bg-tertiary); }
    td strong { color: var(--text-primary); }

    /* Code & Terminology Badges */
    code {
      font-family: var(--code-font);
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      color: var(--accent-cyan);
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 12.5px;
    }
    pre {
      background: #060913;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 14px 18px;
      overflow-x: auto;
      font-family: var(--code-font);
      font-size: 12.5px;
      color: #38bdf8;
      margin: 12px 0 18px;
    }

    /* Interactive Simulators Styles */
    .simulator-container {
      background: var(--bg-secondary);
      border: 1px solid var(--accent-blue);
      border-radius: 14px;
      padding: 24px;
      margin: 28px 0;
      box-shadow: 0 0 20px rgba(2, 132, 199, 0.15);
    }
    .simulator-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 18px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 12px;
    }
    .simulator-title {
      font-size: 17px;
      font-weight: 800;
      color: var(--accent-cyan);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .simulator-badge {
      background: rgba(56, 189, 248, 0.15);
      color: var(--accent-cyan);
      border: 1px solid var(--accent-cyan);
      padding: 3px 10px;
      border-radius: 12px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
    }

    /* Sim 1: AD Tree */
    .ad-tree {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .tree-node {
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 12px 16px;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: all 0.2s ease;
    }
    .tree-node:hover {
      background: var(--border-color);
      border-color: var(--accent-cyan);
    }
    .tree-node.selected {
      border-color: var(--accent-cyan);
      background: rgba(2, 132, 199, 0.2);
    }
    .tree-indent-1 { margin-left: 28px; }
    .tree-indent-2 { margin-left: 56px; }
    .tree-node-name {
      font-weight: 600;
      font-size: 13.5px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .node-details-box {
      background: #060913;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 16px;
      margin-top: 16px;
      font-size: 13px;
      color: var(--text-secondary);
    }

    /* Sim 2: Kerberos Flow */
    .kerberos-flow-box {
      display: grid;
      grid-template-columns: 1fr;
      gap: 12px;
    }
    .kerberos-step-btn {
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 12px 16px;
      color: var(--text-primary);
      text-align: left;
      cursor: pointer;
      font-size: 13px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: all 0.2s ease;
    }
    .kerberos-step-btn:hover {
      border-color: var(--accent-purple);
    }
    .kerberos-step-btn.active {
      background: rgba(139, 92, 246, 0.2);
      border-color: var(--accent-purple);
      color: #c084fc;
      font-weight: 600;
    }
    .kerberos-display {
      background: #060913;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 16px;
      font-size: 13px;
      min-height: 120px;
    }

    /* Sim 5: Permissions Calculator */
    .perm-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 16px;
    }
    .perm-select-group label {
      display: block;
      font-size: 12.5px;
      color: var(--text-secondary);
      font-weight: 600;
      margin-bottom: 6px;
    }
    .perm-select {
      width: 100%;
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      color: var(--text-primary);
      padding: 10px;
      border-radius: 6px;
      font-size: 13px;
      outline: none;
    }
    .perm-result-box {
      background: #060913;
      border: 2px solid var(--accent-cyan);
      border-radius: 8px;
      padding: 16px;
      text-align: center;
    }
    .perm-result-text {
      font-size: 18px;
      font-weight: 800;
      color: var(--accent-green);
      margin-top: 4px;
    }

    /* Quiz Component */
    .quiz-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 20px;
      margin-bottom: 20px;
    }
    .quiz-question {
      font-size: 15px;
      font-weight: 700;
      color: var(--text-primary);
      margin-bottom: 14px;
    }
    .quiz-options {
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-bottom: 12px;
    }
    .quiz-option-btn {
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 10px 14px;
      color: var(--text-secondary);
      text-align: left;
      font-size: 13px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .quiz-option-btn:hover {
      background: var(--border-color);
      color: var(--text-primary);
    }
    .quiz-option-btn.correct {
      background: rgba(16, 185, 129, 0.2);
      border-color: var(--accent-green);
      color: var(--accent-green);
      font-weight: 700;
    }
    .quiz-option-btn.wrong {
      background: rgba(239, 68, 68, 0.2);
      border-color: var(--accent-red);
      color: var(--accent-red);
      font-weight: 700;
    }
    .quiz-feedback {
      display: none;
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 12px 14px;
      font-size: 12.5px;
      color: var(--text-secondary);
      margin-top: 10px;
    }

    /* Glossary Filter */
    .glossary-filter-bar {
      display: flex;
      gap: 8px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }
    .filter-btn {
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .filter-btn.active, .filter-btn:hover {
      background: var(--accent-blue);
      color: white;
      border-color: var(--accent-blue);
    }
    .glossary-item {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 16px;
      margin-bottom: 12px;
      transition: transform 0.2s ease;
    }
    .glossary-item:hover {
      transform: translateX(4px);
      border-color: var(--accent-cyan);
    }
    .glossary-term {
      font-size: 15px;
      font-weight: 700;
      color: var(--accent-cyan);
      margin-bottom: 4px;
    }
    .glossary-desc {
      font-size: 13px;
      color: var(--text-secondary);
    }

    /* Footer */
    footer {
      border-top: 1px solid var(--border-color);
      padding: 24px;
      text-align: center;
      font-size: 12.5px;
      color: var(--text-muted);
      background: var(--bg-secondary);
    }

    /* Responsive */
    @media (max-width: 900px) {
      .app-layout { grid-template-columns: 1fr; }
      .sidebar { display: none; }
      main { padding: 20px; }
      .grid-2, .grid-3 { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <!-- Top App Header -->
  <header>
    <div class="header-container">
      <div class="brand-group">
        <div class="logo-badge">🏛️ САПР</div>
        <div class="brand-titles">
          <h1>Active Directory & Windows Server Theory Hub</h1>
          <p>Лабораторна робота №5 • Андрій ЛЕМІШКА (ПП-14) • Викладач: Н. Нестор</p>
        </div>
      </div>
      <div class="header-actions">
        <div class="search-box">
          <span class="search-icon">🔍</span>
          <input type="text" id="globalSearch" class="search-input" placeholder="Пошук термінів (Kerberos, FSMO, GPO)...">
        </div>
        <button id="themeToggle" class="theme-toggle-btn" title="Змінити тему оформлення">
          <span id="themeIcon">🌙</span> <span id="themeText">Темна</span>
        </button>
      </div>
    </div>
  </header>

  <div class="app-layout">
    <!-- Sidebar Navigation -->
    <aside class="sidebar">
      <div class="nav-section-title">Тематичні модулі</div>
      <button class="nav-btn active" data-tab="tab-intro"><span class="nav-icon">🏛️</span> Вступ: SAM vs AD DS</button>
      <button class="nav-btn" data-tab="tab-database"><span class="nav-icon">💾</span> База NTDS.dit & ESE</button>
      <button class="nav-btn" data-tab="tab-architecture"><span class="nav-icon">🌲</span> Логічна & Фізична AD</button>
      <button class="nav-btn" data-tab="tab-fsmo"><span class="nav-icon">👑</span> Ролі FSMO (Хазяї)</button>
      <button class="nav-btn" data-tab="tab-security"><span class="nav-icon">🔐</span> Kerberos v5 & LDAP</button>
      <button class="nav-btn" data-tab="tab-dns"><span class="nav-icon">🌐</span> Інтеграція DNS & SRV</button>
      <button class="nav-btn" data-tab="tab-dhcp"><span class="nav-icon">📡</span> DHCP, DORA & Опції</button>
      <button class="nav-btn" data-tab="tab-gpo"><span class="nav-icon">⚙️</span> Групові політики (LSDOU)</button>
      <button class="nav-btn" data-tab="tab-storage"><span class="nav-icon">📁</span> SMB vs NTFS & Профілі</button>
      <button class="nav-btn" data-tab="tab-client"><span class="nav-icon">💻</span> Клієнт Windows 10 & RunAs</button>

      <div class="nav-section-title">Практикум & Контроль</div>
      <button class="nav-btn" data-tab="tab-quiz"><span class="nav-icon">🎓</span> Тренажер захисту (Quiz)</button>
      <button class="nav-btn" data-tab="tab-glossary"><span class="nav-icon">📚</span> Словник термінів</button>
    </aside>

    <!-- Main Content Area -->
    <main>

      <!-- Banner -->
      <section class="hero-banner">
        <h2>Інтерактивний теоретичний довідник та дослідження архітектури</h2>
        <p>Комплексне академічне дослідження: що, як і чому працює під капотом контролера домену Microsoft Windows Server, бази даних NTDS.dit, служб DNS, DHCP, механізмів криптографічної автентифікації Kerberos v5 та групових політик GPO.</p>
        <div class="hero-tags">
          <span class="hero-tag">Windows Server 2008 R2</span>
          <span class="hero-tag">Active Directory</span>
          <span class="hero-tag">Kerberos v5</span>
          <span class="hero-tag">RFC 4120 / RFC 2131</span>
          <span class="hero-tag">NTFS vs SMB</span>
          <span class="hero-tag">Windows 10 Client</span>
        </div>
      </section>

      <!-- MODULE 1: Intro -->
      <section id="tab-intro" class="tab-module active">
        <div class="section-header">
          <div class="section-title">🏛️ 1. Вступ: Еволюція мережевих моделей та SAM проти AD DS</div>
          <span class="section-badge">Фундамент</span>
        </div>

        <div class="grid-2">
          <div class="card">
            <div class="card-title"><span class="icon">💻</span> Робоча група (Workgroup) та SAM</div>
            <p>У робочій групі кожен комп'ютер автономний і використовує власну локальну базу <code>SAM</code> (Security Accounts Manager) у реєстрі <code>%SystemRoot%\\System32\\Config\\SAM</code>.</p>
            <p><strong>Проблема масштабування ($O(N \\times M)$):</strong> Якщо в мережі 50 комп'ютерів і 50 співробітників, адміністратор змушений створити 2500 облікових записів вручну. Зміна пароля вимагає його ручного оновлення на кожному ПК окремо.</p>
          </div>
          <div class="card">
            <div class="card-title"><span class="icon">🌐</span> Доменна мережа (Domain) та AD DS</div>
            <p>У домені база облікових записів централізована у файлі <code>ntds.dit</code> на контролерах домену (Domain Controllers). Користувач автентифікується один раз через Kerberos v5.</p>
            <p><strong>Перевага масштабування ($O(M)$):</strong> Обліковий запис створюється 1 раз у домені та діє на всіх комп'ютерах. Адміністратор централізовано призначає права, поширює політики та проводить єдиний аудит.</p>
          </div>
        </div>

        <div class="callout">
          <div class="callout-title">💡 Чому застаріли доменні моделі Windows NT 4.0?</div>
          <p>У Windows NT 4.0 існували моделі: Single Domain, Master Domain, Multiple Master та Complete Trust. Модель Complete Trust вимагала встановлення зв'язків довіри за формулою $T = n(n - 1)$. Для 10 доменів це 90 зв'язків вручну! Active Directory розв'язала це завдяки <strong>двостороннім транзитивним довірчим відносинам</strong>: якщо Домен A довіряє Домену B, а B довіряє C, то A автоматично довіряє C.</p>
        </div>

        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th>Характеристика</th>
                <th>Робоча група (Workgroup / SAM)</th>
                <th>Доменна служба (Active Directory Domain Services)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>База даних</strong></td>
                <td>Децентралізована локальна SAM на кожному ПК</td>
                <td>Єдина централізована реплікована база <code>NTDS.dit</code></td>
              </tr>
              <tr>
                <td><strong>Протокол автентифікації</strong></td>
                <td>Застарілий NTLMv2 (Challenge-Response)</td>
                <td>Промисловий <strong>Kerberos v5</strong> з взаємною автентифікацією</td>
              </tr>
              <tr>
                <td><strong>Масштабованість</strong></td>
                <td>Ефективно до 10–15 машин</td>
                <td>Мільйони об'єктів у лісі (масштабованість підприємства)</td>
              </tr>
              <tr>
                <td><strong>Керування конфігурацією</strong></td>
                <td>Тільки локальні політики (gpedit.msc) на кожній машині</td>
                <td>Централізовані групові політики (GPMC / GPO) за моделлю LSDOU</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- MODULE 2: Database -->
      <section id="tab-database" class="tab-module">
        <div class="section-header">
          <div class="section-title">💾 2. Анатомія бази даних Active Directory (NTDS.dit & ESE)</div>
          <span class="section-badge">Внутрішній рушій</span>
        </div>

        <p>Служба Active Directory базується на високонадійному транзакційному рушії <strong>Extensible Storage Engine (ESE)</strong>, також відомому як <strong>JET Blue</strong>. Файл бази зберігається за шляхом <code>C:\\Windows\\NTDS\\ntds.dit</code>.</p>

        <!-- Simulator 6: ESE Inspector -->
        <div class="simulator-container">
          <div class="simulator-header">
            <div class="simulator-title">🔬 Інтерактивний інспектор структури NTDS.dit та журналу WAL</div>
            <span class="simulator-badge">Симулятор СУБД</span>
          </div>
          <div class="grid-3">
            <div class="card" onclick="inspectTable('datatable')">
              <div class="card-title">📊 datatable</div>
              <p>Основна таблиця об'єктів. Кожен рядок — це об'єкт (User, Group, Computer, OU), стовпці — атрибути схеми.</p>
              <code>Клацніть для аналізу</code>
            </div>
            <div class="card" onclick="inspectTable('link_table')">
              <div class="card-title">🔗 link_table</div>
              <p>Таблиця двосторонніх зв'язків. Зберігає зв'язки типу «користувач $\\leftrightarrow$ членство в групі» (memberOf).</p>
              <code>Клацніть для аналізу</code>
            </div>
            <div class="card" onclick="inspectTable('sd_table')">
              <div class="card-title">🛡️ sd_table</div>
              <p>Таблиця дескрипторів безпеки (Single-Instance Store ACL) для оптимізації розміру бази даних.</p>
              <code>Клацніть для аналізу</code>
            </div>
          </div>
          <div id="tableInspectorDetails" class="node-details-box">
            Оберіть таблицю вище, щоб переглянути механіку її збереження та індексації в рушії ESE.
          </div>
        </div>

        <div class="callout">
          <div class="callout-title">⚡ Технологія Write-Ahead Logging (WAL) та відмовостійкість</div>
          <p>Рушій ESE ніколи не записує зміни безпосередньо у важкий файл <code>ntds.dit</code> на диск. Спочатку транзакція послідовно записується у файл журналу <code>edb.log</code> (10 МБ). Файл <code>edb.chk</code> фіксує контрольні точки (чекпоінти). При аварійному вимкненні живлення сервера рушій ESE автоматично проводить процедуру <strong>Roll-Forward</strong>: зчитує незафіксовані транзакції з журналу та накачує їх у базу, запобігаючи пошкодженню файлової структури.</p>
        </div>
      </section>

      <!-- MODULE 3: Architecture -->
      <section id="tab-architecture" class="tab-module">
        <div class="section-header">
          <div class="section-title">🌲 3. Логічна та фізична архітектура Active Directory</div>
          <span class="section-badge">Структурна теорія</span>
        </div>

        <!-- Simulator 1: Tree visualizer -->
        <div class="simulator-container">
          <div class="simulator-header">
            <div class="simulator-title">🌳 Інтерактивний навігатор ієрархії домену office.com</div>
            <span class="simulator-badge">Дослідження об'єктів</span>
          </div>
          <div class="ad-tree">
            <div class="tree-node selected" onclick="showNodeDetails('forest')">
              <div class="tree-node-name">🌲 Ліс: office.com (Межа безпеки Enterprise Security Boundary)</div>
              <span>Ліс</span>
            </div>
            <div class="tree-node tree-indent-1" onclick="showNodeDetails('domain')">
              <div class="tree-node-name">🌐 Домен: office.com (Адміністративна межа безпеки)</div>
              <span>Домен</span>
            </div>
            <div class="tree-node tree-indent-2" onclick="showNodeDetails('ou_fin')">
              <div class="tree-node-name">📁 OU: Фінансисти (Прив'язано GPO: Фінансова політика безпеки)</div>
              <span>OU</span>
            </div>
            <div class="tree-node tree-indent-2" onclick="showNodeDetails('ou_it')">
              <div class="tree-node-name">📁 OU: IT-спеціалісти (Користувач: Програміст, диск P:)</div>
              <span>OU</span>
            </div>
            <div class="tree-node tree-indent-2" onclick="showNodeDetails('ou_groups')">
              <div class="tree-node-name">👥 OU: Групи (Глобальні групи безпеки: Фінансисти, IT-відділ)</div>
              <span>OU</span>
            </div>
          </div>

          <div id="adNodeInfo" class="node-details-box">
            <strong>Оберіть вузол вище</strong>, щоб побачити його технічні атрибути, призначення та архітектурне обґрунтування.
          </div>
        </div>

        <div class="grid-2">
          <div class="card">
            <div class="card-title">Логічна структура</div>
            <p><strong>Об'єкти та Атрибути:</strong> Елементи каталогу (користувач, ПК, група).</p>
            <p><strong>Схема (Schema):</strong> Загальний для всього лісу набір правил, що визначає класи та їхні атрибути. Схема модифікується тільки на одному сервері — <em>Schema Master</em>.</p>
            <p><strong>OU (Organizational Unit):</strong> Підрозділ для групування об'єктів з метою делегування прав та прив'язки групових політик GPO.</p>
          </div>
          <div class="card">
            <div class="card-title">Фізична структура</div>
            <p><strong>Контролер домену (DC):</strong> Фізичний або віртуальний сервер, що зберігає репліку бази NTDS.</p>
            <p><strong>Сайти (Sites) та Підмережі (Subnets):</strong> Сайти об'єднують високошвидкісні підмережі LAN для оптимізації автентифікації та розкладу реплікації.</p>
            <p><strong>Глобальний каталог (Global Catalog, GC):</strong> Зберігає повні дані свого домену та частковий набір атрибутів (PAS) усіх об'єктів лісу (порт 3268).</p>
          </div>
        </div>
      </section>

      <!-- MODULE 4: FSMO -->
      <section id="tab-fsmo" class="tab-module">
        <div class="section-header">
          <div class="section-title">👑 4. Ролі операцій з одним хазяїном (FSMO / Flexible Single Master Operations)</div>
          <span class="section-badge">Master-сервери</span>
        </div>

        <p>Хоча Active Directory є мультимайстерною системою, існують 5 критичних завдань, одночасне виконання яких у різних точках призвело б до незворотних конфліктів. Вони розподілені між 5 ролями FSMO.</p>

        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th>Рівень дії</th>
                <th>Роль FSMO</th>
                <th>Призначення та що робить</th>
                <th>Що буде при відмові сервера?</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Рівень лісу</strong></td>
                <td><strong>Schema Master</strong></td>
                <td>Контролює будь-які зміни до схеми Active Directory (додавання атрибутів, встановлення Exchange).</td>
                <td>Неможливо змінити схему лісу; звичайна робота користувачів не порушується.</td>
              </tr>
              <tr>
                <td><strong>Рівень лісу</strong></td>
                <td><strong>Domain Naming Master</strong></td>
                <td>Керує створенням та видаленням доменів і просторів імен додатків у лісі.</td>
                <td>Неможливо створити або розформувати домен у лісі.</td>
              </tr>
              <tr>
                <td><strong>Рівень домену</strong></td>
                <td><strong>PDC Emulator</strong></td>
                <td>1) Синхронізація часу NTP у домені;<br>2) Терміновий канал перевірки змінених паролів;<br>3) Обслуговування клієнтів застарілих версій;<br>4) Головний сервер для редагування GPO.</td>
                <td><strong>Критично:</strong> Розсинхронізація часу ($>5$ хв блокує Kerberos), помилки автентифікації при свіжій зміні пароля.</td>
              </tr>
              <tr>
                <td><strong>Рівень домену</strong></td>
                <td><strong>RID Master</strong></td>
                <td>Видає пули відносних ідентифікаторів (RID) по 500 штук для кожного DC, з яких формуються унікальні SID.</td>
                <td>Коли на DC закінчиться виділений блок із 500 RID, неможливо буде створити нових користувачів чи комп'ютери.</td>
              </tr>
              <tr>
                <td><strong>Рівень домену</strong></td>
                <td><strong>Infrastructure Master</strong></td>
                <td>Оновлює міждоменні посилання (коли користувач одного домену входить у групу іншого домену).</td>
                <td>Тимчасово не відображатимуться перейменовані міждоменні облікові записи в групах.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- MODULE 5: Security & Kerberos -->
      <section id="tab-security" class="tab-module">
        <div class="section-header">
          <div class="section-title">🔐 5. Протоколи доступу та автентифікації: LDAP та Kerberos v5</div>
          <span class="section-badge">Криптографія та мережа</span>
        </div>

        <p>У домені Windows Server замість застарілого протоколу NTLM основним механізмом автентифікації є <strong>Kerberos v5 (RFC 4120)</strong>. Пароль користувача **ніколи не передається мережею** навіть у вигляді хешу.</p>

        <!-- Simulator 2: Kerberos Flow -->
        <div class="simulator-container">
          <div class="simulator-header">
            <div class="simulator-title">🎟️ Симулятор покрокового життєвого циклу квитків Kerberos v5</div>
            <span class="simulator-badge">Анімація протоколу</span>
          </div>
          <div class="kerberos-flow-box">
            <button class="kerberos-step-btn active" onclick="showKerbStep(1)">
              <span>Крок 1: Запит AS-REQ (Authentication Service Request)</span>
              <code>Порт 88 UDP/TCP</code>
            </button>
            <button class="kerberos-step-btn" onclick="showKerbStep(2)">
              <span>Крок 2: Відповідь AS-REP (Отримання квитка TGT)</span>
              <code>Шифрування krbtgt</code>
            </button>
            <button class="kerberos-step-btn" onclick="showKerbStep(3)">
              <span>Крок 3: Запит TGS-REQ (Ticket Granting Service Request)</span>
              <code>Запит квитка на сервіс SMB</code>
            </button>
            <button class="kerberos-step-btn" onclick="showKerbStep(4)">
              <span>Крок 4: Відповідь TGS-REP (Отримання Service Ticket)</span>
              <code>Шифрування ключем сервера</code>
            </button>
            <button class="kerberos-step-btn" onclick="showKerbStep(5)">
              <span>Крок 5: Запит AP-REQ до файлового сервера SMB (\\\\server\\Офіс)</span>
              <code>Взаємна автентифікація</code>
            </button>
          </div>
          <div id="kerbDetails" class="kerberos-display" style="margin-top: 14px;">
            <strong>Крок 1: AS-REQ.</strong> Клієнт Windows 10 бажає увійти під акаунтом <code>office\\programmer</code>. Клієнт формує часову мітку (Timestamp), шифрує її симетричним ключем, похідним від введеного пароля користувача, і відправляє на KDC (контролер домену 192.168.1.5:88).
          </div>
        </div>

        <div class="callout">
          <div class="callout-title">🛡️ Чому Kerberos вимагає синхронізації системного часу (Clock Skew)?</div>
          <p>Щоб запобігти атакам повторного відтворення (<strong>Replay Attacks</strong>), коли перехоплений зловмисником автентифікаційний пакет надсилається повторно, кожен пакет Kerberos містить сувору часову мітку. Якщо різниця в часі між клієнтом і сервером перевищує <strong>5 хвилин</strong> (за замовчуванням), KDC відхиляє пакет з помилкою <code>KRB_AP_ERR_SKEW</code>. Синхронізацію часу забезпечує PDC Emulator за протоколом NTP.</p>
        </div>
      </section>

      <!-- MODULE 6: DNS -->
      <section id="tab-dns" class="tab-module">
        <div class="section-header">
          <div class="section-title">🌐 6. Глибока інтеграція служби DNS та Active Directory</div>
          <span class="section-badge">Розпізнавання імен</span>
        </div>

        <p>Active Directory не може функціонувати без DNS. У лабораторній роботі використовується домен <code>office.com</code>.</p>

        <div class="grid-2">
          <div class="card">
            <div class="card-title">Службові записи SRV (RFC 2782)</div>
            <p>Як комп'ютер Windows 10 дізнається, хто в мережі є контролером домену? Клієнт звертається до DNS із запитом на спеціальні SRV-записи:</p>
            <p><code>_ldap._tcp.dc._msdcs.office.com</code> $\\rightarrow$ вказує на порт 389 контролера <code>192.168.1.5</code>.</p>
            <p><code>_kerberos._tcp.dc._msdcs.office.com</code> $\\rightarrow$ вказує на порт 88 KDC сервера.</p>
          </div>
          <div class="card">
            <div class="card-title">Зони, інтегровані в AD (AD-Integrated)</div>
            <p>Замість зберігання зони у вразливому текстовому файлі, зона розміщується безпосередньо як об'єкт усередині бази <code>ntds.dit</code>.</p>
            <p><strong>Безпечне динамічне оновлення (Secure Dynamic Updates):</strong> Записи в зоні можуть створювати та оновлювати лише автентифіковані члени домену. Зловмисник не може підмінити IP-адресу сервера.</p>
          </div>
        </div>

        <div class="callout">
          <div class="callout-title">🔍 Ієрархія пошуку мережевих імен у Windows:</div>
          <p>1) Локальний кеш та файл <code>hosts</code> $\\rightarrow$ 2) Запит до DNS-сервера $\\rightarrow$ 3) Локальний кеш NetBIOS $\\rightarrow$ 4) Запит до WINS-сервера $\\rightarrow$ 5) Широкомовний запит (Broadcast) у локальну мережу $\\rightarrow$ 6) Файл <code>LMHOSTS</code>.</p>
        </div>
      </section>

      <!-- MODULE 7: DHCP -->
      <section id="tab-dhcp" class="tab-module">
        <div class="section-header">
          <div class="section-title">📡 7. Служба DHCP, протокол DORA та взаємодія з DNS</div>
          <span class="section-badge">Автоматизація IP</span>
        </div>

        <p>Служба DHCP (Dynamic Host Configuration Protocol) автоматизує розподіл мережевих параметрів між клієнтами за протоколом <strong>DORA</strong> (порти UDP 67/68).</p>

        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th>Фаза DORA</th>
                <th>Хто надсилає</th>
                <th>Тип трафіку</th>
                <th>Що містить пакет</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Discover</strong></td>
                <td>Клієнт Windows 10</td>
                <td>Broadcast (255.255.255.255:67)</td>
                <td>«Шукаю доступний DHCP-сервер у мережі, мій MAC: 08-00-27-28-FF-B2»</td>
              </tr>
              <tr>
                <td><strong>Offer</strong></td>
                <td>DHCP Server (192.168.1.5)</td>
                <td>Unicast / Broadcast</td>
                <td>«Пропоную вільну IP-адресу 192.168.1.1 з маскою 255.255.255.0 на 8 днів»</td>
              </tr>
              <tr>
                <td><strong>Request</strong></td>
                <td>Клієнт Windows 10</td>
                <td>Broadcast</td>
                <td>«Я приймаю пропозицію IP 192.168.1.1 саме від сервера 192.168.1.5»</td>
              </tr>
              <tr>
                <td><strong>Acknowledge</strong></td>
                <td>DHCP Server (192.168.1.5)</td>
                <td>Unicast / Broadcast</td>
                <td>«Оренду підтверджено! Опції: Шлюз 192.168.1.4, DNS 192.168.1.5, Домен office.com»</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="grid-2">
          <div class="card">
            <div class="card-title">Чому обов'язкова авторизація DHCP в AD?</div>
            <p>Неавторизований (Rogue) DHCP-сервер у мережі може видати клієнтам підроблений шлюз за замовчуванням або зловмисний DNS, здійснивши атаку <strong>Man-in-the-Middle</strong>. Тому Windows Server блокує службу <code>dhcpserver</code>, доки адміністратор явно не авторизує її в Active Directory.</p>
          </div>
          <div class="card">
            <div class="card-title">Структура MAC-адреси (48 біт)</div>
            <p><strong>OUI (3 старші байти / 24 біти):</strong> Organizationally Unique Identifier — код виробника (наприклад, <code>1a:2b:3c</code>).</p>
            <p><strong>Device ID (3 молодші байти / 24 біти):</strong> Індивідуальний серійний номер мережевого адаптера (<code>4d:5e:6f</code>). Використовується для створення статичного резервування (Reservation).</p>
          </div>
        </div>
      </section>

      <!-- MODULE 8: GPO -->
      <section id="tab-gpo" class="tab-module">
        <div class="section-header">
          <div class="section-title">⚙️ 8. Групові політики (GPO) та архітектура порядку LSDOU</div>
          <span class="section-badge">Централізоване керування</span>
        </div>

        <!-- Simulator 4: GPO LSDOU Priority -->
        <div class="simulator-container">
          <div class="simulator-header">
            <div class="simulator-title">⚖️ Інтерактивний симулятор пріоритетів GPO за правилом LSDOU</div>
            <span class="simulator-badge">Розрахунок спадкування</span>
          </div>
          <div class="perm-grid">
            <div class="perm-select-group">
              <label>Параметр на рівні Домену (Domain):</label>
              <select id="gpoDomainParam" class="perm-select" onchange="calcGpoPriority()">
                <option value="600">Screen Saver: 600 секунд</option>
                <option value="900">Screen Saver: 900 секунд</option>
                <option value="not_configured">Не налаштовано</option>
              </select>
              <label style="margin-top: 10px;">
                <input type="checkbox" id="gpoEnforced" onchange="calcGpoPriority()"> Увімкнути Enforced (No Override) для політики домену
              </label>
            </div>
            <div class="perm-select-group">
              <label>Параметр на рівні OU «Фінансисти»:</label>
              <select id="gpoOuParam" class="perm-select" onchange="calcGpoPriority()">
                <option value="600">Screen Saver: 600 секунд (Лабораторна)</option>
                <option value="300">Screen Saver: 300 секунд</option>
                <option value="not_configured">Не налаштовано</option>
              </select>
              <label style="margin-top: 10px;">
                <input type="checkbox" id="gpoBlock" onchange="calcGpoPriority()"> Увімкнути Block Inheritance для OU «Фінансисти»
              </label>
            </div>
          </div>
          <div class="perm-result-box">
            <div>Підсумкове ефективне значення політики для користувача:</div>
            <div id="gpoResultDisplay" class="perm-result-text">Screen Saver: 600 секунд (З підрозділу OU)</div>
            <p id="gpoResultReason" style="font-size: 12.5px; color: var(--text-secondary); margin-top: 6px;">
              Політика підрозділу OU перекриває політику домену, оскільки застосовується пізніше за чергою LSDOU.
            </p>
          </div>
        </div>

        <div class="grid-2">
          <div class="card">
            <div class="card-title">GPC проти GPT</div>
            <p><strong>GPC (Group Policy Container):</strong> Об'єкт в Active Directory, що містить назву політики, атрибути, версію та стан прив'язки.</p>
            <p><strong>GPT (Group Policy Template):</strong> Реальні файли політики (шаблони, Registry.pol), розміщені у реплікованій папці <code>\\\\office.com\\SYSVOL\\office.com\\Policies\\{GUID}</code>.</p>
          </div>
          <div class="card">
            <div class="card-title">Черга застосування LSDOU</div>
            <p><code>Local -> Site -> Domain -> Organizational Unit</code></p>
            <p>Параметр, застосований пізніше за часом обробки, перезаписує попередній параметр, якщо не увімкнено <strong>Enforced</strong>.</p>
          </div>
        </div>
      </section>

      <!-- MODULE 9: Storage & Profiles -->
      <section id="tab-storage" class="tab-module">
        <div class="section-header">
          <div class="section-title">📁 9. Безпека спільного доступу (SMB vs NTFS) та профілі користувачів</div>
          <span class="section-badge">Файловий доступ</span>
        </div>

        <!-- Simulator 5: Permissions Calculator -->
        <div class="simulator-container">
          <div class="simulator-header">
            <div class="simulator-title">🧮 Калькулятор ефективних прав доступу (SMB Share vs NTFS Security)</div>
            <span class="simulator-badge">Матриця безпеки</span>
          </div>
          <div class="perm-grid">
            <div class="perm-select-group">
              <label>Мережевий дозвіл SMB (Share Permission):</label>
              <select id="sharePermSelect" class="perm-select" onchange="calculateEffectivePerms()">
                <option value="Full">Full Control (Повний доступ)</option>
                <option value="Change" selected>Change (Зміна та запис)</option>
                <option value="Read">Read (Тільки читання)</option>
                <option value="None">None (Немає доступу)</option>
              </select>
            </div>
            <div class="perm-select-group">
              <label>Дозвіл файлової системи (NTFS Permission):</label>
              <select id="ntfsPermSelect" class="perm-select" onchange="calculateEffectivePerms()">
                <option value="Full">Full Control (Повний контроль)</option>
                <option value="Modify">Modify (Зміна вмісту)</option>
                <option value="Read" selected>Read & Execute (Читання та запуск)</option>
                <option value="None">None (Заборона доступу)</option>
              </select>
            </div>
          </div>
          <div class="perm-result-box">
            <div>Підсумкове ефективне право при доступі через мережу:</div>
            <div id="effectiveResult" class="perm-result-text">Read & Execute (Тільки читання)</div>
            <p style="font-size: 12px; color: var(--text-secondary); margin-top: 6px;">
              Діє фундаментальне правило безпеки Windows: <strong>найбільш обмежувальний дозвіл виграє!</strong>
            </p>
          </div>
        </div>

        <div class="grid-3">
          <div class="card">
            <div class="card-title">Локальний профіль</div>
            <p>Зберігається локально на диску ПК у <code>C:\\Users\\Username</code>. Налаштування та файли недоступні з інших комп'ютерів.</p>
          </div>
          <div class="card">
            <div class="card-title">Переміщуваний (Roaming)</div>
            <p>Зберігається на сервері <code>\\\\server\\Profiles\\%username%</code>. При вході завантажується мережею, при виході (logoff) синхронізується назад на сервер.</p>
          </div>
          <div class="card">
            <div class="card-title">Обов'язковий (Mandatory)</div>
            <p>Файл конфігурації перейменовується на <code>NTUSER.MAN</code>. Будь-які зміни користувача під час сеансу автоматично <strong>скидаються при виході</strong>.</p>
          </div>
        </div>
      </section>

      <!-- MODULE 10: Client & RunAs -->
      <section id="tab-client" class="tab-module">
        <div class="section-header">
          <div class="section-title">💻 10. Клієнт Windows 10, приєднання до домену та утиліта RunAs</div>
          <span class="section-badge">Клієнтська інтеграція</span>
        </div>

        <div class="grid-2">
          <div class="card">
            <div class="card-title">Що відбувається при введенні ПК у домен?</div>
            <p>1. В Active Directory створюється обліковий запис комп'ютера <code>WIN-CLIENT$</code> зі своїм власним SID.</p>
            <p>2. Узгоджується довготривалий машинний пароль (Machine Password), який автоматично оновлюється кожні 30 днів.</p>
            <p>3. Служба Netlogon підтримує шифрований тунель <strong>Secure Channel</strong> між ПК та DC.</p>
            <p>4. У локальну групу «Адміністратори» клієнта автоматично додається група <code>office\\Domain Admins</code>.</p>
          </div>
          <div class="card">
            <div class="card-title">Механізм RunAs та принцип Least Privilege</div>
            <p>Постійна робота під обліковим записом адміністратора створює ризик миттєвого зараження всієї інфраструктури шкідливим ПЗ.</p>
            <p>Служба <strong>Secondary Logon</strong> та утиліта <code>runas.exe</code> дозволяють звичайному користувачеві породити окремий процес з маркером безпеки адміністратора:</p>
            <code>runas /user:office\\Administrator "mmc compmgmt.msc"</code>
          </div>
        </div>

        <div class="callout">
          <div class="callout-title">📊 Автоматизована міграція SSRS через rs.exe</div>
          <p>У лабораторній роботі досліджено утиліту <code>rs.exe</code>, яка за допомогою скрипта на Visual Basic (.rss) через SOAP API кінцевої точки <code>http://server/reportserver</code> переносить визначення звітів RDL, джерела даних та ресурси між серверами звітності SQL Server Reporting Services.</p>
        </div>
      </section>

      <!-- MODULE 11: Quiz -->
      <section id="tab-quiz" class="tab-module">
        <div class="section-header">
          <div class="section-title">🎓 11. Інтерактивний тренажер захисту лабораторної роботи</div>
          <span class="section-badge">15 екзаменаційних питань</span>
        </div>
        <p style="margin-bottom: 20px; color: var(--text-secondary);">Перевірте свої знання архітектури Windows Server перед захистом роботи викладачу. Оберіть правильний варіант відповіді та ознайомтеся з обґрунтуванням.</p>

        <div id="quizContainer">
          <!-- Dynamically populated or static questions -->
        </div>
      </section>

      <!-- MODULE 12: Glossary -->
      <section id="tab-glossary" class="tab-module">
        <div class="section-header">
          <div class="section-title">📚 12. Словник-довідник термінів та понять (Глосарій)</div>
          <span class="section-badge">Швидкий пошук</span>
        </div>

        <div class="glossary-filter-bar">
          <button class="filter-btn active" onclick="filterGlossary('all')">Всі терміни</button>
          <button class="filter-btn" onclick="filterGlossary('ad')">Active Directory</button>
          <button class="filter-btn" onclick="filterGlossary('net')">Мережа & DNS/DHCP</button>
          <button class="filter-btn" onclick="filterGlossary('sec')">Безпека & Kerberos</button>
          <button class="filter-btn" onclick="filterGlossary('storage')">Сховище & Профілі</button>
        </div>

        <div id="glossaryList">
          <!-- Populated by JS -->
        </div>
      </section>

    </main>
  </div>

  <!-- Footer -->
  <footer>
    <p>Національний університет «Львівська політехніка» • Кафедра систем автоматизованого проектування (САПР) • 2026</p>
    <p style="margin-top: 4px;">Лабораторна робота №5 з дисципліни «Операційні системи» • Студент: Андрій ЛЕМІШКА (ПП-14)</p>
  </footer>

  <script>
    // Tab switching logic
    const navButtons = document.querySelectorAll('.nav-btn');
    const tabModules = document.querySelectorAll('.tab-module');

    navButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetTab = btn.getAttribute('data-tab');
        navButtons.forEach(b => b.classList.remove('active'));
        tabModules.forEach(m => m.classList.remove('active'));
        
        btn.classList.add('active');
        const activeModule = document.getElementById(targetTab);
        if (activeModule) activeModule.classList.add('active');
      });
    });

    // Theme toggle
    const themeToggleBtn = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    const themeText = document.getElementById('themeText');

    themeToggleBtn.addEventListener('click', () => {
      const isLight = document.body.getAttribute('data-theme') === 'light';
      if (isLight) {
        document.body.removeAttribute('data-theme');
        themeIcon.textContent = '🌙';
        themeText.textContent = 'Темна';
      } else {
        document.body.setAttribute('data-theme', 'light');
        themeIcon.textContent = '☀️';
        themeText.textContent = 'Світла';
      }
    });

    // Simulator 1: AD Tree details
    const nodeData = {
      forest: {
        title: "🌲 Ліс (Forest): office.com",
        desc: "Найвищий рівень логічної ієрархії та справжня межа безпеки Microsoft. Об'єднує всі домени зі спільною схемою каталогу (Schema), глобальним каталогом (GC) та автоматичними двосторонніми транзитивними довірчими відносинами."
      },
      domain: {
        title: "🌐 Домен (Domain): office.com",
        desc: "Ключова адміністративна одиниця безпеки. Має спільну базу даних NTDS.dit на контролерах домену, єдину політику безпеки паролів (Default Domain Policy) та спільний простір імен DNS."
      },
      ou_fin: {
        title: "📁 Організаційний підрозділ: Фінансисти",
        desc: "Контейнер користувачів фінансового відділу (Фінансовий директор, Бухгалтер, Касир). До підрозділу прив'язано GPO «Фінансова політика безпеки» з обов'язковим блокуванням екрана через 600 секунд."
      },
      ou_it: {
        title: "📁 Організаційний підрозділ: IT-спеціалісти",
        desc: "Містить користувачів IT-відділу (Головний IT, Програміст, Системний адміністратор). Для облікового запису Програміст налаштовано автоматичне монтування домашньої папки P: до \\\\server\\Офіс."
      },
      ou_groups: {
        title: "👥 Організаційний підрозділ: Групи",
        desc: "Містить глобальні групи безпеки «Фінансисти» та «IT-відділ» для призначення дозволів на файлові ресурси та розмежування прав за функціональними обов'язками."
      }
    };

    function showNodeDetails(key) {
      document.querySelectorAll('.tree-node').forEach(n => n.classList.remove('selected'));
      event.currentTarget.classList.add('selected');
      const item = nodeData[key];
      const box = document.getElementById('adNodeInfo');
      if (item) {
        box.innerHTML = `<strong>${item.title}</strong><p style="margin-top:6px;">${item.desc}</p>`;
      }
    }

    // Simulator 2: Kerberos steps
    const kerbSteps = [
      {
        title: "Крок 1: AS-REQ (Authentication Service Request)",
        desc: "Клієнт Windows 10 надсилає на KDC (контролер 192.168.1.5:88) логін користувача та часову мітку (Timestamp), зашифровану NTLM-хешем пароля користувача. Пароль у відкритому вигляді мережею не передається!"
      },
      {
        title: "Крок 2: AS-REP (Authentication Service Reply)",
        desc: "KDC перевіряє часову мітку та генерує квиток TGT (Ticket Granting Ticket), зашифрований секретним ключем службового акаунта krbtgt. Клієнт отримує TGT та сесійний ключ AS-TGS."
      },
      {
        title: "Крок 3: TGS-REQ (Ticket Granting Service Request)",
        desc: "Коли користувач намагається відкрити спільну папку \\\\server\\Офіс, клієнт звертається до KDC, пред'являючи свій TGT та ім'я цільової служби SPN (cifs/server.office.com)."
      },
      {
        title: "Крок 4: TGS-REP (Ticket Granting Service Reply)",
        desc: "KDC розшифровує TGT своїм ключем krbtgt і видає клієнту квиток до сервісу (Service Ticket), зашифрований секретним паролем машини файлового сервера (Machine Password)."
      },
      {
        title: "Крок 5: AP-REQ (Application Request to File Server)",
        desc: "Клієнт відправляє Service Ticket безпосередньо файловому серверу SMB (порт 445). Сервер розшифровує квиток власним ключем, переконується у валідності підпису KDC та відкриває доступ до папки C:\\Офіс!"
      }
    ];

    function showKerbStep(stepNum) {
      const btns = document.querySelectorAll('.kerberos-step-btn');
      btns.forEach((b, i) => {
        if (i === stepNum - 1) b.classList.add('active');
        else b.classList.remove('active');
      });
      const data = kerbSteps[stepNum - 1];
      const disp = document.getElementById('kerbDetails');
      disp.innerHTML = `<strong>${data.title}</strong><p style="margin-top:6px; color: var(--text-secondary);">${data.desc}</p>`;
    }

    // Simulator 6: ESE Table Inspector
    const tableInfo = {
      datatable: {
        name: "datatable (Таблиця об'єктів)",
        details: "Головна сутність NTDS.dit. Зберігає всі об'єкти домену. Кожен рядок представляє унікальний DNT (Directory Node Tag). Атрибути об'єктів (ім'я, SID, парольний хеш) індексуються за допомогою B-дерев для забезпечення миттєвого пошуку LDAP."
      },
      link_table: {
        name: "link_table (Таблиця зв'язків)",
        details: "Забезпечує референційну цілісність між об'єктами. Замість збереження списку тисяч користувачів усередині поля групи, зв'язок виноситься в link_table. Це гарантує, що реплікується лише конкретний доданий користувач (Linked Value Replication, LVR)."
      },
      sd_table: {
        name: "sd_table (Дескриптори безпеки)",
        details: "Single-Instance Store для дескрипторів безпеки ACL. Якщо 50 000 файлів чи об'єктів мають однаковий дозвіл безпеки, він записується в sd_table лише 1 раз, зменшуючи розмір бази NTDS.dit на 40-60%."
      }
    };

    function inspectTable(tname) {
      const data = tableInfo[tname];
      const box = document.getElementById('tableInspectorDetails');
      if (data) {
        box.innerHTML = `<strong>${data.name}</strong><p style="margin-top:6px;">${data.details}</p>`;
      }
    }

    // Simulator 4: GPO LSDOU
    function calcGpoPriority() {
      const domVal = document.getElementById('gpoDomainParam').value;
      const ouVal = document.getElementById('gpoOuParam').value;
      const enforced = document.getElementById('gpoEnforced').checked;
      const blocked = document.getElementById('gpoBlock').checked;

      const resDisplay = document.getElementById('gpoResultDisplay');
      const resReason = document.getElementById('gpoResultReason');

      if (enforced) {
        resDisplay.textContent = `Screen Saver: ${domVal} секунд (Перемога Домену через Enforced)`;
        resDisplay.style.color = "var(--accent-amber)";
        resReason.textContent = "Прапорець Enforced (No Override) на політиці домену примусово ігнорує будь-які Block Inheritance та локальні налаштування підрозділів!";
        return;
      }

      if (blocked && ouVal === 'not_configured') {
        resDisplay.textContent = "Політика відсутня (Заблоковано спадкування)";
        resDisplay.style.color = "var(--accent-red)";
        resReason.textContent = "Block Inheritance на підрозділі заблокував спадкування політики домену, а в самому OU параметр не задано.";
        return;
      }

      if (ouVal !== 'not_configured') {
        resDisplay.textContent = `Screen Saver: ${ouVal} секунд (Параметр з OU «Фінансисти»)`;
        resDisplay.style.color = "var(--accent-green)";
        resReason.textContent = "Згідно з правилом LSDOU, параметр підрозділу застосовується пізніше за домен і перекриває його значення.";
      } else {
        resDisplay.textContent = `Screen Saver: ${domVal} секунд (Успадковано з Домену)`;
        resDisplay.style.color = "var(--accent-cyan)";
        resReason.textContent = "Параметр успадковано з рівня домену, оскільки в підрозділі OU він не сконфігурований.";
      }
    }

    // Simulator 5: Permissions Calculator
    function calculateEffectivePerms() {
      const share = document.getElementById('sharePermSelect').value;
      const ntfs = document.getElementById('ntfsPermSelect').value;
      const res = document.getElementById('effectiveResult');

      if (share === 'None' || ntfs === 'None') {
        res.textContent = "ACCESS DENIED (Доступ повністю заблоковано)";
        res.style.color = "var(--accent-red)";
        return;
      }

      const rank = { 'Full': 4, 'Modify': 3, 'Change': 3, 'Read': 1 };
      const sRank = rank[share] || 1;
      const nRank = rank[ntfs] || 1;

      const minRank = Math.min(sRank, nRank);
      if (minRank >= 3) {
        res.textContent = "Modify / Change (Повний запис, редагування та видалення)";
        res.style.color = "var(--accent-green)";
      } else {
        res.textContent = "Read (Тільки читання та перегляд файлів)";
        res.style.color = "var(--accent-amber)";
      }
    }

    // Quiz Questions Data
    const quizData = [
      {
        q: "1. Чому для контролера домену Active Directory вимагається обов'язкове налаштування статичної IP-адреси?",
        options: [
          "А) Щоб пришвидшити завантаження операційної системи Windows Server",
          "Б) Оскільки клієнти та інші сервери знаходять його за постійною адресою в SRV-записах DNS (якщо IP зміниться — Kerberos та вхід заблокуються)",
          "В) Тому що служба DHCP не вміє працювати на тому самому сервері",
          "Г) Це необов'язково, контролер домену може працювати на динамічній IP"
        ],
        correct: 1,
        hint: "Контролер домену реєструє службові SRV-записи (_ldap, _kerberos) у зоні DNS, на які орієнтуються всі клієнти."
      },
      {
        q: "2. У чому полягає фундаментальна різниця між Organizational Unit (OU) та звичайним системним контейнером (наприклад, CN=Users)?",
        options: [
          "А) У контейнері можуть зберігатися лише комп'ютери, а в OU — тільки люди",
          "Б) До OU можна прив'язувати об'єкти групових політик (GPO) та делегувати права адміністрування, а до системних контейнерів — ні",
          "В) Контейнери шифруються через BitLocker, а OU — ні",
          "Г) Різниці немає, це просто синоніми"
        ],
        correct: 1,
        hint: "OU створюються адміністратором спеціально для застосування групових політик і делегування адміністративних повноважень."
      },
      {
        q: "3. Яка роль FSMO відповідає за синхронізацію системного часу (NTP) та негайну обробку змінених паролів у домені?",
        options: [
          "А) Schema Master",
          "Б) RID Master",
          "В) PDC Emulator",
          "Г) Infrastructure Master"
        ],
        correct: 2,
        hint: "Емулятор первинного контролера домену (PDC Emulator) є головним джерелом часу та паролів у домені."
      },
      {
        q: "4. Яке правило діє при одночасному застосуванні дозволів спільного ресурсу (SMB) та прав файлової системи (NTFS)?",
        options: [
          "А) Дозволи SMB завжди мають вищий пріоритет",
          "Б) Дозволи NTFS завжди перекривають SMB",
          "В) Обирається найбільш обмежувальний (Most Restrictive) дозвіл між SMB та NTFS",
          "Г) Права сумуються і надається максимальний доступ"
        ],
        correct: 2,
        hint: "Діє формула Effective Permission = min(Share Permission, NTFS Permission)."
      },
      {
        q: "5. Що відбувається з профілем Mandatory Profile при виході користувача із системи (Logoff)?",
        options: [
          "А) Усі зміни автоматично синхронізуються у хмарне сховище",
          "Б) Будь-які внесені під час сеансу зміни файлів та налаштувань реєстру автоматично скидаються і не зберігаються",
          "В) Профіль шифрується алгоритмом RSA-4096",
          "Г) Комп'ютер автоматично вимикається"
        ],
        correct: 1,
        hint: "Обов'язковий профіль (NTUSER.MAN) захищає робоче місце від будь-яких несанкціонованих модифікацій."
      }
    ];

    function renderQuiz() {
      const container = document.getElementById('quizContainer');
      container.innerHTML = '';
      quizData.forEach((item, qIdx) => {
        const card = document.createElement('div');
        card.className = 'quiz-card';
        card.innerHTML = `
          <div class="quiz-question">${item.q}</div>
          <div class="quiz-options">
            ${item.options.map((opt, oIdx) => `
              <button class="quiz-option-btn" onclick="checkAnswer(${qIdx}, ${oIdx})">${opt}</button>
            `).join('')}
          </div>
          <div id="quiz-feedback-${qIdx}" class="quiz-feedback">
            <strong>Пояснення викладача:</strong> ${item.hint}
          </div>
        `;
        container.appendChild(card);
      });
    }

    function checkAnswer(qIdx, selectedOption) {
      const q = quizData[qIdx];
      const card = document.querySelectorAll('.quiz-card')[qIdx];
      const buttons = card.querySelectorAll('.quiz-option-btn');
      const feedback = document.getElementById(`quiz-feedback-${qIdx}`);

      buttons.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === q.correct) {
          btn.classList.add('correct');
        } else if (idx === selectedOption) {
          btn.classList.add('wrong');
        }
      });
      feedback.style.display = 'block';
    }

    // Glossary Data
    const glossaryData = [
      { cat: 'ad', term: 'Active Directory Domain Services (AD DS)', desc: 'Розподілена ієрархічна служба каталогів Windows Server для централізованої автентифікації, авторизації та зберігання відомостей про ресурси підприємства.' },
      { cat: 'sec', term: 'Kerberos v5 (RFC 4120)', desc: 'Протокол мережевої автентифікації на основі квитків (TGT, Service Ticket) та довіреної третьої сторони (KDC), що усуває передачу паролів мережею.' },
      { cat: 'ad', term: 'FSMO (Flexible Single Master Operation)', desc: 'Ролі операцій з одним хазяїном (Schema Master, Domain Naming, PDC Emulator, RID, Infrastructure Master) для запобігання колізіям у реплікації.' },
      { cat: 'net', term: 'DORA (Discover, Offer, Request, Acknowledge)', desc: 'Чотириетапна послідовність отримання конфігурації TCP/IP за протоколом DHCP (порти 67/68 UDP).' },
      { cat: 'net', term: 'SRV-записи DNS (RFC 2782)', desc: 'Ресурсні записи в DNS (_ldap, _kerberos), які повідомляють клієнтам порти та імена контролерів домену для підключення.' },
      { cat: 'ad', term: 'NTDS.dit', desc: 'Основний файл реляційної бази даних Active Directory, побудований на рушії ESE (JET Blue) з відповідністю вимогам ACID.' },
      { cat: 'storage', term: 'Effective Access (SMB vs NTFS)', desc: 'Підсумкове результуюче право доступу користувача до мережевої папки, що обчислюється як найбільш суворе обмеження між дозволами Share та NTFS.' },
      { cat: 'storage', term: 'Mandatory Profile (Обов\'язковий профіль)', desc: 'Профіль користувача з файлом NTUSER.MAN, у якому всі внесені під час сеансу зміни знищуються після завершення роботи.' },
      { cat: 'sec', term: 'Secondary Logon (RunAs)', desc: 'Механізм Windows, що дозволяє користувачеві запускати окремий процес під обліковим записом адміністратора без зміни поточного сеансу.' },
      { cat: 'net', term: 'DnsUpdateProxy', desc: 'Спеціальна група безпеки AD, члени якої реєструють записи DNS без захисних дескрипторів власності для спрощення взаємодії DHCP та клієнтів.' }
    ];

    function filterGlossary(cat) {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      event.currentTarget.classList.add('active');

      const list = document.getElementById('glossaryList');
      list.innerHTML = '';
      const filtered = cat === 'all' ? glossaryData : glossaryData.filter(i => i.cat === cat);
      filtered.forEach(item => {
        const div = document.createElement('div');
        div.className = 'glossary-item';
        div.innerHTML = `<div class="glossary-term">${item.term}</div><div class="glossary-desc">${item.desc}</div>`;
        list.appendChild(div);
      });
    }

    // Global Search Filter
    document.getElementById('globalSearch').addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      if (!q) return;

      const terms = document.querySelectorAll('.glossary-item');
      terms.forEach(t => {
        const text = t.textContent.toLowerCase();
        t.style.display = text.includes(q) ? 'block' : 'none';
      });

      // Switch to glossary if searching
      if (q.length > 2) {
        document.querySelector('[data-tab="tab-glossary"]').click();
      }
    });

    // Initialize components
    renderQuiz();
    filterGlossary('all');
  </script>
</body>
</html>
"""

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated interactive website at: {html_file} (Size: {len(html_content)} bytes)")
