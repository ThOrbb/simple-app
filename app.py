import json

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello12222"


@app.route("/alive")
def alive():
    return json.dumps({'alive': True})


app.run('0.0.0.0', 8000)
