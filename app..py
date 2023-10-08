from flask import Flask, render_template, request, redirect
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///questionnaire.db")

@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "GET":
        return render_template("quiz2.html")
    elif request.method == "POST":
        one = int(request.form.get("one"))
        two = int(request.form.get("two"))
        three = int(request.form.get("three"))
        four = int(request.form.get("four"))
        five = int(request.form.get("five"))
        six = int(request.form.get("six"))
        seven = int(request.form.get("seven"))
        db.execute("INSERT INTO questionnaire (Question1, Question2, Question3, Question4, Question5, Question6, Question7) VALUES(?, ?, ?, ?, ?, ?, ?)", one, two, three, four, five, six, seven)
        table = db.execute("SELECT * FROM questionnaire WHERE id= (SELECT MAX(Id) FROM questionnaire)")

        tally_count = {
            1:0,
            2:0,
            3:0
        }

        questions = []
        for column in table:
            questions.append(column)
        questions.pop(0)
        for question in questions:
            tally_count[table[question][0]] += 1
        planet_to_visit = 1
        if tally_count[2] > tally_count[1]:
            if tally_count[2] > tally_count[3]:
                planet_to_visit = 2
        elif tally_count[3] > tally_count[1]:
            planet_to_visit = 3

        if planet_to_visit == 1:
            return render_template("success1.html", planet_to_visit=planet_to_visit)
        elif planet_to_visit == 2:
            return render_template("success2.html", planet_to_visit=planet_to_visit)
        elif planet_to_visit == 3:
            return render_template("success3.html", planet_to_visit=planet_to_visit)


@app.route("/planets", methods=["GET"])
def planets():
    return render_template("planets.html")

@app.route("/success1", methods=["GET"])
def success1():
    return render_template("success1.html")

@app.route("/success2", methods=["GET"])
def success2():
    return render_template("success2.html")

@app.route("/success3", methods=["GET"])
def success3():
    return render_template("success3.html")
