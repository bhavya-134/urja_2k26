import re

js_path = 'gallery-app.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace GALLERY_FOLDERS object
pattern = r"window\.GALLERY_FOLDERS = \{[\s\S]*?\};"
replacement = """window.GALLERY_FOLDERS = {
  'all': [],
  'faces-of-urja': '',
  'decoration': '',
  'aavishkar': '',
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
print("Updated Gallery JS folders!")
