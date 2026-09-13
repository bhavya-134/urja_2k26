import codecs

js_code = """
// ==========================================
// URJA 2K26 - DYNAMIC GALLERY CONFIGURATION
// ==========================================
window.GALLERY_FOLDERS = {
  'all': [],
  'faces-of-urja': '',
  'decoration': '',
  'aavishkar': '',
  'f1-arena': '',
  'sync': '',
  'robo-soccer': ''
};

(function initGallery() {
  // --- SUB-TAB TOGGLE LOGIC ---
  const btnMemories = document.getElementById('gal-btn-memories');
  const btnCurrent = document.getElementById('gal-btn-current');
  const viewMemories = document.getElementById('gallery-memories');
  const viewCurrent = document.getElementById('gallery-current');

  if(btnMemories && btnCurrent) {
    btnMemories.addEventListener('click', () => {
      btnMemories.classList.add('active');
      btnCurrent.classList.remove('active');
      viewMemories.style.display = 'block';
      viewCurrent.style.display = 'none';
    });
    
    btnCurrent.addEventListener('click', () => {
      btnCurrent.classList.add('active');
      btnMemories.classList.remove('active');
      viewCurrent.style.display = 'block';
      viewMemories.style.display = 'none';
    });
    
    viewMemories.style.display = 'block';
    viewCurrent.style.display = 'none';
  }

  // --- DYNAMIC GRID LOGIC ---
  const chips = document.querySelectorAll('.gchip');
  const grid = document.getElementById('dynamic-gallery-grid');
  if(!grid) return;

  async function loadGallery(category) {
    grid.innerHTML = '<div style="color: var(--gold); text-align: center; width: 100%; grid-column: 1 / -1; padding: 40px;">INITIALIZING SIGNAL...</div>';
    
    chips.forEach(c => c.classList.toggle('active', c.dataset.gf === category));

    const folderIds = window.GALLERY_FOLDERS[category];
    if (!folderIds || (Array.isArray(folderIds) ? folderIds.length === 0 : folderIds === '')) {
      grid.innerHTML = '<div style="color: var(--dimmer); text-align: center; width: 100%; grid-column: 1 / -1; padding: 40px;">Nothing is uploaded yet. Awaiting committee sync...</div>';
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
        }
      }

      if (allImages.length === 0) {
        grid.innerHTML = '<div style="color: var(--dimmer); text-align: center; width: 100%; grid-column: 1 / -1; padding: 40px;">Folder is currently empty or API keys missing.</div>';
        return;
      }

      let html = '';
      allImages.forEach((img, i) => {
        let spanClass = '';
        if (i % 7 === 0) spanClass = 'col2 row2';
        else if (i % 5 === 0) spanClass = 'row2';
        else if (i % 11 === 0) spanClass = 'col2';

        html += `<div data-reveal class="gitem ${spanClass}">
                   <img src="${img.url}" alt="${img.name}" loading="lazy">
                   <div class="gitem-label">${img.name}</div>
                 </div>`;
      });
      grid.innerHTML = html;
      attachLightbox();

    } catch (err) {
      grid.innerHTML = '<div style="color: red; text-align: center; width: 100%; grid-column: 1 / -1; padding: 40px;">SYSTEM ERROR: Unable to establish connection to Drive API.</div>';
    }
  }

  chips.forEach(chip => {
    chip.addEventListener('click', () => loadGallery(chip.dataset.gf));
  });

  loadGallery('all');
})();

// --- LIGHTBOX LOGIC ---
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
"""

with open('gallery-app.js', 'w', encoding='utf-8') as f:
    f.write(js_code)
print("Corrected gallery-app.js syntax securely!")
