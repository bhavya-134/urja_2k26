import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove Faculty Tiers from Teams Page
# We want to remove everything from <!-- TIER 0: HOD --> up to (but not including) <!-- TIER 3: Student Convenors -->
pattern_remove_tiers = r'<!-- TIER 0: HOD -->.*?<!-- TIER 3: Student Convenors -->'
html = re.sub(pattern_remove_tiers, '<!-- TIER 3: Student Convenors -->', html, flags=re.DOTALL)

# 2. Update the Footer
old_footer_pattern = r'<footer id="footer">.*?</footer>'
new_footer = """<footer id="footer">
      <div class="footer-pulse" aria-hidden="true">
        <svg width="100%" height="30" viewBox="0 0 800 30" preserveAspectRatio="none">
          <path d="M0,15 Q100,15 140,15 L170,3 L185,27 L200,10 L215,22 L230,15 Q350,15 400,15 Q500,15 530,15 L570,3 L585,27 L600,10 L615,22 L630,15 Q750,15 800,15" fill="none" stroke="#F2B33D" stroke-width="1" stroke-dasharray="1600" stroke-dashoffset="1600">
            <animate attributeName="stroke-dashoffset" from="1600" to="-1600" dur="6s" repeatCount="indefinite"/>
          </path>
        </svg>
      </div>
      <div class="footer-inner">
        <div class="footer-terminal">● TRANSMISSION COMPLETE</div>
        
        <div class="footer-brand">URJA <span style="color:var(--blue-l)">2K26</span></div>
        <p class="footer-sub">One Spark, Endless Connections</p>
        <p class="footer-date">SEPTEMBER 18-19, 2026<br>Sarvajanik College of Engineering & Technology, Surat</p>
        
        <a href="https://www.instagram.com/urja2k26" target="_blank" rel="noopener" class="footer-ig" aria-label="Instagram" style="margin: 0 auto 16px;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
          @urja2k26
        </a>
        
        <div class="footer-divider"></div>
        
        <div class="footer-guidance-label">UNDER THE GUIDANCE OF</div>
        <div class="footer-hod">
          <strong>Dr. Hardik Desai, Head of Department</strong><br>
          <span style="color:var(--dimmer)">Dept. of Electrical Engineering</span>
        </div>
        
        <div class="footer-fac-section">
          <div class="footer-fac-title">Fest Coordinators:</div>
          <div class="footer-fac-list">
            <span>Prof. Sandhya Rathore</span>
            <span>Prof. Kriti Arora</span>
          </div>
        </div>

        <div class="footer-fac-section">
          <div class="footer-fac-title">Faculty Coordinators:</div>
          <div class="footer-fac-grid">
            <span>Prof. Aditi Hajari</span>
            <span>Prof. Jyoti Shah</span>
            <span>Prof. Naman Bhatt</span>
            <span>Prof. Nilesh Shah</span>
            <span>Prof. Shabbir Bohra</span>
            <span>Prof. Sharad Patel</span>
          </div>
        </div>

        <p class="footer-copy">&copy; 2026 URJA - All Rights Reserved &nbsp;|&nbsp; Made by Bhavya Tharakan</p>
      </div>
    </footer>"""

html = re.sub(old_footer_pattern, new_footer, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated HTML structure for Teams and Footer!")
