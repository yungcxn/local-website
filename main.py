import os
import random 


def main():
  path = os.path.dirname(os.path.realpath(__file__))
  files = [file for file in os.listdir(path + '/video') if file.endswith('.mp4')]
  split_names = [file.split('_')[0] for file in files]
  # remove duplicates
  split_names = list(dict.fromkeys(split_names))
  split_names.sort()
  css = ""
  with open('static/style.css', 'r') as file:
    css = file.read()

  content = f"<style>{css}</style>"
  header = "<h1>Can's Video-Liste</h1>"
  cats = range(1,4)
  # random choice
  i = random.choice(cats)
  header += f"<img src='/img/cat{i}.gif'>"
  # for every file, print it beautifully in HTML
  content = content + header + '<br>'
  content += '<div class="container">'
  for name in split_names:
    content += f'<span><a href="/entry/{name}">{name}</a></span>'

  # add /live link
  content += f'<span><a href="/live">&#x1F534; LIVE</a></span>'
  content += f'<span><a href="/roms">ROMS</a></span>'
  content += f'<span><a href="/pdf">PDFs</a></span>'
  content += '</div>'
  print(content)
  return content

def entry(name):
  path = os.path.dirname(os.path.realpath(__file__))
  files = [file for file in os.listdir(path + '/video') if file.endswith('.mp4')]
  files = [file for file in files if file.startswith(name)]
  # remove name + "_"
  files = [file[len(name)+1:] for file in files]
  files.sort()
  # remove ".mp4"
  files = [file[:-4] for file in files]
  css = ""
  with open('static/style.css', 'r') as file:
    css = file.read()

  content = f"<style>{css}</style>"
  header = "<h1>Can's Video-Liste</h1>"
  cats = range(1,4)
  # random choice
  i = random.choice(cats)
  header += f"<img src='/img/cat{i}.gif'>"
  # for every file, print it beautifully in HTML
  content = content + header + '<br>'
  content += '<div class="container">'
  for file in files:
    content += f'<span><a href="/video/{name}_{file}.mp4">{file}</a></span>'
  content += '</div>'
  print(content)
  return content
