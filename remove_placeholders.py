import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the Silver and Partners tiers
# They are wrapped in <div class="stier" data-reveal>
silver_pattern = r'<div class="stier" data-reveal><div class="stier-label">SILVER SPONSORS</div>.*?</div></div></div>'
partners_pattern = r'<div class="stier" data-reveal><div class="stier-label">PARTNERS</div>.*?</div></div></div>'

html = re.sub(silver_pattern, '', html, flags=re.DOTALL)
html = re.sub(partners_pattern, '', html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed placeholder sponsors!")
