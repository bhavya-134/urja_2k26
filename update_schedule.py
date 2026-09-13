import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

def get_star():
    return '<button class="tl-star"><svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></button>'

def build_slot(start_t, end_t, cards_data, day_num):
    # cards_data is list of (title, venue, type, index)
    cards_html = ""
    for c in cards_data:
        title, venue, ctype, idx = c
        ev_id = f"ev-d{day_num}-{idx}"
        cards_html += f'''
                <div class="tl-card {ctype}" data-scat="{ctype}" data-id="{ev_id}">
                  {get_star()}
                  <div class="tl-title">{title}</div>
                  <div class="tl-details">
                    <div class="tl-venue"><span class="tl-icon">&#x1F4CD;</span> [{venue}]</div>
                  </div>
                </div>'''
    
    end_span = f'<span class="end-t">{end_t}</span>' if end_t else ''
    return f'''
            <div class="tl-slot">
              <div class="tl-time-label"><span class="start-t">{start_t}</span>{end_span}</div>
              <div class="tl-dot"></div>
              <div class="tl-cards">{cards_html}
              </div>
            </div>'''

# DAY 1 DATA
d1_slots = [
    ("09:00 AM", "09:30 AM", [("TEA AND BREAKFAST", "PSP LAB", "default", 1)], 1),
    ("09:30 AM", "10:30 AM", [("ABHIVYAKTI", "E-01", "technical", 2), ("AAVISHKAR", "E-02", "technical", 3)], 1),
    ("10:00 AM", "ONWARDS", [("POWER UP", "E-03", "non-technical", 4)], 1),
    ("10:30 AM", "12:00 PM", [("CLASH OF MINDS (ROUND-1)", "E-05", "technical", 5)], 1),
    ("11:00 AM", "ONWARDS", [("ESCAPE THE UNKNOWN", "E-106", "non-technical", 6), ("ROBO SOCCER (R-1)", "FRONT OF ELECTRICAL DEPT", "technical", 7), ("LAND OF LUDO", "E-103", "non-technical", 8)], 1),
    ("12:00 PM", "01:00 PM", [("THE QUIZ WHITZ BLITZ (R-1)", "E-01", "non-technical", 9)], 1),
    ("12:00 PM", "ONWARDS", [("GAME OF DRONES (R-1)", "SCET DOME", "technical", 10)], 1),
    ("01:00 PM", "01:30 PM", [("LUNCH BREAK", "CAMPUS", "default", 11)], 1),
    ("01:30 PM", "04:00 PM", [("SYNC - THE TECHRELAY (R-1)", "E-02", "technical", 12), ("F1 ARENA (R-1)", "E-01", "technical", 13)], 1)
]

# DAY 2 DATA
d2_slots = [
    ("09:00 AM", "09:30 AM", [("TEA AND BREAKFAST", "PSP LAB", "default", 1)], 2),
    ("09:30 AM", "10:30 AM", [("THE QUIZ WHITZ BLITZ (ROUND-2)", "E-01", "non-technical", 2), ("SYNC - THE TECHRELAY (ROUND-2)", "E-02", "technical", 3), ("ROBO SOCCER (ROUND-2)", "FRONT OF ELECTRICAL DEPT", "technical", 4)], 2),
    ("10:00 AM", "ONWARDS", [("POWER UP", "E-03", "non-technical", 5)], 2),
    ("10:30 AM", "12:00 PM", [("CLASH OF MINDS (ROUND-2)", "E-05", "technical", 6)], 2),
    ("11:00 AM", "ONWARDS", [("LAND OF LUDO", "E-103", "non-technical", 7), ("ESCAPE THE UNKNOWN", "E-106", "non-technical", 8)], 2),
    ("12:00 PM", "03:00 PM", [("F1 ARENA (ROUND-2&3)", "E-01", "technical", 9)], 2),
    ("01:00 PM", "01:30 PM", [("LUNCH BREAK", "CAMPUS", "default", 10)], 2),
    ("01:30 PM", "03:30 PM", [("ROBO SOCCER (R-3)", "FRONT OF ELECTRICAL DEPT", "technical", 11), ("GAME OF DRONES (ROUND-2)", "SCET DOME", "technical", 12)], 2),
    ("03:30 PM", "ONWARDS", [("OPEN MIC & PRIZE DISTRIBUTION", "E-103", "default", 13)], 2)
]

def render_day(slots, d_num):
    html = f'''          <!-- DAY {d_num} TIMELINE -->
          <div id="timeline-d{d_num}" class="timeline axon-track" {'hidden' if d_num == 2 else ''}>
            <div class="axon-line"></div>
            <div class="axon-glow-line" id="axon-glow-{d_num}"></div>\n'''
    for slot in slots:
        html += build_slot(slot[0], slot[1], slot[2], slot[3])
    html += '''\n          </div>\n'''
    return html

new_timeline_content = f'''<div id="timeline-container">
{render_day(d1_slots, 1)}
{render_day(d2_slots, 2)}
        </div>'''

# Replace in html
pattern = r'<div id="timeline-container">.*?</div>\s*</section>\s*</div>'
replacement = new_timeline_content + '\n      </section>\n    </div>'

html = re.sub(pattern, replacement, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated timeline schedule successfully!")
