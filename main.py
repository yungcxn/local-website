import os

def content(files, xspflink):
  header = "<h1>Can's Video-Liste</h1>"
  # for every file, print it beautifully in HTML
  content = header + '<br>'
  for file in files:
    content += f'<a href="/video/{file}">{file}</a><br>'

  content += f'<a href="{xspflink}">XSPF-Liste</a><br>'
  
  return content