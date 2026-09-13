import re

css_path = 'styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Dock Navigation Active state
old_dock = ".dock-btn.active{color:var(--gold);}"
new_dock = ".dock-btn.active{color:#00f0ff; filter: drop-shadow(0 0 5px rgba(0,240,255,0.5));}"
css = css.replace(old_dock, new_dock)

old_dock_svg = ".dock-btn.active svg{stroke:var(--gold);fill:rgba(242,179,61,.1);}"
new_dock_svg = ".dock-btn.active svg{stroke:#00f0ff;fill:rgba(0,240,255,.15);}"
css = css.replace(old_dock_svg, new_dock_svg)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated dock nav to electric cyan!")
