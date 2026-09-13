import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the entire gallery section
old_gallery_pattern = r'<div class="tab-panel" id="tab-gallery" hidden>.*?</div>\s*<!-- ==================== TAB: TEAMS ==================== -->'

new_gallery = '''<div class="tab-panel" id="tab-gallery" hidden>
    <section class="page-section">
      <div class="page-header" data-reveal>
        <div class="page-label">SIGNAL ARCHIVED</div>
        <h2 class="page-title">GALLERY</h2>
      </div>
      
      <div class="gallery-intro" data-reveal style="text-align: center; margin-bottom: 40px;">
        <p style="color: var(--dimmer); font-size: 14px; max-width: 600px; margin: 0 auto 20px;">Relive the incredible moments from our previous editions. Browse through the entire archive directly below.</p>
        <a href="https://drive.google.com/drive/folders/11KRFPRVckNxKhe-JcLN5s2fn3MyDPQ0E" target="_blank" rel="noopener" style="display: inline-flex; align-items: center; gap: 10px; background: rgba(242, 179, 61, 0.1); border: 1px solid var(--gold); color: var(--gold); padding: 12px 24px; border-radius: 30px; font-family: var(--font-mono); font-size: 12px; font-weight: 700; letter-spacing: 1px; transition: background 0.3s;">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
          OPEN IN GOOGLE DRIVE
        </a>
      </div>

      <div class="drive-embed-container" data-reveal style="position: relative; width: 100%; height: 65vh; min-height: 500px; border-radius: 16px; overflow: hidden; border: 1px solid rgba(242, 179, 61, 0.3); box-shadow: 0 10px 40px rgba(0,0,0,0.5); background: #111;">
        <!-- Embedded Google Drive Folder -->
        <iframe src="https://drive.google.com/embeddedfolderview?id=11KRFPRVckNxKhe-JcLN5s2fn3MyDPQ0E#grid" width="100%" height="100%" frameborder="0" style="position: absolute; top: 0; left: 0; border: none;"></iframe>
      </div>
      
    </section>
  </div>
  
  <!-- ==================== TAB: TEAMS ==================== -->'''

html = re.sub(old_gallery_pattern, new_gallery, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated gallery with drive embed!")
