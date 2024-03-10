#Hernández Cortez Kevin Uriel - 217734547
#Computación Tolerante a Fallas - 10/03/24
import requests
from prefect import task, Flow
#----------------------------------------------------------------------------
#EXTRAER
@task
def obtenerInfoCancion(track_id, access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"No se ha podido obtener la información de la pista ID {track_id}")
        return None
#TRANSFORMAR
@task
def analizarInfoCancion(track_info):
    if track_info:
        track_name = track_info.get('name')
        artist_names = [artist.get('name') for artist in track_info.get('artists', [])]
        album_name = track_info.get('album', {}).get('name')
        return {'track_name': track_name, 'artist_names': artist_names, 'album_name': album_name}
    else:
        return None
#----------------------------------------------------------------------------
#CARGAR
@task
def desplegarInfoCancion(track_info):
    if track_info:
        print("Nombre de Cancion:", track_info['track_name'])
        print("Artistas:", ', '.join(track_info['artist_names']))
        print("Nombre de Album:", track_info['album_name'])
    else:
        print("No hay informacion de la cancion disponible")
#----------------------------------------------------------------------------
with Flow("Spotify Track Info Extractor") as f:
    IDCancion = "6Ec5LeRzkisa5KJtwLfOoW?si=58aebfb7e9864092"  #ID de la cancion
    tokenAcceso = "BQBNcbtbXr1_faJDOpe69tJYOzbcPDhIQ9Rr5Vc1Gg23vGk1RbtJ8yAtGdi3nbXcmIUAxp3n-PN6gFWUFs4LteBbSwnGlqrvOaeSSVI7WMfLJLuGQiFpgwtJc3YPzLXFdD9FeuFNHSxWkS_nZl7IWuSg2UlEIwTAfxWDo5AKjB8kiqkfqtwH10MI_DFBPsL0BcrJbIwvag32ubPgJJaporWwP4FkWEccZ0p9RCv5DoDMChYlS1yg_O65UmkYGr15vWPprf8zw3TpeWx7sZVi3zu3v111"  #token de acceso de Spotify
    infoCancion = obtenerInfoCancion(IDCancion, tokenAcceso)
    infoAnalizada = analizarInfoCancion(infoCancion)
    desplegarInfoCancion(infoAnalizada)
#----------------------------------------------------------------------------
f.run()
