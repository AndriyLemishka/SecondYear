/**
 * ChargeUA — Інтерактивна карта зарядних хабів
 * Динамічне підтягування точок із JSON/API, фільтрація за портами та містами,
 * живі статуси портів, синхронізація з калькулятором та каталогом.
 */

(function () {
  'use strict';

  // Базові координати міст та магістралей
  const CITY_CENTERS = {
    'lviv': { coords: [49.8397, 24.0297], zoom: 12 },
    'kyiv': { coords: [50.4501, 30.5238], zoom: 11 },
    'odesa': { coords: [46.4846, 30.7431], zoom: 12 },
    'dnipro': { coords: [48.4647, 35.0462], zoom: 12 },
    'highways': { coords: [49.8, 28.5], zoom: 7 },
    'all': { coords: [49.2, 31.0], zoom: 6 }
  };

  // Резервний локальний датасет на випадок CORS у file:///
  const FALLBACK_STATIONS = [
    // --- ЛЬВІВ (14 станцій) ---
    { id: 'lviv-stryiska', name: 'ChargeUA Hub Стрийська (АЗС ОККО)', city: 'Львів', address: 'вул. Стрийська, 352', coords: [49.7865, 24.0175], type: 'dc', power: 'DC 100 кВт', max_kw: 100, connectors: ['CCS2', 'CHAdeMO'], has_generator: true, schedule: '24/7', total_ports: 2, free_ports: 1, status: 'free', price_kwh: '13.90 ₴', operator: 'ChargeUA Network', rating: 4.9, plugshare_id: '314521' },
    { id: 'lviv-vg', name: 'ChargeUA Ultra-Hub Victoria Gardens', city: 'Львів', address: 'вул. Кульпарківська, 226А', coords: [49.8078, 23.9782], type: 'dc', power: 'DC 150 кВт', max_kw: 150, connectors: ['CCS2', 'CHAdeMO', 'Type 2'], has_generator: true, schedule: '24/7', total_ports: 4, free_ports: 3, status: 'free', price_kwh: '14.50 ₴', operator: 'ChargeUA Network', rating: 5.0, plugshare_id: '320144' },
    { id: 'lviv-chornovola', name: 'ChargeUA Hub Чорновола', city: 'Львів', address: 'просп. В. Чорновола, 93', coords: [49.8582, 24.0221], type: 'dc', power: 'DC 120 кВт', max_kw: 120, connectors: ['CCS2', 'GB/T'], has_generator: false, schedule: '24/7', total_ports: 2, free_ports: 0, status: 'busy', price_kwh: '14.20 ₴', operator: 'ChargeUA Network', rating: 4.8, plugshare_id: '298712' },
    { id: 'lviv-forum', name: 'ChargeUA Hub Forum Lviv', city: 'Львів', address: 'вул. Під Дубом, 7Б', coords: [49.8501, 24.0238], type: 'dc', power: 'DC 60 кВт / AC 22 кВт', max_kw: 60, connectors: ['CCS2', 'Type 2'], has_generator: false, schedule: '10:00–22:00', total_ports: 3, free_ports: 2, status: 'free', price_kwh: '13.50 ₴', operator: 'ChargeUA Network', rating: 4.7, plugshare_id: '281903' },
    { id: 'lviv-soborna', name: 'ChargeUA City пл. Соборна', city: 'Львів', address: 'пл. Соборна, 1', coords: [49.8385, 24.0345], type: 'ac', power: 'AC 22 кВт', max_kw: 22, connectors: ['Type 2'], has_generator: false, schedule: '24/7', total_ports: 2, free_ports: 1, status: 'free', price_kwh: '9.90 ₴', operator: 'ChargeUA Network', rating: 4.6, plugshare_id: '194200' },
    { id: 'lviv-kingcross', name: 'ChargeUA Mega-Hub King Cross Leopolis', city: 'Львів', address: 'с. Сокільники, вул. Стрийська, 30', coords: [49.7735, 24.0112], type: 'dc', power: 'Ultra-DC 240 кВт', max_kw: 240, connectors: ['CCS2', 'CHAdeMO', 'GB/T'], has_generator: true, schedule: '24/7', total_ports: 6, free_ports: 4, status: 'free', price_kwh: '14.80 ₴', operator: 'ChargeUA Network', rating: 4.9, plugshare_id: '334812' },
    { id: 'lviv-spartak', name: 'ChargeUA Hub СТЦ Spartak', city: 'Львів', address: 'вул. Гетьмана Мазепи, 1Б', coords: [49.8705, 24.0195], type: 'dc', power: 'DC 160 кВт', max_kw: 160, connectors: ['CCS2', 'Type 2'], has_generator: true, schedule: '24/7', total_ports: 4, free_ports: 2, status: 'free', price_kwh: '14.40 ₴', operator: 'ChargeUA Network', rating: 4.9, plugshare_id: '312904' },
    { id: 'lviv-sykhiv-vam', name: 'ChargeUA Hub Сихів ТЦ ВАМ', city: 'Львів', address: 'просп. Червоної Калини, 60', coords: [49.7942, 24.0538], type: 'dc', power: 'DC 80 кВт', max_kw: 80, connectors: ['CCS2', 'CHAdeMO'], has_generator: true, schedule: '24/7', total_ports: 3, free_ports: 2, status: 'free', price_kwh: '13.90 ₴', operator: 'ChargeUA Network', rating: 4.7, plugshare_id: '278451' },
    { id: 'lviv-horodotska', name: 'ChargeUA Hub Городоцька (WOG)', city: 'Львів', address: 'вул. Городоцька, 280', coords: [49.8285, 23.9512], type: 'dc', power: 'DC 120 кВт', max_kw: 120, connectors: ['CCS2', 'Type 2'], has_generator: true, schedule: '24/7', total_ports: 3, free_ports: 1, status: 'free', price_kwh: '14.20 ₴', operator: 'ChargeUA Network', rating: 4.8, plugshare_id: '301948' },
    { id: 'lviv-pivdennyi', name: 'ChargeUA Hub ТВК Південний', city: 'Львів', address: 'вул. Щирецька, 36', coords: [49.8125, 23.9735], type: 'dc', power: 'DC 100 кВт / AC 22 кВт', max_kw: 100, connectors: ['CCS2', 'GB/T', 'Type 2'], has_generator: true, schedule: '09:00–22:00', total_ports: 4, free_ports: 3, status: 'free', price_kwh: '13.80 ₴', operator: 'ChargeUA Network', rating: 4.7, plugshare_id: '289104' },
    { id: 'lviv-zelena', name: 'ChargeUA Зелена (Арсен)', city: 'Львів', address: 'вул. Зелена, 149', coords: [49.8185, 24.0521], type: 'dc', power: 'DC 60 кВт / AC 22 кВт', max_kw: 60, connectors: ['CCS2', 'Type 2'], has_generator: false, schedule: '24/7', total_ports: 3, free_ports: 2, status: 'free', price_kwh: '13.50 ₴', operator: 'ChargeUA Network', rating: 4.6, plugshare_id: '245192' },
    { id: 'lviv-airport', name: 'ChargeUA Аеропорт «Львів»', city: 'Львів', address: 'вул. Любінська, 168 (Паркінг)', coords: [49.8168, 23.9562], type: 'dc', power: 'DC 120 кВт', max_kw: 120, connectors: ['CCS2', 'CHAdeMO'], has_generator: true, schedule: '24/7', total_ports: 4, free_ports: 2, status: 'free', price_kwh: '14.50 ₴', operator: 'ChargeUA Network', rating: 4.9, plugshare_id: '318490' },
    { id: 'lviv-dvirceva', name: 'ChargeUA Залізничний Вокзал', city: 'Львів', address: 'пл. Двірцева, 1', coords: [49.8358, 23.9945], type: 'dc', power: 'DC 60 кВт', max_kw: 60, connectors: ['CCS2', 'Type 2'], has_generator: true, schedule: '24/7', total_ports: 2, free_ports: 1, status: 'free', price_kwh: '13.90 ₴', operator: 'ChargeUA Network', rating: 4.7, plugshare_id: '291845' },
    { id: 'lviv-shevchenka', name: 'ChargeUA Рясне (АЗС ОККО)', city: 'Львів', address: 'вул. Шевченка, 311', coords: [49.8665, 23.9525], type: 'dc', power: 'DC 120 кВт', max_kw: 120, connectors: ['CCS2', 'GB/T'], has_generator: true, schedule: '24/7', total_ports: 3, free_ports: 2, status: 'free', price_kwh: '14.20 ₴', operator: 'ChargeUA Network', rating: 4.8, plugshare_id: '304918' },

    // --- КИЇВ (12 станцій) ---
    { id: 'kyiv-central', name: 'ChargeUA Kyiv Central Ocean Plaza', city: 'Київ', address: 'вул. Антоновича, 176', coords: [50.4128, 30.5238], type: 'dc', power: 'DC 150 кВт', max_kw: 150, connectors: ['CCS2', 'CHAdeMO'], has_generator: true, schedule: '24/7', total_ports: 4, free_ports: 2, status: 'free', price_kwh: '14.90 ₴', operator: 'ChargeUA Network', rating: 4.9, plugshare_id: '401123' },
    { id: 'kyiv-respublika', name: 'ChargeUA Mega-Hub Respublika Park', city: 'Київ', address: 'Кільцева дорога, 1', coords: [50.3792, 30.4352], type: 'dc', power: 'Ultra-DC 240 кВт', max_kw: 240, connectors: ['CCS2', 'GB/T', 'Type 2'], has_generator: true, schedule: '24/7', total_ports: 8, free_ports: 5, status: 'free', price_kwh: '15.20 ₴', operator: 'ChargeUA Network', rating: 5.0, plugshare_id: '415890' },
    { id: 'kyiv-lavina', name: 'ChargeUA Ultra-Hub Lavina Mall', city: 'Київ', address: 'вул. Берковецька, 6Д', coords: [50.4952, 30.3605], type: 'dc', power: 'DC 160 кВт', max_kw: 160, connectors: ['CCS2', 'CHAdeMO', 'GB/T'], has_generator: true, schedule: '24/7', total_ports: 6, free_ports: 3, status: 'free', price_kwh: '14.90 ₴', operator: 'ChargeUA Network', rating: 4.9, plugshare_id: '399812' },
    { id: 'kyiv-blockbuster', name: 'ChargeUA Hub Blockbuster Mall', city: 'Київ', address: 'просп. Степана Бандери, 36', coords: [50.4895, 30.5275], type: 'dc', power: 'DC 180 кВт', max_kw: 180, connectors: ['CCS2', 'Type 2'], has_generator: true, schedule: '24/7', total_ports: 6, free_ports: 4, status: 'free', price_kwh: '15.00 ₴', operator: 'ChargeUA Network', rating: 4.9, plugshare_id: '408123' },
    { id: 'kyiv-rivermall', name: 'ChargeUA Hub River Mall', city: 'Київ', address: 'Дніпровська набережна, 12', coords: [50.4045, 30.6175], type: 'dc', power: 'DC 120 кВт', max_kw: 120, connectors: ['CCS2', 'Type 2'], has_generator: true, schedule: '24/7', total_ports: 4, free_ports: 2, status: 'free', price_kwh: '14.80 ₴', operator: 'ChargeUA Network', rating: 4.8, plugshare_id: '391048' },
    { id: 'kyiv-podil', name: 'ChargeUA Hub Поділ', city: 'Київ', address: 'вул. П. Сагайдачного, 12', coords: [50.4615, 30.5225], type: 'dc', power: 'DC 100 кВт', max_kw: 100, connectors: ['CCS2', 'Type 2'], has_generator: true, schedule: '24/7', total_ports: 3, free_ports: 1, status: 'free', price_kwh: '14.60 ₴', operator: 'ChargeUA Network', rating: 4.8, plugshare_id: '378912' },
    { id: 'kyiv-tsum', name: 'ChargeUA City ЦУМ', city: 'Київ', address: 'вул. Хрещатик, 38', coords: [50.4452, 30.5215], type: 'dc', power: 'DC 60 кВт / AC 22 кВт', max_kw: 60, connectors: ['CCS2', 'Type 2'], has_generator: false, schedule: '10:00–22:00', total_ports: 3, free_ports: 1, status: 'free', price_kwh: '14.20 ₴', operator: 'ChargeUA Network', rating: 4.7, plugshare_id: '356781' },
    { id: 'kyiv-dream', name: 'ChargeUA Hub Dream Yellow Оболонь', city: 'Київ', address: 'Оболонський просп., 1Б', coords: [50.5052, 30.4985], type: 'dc', power: 'DC 120 кВт', max_kw: 120, connectors: ['CCS2', 'GB/T'], has_generator: true, schedule: '24/7', total_ports: 4, free_ports: 2, status: 'free', price_kwh: '14.70 ₴', operator: 'ChargeUA Network', rating: 4.8, plugshare_id: '384591' },
    { id: 'kyiv-bazhana', name: 'ChargeUA Позняки (АЗС WOG)', city: 'Київ', address: 'просп. М. Бажана, 8', coords: [50.3985, 30.6385], type: 'dc', power: 'DC 120 кВт', max_kw: 120, connectors: ['CCS2', 'CHAdeMO'], has_generator: true, schedule: '24/7', total_ports: 4, free_ports: 3, status: 'free', price_kwh: '14.80 ₴', operator: 'ChargeUA Network', rating: 4.8, plugshare_id: '368910' },
    { id: 'kyiv-vdng', name: 'ChargeUA ВДНГ', city: 'Київ', address: 'просп. Академіка Глушкова, 1', coords: [50.3785, 30.4785], type: 'dc', power: 'DC 80 кВт', max_kw: 80, connectors: ['CCS2', 'Type 2'], has_generator: false, schedule: '24/7', total_ports: 3, free_ports: 2, status: 'free', price_kwh: '13.90 ₴', operator: 'ChargeUA Network', rating: 4.7, plugshare_id: '349102' },
    { id: 'kyiv-zhuliany', name: 'ChargeUA Аеропорт «Київ» (Жуляни)', city: 'Київ', address: 'вул. Медова, 2', coords: [50.4085, 30.4485], type: 'dc', power: 'DC 120 кВт', max_kw: 120, connectors: ['CCS2', 'CHAdeMO'], has_generator: true, schedule: '24/7', total_ports: 4, free_ports: 2, status: 'free', price_kwh: '14.80 ₴', operator: 'ChargeUA Network', rating: 4.9, plugshare_id: '374189' },
    { id: 'kyiv-boryspil-hwy', name: 'ChargeUA Бориспільське шосе (SOCAR)', city: 'Київ', address: 'Бориспільське шосе, 18 км', coords: [50.3585, 30.8285], type: 'dc', power: 'Ultra-DC 200 кВт', max_kw: 200, connectors: ['CCS2', 'GB/T'], has_generator: true, schedule: '24/7', total_ports: 6, free_ports: 4, status: 'free', price_kwh: '15.40 ₴', operator: 'ChargeUA Network', rating: 5.0, plugshare_id: '410291' },

    // --- ОДЕСА (5 станцій) ---
    { id: 'odesa-prymorskyi', name: 'ChargeUA Одеса Приморський', city: 'Одеса', address: 'Приморський бул., 14', coords: [46.4846, 30.7431], type: 'ac', power: 'AC 22 кВт', max_kw: 22, connectors: ['Type 2'], has_generator: false, schedule: '08:00–22:00', total_ports: 3, free_ports: 2, status: 'free', price_kwh: '10.50 ₴', operator: 'ChargeUA Network', rating: 4.7, plugshare_id: '210492' },
    { id: 'odesa-arkadia', name: 'ChargeUA Аркадія Gagarinn Plaza', city: 'Одеса', address: 'вул. Генуезька, 5', coords: [46.4325, 30.7625], type: 'dc', power: 'DC 150 кВт', max_kw: 150, connectors: ['CCS2', 'CHAdeMO', 'Type 2'], has_generator: true, schedule: '24/7', total_ports: 4, free_ports: 3, status: 'free', price_kwh: '14.60 ₴', operator: 'ChargeUA Network', rating: 4.9, plugshare_id: '319482' },
    { id: 'odesa-riviera', name: 'ChargeUA Hub ТРЦ Riviera', city: 'Одеса', address: 'Південна дорога, 101А', coords: [46.5685, 30.7985], type: 'dc', power: 'DC 120 кВт', max_kw: 120, connectors: ['CCS2', 'GB/T'], has_generator: true, schedule: '24/7', total_ports: 4, free_ports: 2, status: 'free', price_kwh: '14.40 ₴', operator: 'ChargeUA Network', rating: 4.8, plugshare_id: '308419' },
    { id: 'odesa-airport', name: 'ChargeUA Аеропорт «Одеса»', city: 'Одеса', address: 'вул. Центральний аеропорт, 2', coords: [46.4285, 30.6825], type: 'dc', power: 'DC 100 кВт', max_kw: 100, connectors: ['CCS2', 'CHAdeMO'], has_generator: true, schedule: '24/7', total_ports: 3, free_ports: 1, status: 'free', price_kwh: '14.20 ₴', operator: 'ChargeUA Network', rating: 4.7, plugshare_id: '295104' },
    { id: 'odesa-liustdorf', name: 'ChargeUA Люстдорфська (ОККО)', city: 'Одеса', address: 'Люстдорфська дорога, 55', coords: [46.4415, 30.7185], type: 'dc', power: 'DC 120 кВт', max_kw: 120, connectors: ['CCS2', 'Type 2'], has_generator: true, schedule: '24/7', total_ports: 3, free_ports: 2, status: 'free', price_kwh: '14.30 ₴', operator: 'ChargeUA Network', rating: 4.8, plugshare_id: '299182' },

    // --- ДНІПРО (4 станції) ---
    { id: 'dnipro-most', name: 'ChargeUA ТРК МОСТ-Сіті', city: 'Дніпро', address: 'вул. Глинки, 2', coords: [48.4675, 35.0515], type: 'dc', power: 'DC 150 кВт', max_kw: 150, connectors: ['CCS2', 'CHAdeMO', 'Type 2'], has_generator: true, schedule: '24/7', total_ports: 4, free_ports: 2, status: 'free', price_kwh: '14.60 ₴', operator: 'ChargeUA Network', rating: 4.9, plugshare_id: '351094' },
    { id: 'dnipro-center', name: 'ChargeUA Центр Пасаж', city: 'Дніпро', address: 'просп. Д. Яворницького, 50', coords: [48.4645, 35.0485], type: 'dc', power: 'DC 80 кВт', max_kw: 80, connectors: ['CCS2', 'Type 2'], has_generator: false, schedule: '24/7', total_ports: 3, free_ports: 1, status: 'free', price_kwh: '13.90 ₴', operator: 'ChargeUA Network', rating: 4.7, plugshare_id: '332810' },
    { id: 'dnipro-karavan', name: 'ChargeUA Hub ТРЦ Караван', city: 'Дніпро', address: 'вул. Нижньодніпровська, 17', coords: [48.5325, 35.0345], type: 'dc', power: 'DC 120 кВт', max_kw: 120, connectors: ['CCS2', 'GB/T'], has_generator: true, schedule: '24/7', total_ports: 4, free_ports: 3, status: 'free', price_kwh: '14.30 ₴', operator: 'ChargeUA Network', rating: 4.8, plugshare_id: '341908' },
    { id: 'dnipro-peremoha', name: 'ChargeUA Набережна Перемоги (WOG)', city: 'Дніпро', address: 'Набережна Перемоги, 10', coords: [48.4415, 35.0785], type: 'dc', power: 'DC 100 кВт', max_kw: 100, connectors: ['CCS2', 'CHAdeMO'], has_generator: true, schedule: '24/7', total_ports: 3, free_ports: 2, status: 'free', price_kwh: '14.20 ₴', operator: 'ChargeUA Network', rating: 4.8, plugshare_id: '338901' },

    // --- ТРАСИ УКРАЇНИ (5 магістральних хабів) ---
    { id: 'hwy-m06-zhytomyr', name: 'ChargeUA Траса М-06 Житомир (WOG)', city: 'Траса М-06', address: 'траса М-06 Київ — Чоп, с. Глибочиця', coords: [50.2855, 28.7755], type: 'dc', power: 'Ultra-DC 180 кВт', max_kw: 180, connectors: ['CCS2', 'CHAdeMO', 'Type 2'], has_generator: true, schedule: '24/7', total_ports: 4, free_ports: 3, status: 'free', price_kwh: '15.00 ₴', operator: 'ChargeUA Network', rating: 5.0, plugshare_id: '389104' },
    { id: 'hwy-m06-rivne', name: 'ChargeUA Траса М-06 Рівне (ОККО)', city: 'Траса М-06', address: 'траса М-06 Київ — Чоп, с. Біла Криниця', coords: [50.5985, 26.3685], type: 'dc', power: 'Ultra-DC 200 кВт', max_kw: 200, connectors: ['CCS2', 'GB/T'], has_generator: true, schedule: '24/7', total_ports: 4, free_ports: 2, status: 'free', price_kwh: '15.20 ₴', operator: 'ChargeUA Network', rating: 4.9, plugshare_id: '395401' },
    { id: 'hwy-m06-brody', name: 'ChargeUA Траса М-06 Броди (ОККО)', city: 'Траса М-06', address: 'траса М-06 Львів — Київ, м. Броди', coords: [50.0755, 25.1585], type: 'dc', power: 'DC 120 кВт', max_kw: 120, connectors: ['CCS2', 'CHAdeMO'], has_generator: true, schedule: '24/7', total_ports: 3, free_ports: 2, status: 'free', price_kwh: '14.60 ₴', operator: 'ChargeUA Network', rating: 4.8, plugshare_id: '364102' },
    { id: 'hwy-m05-uman', name: 'ChargeUA Траса М-05 Умань (SOCAR)', city: 'Траса М-05', address: 'траса М-05 Київ — Одеса, м. Умань', coords: [48.7455, 30.2285], type: 'dc', power: 'Ultra-DC 240 кВт', max_kw: 240, connectors: ['CCS2', 'GB/T', 'CHAdeMO'], has_generator: true, schedule: '24/7', total_ports: 6, free_ports: 4, status: 'free', price_kwh: '15.50 ₴', operator: 'ChargeUA Network', rating: 5.0, plugshare_id: '418902' },
    { id: 'hwy-m05-bilatserkva', name: 'ChargeUA Траса М-05 Біла Церква (ОККО)', city: 'Траса М-05', address: 'траса М-05 Київ — Одеса, м. Біла Церква', coords: [49.8155, 30.1285], type: 'dc', power: 'DC 150 кВт', max_kw: 150, connectors: ['CCS2', 'Type 2'], has_generator: true, schedule: '24/7', total_ports: 4, free_ports: 3, status: 'free', price_kwh: '14.90 ₴', operator: 'ChargeUA Network', rating: 4.9, plugshare_id: '384910' }
  ];

  let mapInstance = null;
  let markersLayer = null;
  let allStations = [];
  let currentFilter = 'all';
  let currentCity = 'lviv';
  let markerMap = {};

  // Створення HTML для маркера Leaflet
  function createMarkerIcon(station) {
    const statusClass = station.free_ports > 0 ? 'marker--free' : 'marker--busy';
    const genBadge = station.has_generator ? '<span class="pin-gen" title="Працює від генератора">🔋</span>' : '';
    const iconHtml = `
      <div class="custom-map-pin ${statusClass}">
        <i class="fa-solid fa-bolt"></i>
        ${genBadge}
        <span class="pin-badge">${station.free_ports}/${station.total_ports}</span>
      </div>
    `;
    return L.divIcon({
      html: iconHtml,
      className: 'chargeua-pin-wrapper',
      iconSize: [38, 44],
      iconAnchor: [19, 44],
      popupAnchor: [0, -42]
    });
  }

  // Створення контенту для спливаючого вікна (Popup)
  function createPopupContent(station) {
    const googleMapsUrl = `https://www.google.com/maps/dir/?api=1&destination=${station.coords[0]},${station.coords[1]}`;
    const wazeUrl = `https://waze.com/ul?ll=${station.coords[0]},${station.coords[1]}&navigate=yes`;
    const plugshareUrl = station.plugshare_id 
      ? `https://www.plugshare.com/location/${station.plugshare_id}` 
      : `https://www.plugshare.com`;

    const statusBadge = station.free_ports > 0 
      ? `<span class="popup-badge popup-badge--free"><i class="fa-solid fa-circle-check"></i> Вільний (${station.free_ports}/${station.total_ports} портів)</span>`
      : `<span class="popup-badge popup-badge--busy"><i class="fa-solid fa-circle-xmark"></i> Всі зайняті (0/${station.total_ports})</span>`;

    const genNotice = station.has_generator 
      ? `<div class="popup-gen-tag"><i class="fa-solid fa-shield-halved"></i> 100% автономність: резервний генератор при відключеннях</div>` 
      : '';

    const connectorsBadges = station.connectors.map(c => `<span class="chip-mini">${c}</span>`).join(' ');

    return `
      <div class="station-popup">
        <div class="station-popup__header">
          <span class="station-popup__type">${station.power}</span>
          <span class="station-popup__price">${station.price_kwh}</span>
        </div>
        <h4 class="station-popup__title">${station.name}</h4>
        <p class="station-popup__address"><i class="fa-solid fa-location-dot"></i> ${station.address}, ${station.city}</p>
        
        <div class="station-popup__status">
          ${statusBadge}
        </div>

        ${genNotice}

        <div class="station-popup__connectors">
          <span class="connectors-label">Порти:</span>
          ${connectorsBadges}
        </div>

        <div class="station-popup__actions">
          <a href="${googleMapsUrl}" target="_blank" rel="noopener noreferrer" class="btn-popup btn-popup--primary">
            <i class="fa-solid fa-diamond-turn-right"></i> Маршрут (Google Maps)
          </a>
          <a href="${wazeUrl}" target="_blank" rel="noopener noreferrer" class="btn-popup btn-popup--secondary" title="Відкрити у Waze">
            <i class="fa-brands fa-waze"></i> Waze
          </a>
          <a href="${plugshareUrl}" target="_blank" rel="noopener noreferrer" class="btn-popup btn-popup--tertiary" title="Перевірити у PlugShare">
            <i class="fa-solid fa-charging-station"></i> PlugShare
          </a>
        </div>
      </div>
    `;
  }

  // Рендеринг маркерів на карті
  function renderMarkers(stationsToRender) {
    if (!markersLayer) return;
    markersLayer.clearLayers();
    markerMap = {};

    let totalFree = 0;

    stationsToRender.forEach(station => {
      totalFree += station.free_ports;
      const marker = L.marker(station.coords, {
        icon: createMarkerIcon(station),
        title: station.name
      });

      marker.bindPopup(createPopupContent(station), {
        maxWidth: 320,
        className: 'chargeua-leaflet-popup'
      });

      markersLayer.addLayer(marker);
      markerMap[station.id] = marker;
    });

    // Оновлення лічильника
    const counterEl = document.getElementById('map-live-counter');
    if (counterEl) {
      counterEl.innerHTML = `<i class="fa-solid fa-charging-station"></i> Показано станцій: <strong>${stationsToRender.length}</strong> (вільних портів: <strong>${totalFree}</strong>)`;
    }
  }

  // Фільтрація станцій
  function applyFilter(filterKey) {
    currentFilter = filterKey;
    let filtered = allStations;

    // Фільтр за містом (якщо не 'all')
    if (currentCity !== 'all') {
      if (currentCity === 'lviv') {
        filtered = filtered.filter(s => s.city.includes('Львів'));
      } else if (currentCity === 'kyiv') {
        filtered = filtered.filter(s => s.city.includes('Київ'));
      } else if (currentCity === 'odesa') {
        filtered = filtered.filter(s => s.city.includes('Одеса'));
      } else if (currentCity === 'dnipro') {
        filtered = filtered.filter(s => s.city.includes('Дніпро'));
      } else if (currentCity === 'highways') {
        filtered = filtered.filter(s => s.city.includes('Траса'));
      }
    }

    // Фільтр за типом / конектором
    if (filterKey === 'dc') {
      filtered = filtered.filter(s => s.type === 'dc' || s.max_kw >= 50);
    } else if (filterKey === 'ac') {
      filtered = filtered.filter(s => s.type === 'ac' || s.max_kw < 50);
    } else if (filterKey === 'free') {
      filtered = filtered.filter(s => s.free_ports > 0);
    } else if (filterKey === 'generator') {
      filtered = filtered.filter(s => s.has_generator === true);
    } else if (filterKey === 'ccs2' || filterKey === 'ccs') {
      filtered = filtered.filter(s => s.connectors.some(c => c.toUpperCase().includes('CCS')));
    } else if (filterKey === 'chademo') {
      filtered = filtered.filter(s => s.connectors.some(c => c.toUpperCase().includes('CHADEMO')));
    } else if (filterKey === 'type2') {
      filtered = filtered.filter(s => s.connectors.some(c => c.toUpperCase().includes('TYPE 2') || c.toUpperCase().includes('TYPE2')));
    } else if (filterKey === 'gbt' || filterKey === 'gb/t') {
      filtered = filtered.filter(s => s.connectors.some(c => c.toUpperCase().includes('GB/T') || c.toUpperCase().includes('GBT')));
    }

    renderMarkers(filtered);
  }

  // Ініціалізація карти
  function initMap() {
    const container = document.getElementById('map-container');
    if (!container || !window.L) return;

    container.innerHTML = '<div id="map-leaflet-canvas" style="width: 100%; height: 520px; border-radius: var(--radius-md);"></div>';

    mapInstance = L.map('map-leaflet-canvas', {
      zoomControl: true,
      scrollWheelZoom: false
    }).setView(CITY_CENTERS.lviv.coords, CITY_CENTERS.lviv.zoom);

    // Швидка, стабільна підкладка ESRI World Street Map
    L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
      maxZoom: 19,
      attribution: 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS | ChargeUA Live Map'
    }).addTo(mapInstance);

    markersLayer = L.layerGroup().addTo(mapInstance);

    // Завантаження точок
    loadStationData();

    // Налаштування фільтрів
    setupFilters();

    // Налаштування перемикача міст
    setupCitySwitcher();

    // Симуляція статусів
    startLiveStatusSimulation();
  }

  // Завантаження точок (fetch з fallback на локальні)
  async function loadStationData() {
    try {
      const response = await fetch('assets/data/stations.json', { cache: 'no-cache' });
      if (!response.ok) throw new Error('Network error');
      allStations = await response.json();
      console.log('✅ ChargeUA: Станції успішно підтягнуто:', allStations.length);
    } catch (err) {
      console.warn('⚠️ ChargeUA: Fallback на локальний масив 40 станцій:', err.message);
      allStations = FALLBACK_STATIONS;
    }

    applyFilter('all');
  }

  // Обробники кліків по фільтрах конекторів
  function setupFilters() {
    const filterButtons = document.querySelectorAll('.map-filters .chip');
    filterButtons.forEach(btn => {
      btn.addEventListener('click', function () {
        filterButtons.forEach(b => {
          b.setAttribute('aria-pressed', 'false');
          b.classList.remove('chip--active');
        });
        this.setAttribute('aria-pressed', 'true');
        this.classList.add('chip--active');

        const filterVal = this.dataset.filter || 'all';
        applyFilter(filterVal);
      });
    });
  }

  // Перемикач швидкого масштабування міст
  function setupCitySwitcher() {
    const cityButtons = document.querySelectorAll('.city-tab, .btn-city');
    cityButtons.forEach(btn => {
      btn.addEventListener('click', function () {
        cityButtons.forEach(b => {
          b.classList.remove('city-tab--active', 'btn-city--active');
          b.setAttribute('aria-selected', 'false');
        });
        this.classList.add('city-tab--active');
        this.setAttribute('aria-selected', 'true');

        const cityKey = this.getAttribute('data-city') || 'lviv';
        currentCity = cityKey;

        const cityConfig = CITY_CENTERS[cityKey];
        if (cityConfig && mapInstance) {
          mapInstance.flyTo(cityConfig.coords, cityConfig.zoom, { duration: 1.2 });
        }

        applyFilter(currentFilter);
      });
    });
  }

  // Симуляція динамічного оновлення статусів у реальному часі
  function startLiveStatusSimulation() {
    setInterval(() => {
      if (!allStations || allStations.length === 0) return;
      const randomIdx = Math.floor(Math.random() * allStations.length);
      const st = allStations[randomIdx];
      if (st.free_ports > 0 && Math.random() > 0.5) {
        st.free_ports = Math.max(0, st.free_ports - 1);
      } else if (st.free_ports < st.total_ports) {
        st.free_ports = Math.min(st.total_ports, st.free_ports + 1);
      }
      applyFilter(currentFilter);
    }, 20000);
  }

  function loadLeaflet(callback) {
    if (window.L) {
      callback();
      return;
    }
    const script = document.createElement('script');
    script.src = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js';
    script.integrity = 'sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=';
    script.crossOrigin = '';
    script.onload = callback;
    document.body.appendChild(script);
  }

  let mapInitialized = false;
  function ensureMapInit() {
    if (mapInitialized) return;
    mapInitialized = true;
    loadLeaflet(function () {
      initMap();
    });
  }

  function setupLazyMap() {
    const mapSection = document.getElementById('map');
    if ('IntersectionObserver' in window && mapSection) {
      const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting || entry.intersectionRatio > 0) {
            ensureMapInit();
            observer.disconnect();
          }
        });
      }, { rootMargin: '0px' });
      observer.observe(mapSection);
      mapSection.addEventListener('pointerdown', ensureMapInit, { once: true, passive: true });
      mapSection.addEventListener('focusin', ensureMapInit, { once: true, passive: true });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupLazyMap);
  } else {
    setupLazyMap();
  }

  // Експорт глобального API ChargeUA
  window.ChargeUAMap = {
    getMap: () => mapInstance,
    getMarkers: () => markerMap,
    getStations: () => allStations,
    focusStation: function (stationId) {
      ensureMapInit();
      const st = allStations.find(s => s.id === stationId);
      if (st && mapInstance) {
        mapInstance.flyTo(st.coords, 14, { duration: 1.0 });
        const mapSection = document.getElementById('map');
        if (mapSection) mapSection.scrollIntoView({ behavior: 'smooth' });
        setTimeout(() => {
          if (markerMap[stationId]) {
            markerMap[stationId].openPopup();
          }
        }, 1100);
      }
    },
    filterByConnector: function (connector) {
      let connKey = connector.toLowerCase();
      if (connKey.includes('ccs')) connKey = 'ccs2';
      else if (connKey.includes('chademo')) connKey = 'chademo';
      else if (connKey.includes('gb/t') || connKey.includes('gbt')) connKey = 'gbt';
      else if (connKey.includes('type 2') || connKey.includes('type2')) connKey = 'type2';

      // Оновлюємо активний чіп
      const filterButtons = document.querySelectorAll('.map-filters .chip');
      filterButtons.forEach(b => {
        if (b.dataset.filter === connKey) {
          b.classList.add('chip--active');
          b.setAttribute('aria-pressed', 'true');
        } else {
          b.classList.remove('chip--active');
          b.setAttribute('aria-pressed', 'false');
        }
      });

      applyFilter(connKey);

      // Підсвічуємо найближчу підходящу вільну станцію
      const matching = allStations.filter(s => 
        s.connectors.some(c => c.toLowerCase().includes(connKey)) && s.free_ports > 0
      );

      if (matching.length > 0 && mapInstance) {
        // Знаходимо першу в поточному місті або загалом
        const inCity = matching.find(s => currentCity === 'all' || s.city.toLowerCase().includes(currentCity)) || matching[0];
        mapInstance.flyTo(inCity.coords, 13, { duration: 1.0 });
        setTimeout(() => {
          if (markerMap[inCity.id]) markerMap[inCity.id].openPopup();
        }, 1100);
      }
    }
  };

})();
