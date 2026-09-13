import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Generate Tier 2 names
t2_names = "".join([f'<div class="t-item"><div class="t-dot"></div><span>[Name]</span></div>' for _ in range(6)])

# Generate Tier 5 names
t5_names = "".join([f'<div class="t-item"><div class="t-dot"></div><span>[Name]</span></div>' for _ in range(23)])

teams_html = f'''<!-- ==================== TAB: TEAMS ==================== -->
  <div class="tab-panel" id="tab-teams" hidden>
    <section class="page-section">
      <div class="page-header" data-reveal>
        <div class="page-label">NETWORK TOPOLOGY</div>
        <h2 class="page-title">THE AXONS</h2>
      </div>

      <div class="teams-container">
        
        <!-- TIER 0: HOD -->
        <div class="team-tier tier-0" data-reveal>
          <div class="t-node-label">SIGNAL SOURCE</div>
          <div class="t-gold-dot lg"></div>
          <div class="t-name t-name-xl">Dr. [Name]</div>
          <div class="t-role">Head of Department<br>Department of Electrical Engineering</div>
          <div class="t-grad-line"></div>
        </div>

        <!-- TIER 1: Fest Coordinators -->
        <div class="team-tier tier-1" data-reveal>
          <div class="t-node-label">SIGNAL RELAY (UNDER THE GUIDANCE OF)</div>
          <div class="t1-grid">
            <div class="t1-card">
              <div class="t-name t-name-lg">Prof. [Name]</div>
              <div class="t-role">FEST COORDINATOR</div>
            </div>
            <div class="t1-card">
              <div class="t-name t-name-lg">Prof. [Name]</div>
              <div class="t-role">FEST COORDINATOR</div>
            </div>
          </div>
        </div>

        <!-- TIER 2: Event Coordinators -->
        <div class="team-tier tier-2" data-reveal>
          <div class="t-node-label">BRANCH CONTROLLERS (EVENT COORDINATORS)</div>
          <div class="t2-grid">
            {t2_names}
          </div>
        </div>

        <!-- TIER 3: Student Convenors -->
        <div class="team-tier tier-3" data-reveal>
           <div class="t-node-label">STUDENT CONVENORS</div>
           <div class="t3-list">
              <div class="t3-row"><span>[Name]</span><span class="t-role">Convenor</span></div>
              <div class="t3-row"><span>[Name]</span><span class="t-role">Co-Convenor</span></div>
              <div class="t3-row"><span>[Name]</span><span class="t-role">Co-Convenor</span></div>
           </div>
        </div>

        <!-- TIER 4: Committee Heads -->
        <div class="team-tier tier-4" data-reveal>
           <div class="t-node-label">FUNCTION NODES (COMMITTEE HEADS)</div>
           <div class="t4-cards">
              
              <div class="t4-card">
                 <div class="t4-header" style="color:var(--amber-l);"><span class="t-dot" style="background:var(--amber-l);"></span> DECORATION</div>
                 <div class="pulse-divider"><div class="pulse-dot"></div></div>
                 <div class="t4-members">
                    <div class="t4-row"><span>[Name]</span><span class="t-role">Head</span></div>
                    <div class="t4-row"><span>[Name]</span><span class="t-role">Head</span></div>
                    <div class="t4-row"><span>[Name]</span><span class="t-role">Head</span></div>
                 </div>
              </div>
              
              <div class="t4-card">
                 <div class="t4-header" style="color:var(--blue-l);"><span class="t-dot" style="background:var(--blue-l);"></span> INTERACTIVE RELATIONS (IR)</div>
                 <div class="pulse-divider"><div class="pulse-dot" style="background:var(--blue-l); box-shadow: 0 0 8px var(--blue-l);"></div></div>
                 <div class="t4-members">
                    <div class="t4-row"><span>[Name]</span><span class="t-role">Head</span></div>
                    <div class="t4-row"><span>[Name]</span><span class="t-role">Head</span></div>
                    <div class="t4-row"><span>[Name]</span><span class="t-role">Head</span></div>
                 </div>
              </div>

              <div class="t4-card">
                 <div class="t4-header"><span class="t-dot"></span> PHOTOGRAPHY</div>
                 <div class="pulse-divider"><div class="pulse-dot"></div></div>
                 <div class="t4-members">
                    <div class="t4-row"><span>[Name]</span><span class="t-role">Head</span></div>
                    <div class="t4-row"><span>[Name]</span><span class="t-role">Head</span></div>
                 </div>
              </div>

              <div class="t4-card">
                 <div class="t4-header"><span class="t-dot"></span> PUBLIC RELATIONS (PR)</div>
                 <div class="pulse-divider"><div class="pulse-dot"></div></div>
                 <div class="t4-members">
                    <div class="t4-row"><span>[Name]</span><span class="t-role">Head</span></div>
                    <div class="t4-row"><span>[Name]</span><span class="t-role">Head</span></div>
                 </div>
              </div>

           </div>
        </div>

        <!-- TIER 5: Event Heads -->
        <div class="team-tier tier-5" data-reveal>
           <div class="t-node-label">EVENT NODES (EVENT HEADS)</div>
           <div class="t5-grid">
              {t5_names}
           </div>
        </div>

        <!-- TIER 6: Volunteers -->
        <div class="team-tier tier-6" data-reveal id="volunteer-section">
           <div class="t-node-label"><span class="t-dot"></span> TERMINAL NODES (VOLUNTEERS) — 57 NODES</div>
           <div class="pulse-divider"><div class="pulse-dot"></div></div>
           
           <div class="t6-grid" id="vol-grid">
              <!-- JS Injects 57 Volunteers Here -->
           </div>
           
           <button class="btn-ghost" id="vol-show-all" style="font-size: 11px; padding: 6px 12px; margin-top: 10px;">SHOW ALL</button>
           
           <div class="terminal-line" id="term-line">
              ✓ NETWORK CONNECTED — 102 NODES ONLINE
           </div>
        </div>

      </div>
    </section>
  </div>
  
  <!-- ==================== TAB: SPONSORS ==================== -->'''

pattern = r'<!-- ==================== TAB: TEAMS ==================== -->.*?<!-- ==================== TAB: SPONSORS ==================== -->'
html = re.sub(pattern, teams_html, html, flags=re.DOTALL)

# Inject teams-app.js
if '<script src="teams-app.js" defer></script>' not in html:
    html = html.replace('</body>', '  <script src="teams-app.js" defer></script>\n</body>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html with new Teams structure!")
