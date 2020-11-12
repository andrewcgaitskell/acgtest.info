from app import app

PORT = 5005;
#ADDRESS = '127.0.0.1'
ADDRESS = '0.0.0.0'

if __name__ == '__main__':
    socketio.run(app,port=5005, use_reloader=False, debug=False)
