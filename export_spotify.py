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

# export des titres likés
tracks = []
results = sp.current_user_saved_tracks()

print(f'Récupération en cours de {sp.current_user_saved_tracks(limit=1)["total"]} titres')
while  results:
    for item in results['items']:
        track = item['track']
        tracks.append([track["name"], track['artists'][0]['name']])
    if results['next']:
        results = sp.next(results)
    else:
        break

# sauvegarde des titres dans un fichier csv
df = pandas.DataFrame(tracks, columns=["Titre", "Artiste"])
df.to_csv("titres_likes.csv", index=False)
print('Sauvegarde terminée.')
