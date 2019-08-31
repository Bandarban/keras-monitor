from flask import Flask, request
import json

JSON = ''

app = Flask(__name__)


@app.route('/')
def hello_world():
    return JSON

@app.route('/reset')
def reset():
    global  JSON
    JSON = ''
    return 'OK'

@app.route('/set', methods=['POST'])
def set_json():
    global JSON
    JSON += str(request.json)+'\n'
    return 'OK', 418


if __name__ == '__main__':
    print("YOBA")
    app.run(host='0.0.0.0', port=4800)
