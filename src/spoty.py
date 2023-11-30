import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Configuración de autenticación de Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="35b3468f95034fb698d25cf48163e8ad",
    client_secret="a729faa1bab24b43a7d06c21398afbcf",
    redirect_uri="http://127.0.0.1:8080",
    scope="user-library-read"
))

def obtener_datos_spotify():
# Obtener las canciones de la biblioteca del usuario
    resultados = sp.current_user_saved_tracks()

# Itera sobre las canciones en la lista de resultados
    for idx, item in enumerate(resultados['items']):
        # Obtiene la información de la canción actual
        track = item['track']

        # Imprime información formateada sobre la canción
        print(f"{idx + 1}: {track['name']} - {track['artists'][0]['name']}")
        # idx + 1: Número de canción
        # track['name']: Nombre de la canción
        # track['artists'][0]['name']: Nombre del primer artista de la canción
