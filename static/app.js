/* ── Generic fetch wrapper ──────────────────────────────────────────────── */
async function fetchAndRender(endpoint, containerId, renderFn) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.innerHTML = '<div class="skeleton" style="height:80px;width:100%;"></div>';
  try {
    const res = await fetch(endpoint);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    renderFn(data, container);
  } catch (err) {
    container.innerHTML = `<p class="text-red-400 text-sm p-3">Error: ${err.message}</p>`;
  }
}

/* ── animateProgressBars ─────────────────────────────────────────────────── */
function animateProgressBars() {
  const bars = document.querySelectorAll('[data-progress]');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.style.width = e.target.dataset.progress + '%';
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.1 });
  bars.forEach(b => observer.observe(b));
}

/* ── Coverage bars ───────────────────────────────────────────────────────── */
function animateCoverageBars() {
  setTimeout(() => {
    document.querySelectorAll('.cov-bar[data-cov]').forEach(el => {
      el.style.width = el.dataset.cov + '%';
    });
  }, 300);
}

/* ── copyToClipboard ─────────────────────────────────────────────────────── */
function copyToClipboard(elementId) {
  const el = document.getElementById(elementId);
  if (!el) return;
  navigator.clipboard.writeText(el.innerText || el.textContent).then(() => {
    const btn = document.getElementById('copy-btn');
    if (btn) { btn.textContent = '✓ Copiado'; setTimeout(() => { btn.textContent = 'Copiar'; }, 2000); }
  });
}

/* ── renderTests ─────────────────────────────────────────────────────────── */
function renderTests(tests, container) {
  container.innerHTML = tests.map(t => {
    const pct = Math.round((t.passed / t.total) * 100);
    return `
      <div class="card flex flex-col gap-3">
        <div class="flex items-center justify-between">
          <h3 class="font-semibold text-sm text-white">${t.type}</h3>
          <span class="task-type-badge" style="background:rgba(34,197,94,0.15);color:#4ade80;border-color:rgba(34,197,94,0.3);">
            ${t.passed}/${t.total} ✓
          </span>
        </div>
        <div class="progress-bar-track">
          <div class="progress-bar bg-green-500" data-progress="${pct}"></div>
        </div>
        <p class="text-xs text-[#8888aa]">${t.description}</p>
      </div>`;
  }).join('');
  animateProgressBars();
}

/* ── renderBugs ──────────────────────────────────────────────────────────── */
function renderBugs(bugs, container) {
  container.innerHTML = `
    <table class="data-table">
      <thead>
        <tr><th>ID</th><th>Descripción</th><th>Severidad</th><th>Estado</th><th>Resuelto por</th></tr>
      </thead>
      <tbody>
        ${bugs.map(b => `
          <tr>
            <td><span class="task-id">#${b.id}</span></td>
            <td class="text-sm">${b.description}</td>
            <td>${severityBadge(b.severity)}</td>
            <td><span class="text-green-400 text-xs font-semibold">Resuelto ✓</span></td>
            <td class="text-sm text-[#e8e8f0]">${b.resolved_by}</td>
          </tr>`).join('')}
      </tbody>
    </table>`;
}

function severityBadge(s) {
  const map = {
    alta:  'background:rgba(239,68,68,0.15);color:#f87171;border-color:rgba(239,68,68,0.3);',
    media: 'background:rgba(249,115,22,0.15);color:#fb923c;border-color:rgba(249,115,22,0.3);',
    baja:  'background:rgba(107,114,128,0.15);color:#9ca3af;border-color:rgba(107,114,128,0.3);',
  };
  return `<span class="task-type-badge" style="${map[s] || ''}">${s}</span>`;
}

/* ── renderMetrics (development page) ───────────────────────────────────── */
function renderMetrics(metrics, container) {
  container.innerHTML = metrics.map(m => `
    <div class="card text-center p-4">
      <div class="text-2xl mb-1">${m.icon}</div>
      <div class="text-xl font-bold text-white mb-0.5">${m.value}</div>
      <div class="text-xs text-[#8888aa]">${m.label}</div>
    </div>
  `).join('');
}

/* ── Page init ───────────────────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  const page = document.body.dataset.page;

  animateProgressBars();
  animateCoverageBars();

  if (page === 'development') {
    fetchAndRender('/api/metrics', 'metrics-container', renderMetrics);
  }

  if (page === 'testing') {
    fetchAndRender('/api/tests', 'tests-container', renderTests);
    fetchAndRender('/api/bugs',  'bugs-container',  renderBugs);
  }
});
