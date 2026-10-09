(() => {
  'use strict';
  const form = document.getElementById('calculator');
  const result = document.getElementById('result');
  if (!form || !result) return;
  const lang = form.dataset.language === 'en' ? 'en' : 'id';
  const compare = form.dataset.tool === 'compare';
  const words = lang === 'id' ? {
    invalid: 'Masukkan angka yang valid. Jam harus 0–24; hari dan jumlah unit harus lebih dari nol.',
    kwh: 'kWh selama periode ini', optionA: 'Pilihan A', optionB: 'Pilihan B',
    bmore: 'Pilihan B memakai lebih banyak', bless: 'Pilihan B memakai lebih sedikit', equal: 'Kedua pilihan memakai energi yang sama',
    energyCost: 'Perkiraan biaya energi', costDifference: 'Perkiraan selisih biaya energi',
    noRate: 'Tarif belum diisi; biaya tidak dihitung.',
    assumption: 'Perkiraan menganggap daya konstan. Tagihan nyata dapat mencakup biaya lain.'
  } : {
    invalid: 'Enter valid numbers. Hours must be 0–24; days and quantity must be greater than zero.',
    kwh: 'kWh for this period', optionA: 'Option A', optionB: 'Option B',
    bmore: 'Option B uses more', bless: 'Option B uses less', equal: 'Both options use the same energy',
    energyCost: 'Estimated energy charge', costDifference: 'Estimated energy-charge difference',
    noRate: 'No rate entered; cost is not calculated.',
    assumption: 'The estimate assumes constant power. An actual bill can include other charges.'
  };
  const value = id => Number(form.elements.namedItem(id).value);
  const formatted = n => new Intl.NumberFormat(lang === 'id' ? 'id-ID' : 'en-US', { maximumFractionDigits: 3 }).format(n);
  const line = (label, number, unit) => {
    const li = document.createElement('li');
    li.textContent = `${label}: ${formatted(number)} ${unit}`;
    return li;
  };
  form.addEventListener('submit', event => {
    event.preventDefault();
    const hours = value('hours');
    const days = value('days');
    const quantity = value('quantity');
    const rateText = form.elements.namedItem('rate').value.trim();
    const rate = rateText === '' ? null : Number(rateText);
    const currency = form.elements.namedItem('currency').value.trim().slice(0, 12);
    const power = compare ? [value('power-a'), value('power-b')] : [value('power')];
    const valid = power.every(n => Number.isFinite(n) && n >= 0 && n <= 20000)
      && Number.isFinite(hours) && hours >= 0 && hours <= 24
      && Number.isFinite(days) && days > 0 && days <= 366
      && Number.isInteger(quantity) && quantity > 0 && quantity <= 100
      && (rate === null || Number.isFinite(rate) && rate >= 0 && rate <= 10000000);
    if (!valid) {
      result.replaceChildren();
      const message = document.createElement('p');
      message.textContent = words.invalid;
      result.append(message);
      return;
    }
    const kwh = power.map(watts => watts * hours * days * quantity / 1000);
    result.replaceChildren();
    const kicker = document.createElement('span');
    kicker.className = 'eyebrow';
    kicker.textContent = lang === 'id' ? 'HASIL PERKIRAAN' : 'ESTIMATED RESULT';
    const headline = document.createElement('strong');
    const list = document.createElement('ul');
    if (compare) {
      const difference = kwh[1] - kwh[0];
      headline.textContent = `${formatted(Math.abs(difference))} kWh`;
      list.append(line(words.optionA, kwh[0], words.kwh), line(words.optionB, kwh[1], words.kwh));
      const li = document.createElement('li');
      li.textContent = difference === 0 ? words.equal : `${difference > 0 ? words.bmore : words.bless}: ${formatted(Math.abs(difference))} kWh`;
      list.append(li);
      if (rate !== null) list.append(line(words.costDifference, Math.abs(difference) * rate, currency));
    } else {
      headline.textContent = `${formatted(kwh[0])} kWh`;
      if (rate !== null) list.append(line(words.energyCost, kwh[0] * rate, currency));
    }
    const note = document.createElement('p');
    note.textContent = `${rate === null ? words.noRate + ' ' : ''}${words.assumption}`;
    result.append(kicker, headline, list, note);
    if (typeof window.gtag === 'function') window.gtag('event', 'calculator_used', { tool_name: form.dataset.tool, language: lang });
  });
})();
