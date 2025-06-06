import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas
from dotenv import load_dotenv
import os

# charge les variable d'environnement depuis le fichier .env
load_dotenv()

# Crée le dossier csv s'il n'existe pas
csv_dir = "csv"
if not os.path.exists(csv_dir):
    os.makedirs(csv_dir)

# Authentification par l'APi Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
        scope="user-library-read playlist-read-private",
    )
)

# export des titres likés
tracks = []
results = sp.current_user_saved_tracks()
print("************************************************************************ \n ")
print(
    f"Récupération en cours de {sp.current_user_saved_tracks(limit=1)['total']} titres"
)
while results:
    for item in results["items"]:
        track = item["track"]
        tracks.append([track["name"], track["artists"][0]["name"]])
    if results["next"]:
        results = sp.next(results)
    else:
        break

# sauvegarde des titres dans un fichier csv
df = pandas.DataFrame(tracks, columns=["Titre", "Artiste"])
df.to_csv(os.path.join(csv_dir, "titres_likes.csv"), index=False)
print("Export terminé. \n")
print("************************************************************************ \n ")

# Export playlists
playlists = sp.current_user_playlists()

# Crée le dossier 'playlists' s'il n'existe pas
playlists_dir = "csv/playlists"
if not os.path.exists(playlists_dir):
    os.makedirs(playlists_dir)

for playlist in playlists["items"]:
    pl_tracks = []
    results = sp.playlist_tracks(playlist["id"])
    print(f"Récupération en cours des titres de la playlist {playlist['name']}.")
    while results:
        for item in results["items"]:
            track = item["track"]
            if track:
                pl_tracks.append([track["name"], track["artists"][0]["name"]])
        if results["next"]:
            results = sp.next(results)
        else:
            break
    df = pandas.DataFrame(pl_tracks, columns=["Titre", "Artiste"])
    df.to_csv(os.path.join(playlists_dir, f"{playlist['name']}.csv"), index=False)

print("Exports terminés. \n")
