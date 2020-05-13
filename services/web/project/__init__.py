from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

import base64

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email


@app.route('/')
def hello_world():
    return jsonify(hello="world")


@app.route('/hello')
def hello():
    lInt = [0xff, 0b11000000]
    myBytes = bytearray(lInt)
    Base64Str = base64.b64encode(myBytes).decode('ascii')
    return Base64Str


if __name__ == '__main__':
    app.run()
