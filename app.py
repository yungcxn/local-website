from dotenv import load_dotenv
load_dotenv()

from flask import Flask, send_file, send_from_directory, render_template
app = Flask(__name__)

import main
import notfound

@app.route('/')
def index():
  return main.content()

@app.errorhandler(404)
def page_not_found(e):
  return notfound.content()


if __name__ == '__main__':
  app.run(host='0.0.0.0')