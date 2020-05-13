from flask import Flask, jsonify
import base64

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify(hello="world")


@app.route('/hello')
def hello():
    lInt = [0xff,0b11000000]
    myBytes = bytearray(lInt)
    Base64Str = base64.b64encode(myBytes).decode('ascii')
    return Base64Str


if __name__ == '__main__':
    app.run()
