from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap

from tests.sample import lyrics as sample_lyrics

import pylyrics

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    return redirect("/home")


@app.route("/home")
def home():
    # artist, song, raw_lyrics = pylyrics.get_lyrics()
    artist, song, raw_lyrics = "Bon Jovi", "You give love a bad name", sample_lyrics
    if raw_lyrics and artist and song:
        lyrics = raw_lyrics.split("\n")
        return render_template("home.j2", artist=artist, song=song, lyrics=lyrics)
    return render_template("nolyrics.j2")


@app.route("/artist/")
@app.route("/artist/<artist_name>")
def artist(artist_name=None):
    return render_template("artist.j2", artist_name=artist_name)


@app.route("/song/")
@app.route("/song/<song_name>")
def song(song_name=None):
    return render_template("song.j2", song_name=song_name)
