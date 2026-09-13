import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all lowercase /logos/ with uppercase /LOGOS/
html = html.replace('src="./logos/', 'src="./LOGOS/')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated HTML paths to strictly match case for Linux!")
