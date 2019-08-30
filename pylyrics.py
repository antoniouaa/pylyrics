import requests
import re
import subprocess, shlex
from bs4 import BeautifulSoup

BASE_URL = f"https://www.google.com/search?q="

def get_window_info():
    command = 'tasklist /fi "imagename eq spotify.exe" /fo csv /v'
    args = shlex.split(command)
    windows_active = subprocess.run(args, capture_output=True)

    string_window_active = "".join(chr(x) for x in windows_active.stdout)
    list_windows = [row for row in string_window_active.split("\r\n") if row != ""]
    song_info = list_windows[1].split(",", 9)[-1]
    return song_info 

def get_song_info():
    try:
        song = get_window_info()
        artist, title = song[1:-1].split(" - ", 1)
        reg = re.compile(r"\(.*\)")
        new_title = re.sub(r"\(.*\)", "", title)
        return artist, new_title
    except:
        return None, None

def get_page(song):
    FULL_URL = f"{BASE_URL}/{song}+lyrics"
    page = requests.get(FULL_URL).content
    soup = BeautifulSoup(page, "lxml")
    try:
        lyric_pane = soup.find_all("div", class_="BNeawe tAd8D AP7Wnd")
        return lyric_pane[2].text
    except:
        return None

def prepare_artist_title_for_search(artist, title):
    artist = re.sub(r"\s", "+", artist)
    title = re.sub(r"\s", "+", title)
    return f"{artist}+{title}"

def prepare_lyrics(lyrics):
    html_tag = re.compile(r"<.*?>")
    try:
        lyrics = re.sub(html_tag, "", lyrics)
        return lyrics
    except TypeError:
       return None 

def clear_screen():
    command = 'cls'
    subprocess.run(command, shell=True)
    
if __name__ == "__main__":
    artist, title = get_song_info()
    if artist and title:
        ready_song = prepare_artist_title_for_search(artist.lower(), title.lower())
        lyrics = prepare_lyrics(get_page(ready_song))
        if lyrics:
            clear_screen()
            print(f"Lyrics for {title} by {artist}\n")
            print(lyrics)
        else:
            print("Song does not have lyrics available")
    else:
       print("No song playing")
