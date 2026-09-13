import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Make CO-POWERED BY blue
old_cop = '<div class="stier-label">CO-POWERED BY</div>'
new_cop = '<div class="stier-label" style="color: var(--blue-l); border-bottom-color: rgba(58,160,255,0.2);">CO-POWERED BY</div>'
html = html.replace(old_cop, new_cop)

# Let's make one of the ghost buttons blue in the hero page.
# Find "VIEW SCHEDULE" button
old_btn = '<button class="btn-ghost" data-hero-btn="schedule">VIEW SCHEDULE</button>'
new_btn = '<button class="btn-ghost blue" data-hero-btn="schedule">VIEW SCHEDULE</button>'
html = html.replace(old_btn, new_btn)

# Make the secondary hero title text blue
old_hero = '<span class="ht-year">2K26</span>'
new_hero = '<span class="ht-year" style="color: var(--blue-l);">2K26</span>'
html = html.replace(old_hero, new_hero)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated Hero and Sponsors for dual color!")
