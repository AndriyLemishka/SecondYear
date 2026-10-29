# -*- coding: utf-8 -*-
import os

TARGET_FILE = r"D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\Explenation material\index.html"

# Read existing file to check structure
with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add DORA Simulator HTML in Section tab-dhcp
dora_simulator_html = """
        <!-- Simulator 3: DHCP DORA Interactive Flow -->
        <div class="simulator-container">
          <div class="simulator-header">
            <div class="simulator-title">🔄 Покроковий інтерактивний симулятор протоколу DORA</div>
            <span class="simulator-badge">UDP 67 (Server) / 68 (Client)</span>
          </div>
          <p style="margin-bottom: 14px; font-size: 13.5px; color: var(--text-secondary);">
            Натискайте на фази, щоб дослідити мережеві заголовки, адреси відправника/отримувача та службове навантаження пакетів:
          </p>
          <div class="kerberos-flow">
            <button class="kerberos-step-btn active dora-btn" onclick="showDoraStep(1)">1. DHCPDISCOVER</button>
            <button class="kerberos-step-btn dora-btn" onclick="showDoraStep(2)">2. DHCPOFFER</button>
            <button class="kerberos-step-btn dora-btn" onclick="showDoraStep(3)">3. DHCPREQUEST</button>
            <button class="kerberos-step-btn dora-btn" onclick="showDoraStep(4)">4. DHCPACK</button>
          </div>
          <div id="doraDetails" class="kerberos-display" style="margin-top: 14px;">
            <strong>Фаза 1: DHCPDISCOVER.</strong> Клієнт Windows 10 (MAC: 08-00-27-28-FF-B2) надсилає широкомовний запит Broadcast на 255.255.255.255:67 із порту 68. Джерело IP: 0.0.0.0. Зміст: пошук доступних DHCP-серверів у локальному широкомовному домені.
          </div>
        </div>
"""

# Replace in tab-dhcp before <div class="grid-2">
if '<div class="grid-2">' in content and 'doraDetails' not in content:
    target_pos = content.find('<!-- MODULE 7: DHCP -->')
    if target_pos != -1:
        grid_pos = content.find('<div class="grid-2">', target_pos)
        if grid_pos != -1:
            content = content[:grid_pos] + dora_simulator_html + "\n" + content[grid_pos:]

# 2. Add DORA JS logic
dora_js = """
    // Simulator 3: DHCP DORA interactive logic
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
"""

# 3. Replace quizData with complete 15 questions and add score counter logic
quiz_15_js = """
    // Full 15 Academic Quiz Questions for Defense Preparation
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
          "В) Виникне збій групових політок (GPO Error 1002)",
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
      if (userAnswers[qIdx] !== undefined) return; // already answered
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
"""

# Replace quizData block in content
quiz_start = content.find('// Quiz Questions Data')
quiz_end = content.find('// Glossary Data')

if quiz_start != -1 and quiz_end != -1:
    content = content[:quiz_start] + quiz_15_js + "\n\n    " + content[quiz_end:]

# Add DORA JS before // Simulator 6: ESE Table Inspector
ese_pos = content.find('// Simulator 6: ESE Table Inspector')
if ese_pos != -1 and 'showDoraStep' not in content:
    content = content[:ese_pos] + dora_js + "\n    " + content[ese_pos:]

