from bs4 import BeautifulSoup
import requests
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "###########################"
SPOTIPY_CLIENT_SECRET = "#######################"
SPOTIPY_REDIRECT_URI = "http://example.com"
SPOTIFY_USERNAME = "###################"

#Part 1
date = input("What year do you want to travel to? Type the date in this format: YYYY-MM-DD:\n")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")
all_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
song_titles = [song.getText() for song in all_songs]

#Part 2
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

#Part 3
song_uris = []
year = date.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped.")
#Part 4
billboard_playlist = sp.user_playlist_create(user=SPOTIFY_USERNAME, name=f"{date} Billboard 100", public=True, collaborative=False, description='100 Days of Code')
billboard_playlist_id = sp.current_user_playlists()["items"][0]["id"]

sp.playlist_add_items(playlist_id=billboard_playlist_id, items=song_uris, position=None)

