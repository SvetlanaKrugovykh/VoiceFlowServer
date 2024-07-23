# app.py
import os

from app import create_app

app = create_app()

if __name__ == '__main__':
    HOST = os.getenv('HOST', '127.0.0.1')
    PORT = int(os.getenv('PORT', 5000))
    app.run(host=HOST, port=PORT)

