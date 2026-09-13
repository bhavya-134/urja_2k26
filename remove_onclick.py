import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove onclick from html just in case
html = html.replace('onclick="switchGalleryTab(\'memories\')"', '')
html = html.replace('onclick="switchGalleryTab(\'current\')"', '')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
