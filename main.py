# /usr/bin/env python3
import os.path

from flask import Flask, render_template, redirect, request, url_for, make_response
import pandas as pd

if not os.path.exists("polls.csv"):
    structure = {
        "id": [],
        "poll": [],
        "option1": [],
        "option2": [],
        "option3": [],
        "votes1": [],
        "votes2": [],
        "votes3": []
    }

    pd.DataFrame(structure).set_index("id").to_csv("polls.csv")

polls_df = pd.read_csv("polls.csv").set_index("id")

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html", polls=polls_df)

# html calls the function not the endpoint
@app.route("/polls/<id>")
def polls(id):
    poll = polls_df.loc[int(id)]
    return render_template("show_poll.html", poll=poll)

@app.route("/polls", methods=["GET", "POST"])
def create_poll():
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass

@app.route("/vote/<id>/<option>")
def vote(id, option):
    pass

if __name__ == "__main__":
    app.run(host="localhost", debug=True)