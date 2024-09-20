from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import main
import notfound
import os
from flask_cors import CORS
import eventlet
import ssl

eventlet.monkey_patch()

app = Flask(__name__, static_folder="static")
CORS(app)
socketio = SocketIO(app, logger=True, engineio_logger=True, cors_allowed_origins="*", async_mode='eventlet',ping_interval=25, ping_timeout=50)

@app.route('/')
def index():
    return main.main()

@app.route('/entry/<entryname>')
def entry_view(entryname):
    return main.entry(entryname)

@app.errorhandler(404)
def page_not_found(e):
    return notfound.content()


currentvideo = ""

def setvideo(url):
    global currentvideo
    currentvideo = url
    app.logger.info("Video updated to " + url)
    emit("setvideo", {"url": url}, broadcast=True, include_self=True)

@socketio.on('requestvideo')
def requestvideo(data):
    url = data['url']
    if os.path.exists("." + url):
        setvideo(url)
    else:
        app.logger.info("File not found: " + url)

@socketio.on('join')
def on_join():
    emit('giveMeTime', broadcast=True, include_self=False)
    app.logger.info('User has entered')

@socketio.on('syncWithTime')
def sync_time(data):
    time = data['time']
    emit('syncWithTime', {'time': time, 'paused': data['paused']}, broadcast=True, include_self=False)

@socketio.on('play')
def play(data):
    time = data['time']
    app.logger.info(str(time) + ' PLAY REQUEST RECEIVED')
    emit('play', {'time': time}, broadcast=True, include_self=False)

@socketio.on('pause')
def pause(data):
    app.logger.info('Pause event received')
    if data is not None and 'time' in data:
        time = data['time']
        app.logger.info(str(time) + ' PAUSE REQUEST RECEIVED')
        emit('pause', {'time': time}, broadcast=True, include_self=False)
    else:
        app.logger.info('No data or time key in data')

@app.route('/live')
def live():
    return render_template('live.html')

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    try:
        context.load_cert_chain('/etc/nginx/ssl/can.fritz.box+3.pem', '/etc/nginx/ssl/can.fritz.box+3-key.pem')
        app.logger.info("SSL certificates loaded successfully.")
    except Exception as e:
        app.logger.info(f"Error loading SSL certificates: {e}")
        
    socketio.run(app, host='0.0.0.0', port=8000, debug=True) 
