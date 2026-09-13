import re

css_path = 'styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Revert Hero Kicker to Amber
old_kicker = ".hero-kicker{font-family:var(--font-mono);font-size:11px;color:#00f0ff;letter-spacing:3px;text-transform:uppercase;margin-bottom:16px; text-shadow: 0 0 8px rgba(0,240,255,0.4);}"
new_kicker = ".hero-kicker{font-family:var(--font-mono);font-size:11px;color:var(--amber-l);letter-spacing:3px;text-transform:uppercase;margin-bottom:16px;}"
css = css.replace(old_kicker, new_kicker)

# 2. Make Hero Title (URJA) flat blue, no gradients
old_title = ".hero-title{font-family:var(--font-head);font-weight:900;font-size:clamp(52px,13vw,100px);letter-spacing:-2px;line-height:.9;margin-bottom:16px;background:linear-gradient(135deg,#00f0ff 0%,var(--blue-l) 40%,var(--gold) 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;filter:drop-shadow(0 0 30px rgba(58,160,255,.4));}"
new_title = ".hero-title{font-family:var(--font-head);font-weight:900;font-size:clamp(52px,13vw,100px);letter-spacing:-2px;line-height:.9;margin-bottom:16px;color:var(--blue-l);filter:drop-shadow(0 0 30px rgba(58,160,255,.4));}"
css = css.replace(old_title, new_title)

# 3. Make HT Year (2K26) flat blue to match, no overrides
old_year = ".ht-year{display:block;font-size:.55em;letter-spacing:8px;color:var(--blue-l);-webkit-text-fill-color:var(--blue-l);background:none;filter:drop-shadow(0 0 10px rgba(58,160,255,.5));margin-top:8px;}"
new_year = ".ht-year{display:block;font-size:.55em;letter-spacing:8px;color:var(--blue-l);background:none;margin-top:8px;}"
css = css.replace(old_year, new_year)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Reverted to flat colors!")
