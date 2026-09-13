import re

css_path = 'styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Make hero-title heavily blue-cyan
old_title = ".hero-title{font-family:var(--font-head);font-weight:900;font-size:clamp(52px,13vw,100px);letter-spacing:-2px;line-height:.9;margin-bottom:16px;background:linear-gradient(135deg,var(--amber) 0%,var(--gold) 40%,var(--amber-l) 60%,var(--blue-l) 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;filter:drop-shadow(0 0 30px rgba(255,138,0,.3));}"
new_title = ".hero-title{font-family:var(--font-head);font-weight:900;font-size:clamp(52px,13vw,100px);letter-spacing:-2px;line-height:.9;margin-bottom:16px;background:linear-gradient(135deg,#00f0ff 0%,var(--blue-l) 40%,var(--gold) 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;filter:drop-shadow(0 0 30px rgba(58,160,255,.4));}"

# Fix ht-year to be blue, remove hardcoded amber
old_year = ".ht-year{display:block;font-size:.55em;letter-spacing:8px;color:var(--amber-l);-webkit-text-fill-color:var(--amber-l);background:none;filter:none;margin-top:8px;}"
new_year = ".ht-year{display:block;font-size:.55em;letter-spacing:8px;color:var(--blue-l);-webkit-text-fill-color:var(--blue-l);background:none;filter:drop-shadow(0 0 10px rgba(58,160,255,.5));margin-top:8px;}"

# Make hero-kicker (Department of Electrical Engineering) blue to fit the electrical vibe
old_kicker = ".hero-kicker{font-family:var(--font-mono);font-size:11px;color:var(--amber-l);letter-spacing:3px;text-transform:uppercase;margin-bottom:16px;}"
new_kicker = ".hero-kicker{font-family:var(--font-mono);font-size:11px;color:#00f0ff;letter-spacing:3px;text-transform:uppercase;margin-bottom:16px; text-shadow: 0 0 8px rgba(0,240,255,0.4);}"

# The SVG Neural icon (brain) in the hero section! Wait, does the hero have a brain SVG? No, that's in the loading screen.
# The neural-canvas gradient in the hero section: 
old_hero_bg = ".hero-section{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:80px 24px 120px;position:relative;overflow:hidden;background:radial-gradient(ellipse 80% 60% at 50% 0%,rgba(255,138,0,.04) 0%,transparent 60%),radial-gradient(ellipse 60% 40% at 80% 60%,rgba(58,160,255,.03) 0%,transparent 60%);}"
new_hero_bg = ".hero-section{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:80px 24px 120px;position:relative;overflow:hidden;background:radial-gradient(ellipse 80% 60% at 50% 0%,rgba(58,160,255,.08) 0%,transparent 60%),radial-gradient(ellipse 60% 40% at 80% 60%,rgba(255,138,0,.04) 0%,transparent 60%);}"

css = css.replace(old_title, new_title)
css = css.replace(old_year, new_year)
css = css.replace(old_kicker, new_kicker)
css = css.replace(old_hero_bg, new_hero_bg)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated Hero CSS for deep Electrical Blue vibes!")
