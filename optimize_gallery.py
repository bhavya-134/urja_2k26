import re

js_path = 'gallery-app-v2.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Auto-populate the 'all' tab dynamically and optimize fetch with Promise.all
pattern = r"const idsToFetch = Array\.isArray\(folderIds\) \? folderIds : \[folderIds\];[\s\S]*?if \(allImages\.length === 0\) \{"
replacement = """// Auto-populate 'all' tab if it's the all category
      let idsToFetch = Array.isArray(folderIds) ? folderIds : [folderIds];
      if (category === 'all' && idsToFetch.length === 0) {
        idsToFetch = [];
        for (const [k, v] of Object.entries(window.GALLERY_FOLDERS)) {
          if (k !== 'all' && v) idsToFetch.push(v);
        }
      }
      
      let allImages = [];
  
      try {
        // Fetch all folders simultaneously for maximum speed
        const fetchPromises = idsToFetch.map(fId => 
          fetch('/api/gallery?folderId=' + fId).then(res => res.ok ? res.json() : [])
        );
        const results = await Promise.all(fetchPromises);
        results.forEach(data => allImages = allImages.concat(data));
  
        // Shuffle the 'all' array so different events are mixed beautifully
        if (category === 'all') {
          for (let i = allImages.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [allImages[i], allImages[j]] = [allImages[j], allImages[i]];
          }
        }
  
        if (allImages.length === 0) {"""

js = re.sub(pattern, replacement, js)

with open(js_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(js)
print("Optimized Gallery fetch and auto-populated ALL tab!")
