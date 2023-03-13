# /usr/bin/env python3
import os.path

from flask import Flask, render_template, redirect, request, url_for, make_response
import pandas as pd


app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(host="localhost", debug=True)