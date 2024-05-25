import os

def content():
  header = "<h1>Can's Video-Liste</h1>"
  # get all files in /video
  files = os.listdir('video')
  # remove . files
  files = [file for file in files if not file.startswith('.')]
  # for every file, print it beautifully in HTML
  content = header + '<br>'
  for file in files:
    content += f'<a href="/video/{file}">{file}</a><br>'
  
  return content