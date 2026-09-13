import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the Robo-Soccer ecard block
# It starts with <div data-reveal class="ecard non-technical" ... data-name="Robo-Soccer"
match = re.search(r'(<div data-reveal class="ecard[^>]+data-name="Robo-Soccer".*?<button class="ecard-btn">VIEW &rarr;</button>\s*</div>)', html, re.DOTALL)

if match:
    robo_soccer_html = match.group(1)
    
    # Remove it from its current wrong position
    html = html.replace(robo_soccer_html, '')
    
    # Insert it at the end of the events-grid
    # The events grid ends with </div><!-- /events-grid -->
    grid_end = html.find('</div><!-- /events-grid -->')
    if grid_end != -1:
        html = html[:grid_end] + "  " + robo_soccer_html + "\n      " + html[grid_end:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Successfully moved Robo-Soccer back to the events grid!")
    else:
        print("Could not find the end of events-grid.")
else:
    print("Could not find Robo-Soccer ecard.")
