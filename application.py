from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from threading import Thread, Event
from time import sleep
from werkzeug.contrib.cache import SimpleCache

cache = SimpleCache()

__author__ = 'andrew_ghaly'

app = Flask(__name__)
app.debug = False
sock = SocketIO(app)

thread = Thread()
cache.set("current-action", "play")


class ControlThread(Thread):
    def __init__(self):
        self.delay = 3
        super(ControlThread, self).__init__()

    def main(self):
        while True:
            current_action = cache.get("current-action")
            sock.emit('control-update', {
                      'message': current_action}, namespace='/control')
            sleep(self.delay)

    def run(self):
        self.main()


@app.route('/')
def index():
    return render_template('video.html')


@app.route('/play')
def play_command():
    cache.set("current-action", "play")
    return "play command"


@app.route('/pause')
def pause_command():
    cache.set("current-action", "pause")
    return "pause command"


@sock.on('connect', namespace='/control')
def connect():
    global thread
    if not thread.isAlive():
        thread = ControlThread()
        thread.start()


if __name__ == '__main__':
    sock.run(app, host='0.0.0.0', port=25200)
