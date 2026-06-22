const state = {
  resources: [],
  filtered: [],
  activeTag: null,
  activeLicense: null,
  activeType: null,
};

const searchInput = document.querySelector("#search");
const results = document.querySelector("#results");
const summary = document.querySelector("#summary");
const tagsContainer = document.querySelector("#tags");
const licensesContainer = document.querySelector("#licenses");
const typesContainer = document.querySelector("#types");
const searchPanel = searchInput.closest(".panel");
const resultsPanel = results.closest(".panel");
const overviewPanels = Array.from(document.querySelectorAll(".overview-panel"));

const asArray = (value) => (Array.isArray(value) ? value : value ? [value] : []);
const joinValues = (value) => asArray(value).join(", ");
const toUrlList = (value) => asArray(value)
  .flatMap((entry) => String(entry || "").split(","))
  .map((url) => url.trim())
  .filter(Boolean);

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
    if (count > 5) { // only show filters that apply to at least 5 resources
      const isActive = (kind === "tag" && state.activeTag === value)
        || (kind === "license" && state.activeLicense === value)
        || (kind === "type" && state.activeType === value);

      container.appendChild(makeChip(value, count, () => {
        if (kind === "tag") {
          state.activeTag = state.activeTag === value ? null : value;
        }
        if (kind === "license") {
          state.activeLicense = state.activeLicense === value ? null : value;
        }
        if (kind === "type") {
          state.activeType = state.activeType === value ? null : value;
        }
        applyFilters();
        renderFilters(window.trainingData);
      }, isActive));
    }
  });
}

function renderFilters(data) {
  renderChips(data.mostCommonTags, tagsContainer, "tag");
  renderChips(data.mostCommonLicenses, licensesContainer, "license");
  renderChips(data.mostCommonTypes, typesContainer, "type");
}

function applyFilters() {
  const query = searchInput.value.trim().toLowerCase();
  const hasQuery = query.length > 0 || state.activeTag || state.activeLicense || state.activeType;

  state.filtered = state.resources.filter((resource) => {
    const matchesQuery = !query || (resource.searchText || "").toLowerCase().includes(query);
    const matchesTag = !state.activeTag || asArray(resource.tags).some((tag) => String(tag).toLowerCase() === state.activeTag.toLowerCase());
    const matchesLicense = !state.activeLicense || String(resource.license || "").toLowerCase() === state.activeLicense.toLowerCase();
    const matchesType = !state.activeType || asArray(resource.type).some((type) => String(type).toLowerCase() === state.activeType.toLowerCase());
    return matchesQuery && matchesTag && matchesLicense && matchesType;
  });

  resultsPanel.classList.toggle("is-hidden", !hasQuery);
  overviewPanels.forEach((panel) => panel.classList.toggle("is-hidden", hasQuery));

  renderResults();
}

function renderResults() {
  results.innerHTML = "";

  const hasInputOrFilter = Boolean(
    searchInput.value.trim() || state.activeTag || state.activeLicense || state.activeType,
  );

  if (!hasInputOrFilter) {
    summary.textContent = "Start typing to show matching resources.";
    return;
  }

  summary.textContent = `${state.filtered.length} of ${state.resources.length} resources shown`;

  state.filtered.forEach((resource) => {
    const urls = toUrlList(resource.url);
    const primaryUrl = urls[0] || "";
    const authors = joinValues(resource.authors);
    const tags = joinValues(resource.tags);
    const types = joinValues(resource.type);
    const license = resource.license;
    const description = resource.description
      ? String(resource.description).slice(0, 330)
      : "";

    const detailsLinks = urls
      .slice(0, 2)
      .map((url) => `<a href="${url}" target="_blank" rel="noopener noreferrer">${url}</a>`)
      .join(" · ");

    const metaItems = [
      license && `<span>License: ${license}</span>`,
      types && `<span>Type: ${types}</span>`,
      tags && `<span>Tags: ${tags}</span>`,
    ].filter(Boolean).join("");

    const card = document.createElement("article");
    card.className = "result";
    card.innerHTML = `
      <h3>${primaryUrl
        ? `<a href="${primaryUrl}" target="_blank" rel="noopener noreferrer">${resource.name || primaryUrl}</a>`
        : `${resource.name || "Untitled resource"}`}</h3>
      ${authors ? `<p><strong>Authors:</strong> ${authors}</p>` : ""}
      ${description ? `<p>${description}</p>` : ""}
      ${metaItems ? `<div class="result-meta">${metaItems}</div>` : ""}
      ${detailsLinks ? `<div class="result-links">${detailsLinks}</div>` : ""}
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
    `Distinct tags: <strong>${data.mostCommonTags.length}</strong>`,
    `Distinct licenses: <strong>${data.mostCommonLicenses.length}</strong>`,
    `Distinct resource types: <strong>${data.mostCommonTypes.length}</strong>`,
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
