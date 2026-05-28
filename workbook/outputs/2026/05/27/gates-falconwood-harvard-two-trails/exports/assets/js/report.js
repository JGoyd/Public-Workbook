(function () {
  const data = window.DISCLOSURE_DATA || {};
  const state = {
    filter: "all",
    search: ""
  };

  function escapeHtml(value) {
    return String(value || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  function slug(value) {
    return String(value || "").replace(/[^a-zA-Z0-9_-]/g, "_");
  }

  function label(value) {
    const labels = {
      screenshot_done: "rendered pages",
      source_pdf_found: "source PDF",
      ocr_only: "search gap",
      direct_text: "direct text",
      strong_continuation: "continuation",
      pattern_support: "pattern support",
      context_only: "context only",
      quarantine: "unresolved",
      closed_for_packet: "closed for this packet",
      partly_closed: "partly resolved",
      still_open: "still open",
      not_established: "not established"
    };
    return labels[value] || String(value || "");
  }

  function requestedSet(element, attr) {
    const raw = element && element.dataset ? element.dataset[attr] || "" : "";
    const values = raw.split(",").map((item) => item.trim()).filter(Boolean);
    return values.length ? new Set(values) : null;
  }

  function setCounts() {
    const meta = data.meta || {};
    setText("sourcePdfCount", meta.sourcePdfCount || 0);
    setText("screenshotCount", meta.screenshotCount || 0);
    setText("claimCount", meta.claimCount || 0);
  }

  function setText(id, value) {
    const el = document.getElementById(id);
    if (el) el.textContent = value;
  }

  function renderTimeline() {
    const root = document.getElementById("timeline");
    if (!root) return;
    root.innerHTML = (data.timeline || []).map((item) => `
      <article class="timeline-item">
        <span class="timeline-date">${escapeHtml(item.date)}</span>
        <h3>${escapeHtml(item.title)}</h3>
        <p>${escapeHtml(item.body)}</p>
        <span class="timeline-claim">${escapeHtml(item.claim)}</span>
      </article>
    `).join("");
  }

  function sourceLink(efta) {
    return `assets/source_pdfs/${encodeURIComponent(efta)}.pdf`;
  }

  function screenshotPath(name) {
    return `assets/screenshots/${encodeURIComponent(name)}`;
  }

  function renderEvidenceCards() {
    const root = document.getElementById("evidenceGrid");
    if (!root) return;

    const ids = requestedSet(root, "ids");
    const cards = (data.evidenceCards || []).filter((card) => !ids || ids.has(card.id));

    root.innerHTML = cards.map((card) => {
      const screenshots = card.screenshots || [];
      const first = screenshots[0];
      const thumbs = screenshots.slice(1, 4).map((shot) => `
        <button type="button" data-lightbox-src="${screenshotPath(shot)}" data-lightbox-title="${escapeHtml(card.id)} - ${escapeHtml(shot)}">
          <img src="${screenshotPath(shot)}" alt="${escapeHtml(card.id)} supporting screenshot ${escapeHtml(shot)}" loading="lazy">
        </button>
      `).join("");
      const eftaLinks = (card.eftas || []).map((efta) => `
        <a href="${sourceLink(efta)}">${escapeHtml(efta)}</a>
      `).join("");

      return `
        <article class="evidence-card" id="${escapeHtml(card.id)}">
          <div class="evidence-media">
            <button type="button" data-lightbox-src="${screenshotPath(first)}" data-lightbox-title="${escapeHtml(card.id)} - ${escapeHtml(first)}">
              <img src="${screenshotPath(first)}" alt="${escapeHtml(card.id)} primary source screenshot" loading="lazy">
            </button>
            <div class="thumb-row">${thumbs}</div>
          </div>
          <div>
            <span class="card-kicker">${escapeHtml(card.id)} / ${escapeHtml(card.lane)}</span>
            <h3>${escapeHtml(card.label)}</h3>
            <p>${escapeHtml(card.summary)}</p>
            <div class="efta-list">${eftaLinks}</div>
            <span class="tag proof-${slug(card.proof)}">${escapeHtml(label(card.proof))}</span>
            <div class="card-caution">${escapeHtml(card.caution)}</div>
          </div>
        </article>
      `;
    }).join("");
  }

  function renderClaims() {
    const root = document.getElementById("claimRows");
    if (!root) return;

    const search = state.search.trim().toLowerCase();
    const ids = requestedSet(root, "ids");
    const rows = (data.claims || []).filter((claim) => {
      if (ids && !ids.has(claim.claim_id)) return false;
      const proofMatch = state.filter === "all"
        || claim.proof_status === state.filter
        || claim.confidence === state.filter;
      const blob = Object.values(claim).join(" ").toLowerCase();
      return proofMatch && (!search || blob.includes(search));
    });

    root.innerHTML = rows.map((claim) => `
      <tr>
        <td><strong>${escapeHtml(claim.claim_id)}</strong><br>${escapeHtml(claim.claim_limited_summary)}</td>
        <td>${escapeHtml(claim.lane)}</td>
        <td>${escapeHtml(claim.evidence_eftas)}</td>
        <td><span class="tag proof-${slug(claim.proof_status)}">${escapeHtml(label(claim.proof_status))}</span></td>
        <td><span class="tag confidence-${slug(claim.confidence)}">${escapeHtml(label(claim.confidence))}</span></td>
        <td>${escapeHtml(claim.caution)}</td>
        <td>${escapeHtml(claim.next_gap)}</td>
      </tr>
    `).join("");
  }

  function renderGallery() {
    const root = document.getElementById("galleryGrid");
    if (!root) return;

    const eftas = requestedSet(root, "eftas");
    const screenshots = (data.screenshots || []).filter((shot) => !eftas || eftas.has(shot.efta));

    root.innerHTML = screenshots.map((shot) => {
      const path = shot.asset_path || screenshotPath(`${shot.efta}-${shot.page}.png`);
      const label = `${shot.efta} page ${shot.page}`;
      return `
        <button class="gallery-button" type="button" data-lightbox-src="${escapeHtml(path)}" data-lightbox-title="${escapeHtml(label)}">
          <img src="${escapeHtml(path)}" alt="${escapeHtml(label)}" loading="lazy">
          <span>${escapeHtml(label)}</span>
        </button>
      `;
    }).join("");
  }

  function renderOpenItems() {
    const root = document.getElementById("openItems");
    if (!root) return;

    root.innerHTML = (data.openItems || []).map((item) => `
      <article class="open-card ${slug(item.status)}">
        <span class="tag">${escapeHtml(label(item.status))}</span>
        <h3>${escapeHtml(item.open_item)}</h3>
        <p>${escapeHtml(item.result)}</p>
        <p><strong>Evidence:</strong> ${escapeHtml(item.evidence)}</p>
        <p><strong>Next drill:</strong> ${escapeHtml(item.next_drill)}</p>
      </article>
    `).join("");
  }

  function bindFilters() {
    document.querySelectorAll(".filter-button").forEach((button) => {
      button.addEventListener("click", () => {
        document.querySelectorAll(".filter-button").forEach((item) => item.classList.remove("active"));
        button.classList.add("active");
        state.filter = button.dataset.filter || "all";
        renderClaims();
      });
    });

    const search = document.getElementById("ledgerSearch");
    if (search) {
      search.addEventListener("input", () => {
        state.search = search.value || "";
        renderClaims();
      });
    }
  }

  function bindLightbox() {
    const lightbox = document.getElementById("lightbox");
    const image = document.getElementById("lightboxImage");
    const title = document.getElementById("lightboxTitle");
    const close = document.getElementById("lightboxClose");
    if (!lightbox || !image || !title || !close) return;

    document.body.addEventListener("click", (event) => {
      const trigger = event.target.closest("[data-lightbox-src]");
      if (!trigger) return;
      image.src = trigger.dataset.lightboxSrc;
      image.alt = trigger.dataset.lightboxTitle || "Source screenshot";
      title.textContent = trigger.dataset.lightboxTitle || "Source screenshot";
      lightbox.hidden = false;
      close.focus();
    });

    function hide() {
      lightbox.hidden = true;
      image.removeAttribute("src");
    }

    close.addEventListener("click", hide);
    lightbox.addEventListener("click", (event) => {
      if (event.target === lightbox) hide();
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && !lightbox.hidden) hide();
    });
  }

  function init() {
    setCounts();
    renderTimeline();
    renderEvidenceCards();
    renderClaims();
    renderGallery();
    renderOpenItems();
    bindFilters();
    bindLightbox();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
