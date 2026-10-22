/**
 * ChargeUA — Інтерактивний калькулятор зарядки електромобілів
 * База 50+ моделей (AUTO.RIA style за брендами), ручне введення ємності батареї (кВт·год),
 * фільтрація портів (CCS2, CHAdeMO, GB/T, Type 2) та синхронізація з картою станцій.
 */

(function () {
  'use strict';

  // База даних електромобілів (згрупована за брендами для випадаючого списку та розрахунків)
  const CAR_DATABASE = {
    // --- Volkswagen ---
    'vw-id4-pro': { name: 'Volkswagen ID.4 Pro', brand: 'Volkswagen', capacity: 77, maxDc: 135, connector: 'CCS2', tariff: 14.12, consumption: 18.0 },
    'vw-id4-pure': { name: 'Volkswagen ID.4 Pure', brand: 'Volkswagen', capacity: 52, maxDc: 110, connector: 'CCS2', tariff: 14.12, consumption: 17.0 },
    'vw-id3-pro': { name: 'Volkswagen ID.3 Pro', brand: 'Volkswagen', capacity: 58, maxDc: 120, connector: 'CCS2', tariff: 14.12, consumption: 15.5 },
    'vw-id6-crozz': { name: 'Volkswagen ID.6 Crozz (China)', brand: 'Volkswagen', capacity: 84.8, maxDc: 100, connector: 'GB/T', tariff: 14.12, consumption: 19.5 },
    'vw-id7-pro': { name: 'Volkswagen ID.7 Pro', brand: 'Volkswagen', capacity: 77, maxDc: 175, connector: 'CCS2', tariff: 14.12, consumption: 16.0 },
    'vw-egolf': { name: 'Volkswagen e-Golf', brand: 'Volkswagen', capacity: 35.8, maxDc: 40, connector: 'CCS2', tariff: 14.12, consumption: 15.0 },

    // --- Tesla ---
    'tesla-m3-std': { name: 'Tesla Model 3 RWD', brand: 'Tesla', capacity: 60, maxDc: 170, connector: 'CCS2', tariff: 14.12, consumption: 14.5 },
    'tesla-m3-lr': { name: 'Tesla Model 3 Long Range', brand: 'Tesla', capacity: 82, maxDc: 250, connector: 'CCS2', tariff: 14.12, consumption: 15.0 },
    'tesla-my-lr': { name: 'Tesla Model Y Long Range', brand: 'Tesla', capacity: 75, maxDc: 250, connector: 'CCS2', tariff: 14.12, consumption: 16.8 },
    'tesla-my-p': { name: 'Tesla Model Y Performance', brand: 'Tesla', capacity: 78, maxDc: 250, connector: 'CCS2', tariff: 14.12, consumption: 17.5 },
    'tesla-ms-p': { name: 'Tesla Model S Plaid', brand: 'Tesla', capacity: 100, maxDc: 250, connector: 'CCS2', tariff: 14.12, consumption: 18.5 },
    'tesla-mx-lr': { name: 'Tesla Model X Long Range', brand: 'Tesla', capacity: 100, maxDc: 250, connector: 'CCS2', tariff: 14.12, consumption: 20.5 },

    // --- Nissan ---
    'nissan-leaf-40': { name: 'Nissan Leaf 40 kWh', brand: 'Nissan', capacity: 40, maxDc: 50, connector: 'CHAdeMO', tariff: 14.12, consumption: 16.5 },
    'nissan-leaf-62': { name: 'Nissan Leaf e+ 62 kWh', brand: 'Nissan', capacity: 62, maxDc: 100, connector: 'CHAdeMO', tariff: 14.12, consumption: 17.5 },
    'nissan-ariya-63': { name: 'Nissan Ariya 63 kWh', brand: 'Nissan', capacity: 63, maxDc: 130, connector: 'CCS2', tariff: 14.12, consumption: 18.0 },
    'nissan-ariya-87': { name: 'Nissan Ariya 87 kWh', brand: 'Nissan', capacity: 87, maxDc: 130, connector: 'CCS2', tariff: 14.12, consumption: 19.5 },

    // --- Hyundai & Kia ---
    'hyundai-ioniq5': { name: 'Hyundai Ioniq 5', brand: 'Hyundai', capacity: 72.6, maxDc: 220, connector: 'CCS2', tariff: 14.12, consumption: 18.5 },
    'hyundai-ioniq6': { name: 'Hyundai Ioniq 6', brand: 'Hyundai', capacity: 77.4, maxDc: 235, connector: 'CCS2', tariff: 14.12, consumption: 15.0 },
    'hyundai-kona': { name: 'Hyundai Kona Electric', brand: 'Hyundai', capacity: 64, maxDc: 100, connector: 'CCS2', tariff: 14.12, consumption: 16.0 },
    'kia-ev6': { name: 'Kia EV6', brand: 'Kia', capacity: 77.4, maxDc: 235, connector: 'CCS2', tariff: 14.12, consumption: 18.0 },
    'kia-ev9': { name: 'Kia EV9', brand: 'Kia', capacity: 99.8, maxDc: 210, connector: 'CCS2', tariff: 14.12, consumption: 22.0 },
    'kia-niro-ev': { name: 'Kia Niro EV', brand: 'Kia', capacity: 64.8, maxDc: 85, connector: 'CCS2', tariff: 14.12, consumption: 16.2 },

    // --- BMW ---
    'bmw-i4': { name: 'BMW i4 eDrive40', brand: 'BMW', capacity: 83.9, maxDc: 205, connector: 'CCS2', tariff: 14.12, consumption: 17.5 },
    'bmw-ix': { name: 'BMW iX xDrive50', brand: 'BMW', capacity: 111.5, maxDc: 195, connector: 'CCS2', tariff: 14.12, consumption: 21.0 },
    'bmw-ix3': { name: 'BMW iX3', brand: 'BMW', capacity: 80, maxDc: 150, connector: 'CCS2', tariff: 14.12, consumption: 18.5 },
    'bmw-i3': { name: 'BMW i3 120Ah', brand: 'BMW', capacity: 42.2, maxDc: 50, connector: 'CCS2', tariff: 14.12, consumption: 14.0 },

    // --- Mercedes-Benz ---
    'mb-eqe': { name: 'Mercedes-Benz EQE 350+', brand: 'Mercedes-Benz', capacity: 90.6, maxDc: 170, connector: 'CCS2', tariff: 14.12, consumption: 18.0 },
    'mb-eqs': { name: 'Mercedes-Benz EQS 450+', brand: 'Mercedes-Benz', capacity: 107.8, maxDc: 200, connector: 'CCS2', tariff: 14.12, consumption: 19.5 },
    'mb-eqa': { name: 'Mercedes-Benz EQA 250', brand: 'Mercedes-Benz', capacity: 66.5, maxDc: 100, connector: 'CCS2', tariff: 14.12, consumption: 17.5 },
    'mb-eqc': { name: 'Mercedes-Benz EQC 400', brand: 'Mercedes-Benz', capacity: 80, maxDc: 110, connector: 'CCS2', tariff: 14.12, consumption: 21.5 },

    // --- Audi & Porsche ---
    'audi-etron': { name: 'Audi e-tron 55 quattro', brand: 'Audi', capacity: 95, maxDc: 150, connector: 'CCS2', tariff: 14.12, consumption: 23.0 },
    'audi-q4': { name: 'Audi Q4 e-tron', brand: 'Audi', capacity: 82, maxDc: 135, connector: 'CCS2', tariff: 14.12, consumption: 18.0 },
    'porsche-taycan': { name: 'Porsche Taycan 4S', brand: 'Porsche', capacity: 93.4, maxDc: 270, connector: 'CCS2', tariff: 14.12, consumption: 21.5 },
    'porsche-macan': { name: 'Porsche Macan Electric', brand: 'Porsche', capacity: 100, maxDc: 270, connector: 'CCS2', tariff: 14.12, consumption: 20.0 },

    // --- BYD & Zeekr (Китайські електрокари, порт GB/T) ---
    'byd-song-plus': { name: 'BYD Song Plus EV', brand: 'BYD', capacity: 71.7, maxDc: 90, connector: 'GB/T', tariff: 14.12, consumption: 17.0 },
    'byd-tang': { name: 'BYD Tang EV', brand: 'BYD', capacity: 108.8, maxDc: 120, connector: 'GB/T', tariff: 14.12, consumption: 22.0 },
    'byd-yuan-plus': { name: 'BYD Yuan Plus / Atto 3', brand: 'BYD', capacity: 60.5, maxDc: 88, connector: 'GB/T', tariff: 14.12, consumption: 16.0 },
    'zeekr-001': { name: 'Zeekr 001', brand: 'Zeekr', capacity: 100, maxDc: 200, connector: 'GB/T', tariff: 14.12, consumption: 19.0 },
    'zeekr-x': { name: 'Zeekr X', brand: 'Zeekr', capacity: 66, maxDc: 150, connector: 'GB/T', tariff: 14.12, consumption: 17.5 },
    'zeekr-007': { name: 'Zeekr 007', brand: 'Zeekr', capacity: 75, maxDc: 220, connector: 'GB/T', tariff: 14.12, consumption: 16.5 },

    // --- Інші популярні бренди ---
    'renault-zoe': { name: 'Renault Zoe Z.E. 50', brand: 'Renault', capacity: 52, maxDc: 50, connector: 'CCS2', tariff: 14.12, consumption: 15.5 },
    'volvo-ex30': { name: 'Volvo EX30', brand: 'Volvo', capacity: 69, maxDc: 153, connector: 'CCS2', tariff: 14.12, consumption: 17.0 },
    'mg-mg4': { name: 'MG 4 Electric', brand: 'MG', capacity: 64, maxDc: 135, connector: 'CCS2', tariff: 14.12, consumption: 16.5 },
    'ford-mach-e': { name: 'Ford Mustang Mach-E ER', brand: 'Ford', capacity: 98.7, maxDc: 150, connector: 'CCS2', tariff: 14.12, consumption: 20.0 },
    'chevy-bolt': { name: 'Chevrolet Bolt EV', brand: 'Chevrolet', capacity: 65, maxDc: 55, connector: 'CCS2', tariff: 14.12, consumption: 16.0 }
  };

  const BENZIN_PRICE_PER_LITER = 58.50; // грн/л А-95
  const BENZIN_CONSUMPTION_L_100KM = 8.5; // л на 100 км для авто аналогічного класу

  let currentCarKey = 'vw-id4-pro';
  let isManualMode = false;
  let manualCapacity = 65;
  let manualConnector = 'CCS2';

  let startPercent = 20;
  let targetPercent = 80;

  function initCalculator() {
    const carButtons = document.querySelectorAll('.car-pill');
    const carDropdown = document.getElementById('car-select-dropdown');
    const rangeSlider = document.getElementById('calc-range-slider');
    const findBtn = document.getElementById('btn-calc-find');
    const btnToggleManual = document.getElementById('btn-toggle-manual');
    const manualPanel = document.getElementById('calc-manual-panel');
    const manualInput = document.getElementById('manual-kwh-input');
    const portChips = document.querySelectorAll('.manual-ports-row .port-chip');

    if (!rangeSlider) return;

    // Швидкі пресети (пилюлі)
    carButtons.forEach(btn => {
      btn.addEventListener('click', function () {
        isManualMode = false;
        if (manualPanel) manualPanel.style.display = 'none';
        if (btnToggleManual) btnToggleManual.classList.remove('active');

        carButtons.forEach(b => {
          b.classList.remove('active');
          b.setAttribute('aria-checked', 'false');
        });
        this.classList.add('active');
        this.setAttribute('aria-checked', 'true');

        const carKey = this.dataset.car;
        if (CAR_DATABASE[carKey]) {
          currentCarKey = carKey;
          if (carDropdown) carDropdown.value = carKey;
          updateCalculation();
        }
      });
    });

    // Випадаючий список за групами (AutoRia style)
    if (carDropdown) {
      carDropdown.addEventListener('change', function () {
        const selectedKey = this.value;
        if (CAR_DATABASE[selectedKey]) {
          isManualMode = false;
          if (manualPanel) manualPanel.style.display = 'none';
          if (btnToggleManual) btnToggleManual.classList.remove('active');

          currentCarKey = selectedKey;

          // Синхронізуємо активність кнопок пресетів
          carButtons.forEach(btn => {
            const matches = btn.dataset.car === selectedKey;
            btn.classList.toggle('active', matches);
            btn.setAttribute('aria-checked', matches ? 'true' : 'false');
          });

          updateCalculation();
        }
      });
    }

    // Перемикач режиму ручного введення
    if (btnToggleManual && manualPanel) {
      btnToggleManual.addEventListener('click', function () {
        isManualMode = !isManualMode;
        if (isManualMode) {
          manualPanel.style.display = 'block';
          this.classList.add('active');
          carButtons.forEach(b => {
            b.classList.remove('active');
            b.setAttribute('aria-checked', 'false');
          });
          if (carDropdown) carDropdown.value = '';
          if (manualInput) manualCapacity = parseFloat(manualInput.value) || 65;
        } else {
          manualPanel.style.display = 'none';
          this.classList.remove('active');
          // Повертаємо останнє обране авто
          const activeBtn = document.querySelector(`.car-pill[data-car="${currentCarKey}"]`);
          if (activeBtn) {
            activeBtn.classList.add('active');
            activeBtn.setAttribute('aria-checked', 'true');
          }
        }
        updateCalculation();
      });
    }

    // Ручне введення значення кВт·год
    if (manualInput) {
      manualInput.addEventListener('input', function () {
        const val = parseFloat(this.value);
        if (!isNaN(val) && val > 0 && val <= 300) {
          manualCapacity = val;
          updateCalculation();
        }
      });
    }

    // Вибір порту в ручному режимі
    portChips.forEach(chip => {
      chip.addEventListener('click', function () {
        portChips.forEach(c => c.classList.remove('active'));
        this.classList.add('active');
        manualConnector = this.dataset.port || 'CCS2';
        updateCalculation();
      });
    });

    // Повзунок заряду батареї
    rangeSlider.addEventListener('input', function () {
      targetPercent = parseInt(this.value, 10);
      updateCalculation();
    });

    // Кнопка швидкого переходу до карти з фільтром порту
    if (findBtn) {
      findBtn.addEventListener('click', function () {
        const activeCar = getActiveCarData();
        const mapEl = document.getElementById('map');
        if (mapEl) {
          mapEl.scrollIntoView({ behavior: 'smooth' });
        }
        if (window.ChargeUAMap && typeof window.ChargeUAMap.filterByConnector === 'function') {
          window.ChargeUAMap.filterByConnector(activeCar.connector);
        }
      });
    }

    // updateCalculation() is omitted on init since HTML is pre-rendered statically
  }

  // Отримання даних поточного активного авто (або ручних параметрів)
  function getActiveCarData() {
    if (isManualMode) {
      return {
        name: `Власна ємність (${manualCapacity} кВт·год)`,
        brand: 'Користувацьке авто',
        capacity: manualCapacity,
        maxDc: 120,
        connector: manualConnector,
        tariff: 14.12,
        consumption: 18.0
      };
    }
    return CAR_DATABASE[currentCarKey] || CAR_DATABASE['vw-id4-pro'];
  }

  function updateCalculation() {
    const car = getActiveCarData();
    const addedPercent = Math.max(0, targetPercent - startPercent);
    const addedKwh = (addedPercent / 100) * car.capacity;
    const sessionCost = addedKwh * car.tariff;

    // Розрахунок часу на швидкій станції
    const effectiveKw = Math.min(car.maxDc, 120);
    const chargingMinutes = Math.max(5, Math.round((addedKwh / effectiveKw) * 60));

    // Розрахунок економії проти бензину на цей кілометраж
    const kmAdded = (addedKwh / car.consumption) * 100;
    const benzinCost = (kmAdded / 100) * BENZIN_CONSUMPTION_L_100KM * BENZIN_PRICE_PER_LITER;
    const savings = Math.max(0, Math.round(benzinCost - sessionCost + (car.capacity >= 70 ? 550 : 350)));

    // Оновлення тексту повзунка
    const rangeValEl = document.getElementById('slider-range-val');
    if (rangeValEl) {
      rangeValEl.innerHTML = `${startPercent}% &rarr; ${targetPercent}% (Додано +${addedKwh.toFixed(1)} кВт·год)`;
    }

    const sliderFillEl = document.getElementById('slider-fill');
    if (sliderFillEl) {
      sliderFillEl.style.left = `${startPercent}%`;
      sliderFillEl.style.width = `${Math.max(0, targetPercent - startPercent)}%`;
    }

    const sliderBadgeEl = document.getElementById('slider-badge');
    if (sliderBadgeEl) {
      sliderBadgeEl.style.left = `${targetPercent}%`;
      sliderBadgeEl.textContent = `${targetPercent}% (${targetPercent >= 80 ? 'Цільовий' : 'Рівень'})`;
    }

    // Оновлення плашки характеристик активного авто
    const specCarName = document.getElementById('spec-car-name');
    if (specCarName) specCarName.textContent = car.name;

    const specCarKwh = document.getElementById('spec-car-kwh');
    if (specCarKwh) specCarKwh.textContent = `${car.capacity} кВт·год`;

    const specCarPort = document.getElementById('spec-car-port');
    if (specCarPort) {
      specCarPort.textContent = car.connector;
      specCarPort.className = `badge-port badge-port--${car.connector.toLowerCase().replace(/[^a-z0-9]/g, '')}`;
    }

    const specCarDc = document.getElementById('spec-car-dc');
    if (specCarDc) specCarDc.textContent = `до ${car.maxDc} кВт`;

    // Оновлення картки вартості
    const priceEl = document.getElementById('res-price');
    if (priceEl) priceEl.textContent = `${sessionCost.toFixed(2)} ₴`;

    const metaEl = document.getElementById('res-meta');
    if (metaEl) {
      metaEl.textContent = `Тариф: ${car.tariff.toFixed(2)} ₴/кВт·год · ${addedKwh.toFixed(1)} кВт·год енергії`;
    }

    const timeEl = document.getElementById('res-time');
    if (timeEl) timeEl.textContent = `~${chargingMinutes} хвилин`;

    const savingsEl = document.getElementById('res-savings');
    if (savingsEl) savingsEl.textContent = `~${savings.toLocaleString('uk-UA')} ₴`;
  }

  let isCalculatorInitialized = false;
  function ensureCalculatorInit() {
    if (isCalculatorInitialized) return;
    isCalculatorInitialized = true;
    initCalculator();
  }

  function setupLazyCalculator() {
    const calcEl = document.getElementById('calculator');
    if ('IntersectionObserver' in window && calcEl) {
      const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting || entry.intersectionRatio > 0) {
            ensureCalculatorInit();
            observer.disconnect();
          }
        });
      }, { rootMargin: '250px' });
      observer.observe(calcEl);
      calcEl.addEventListener('pointerdown', ensureCalculatorInit, { once: true, passive: true });
      calcEl.addEventListener('focusin', ensureCalculatorInit, { once: true, passive: true });
    } else {
      setTimeout(ensureCalculatorInit, 2000);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupLazyCalculator);
  } else {
    setupLazyCalculator();
  }

  window.ChargeUACalculator = {
    getCars: () => CAR_DATABASE,
    setCar: function (carKey) {
      if (CAR_DATABASE[carKey]) {
        currentCarKey = carKey;
        isManualMode = false;
        updateCalculation();
      }
    }
  };

})();
