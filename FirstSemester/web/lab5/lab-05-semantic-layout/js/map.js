/**
 * ChargeUA — Інтерактивна карта зарядних хабів
 * Динамічне підтягування точок із JSON/API, фільтрація, живі статуси портів,
 * синхронізація з каталогом та перехід у зовнішні навігатори (Google Maps / PlugShare).
 */

(function () {
  'use strict';

  // Базові координати
  const CITY_CENTERS = {
    'lviv': { coords: [49.8397, 24.0297], zoom: 12 },
    'kyiv': { coords: [50.4501, 30.5238], zoom: 12 },
    'odesa': { coords: [46.4846, 30.7431], zoom: 13 },
    'all': { coords: [49.2, 28.5], zoom: 6 }
  };

  // Резервний локальний датасет (Fallback на випадок CORS у file:///)
  const FALLBACK_STATIONS = [
    {
      id: 'lviv-stryiska',
      name: 'ChargeUA Hub Стрийська (АЗС ОККО)',
      city: 'Львів',
      address: 'вул. Стрийська, 352',
      coords: [49.7865, 24.0175],
      type: 'dc',
      power: 'DC 100 кВт',
      max_kw: 100,
      connectors: ['CCS2', 'CHAdeMO'],
      schedule: '24/7',
      total_ports: 2,
      free_ports: 1,
      status: 'free',
      price_kwh: '13.90 ₴',
      operator: 'ChargeUA Network',
      rating: 4.9,
      plugshare_id: '314521'
    },
    {
      id: 'lviv-vg',
      name: 'ChargeUA Ultra-Hub Victoria Gardens',
      city: 'Львів',
      address: 'вул. Кульпарківська, 226А',
      coords: [49.8078, 23.9782],
      type: 'dc',
      power: 'DC 150 кВт',
      max_kw: 150,
      connectors: ['CCS2', 'CHAdeMO', 'Type 2'],
      schedule: '24/7',
      total_ports: 4,
      free_ports: 3,
      status: 'free',
      price_kwh: '14.50 ₴',
      operator: 'ChargeUA Network',
      rating: 5.0,
      plugshare_id: '320144'
    },
    {
      id: 'lviv-chornovola',
      name: 'ChargeUA Hub Чорновола',
      city: 'Львів',
      address: 'просп. В. Чорновола, 93',
      coords: [49.8582, 24.0221],
      type: 'dc',
      power: 'DC 120 кВт',
      max_kw: 120,
      connectors: ['CCS2'],
      schedule: '24/7',
      total_ports: 2,
      free_ports: 0,
      status: 'busy',
      price_kwh: '14.20 ₴',
      operator: 'ChargeUA Network',
      rating: 4.8,
      plugshare_id: '298712'
    },
    {
      id: 'lviv-forum',
      name: 'ChargeUA Hub Forum Lviv',
      city: 'Львів',
      address: 'вул. Під Дубом, 7Б',
      coords: [49.8501, 24.0238],
      type: 'dc',
      power: 'DC 60 кВт / AC 22 кВт',
      max_kw: 60,
      connectors: ['CCS2', 'Type 2'],
      schedule: '10:00–22:00',
      total_ports: 3,
      free_ports: 2,
      status: 'free',
      price_kwh: '13.50 ₴',
      operator: 'ChargeUA Network',
      rating: 4.7,
      plugshare_id: '281903'
    },
    {
      id: 'lviv-soborna',
      name: 'ChargeUA City пл. Соборна',
      city: 'Львів',
      address: 'пл. Соборна, 1',
      coords: [49.8385, 24.0345],
      type: 'ac',
      power: 'AC 22 кВт',
      max_kw: 22,
      connectors: ['Type 2'],
      schedule: '24/7',
      total_ports: 2,
      free_ports: 1,
      status: 'reserved',
      price_kwh: '9.90 ₴',
      operator: 'ChargeUA Network',
      rating: 4.6,
      plugshare_id: '194200'
    },
    {
      id: 'kyiv-central',
      name: 'ChargeUA Kyiv Central Ocean Plaza',
      city: 'Київ',
      address: 'вул. Антоновича, 176',
      coords: [50.4128, 30.5238],
      type: 'dc',
      power: 'DC 150 кВт',
      max_kw: 150,
      connectors: ['CCS2', 'CHAdeMO'],
      schedule: '24/7',
      total_ports: 4,
      free_ports: 2,
      status: 'free',
      price_kwh: '14.90 ₴',
      operator: 'ChargeUA Network',
      rating: 4.9,
      plugshare_id: '401123'
    },
    {
      id: 'odesa-prymorskyi',
      name: 'ChargeUA Одеса Приморський',
      city: 'Одеса',
      address: 'Приморський бул., 14',
      coords: [46.4846, 30.7431],
      type: 'ac',
      power: 'AC 22 кВт',
      max_kw: 22,
      connectors: ['Type 2'],
      schedule: '08:00–22:00',
      total_ports: 3,
      free_ports: 2,
      status: 'free',
      price_kwh: '10.50 ₴',
      operator: 'ChargeUA Network',
      rating: 4.7,
      plugshare_id: '210492'
    }
  ];

  let mapInstance = null;
  let markersLayer = null;
  let allStations = [];
  let currentFilter = 'all';
  let markerMap = {};

  // Створення HTML для маркера
  function createMarkerIcon(station) {
    const statusClass = station.free_ports > 0 ? 'marker--free' : 'marker--busy';
    const iconHtml = `
      <div class="custom-map-pin ${statusClass}">
        <i class="fa-solid fa-bolt"></i>
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

        <div class="station-popup__connectors">
          <small>Конектори:</small> ${connectorsBadges}
        </div>

        <div class="station-popup__meta">
          <span><i class="fa-regular fa-clock"></i> ${station.schedule}</span>
          <span><i class="fa-solid fa-star" style="color:#F59E0B"></i> ${station.rating}</span>
        </div>

        <div class="station-popup__actions">
          <a href="${googleMapsUrl}" target="_blank" rel="noopener noreferrer" class="btn-popup btn-popup--primary">
            <i class="fa-solid fa-route"></i> Маршрут
          </a>
          <a href="${plugshareUrl}" target="_blank" rel="noopener noreferrer" class="btn-popup btn-popup--secondary" title="Відкрити сторінку в PlugShare">
            <i class="fa-solid fa-arrow-up-right-from-square"></i> PlugShare
          </a>
        </div>
      </div>
    `;
  }

  // Відображення маркерів на карті
  function renderMarkers(stationsToRender) {
    if (!markersLayer) return;
    markersLayer.clearLayers();

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
      counterEl.innerHTML = `<i class="fa-solid fa-charging-station"></i> Знайдено станцій: <strong>${stationsToRender.length}</strong> (вільних портів: <strong>${totalFree}</strong>)`;
    }
  }

  // Фільтрація станцій
  function applyFilter(filterKey) {
    currentFilter = filterKey;
    let filtered = allStations;

    if (filterKey === 'dc') {
      filtered = allStations.filter(s => s.type === 'dc' || s.max_kw >= 50);
    } else if (filterKey === 'ac') {
      filtered = allStations.filter(s => s.type === 'ac' || s.max_kw < 50);
    } else if (filterKey === 'free') {
      filtered = allStations.filter(s => s.free_ports > 0);
    } else if (filterKey === '247') {
      filtered = allStations.filter(s => s.schedule === '24/7');
    } else if (filterKey === 'ccs2') {
      filtered = allStations.filter(s => s.connectors.includes('CCS2'));
    } else if (filterKey === 'chademo') {
      filtered = allStations.filter(s => s.connectors.includes('CHAdeMO'));
    }

    renderMarkers(filtered);
  }

  // Ініціалізація карти
  function initMap() {
    const container = document.getElementById('map-container');
    if (!container || !window.L) return;

    // Створюємо холст карти
    container.innerHTML = '<div id="map-leaflet-canvas" style="width: 100%; height: 500px; border-radius: var(--radius-md);"></div>';

    mapInstance = L.map('map-leaflet-canvas', {
      zoomControl: true,
      scrollWheelZoom: false
    }).setView(CITY_CENTERS.lviv.coords, CITY_CENTERS.lviv.zoom);

    // Підкладка карти ESRI World Street Map (чиста, швидка, детальна, без ключів та водяних знаків)
    L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
      maxZoom: 19,
      attribution: 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012 | <a href="https://chargeua.ua" target="_blank">ChargeUA Live</a>'
    }).addTo(mapInstance);

    markersLayer = L.layerGroup().addTo(mapInstance);

    // Додаємо статус підвантаження
    loadStationData();

    // Налаштування фільтрів
    setupFilters();

    // Додаємо перемикач міст
    setupCitySwitcher();

    // Запуск емуляції оновлення статусів у реальному часі (Live Dynamic Updates)
    startLiveStatusSimulation();
  }

  // Завантаження точок (fetch -> fallback)
  async function loadStationData() {
    try {
      const response = await fetch('assets/data/stations.json', { cache: 'no-cache' });
      if (!response.ok) throw new Error('Network error');
      allStations = await response.json();
      console.log('✅ ChargeUA: Станції успішно підтягнуто з assets/data/stations.json:', allStations.length);
    } catch (err) {
      console.warn('⚠️ ChargeUA: Режим fallback (локальні дані):', err.message);
      allStations = FALLBACK_STATIONS;
    }

    renderMarkers(allStations);
  }

  // Обробники кліків по фільтрах
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

        const text = this.textContent.trim().toLowerCase();
        if (text.includes('усі')) applyFilter('all');
        else if (text.includes('dc')) applyFilter('dc');
        else if (text.includes('ac')) applyFilter('ac');
        else if (text.includes('вільні')) applyFilter('free');
        else if (text.includes('24/7')) applyFilter('247');
        else if (text.includes('ccs2')) applyFilter('ccs2');
        else if (text.includes('chademo')) applyFilter('chademo');
      });
    });
  }

  // Перемикач швидкого масштабування міст
  function setupCitySwitcher() {
    const filtersAside = document.querySelector('.map-filters');
    if (!filtersAside) return;

    const switcherContainer = document.createElement('div');
    switcherContainer.className = 'map-city-switcher';
    switcherContainer.innerHTML = `
      <h4 class="map-city-switcher__title"><i class="fa-solid fa-city"></i> Швидкий перехід:</h4>
      <div class="map-city-buttons">
        <button type="button" class="btn-city btn-city--active" data-city="lviv">Львів</button>
        <button type="button" class="btn-city" data-city="kyiv">Київ</button>
        <button type="button" class="btn-city" data-city="odesa">Одеса</button>
        <button type="button" class="btn-city" data-city="all">Вся Україна</button>
      </div>
      <div id="map-live-counter" class="map-live-counter">
        <i class="fa-solid fa-arrows-rotate fa-spin"></i> Підтягування актуальних точок...
      </div>
    `;

    filtersAside.appendChild(switcherContainer);

    switcherContainer.querySelectorAll('.btn-city').forEach(btn => {
      btn.addEventListener('click', function () {
        switcherContainer.querySelectorAll('.btn-city').forEach(b => b.classList.remove('btn-city--active'));
        this.classList.add('btn-city--active');

        const cityKey = this.getAttribute('data-city');
        const cityConfig = CITY_CENTERS[cityKey];
        if (cityConfig && mapInstance) {
          mapInstance.flyTo(cityConfig.coords, cityConfig.zoom, { duration: 1.2 });
        }
      });
    });
  }

  // Симуляція динамічного оновлення статусів у реальному часі (кожні 25 сек)
  function startLiveStatusSimulation() {
    setInterval(() => {
      if (!allStations || allStations.length === 0) return;
      // Випадково змінюємо вільний порт на одній зі станцій
      const randomIdx = Math.floor(Math.random() * allStations.length);
      const st = allStations[randomIdx];
      if (st.free_ports > 0 && Math.random() > 0.5) {
        st.free_ports = Math.max(0, st.free_ports - 1);
      } else if (st.free_ports < st.total_ports) {
        st.free_ports = Math.min(st.total_ports, st.free_ports + 1);
      }
      applyFilter(currentFilter);
      console.log(`⚡ ChargeUA Live: Станція ${st.name} оновила доступність: ${st.free_ports}/${st.total_ports} портів.`);
    }, 25000);
  }

  // Запуск після завантаження DOM
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMap);
  } else {
    initMap();
  }

  // Експорт у глобальну область для синхронізації з каталогом
  window.ChargeUAMap = {
    getMap: () => mapInstance,
    getMarkers: () => markerMap,
    getStations: () => allStations,
    focusStation: function (stationId) {
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
    }
  };

})();
