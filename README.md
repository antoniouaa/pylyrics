# pylyrics
Python script that detects the song Spotify is currently playing and retrieves its lyrics.
Song needs to be playing for the script to detect it.

Clears the console screen before displaying the lyrics.

The script fetches lyrics from [azlyrics](https://www.azlyrics.com/). If the song's lyrics don't exist there you will get the following error message:
    "Song 

## Prerequisites
The script makes use of BeautifulSoup4 and the requests library. To install them:
    
    pip install bs4
    pip install requests

## Installation
    mkdir pylyrics
    cd pylyrics
    git clone https://github.com/antoniouaa/pylyrics
    
## To run
    cd pylyrics
    python pylyrics.py
