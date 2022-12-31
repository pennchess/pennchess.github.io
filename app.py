from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", name="home")

@app.route("/board.html")
def board():
    return render_template("board.html", name="board")

@app.route("/team.html")
def team():
    return render_template("team.html", name="team")

@app.route("/volunteering.html")
def volunteering():
    return render_template("volunteering.html", name="volunteering")

@app.route("/club-games.html")
def club_games():
    return render_template("club-games.html", name="club-games")

@app.route("/sponsors.html")
def sponsors():
    return render_template("sponsors.html", name="sponsors")

@app.route("/contact.html")
def contact():
    return render_template("contact.html", name="contact")