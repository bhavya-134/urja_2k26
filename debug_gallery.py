import re

js_path = 'gallery-app-v2.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Enhance the error handling to print the EXACT API response to the screen for debugging
pattern = r"const res = await fetch\('/api/gallery\?folderId=' \+ fId\);\s*if \(res\.ok\) \{\s*const data = await res\.json\(\);\s*allImages = allImages\.concat\(data\);\s*\}"
replacement = """const res = await fetch('/api/gallery?folderId=' + fId);
          if (res.ok) {
            const data = await res.json();
            allImages = allImages.concat(data);
          } else {
            const errText = await res.text();
            grid.innerHTML = `<div style="color: red; text-align: center; width: 100%; grid-column: 1 / -1; padding: 40px;" class="visible">API ERROR (${res.status}): ${errText}</div>`;
            return;
          }"""

js = re.sub(pattern, replacement, js)

with open(js_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(js)
print("Updated Gallery JS error handling!")
