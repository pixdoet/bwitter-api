# lyrical.py
# for finding a song's lyrics

from lyricsgenius import Genius
TOKEN = ('oqN_tG3oStHRkEI0QODREeEZfppLys85xl-1PKArfJoeIqe7ykwoL37wp259rf28')
genius = Genius(TOKEN)

def find(inputSong,inputArtist):
    songToSearch = (inputSong,inputArtist)
    songlyrics = genius.search_song(songToSearch)
    return songlyrics.lyrics
