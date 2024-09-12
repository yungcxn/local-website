from dotenv import load_dotenv
load_dotenv()

from flask import Flask, send_file, send_from_directory, render_template, Response
app = Flask(__name__)

import main
import notfound
import os

URL = 'http://can.fritz.box'

@app.route('/')
def index():
  return main.main()

@app.route('/entry/<entryname>')
def entry_view(entryname):
    return main.entry(entryname)

@app.errorhandler(404)
def page_not_found(e):
  return notfound.content()


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)