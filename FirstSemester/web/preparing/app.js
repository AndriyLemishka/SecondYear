// ==========================================================================
// CHARGEUA PREPARING PORTAL — APP.JS
// Інтерактивна логіка навчального порталу підготовки до Лаб 5
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initReadingProgress();
  initSearch();
  initAccordions();
  initCopyButtons();
  initQuiz();
});

// 1. Керування темами (Dark/Light)
function initTheme() {
  const themeBtn = document.getElementById('theme-toggle');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const savedTheme = localStorage.getItem('chargeua_prep_theme') || (prefersDark ? 'dark' : 'light');
  
  applyTheme(savedTheme);

  if (themeBtn) {
    themeBtn.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      applyTheme(newTheme);
      localStorage.setItem('chargeua_prep_theme', newTheme);
    });
  }
}

function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  const themeBtn = document.getElementById('theme-toggle');
  if (themeBtn) {
    themeBtn.innerHTML = theme === 'dark' 
      ? '☀️ <span class="hide-sm">Світла</span>' 
      : '🌙 <span class="hide-sm">Темна</span>';
  }
}

// 2. Смуга прогресу читання
function initReadingProgress() {
  const progressBar = document.getElementById('reading-progress');
  if (!progressBar) return;

  window.addEventListener('scroll', () => {
    const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    progressBar.style.width = scrolled + '%';
  });
}

// 3. Інтерактивний пошук по порталу
function initSearch() {
  const searchInput = document.getElementById('global-search');
  if (!searchInput) return;

  searchInput.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase().trim();
    const accordionItems = document.querySelectorAll('.accordion-item');
    const conceptCards = document.querySelectorAll('.concept-card');

    // Фільтрація контрольних питань
    accordionItems.forEach(item => {
      const text = item.textContent.toLowerCase();
      if (text.includes(query)) {
        item.style.display = '';
        if (query.length > 2) {
          item.classList.add('active'); // авто-розкриття при співпаданні
        }
      } else {
        item.style.display = 'none';
        item.classList.remove('active');
      }
    });

    // Фільтрація концептуальних карток
    conceptCards.forEach(card => {
      const text = card.textContent.toLowerCase();
      card.style.display = text.includes(query) ? '' : 'none';
    });
  });
}

// 4. Акордеон для 20 контрольних запитань
function initAccordions() {
  const headers = document.querySelectorAll('.accordion-header');
  headers.forEach(header => {
    header.addEventListener('click', () => {
      const parent = header.closest('.accordion-item');
      const wasActive = parent.classList.contains('active');
      
      // Можна закрити/відкрити поточне
      parent.classList.toggle('active', !wasActive);
    });
  });

  // Кнопка "Розкрити всі / Згорнути всі"
  const toggleAllBtn = document.getElementById('toggle-all-questions');
  if (toggleAllBtn) {
    let allExpanded = false;
    toggleAllBtn.addEventListener('click', () => {
      allExpanded = !allExpanded;
      document.querySelectorAll('.accordion-item').forEach(item => {
        item.classList.toggle('active', allExpanded);
      });
      toggleAllBtn.textContent = allExpanded ? 'Згорнути всі' : 'Розкрити всі';
    });
  }
}

// 5. Копіювання коду
function initCopyButtons() {
  document.querySelectorAll('.code-box__copy-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const codeBlock = btn.closest('.code-box').querySelector('pre code');
      if (!codeBlock) return;
      
      navigator.clipboard.writeText(codeBlock.innerText).then(() => {
        const origText = btn.innerText;
        btn.innerText = 'Скопійовано! ✓';
        btn.style.color = '#10B981';
        setTimeout(() => {
          btn.innerText = origText;
          btn.style.color = '';
        }, 2000);
      });
    });
  });
}

