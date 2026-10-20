# Лабораторна робота №6: Компонентна верстка, стилізація та адаптивність
## Підготовка до міграції на Tailwind CSS

Цей каталог містить семантичну базу проєкту **ChargeUA**, підготовлену для виконання завдань **Лабораторної роботи №6**.

### План роботи з міграції на Tailwind CSS:
1. **Етап 1–3**: Підключення Tailwind CSS через CDN (`https://cdn.tailwindcss.com`) у файлі `index.html`.
2. **Етап 4–7**: Ознайомлення з пісочницею Tailwind Play та принципом Mobile-First (`sm:`, `md:`, `lg:`, `xl:`).
3. **Етап 8–10**: Покомпонентна заміна правил `style.css` на утилітарні класи Tailwind:
   - Кнопки дій: `.btn-primary` $\to$ `bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-xl transition duration-200`.
   - Шапка: `.site-header` $\to$ `flex items-center justify-between py-4 px-6 bg-white/95 backdrop-blur shadow-sm`.
   - Сітка карток: `.station-grid` $\to$ `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6`.
   - Футер: `.site-footer` $\to$ `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 bg-slate-900 text-white`.
4. **Етап 14**: Перенесення дизайн-системи Figma (ЛР №4) у конфігурацію `tailwind.config` або CSS Custom Properties.
5. **Етап 18**: Хмарний деплой на Netlify (Drag & Drop папки або через Git).