# 4. Expand Glossary to 25 items
expanded_glossary_js = """// Glossary Data - 25 Essential Concepts
    const glossaryData = [
      { cat: 'ad', term: 'Active Directory Domain Services (AD DS)', desc: 'Розподілена ієрархічна служба каталогів Windows Server для централізованої автентифікації, авторизації та зберігання відомостей про ресурси підприємства.' },
      { cat: 'sec', term: 'Kerberos v5 (RFC 4120)', desc: 'Протокол мережевої автентифікації на основі квитків (TGT, Service Ticket) та довіреної третьої сторони (KDC), що усуває передачу паролів мережею.' },
      { cat: 'ad', term: 'FSMO (Flexible Single Master Operation)', desc: '5 ролей операцій з одним хазяїном (Schema Master, Domain Naming, PDC Emulator, RID, Infrastructure Master) для запобігання колізіям у розподіленій базі даних.' },
      { cat: 'ad', term: 'Schema Master (Хазяїн схеми)', desc: 'Єдина на весь ліс AD роль FSMO, яка контролює право внесення змін та доповнень до класів та атрибутів об'єктів каталогу.' },
      { cat: 'ad', term: 'Domain Naming Master (Хазяїн іменування)', desc: 'Роль рівня лісу FSMO, що відповідає за додавання або видалення доменів та розділів каталогів у просторі лісу.' },
      { cat: 'ad', term: 'PDC Emulator (Емулятор первинного контролера)', desc: 'Роль FSMO рівня домену: головне джерело часу (NTP), обробка термінових змін паролів, сумісність з NT 4.0 та пріоритетне редагування GPO.' },
      { cat: 'ad', term: 'RID Master (Хазяїн відносних ідентифікаторів)', desc: 'Роль FSMO, яка виділяє пули відносних ідентифікаторів (RID) для створення нових користувачів, груп та комп'ютерів із унікальними SID.' },
      { cat: 'ad', term: 'Infrastructure Master (Хазяїн інфраструктури)', desc: 'Роль FSMO, що синхронізує міждоменні посилання та оновлює імена об'єктів при зміні членства в групах інших доменів.' },
      { cat: 'net', term: 'DORA (Discover, Offer, Request, Acknowledge)', desc: 'Чотириетапна послідовність отримання конфігурації TCP/IP за протоколом DHCP (порти 67/68 UDP).' },
      { cat: 'net', term: 'SRV-записи DNS (RFC 2782)', desc: 'Службові записи в DNS (_ldap, _kerberos), які повідомляють клієнтам порти та імена контролерів домену для підключення.' },
      { cat: 'net', term: 'AD-Integrated DNS Zone', desc: 'Зона DNS, збережена в базі NTDS.dit, що забезпечує мультимайстерну реплікацію та безпечне динамічне оновлення Secure Dynamic Update.' },
      { cat: 'net', term: 'DnsUpdateProxy', desc: 'Спеціальна група безпеки AD, члени якої реєструють записи DNS без захисних дескрипторів власності для спрощення взаємодії DHCP та застарілих клієнтів.' },
      { cat: 'ad', term: 'NTDS.dit', desc: 'Основний файл реляційної бази даних Active Directory, побудований на рушії ESE (JET Blue) з повною відповідністю вимогам ACID.' },
      { cat: 'ad', term: 'datatable', desc: 'Головна таблиця бази NTDS.dit, де кожен рядок представляє об'єкт каталогу, а стовпці — його схематичні атрибути.' },
      { cat: 'ad', term: 'link_table', desc: 'Таблиця зв'язків у NTDS.dit для реалізації механізму Linked Value Replication (LVR) при додаванні окремих користувачів у групи.' },
      { cat: 'ad', term: 'sd_table', desc: 'Single-Instance Store для дескрипторів безпеки (DACL) у NTDS.dit, що запобігає дублюванню однакових прав і заощаджує до 50% обсягу диска.' },
      { cat: 'storage', term: 'Effective Access (SMB vs NTFS)', desc: 'Підсумкове результуюче право доступу користувача до мережевої папки, що обчислюється як найбільш суворе обмеження: min(Share, NTFS).' },
      { cat: 'storage', term: 'Mandatory Profile (Обов\'язковий профіль)', desc: 'Профіль користувача з файлом NTUSER.MAN, у якому всі внесені під час сеансу зміни знищуються після завершення роботи.' },
      { cat: 'storage', term: 'Roaming User Profile (Переміщуваний профіль)', desc: 'Профіль, що зберігається на сервері (\\\\server\\Profiles\\%username%) і завантажується на будь-який ПК у домені під час входу.' },
      { cat: 'sec', term: 'Secondary Logon (RunAs)', desc: 'Механізм Windows, що дозволяє користувачеві запускати окремий процес під обліковим записом адміністратора без зміни поточного сеансу.' },
      { cat: 'sec', term: 'KDC (Key Distribution Center)', desc: 'Служба на контролері домену, що об'єднує службу автентифікації (AS) та службу надання квитків (TGS) за стандартом Kerberos.' },
      { cat: 'sec', term: 'TGT (Ticket Granting Ticket)', desc: 'Квиток на отримання квитків, виданий KDC клієнту, зашифрований секретним ключем службового облікового запису krbtgt.' },
      { cat: 'sec', term: 'SYSVOL', desc: 'Спільна папка на всіх DC домену (C:\\Windows\\SYSVOL), де зберігаються файли GPT групових політик та скрипти входу netlogon.' },
      { cat: 'ad', term: 'LSDOU (Local, Site, Domain, OU)', desc: 'Ієрархічний порядок застосування об'єктів групових політик (GPO), де кожний наступний рівень перекриває налаштування попереднього.' },
      { cat: 'ad', term: 'GPC vs GPT', desc: 'GPC (Group Policy Container) зберігається в Active Directory і містить атрибути політики; GPT (Group Policy Template) зберігається у SYSVOL і містить фізичні налаштування.' }
    ];"""

gloss_start = content.find('// Glossary Data')
gloss_end = content.find('function filterGlossary(cat)')
if gloss_start != -1 and gloss_end != -1:
    content = content[:gloss_start] + expanded_glossary_js + "\n\n    " + content[gloss_end:]

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully updated {TARGET_FILE}. New size: {len(content)} bytes")
