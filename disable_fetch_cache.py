import re

js_path = 'gallery-app-v2.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Add cache: 'no-store' to the fetch call
pattern = r"const res = await fetch\('/api/gallery\?folderId=' \+ fId\);"
replacement = "const res = await fetch('/api/gallery?folderId=' + fId + '&t=' + Date.now(), { cache: 'no-store' });"

js = re.sub(pattern, replacement, js)

with open(js_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(js)
print("Updated frontend fetch to bypass browser cache!")
