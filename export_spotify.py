import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas
from dotenv import load_dotenv
import os

# charge les variable d'environnement depuis le fichier .env
load_dotenv()

# Authentification par l'APi Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
    scope="user-library-read playlist-read-private"
))
