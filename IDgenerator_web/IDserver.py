import os
from pprint import pprint
from flask import Flask
import sys
import url_mkr
from waitress import serve
sys.path.append(os.path.join(os.getcwd(), 'IDgenerator'))
pprint(sys.path)
from IDmodule import IDGen


app = Flask(__name__)


@app.route("/")
def index():
    idd = IDGen()
    return idd.json()


if __name__ == "__main__":
    serve(app, host=url_mkr.IP, port=url_mkr.port)
