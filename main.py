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
        return render_template("new_poll.html")
    elif request.method == "POST":
        poll = request.form["poll"]
        option1 = request.form["option1"]
        option2 = request.form["option2"]
        option3 = request.form["option3"]
        polls_df.loc[max(polls_df.index.values) + 1] = [poll, option1, option2, option3, 0, 0, 0]
        polls_df.to_csv("polls.csv")
        return redirect(url_for("index"))

@app.route("/vote/<id>/<option>")
def vote(id, option):
    pass

if __name__ == "__main__":
    app.run(host="localhost", debug=True)