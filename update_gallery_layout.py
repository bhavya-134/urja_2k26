import re

js_path = 'gallery-app-v2.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Remove the masonry span logic to make all images the same size
pattern = r"let spanClass = '';\s*if \(i % 7 === 0\) spanClass = 'col2 row2';\s*else if \(i % 5 === 0\) spanClass = 'col2';\s*html \+= `<div class=\"gitem \$\{spanClass\}\" data-reveal>"
replacement = """html += `<div class="gitem" data-reveal style="aspect-ratio: 1/1;">"""

js = re.sub(pattern, replacement, js)

with open(js_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(js)
print("Updated gallery grid to be uniform squares!")
