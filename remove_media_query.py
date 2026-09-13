import re

css_path = 'styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the media query that moves the dock to the top
media_pattern = r'@media\(min-width:1001px\)\{.*?\}\s*\}'
# The block looks like:
# @media(min-width:1001px){
#     body{...}
#     #dock{...}
#     ...
#   }
# Wait, let's use a more precise regex.
media_block_start = css.find('@media(min-width:1001px){')
if media_block_start != -1:
    # Find the closing brace for the media block
    open_braces = 0
    in_block = False
    media_block_end = -1
    for i in range(media_block_start, len(css)):
        if css[i] == '{':
            open_braces += 1
            in_block = True
        elif css[i] == '}':
            open_braces -= 1
        
        if in_block and open_braces == 0:
            media_block_end = i + 1
            break
            
    if media_block_end != -1:
        css = css[:media_block_start] + css[media_block_end:]
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(css)
        print("Removed desktop dock media query!")
    else:
        print("Could not find end of media block.")
else:
    print("Could not find media block.")
