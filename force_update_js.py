import re

js_path = 'gallery-app.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the entire window.GALLERY_FOLDERS block, but keep the user's aavishkar ID
pattern = r"window\.GALLERY_FOLDERS = \{[\s\S]*?\};"
replacement = """window.GALLERY_FOLDERS = {
  'all': [],
  'faces-of-urja': '',
  'decoration': '',
  'aavishkar': '1-IiZ2RgbBHEOtA5xr4q96-vGkVj1IYpj',
  'f1-arena': '',
  'sync': '',
  'power-up': '',
  'abhivyakti': '',
  'human-ludo': '',
  'game-of-drones': '',
  'quiz-whiz': '',
  'escape': '',
  'clash-of-minds': '',
  'robo-soccer': ''
};"""

js = re.sub(pattern, replacement, js)

with open(js_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(js)
print("Updated Gallery JS folders while preserving Aavishkar ID!")
