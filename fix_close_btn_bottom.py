import re

app_path = 'app.js'
with open(app_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Add a close button at the bottom of the modal as well
pattern = r"<button class=\"modal-reg reg-charge\" id=\"modal-reg-btn\">REGISTER NOW &rarr;</button>"
replacement = """<button class="modal-reg reg-charge" id="modal-reg-btn">REGISTER NOW &rarr;</button>
            <button class="modal-close-bottom" id="modal-close-bottom-btn" style="width: 100%; padding: 16px; border-radius: 40px; background: transparent; border: 1px solid var(--dim); color: var(--dim); font-family: var(--font-head); font-weight: 700; font-size: 15px; cursor: pointer; margin-top: -8px;">CLOSE DETAILS</button>"""

js = re.sub(pattern, replacement, js)

# Bind the new bottom button to close function
bind_pattern = r"const closeXBtn = document.getElementById\('modal-close-btn'\);\s*if\(closeXBtn\) closeXBtn.addEventListener\('click', closeModal\);"
bind_replacement = """const closeXBtn = document.getElementById('modal-close-btn');
          if(closeXBtn) closeXBtn.addEventListener('click', closeModal);
          const closeBottomBtn = document.getElementById('modal-close-bottom-btn');
          if(closeBottomBtn) closeBottomBtn.addEventListener('click', closeModal);"""

js = re.sub(bind_pattern, bind_replacement, js)

with open(app_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(js)
print("Injected bottom close button!")
