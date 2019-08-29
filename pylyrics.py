import requests
import os
import re
import subprocess, shlex
from win32gui import FindWindow, GetWindowText
from bs4 import BeautifulSoup

BASE_URL = f"https://www.azlyrics.com/lyrics/"

def get_window_info():
    command = 'tasklist /fi "imagename eq spotify.exe" /fo csv /v'
    args = shlex.split(command)
    windows_active = subprocess.run(args, capture_output=True)

    string_window_active = "".join(chr(x) for x in windows_active.stdout)
    list_windows = [row for row in string_window_active.split("\r\n") if row != ""]
    
    song_info = list_windows[1].split(",")[-1]
    return song_info 

def get_song_info():
    try:
        song = get_window_info()
        artist, title = song[1:-1].split(" - ", 1)
        return artist, title
    except:
        return "No window found"

def get_page(band, song_title):
    FULL_URL = f"{BASE_URL}/{band}/{song_title}.html"
    page = requests.get(FULL_URL).content

    soup = BeautifulSoup(page, "lxml")
    try:
        lyric_pane = soup.find("div", class_="col-xs-12 col-lg-8 text-center")
        lyrics = lyric_pane.find("div", class_="")
        return lyrics.text
    except AttributeError:
        return "Song does not have any lyrics"

def prepare_artist_title_for_search(artist, title):
    non_alpha = re.compile(r"\W")
    dollar_sign = re.compile(r"\$")
    artist = re.sub(dollar_sign, "s", artist)
    title = re.sub(dollar_sign, "s", title)
    artist = re.sub(non_alpha, "", artist)
    title = re.sub(non_alpha, "", title)
    return artist, title

if __name__ == "__main__":
    try:
        artist, title = get_song_info()
        ready_artist, ready_title = prepare_artist_title_for_search(artist.lower(), title.lower())
        lyrics = get_page(ready_artist, ready_title)
        print(f"Lyrics for {title} by {artist}")
        print(lyrics) 
    except ValueError:
        print("Error")
   
