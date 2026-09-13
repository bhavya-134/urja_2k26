import re

js_path = 'gallery-app-v2.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Fix the early return bug blocking the ALL tab
pattern = r"const folderIds = window\.GALLERY_FOLDERS\[category\];\s*if \(\!folderIds \|\| \(Array\.isArray\(folderIds\) \? folderIds\.length === 0 : folderIds === ''\)\) \{\s*grid\.innerHTML = '<div style=\"color: var\(--dimmer\); text-align: center; width: 100%; grid-column: 1 / -1; padding: 40px;\" class=\"visible\">Nothing is uploaded yet\. Awaiting committee sync\.\.\.</div>';\s*return;\s*\}\s*// Auto-populate 'all' tab if it's the all category\s*let idsToFetch = Array\.isArray\(folderIds\) \? folderIds : \[folderIds\];\s*if \(category === 'all' && idsToFetch\.length === 0\) \{\s*idsToFetch = \[\];\s*for \(const \[k, v\] of Object\.entries\(window\.GALLERY_FOLDERS\)\) \{\s*if \(k !== 'all' && v\) idsToFetch\.push\(v\);\s*\}\s*\}"

replacement = """const folderIds = window.GALLERY_FOLDERS[category];
      let idsToFetch = Array.isArray(folderIds) ? folderIds : [folderIds];
      
      // Auto-populate 'all' tab BEFORE checking if it's empty
      if (category === 'all' && idsToFetch.length === 0) {
        idsToFetch = [];
        for (const [k, v] of Object.entries(window.GALLERY_FOLDERS)) {
          if (k !== 'all' && v) idsToFetch.push(v);
        }
      }

      if (idsToFetch.length === 0 || (idsToFetch.length === 1 && idsToFetch[0] === '')) {
        grid.innerHTML = '<div style="color: var(--dimmer); text-align: center; width: 100%; grid-column: 1 / -1; padding: 40px;" class="visible">Nothing is uploaded yet. Awaiting committee sync...</div>';
        return;
      }"""

js = re.sub(pattern, replacement, js)

with open(js_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(js)
print("Fixed ALL tab early return bug!")
