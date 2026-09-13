import re

app_path = 'app.js'
with open(app_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Remove the swipe down to close logic for the modal
swipe_logic = """    let mTY = 0;
    if (modal) {
      modal.addEventListener('touchstart', e => { mTY = e.touches[0].clientY; }, { passive: true });
      modal.addEventListener('touchmove', e => { const dy = e.touches[0].clientY - mTY; if (dy > 0) modal.style.transform = `translateY(${dy}px)`; }, { passive: true });
      modal.addEventListener('touchend', e => { const dy = e.changedTouches[0].clientY - mTY; modal.style.transform = ''; if (dy > 100) closeModal(); }, { passive: true });
    }"""

js = js.replace(swipe_logic, "")

with open(app_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(js)
print("Removed swipe logic from app.js!")
