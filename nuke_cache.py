import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Inject a cache-busting script right after the body tag
nuke_script = """
<script>
  // ONE-TIME CACHE NUKE TO FORCE MOBILE PHONES TO UPDATE
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.getRegistrations().then(function(registrations) {
      let shouldReload = false;
      for(let registration of registrations) {
        registration.unregister();
        shouldReload = true;
      }
      if (shouldReload && !window.location.search.includes('cleared=1')) {
        window.location.replace(window.location.pathname + '?cleared=1');
      }
    });
  }
</script>
"""

if "ONE-TIME CACHE NUKE" not in html:
    html = html.replace('<body>', '<body>\n' + nuke_script)
    with open(html_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(html)
    print("Injected cache-nuke script into index.html!")
else:
    print("Already injected.")
