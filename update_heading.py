import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the heading
html = html.replace('<h2 class="page-title">THE AXONS</h2>', '<h2 class="page-title">THE TEAM</h2>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated heading to THE TEAM!")
