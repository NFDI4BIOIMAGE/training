const state = {
  resources: [],
  filtered: [],
  activeTag: null,
  activeLicense: null,
  activeKeyword: null,
};

const searchInput = document.querySelector("#search");
const results = document.querySelector("#results");
const summary = document.querySelector("#summary");
const tagsContainer = document.querySelector("#tags");
const licensesContainer = document.querySelector("#licenses");
const keywordsContainer = document.querySelector("#keywords");
const searchPanel = searchInput.closest(".panel");
const resultsPanel = results.closest(".panel");
const overviewPanels = Array.from(document.querySelectorAll("main > section")).filter((section) => section !== searchPanel && section !== resultsPanel);

const asArray = (value) => (Array.isArray(value) ? value : value ? [value] : []);
const joinValues = (value) => asArray(value).join(", ");

function makeChip(label, count, onClick, isActive) {
  const button = document.createElement("button");
  button.className = `chip ${isActive ? "active" : ""}`.trim();
  button.type = "button";
  button.textContent = count !== undefined ? `${label} (${count})` : label;
  button.addEventListener("click", onClick);
  return button;
}

function renderChips(data, container, kind) {
  container.innerHTML = "";
  data.forEach(({ value, count }) => {
    const isActive = (kind === "tag" && state.activeTag === value)
      || (kind === "license" && state.activeLicense === value)
      || (kind === "keyword" && state.activeKeyword === value);

    container.appendChild(makeChip(value, count, () => {
      if (kind === "tag") {
        state.activeTag = state.activeTag === value ? null : value;
      }
      if (kind === "license") {
        state.activeLicense = state.activeLicense === value ? null : value;
      }
      if (kind === "keyword") {
        state.activeKeyword = state.activeKeyword === value ? null : value;
      }
      applyFilters();
      renderFilters(window.trainingData);
    }, isActive));
  });
}

function renderFilters(data) {
  renderChips(data.mostCommonTags, tagsContainer, "tag");
  renderChips(data.mostCommonLicenses, licensesContainer, "license");
  renderChips(data.keywords.map((k) => ({ value: k })), keywordsContainer, "keyword");
}

function applyFilters() {
  const query = searchInput.value.trim().toLowerCase();
  const hasQuery = query.length > 0;

  state.filtered = state.resources.filter((resource) => {
    const matchesQuery = !query || (resource.searchText || "").toLowerCase().includes(query);
    const matchesTag = !state.activeTag || asArray(resource.tags).some((tag) => String(tag).toLowerCase() === state.activeTag.toLowerCase());
    const matchesLicense = !state.activeLicense || String(resource.license || "").toLowerCase() === state.activeLicense.toLowerCase();
    const matchesKeyword = !state.activeKeyword || (resource.searchText || "").toLowerCase().includes(state.activeKeyword.toLowerCase());
    return matchesQuery && matchesTag && matchesLicense && matchesKeyword;
  });

  resultsPanel.classList.toggle("is-hidden", !hasQuery);
  overviewPanels.forEach((panel) => panel.classList.toggle("is-hidden", hasQuery));

  renderResults();
}

function renderResults() {
  results.innerHTML = "";

  if (!searchInput.value.trim()) {
    summary.textContent = "Start typing to show matching resources.";
    return;
  }

  summary.textContent = `${state.filtered.length} of ${state.resources.length} resources shown`;

  state.filtered.forEach((resource) => {
    const card = document.createElement("article");
    card.className = "result";
    card.innerHTML = `
      <h3><a href="${resource.url}" target="_blank" rel="noopener noreferrer">${resource.name || resource.url}</a></h3>
      <p><strong>Authors:</strong> ${joinValues(resource.authors) || "n/a"}</p>
      <p><strong>Tags:</strong> ${joinValues(resource.tags) || "n/a"}</p>
      <p><strong>Type:</strong> ${joinValues(resource.type) || "n/a"}</p>
      <p><strong>License:</strong> ${resource.license || "unknown"}</p>
    `;
    results.appendChild(card);
  });
}

function renderList(selector, rows, formatter) {
  const target = document.querySelector(selector);
  target.innerHTML = "";
  rows.forEach((row) => {
    const li = document.createElement("li");
    li.innerHTML = formatter(row);
    target.appendChild(li);
  });
}

function renderStats(data) {
  const statsRows = [
    `Total resources: <strong>${data.totalResources}</strong>`,
    `Distinct tags: <strong>${data.mostCommonTags.length}</strong> (showing top 20)`,
    `Distinct licenses: <strong>${data.mostCommonLicenses.length}</strong> (showing top 10)`,
    `Distinct resource types: <strong>${data.mostCommonTypes.length}</strong> (showing top 10)`,
  ];
  renderList("#stats", statsRows, (row) => row);
}

async function init() {
  const response = await fetch("data.json");
  const data = await response.json();
  window.trainingData = data;

  state.resources = data.resources;
  state.filtered = data.resources;

  renderFilters(data);
  renderStats(data);

  renderList("#recent", data.recentAdditions, (row) => `<a href="${row.url}" target="_blank" rel="noopener noreferrer">${row.name || row.url}</a>`);
  renderList("#downloads", data.topDownloads, (row) => `<a href="${row.url}" target="_blank" rel="noopener noreferrer">${row.name}</a> (+${row.download_difference})`);

  searchInput.addEventListener("input", applyFilters);
  applyFilters();
}

init();
