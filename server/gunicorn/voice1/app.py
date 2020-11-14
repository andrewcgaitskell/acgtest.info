from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, logger=True, engineio_logger=True)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    emit('message', {'data': 'Connected to server successfully'})
    return render_template("message.html", message=message)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    return render_template("message.html", message=message)

@socketio.on('message')
def handle_message(message):
    send(message)

if __name__ == '__main__':
    socketio.run(app, debug=True)
