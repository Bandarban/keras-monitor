from flask import Flask, request

JSON = {}

app = Flask(__name__)


@app.route('/')
def hello_world():
    return JSON


@app.route('/set', methods=['GET', 'POST'])
def set_json():
    global JSON
    JSON = request.json
    return JSON


if __name__ == '__main__':
    print("YOBA")
    app.run(host='http://youtrack.raiko.io', port=4800)
