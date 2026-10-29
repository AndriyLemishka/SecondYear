# -*- coding: utf-8 -*-
import json
import re
import subprocess

HTML_PATH = r"D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\Explenation material\index.html"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Clean, robust JavaScript code with zero syntax errors, using double quotes and escaped strings
clean_js = """
    // 1. Tab switching logic
    const navButtons = document.querySelectorAll('.nav-btn');
    const tabModules = document.querySelectorAll('.tab-module');

    navButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetTab = btn.getAttribute('data-tab');
        navButtons.forEach(b => b.classList.remove('active'));
        tabModules.forEach(m => m.classList.remove('active'));

        btn.classList.add('active');
        const activeModule = document.getElementById(targetTab);
        if (activeModule) {
          activeModule.classList.add('active');
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      });
    });

    // 2. Theme toggle
    const themeToggleBtn = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    const themeText = document.getElementById('themeText');

    if (themeToggleBtn) {
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
    }

    // 3. Subnet Calculator Interactive Engine
    function ipToBinary(ipStr) {
      return ipStr.split('.').map(octet => {
        let b = parseInt(octet, 10).toString(2);
        while (b.length < 8) b = '0' + b;
        return b;
      }).join('.');
    }

    function runSubnetCalc() {
      const ipInput = document.getElementById('calcIpInput');
      const maskSelect = document.getElementById('calcMaskSelect');
      const res = document.getElementById('subnetCalcResult');
      if (!ipInput || !maskSelect || !res) return;

      const ip = ipInput.value.trim();
      const mask = maskSelect.value.trim();

      const ipParts = ip.split('.').map(Number);
      const maskParts = mask.split('.').map(Number);

      if (ipParts.length !== 4 || ipParts.some(p => isNaN(p) || p < 0 || p > 255)) {
        res.innerHTML = '<span style="color:var(--accent-red);">Помилка: Введіть коректну IPv4 адресу (наприклад, 192.168.1.5)</span>';
        return;
      }

      const netParts = [];
      const bcastParts = [];
      for (let i = 0; i < 4; i++) {
        netParts.push(ipParts[i] & maskParts[i]);
        bcastParts.push(netParts[i] | (255 - maskParts[i]));
      }

      const netStr = netParts.join('.');
      const bcastStr = bcastParts.join('.');
      const ipBin = ipToBinary(ip);
      const maskBin = ipToBinary(mask);

      const cidr = maskBin.replace(/\\./g, '').split('1').length - 1;
      const totalHosts = Math.pow(2, 32 - cidr);
      const usableHosts = totalHosts > 2 ? totalHosts - 2 : 0;

      const firstHost = `${netParts[0]}.${netParts[1]}.${netParts[2]}.${netParts[3] + 1}`;
      const lastHost = `${bcastParts[0]}.${bcastParts[1]}.${bcastParts[2]}.${bcastParts[3] - 1}`;

      res.innerHTML = `
        <div style="color: var(--accent-cyan); font-weight:700; margin-bottom: 8px;">📊 Результати розрахунку підмережі:</div>
        <div><strong>IP-адреса (Dec):</strong> <span style="color:var(--text-primary);">${ip}</span> /${cidr}</div>
        <div><strong>IP-адреса (Bin):</strong> <span style="color:#38bdf8;">${ipBin}</span></div>
        <div><strong>Маска підмережі:</strong> <span style="color:#f59e0b;">${maskBin}</span> (${mask})</div>
        <hr style="border:none; border-top: 1px dashed var(--border-color); margin: 8px 0;">
        <div><strong>Адреса підмережі (Network ID):</strong> <span style="color:var(--accent-green); font-weight:700;">${netStr}</span></div>
        <div><strong>Широкомовна адреса (Broadcast):</strong> <span style="color:var(--accent-red); font-weight:700;">${bcastStr}</span></div>
        <div><strong>Діапазон доступних адрес для ПК:</strong> <span style="color:var(--accent-cyan);">${firstHost} &mdash; ${lastHost}</span></div>
        <div><strong>Кількість робочих станцій у мережі:</strong> <span style="color:var(--accent-green); font-weight:700;">${usableHosts} ПК</span> (2<sup>${32-cidr}</sup> &minus; 2)</div>
        <div><strong>Тип адреси:</strong> Приватна (Private / RFC 1918), Клас C локальної мережі</div>
      `;
    }

    // 4. Simulator 1: AD Tree details
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
        desc: "Містить користувачів IT-відділу (Головний IT, Програміст, Системний адміністратор). Для облікового запису Програміст налаштовано автоматичне монтування домашньої папки P: до \\\\server\\\\Офіс."
      },
      ou_groups: {
        title: "👥 Організаційний підрозділ: Групи",
        desc: "Містить глобальні групи безпеки «Фінансисти» та «IT-відділ» для призначення дозволів на файлові ресурси та розмежування прав за функціональними обов'язками."
      }
    };

    function showNodeDetails(key) {
      document.querySelectorAll('.tree-node').forEach(n => n.classList.remove('selected'));
      if (event && event.currentTarget) event.currentTarget.classList.add('selected');
      const item = nodeData[key];
      const box = document.getElementById('adNodeInfo');
      if (box && item) {
        box.innerHTML = `<strong>${item.title}</strong><p style="margin-top:6px;">${item.desc}</p>`;
      }
    }

    // 5. Simulator 2: Kerberos steps
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
        desc: "Коли користувач намагається відкрити спільну папку \\\\server\\\\Офіс, клієнт звертається до KDC, пред'являючи свій TGT та ім'я цільової служби SPN (cifs/server.office.com)."
      },
      {
        title: "Крок 4: TGS-REP (Ticket Granting Service Reply)",
        desc: "KDC розшифровує TGT своїм ключем krbtgt і видає клієнту квиток до сервісу (Service Ticket), зашифрований секретним паролем машини файлового сервера (Machine Password)."
      },
      {
        title: "Крок 5: AP-REQ (Application Request to File Server)",
        desc: "Клієнт відправляє Service Ticket безпосередньо файловому серверу SMB (порт 445). Сервер розшифровує квиток власним ключем, переконується у валідності підпису KDC та відкриває доступ до папки C:\\\\Офіс!"
      }
    ];

    function showKerbStep(stepNum) {
      const btns = document.querySelectorAll('.kerberos-step-btn:not(.dora-btn)');
      btns.forEach((b, i) => {
        if (i === stepNum - 1) b.classList.add('active');
        else b.classList.remove('active');
      });
      const data = kerbSteps[stepNum - 1];
      const disp = document.getElementById('kerbDetails');
      if (disp && data) {
        disp.innerHTML = `<strong>${data.title}</strong><p style="margin-top:6px; color: var(--text-secondary);">${data.desc}</p>`;
      }
    }

    // 6. Simulator 3: DHCP DORA interactive logic
    const doraSteps = [
      {
        title: "Фаза 1: DHCPDISCOVER (Виявлення)",
        desc: "<strong>Хто:</strong> Клієнт Windows 10 &rarr; <strong>Кому:</strong> Broadcast (255.255.255.255:67)<br><strong>IP джерела:</strong> 0.0.0.0:68 | <strong>IP призначення:</strong> 255.255.255.255:67<br><strong>Повідомлення:</strong> Клієнт не має адреси, тому розсилає широкомовний кадр із вказівкою свого MAC (08-00-27-28-FF-B2) та списком запитуваних опцій (Subnet Mask, Router, DNS Server, Domain Name)."
      },
      {
        title: "Фаза 2: DHCPOFFER (Пропозиція)",
        desc: "<strong>Хто:</strong> DHCP-сервер (192.168.1.5:67) &rarr; <strong>Кому:</strong> Клієнт (192.168.1.1 або Broadcast:68)<br><strong>Запропонована IP:</strong> 192.168.1.1 | <strong>Маска:</strong> 255.255.255.0 | <strong>Оренда:</strong> 8 днів<br><strong>Повідомлення:</strong> Сервер тимчасово бронює адресу з пулу 192.168.1.1-192.168.1.100 і повідомляє клієнту свої реквізити та параметри оренди."
      },
      {
        title: "Фаза 3: DHCPREQUEST (Запит вибору)",
        desc: "<strong>Хто:</strong> Клієнт Windows 10 &rarr; <strong>Кому:</strong> Broadcast (255.255.255.255:67)<br><strong>IP джерела:</strong> 0.0.0.0:68 | <strong>Server Identifier:</strong> 192.168.1.5<br><strong>Повідомлення:</strong> Клієнт транслює Broadcast, оголошуючи, що приймає офер саме від сервера 192.168.1.5. Інші можливі сервери розуміють, що їхні офери відхилено, і повертають адреси в пул."
      },
      {
        title: "Фаза 4: DHCPACK (Підтвердження)",
        desc: "<strong>Хто:</strong> DHCP-сервер (192.168.1.5:67) &rarr; <strong>Кому:</strong> Клієнт (192.168.1.1:68)<br><strong>Статус:</strong> Оренду активовано | <strong>Запис у базі:</strong> MAC 08-00-27-28-FF-B2 &harr; IP 192.168.1.1<br><strong>Передані опції:</strong> Option 003 (Router = 192.168.1.4), Option 006 (DNS = 192.168.1.5), Option 015 (Domain = office.com). Одночасно сервер оновлює PTR/A записи в DNS."
      }
    ];

    function showDoraStep(stepNum) {
      const btns = document.querySelectorAll('.dora-btn');
      btns.forEach((b, i) => {
        if (i === stepNum - 1) b.classList.add('active');
        else b.classList.remove('active');
      });
      const data = doraSteps[stepNum - 1];
      const disp = document.getElementById('doraDetails');
      if (disp && data) {
        disp.innerHTML = `<strong>${data.title}</strong><div style="margin-top:6px; color: var(--text-secondary); line-height:1.5;">${data.desc}</div>`;
      }
    }

    // 7. Simulator 4: ESE Table Inspector
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
      if (box && data) {
        box.innerHTML = `<strong>${data.name}</strong><p style="margin-top:6px;">${data.details}</p>`;
      }
    }

    // 8. Simulator 5: GPO LSDOU Priority
    function calcGpoPriority() {
      const domSelect = document.getElementById('gpoDomainParam');
      const ouSelect = document.getElementById('gpoOuParam');
      const enforcedCb = document.getElementById('gpoEnforced');
      const blockedCb = document.getElementById('gpoBlock');
      const resDisplay = document.getElementById('gpoResultDisplay');
      const resReason = document.getElementById('gpoResultReason');

      if (!domSelect || !ouSelect || !enforcedCb || !blockedCb || !resDisplay || !resReason) return;

      const domVal = domSelect.value;
      const ouVal = ouSelect.value;
      const enforced = enforcedCb.checked;
      const blocked = blockedCb.checked;

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

    // 9. Simulator 6: Effective Permissions Calculator
    function calculateEffectivePerms() {
      const shareSelect = document.getElementById('sharePermSelect');
      const ntfsSelect = document.getElementById('ntfsPermSelect');
      const res = document.getElementById('effectiveResult');
      if (!shareSelect || !ntfsSelect || !res) return;

      const share = shareSelect.value;
      const ntfs = ntfsSelect.value;

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

    // 10. Full 15 Defense Questions Quiz Data
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
          "В) Обирається найбільш обмежувальний (Most Restrictive) дозвіл між SMB та NTFS: min(Share, NTFS)",
          "Г) Права сумуються і надається максимальний доступ"
        ],
        correct: 2,
        hint: "Діє формула Effective Permission = min(Share Permission, NTFS Permission). Обмежувальне правило захищає сервер."
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
      },
      {
        q: "6. Чому протокол автентифікації Kerberos v5 вимагає різницю системного часу (Clock Skew) між клієнтом і KDC не більше 5 хвилин?",
        options: [
          "А) Щоб економити тактову частоту процесора сервера",
          "Б) Для захисту від атак повторного відтворення (Replay Attack) перехоплених зловмисником пакетів автентифікації",
          "В) Це апаратне обмеження мережевої карти Ethernet",
          "Г) Щоб гарантувати швидке відкриття папок SMB"
        ],
        correct: 1,
        hint: "Пакет автентифікації містить зашифровану часову мітку. Якщо час застарів (>5 хв), сервер відхиляє його з кодом KRB_AP_ERR_SKEW."
      },
      {
        q: "7. Як клієнт Windows 10 знаходить контролер домену при приєднанні до мережі office.com?",
        options: [
          "А) Сканує всю мережу за протоколом ICMP Ping",
          "Б) Звертається до DNS-сервера за спеціальним SRV-записом _ldap._tcp.dc._msdcs.office.com",
          "В) Шукає файл hosts на диску C:",
          "Г) Читає MAC-адресу з таблиці роутера"
        ],
        correct: 1,
        hint: "Служба Netlogon на клієнті через DNS знаходить SRV-записи контролера домену та надсилає UDP LDAP Ping."
      },
      {
        q: "8. Що станеться, якщо на підрозділ накладено «Block Inheritance», але на рівні домену політика позначена як «Enforced»?",
        options: [
          "А) Політика домену не застосується, оскільки Block Inheritance сильніший",
          "Б) Політика домену Enforced примусово застосується, проігнорувавши блокування спадкування",
          "В) Виникне збій групових політик (GPO Error 1002)",
          "Г) Дозволи накладаються випадковим чином"
        ],
        correct: 1,
        hint: "Прапорець Enforced (No Override) має абсолютний пріоритет над блокуванням спадкування Block Inheritance."
      },
      {
        q: "9. У чому полягає безпекова перевага використання утиліти runas (Secondary Logon)?",
        options: [
          "А) Вона пришвидшує інтернет-з'єднання",
          "Б) Реалізує принцип «Найменших привілеїв» (Least Privilege): адміністратор працює як звичайний користувач, відкриваючи з підвищеними правами лише окремі процеси",
          "В) Автоматично робить копію реєстру",
          "Г) Запобігає введенню неправильного пароля"
        ],
        correct: 1,
        hint: "RunAs виключає ризик зараження системи зловмисним ПЗ під час повсякденної роботи з поштою та вебом під акаунтом Administrator."
      },
      {
        q: "10. Чому Windows Server вимагає явної авторизації DHCP-сервера в Active Directory перед початком роботи?",
        options: [
          "А) Щоб заплатити ліцензійний збір Microsoft",
          "Б) Для запобігання появі неавторизованих (Rogue) DHCP-серверів, здатних підмінити шлюз чи DNS і перехоплювати трафік (Man-in-the-Middle)",
          "В) Оскільки без цього не запуститься мережева карта",
          "Г) Це вимоги файлової системи NTFS"
        ],
        correct: 1,
        hint: "Rogue DHCP може видати фальшивий Default Gateway і перенаправити весь банківський та конфіденційний трафік на хакерський вузол."
      },
      {
        q: "11. Яка роль FSMO у межах лісу контролює розширення схеми та визначення класів/атрибутів об'єктів?",
        options: [
          "А) Domain Naming Master",
          "Б) Schema Master",
          "В) RID Master",
          "Г) Infrastructure Master"
        ],
        correct: 1,
        hint: "Schema Master єдина на весь ліс Active Directory та дозволяє змінювати структуру класів та атрибутів (наприклад, при встановленні MS Exchange)."
      },
      {
        q: "12. Яке призначення таблиці sd_table у структурі бази даних NTDS.dit?",
        options: [
          "А) Зберігання списку паролів адміністраторів",
          "Б) Single-Instance Store для дескрипторів безпеки ACL, що заощаджує 40-60% місця на диску завдяки усуненню дублювання однакових прав",
          "В) Зберігання файлів резервних копій GPO",
          "Г) Таблиця маршрутизації мережевих пакетів"
        ],
        correct: 1,
        hint: "sd_table зберігає дескриптори безпеки в єдиному екземплярі (Single-Instance Store), оптимізуючи дисковий простір NTDS.dit."
      },
      {
        q: "13. Що таке спеціальна група безпеки DnsUpdateProxy та який потенційний ризик вона несе?",
        options: [
          "А) Прискорює кеш DNS у 10 разів",
          "Б) Дозволяє DHCP-серверу реєструвати записи без дескриптора власності (ACL), що у випадку зламу сервера дає змогу підмінити будь-який незахищений запис у зоні",
          "В) Шифрує DNS-запити алгоритмом TLS",
          "Г) Використовується виключно для друку документів"
        ],
        correct: 1,
        hint: "Члени DnsUpdateProxy не стають власниками створених DNS-записів, тому інші вузли можуть перезаписати їх, якщо не налаштовано ACL."
      },
      {
        q: "14. Що містить спільна системна папка SYSVOL на контролері домену?",
        options: [
          "А) Тільки файли встановлення Windows Server",
          "Б) Скрипти входу (Logon Scripts) та шаблони групових політик GPT (файли Registry.pol, GUID політик), які реплікуються між усіма DC",
          "В) Папки робочих столів усіх користувачів",
          "Г) Журнали аудиту антивіруса"
        ],
        correct: 1,
        hint: "SYSVOL реплікується службою DFS-R (або FRS) і містить фізичну частину GPO (GPT) та logon-скрипти netlogon."
      },
      {
        q: "15. Чому файли бази даних NTDS.dit та журнали транзакцій edb.log рекомендується виносити на окремі фізичні накопичувачі?",
        options: [
          "А) Щоб обійти обмеження за розміром файлу 4 ГБ у системі FAT32",
          "Б) Для підвищення продуктивності (послідовний запис логів WAL не конкурує з випадковим читанням/записом бази) та надійності при відмові диска",
          "В) Це заборонено правилами Microsoft",
          "Г) Тільки для того, щоб звільнити місце на диску C:"
        ],
        correct: 1,
        hint: "Розділення дисків забезпечує максимальну швидкодію дискової підсистеми I/O та уможливлює повне відновлення після збою."
      }
    ];

    let userAnswers = {};

    function renderQuiz() {
      const container = document.getElementById('quizContainer');
      if (!container) return;
      container.innerHTML = `
        <div style="background: var(--bg-tertiary); border: 1px solid var(--border-color); border-radius: 10px; padding: 16px 20px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
          <div>
            <div style="font-size: 15px; font-weight: 700; color: var(--accent-cyan);">📊 Прогрес тестування:</div>
            <div id="quizScoreText" style="font-size: 13.5px; color: var(--text-secondary); margin-top: 2px;">
              Відповідей: 0 із 15 | Правильних: 0 (0%)
            </div>
          </div>
          <button onclick="resetQuiz()" class="filter-btn" style="padding: 8px 16px; border-radius: 6px; font-size: 13px;">🔄 Почати заново</button>
        </div>
      `;

      quizData.forEach((item, qIdx) => {
        const card = document.createElement('div');
        card.className = 'quiz-card';
        card.innerHTML = `
          <div class="quiz-question">${item.q}</div>
          <div class="quiz-options">
            ${item.options.map((opt, oIdx) => `
              <button class="quiz-option-btn" id="qbtn_${qIdx}_${oIdx}" onclick="checkAnswer(${qIdx}, ${oIdx})">${opt}</button>
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
      if (userAnswers[qIdx] !== undefined) return;
      userAnswers[qIdx] = selectedOption;

      const q = quizData[qIdx];
      const buttons = document.querySelectorAll(`[id^="qbtn_${qIdx}_"]`);
      const feedback = document.getElementById(`quiz-feedback-${qIdx}`);

      buttons.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === q.correct) {
          btn.classList.add('correct');
        } else if (idx === selectedOption) {
          btn.classList.add('wrong');
        }
      });
      if (feedback) feedback.style.display = 'block';

      updateScore();
    }

    function updateScore() {
      const answered = Object.keys(userAnswers).length;
      let correct = 0;
      for (const [qIdx, sel] of Object.entries(userAnswers)) {
        if (sel === quizData[qIdx].correct) correct++;
      }
      const pct = answered > 0 ? Math.round((correct / 15) * 100) : 0;
      const scoreEl = document.getElementById('quizScoreText');
      if (scoreEl) {
        scoreEl.innerHTML = `Відповідей: <strong>${answered}</strong> із 15 | Правильних: <strong style="color:var(--accent-green);">${correct}</strong> (${pct}%)`;
      }
    }

    function resetQuiz() {
      userAnswers = {};
      renderQuiz();
    }

    // 11. Glossary Data - 25 Essential Concepts (Using clean double-quoted strings)
    const glossaryData = [
      { cat: "ad", term: "Active Directory Domain Services (AD DS)", desc: "Розподілена ієрархічна служба каталогів Windows Server для централізованої автентифікації, авторизації та зберігання відомостей про ресурси підприємства." },
      { cat: "sec", term: "Kerberos v5 (RFC 4120)", desc: "Протокол мережевої автентифікації на основі квитків (TGT, Service Ticket) та довіреної третьої сторони (KDC), що усуває передачу паролів мережею." },
      { cat: "ad", term: "FSMO (Flexible Single Master Operation)", desc: "5 ролей операцій з одним хазяїном (Schema Master, Domain Naming, PDC Emulator, RID, Infrastructure Master) для запобігання колізіям у розподіленій базі даних." },
      { cat: "ad", term: "Schema Master (Хазяїн схеми)", desc: "Єдина на весь ліс AD роль FSMO, яка контролює право внесення змін та доповнень до класів та атрибутів об'єктів каталогу." },
      { cat: "ad", term: "Domain Naming Master (Хазяїн іменування)", desc: "Роль рівня лісу FSMO, що відповідає за додавання або видалення доменів та розділів каталогів у просторі лісу." },
      { cat: "ad", term: "PDC Emulator (Емулятор первинного контролера)", desc: "Роль FSMO рівня домену: головне джерело часу (NTP), обробка термінових змін паролів, сумісність з NT 4.0 та пріоритетне редагування GPO." },
      { cat: "ad", term: "RID Master (Хазяїн відносних ідентифікаторів)", desc: "Роль FSMO, яка виділяє пули відносних ідентифікаторів (RID) для створення нових користувачів, груп та комп'ютерів із унікальними SID." },
      { cat: "ad", term: "Infrastructure Master (Хазяїн інфраструктури)", desc: "Роль FSMO, що синхронізує міждоменні посилання та оновлює імена об'єктів при зміні членства в групах інших доменів." },
      { cat: "net", term: "DORA (Discover, Offer, Request, Acknowledge)", desc: "Чотириетапна послідовність отримання конфігурації TCP/IP за протоколом DHCP (порти 67/68 UDP)." },
      { cat: "net", term: "SRV-записи DNS (RFC 2782)", desc: "Службові записи в DNS (_ldap, _kerberos), які повідомляють клієнтам порти та імена контролерів домену для підключення." },
      { cat: "net", term: "AD-Integrated DNS Zone", desc: "Зона DNS, збережена в базі NTDS.dit, що забезпечує мультимайстерну реплікацію та безпечне динамічне оновлення Secure Dynamic Update." },
      { cat: "net", term: "DnsUpdateProxy", desc: "Спеціальна група безпеки AD, члени якої реєструють записи DNS без захисних дескрипторів власності для спрощення взаємодії DHCP та застарілих клієнтів." },
      { cat: "ad", term: "NTDS.dit", desc: "Основний файл реляційної бази даних Active Directory, побудований на рушії ESE (JET Blue) з повною відповідністю вимогам ACID." },
      { cat: "ad", term: "datatable", desc: "Головна таблиця бази NTDS.dit, де кожен рядок представляє об'єкт каталогу, а стовпці — його схематичні атрибути." },
      { cat: "ad", term: "link_table", desc: "Таблиця зв'язків у NTDS.dit для реалізації механізму Linked Value Replication (LVR) при додаванні окремих користувачів у групи." },
      { cat: "ad", term: "sd_table", desc: "Single-Instance Store для дескрипторів безпеки (DACL) у NTDS.dit, що запобігає дублюванню однакових прав і заощаджує до 50% обсягу диска." },
      { cat: "storage", term: "Effective Access (SMB vs NTFS)", desc: "Підсумкове результуюче право доступу користувача до мережевої папки, що обчислюється як найбільш суворе обмеження: min(Share, NTFS)." },
      { cat: "storage", term: "Mandatory Profile (Обов'язковий профіль)", desc: "Профіль користувача з файлом NTUSER.MAN, у якому всі внесені під час сеансу зміни знищуються після завершення роботи." },
      { cat: "storage", term: "Roaming User Profile (Переміщуваний профіль)", desc: "Профіль, що зберігається на сервері (\\\\server\\\\Profiles\\\\%username%) і завантажується на будь-який ПК у домені під час входу." },
      { cat: "sec", term: "Secondary Logon (RunAs)", desc: "Механізм Windows, що дозволяє користувачеві запускати окремий процес під обліковим записом адміністратора без зміни поточного сеансу." },
      { cat: "sec", term: "KDC (Key Distribution Center)", desc: "Служба на контролері домену, що об'єднує службу автентифікації (AS) та службу надання квитків (TGS) за стандартом Kerberos." },
      { cat: "sec", term: "TGT (Ticket Granting Ticket)", desc: "Квиток на отримання квитків, виданий KDC клієнту, зашифрований секретним ключем службового облікового запису krbtgt." },
      { cat: "sec", term: "SYSVOL", desc: "Спільна папка на всіх DC домену (C:\\\\Windows\\\\SYSVOL), де зберігаються файли GPT групових політик та скрипти входу netlogon." },
      { cat: "ad", term: "LSDOU (Local, Site, Domain, OU)", desc: "Ієрархічний порядок застосування об'єктів групових політик (GPO), де кожний наступний рівень перекриває налаштування попереднього." },
      { cat: "ad", term: "GPC vs GPT", desc: "GPC (Group Policy Container) зберігається в Active Directory і містить атрибути політики; GPT (Group Policy Template) зберігається у SYSVOL і містить фізичні налаштування." }
    ];

    function filterGlossary(cat) {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      if (event && event.currentTarget) event.currentTarget.classList.add('active');

      const list = document.getElementById('glossaryList');
      if (!list) return;
      list.innerHTML = '';
      const filtered = cat === 'all' ? glossaryData : glossaryData.filter(i => i.cat === cat);
      filtered.forEach(item => {
        const div = document.createElement('div');
        div.className = 'glossary-item';
        div.innerHTML = `<div class="glossary-term">${item.term}</div><div class="glossary-desc">${item.desc}</div>`;
        list.appendChild(div);
      });
    }

    // 12. Global Search Filter
    const searchInput = document.getElementById('globalSearch');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        const q = e.target.value.toLowerCase().trim();
        if (!q) return;

        const terms = document.querySelectorAll('.glossary-item');
        terms.forEach(t => {
          const text = t.textContent.toLowerCase();
          t.style.display = text.includes(q) ? 'block' : 'none';
        });

        if (q.length > 2) {
          const glossTab = document.querySelector('[data-tab="tab-glossary"]');
          if (glossTab) glossTab.click();
        }
      });
    }

    // 13. Initialize on Load
    document.addEventListener('DOMContentLoaded', () => {
      runSubnetCalc();
      renderQuiz();
      filterGlossary('all');
    });
    // Fallback if already loaded
    runSubnetCalc();
    renderQuiz();
    filterGlossary('all');
"""

# Replace script block in html
script_pattern = re.compile(r'<script>.*?</script>', re.DOTALL)
new_html = script_pattern.sub(f"<script>{clean_js}\n  </script>", html)

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(new_html)

# Extract and run node check
script_match = re.search(r'<script>(.*?)</script>', new_html, re.DOTALL)
test_js_path = r"C:\Users\andri_gxiil3v\.gemini\antigravity\brain\1a5da84c-8d99-4296-a69e-e7ee78079827\scratch\check_fixed.js"
with open(test_js_path, "w", encoding="utf-8") as f:
    f.write(script_match.group(1))

res = subprocess.run(["node", "--check", test_js_path], capture_output=True, text=True)
if res.returncode == 0:
    print("SUCCESS: node --check passed with 0 errors!")
else:
    print("FAILED node check:\n", res.stderr)
