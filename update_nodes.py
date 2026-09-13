import re

app_path = 'app.js'
with open(app_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Reduce NODE_COUNT from 60 to 35
js = js.replace('const NODE_COUNT = 60, LINK_DIST = 130;', 'const NODE_COUNT = 35, LINK_DIST = 130;')

# Make mixed connections alternate based on x position to balance it visually
old_col = """const col = a.type === b.type
            ? (a.type === 'amber' ? `rgba(255,138,0,${alpha})` : `rgba(58,160,255,${alpha})`)
            : `rgba(58,160,255,${alpha * 1.5})`;"""
            
new_col = """const col = a.type === b.type
            ? (a.type === 'amber' ? `rgba(255,138,0,${alpha})` : `rgba(58,160,255,${alpha})`)
            : ((a.x + b.x) % 2 > 1 ? `rgba(255,138,0,${alpha * 1.2})` : `rgba(58,160,255,${alpha * 1.2})`);"""

js = js.replace(old_col, new_col)

with open(app_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(js)
print("Updated app.js for fewer nodes and balanced colors!")
