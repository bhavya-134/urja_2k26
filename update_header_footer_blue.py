import re

css_path = 'styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Header
css = css.replace('color: var(--gold); letter-spacing: 1px;', 'color: var(--blue-l); letter-spacing: 1px;') # for gh-name
css = css.replace('border: 1px dashed rgba(242, 179, 61, 0.5);', 'border: 1px dashed rgba(58, 160, 255, 0.5);') # for gh-logo

# Footer brand
css = css.replace('color:var(--gold);letter-spacing:-1px;}', 'color:var(--blue-l);letter-spacing:-1px;}')
css = css.replace('.footer-brand span{color:var(--amber-l);}', '.footer-brand span{color:#00f0ff;}')

# Footer IG
css = css.replace('border:1px solid var(--gold);border-radius:28px;padding:10px 22px;color:var(--gold);', 'border:1px solid var(--blue-l);border-radius:28px;padding:10px 22px;color:var(--blue-l);')
css = css.replace('.footer-ig:hover{background:rgba(242,179,61,.08);}', '.footer-ig:hover{background:rgba(58,160,255,.1);}')
css = css.replace('@keyframes ig-pulse{0%,100%{box-shadow:0 0 0 0 rgba(242,179,61,.3);}50%{box-shadow:0 0 0 8px rgba(242,179,61,0);}}', '@keyframes ig-pulse{0%,100%{box-shadow:0 0 0 0 rgba(58,160,255,.4);}50%{box-shadow:0 0 0 8px rgba(58,160,255,0);}}')

# New Footer text classes
css = css.replace('.footer-terminal { font-family: var(--font-mono); font-size: 11px; color: var(--gold);', '.footer-terminal { font-family: var(--font-mono); font-size: 11px; color: var(--blue-l);')
css = css.replace('.footer-guidance-label { font-family: var(--font-mono); font-size: 11px; color: var(--amber-l);', '.footer-guidance-label { font-family: var(--font-mono); font-size: 11px; color: var(--blue-l);')
css = css.replace('.footer-hod strong { font-weight: 500; color: var(--gold);', '.footer-hod strong { font-weight: 500; color: var(--blue-l);')

# The SVG Pulse Line in the footer HTML!
# Let's fix that in index.html too.
html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as hf:
    html = hf.read()
html = html.replace('stroke="#F2B33D"', 'stroke="#3AA0FF"')
html = html.replace('<span style="color:var(--blue-l)">2K26</span>', '<span style="color:#00f0ff">2K26</span>') # Just to make it pop

with open(html_path, 'w', encoding='utf-8') as hf:
    hf.write(html)
    
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated header and footer to Blue!")
