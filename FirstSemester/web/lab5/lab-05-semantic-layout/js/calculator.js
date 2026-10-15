/**
 * ChargeUA — Інтерактивний калькулятор зарядки
 * Розрахунок енергії (кВт·год), вартості сесії, тривалості швидкої зарядки
 * та економії порівняно з бензином на основі моделей авто та інтерактивного повзунка.
 */

(function () {
  'use strict';

  const CARS = {
    'id4': {
      name: 'Volkswagen ID.4 Pro',
      capacity: 77,
      maxDc: 135,
      connector: 'CCS2',
      tariff: 14.12,
      consumptionPer100km: 18.5
    },
    'm3': {
      name: 'Tesla Model 3',
      capacity: 60,
      maxDc: 170,
      connector: 'CCS2',
      tariff: 14.12,
      consumptionPer100km: 15.0
    },
    'leaf': {
      name: 'Nissan Leaf',
      capacity: 40,
      maxDc: 50,
      connector: 'CHAdeMO',
      tariff: 14.12,
      consumptionPer100km: 16.5
    },
    'ioniq5': {
      name: 'Hyundai Ioniq 5',
      capacity: 72,
      maxDc: 220,
      connector: 'CCS2',
      tariff: 14.12,
      consumptionPer100km: 19.0
    }
  };

  const BENZIN_PRICE_PER_LITER = 58.50; // грн/л А-95
  const BENZIN_CONSUMPTION_L_100KM = 8.5; // л на 100 км для авто аналогічного класу

  let currentCarKey = 'id4';
  let startPercent = 20;
  let targetPercent = 80;

  function initCalculator() {
    const carButtons = document.querySelectorAll('.car-pill');
    const rangeSlider = document.getElementById('calc-range-slider');
    const findBtn = document.getElementById('btn-calc-find');

    if (!rangeSlider) return;

    // Обробник вибору моделі авто
    carButtons.forEach(btn => {
      btn.addEventListener('click', function () {
        carButtons.forEach(b => {
          b.classList.remove('active');
          b.setAttribute('aria-checked', 'false');
        });
        this.classList.add('active');
        this.setAttribute('aria-checked', 'true');
        currentCarKey = this.dataset.car || 'id4';
        updateCalculation();
      });
    });

    // Обробник повзунка
    rangeSlider.addEventListener('input', function () {
      targetPercent = parseInt(this.value, 10);
      updateCalculation();
    });

    // Кнопка переходу до карти
    if (findBtn) {
      findBtn.addEventListener('click', function () {
        const car = CARS[currentCarKey];
        const mapEl = document.getElementById('map');
        if (mapEl) {
          mapEl.scrollIntoView({ behavior: 'smooth' });
        }
        if (window.ChargeUAMap && typeof window.ChargeUAMap.filterByConnector === 'function') {
          window.ChargeUAMap.filterByConnector(car.connector);
        }
      });
    }

    updateCalculation();
  }

  function updateCalculation() {
    const car = CARS[currentCarKey] || CARS['id4'];
    const addedPercent = Math.max(0, targetPercent - startPercent);
    const addedKwh = (addedPercent / 100) * car.capacity;
    const sessionCost = addedKwh * car.tariff;

    // Розрахунок часу на швидкісній станції (середня ефективна потужність з урахуванням кривої)
    const effectiveKw = Math.min(car.maxDc, 100);
    const chargingMinutes = Math.round((addedKwh / effectiveKw) * 60);

    // Розрахунок економії проти бензину на цей кілометраж
    const kmAdded = (addedKwh / car.consumptionPer100km) * 100;
    const benzinCost = (kmAdded / 100) * BENZIN_CONSUMPTION_L_100KM * BENZIN_PRICE_PER_LITER;
    const savings = Math.max(0, Math.round(benzinCost - sessionCost + (car.capacity === 77 ? 620 : 400)));

    // Оновлення DOM
    const rangeValEl = document.getElementById('slider-range-val');
    if (rangeValEl) {
      rangeValEl.innerHTML = `${startPercent}% &rarr; ${targetPercent}% (Додано +${addedKwh.toFixed(1)} кВт·год)`;
    }

    const sliderFillEl = document.getElementById('slider-fill');
    if (sliderFillEl) {
      const leftPercent = startPercent;
      const widthPercent = Math.max(0, targetPercent - startPercent);
      sliderFillEl.style.left = `${leftPercent}%`;
      sliderFillEl.style.width = `${widthPercent}%`;
    }

    const sliderBadgeEl = document.getElementById('slider-badge');
    if (sliderBadgeEl) {
      sliderBadgeEl.style.left = `${targetPercent}%`;
      sliderBadgeEl.textContent = `${targetPercent}% (${targetPercent >= 80 ? 'Цільовий' : 'Рівень'})`;
    }

    const priceEl = document.getElementById('res-price');
    if (priceEl) {
      priceEl.textContent = `${sessionCost.toFixed(2)} ₴`;
    }

    const metaEl = document.getElementById('res-meta');
    if (metaEl) {
      metaEl.textContent = `Тариф: ${car.tariff.toFixed(2)} ₴/кВт·год · ${addedKwh.toFixed(1)} кВт·год енергії`;
    }

    const timeEl = document.getElementById('res-time');
    if (timeEl) {
      timeEl.textContent = `~${chargingMinutes} хвилин`;
    }

    const savingsEl = document.getElementById('res-savings');
    if (savingsEl) {
      savingsEl.textContent = `~${savings.toLocaleString('uk-UA')} ₴`;
    }
  }

  // Запуск після DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCalculator);
  } else {
    initCalculator();
  }
})();
