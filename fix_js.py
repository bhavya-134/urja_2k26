import codecs

js_path = 'teams-app.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Fix the IntersectionObserver threshold and logic
# The issue was threshold: 0.2 on a very tall element, which might never trigger on smaller screens
old_obs = """const volObserver = new IntersectionObserver((entries) => {
          entries.forEach(e => {
            if(e.isIntersecting && window.getComputedStyle(e.target).display !== 'none') {
              bootNetwork();
              volObserver.unobserve(e.target);
            }
          });
        }, { threshold: 0.2 });"""

new_obs = """const volObserver = new IntersectionObserver((entries) => {
          entries.forEach(e => {
            if(e.isIntersecting) {
              bootNetwork();
              volObserver.unobserve(e.target);
            }
          });
        }, { threshold: 0.05, rootMargin: "0px 0px -50px 0px" });"""

js = js.replace(old_obs, new_obs)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated teams-app.js observer threshold!")
