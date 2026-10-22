# -*- coding: utf-8 -*-
import os

html_content = '''<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ЛР №4 Чисельні методи | Персональний тренажер захисту (Варіант 12)</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- KaTeX for formulas -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js" onload="renderAllMath();"></script>
  <style>
    @keyframes softPulse {
      0%, 100% { opacity: 0.9; transform: scale(1); }
      50% { opacity: 1; transform: scale(1.02); }
    }
    .pulse-btn { animation: softPulse 2.5s infinite ease-in-out; }
    .tab-active { 
      background-color: rgba(6, 182, 212, 0.15); 
      border-bottom: 3px solid #06b6d4; 
      color: #22d3ee !important; 
      font-weight: 700; 
    }
    .flashcard { perspective: 1000px; }
    .flashcard-inner { transition: transform 0.5s cubic-bezier(0.4, 0.2, 0.2, 1); transform-style: preserve-3d; }
    .flashcard.flipped .flashcard-inner { transform: rotateY(180deg); }
    .front, .back { backface-visibility: hidden; -webkit-backface-visibility: hidden; }
    .back { transform: rotateY(180deg); }
    code { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }
  </style>
</head>
<body class="bg-[#0A0F1D] text-slate-100 min-h-screen font-sans antialiased selection:bg-cyan-500 selection:text-black">

  <!-- TOP APP BAR -->
  <header class="bg-[#11192E]/95 backdrop-blur-md border-b border-slate-800 sticky top-0 z-50 px-4 lg:px-8 py-3.5 shadow-xl">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-4">
      <div class="flex items-center space-x-3.5">
        <div class="w-11 h-11 rounded-2xl bg-gradient-to-tr from-cyan-500 to-indigo-600 flex items-center justify-center font-black text-white shadow-lg shadow-cyan-500/25 text-xl tracking-wider">
          ЧМ
        </div>
        <div>
          <div class="flex items-center space-x-2">
            <h1 class="text-base sm:text-lg font-black text-white tracking-wide">ЛР №4: Чисельне розв’язування СЛАР</h1>
            <span class="bg-cyan-950 text-cyan-300 text-xs px-2.5 py-0.5 rounded-full border border-cyan-500/40 font-mono font-bold">Варіант 12</span>
          </div>
          <p class="text-xs text-slate-400">НУ «Львівська політехніка» • Кафедра САПР • Викладач: Чумакевич В.В.</p>
        </div>
      </div>

      <!-- STUDENT & TARGET BADGES -->
      <div class="flex items-center space-x-3 text-xs sm:text-sm">
        <div class="bg-slate-900/90 px-3.5 py-2 rounded-xl border border-slate-800 flex items-center space-x-2.5">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
          <span class="text-slate-300">Студент: <strong class="text-white font-semibold">Андрій Лемішка (ПП-24)</strong></span>
        </div>
        <div class="bg-cyan-950/80 px-3.5 py-2 rounded-xl border border-cyan-500/40 text-cyan-200">
          Точна відповідь: <strong class="text-emerald-400 font-mono text-sm">a = b = c = d = e = 1.2</strong>
        </div>
      </div>
    </div>

    <!-- NAVIGATION TABS -->
    <nav class="max-w-7xl mx-auto mt-3 flex space-x-2 sm:space-x-3 overflow-x-auto text-xs sm:text-sm font-medium pt-2 border-t border-slate-800/80">
      <button onclick="switchTab('simple')" id="tab-simple" class="tab-btn px-4 py-2 rounded-xl text-slate-300 hover:text-white transition flex items-center gap-2 whitespace-nowrap tab-active">
        <span>💡</span> Поясни на пальцях («Я не шарю»)
      </button>
      <button onclick="switchTab('dialogue')" id="tab-dialogue" class="tab-btn px-4 py-2 rounded-xl text-slate-400 hover:text-white transition flex items-center gap-2 whitespace-nowrap">
        <span>🗣️</span> Симулятор захисту (Що казати)
      </button>
      <button onclick="switchTab('visual')" id="tab-visual" class="tab-btn px-4 py-2 rounded-xl text-slate-400 hover:text-white transition flex items-center gap-2 whitespace-nowrap">
        <span>⚡</span> Покроковий симулятор
      </button>
      <button onclick="switchTab('paper')" id="tab-paper" class="tab-btn px-4 py-2 rounded-xl text-slate-400 hover:text-white transition flex items-center gap-2 whitespace-nowrap">
        <span>📝</span> Як рахувати «на листочку»
      </button>
      <button onclick="switchTab('cards')" id="tab-cards" class="tab-btn px-4 py-2 rounded-xl text-slate-400 hover:text-white transition flex items-center gap-2 whitespace-nowrap">
        <span>❓</span> 9 карток-шпаргалок
      </button>
      <button onclick="switchTab('theory')" id="tab-theory" class="tab-btn px-4 py-2 rounded-xl text-slate-400 hover:text-white transition flex items-center gap-2 whitespace-nowrap">
        <span>📚</span> Теорія з методички (с. 13-15)
      </button>
    </nav>
  </header>

  <main class="max-w-7xl mx-auto p-4 sm:p-6 lg:p-8 space-y-6">

    <!-- ========================================== -->
    <!-- TAB 1: ПОЯСНИ НА ПАЛЬЦЯХ (ДЛЯ ЧАЙНИКІВ)   -->
    <!-- ========================================== -->
    <section id="pane-simple" class="tab-pane space-y-6">
      
      <!-- HERO MOTIVATION BANNER -->
      <div class="bg-gradient-to-r from-cyan-950/70 via-slate-900 to-indigo-950/60 border border-cyan-500/30 rounded-3xl p-6 sm:p-8 shadow-2xl relative overflow-hidden">
        <div class="absolute -right-12 -bottom-12 w-64 h-64 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none"></div>
        <div class="max-w-3xl space-y-3">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs font-semibold">
            <span>🛡️</span> Спокійно: ти розберешся за 5 хвилин
          </div>
          <h2 class="text-xl sm:text-2xl font-black text-white leading-tight">
            Не хвилюйся, тут немає нічого страшного!
          </h2>
          <p class="text-sm sm:text-base text-slate-300 leading-relaxed font-normal">
            Вся ця лабораторна робота — це просто <strong>пошук 5 невідомих чисел (a, b, c, d, e)</strong> за 5 підказками-рівняннями. І найприємніше: у нашому варіанті 12 усі 5 чисел виявляються однаковими і дорівнюють <strong class="text-emerald-400 text-lg font-mono">1.2</strong>!
          </p>
        </div>
      </div>

      <!-- 4 SIMPLE METAPHORS -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">

        <!-- METAPHOR 1: WHAT IS SLAR -->
        <div class="bg-[#11192E] border border-slate-800 hover:border-cyan-500/40 transition rounded-2xl p-6 space-y-4 shadow-lg">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-xl">
              🛒
            </div>
            <div>
              <h3 class="text-base font-bold text-white">1. Що таке СЛАР простою мовою?</h3>
              <p class="text-xs text-slate-400">Аналогія з покупками в магазині</p>
            </div>
          </div>
          <div class="text-xs sm:text-sm text-slate-300 space-y-2 leading-relaxed">
            <p>
              Уявіть, що ви зайшли в супермаркет і купили 5 різних товарів: <span class="font-mono text-cyan-300 font-bold">a, b, c, d, e</span> (наприклад: яблуко, банан, сік, шоколад, хліб).
            </p>
            <p>
              Вам дали 5 чеків з різними комбінаціями покупок і загальними сумами. Ваше завдання — дізнатися, <strong>скільки коштує кожен товар окремо</strong>.
            </p>
            <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800 text-xs font-mono text-emerald-400 font-semibold">
              Результат: кожен товар коштує рівно 1.20 грн!
            </div>
          </div>
        </div>

        <!-- METAPHOR 2: DIRECT VS ITERATIVE -->
        <div class="bg-[#11192E] border border-slate-800 hover:border-amber-500/40 transition rounded-2xl p-6 space-y-4 shadow-lg">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-xl">
              🎯
            </div>
            <div>
              <h3 class="text-base font-bold text-white">2. Прямий метод чи Ітераційний?</h3>
              <p class="text-xs text-slate-400">Два абсолютно різні підходи до життя</p>
            </div>
          </div>
          <div class="text-xs sm:text-sm text-slate-300 space-y-2.5 leading-relaxed">
            <p>
              • <strong class="text-cyan-300">Прямий метод (Гаусс):</strong> Це як розв'язати головоломку за чіткою математичною формулою. Раз-два-три — і в кінці ми отримали точну відповідь 1.2 без жодних наближень.
            </p>
            <p>
              • <strong class="text-amber-300">Ітераційний метод (Зейдель):</strong> Це як підбирати фокус на об'єктиві або прицілюватися в тирі. Спочатку ми беремо нулі: <code class="text-slate-400">[0, 0, 0, 0, 0]</code>. На першому кроці отримуємо неточні числа, на другому ближче, на сьомому майже влучили, а на 21-му кроці похибка менша ніж 0.0000000001!
            </p>
          </div>
        </div>

        <!-- METAPHOR 3: WHY KHALECKIY IS COOL -->
        <div class="bg-[#11192E] border border-slate-800 hover:border-purple-500/40 transition rounded-2xl p-6 space-y-4 shadow-lg">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-xl bg-purple-500/10 border border-purple-500/30 flex items-center justify-center text-xl">
              ⚡
            </div>
            <div>
              <h3 class="text-base font-bold text-white">3. Чому схема Халецького крутіша за Гаусса?</h3>
              <p class="text-xs text-slate-400">Секрет швидкості (45 дій проти 68)</p>
            </div>
          </div>
          <div class="text-xs sm:text-sm text-slate-300 space-y-2 leading-relaxed">
            <p>
              Звичайний Гаусс постійно переписує і змінює всю таблицю чисел. Це довго.
            </p>
            <p>
              <strong>Халецький придумав трюк (LU-розклад):</strong> розбити матрицю на дві трикутні (нижню C і верхню B). Це дозволяє розв'язати систему всього за <strong class="text-emerald-400">45 операцій</strong> замість <strong class="text-rose-400">68</strong> у схемі єдиного ділення. Менше рахувати — швидша програма!
            </p>
          </div>
        </div>

        <!-- METAPHOR 4: WHY ZEIDEL WINS -->
        <div class="bg-[#11192E] border border-slate-800 hover:border-emerald-500/40 transition rounded-2xl p-6 space-y-4 shadow-lg">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-xl">
              🚀
            </div>
            <div>
              <h3 class="text-base font-bold text-white">4. У чому головна фішка методу Зейделя?</h3>
              <p class="text-xs text-slate-400">Головне запитання викладача на захисті!</p>
            </div>
          </div>
          <div class="text-xs sm:text-sm text-slate-300 space-y-2 leading-relaxed">
            <p>
              Уявіть, що ви вгадуєте 5 чисел.
            </p>
            <p>
              У <em>простій ітерації</em>: ви знайшли нове число <span class="text-cyan-300 font-bold">a</span>, але вам заборонено ним користуватися, поки ви не дорахуєте решту зі старими нулями.
            </p>
            <p>
              <strong>А в Зейделя:</strong> щойно ви дізналися свіже <span class="text-cyan-300 font-bold">a</span>, ви <strong class="text-emerald-400">відразу ж підставляєте його для пошуку b</strong>! Через це Зейдель летить до правильної відповіді <strong>вдвічі швидше</strong>.
            </p>
          </div>
        </div>

      </div>

      <!-- CHEAT CARD: SUMMARY TO MEMORIZE -->
      <div class="bg-gradient-to-r from-slate-900 to-[#11192E] p-6 rounded-2xl border border-slate-800 space-y-3">
        <h3 class="text-base font-bold text-cyan-300 flex items-center gap-2">
          <span>🧠</span> 3 речі, які треба просто запам'ятати (і ти здаси на 5):
        </h3>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs sm:text-sm font-mono">
          <div class="bg-slate-950/80 p-3.5 rounded-xl border border-slate-800">
            <span class="text-slate-400 block mb-1 font-sans">1. Точна відповідь:</span>
            <span class="text-emerald-400 font-bold text-base">a=b=c=d=e = 1.2</span>
          </div>
          <div class="bg-slate-950/80 p-3.5 rounded-xl border border-slate-800">
            <span class="text-slate-400 block mb-1 font-sans">2. Кількість ітерацій Зейделя:</span>
            <span class="text-cyan-400 font-bold text-base">21 ітерація (при 10⁻¹⁰)</span>
          </div>
          <div class="bg-slate-950/80 p-3.5 rounded-xl border border-slate-800">
            <span class="text-slate-400 block mb-1 font-sans">3. Чому Зейдель зійшовся:</span>
            <span class="text-amber-300 font-bold text-base">Діагональне переважання</span>
          </div>
        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- TAB 2: СИМУЛЯТОР ЗАХИСТУ (ЩО КАЗАТИ)        -->
    <!-- ========================================== -->
    <section id="pane-dialogue" class="tab-pane hidden space-y-6">

      <!-- 30-SEC INTRO SPEECH -->
      <div class="bg-[#11192E] border border-cyan-500/40 rounded-3xl p-6 sm:p-8 shadow-2xl relative">
        <div class="flex flex-wrap items-center justify-between gap-3 mb-4">
          <h2 class="text-lg sm:text-xl font-bold text-cyan-300 flex items-center gap-2">
            <span>🗣️</span> Твій вступний спіч: що казати, коли викладач скаже «Розповідай» (30 сек)
          </h2>
          <div class="flex items-center space-x-2">
            <button onclick="speakSpeech()" class="px-4 py-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-bold transition shadow-lg shadow-cyan-600/30 flex items-center gap-1.5 pulse-btn">
              🔊 Озвучити спіч
            </button>
            <button onclick="copySpeech()" id="copySpeechBtn" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs transition">
              📋 Скопіювати
            </button>
          </div>
        </div>

        <div id="speechText" class="bg-slate-950/90 rounded-2xl p-5 border border-slate-800 text-sm sm:text-base leading-relaxed text-slate-200 space-y-3 font-normal">
          <p>
            «У 4-й лабораторній роботі я розв'язував систему з 5 лінійних алгебраїчних рівнянь варіанта 12 двома чисельними методами: прямим методом Гауса та ітераційним методом Гауса — Зейделя. Розрахунки виконано мовою Python, а динаміку наближень зведено в таблицю та графік Excel.
          </p>
          <p>
            1. <strong class="text-cyan-300">Прямим методом Гауса</strong> з вибором головного елемента знайдено точний аналітичний розв’язок: усі змінні строго дорівнюють <strong class="text-emerald-400">1,2</strong>.
          </p>
          <p>
            2. <strong class="text-cyan-300">Ітераційним методом Зейделя</strong>, стартуючи з нульового початкового наближення з високою точністю 10⁻¹⁰, розв'язок зійшовся за <strong class="text-emerald-400">21 ітерацію</strong> до тих самих значень 1,2.
          </p>
          <p>
            Побудований графік підтвердив швидку збіжність: уже після 7-ї ітерації похибка становить менше 0,0001, а лінії наближень практично зливаються на рівні 1.2 завдяки діагональному переважанню коефіцієнтів».
          </p>
        </div>
      </div>

      <!-- DIALOGUE SIMULATOR (Q&A WITH TEACHER) -->
      <div class="space-y-4">
        <h3 class="text-base font-bold text-amber-300 flex items-center gap-2">
          <span>💬</span> Запитання викладача в ході захисту (натисни питання, щоб побачити відповідь):
        </h3>

        <div class="space-y-3">

          <details class="group bg-[#11192E] border border-slate-800 rounded-2xl p-4 transition open:border-cyan-500/40">
            <summary class="flex items-center justify-between cursor-pointer font-semibold text-sm sm:text-base text-slate-200 group-open:text-cyan-300 select-none">
              <span>❓ 1. «А чому у вас всі змінні вийшли рівно по 1.2? Це правильно?»</span>
              <span class="text-xs text-slate-500 group-open:rotate-180 transition">▼</span>
            </summary>
            <div class="mt-3 pt-3 border-t border-slate-800 text-xs sm:text-sm text-slate-300 leading-relaxed space-y-2">
              <p>
                <strong>Твоя відповідь:</strong> «Так, це абсолютно правильно! У вихідній методичці на стор. 17 через вузьку колонку два коефіцієнти випадково перенеслися в кінець сусідніх рядків. Після відновлення правильної верстки система стала симетричною і гармонійною, а прямий метод Гауса підтвердив точний розв'язок: $a = b = c = d = e = 1{,}2$. Якщо підставити $1{,}2$ у кожне з 5 рівнянь, виходить точна тотожність: $6{,}0 = 6{,}0$, $0{,}6 = 0{,}6$ тощо».
              </p>
            </div>
          </details>

          <details class="group bg-[#11192E] border border-slate-800 rounded-2xl p-4 transition open:border-cyan-500/40">
            <summary class="flex items-center justify-between cursor-pointer font-semibold text-sm sm:text-base text-slate-200 group-open:text-cyan-300 select-none">
              <span>❓ 2. «Чим метод Зейделя відрізняється від простої ітерації?» (ГОЛОВНЕ ПИТАННЯ!)</span>
              <span class="text-xs text-slate-500 group-open:rotate-180 transition">▼</span>
            </summary>
            <div class="mt-3 pt-3 border-t border-slate-800 text-xs sm:text-sm text-slate-300 leading-relaxed space-y-2">
              <p>
                <strong>Твоя відповідь:</strong> «У методі простої ітерації всі нові значення на новому кроці рахуються лише за старими значеннями попереднього кроку. А в методі Зейделя, щойно ми обчислили нове значення компоненти (наприклад, $x_1$), ми <strong>відразу ж підставляємо його в наступне рівняння на цій же самій ітерації</strong>. Через це метод Зейделя збігається приблизно вдвічі швидше і вимагає менше пам'яті».
              </p>
            </div>
          </details>

          <details class="group bg-[#11192E] border border-slate-800 rounded-2xl p-4 transition open:border-cyan-500/40">
            <summary class="flex items-center justify-between cursor-pointer font-semibold text-sm sm:text-base text-slate-200 group-open:text-cyan-300 select-none">
              <span>❓ 3. «Що таке схема єдиного ділення в методі Гаусса?»</span>
              <span class="text-xs text-slate-500 group-open:rotate-180 transition">▼</span>
            </summary>
            <div class="mt-3 pt-3 border-t border-slate-800 text-xs sm:text-sm text-slate-300 leading-relaxed space-y-2">
              <p>
                <strong>Твоя відповідь:</strong> «Це алгоритм прямого ходу Гаусса, де на кожному кроці весь рядок один раз ділиться на свій діагональний елемент, щоб зробити його одиницею ($a_{kk}=1$). Це прискорює обчислення (бо ділення повільніше за множення) і позбавляє необхідності ділити під час зворотного ходу. Для $n=5$ вона потребує близько 68 операцій».
              </p>
            </div>
          </details>

          <details class="group bg-[#11192E] border border-slate-800 rounded-2xl p-4 transition open:border-cyan-500/40">
            <summary class="flex items-center justify-between cursor-pointer font-semibold text-sm sm:text-base text-slate-200 group-open:text-cyan-300 select-none">
              <span>❓ 4. «А що таке схема Халецького і скільки там операцій?»</span>
              <span class="text-xs text-slate-500 group-open:rotate-180 transition">▼</span>
            </summary>
            <div class="mt-3 pt-3 border-t border-slate-800 text-xs sm:text-sm text-slate-300 leading-relaxed space-y-2">
              <p>
                <strong>Твоя відповідь:</strong> «Це компактний LU-розклад матриці коефіцієнтів $A = C \\cdot B$, де $C$ — нижня трикутна, а $B$ — верхня трикутна з одиницями на діагоналі. Система розв'язується у два простих кроки: $Cy = d$ (прямий хід), потім $Bx = y$ (зворотний хід). За формулою методички вона потребує лише $n(2n-1) = 45$ операцій для $n=5$, що на третину швидше за звичайного Гаусса».
              </p>
            </div>
          </details>

          <details class="group bg-[#11192E] border border-slate-800 rounded-2xl p-4 transition open:border-cyan-500/40">
            <summary class="flex items-center justify-between cursor-pointer font-semibold text-sm sm:text-base text-slate-200 group-open:text-cyan-300 select-none">
              <span>❓ 5. «Чому саме 21 ітерація, а не 5 чи 100?»</span>
              <span class="text-xs text-slate-500 group-open:rotate-180 transition">▼</span>
            </summary>
            <div class="mt-3 pt-3 border-t border-slate-800 text-xs sm:text-sm text-slate-300 leading-relaxed space-y-2">
              <p>
                <strong>Твоя відповідь:</strong> «Тому що в програмі було встановлено надзвичайно високу точність: десять знаків після коми (\\(\\delta = 10^{-10}\\)). Якщо взяти звичайну інженерну точність \\(10^{-4}\\) (до 4-го знака), то Зейдель завершує роботу всього за 7–8 ітерацій».
              </p>
            </div>
          </details>

        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- TAB 3: ПОКРОКОВИЙ СИМУЛЯТОР                -->
    <!-- ========================================== -->
    <section id="pane-visual" class="tab-pane hidden space-y-6">

      <!-- SYSTEM EQUATIONS -->
      <div class="bg-[#11192E] border border-slate-800 rounded-2xl p-5 shadow-lg space-y-3">
        <h3 class="text-sm font-bold text-cyan-300 flex items-center justify-between">
          <span>📐 Система 5 рівнянь твого варіанта 12:</span>
          <span class="text-xs text-slate-400 font-mono">Шукаємо: a, b, c, d, e</span>
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs font-mono text-slate-300 bg-slate-950/70 p-3 rounded-xl border border-slate-800">
          <div>1) &nbsp;1.0·a + 1.0·b + 1.0·c + 1.0·d + 1.0·e = <span class="text-emerald-400 font-bold">6.0</span></div>
          <div>2) &nbsp;0.0·a + <span class="text-amber-300 font-bold">2.1·b</span> + 0.0·c - 0.9·d - 0.7·e = <span class="text-emerald-400 font-bold">0.6</span></div>
          <div>3) -0.5·a - 0.9·b + <span class="text-amber-300 font-bold">1.7·c</span> - 0.4·d - 0.5·e = <span class="text-emerald-400 font-bold">-0.72</span></div>
          <div>4) &nbsp;0.0·a - 0.5·b - 0.5·c + <span class="text-amber-300 font-bold">2.4·d</span> - 0.3·e = <span class="text-emerald-400 font-bold">1.32</span></div>
          <div>5) -0.2·a - 0.7·b - 0.6·c - 0.6·d + <span class="text-amber-300 font-bold">1.8·e</span> = <span class="text-emerald-400 font-bold">-0.36</span></div>
        </div>
      </div>

      <!-- CONTROLS & STEPPER -->
      <div class="bg-[#11192E] border border-slate-800 rounded-3xl p-6 shadow-xl space-y-6">
        <div class="flex flex-wrap items-center justify-between gap-4">
          <div>
            <h2 class="text-lg font-bold text-white flex items-center gap-2">
              <span>🚀</span> Інтерактивний рух змінних до 1.2
            </h2>
            <p class="text-xs text-slate-400">Натискай кнопки або рухай повзунок, щоб бачити розрахунок на кожному кроці</p>
          </div>
          <div class="flex items-center space-x-2">
            <button onclick="prevStep()" class="bg-slate-800 hover:bg-slate-700 text-white px-3.5 py-2 rounded-xl text-xs font-semibold transition border border-slate-700">
              ◀ Крок назад
            </button>
            <button onclick="nextStep()" class="bg-cyan-600 hover:bg-cyan-500 text-white px-4 py-2 rounded-xl text-xs font-semibold shadow-lg shadow-cyan-600/30 transition">
              Наступний крок ▶
            </button>
            <button onclick="toggleAutoPlay()" id="playBtn" class="bg-emerald-600 hover:bg-emerald-500 text-white px-3.5 py-2 rounded-xl text-xs font-semibold transition">
              ▶ Авто-гра
            </button>
            <button onclick="resetSimulation()" class="bg-slate-800 hover:bg-slate-700 text-slate-400 px-3 py-2 rounded-xl text-xs transition">
              Скинути
            </button>
          </div>
        </div>

        <!-- RANGE SLIDER -->
        <div class="space-y-1.5">
          <div class="flex justify-between text-xs text-slate-400 font-mono">
            <span>Ітерація Зейделя: <strong id="stepLabel" class="text-cyan-400 text-base font-bold">0</strong> / 21</span>
            <span id="errorLabel">Поточна похибка max: <strong class="text-amber-400 font-mono">1.200000</strong></span>
          </div>
          <input type="range" min="0" max="21" value="0" id="stepRange" oninput="setStep(parseInt(this.value))" class="w-full accent-cyan-400 cursor-pointer">
        </div>

        <!-- 5 BIG TILES -->
        <div class="grid grid-cols-2 sm:grid-cols-5 gap-3">
          <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 text-center">
            <span class="text-xs text-slate-400 font-mono">Змінна a</span>
            <div id="val-a" class="text-lg sm:text-xl font-bold font-mono text-cyan-400 mt-1">0.000000</div>
            <div id="diff-a" class="text-[11px] text-slate-500 font-mono mt-0.5">відхилення: -1.2</div>
          </div>
          <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 text-center">
            <span class="text-xs text-slate-400 font-mono">Змінна b</span>
            <div id="val-b" class="text-lg sm:text-xl font-bold font-mono text-amber-400 mt-1">0.000000</div>
            <div id="diff-b" class="text-[11px] text-slate-500 font-mono mt-0.5">відхилення: -1.2</div>
          </div>
          <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 text-center">
            <span class="text-xs text-slate-400 font-mono">Змінна c</span>
            <div id="val-c" class="text-lg sm:text-xl font-bold font-mono text-emerald-400 mt-1">0.000000</div>
            <div id="diff-c" class="text-[11px] text-slate-500 font-mono mt-0.5">відхилення: -1.2</div>
          </div>
          <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 text-center">
            <span class="text-xs text-slate-400 font-mono">Змінна d</span>
            <div id="val-d" class="text-lg sm:text-xl font-bold font-mono text-rose-400 mt-1">0.000000</div>
            <div id="diff-d" class="text-[11px] text-slate-500 font-mono mt-0.5">відхилення: -1.2</div>
          </div>
          <div class="col-span-2 sm:col-span-1 bg-slate-950 p-4 rounded-2xl border border-slate-800 text-center">
            <span class="text-xs text-slate-400 font-mono">Змінна e</span>
            <div id="val-e" class="text-lg sm:text-xl font-bold font-mono text-purple-400 mt-1">0.000000</div>
            <div id="diff-e" class="text-[11px] text-slate-500 font-mono mt-0.5">відхилення: -1.2</div>
          </div>
        </div>

        <!-- EXPLANATION IN PLAIN WORDS -->
        <div class="bg-slate-950/80 p-4 rounded-2xl border border-slate-800 text-xs sm:text-sm font-sans space-y-1.5">
          <div class="text-cyan-400 font-bold flex items-center gap-1.5">
            <span>🔍</span> Пояснення кроку №<span id="stepFormulaNum">0</span>:
          </div>
          <div id="formulaExplanation" class="text-slate-300 leading-relaxed">
            Початковий стан: усі змінні дорівнюють нулю. Натисни «Наступний крок ▶», щоб побачити розрахунок.
          </div>
        </div>
      </div>

      <!-- CANVAS CONVERGENCE CHART -->
      <div class="bg-[#11192E] border border-slate-800 rounded-3xl p-6 shadow-xl space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-3">
          <h3 class="text-base font-bold text-white flex items-center gap-2">
            <span>📈</span> Графік збіжності: як коливання затухають біля 1.2
          </h3>
          <div class="flex items-center space-x-3 text-xs">
            <span class="inline-flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-cyan-400"></span> a</span>
            <span class="inline-flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-amber-400"></span> b</span>
            <span class="inline-flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span> c</span>
            <span class="inline-flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-rose-400"></span> d</span>
            <span class="inline-flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-purple-400"></span> e</span>
            <span class="inline-flex items-center gap-1"><span class="w-3 h-0.5 bg-white border-t border-dashed"></span> точне 1.2</span>
          </div>
        </div>
        <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800">
          <canvas id="convergenceCanvas" width="900" height="380" class="w-full h-auto"></canvas>
        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- TAB 4: НА ЛИСТОЧКУ РУЧКОЮ                 -->
    <!-- ========================================== -->
    <section id="pane-paper" class="tab-pane hidden space-y-6">
      <div class="bg-[#11192E] border border-slate-800 rounded-3xl p-6 sm:p-8 shadow-xl space-y-6">
        <div>
          <h2 class="text-lg sm:text-xl font-bold text-amber-300 flex items-center gap-2">
            <span>📝</span> Як порахувати ручкою на листочку (якщо викладач дасть калькулятор)
          </h2>
          <p class="text-xs sm:text-sm text-slate-400 mt-1">Викладач часто каже: «А порахуй мені першу ітерацію на листочку прямо зараз». Ось готова шпаргалка:</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="bg-slate-950 p-5 rounded-2xl border border-slate-800 space-y-3">
            <h3 class="text-sm font-bold text-cyan-300 border-b border-slate-800 pb-2">1. Виписуємо 5 простих формул:</h3>
            <div class="space-y-2 text-xs font-mono text-slate-200">
              <div class="p-2 rounded bg-slate-900 border border-slate-800"><span class="text-cyan-400 font-bold">a</span> = (6.0 - b - c - d - e) / 1.0</div>
              <div class="p-2 rounded bg-slate-900 border border-slate-800"><span class="text-amber-400 font-bold">b</span> = (0.6 + 0.9·d + 0.7·e) / 2.1</div>
              <div class="p-2 rounded bg-slate-900 border border-slate-800"><span class="text-emerald-400 font-bold">c</span> = (-0.72 + 0.5·a + 0.9·b + 0.4·d + 0.5·e) / 1.7</div>
              <div class="p-2 rounded bg-slate-900 border border-slate-800"><span class="text-rose-400 font-bold">d</span> = (1.32 + 0.5·b + 0.5·c + 0.3·e) / 2.4</div>
              <div class="p-2 rounded bg-slate-900 border border-slate-800"><span class="text-purple-400 font-bold">e</span> = (-0.36 + 0.2·a + 0.7·b + 0.6·c + 0.6·d) / 1.8</div>
            </div>
          </div>

          <div class="bg-slate-950 p-5 rounded-2xl border border-slate-800 space-y-3">
            <h3 class="text-sm font-bold text-emerald-300 border-b border-slate-800 pb-2">2. Підставляємо числа 1-ї ітерації:</h3>
            <div class="space-y-2 font-mono text-xs text-slate-300 leading-relaxed">
              <p>• Стартуємо з нулів: <span class="text-slate-500">a=0, b=0, c=0, d=0, e=0</span></p>
              <p>• <strong class="text-cyan-400">a⁽¹⁾</strong> = 6.0 - 0 - 0 - 0 - 0 = <strong class="text-cyan-300">6.0</strong></p>
              <p>• <strong class="text-amber-400">b⁽¹⁾</strong> = (0.6 + 0 + 0) / 2.1 = 0.6 / 2.1 ≈ <strong class="text-amber-300">0.2857</strong></p>
              <p>• <strong class="text-emerald-400">c⁽¹⁾</strong> = (-0.72 + 0.5·<strong class="text-cyan-300">6.0</strong> + 0.9·<strong class="text-amber-300">0.2857</strong>) / 1.7 ≈ <strong class="text-emerald-300">1.4924</strong></p>
              <p>• <strong class="text-rose-400">d⁽¹⁾</strong> = (1.32 + 0.5·<strong class="text-amber-300">0.2857</strong> + 0.5·<strong class="text-emerald-300">1.4924</strong>) / 2.4 ≈ <strong class="text-rose-300">0.9204</strong></p>
              <p>• <strong class="text-purple-400">e⁽¹⁾</strong> = (-0.36 + 0.2·<strong class="text-cyan-300">6.0</strong> + 0.7·<strong class="text-amber-300">0.2857</strong> + 0.6·<strong class="text-emerald-300">1.4924</strong> + 0.6·<strong class="text-rose-300">0.9204</strong>) / 1.8 ≈ <strong class="text-purple-300">1.3821</strong></p>
              <div class="p-2.5 bg-emerald-950/60 border border-emerald-500/30 rounded-xl text-emerald-300 text-xs font-sans">
                💡 <strong>Головна фраза:</strong> «Бачите, при обчисленні c я вже підставив щойно знайдені свіжі 6.0 та 0.2857. Саме тому це метод Зейделя!»
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 5: 9 КАРТОК-ШПАРГАЛОК (FLASHCARDS)      -->
    <!-- ========================================== -->
    <section id="pane-cards" class="tab-pane hidden space-y-6">
      <div class="bg-[#11192E] border border-slate-800 rounded-3xl p-6 sm:p-8 shadow-xl space-y-6">
        <div class="flex flex-wrap items-center justify-between gap-4">
          <div>
            <h2 class="text-lg sm:text-xl font-bold text-amber-300 flex items-center gap-2">
              <span>❓</span> 9 карток-шпаргалок за методичкою
            </h2>
            <p class="text-xs text-slate-400">Клікни на картку — вона повернеться і покаже готову коротку відповідь для викладача</p>
          </div>
          <div class="flex items-center space-x-3">
            <button onclick="speakCurrentCard()" class="text-xs bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 px-3 py-1.5 rounded-xl transition flex items-center gap-1.5">
              🔊 Озвучити картку
            </button>
            <div class="text-xs text-slate-400 font-mono">
              Картка <span id="cardCounter" class="text-cyan-400 font-bold">1</span> з 9
            </div>
          </div>
        </div>

        <!-- FLASHCARD COMPONENT -->
        <div class="max-w-2xl mx-auto">
          <div id="flashcard" onclick="flipCard()" class="flashcard w-full h-80 sm:h-88 cursor-pointer select-none">
            <div id="flashcardInner" class="flashcard-inner w-full h-full relative rounded-3xl shadow-2xl">
              <!-- FRONT -->
              <div class="front absolute inset-0 bg-gradient-to-br from-[#1C2541] to-[#0D1424] border-2 border-cyan-500/40 rounded-3xl p-6 sm:p-8 flex flex-col justify-between">
                <div class="flex items-center justify-between text-xs text-cyan-400 font-mono">
                  <span>Контрольне запитання №<span id="cardNumFront">1</span></span>
                  <span class="bg-cyan-950 px-2.5 py-1 rounded-full border border-cyan-500/30">Натисни щоб перевернути 🔄</span>
                </div>
                <div id="cardQuestion" class="text-base sm:text-lg font-bold text-white text-center px-4 leading-relaxed my-auto">
                  1. Які існують типи методів розв'язання систем лінійних рівнянь (СЛАР) і чим вони відрізняються?
                </div>
                <div class="text-[11px] text-center text-slate-500 font-mono">
                  ЧМ лаб практикум.pdf • стор. 13-15
                </div>
              </div>

              <!-- BACK -->
              <div class="back absolute inset-0 bg-gradient-to-br from-[#0B2538] to-[#0A1628] border-2 border-emerald-500/50 rounded-3xl p-6 sm:p-8 flex flex-col justify-between overflow-y-auto">
                <div class="flex items-center justify-between text-xs text-emerald-400 font-mono">
                  <span>Готова відповідь для викладача</span>
                  <span class="bg-emerald-950 px-2.5 py-1 rounded-full border border-emerald-500/30">Назад 🔄</span>
                </div>
                <div id="cardAnswer" class="text-xs sm:text-sm text-slate-200 leading-relaxed my-auto font-normal space-y-2">
                  <!-- JS populated -->
                </div>
                <div class="text-[11px] text-center text-slate-400 italic">
                  💡 Сказати своїми словами на захисті
                </div>
              </div>
            </div>
          </div>

          <!-- CARD CONTROLS -->
          <div class="flex justify-center items-center space-x-4 mt-6">
            <button onclick="prevCard()" class="bg-slate-800 hover:bg-slate-700 text-white px-4 py-2 rounded-xl text-xs font-semibold border border-slate-700 transition">
              ◀ Попередня
            </button>
            <button onclick="flipCard()" class="bg-cyan-600 hover:bg-cyan-500 text-white px-6 py-2 rounded-xl text-xs font-semibold shadow-lg shadow-cyan-600/30 transition">
              Перевернути картку 🔄
            </button>
            <button onclick="nextCard()" class="bg-slate-800 hover:bg-slate-700 text-white px-4 py-2 rounded-xl text-xs font-semibold border border-slate-700 transition">
              Наступна ▶
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 6: ОФІЦІЙНА ТЕОРІЯ З МЕТОДИЧКИ         -->
    <!-- ========================================== -->
    <section id="pane-theory" class="tab-pane hidden space-y-6">
      <div class="bg-[#11192E] border border-slate-800 rounded-3xl p-6 sm:p-8 shadow-xl space-y-6">
        <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800 pb-4">
          <div>
            <h2 class="text-lg sm:text-xl font-bold text-cyan-300 flex items-center gap-2">
              <span>📚</span> Академічна теорія за посібником «ЧМ лаб практикум.pdf» (с. 13-15)
            </h2>
            <p class="text-xs text-slate-400 mt-1">Офіційні формули кафедри САПР для перевірки викладачем</p>
          </div>
          <span class="bg-cyan-950 text-cyan-300 px-3 py-1 rounded-full border border-cyan-500/40 text-xs font-mono">
            ЧМ лаб практикум.pdf
          </span>
        </div>

        <!-- 2 METHOD TYPES -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="bg-slate-950 p-5 rounded-2xl border border-slate-800 space-y-3">
            <h3 class="text-sm font-bold text-cyan-300">1. Прямі методи (п. 2.1)</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              Дають точний розв'язок за скінченну, наперед відому кількість арифметичних дій:
            </p>
            <div class="p-3 bg-slate-900 rounded-xl border border-slate-800 text-xs space-y-2">
              <div class="flex justify-between items-center">
                <span class="text-slate-400">Схема єдиного ділення Гаусса:</span>
                <span class="math-tex font-mono text-cyan-300 font-bold" data-tex="\\frac{n(4n^2 - 3n - 4)}{6}"></span>
              </div>
              <div class="flex justify-between items-center">
                <span class="text-slate-400">Схема Халецького (LU-розклад):</span>
                <span class="math-tex font-mono text-emerald-400 font-bold" data-tex="n(2n - 1)"></span>
              </div>
              <div class="text-[11px] text-slate-400 pt-1 border-t border-slate-800">
                Для n=5: Халецький потребує <strong>45 операцій</strong> проти <strong>68</strong> у схемі єдиного ділення (на 34% швидше!).
              </div>
            </div>
          </div>

          <div class="bg-slate-950 p-5 rounded-2xl border border-slate-800 space-y-3">
            <h3 class="text-sm font-bold text-amber-300">2. Ітераційні методи (п. 2.2)</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              Будують нескінченну послідовність наближень, що прямує до точного розв'язку:
            </p>
            <div class="p-3 bg-slate-900 rounded-xl border border-slate-800 text-xs space-y-2">
              <div class="flex justify-between items-center">
                <span class="text-slate-400">Проста ітерація:</span>
                <span class="math-tex font-mono text-amber-300" data-tex="x^{k+1} = B x^k + e"></span>
              </div>
              <div class="flex justify-between items-center">
                <span class="text-slate-400">Метод Зейделя:</span>
                <span class="text-emerald-400 font-mono text-[11px]">свіжі x_1^(k+1)... негайно</span>
              </div>
              <div class="text-[11px] text-slate-400 pt-1 border-t border-slate-800">
                Умова збіжності: строге діагональне переважання (<span class="math-tex text-amber-300" data-tex="q < 1"></span>).
              </div>
            </div>
          </div>
        </div>

        <!-- SCHEMES 5 & 4 STEPS -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="bg-slate-950 p-5 rounded-2xl border border-slate-800 space-y-3">
            <h3 class="text-sm font-bold text-amber-300 border-b border-slate-800 pb-2">
              📋 Схема простої ітерації (5 кроків, с. 14)
            </h3>
            <ol class="text-xs text-slate-300 space-y-1.5 list-decimal list-inside leading-relaxed">
              <li>Обчислення матриці B і вектора e: <span class="math-tex text-cyan-300" data-tex="b_{ij} = -a_{ij}/a_{ii}"></span> (<span class="math-tex text-slate-400" data-tex="i \\ne j"></span>), <span class="math-tex text-cyan-300" data-tex="b_{ii}=0"></span>, <span class="math-tex text-cyan-300" data-tex="e_i = d_i/a_{ii}"></span>.</li>
              <li>Перевірка норми: <span class="math-tex text-amber-300" data-tex="C = \\|B\\|_1 = \\max_i \\sum |b_{ij}| < 1"></span>.</li>
              <li>Вибір початкового наближення <span class="math-tex text-cyan-300" data-tex="x^0 = e"></span>.</li>
              <li>Апріорна оцінка K за формулою (9):
                <div class="math-tex text-center my-1 text-amber-300" data-tex="K > -\\frac{1}{\\lg C} \\left[ \\lg \\|e\\|_1 - \\lg(\\Delta (1 - C)) \\right] - 1"></div>
              </li>
              <li>Реалізація K кроків до похибки <span class="math-tex text-cyan-300" data-tex="\\Delta"></span>.</li>
            </ol>
          </div>

          <div class="bg-slate-950 p-5 rounded-2xl border border-slate-800 space-y-3">
            <h3 class="text-sm font-bold text-emerald-300 border-b border-slate-800 pb-2">
              ⚡ Схема методу Зейделя (4 кроки, с. 15)
            </h3>
            <ol class="text-xs text-slate-300 space-y-1.5 list-decimal list-inside leading-relaxed">
              <li>Перевірка діагонального переважання (ф. 10):
                <div class="math-tex text-center my-1 text-emerald-300" data-tex="\\sum_{j \\ne i} |a_{ij}| \\le q |a_{ii}|, \\quad q < 1"></div>
              </li>
              <li>Обчислення норми матриці B: <span class="math-tex text-cyan-300" data-tex="C = \\max_i \\sum_{j \\ne i} |b_{ij}|"></span>.</li>
              <li>Вибір <span class="math-tex text-cyan-300" data-tex="x^0 = e"></span> (або 0), оцінка кроків K за (9).</li>
              <li>Ітераційний процес через поправки <span class="math-tex text-emerald-300" data-tex="\\delta_i^k"></span>:
                <div class="math-tex text-center my-1 text-emerald-300" data-tex="\\delta_i^k = \\sum_{j=1}^{i-1} b_{ij} x_j^{k+1} + \\sum_{j=i+1}^n b_{ij} x_j^k, \\quad x_i^{k+1} = \\delta_i^k + e_i"></div>
              </li>
            </ol>
          </div>
        </div>

        <!-- COMPLEXITY CALCULATOR -->
        <div class="bg-slate-950 p-5 rounded-2xl border border-slate-800 space-y-3">
          <h3 class="text-sm font-bold text-white flex items-center gap-2">
            <span>🧮</span> Інтерактивний калькулятор складності:
          </h3>
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs">
            <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
              <label class="block text-slate-400 mb-1">Кількість рівнянь (n):</label>
              <input type="number" id="inputN" value="5" min="2" max="50" oninput="calcComplexity()" class="w-full bg-slate-950 border border-slate-700 rounded-lg p-1.5 text-white font-mono">
            </div>
            <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 flex flex-col justify-between">
              <span class="text-slate-400">Схема єдиного ділення Гаусса:</span>
              <span id="resSingleDiv" class="text-base font-bold font-mono text-cyan-300 mt-1">68 операцій</span>
            </div>
            <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 flex flex-col justify-between">
              <span class="text-slate-400">Схема Халецького:</span>
              <span id="resKhaleckiy" class="text-base font-bold font-mono text-emerald-300 mt-1">45 операцій</span>
            </div>
          </div>
        </div>

      </div>
    </section>

  </main>

  <!-- JAVASCRIPT LOGIC -->
  <script>
    // SIMULATION DATA
    const historyData = [
      { i: 0, x: [0.0, 0.0, 0.0, 0.0, 0.0] },
      { i: 1, x: [6.0, 0.285714, 1.492437, 0.920448, 1.382073] },
      { i: 2, x: [1.919328, 1.140883, 1.368044, 1.245452, 1.328101] },
      { i: 3, x: [0.917520, 1.262180, 1.198208, 1.228593, 1.201728] },
      { i: 4, x: [1.109291, 1.212830, 1.187350, 1.200253, 1.190778] },
      { i: 5, x: [1.208788, 1.197035, 1.198362, 1.197888, 1.198574] },
      { i: 6, x: [1.208141, 1.198620, 1.200747, 1.199690, 1.200513] },
      { i: 7, x: [1.200430, 1.200038, 1.200225, 1.200119, 1.200177] },
      { i: 8, x: [1.199441, 1.200110, 1.199974, 1.200040, 1.199985] },
      { i: 9, x: [1.199891, 1.200012, 1.199979, 1.199996, 1.199985] },
      { i: 10, x: [1.200028, 1.199993, 1.199999, 1.199996, 1.199999] },
      { i: 11, x: [1.200012, 1.199998, 1.200001, 1.200000, 1.200001] },
      { i: 12, x: [1.200000, 1.200000, 1.200000, 1.200000, 1.200000] },
      { i: 13, x: [1.199999, 1.200000, 1.200000, 1.200000, 1.200000] },
      { i: 14, x: [1.200000, 1.200000, 1.200000, 1.200000, 1.200000] },
      { i: 15, x: [1.200000, 1.200000, 1.200000, 1.200000, 1.200000] },
      { i: 16, x: [1.200000, 1.200000, 1.200000, 1.200000, 1.200000] },
      { i: 17, x: [1.200000, 1.200000, 1.200000, 1.200000, 1.200000] },
      { i: 18, x: [1.200000, 1.200000, 1.200000, 1.200000, 1.200000] },
      { i: 19, x: [1.200000, 1.200000, 1.200000, 1.200000, 1.200000] },
      { i: 20, x: [1.200000, 1.200000, 1.200000, 1.200000, 1.200000] },
      { i: 21, x: [1.200000, 1.200000, 1.200000, 1.200000, 1.200000] }
    ];

    let currentStep = 0;
    let autoPlayInterval = null;

    function renderAllMath() {
      if (typeof katex === 'undefined') return;
      document.querySelectorAll('.math-tex').forEach(el => {
        try {
          const tex = el.getAttribute('data-tex') || el.textContent;
          katex.render(tex, el, { throwOnError: false });
        } catch(e) {}
      });
    }

    function setStep(step) {
      if (step < 0) step = 0;
      if (step > 21) step = 21;
      currentStep = step;

      document.getElementById('stepRange').value = currentStep;
      document.getElementById('stepLabel').innerText = currentStep;
      document.getElementById('stepFormulaNum').innerText = currentStep;

      const vars = ['a', 'b', 'c', 'd', 'e'];
      const curX = historyData[currentStep].x;
      let maxDiff = 0;

      for (let i = 0; i < 5; ++i) {
        const val = curX[i];
        const diff = val - 1.2;
        if (Math.abs(diff) > maxDiff) maxDiff = Math.abs(diff);

        document.getElementById('val-' + vars[i]).innerText = val.toFixed(6);
        const diffEl = document.getElementById('diff-' + vars[i]);
        diffEl.innerText = (diff >= 0 ? '+' : '') + diff.toFixed(6);
        if (Math.abs(diff) < 0.0001) {
          diffEl.className = 'text-[11px] text-emerald-400 font-mono mt-0.5 font-bold';
        } else {
          diffEl.className = 'text-[11px] text-slate-500 font-mono mt-0.5';
        }
      }

      document.getElementById('errorLabel').innerHTML = `Поточна похибка max: <strong class="text-amber-400 font-mono">${maxDiff.toFixed(6)}</strong>`;

      const expDiv = document.getElementById('formulaExplanation');
      if (currentStep === 0) {
        expDiv.innerHTML = 'Початковий стан: усі змінні дорівнюють нулю. Натисни «Наступний крок ▶», щоб виконати 1-й крок.';
      } else if (currentStep === 1) {
        expDiv.innerHTML = '<strong>Крок 1:</strong> Знайшли перше наближення a=6.0, далі для b підставили нулі (0.2857), а для c вже підставили свіжі 6.0 та 0.2857! Бачите, як змінні почали прокидатися?';
      } else if (currentStep === 2) {
        expDiv.innerHTML = '<strong>Крок 2:</strong> a різко падає з 6.0 до 1.919, а інші змінні вирівнюються навколо 1.2.';
      } else if (currentStep <= 5) {
        expDiv.innerHTML = `<strong>Крок ${currentStep}:</strong> Коливання затухають: a=${curX[0].toFixed(3)}, b=${curX[1].toFixed(3)}, c=${curX[2].toFixed(3)}, d=${curX[3].toFixed(3)}, e=${curX[4].toFixed(3)}. Вони все ближче до 1.200!`;
      } else if (currentStep < 21) {
        expDiv.innerHTML = `<strong>Крок ${currentStep}:</strong> Відхилення вже менші за 0.0001. Візуально на графіку це вже чисте 1.200.`;
      } else {
        expDiv.innerHTML = '<strong>Крок 21: ТОЧНІСТЬ 10⁻¹⁰ ДОСЯГНУТА!</strong> Програма зупинилася, тому що всі змінні стали строго рівними 1.2000000000.';
      }

      drawConvergenceChart(currentStep);
    }

    function nextStep() { setStep(currentStep + 1); }
    function prevStep() { setStep(currentStep - 1); }
    function resetSimulation() {
      if (autoPlayInterval) toggleAutoPlay();
      setStep(0);
    }

    function toggleAutoPlay() {
      const btn = document.getElementById('playBtn');
      if (autoPlayInterval) {
        clearInterval(autoPlayInterval);
        autoPlayInterval = null;
        btn.innerText = '▶ Авто-гра';
        btn.classList.replace('bg-rose-600', 'bg-emerald-600');
      } else {
        btn.innerText = '⏸ Пауза';
        btn.classList.replace('bg-emerald-600', 'bg-rose-600');
        autoPlayInterval = setInterval(() => {
          if (currentStep >= 21) {
            toggleAutoPlay();
          } else {
            setStep(currentStep + 1);
          }
        }, 500);
      }
    }

    // TAB SWITCHING
    function switchTab(name) {
      document.querySelectorAll('.tab-pane').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('tab-active'));

      document.getElementById('pane-' + name).classList.remove('hidden');
      document.getElementById('tab-' + name).classList.add('tab-active');

      if (name === 'visual') {
        drawConvergenceChart(currentStep);
      }
      renderAllMath();
    }

    // COMPLEXITY CALCULATOR
    function calcComplexity() {
      const n = parseInt(document.getElementById('inputN').value) || 5;
      const singleDiv = Math.round((n * (4 * n * n - 3 * n - 4)) / 6);
      const khaleckiy = n * (2 * n - 1);
      document.getElementById('resSingleDiv').innerText = singleDiv + ' операцій';
      document.getElementById('resKhaleckiy').innerText = khaleckiy + ' операцій';
    }

    // CANVAS CONVERGENCE CHART
    function drawConvergenceChart(highlightIter = -1) {
      const canvas = document.getElementById('convergenceCanvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width;
      const h = canvas.height;

      ctx.clearRect(0, 0, w, h);

      const padL = 50, padR = 30, padT = 30, padB = 40;
      const chartW = w - padL - padR;
      const chartH = h - padT - padB;

      const maxIter = 10;
      const minY = 0.0;
      const maxY = 6.2;

      function getX(i) { return padL + (i / maxIter) * chartW; }
      function getY(val) { return padT + (1 - (val - minY) / (maxY - minY)) * chartH; }

      // Grid
      ctx.strokeStyle = '#1e293b';
      ctx.lineWidth = 1;
      for (let yVal = 0; yVal <= 6; yVal += 1) {
        const y = getY(yVal);
        ctx.beginPath();
        ctx.moveTo(padL, y);
        ctx.lineTo(w - padR, y);
        ctx.stroke();

        ctx.fillStyle = '#64748b';
        ctx.font = '11px monospace';
        ctx.textAlign = 'right';
        ctx.fillText(yVal.toFixed(1), padL - 10, y + 4);
      }

      for (let i = 0; i <= maxIter; ++i) {
        const x = getX(i);
        ctx.beginPath();
        ctx.moveTo(x, padT);
        ctx.lineTo(x, h - padB);
        ctx.stroke();

        ctx.fillStyle = '#94a3b8';
        ctx.font = '11px monospace';
        ctx.textAlign = 'center';
        ctx.fillText(i, x, h - padB + 18);
      }

      // Exact reference line (1.2)
      const exactY = getY(1.2);
      ctx.strokeStyle = '#ffffff';
      ctx.setLineDash([5, 5]);
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(padL, exactY);
      ctx.lineTo(w - padR, exactY);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 11px sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('x = 1.2 (Точний розв’язок)', padL + 10, exactY - 6);

      const colors = ['#22d3ee', '#fbbf24', '#34d399', '#fb7185', '#c084fc'];

      for (let varIdx = 0; varIdx < 5; ++varIdx) {
        ctx.strokeStyle = colors[varIdx];
        ctx.lineWidth = 2.2;
        ctx.beginPath();
        for (let i = 0; i <= maxIter; ++i) {
          const val = historyData[i].x[varIdx];
          const px = getX(i);
          const py = getY(val);
          if (i === 0) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();

        for (let i = 0; i <= maxIter; ++i) {
          const val = historyData[i].x[varIdx];
          const px = getX(i);
          const py = getY(val);
          ctx.fillStyle = (i === highlightIter) ? '#ffffff' : colors[varIdx];
          ctx.beginPath();
          ctx.arc(px, py, (i === highlightIter) ? 6 : 4, 0, Math.PI * 2);
          ctx.fill();
        }
      }

      if (highlightIter >= 0 && highlightIter <= maxIter) {
        const hx = getX(highlightIter);
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
        ctx.setLineDash([3, 3]);
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(hx, padT);
        ctx.lineTo(hx, h - padB);
        ctx.stroke();
        ctx.setLineDash([]);
      }
    }

    // 9 FLASHCARDS
    const flashcards = [
      {
        q: "1. Які існують типи методів розв'язання систем лінійних рівнянь (СЛАР) і чим вони відрізняються?",
        a: "<strong>Прямі (точні) методи:</strong> дають можливість дістати розв'язок за скінченну, наперед відому кількість операцій (як метод Гаусса). Похибка виникає тільки через машинне заокруглення.<br><br><strong>Ітераційні методи:</strong> будують ланцюжок наближень X(0), X(1)..., який крок за кроком наближається до розв'язку. Зупиняються при досягненні потрібної точності Δ.",
        voice: "Методи розв'язування СЛАР поділяються на прямі та ітераційні. Прямі дають точний розв'язок за фіксовану кількість операцій, а ітераційні наближаються до нього покроково."
      },
      {
        q: "2. Які методи належать до прямих методів розв'язування СЛАР за методичкою?",
        a: "У методичці наведено два прямі методи:<br>1. <strong>Метод Гаусса за схемою єдиного ділення</strong> (потребує близько 68 операцій для n=5);<br>2. <strong>Метод Гаусса за схемою Халецького</strong> (потребує лише 45 операцій для n=5).",
        voice: "До прямих методів за методичкою належать метод Гаусса за схемою єдиного ділення та метод Гаусса за схемою Халецького."
      },
      {
        q: "3. Який алгоритм розв'язування СЛАР методом Гаусса за схемою Халецького?",
        a: "Матрицю A розкладають на дві трикутні: <strong>A = C · B</strong>, де C — нижня трикутна, B — верхня трикутна з одиницями на діагоналі.<br>1. <strong>Прямий хід:</strong> розв'язують систему C · y = d і знаходять вектор y зверху вниз.<br>2. <strong>Зворотний хід:</strong> розв'язують B · x = y і знаходять x знизу вгору.",
        voice: "За схемою Халецького матрицю розкладають у добуток Це помножити на Бе. Прямий хід розв'язує Це на ігрек дорівнює де, а зворотний Бе на ікс дорівнює ігрек."
      },
      {
        q: "4. Які методи належать до ітераційних методів розв'язування СЛАР?",
        a: "Згідно з методичкою (розділ 2.2):<br>1. <strong>Метод простої ітерації</strong> (п. 2.2.1);<br>2. <strong>Метод Зейделя</strong> (п. 2.2.2).",
        voice: "До ітераційних методів за нашою методичкою належать метод простої ітерації та метод Зейделя."
      },
      {
        q: "5. Як записується ітераційний процес методу простої ітерації?",
        a: "Система Ax = d перетворюється до канонічного вигляду <strong>x = Bx + e</strong>, де елементи матриці B: b_ij = -a_ij/a_ii (на діагоналі b_ii = 0), а вектор e_i = d_i/a_ii.<br>Формула ітерації: <strong>x^(k+1) = B · x^k + e</strong>.",
        voice: "Система зводиться до вигляду ікс дорівнює бе помножити на ікс плюс є, а ітераційний процес записується рекурентно: ікс ка плюс перший дорівнює бе на ікс катий плюс є."
      },
      {
        q: "6. Як оцінюється необхідна кількість ітерацій K для досягнення потрібної точності?",
        a: "За формулою (9) методички через норму матриці C = ||B||₁ < 1:<br><strong>K > -(1 / lg C) · [lg ||e|| - lg(Δ(1 - C))] - 1</strong><br>Вона дозволяє ще до старту програми точно сказати, скільки ітерацій знадобиться для досягнення заданої точності Δ.",
        voice: "Кількість ітерацій ка оцінюється через норму матриці за формулою дев'ять методички за допомогою десяткового логарифма похибки дельта."
      },
      {
        q: "7. Яка обчислювальна схема методу простої ітерації?",
        a: "1. Рахуємо матрицю B і вектор e.<br>2. Перевіряємо норму: чи C = ||B|| < 1.<br>3. Обираємо старт: x⁰ = e (або нулі).<br>4. Оцінюємо потрібне число кроків K за формулою (9).<br>5. Рахуємо x^(k+1) = B·x^k + e, доки похибка не стане меншою за Δ.",
        voice: "Схема складається з п'яти кроків: обчислення матриці бе та вектора є, перевірки норми, вибору стартового наближення, оцінки кількості кроків та виконання ітерацій."
      },
      {
        q: "8. Чим відрізняється метод Зейделя від методу простої ітерації? (НАЙВАЖЛИВІШЕ ПИТАННЯ)",
        a: "<strong>Ключова відмінність:</strong> у простій ітерації на кроці (k+1) всі змінні рахуються суто за старими значеннями з попереднього кроку k.<br><br><strong>У методі Зейделя при обчисленні кожної наступної змінної відразу ж підставляються найновіші значення, щойно отримані на цьому самому поточному кроці!</strong> Це прискорює збіжність вдвічі!",
        voice: "У методі Зейделя щойно обчислене значення відразу ж підставляється в наступні рівняння на тій самій ітерації, тому він збігається вдвічі швидше."
      },
      {
        q: "9. Яка умова збіжності методу Зейделя?",
        a: "Достатньою умовою є <strong>строге діагональне переважання</strong> (формула 10): модуль коефіцієнта на головній діагоналі кожного рядка має бути строго більшим за суму модулів решти коефіцієнтів цього рядка.<br>За цієї умови метод збігається з будь-якого старту x⁰.",
        voice: "Достатньою умовою збіжності є строге діагональне переважання: модуль діагонального елемента в кожному рядку має бути більшим за суму інших елементів рядка."
      }
    ];

    let currentCard = 0;
    function showCard(idx) {
      currentCard = (idx + flashcards.length) % flashcards.length;
      document.getElementById('cardCounter').innerText = currentCard + 1;
      document.getElementById('cardNumFront').innerText = currentCard + 1;
      document.getElementById('cardQuestion').innerHTML = flashcards[currentCard].q;
      document.getElementById('cardAnswer').innerHTML = flashcards[currentCard].a;
      document.getElementById('flashcard').classList.remove('flipped');
    }

    function flipCard() {
      document.getElementById('flashcard').classList.toggle('flipped');
    }
    function nextCard() { showCard(currentCard + 1); }
    function prevCard() { showCard(currentCard - 1); }

    // TTS & SPEECH
    function speakSpeech() {
      if (!('speechSynthesis' in window)) {
        alert("Браузер не підтримує Web Speech API");
        return;
      }
      window.speechSynthesis.cancel();
      const text = "У четвертій лабораторній роботі я розв'язував систему з п'яти лінійних рівнянь дванадцятого варіанта двома методами: прямим методом Гаусса та ітераційним методом Гауса-Зейделя. Методом Гаусса з вибором головного елемента знайдено точний розв'язок: усі змінні дорівнюють один цілих дві десятих. Методом Гауса-Зейделя при точності десять в мінус десятому степені розв'язок зійшовся за двадцять одну ітерацію до тих самих значень один і два.";
      const u = new SpeechSynthesisUtterance(text);
      u.lang = 'uk-UA';
      u.rate = 1.0;
      window.speechSynthesis.speak(u);
    }

    function speakCurrentCard() {
      if (!('speechSynthesis' in window)) return;
      window.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(flashcards[currentCard].voice || flashcards[currentCard].q);
      u.lang = 'uk-UA';
      u.rate = 1.0;
      window.speechSynthesis.speak(u);
    }

    function copySpeech() {
      const text = document.getElementById('speechText').innerText;
      navigator.clipboard.writeText(text).then(() => {
        const btn = document.getElementById('copySpeechBtn');
        btn.innerText = '✅ Скопійовано!';
        setTimeout(() => { btn.innerText = '📋 Скопіювати'; }, 2000);
      });
    }

    // INITIALIZATION
    window.addEventListener('load', () => {
      setStep(0);
      showCard(0);
      calcComplexity();
      setTimeout(renderAllMath, 100);
      setTimeout(renderAllMath, 500);
    });
  </script>
</body>
</html>
'''

target_paths = [
    r'D:\Studing\SecondYear\FirstSemester\Numerical methods\Lab4\trainer.html',
    r'C:\Users\andri_gxiil3v\.gemini\antigravity\brain\b6dddea9-4b7f-464b-b4a6-3dcd2045af31\trainer.html'
]

for p in target_paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f'Successfully updated: {p}')
