import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Inject into modal body using regex to ignore spaces
content = re.sub(
    r'(<div class="modal-icon \$\{cat\}" id="mi-target">\$\{iconSvg\}</div>)',
    r'<button class="modal-close-btn" id="modal-close-btn" aria-label="Close modal">&times;</button>\n          \1',
    content
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("Injected close button HTML!")