// 6. Інтерактивний тест (Quiz) — 10 найважливіших питань
const quizData = [
  {
    question: "Чому на сторінці має бути лише один тег <h1>?",
    options: [
      "Бо CSS забороняє мати кілька однакових заголовків",
      "<h1> позначає головну тему всього документа для пошукових роботів та Accessibility Tree",
      "Це технічне обмеження браузерів Chromium, інакше сайт зависає",
      "Щоб шрифт автоматично не зменшувався на мобільних пристроях"
    ],
    correct: 1,
    explanation: "Правило 'One H1 per page' є золотим стандартом W3C та SEO: h1 визначає головну тему сторінки. Для внутрішніх секцій слід використовувати h2, а для карток всередині них — h3."
  },
  {
    question: "У чому полягає ключова різниця між тегами <section> та <article>?",
    options: [
      "<section> не може мати заголовок, а <article> може",
      "<article> — це самодостатня одиниця контенту, яку можна опублікувати окремо (наприклад, картка станції або стаття), а <section> — це тематичний розділ документа",
      "<section> використовується тільки з Flexbox, а <article> тільки з CSS Grid",
      "Між ними немає жодної різниці, це синоніми"
    ],
    correct: 1,
    explanation: "Згідно зі специфікацією HTML5, <article> є автономним самостійним блоком (може бути синдикований у RSS або розміщений на іншій сторінці). <section> обов'язково групує тематичний контент і повинен містити власний заголовок h2-h6."
  },
  {
    question: "Коли необхідно використовувати <button>, а коли посилання <a>?",
    options: [
      "<a> використовується тільки для посилань на сторонні сайти, а <button> — для внутрішніх",
      "<a> (з атрибутом href) використовується для навігації між сторінками або до якоря, а <button> — для виклику дій чи відправки форми",
      "Різниця лише у візуальному стилі та кольорі за замовчуванням",
      "<button> заборонено використовувати без JavaScript"
    ],
    correct: 1,
    explanation: "Золоте правило доступності: якщо користувач кудись ПЕРЕХОДИТЬ (зміна URL чи скрол до якоря) — використовуємо <a>. Якщо елемент виконує ДІЮ (розрахунок, відкриття меню, сабміт) — використовуємо <button>."
  },
  {
    question: "Що робить CSS-правило 'grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))'?",
    options: [
      "Створює фіксовані 4 колонки шириною по 280px",
      "Автоматично генерує стільки колонок, скільки поміщається в екран, з мінімальною шириною 280px та пропорційним розтягуванням",
      "Обмежує ширину сітки до 280px на мобільних телефонах",
      "Центрує одну картку на екрані"
    ],
    correct: 1,
    explanation: "Це класичний патерн респонсивного гріда: 'auto-fit' підбирає максимальну кількість колонок під ширину контейнера, а 'minmax(280px, 1fr)' гарантує, що вони не стиснуться менше 280px і пропорційно поділять вільне місце."
  },
  {
    question: "Чому змінні в :root слід називати '--color-primary', а не '--blue'?",
    options: [
      "Браузери не підтримують англійські назви кольорів у змінних",
      "Семантична назва описує призначення кольору в інтерфейсі, дозволяючи змінити бренд-колір або тему без зміни назв змінних по всьому CSS",
      "Це вимога консорціуму W3C тільки для десктопних браузерів",
      "Щоб зменшити вагу кінцевого CSS-файлу"
    ],
    correct: 1,
    explanation: "Назви за призначенням (role-based) забезпечують масштабованість: якщо завтра бренд оновить колір із синього на фіолетовий, вам не доведеться перейменовувати змінну '--blue: purple', а лише змінити значення '--color-primary: #7C3AED;'."
  },
  {
    question: "Для чого використовується елемент <a class='skip-link' href='#main'>?",
    options: [
      "Для переходу на головну сторінку сайту",
      "Для швидкого пропуску блоку шапки та навігації користувачами, які використовують клавіатуру або скрінрідери (WCAG 2.4.1)",
      "Це службовий скрипт для швидкого завантаження зображень",
      "Для обходу захисту Cloudflare"
    ],
    correct: 1,
    explanation: "Skip-link є обов'язковою вимогою доступності (WCAG 2.4.1 Bypass Blocks). Користувачі з клавіатурною навігацією при натисканні Tab одразу отримують можливість перейти до суті сторінки (#main), не табаючи через десятки пунктів меню."
  },
  {
    question: "У чому різниця між 'auto-fit' та 'auto-fill' у CSS Grid?",
    options: [
      "'auto-fit' розтягує наявні колонки на всю ширину, закриваючи пусті слоти, тоді як 'auto-fill' зберігає порожні фантомні треки",
      "'auto-fit' підходить лише для Flexbox, а 'auto-fill' для Grid",
      "Жодної різниці, це взаємозамінні ключові слова",
      "'auto-fill' швидше рендериться у Safari"
    ],
    correct: 0,
    explanation: "Якщо елементів менше, ніж вміщується колонок: auto-fit розтягує наявні картки на всю доступну ширину (collapse empty tracks), а auto-fill залишає порожні місця для гіпотетичних нових елементів."
  },
  {
    question: "Як працює функція 'clamp(2rem, 5vw, 3.25rem)'?",
    options: [
      "Вона обирає випадкове значення з трьох вказаних",
      "Встановлює гнучке значення 5vw, але обмежує його знизу мінімумом 2rem, а зверху максимумом 3.25rem",
      "Працює лише всередині медіа-запитів @media",
      "Множить 2rem на 5vw"
    ],
    correct: 1,
    explanation: "clamp(MIN, PREFERRED, MAX) дозволяє робити ідеальну fluid-типографіку: розмір плавно зростає разом із шириною вікна (5vw), але ніколи не стане меншим за 2rem чи більшим за 3.25rem."
  },
  {
    question: "Чому клас '.visually-hidden' не можна реалізувати як 'display: none'?",
    options: [
      "'display: none' повністю видаляє елемент із дерева доступності, і скрінрідери його не озвучують",
      "'display: none' видає помилку у валідаторі W3C",
      "'display: none' не підтримується на мобільних пристроях",
      "Це зламає CSS Grid макет"
    ],
    correct: 0,
    explanation: "Властивість 'display: none' або 'visibility: hidden' вилучає вузол з Accessibility Tree. Патерн '.visually-hidden' приховує елемент візуально (через clip-path, width: 1px), залишаючи його доступним для незрячих користувачів зі скрінрідерами."
  },
  {
    question: "Що означає, коли кнопка в статусному рядку VS Code показує '⊘ Port : 5500'?",
    options: [
      "Виникла помилка порту 5500, сервер заблоковано",
      "Live Server успішно запущено і він веде локальну трансляцію сайту на порті 5500",
      "Потрібно оновити розширення Ritwick Dey",
      "Сервер працює в аварійному режимі без CSS"
    ],
    correct: 1,
    explanation: "У розширенні Live Server стан 'Go Live' означає готовність до старту, а напис 'Port : 5500' з піктограмою антени підтверджує, що локальний вебсервер уже активний і відкрив порт 5500."
  }
];

