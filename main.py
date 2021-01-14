import tkinker
import time
from flask import Flask
app = Flask(_name_)

@app.route("/")
def run_app():
    return 'Hello, World!'

