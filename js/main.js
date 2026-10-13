const filters = document.querySelector('.skill-filters');
const skillCards = [...document.querySelectorAll('[data-category]')];
const filterStatus = document.querySelector('#filter-status');

if (filters && filterStatus && skillCards.length) {
  filters.hidden = false;
  filters.addEventListener('click', (event) => {
    const button = event.target.closest('[data-filter]');
    if (!button) return;

    for (const option of filters.querySelectorAll('[data-filter]')) {
      option.setAttribute('aria-pressed', String(option === button));
    }
    for (const card of skillCards) {
      card.hidden = button.dataset.filter !== 'all'
        && card.dataset.category !== button.dataset.filter;
    }
    const count = skillCards.filter((card) => !card.hidden).length;
    filterStatus.textContent = `${button.textContent}: ${count} ${count === 1 ? 'área visible' : 'áreas visibles'}.`;
  });
}
