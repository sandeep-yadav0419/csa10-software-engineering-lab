"""Experiment 13: minimal Flask application for the supplied lab."""
from flask import Flask

app = Flask(__name__)

@app.get('/')
def home():
    return 'Hello from CI/CD Docker Pipeline!'

@app.get('/about')
def about():
    return 'This is a simple Flask API'

@app.get('/health')
def health():
    return {'status': 'ok', 'experiment': 13}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
