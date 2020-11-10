from app import app

PORT = 8000;
ADDRESS = '127.0.0.1'

if __name__ == '__main__':
    app.run_server(
        port=PORT,
        host=ADDRESS,
        debug=True)

