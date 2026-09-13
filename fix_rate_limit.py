import re

js_path = 'gallery-app-v2.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Revert Promise.all to sequential fetching to prevent API rate limiting
pattern = r"const fetchPromises = idsToFetch\.map\(fId =>[\s\S]*?results\.forEach\(data => allImages = allImages\.concat\(data\)\);"
replacement = """for (const fId of idsToFetch) {
          const res = await fetch('/api/gallery?folderId=' + fId);
          if (res.ok) {
            const data = await res.json();
            allImages = allImages.concat(data);
          }
        }"""

js = re.sub(pattern, replacement, js)

with open(js_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(js)
print("Reverted to sequential fetch!")
