import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_header = '''<!-- GLOBAL HEADER -->
<header id="global-header" style="position: fixed; top: 0; left: 0; right: 0; height: 65px; display: flex; align-items: center; padding: 0 20px; background: rgba(5,5,8,0.9); border-bottom: 1px solid rgba(242,179,61,0.3); z-index: 99999; backdrop-filter: blur(15px);">
  <div style="display: flex; align-items: center; cursor: pointer; flex-grow: 1;" onclick="window.URJA.switchTab('home')">
    <div class="gh-logo" style="width: 40px; height: 40px; border-radius: 50%; overflow: hidden; margin-right: 12px; border: 1px solid var(--gold);">
      <img src="./LOGO.jpeg" alt="Logo" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.style.display='none';">
    </div>
    <div class="gh-name" style="font-family: 'Orbitron', sans-serif; font-size: 22px; font-weight: 700; color: #F2B33D; letter-spacing: 1px;">URJA <span style="color: #FF8A00;">2K26</span></div>
  </div>
  
  <div class="gh-menu-btn" onclick="document.getElementById('gh-menu').style.display = document.getElementById('gh-menu').style.display === 'flex' ? 'none' : 'flex'" style="cursor: pointer; color: #F2B33D; padding: 10px; z-index: 100000;">
    <svg viewBox="0 0 24 24" width="28" height="28" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
  </div>
</header>

<div id="gh-menu" style="display: none; position: fixed; top: 65px; left: 0; right: 0; background: rgba(5,5,8,0.95); backdrop-filter: blur(15px); border-bottom: 1px solid rgba(242,179,61,0.3); z-index: 99998; padding: 20px 0; flex-direction: column; align-items: stretch;">
  <button class="gh-menu-link" onclick="window.URJA.switchTab('home'); this.parentElement.style.display='none'">HOME</button>
  <button class="gh-menu-link" onclick="window.URJA.switchTab('events'); this.parentElement.style.display='none'">EVENTS</button>
  <button class="gh-menu-link" onclick="window.URJA.switchTab('schedule'); this.parentElement.style.display='none'">SCHEDULE</button>
  <button class="gh-menu-link" onclick="window.URJA.switchTab('gallery'); this.parentElement.style.display='none'">GALLERY</button>
  <button class="gh-menu-link" onclick="window.URJA.switchTab('teams'); this.parentElement.style.display='none'">TEAMS</button>
  <button class="gh-menu-link" onclick="window.URJA.switchTab('sponsors'); this.parentElement.style.display='none'">SPONSORS</button>
</div>
'''

html = re.sub(r'<header id="global-header".*?</header>', new_header, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated header and added dropdown menu!")
