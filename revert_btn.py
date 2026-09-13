import re

css_path = 'styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Revert .btn-primary back to amber
old_btn = ".btn-primary{padding:13px 32px;border-radius:40px;background:linear-gradient(135deg,#00f0ff,var(--blue-l));color:#000;font-family:var(--font-head);font-weight:700;font-size:12px;letter-spacing:1px;cursor:pointer;border:none;transition:transform .2s,box-shadow .2s,filter .2s;min-height:44px; text-shadow: 0 0 2px rgba(255,255,255,0.5);}"
new_btn = ".btn-primary{padding:13px 32px;border-radius:40px;background:linear-gradient(135deg,var(--amber),var(--gold));color:#000;font-family:var(--font-head);font-weight:700;font-size:12px;letter-spacing:1px;cursor:pointer;border:none;transition:transform .2s,box-shadow .2s,filter .2s;min-height:44px;}"

old_btn_hover = ".btn-primary:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(0,240,255,.5);filter:brightness(1.15);}"
new_btn_hover = ".btn-primary:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(255,138,0,.4);filter:brightness(1.1);}"

css = css.replace(old_btn, new_btn)
css = css.replace(old_btn_hover, new_btn_hover)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Reverted primary button to Amber!")
