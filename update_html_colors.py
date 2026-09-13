import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Make the second Fest Coordinator (Kriti Arora) blue
old_fc2 = '<div class="t1-card">\n              <div class="t-name t-name-lg">Prof. Kriti Arora</div>'
new_fc2 = '<div class="t1-card" style="border-top: 1px solid var(--blue-l); padding-top: 16px;">\n              <div class="t-name t-name-lg" style="color: var(--blue-l);">Prof. Kriti Arora</div>'
html = html.replace(old_fc2, new_fc2)

# Make the first Fest Coordinator (Sandhya Rathore) amber
old_fc1 = '<div class="t1-card">\n              <div class="t-name t-name-lg">Prof. Sandhya Rathore</div>'
new_fc1 = '<div class="t1-card" style="border-top: 1px solid var(--gold); padding-top: 16px;">\n              <div class="t-name t-name-lg" style="color: var(--gold);">Prof. Sandhya Rathore</div>'
html = html.replace(old_fc1, new_fc1)

# Alternating dots for Faculty Coordinators and Event Heads
# Since they are generated exactly as <div class="t-dot"></div>, we can use regex to replace every other instance in the tiers.

# A simple way: find all '<div class="t-dot"></div>' and replace alternatingly
parts = html.split('<div class="t-dot"></div>')
new_html = parts[0]
for i in range(1, len(parts)):
    if i % 2 == 0:
        new_html += '<div class="t-blue-dot"></div>' + parts[i]
    else:
        new_html += '<div class="t-dot"></div>' + parts[i]
html = new_html

# PR Committee should be blue
old_pr = '<div class="t4-header"><span class="t-dot"></span> PUBLIC RELATIONS (PR)</div>\n                 <div class="pulse-divider"><div class="pulse-dot"></div></div>'
new_pr = '<div class="t4-header" style="color:var(--blue-l);"><span class="t-blue-dot"></span> PUBLIC RELATIONS (PR)</div>\n                 <div class="pulse-divider"><div class="pulse-dot blue"></div></div>'
html = html.replace(old_pr, new_pr)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated alternating colors in index.html!")
