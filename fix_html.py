import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix HOD Name
html = html.replace('Dr. [Name]', 'Dr. Hardik Desai')

# Remove data-reveal from volunteer section to avoid double-opacity conflicts
html = html.replace('<div class="team-tier tier-6" data-reveal id="volunteer-section">', '<div class="team-tier tier-6" id="volunteer-section">')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated HOD Name and removed data-reveal from vol section!")
