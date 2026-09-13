import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's remove data-reveal from gallery-memories and gallery-current wrappers
# Specifically the <p data-reveal> and <div class="gallery-chips" data-reveal> and <div ... data-reveal> inside gallery
# Actually, the easiest is to just add a tiny snippet of JS to gallery-app.js that forces .visible on tab switch.

js_path = 'gallery-app.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

replacement = """
    btnMemories.addEventListener('click', () => {
      btnMemories.classList.add('active');
      btnCurrent.classList.remove('active');
      viewMemories.style.display = 'block';
      viewCurrent.style.display = 'none';
      // Force reveal
      viewMemories.querySelectorAll('[data-reveal]').forEach(el => el.classList.add('visible'));
    });
    
    btnCurrent.addEventListener('click', () => {
      btnCurrent.classList.add('active');
      btnMemories.classList.remove('active');
      viewCurrent.style.display = 'block';
      viewMemories.style.display = 'none';
      // Force reveal
      viewCurrent.querySelectorAll('[data-reveal]').forEach(el => el.classList.add('visible'));
    });
    
    viewMemories.style.display = 'block';
    viewCurrent.style.display = 'none';
    // Force reveal on initial load
    setTimeout(() => {
      viewMemories.querySelectorAll('[data-reveal]').forEach(el => el.classList.add('visible'));
    }, 100);
"""

# We need to replace the exact block in gallery-app.js
# Let's write it carefully.
pattern = re.compile(r"btnMemories\.addEventListener\('click', \(\) => \{.*?viewCurrent\.style\.display = 'none';\n\s*\}", re.DOTALL)

js = re.sub(r"btnMemories\.addEventListener\('click', \(\) => \{[\s\S]*?viewCurrent\.style\.display = 'none';\n\s*\}", replacement.strip(), js)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated gallery-app.js to force visibility!")
