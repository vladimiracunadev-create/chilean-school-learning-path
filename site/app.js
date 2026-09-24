const $ = (selector) => document.querySelector(selector);
const state = { all: [], filtered: [], shown: 24 };
const controls = { query: $("#q"), level: $("#level"), subject: $("#subject"), coverage: $("#coverage") };

function escapeHtml(value) {
  return String(value).replace(/[&<>'"]/g, (character) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" })[character]);
}

function unique(key) {
  return [...new Set(state.all.map((item) => item[key]))].sort((a, b) => a.localeCompare(b, "es"));
}

function appendOptions(control, values) {
  control.insertAdjacentHTML("beforeend", values.map((value) => `<option value="${escapeHtml(value)}">${escapeHtml(value)}</option>`).join(""));
}

function normalize(value) {
  return value.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
}

function card(item) {
  const developed = item.editorial_status === "desarrollada";
  return `<article class="card">
    <div class="card-top"><span class="tag">${escapeHtml(item.course)}</span><span class="card-status ${developed ? "developed" : ""}">${developed ? "Desarrollada" : "Secuenciada"}</span><span class="card-index">${escapeHtml(item.class_code)}</span></div>
    <p class="meta">${escapeHtml(item.subject)} · ${escapeHtml(item.oa_code)}</p>
    <h3>${escapeHtml(item.topic)}</h3>
    <p class="axis">${escapeHtml(item.axis)}</p>
    <div class="card-footer"><p class="phase">${escapeHtml(item.phase)}<br>${item.lesson} de ${item.lesson_count}</p><a class="card-link" href="${escapeHtml(item.web_path)}" aria-label="Abrir ${escapeHtml(item.oa_code)}">Abrir →</a></div>
  </article>`;
}

function updateUrl() {
  const params = new URLSearchParams();
  if (controls.query.value.trim()) params.set("q", controls.query.value.trim());
  if (controls.level.value) params.set("nivel", controls.level.value);
  if (controls.subject.value) params.set("asignatura", controls.subject.value);
  if (controls.coverage.value) params.set("cobertura", controls.coverage.value);
  history.replaceState(null, "", `${location.pathname}${params.size ? `?${params}` : ""}${location.hash}`);
}

function render(reset = true) {
  if (reset) state.shown = 24;
  const term = normalize(controls.query.value.trim());
  state.filtered = state.all.filter((item) => {
    const haystack = normalize(`${item.topic} ${item.oa_code} ${item.oa_text} ${item.axis} ${item.subject}`);
    return (!term || haystack.includes(term)) && (!controls.level.value || item.course === controls.level.value) && (!controls.subject.value || item.subject === controls.subject.value) && (!controls.coverage.value || item.coverage === controls.coverage.value);
  });
  const visible = state.filtered.slice(0, state.shown);
  $("#result").textContent = `${state.filtered.length.toLocaleString("es-CL")} ${state.filtered.length === 1 ? "clase encontrada" : "clases encontradas"}`;
  $("#cards").innerHTML = visible.length ? visible.map(card).join("") : '<div class="empty-state"><h3>Sin coincidencias</h3><p>Prueba una palabra más amplia o limpia los filtros.</p></div>';
  $("#load-more").hidden = visible.length >= state.filtered.length;
  updateUrl();
}

function restoreFilters() {
  const params = new URLSearchParams(location.search);
  controls.query.value = params.get("q") || "";
  controls.level.value = params.get("nivel") || "";
  controls.subject.value = params.get("asignatura") || "";
  controls.coverage.value = params.get("cobertura") || "";
}

function setTheme(theme) {
  document.documentElement.dataset.theme = theme;
  localStorage.setItem("trayectoria-theme", theme);
  $("#theme-toggle").setAttribute("aria-label", theme === "dark" ? "Activar tema claro" : "Activar tema oscuro");
}

setTheme(localStorage.getItem("trayectoria-theme") || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light"));
$("#theme-toggle").addEventListener("click", () => setTheme(document.documentElement.dataset.theme === "dark" ? "light" : "dark"));
Object.values(controls).forEach((control) => control.addEventListener("input", () => render(true)));
$("#clear-filters").addEventListener("click", () => { Object.values(controls).forEach((control) => { control.value = ""; }); render(true); controls.query.focus(); });
$("#load-more").addEventListener("click", () => { state.shown += 24; render(false); });

fetch("catalog.json")
  .then((response) => { if (!response.ok) throw new Error(`HTTP ${response.status}`); return response.json(); })
  .then((catalog) => {
    state.all = catalog.classes;
    $("#stats").innerHTML = [
      [catalog.course_count, "niveles"], [catalog.objective_count, "OA inventariados"], [catalog.class_count, "clases"], [catalog.editorial_counts.desarrollada, "clases desarrolladas"], [catalog.reading_link_count, "lecturas vinculadas"]
    ].map(([value, label]) => `<div class="stat"><strong>${value.toLocaleString("es-CL")}</strong><span>${label}</span></div>`).join("");
    appendOptions(controls.level, unique("course"));
    appendOptions(controls.subject, unique("subject"));
    appendOptions(controls.coverage, unique("coverage"));
    restoreFilters();
    render(true);
  })
  .catch(() => {
    $("#result").textContent = "No pudimos cargar el catálogo.";
    $("#cards").innerHTML = '<div class="empty-state"><h3>Catálogo no disponible</h3><p>Revisa tu conexión y vuelve a cargar la página.</p><button class="button dark-text" type="button" onclick="location.reload()">Reintentar</button></div>';
  });
