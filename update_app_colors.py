import re

js_path = 'app.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Change mixed links from Gold to Blue to balance out
# Old: : `rgba(242,179,61,${alpha * 1.5})`;
# New: : `rgba(58,160,255,${alpha * 1.5})`;
js = js.replace(": `rgba(242,179,61,${alpha * 1.5})`);", ": `rgba(58,160,255,${alpha * 1.5})`);")

# Change touch trail from Gold to Cyan/Blue
# Old: g.addColorStop(0, `rgba(242,179,61,${p.life * .5})`);
# New: g.addColorStop(0, `rgba(58,160,255,${p.life * .5})`);
js = js.replace("g.addColorStop(0, `rgba(242,179,61,${p.life * .5})`);", "g.addColorStop(0, `rgba(58,160,255,${p.life * .5})`);")

# In initEEG() the wave was gold. Let's make it alternate or just make it blue.
# ctx.strokeStyle = '#F2B33D'; -> ctx.strokeStyle = '#3AA0FF';
js = js.replace("ctx.strokeStyle = '#F2B33D';", "ctx.strokeStyle = '#3AA0FF';")

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated app.js safely!")
