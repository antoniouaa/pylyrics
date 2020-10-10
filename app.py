from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    return redirect("/home")


@app.route("/home")
def home():
    return render_template("home.j2")


@app.route("/artist")
@app.route("/artist/<artist>")
def artist(artist=None):
    if artist is None:
        return redirect("/home")
    return render_template("result.j2", name="artist", result=artist)


@app.route("/song")
@app.route("/song/<song_name>")
def song(song_name=None):
    if song_name is None:
        return redirect("/home")
    return render_template("result.j2", name="song", result=song_name)


@app.route("/album")
@app.route("/album/<album_title>")
def album(album_title=None):
    if album_title is None:
        return redirect("/home")
    return render_template("result.j2", name="album", result=album_title)
