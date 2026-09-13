import re

js_path = 'gallery-app.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace("document.addEventListener('DOMContentLoaded', attachLightbox);", "attachLightbox();")

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("Removed second DOMContentLoaded!")
