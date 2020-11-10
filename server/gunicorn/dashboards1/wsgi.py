from app import app

PORT = 5004;
ADDRESS = '127.0.0.1'
#ADDRESS = '0.0.0.0'

if __name__ == '__main__':
    app.run_server(
        port=PORT,
        host=ADDRESS,
        debug=True)

