import re

js_path = 'gallery-app.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace document.addEventListener('DOMContentLoaded', () => { ... });
# with an IIFE or just bare code since defer guarantees DOM is loaded.
js = js.replace("document.addEventListener('DOMContentLoaded', () => {", "(function initGallery() {")
# We need to find the closing '});' for DOMContentLoaded.
# Since it's at the end of the loadGallery function definition and chip binding, let's just replace the exact text.
js = js.replace("  loadGallery('all');\n});", "  loadGallery('all');\n})();")

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("Removed DOMContentLoaded from gallery-app.js!")
