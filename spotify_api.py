import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from os import getenv
from dotenv import load_dotenv

load_dotenv()

client_id = getenv("SPOTIFY_CLIENT_ID")
client_secret = getenv("SPOTIFY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_track(name: str):
    results = sp.search(q=name, type="track", limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return {
            "name": track['name'],
            "artist": track['artists'][0]['name'],
            "url": track['external_urls']['spotify']
        }
    return None
