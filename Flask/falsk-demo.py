# cython: language_level=3

import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_baidu():
    return """
        <h1>百度一下, 你就知道</h1> <a href = 'https:www.baidu.com'>baidu</a>
    """

@app.route("/xmlTest")
def prase_xml():
    return open('xmlFile.xml').read()

# @app.route("/tran")
# def tran():
#     kd = requests.


if __name__ == "__main__":
    app.run()
