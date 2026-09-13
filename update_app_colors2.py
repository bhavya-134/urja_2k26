import re

js_path = 'app.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace("`rgba(242,179,61,${alpha * 1.5})`", "`rgba(58,160,255,${alpha * 1.5})`")

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated mixed links in app.js safely!")
