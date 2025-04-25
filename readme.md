# Spotify Exporter

Un script Python qui permet d'exporter facilement les titres likés et toutes les playlists Spotify dans des fichiers CSV.

## Fonctionnalités

- 🔐 Authentification sécurisée avec les clés stockées dans un `.env`
- 🎶 Export des titres likés dans le dossier `csv`
- 📂 Export de toutes les playlists dans des fichiers CSV organisés dans le dossier `playlists`

## Installation

1. Clone le repo :

   ```bash
   git clone https://github.com/ton-utilisateur/spotify_exporter.git
   cd spotify_exporter
   ```

2. Crée un environnement virtuel et installe les dépendances :

   ```
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Crée un fichier .env à la racine du projet :

   ```
   SPOTIFY_CLIENT_ID=ton_client_id
   SPOTIFY_CLIENT_SECRET=ton_client_secret
   SPOTIFY_REDIRECT_URI=http://127.0.0.1:8888/callback
   ```

4. Lance le script :

   ```
   python3 export_spotify.py
   ```

## Organisation des fichiers exportés

Les titres likés sont sauvegardés dans csv/titres_likes.csv

Chaque playlist est sauvegardée dans un fichier CSV séparé dans le dossier csv/playlists/

## À savoir

Ton navigateur s'ouvrira à la première exécution pour t'authentifier auprès de Spotify.

Les clés sont lues depuis .env (non versionné grâce à .gitignore)
