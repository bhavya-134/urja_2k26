import re

sw_path = 'sw.js'
with open(sw_path, 'r', encoding='utf-8') as f:
    sw = f.read()

# Bump cache version to v4 to aggressively force user devices to dump the old cache
sw = re.sub(r"const CACHE_NAME = 'urja-2k26-v\d+';", "const CACHE_NAME = 'urja-2k26-v4';", sw)

with open(sw_path, 'w', encoding='utf-8') as f:
    f.write(sw)
print("Bumped Service Worker cache version!")
