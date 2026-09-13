import re

js_path = 'app.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the orphaned }); before // Lightbox
# Pattern: \s*}\);\s*// Lightbox
# Let's use a very safe replacement
pattern = r'\}\);\s*// Lightbox'
js = re.sub(pattern, '// Lightbox', js)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("Removed orphaned bracket!")
