import re
import os

# Rename the JS file
if os.path.exists('gallery-app.js'):
    os.rename('gallery-app.js', 'gallery-app-v2.js')

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update script tag
html = html.replace('src="gallery-app.js"', 'src="gallery-app-v2.js"')

# Also let's completely strip the hidden attribute from index.html just to be safe
html = html.replace('<div id="gallery-current" hidden>', '<div id="gallery-current" style="display: none;">')
html = html.replace('<div id="gallery-memories" hidden>', '<div id="gallery-memories" style="display: none;">')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Renamed JS file and updated HTML to permanently bypass cache!")
