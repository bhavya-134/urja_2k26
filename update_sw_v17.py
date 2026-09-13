import re

sw_path = 'sw.js'
with open(sw_path, 'r', encoding='utf-8') as f:
    sw = f.read()

# Update script array and bump cache to v17
sw = sw.replace("'/gallery.js',", "") # Wait, the array had '/gallery.js'?
sw = sw.replace("'/gallery-app.js',", "'/gallery-app-v2.js',")
sw = re.sub(r"const CACHE_NAME = 'urja-2k26-v\d+';", "const CACHE_NAME = 'urja-2k26-v17';", sw)

with open(sw_path, 'w', encoding='utf-8') as f:
    f.write(sw)
print("Updated SW to cache v2!")
