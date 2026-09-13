import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace long title with short title
old_title = '<title>URJA 2K26 - Synapse: The Pulse Within</title>'
new_title = '<title>URJA 2K26</title>'

# Sometimes it might have been saved with an em-dash, so let's do a regex just in case
html = re.sub(r'<title>URJA 2K2[56].*?</title>', '<title>URJA 2K26</title>', html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated website title!")
