PORT = 8000
ADDRESS = 127.0.0.1

from app import app

if __name__ == '__main__':
    app.run(
        port=PORT,
        host=ADDRESS)
