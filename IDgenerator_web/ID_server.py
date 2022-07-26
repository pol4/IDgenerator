from flask import Flask
from IDmodule import IDGen


app = Flask(__name__)


@app.route("/")
def index():
    idd = IDGen()
    return idd.json()


