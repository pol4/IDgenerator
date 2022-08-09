from flask import Flask
from waitress import serve
from IDsource.IDmodule import IDGen
from IDweb.url_mkr import get_config

app = Flask(__name__)


@app.route("/")
def index():
    idd = IDGen()
    return idd.json()


def run_server():
    ip_port = get_config()
    serve(app, host=ip_port[0], port=ip_port[1])
