import requests
import re
import subprocess, shlex
from timeit import default_timer
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
    remix_tag = re.compile(r"(\(|-).*(R|r)emix.*")
    artist = re.sub(r"\s", "+", artist)
    title = re.sub(remix_tag, "", title)
    title = re.sub(r"\s", "+", title)
    return f"{artist}+{title}"

def prepare_lyrics(lyrics):
    if len(lyrics) > 20:
        return lyrics
    return None 

def clear_screen():
    command = 'cls'
    subprocess.run(command, shell=True)
    
if __name__ == "__main__":
    fetch_timer_start = default_timer()
    artist, title = get_song_info()
    fetch_timer_end = default_timer()
    display_timer = None
    fetch_time = fetch_timer_end - fetch_timer_start
    if artist and title:
        ready_song = prepare_artist_title_for_search(artist.lower(), title.lower())
        lyrics = get_page(ready_song)
        if lyrics:
            prepared_lyrics = prepare_lyrics(lyrics)
            clear_screen()
            print(f"Lyrics for {title} by {artist}\n")
            print(prepared_lyrics)
            total_timer_end = default_timer()
            print(f"\n    Query took {fetch_time:.5f} seconds to complete.")
        try:
            display_timer = total_timer_end - fetch_timer_end
            print(f"    Processing and displaying took {display_timer:.5f} seconds to complete.")
        except Exception as e:
            print("Song does not have lyrics available")
    else:
        print("No song playing")
