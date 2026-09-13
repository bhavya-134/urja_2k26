import re

js_path = 'gallery-app-v2.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Completely obliterate the spanClass logic
pattern = r"let spanClass = '';[\s\S]*?html \+= `<div data-reveal class=\"gitem visible \$\{spanClass\}\">"
replacement = "html += `<div data-reveal class=\"gitem visible\" style=\"aspect-ratio: 1/1;\">"

js = re.sub(pattern, replacement, js)

# Also check for any other variations of html += `<div class="gitem...
pattern2 = r"let spanClass = '';[\s\S]*?html \+= `<div class=\"gitem \$\{spanClass\}\" data-reveal>"
replacement2 = "html += `<div class=\"gitem\" data-reveal style=\"aspect-ratio: 1/1;\">"
js = re.sub(pattern2, replacement2, js)

with open(js_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(js)
print("Forced uniform grid layout!")
