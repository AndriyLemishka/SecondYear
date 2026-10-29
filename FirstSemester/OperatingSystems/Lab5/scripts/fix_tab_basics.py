# -*- coding: utf-8 -*-
HTML_FILE = r"D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\Explenation material\index.html"

with open(HTML_FILE, "r", encoding="utf-8") as f:
    html = f.read()

# Tab basics section definition
tab_basics_section = """
      <!-- MODULE 0: Fundamental Basics (Server, IP, DNS, DHCP, Gateway, Subnet) -->
      <section id="tab-basics" class="tab-module active">
        <div class="section-header">
          <div class="section-title">💡 0. Фундаментальний базис комп'ютерних мереж та ОС</div>
          <span class="section-badge">Академічні визначення</span>
        </div>

        <p style="margin-bottom: 20px; color: var(--text-secondary); font-size: 14.5px;">
          Перед тим як вивчати внутрішнє влаштування Active Directory, викладач обов'язково перевіряє розуміння <strong>фундаментальних основ</strong>: що таке сервер, як влаштована IP-адресація, чому серверу не можна давати динамічний IP та що таке петльова (домашня) адреса.
        </p>

        <!-- Interactive Subnet Calculator Simulator -->
        <div class="simulator-container">
          <div class="simulator-header">
            <div class="simulator-title">🧮 Інтерактивний калькулятор IP-адреси, Маски та Підмережі</div>
            <span class="simulator-badge">Аналізатор L3 адресації</span>
          </div>
          <p style="font-size: 13.5px; color: var(--text-secondary); margin-bottom: 14px;">
            Введіть IP-адресу та маску підмережі, щоб розрахувати двійковий вигляд, номер мережі (Network ID), широкомовну адресу (Broadcast) та кількість доступних комп'ютерів:
          </p>
          <div class="perm-grid">
            <div class="perm-select-group">
              <label>IP-адреса вузла:</label>
              <input type="text" id="calcIpInput" class="perm-select" value="192.168.1.5" style="color:var(--accent-cyan); font-family:var(--code-font);">
            </div>
            <div class="perm-select-group">
              <label>Маска підмережі (Subnet Mask):</label>
              <select id="calcMaskSelect" class="perm-select" onchange="runSubnetCalc()">
                <option value="255.255.255.0" selected>255.255.255.0 (/24 — 254 ПК, Лаб №5)</option>
                <option value="255.255.0.0">255.255.0.0 (/16 — 65 534 ПК)</option>
                <option value="255.255.255.128">255.255.255.128 (/25 — 126 ПК)</option>
                <option value="255.255.255.192">255.255.255.192 (/26 — 62 ПК)</option>
              </select>
            </div>
          </div>
          <button onclick="runSubnetCalc()" class="filter-btn" style="margin-bottom: 16px; padding: 8px 18px; border-radius: 6px; font-weight:700;">⚡ Розрахувати підмережу</button>

          <div id="subnetCalcResult" style="background: #060913; border: 1px solid var(--border-color); border-radius: 8px; padding: 18px; font-family: var(--code-font); font-size: 13px; line-height: 1.7;">
            <!-- Populated by JS -->
          </div>
        </div>

        <!-- Definition Cards Grid -->
        <div class="grid-2">
          <div class="card">
            <div class="card-title">🖥️ 1. Що таке Сервер та Клієнт?</div>
            <p><strong>Сервер (Server):</strong> Апаратний комп'ютер або спеціалізована фонова служба (Daemon), що централізовано очікує підключень на відкритих мережевих портах і обслуговує запити клієнтів за моделлю «клієнт-сервер».</p>
            <p style="margin-top: 6px;"><strong>Клієнт (Client):</strong> Кінцева робоча станція користувача (Windows 10 Pro), що ініціює запити до сервера для аутентифікації, доступу до файлів або розпізнавання імен.</p>
          </div>

          <div class="card">
            <div class="card-title">🔢 2. Що таке IP-адреса (RFC 791)?</div>
            <p><strong>Визначення:</strong> Унікальний логічний числовий номер мережевого інтерфейсу пристрою на 3-му (мережевому) рівні моделі OSI.</p>
            <p style="margin-top: 6px;"><strong>Формат IPv4:</strong> 32 біти (4 байти), записані як 4 числа від 0 до 255 через крапку: <code>192.168.1.5</code>. Без IP-адреси пакети не можуть бути маршрутизовані.</p>
          </div>
        </div>

        <div class="grid-2">
          <div class="card">
            <div class="card-title">📌 3. Статичний проти Динамічного IP</div>
            <p><strong>Статичний IP:</strong> Задається адміністратором назавжди вручну. <strong>Обов'язковий для серверів!</strong> Якщо адреса контролера зміниться, клієнти не зможуть знайти DNS і Kerberos заблокує вхід у домен.</p>
            <p style="margin-top: 6px;"><strong>Динамічний IP:</strong> Видається автоматично службою <strong>DHCP</strong> в оренду на обмежений час (Lease Time). Використовується для звичайних робочих станцій, ноутбуків та смартфонів.</p>
          </div>

          <div class="card">
            <div class="card-title">🏠 4. Що таке «Домашня адреса»?</div>
            <p><strong>1. Петльовий інтерфейс (Loopback / 127.0.0.1):</strong> Адреса комп'ютера «на самого себе» за стандартом RFC 1122. Пакети не йдуть у мережевий кабель, а розвертаються всередині ОС.</p>
            <p style="margin-top: 6px;"><strong>2. Домашня папка (Home Directory):</strong> Мережева папка на сервері (диск <code>P:\\</code> у лабі), що автоматично підключається користувачеві при вході в систему.</p>
          </div>
        </div>

        <div class="grid-2">
          <div class="card">
            <div class="card-title">🎭 5. Маска підмережі (Subnet Mask)</div>
            <p>32-бітне число (<code>255.255.255.0</code> або <code>/24</code>), яке через операцію логічного «І» (Bitwise AND) ділить IP-адресу на дві частини: <strong>Network ID</strong> (номер мережі: <code>192.168.1.0</code>) та <strong>Host ID</strong> (номер вузла: <code>.5</code>).</p>
          </div>

          <div class="card">
            <div class="card-title">🚪 6. Основний шлюз (Default Gateway)</div>
            <p>Мережева адреса маршрутизатора (у нас <code>192.168.1.4</code>), на яку операційна система відправляє пакети, якщо IP-адреса отримувача знаходиться <strong>за межами поточної підмережі</strong> (в іншій мережі або Інтернеті).</p>
          </div>
        </div>

        <div class="grid-2">
          <div class="card">
            <div class="card-title">🆔 7. MAC-адреса проти IP-адреси</div>
            <p><strong>MAC (L2 канальний рівень):</strong> Фізична апаратна адреса з 48 біт (наприклад, <code>08-00-27-28-FF-B2</code>), вшита виробником у чіп карти. Це незмінний «паспорт» залізяки.</p>
            <p style="margin-top: 6px;"><strong>IP (L3 мережевий рівень):</strong> Логічна змінна адреса, яка визначається місцем підключення комп'ютера в мережі.</p>
          </div>

          <div class="card">
            <div class="card-title">📖 8. Що таке DNS та DHCP?</div>
            <p><strong>DNS (Порт 53):</strong> «Телефонна книга» мережі, яка перекладає текстові імена (<code>office.com</code>) у цифрові IP (<code>192.168.1.5</code>).</p>
            <p style="margin-top: 6px;"><strong>DHCP (Порти 67/68):</strong> Автоматичний адміністратор, що видає клієнтам IP, шлюз і DNS за протоколом DORA.</p>
          </div>
        </div>

        <div class="callout">
          <div class="callout-title">⚠️ Головна теза для викладача:</div>
          <p>
            Контролер домену <code>office.com</code> зобов'язаний мати фіксовану <strong>статичну IP-адресу 192.168.1.5</strong> та маску <strong>255.255.255.0</strong>, оскільки служба DNS публікує на цю адресу спеціальні SRV-записи (<code>_ldap</code>, <code>_kerberos</code>). Якби сервер отримав динамічну IP-адресу, перша ж зміна оренди призвела б до повного колапсу домену та відмови входу клієнтів Windows 10!
          </p>
        </div>
      </section>
"""

intro_marker = '      <!-- MODULE 1: Intro -->'
if '<section id="tab-basics"' not in html:
    html = html.replace(intro_marker, tab_basics_section + "\n" + intro_marker)

# Ensure tab-intro is not marked active
html = html.replace('<section id="tab-intro" class="tab-module active">', '<section id="tab-intro" class="tab-module">')

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print("Properly inserted tab-basics into index.html")
