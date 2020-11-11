from app import app

PORT = 8883;
#ADDRESS = '127.0.0.1'
ADDRESS = '0.0.0.0'

if __name__ == '__main__':
    socketio.run(app,port=8883, use_reloader=False, debug=False)
