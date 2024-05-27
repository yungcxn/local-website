from dotenv import load_dotenv
load_dotenv()

from flask import Flask, send_file, send_from_directory, render_template, Response
app = Flask(__name__)

import main
import notfound
import os
import xspf

URL = 'http://can.fritz.box'

# get all files in /video
FILES = [file for file in os.listdir('video') if not file.startswith('.')]

@app.route('/')
def index():
  return main.content(FILES, '/xspf')

@app.route('/xspf')
def xspf_route():
  return Response(xspf.content(FILES, URL), mimetype='application/xspf+xml')


@app.errorhandler(404)
def page_not_found(e):
  return notfound.content()


if __name__ == '__main__':
  app.run(host='0.0.0.0')