let currentQuestion = 0;
let userScore = 0;
let answered = false;

function initQuiz() {
  const quizBox = document.getElementById('quiz-box');
  if (!quizBox) return;

  renderQuestion();

  document.getElementById('quiz-next-btn').addEventListener('click', () => {
    if (!answered) return;
    currentQuestion++;
    if (currentQuestion < quizData.length) {
      renderQuestion();
    } else {
      showQuizResults();
    }
  });

  document.getElementById('quiz-restart-btn')?.addEventListener('click', () => {
    currentQuestion = 0;
    userScore = 0;
    answered = false;
    document.getElementById('quiz-result-view').style.display = 'none';
    document.getElementById('quiz-question-view').style.display = 'block';
    renderQuestion();
  });
}

function renderQuestion() {
  answered = false;
  const q = quizData[currentQuestion];
  
  // Progress
  const progressPercent = ((currentQuestion + 1) / quizData.length) * 100;
  document.getElementById('quiz-progress-fill').style.width = progressPercent + '%';
  document.getElementById('quiz-counter').textContent = `Питання ${currentQuestion + 1} з ${quizData.length}`;
  
  // Title
  document.getElementById('quiz-question-text').textContent = q.question;
  
  // Explanation & Next button
  const expBox = document.getElementById('quiz-explanation');
  expBox.style.display = 'none';
  const nextBtn = document.getElementById('quiz-next-btn');
  nextBtn.disabled = true;
  nextBtn.textContent = (currentQuestion === quizData.length - 1) ? 'Завершити тест' : 'Наступне питання →';

  // Options
  const optionsContainer = document.getElementById('quiz-options');
  optionsContainer.innerHTML = '';

  q.options.forEach((optText, index) => {
    const btn = document.createElement('button');
    btn.className = 'quiz-option-btn';
    btn.type = 'button';
    btn.innerHTML = `<strong>${String.fromCharCode(65 + index)}.</strong> <span>${optText}</span>`;
    
    btn.addEventListener('click', () => handleOptionClick(index, btn, q));
    optionsContainer.appendChild(btn);
  });
}

function handleOptionClick(selectedIndex, clickedBtn, q) {
  if (answered) return;
  answered = true;

  const allBtns = document.querySelectorAll('.quiz-option-btn');
  allBtns.forEach(b => b.disabled = true);

  const expBox = document.getElementById('quiz-explanation');
  expBox.style.display = 'block';

  if (selectedIndex === q.correct) {
    userScore++;
    clickedBtn.classList.add('selected-correct');
    expBox.innerHTML = `<strong>Правильно! 🎉</strong><br>${q.explanation}`;
    expBox.style.borderColor = '#10B981';
  } else {
    clickedBtn.classList.add('selected-wrong');
    allBtns[q.correct].classList.add('selected-correct');
    expBox.innerHTML = `<strong>Не зовсім так. ⚠️</strong><br>${q.explanation}`;
    expBox.style.borderColor = '#EF4444';
  }

  document.getElementById('quiz-next-btn').disabled = false;
}

function showQuizResults() {
  document.getElementById('quiz-question-view').style.display = 'none';
  const resultView = document.getElementById('quiz-result-view');
  resultView.style.display = 'block';

  const scoreText = document.getElementById('quiz-final-score');
  const msgText = document.getElementById('quiz-final-msg');
  
  scoreText.textContent = `${userScore} / ${quizData.length}`;

  if (userScore >= 9) {
    msgText.innerHTML = "🏆 <strong>Блискуче! 100 балів!</strong><br>Ви досконало володієте всіма тонкощами семантики HTML5, CSS Grid/Flexbox та вимогами WCAG 2.2. Захист пройде ідеально!";
  } else if (userScore >= 7) {
    msgText.innerHTML = "👍 <strong>Дуже добрий результат!</strong><br>Ви маєте міцне розуміння матеріалу. Перегляньте ще раз пару запитань викладача у блоці вище, і будете повністю готові до будь-яких додаткових питань!";
  } else {
    msgText.innerHTML = "📖 <strong>Потрібно трохи повторити.</strong><br>Рекомендуємо детальніше перечитати розділи 'Як, що і навіщо' та 'Анатомія коду', після чого пройти тест ще раз!";
  }
}
