
// ==========================================
// URJA 2K26 - DYNAMIC GALLERY CONFIGURATION
// ==========================================
window.GALLERY_FOLDERS = {
  'all': [],
  'faces-of-urja': '1FcBN3XDFI1EaGF8_BYo32MXgz0sOYJwc',
  'decoration': '15UuVrTpl4BwvEHFfBG5PaAdgNlosDRG4',
  'aavishkar': '1-IiZ2RgbBHEOtA5xr4q96-vGkVj1IYpj',
  'f1-arena': '1WRO_4ZZO9KlCf1EggBrvRogYa52lcU99',
  'sync': '1R9N-o3Ync67tXlq-zy-C-uua1FYvnnq5',
  'power-up': '10ALIJTnDRi5YqGgmOrNPutoqdnnAgaYL',
  'abhivyakti': '1za0r7_iJHhJ8Z6RsBG19dxbvzXyY7j-8',
  'human-ludo': '18Ra-tq2T6DeyEDMebzpBGGTX5tZbmJ7R',
  'game-of-drones': '14TMqd7PTSOIo4zxMpEpo7HbiphAaYADw',
  'quiz-whiz': '1Ojcay4X3QwV0vv6k-6zOPzYcNqSkxqoq',
  'escape': '1RQzMq1OE0gDk0WUPd0C8Gq50VTvHVRBR',
  'clash-of-minds': '1A44_IMt9Q0eN0us-dvBlqTJR1Q0xq4CD',
  'robo-soccer': '1Jmm__VANf3PXwE02P8RjbGj_Qj9LPQ51'
};

(function initGallery() {
  const btnMemories = document.getElementById('gal-btn-memories');
  const btnCurrent = document.getElementById('gal-btn-current');
  const viewMemories = document.getElementById('gallery-memories');
  const viewCurrent = document.getElementById('gallery-current');

  if(btnMemories && btnCurrent) {
    btnMemories.addEventListener('click', () => {
      btnMemories.classList.add('active');
      btnCurrent.classList.remove('active');
      viewMemories.style.display = 'block'; viewMemories.removeAttribute('hidden');
      viewCurrent.style.display = 'none'; viewCurrent.setAttribute('hidden', '');
      viewMemories.querySelectorAll('[data-reveal]').forEach(el => el.classList.add('visible'));
    });
    
    btnCurrent.addEventListener('click', () => {
      btnCurrent.classList.add('active');
      btnMemories.classList.remove('active');
      viewCurrent.style.display = 'block'; viewCurrent.removeAttribute('hidden');
      viewMemories.style.display = 'none'; viewMemories.setAttribute('hidden', '');
      viewCurrent.querySelectorAll('[data-reveal]').forEach(el => el.classList.add('visible'));
    });
    
    viewMemories.style.display = 'block'; viewMemories.removeAttribute('hidden');
      viewCurrent.style.display = 'none'; viewCurrent.setAttribute('hidden', '');
    setTimeout(() => {
      viewMemories.querySelectorAll('[data-reveal]').forEach(el => el.classList.add('visible'));
    }, 100);
  }

  const chips = document.querySelectorAll('.gchip');
  const grid = document.getElementById('dynamic-gallery-grid');
  if(!grid) return;

  async function loadGallery(category) {
    grid.innerHTML = '<div style="color: var(--gold); text-align: center; width: 100%; grid-column: 1 / -1; padding: 40px;">INITIALIZING SIGNAL...</div>';
    
    chips.forEach(c => c.classList.toggle('active', c.dataset.gf === category));

    const folderIds = window.GALLERY_FOLDERS[category];
    if (!folderIds || (Array.isArray(folderIds) ? folderIds.length === 0 : folderIds === '')) {
      grid.innerHTML = '<div style="color: var(--dimmer); text-align: center; width: 100%; grid-column: 1 / -1; padding: 40px;" class="visible">Nothing is uploaded yet. Awaiting committee sync...</div>';
      return;
    }

    const idsToFetch = Array.isArray(folderIds) ? folderIds : [folderIds];
    let allImages = [];

    try {
      for (const fId of idsToFetch) {
        const res = await fetch('/api/gallery?folderId=' + fId);
          if (res.ok) {
            const data = await res.json();
            allImages = allImages.concat(data);
          } else {
            const errText = await res.text();
            grid.innerHTML = `<div style="color: red; text-align: center; width: 100%; grid-column: 1 / -1; padding: 40px;" class="visible">API ERROR (${res.status}): ${errText}</div>`;
            return;
          }
      }

      if (allImages.length === 0) {
        grid.innerHTML = '<div style="color: var(--dimmer); text-align: center; width: 100%; grid-column: 1 / -1; padding: 40px;" class="visible">Folder is currently empty or API keys missing.</div>';
        return;
      }

      let html = '';
      allImages.forEach((img, i) => {
        let spanClass = '';
        if (i % 7 === 0) spanClass = 'col2 row2';
        else if (i % 5 === 0) spanClass = 'row2';
        else if (i % 11 === 0) spanClass = 'col2';

        html += `<div data-reveal class="gitem visible ${spanClass}">
                   <img src="${img.url}" alt="${img.name}" loading="lazy">
                   <div class="gitem-label">${img.name}</div>
                 </div>`;
      });
      grid.innerHTML = html;
      attachLightbox();

    } catch (err) {
      grid.innerHTML = '<div style="color: red; text-align: center; width: 100%; grid-column: 1 / -1; padding: 40px;" class="visible">SYSTEM ERROR: Unable to establish connection to Drive API.</div>';
    }
  }

  chips.forEach(chip => {
    chip.addEventListener('click', () => loadGallery(chip.dataset.gf));
  });

  loadGallery('all');
})();

function attachLightbox() {
  const lb = document.getElementById('lightbox');
  const lbImg = document.getElementById('lb-img');
  const lbCap = document.getElementById('lb-caption');
  
  document.querySelectorAll('.gitem').forEach(item => {
    const newItem = item.cloneNode(true);
    item.parentNode.replaceChild(newItem, item);
    
    newItem.addEventListener('click', () => {
      const img = newItem.querySelector('img');
      const cap = newItem.querySelector('.gitem-label');
      if (!img) return;
      
      const container = newItem.closest('#gallery-memories') ? '#gallery-memories' : '#gallery-current';
      let lbImages = Array.from(document.querySelectorAll(`${container} .gitem img`));
      
      let lbIdx = lbImages.indexOf(img);
      if(lbIdx === -1) lbIdx = 0;
      
      lbImg.src = img.src;
      if (cap) lbCap.textContent = cap.textContent;
      lb.setAttribute('aria-hidden', 'false');
    });
  });
}
attachLightbox();
