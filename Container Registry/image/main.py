from flask import Flask

import logging

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    logging.info("/ called")
    return 'hello world', 200, {'Content-Type': 'text/plain; charset=utf-8'}

@app.route('/_ah/health')
def healthcheck():
    return 'ok', 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
