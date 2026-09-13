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
      </div>

      <!-- Gallery Sub-Tabs Toggle -->
      <div class="freq-dial-wrap" data-reveal style="margin-bottom: 30px;">
        <div class="brain-labels" style="max-width: 400px; margin: 0 auto;">
          <span class="bl-left active" id="gal-btn-memories" onclick="switchGalleryTab('memories')" style="cursor:pointer;">MEMORIES</span>
          <span class="bl-right" id="gal-btn-current" onclick="switchGalleryTab('current')" style="cursor:pointer;">URJA 2K26</span>
        </div>
      </div>

      <!-- ==================== MEMORIES (PAST EVENTS) ==================== -->
      <div id="gallery-memories">
        <p style="text-align: center; color: var(--dimmer); font-size: 14px; margin-bottom: 30px;" data-reveal>Glimpses from the previous edition of URJA.</p>
        
        <div class="gallery-grid">
          <div data-reveal class="gitem col2 row2"><img src="./GALLERY/1.jpg" alt="Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+1'"><div class="gitem-label">Memory</div></div>
          <div data-reveal class="gitem"><img src="./GALLERY/2.jpg" alt="Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+2'"><div class="gitem-label">Memory</div></div>
          <div data-reveal class="gitem"><img src="./GALLERY/3.jpg" alt="Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+3'"><div class="gitem-label">Memory</div></div>
          <div data-reveal class="gitem row2"><img src="./GALLERY/4.jpg" alt="Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+4'"><div class="gitem-label">Memory</div></div>
          <div data-reveal class="gitem"><img src="./GALLERY/5.jpg" alt="Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+5'"><div class="gitem-label">Memory</div></div>
          <div data-reveal class="gitem"><img src="./GALLERY/6.jpg" alt="Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+6'"><div class="gitem-label">Memory</div></div>
          <div data-reveal class="gitem col2 row2"><img src="./GALLERY/7.jpg" alt="Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+7'"><div class="gitem-label">Memory</div></div>
          <div data-reveal class="gitem"><img src="./GALLERY/8.jpg" alt="Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+8'"><div class="gitem-label">Memory</div></div>
          <div data-reveal class="gitem row2"><img src="./GALLERY/9.jpg" alt="Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+9'"><div class="gitem-label">Memory</div></div>
          <div data-reveal class="gitem"><img src="./GALLERY/10.jpg" alt="Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+10'"><div class="gitem-label">Memory</div></div>
          <div data-reveal class="gitem col2"><img src="./GALLERY/11.jpg" alt="Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+11'"><div class="gitem-label">Memory</div></div>
        </div>

        <div style="text-align: center; margin-top: 50px;" data-reveal>
          <a href="https://drive.google.com/drive/folders/11KRFPRVckNxKhe-JcLN5s2fn3MyDPQ0E" target="_blank" rel="noopener" class="btn-ghost" style="display: inline-flex; align-items: center; justify-content: center; width: 100%; max-width: 300px; margin: 0 auto;">VIEW ALL ARCHIVES &rarr;</a>
        </div>
      </div>

      <!-- ==================== URJA 2K26 (CURRENT EVENTS) ==================== -->
      <div id="gallery-current" hidden>
        <p style="text-align: center; color: var(--dimmer); font-size: 14px; margin-bottom: 30px;" data-reveal>Live uploads from the URJA 2K26 committees.</p>
        
        <!-- Filters -->
        <div class="gallery-chips" data-reveal style="display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; margin-bottom: 30px;">
          <button class="gchip active" data-gf="all">ALL</button>
          <button class="gchip" data-gf="faces-of-urja">FACES OF URJA</button>
          <button class="gchip" data-gf="decoration">DECORATION</button>
          <button class="gchip" data-gf="aavishkar">AAVISHKAR</button>
          <button class="gchip" data-gf="robo-soccer">ROBO SOCCER</button>
          <button class="gchip" data-gf="f1-arena">F1 ARENA</button>
          <button class="gchip" data-gf="sync">SYNC</button>
        </div>
        
        <!-- Dynamic Grid Container -->
        <div class="gallery-grid" id="dynamic-gallery-grid">
          <!-- Javascript will inject images here -->
        </div>
      </div>
      
    </section>
  </div>
  
  <!-- ==================== TAB: TEAMS ==================== -->'''

html = re.sub(old_gallery_pattern, new_gallery, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated HTML with split tabs!")
