from flask import Flask, render_template
import requests
import time


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("dag.html")
