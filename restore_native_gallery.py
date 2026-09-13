import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_gallery_pattern = r'<div class="tab-panel" id="tab-gallery" hidden>.*?<!-- ==================== TAB: TEAMS ==================== -->'

new_gallery = '''<div class="tab-panel" id="tab-gallery" hidden>
    <section class="page-section">
      <div class="page-header" data-reveal>
        <div class="page-label">SIGNAL ARCHIVED</div>
        <h2 class="page-title">GALLERY</h2>
        <p class="page-sub">A glimpse into the energy of URJA.</p>
      </div>
      
      <div class="gallery-grid" id="gallery-grid">
        <div data-reveal class="gitem col2 row2"><img src="./GALLERY/1.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+1'"><div class="gitem-label">URJA Memory</div></div>
        <div data-reveal class="gitem"><img src="./GALLERY/2.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+2'"><div class="gitem-label">URJA Memory</div></div>
        <div data-reveal class="gitem"><img src="./GALLERY/3.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+3'"><div class="gitem-label">URJA Memory</div></div>
        <div data-reveal class="gitem row2"><img src="./GALLERY/4.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+4'"><div class="gitem-label">URJA Memory</div></div>
        <div data-reveal class="gitem"><img src="./GALLERY/5.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+5'"><div class="gitem-label">URJA Memory</div></div>
        <div data-reveal class="gitem"><img src="./GALLERY/6.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+6'"><div class="gitem-label">URJA Memory</div></div>
        <div data-reveal class="gitem col2"><img src="./GALLERY/7.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+7'"><div class="gitem-label">URJA Memory</div></div>
        <div data-reveal class="gitem"><img src="./GALLERY/8.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+8'"><div class="gitem-label">URJA Memory</div></div>
      </div>

      <div style="text-align: center; margin-top: 50px;" data-reveal>
        <a href="https://drive.google.com/drive/folders/11KRFPRVckNxKhe-JcLN5s2fn3MyDPQ0E" target="_blank" rel="noopener" class="btn-ghost" style="display: inline-flex; align-items: center; justify-content: center; width: 100%; max-width: 300px; margin: 0 auto;">VIEW ALL ON GOOGLE DRIVE &rarr;</a>
      </div>
      
    </section>
  </div>
  
  <!-- ==================== TAB: TEAMS ==================== -->'''

html = re.sub(old_gallery_pattern, new_gallery, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Restored native gallery grid!")
