import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if close button is already there
if '<button class="modal-close-btn" id="modal-close-btn"' in content:
    print("Already has close button!")
else:
    # Inject into modal body
    broken_html = '<div class="modal-icon " id="mi-target"></div>'
    fixed_html = '<button class="modal-close-btn" id="modal-close-btn" aria-label="Close modal">&times;</button>\n          <div class="modal-icon " id="mi-target"></div>'
    content = content.replace(broken_html, fixed_html)
    
    # Inject event listener
    broken_js = "const regBtn = document.getElementById('modal-reg-btn');"
    fixed_js = "const closeXBtn = document.getElementById('modal-close-btn');\n        if(closeXBtn) closeXBtn.addEventListener('click', closeModal);\n\n        const regBtn = document.getElementById('modal-reg-btn');"
    content = content.replace(broken_js, fixed_js)
    
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injected close button!")
