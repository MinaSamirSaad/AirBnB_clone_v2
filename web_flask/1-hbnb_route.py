#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Function that generates the main route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function that generates the /hbnb route """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
