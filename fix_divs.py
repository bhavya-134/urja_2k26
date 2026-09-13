import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix extra closing divs in the sponsors tab
html = html.replace('''        </div>
        </div>
      </div>
    </section>
  </div>
  
  <footer id="footer">''', '''      </div>
    </section>
  </div>
  
  <footer id="footer">''')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed tab-sponsors divs!")
