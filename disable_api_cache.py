import re

api_path = 'api/gallery.js'
with open(api_path, 'r', encoding='utf-8') as f:
    api = f.read()

# Add Cache-Control headers to disable caching
pattern = r"res\.status\(200\)\.json\(images\);"
replacement = "res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate');\n    res.status(200).json(images);"

api = re.sub(pattern, replacement, api)

with open(api_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(api)
print("Updated API to disable caching!")
