from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/home")


@app.route("/home")
def home():
    return render_template("base.html")


@app.route("/artist/<artist>")
def artist(artist=None):
    if artist is None:
        return f"Artist default"
    return f"Artist {artist}"


@app.route("/song")
def song():
    return "Song numero dos"


@app.route("/album")
def album():
    return "Album numero tres"
