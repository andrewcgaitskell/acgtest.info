from app import app

PORT = 5006;
ADDRESS = '127.0.0.1'
#ADDRESS = '0.0.0.0'

if __name__ == '__main__':
    socketio.run(app,use_reloader=False, debug=False)

