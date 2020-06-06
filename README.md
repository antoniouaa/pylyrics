# pylyrics
Python script that detects the song Spotify is currently playing and retrieves its lyrics.
Song needs to be playing for the script to detect it. Paused songs are not detected.

Clears the console screen before displaying the lyrics.

## Installation
    git clone https://github.com/antoniouaa/pylyrics
    cd pylyrics
    python -m pip install -r requirements.txt
    
## To run
    python pylyrics.py

## Errors
The script fetches lyrics from Google's search results. If even Google doesn't carry the lyrics, and God help us if they don't, you'll see this error message:
    
    "Song does not have lyrics available"
If nothing is playing while the script is running, the following error message will be shown:
    
    "No song playing"
    
If you spot a song whose lyrics are actually up in the site but get an error message, please raise an issue.

## Why
The only reason this script exists is because Spotify had a built-in function that fetched you the lyrics for any song you were listening to, via MusixMatch.

 I liked it. They got rid of it.

Now here we are wrestling with Python all because I wanna know what the hell mumblerappers sing about.
