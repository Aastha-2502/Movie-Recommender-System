import requests
import os

API_KEY = os.getenv('TMDB_API_KEY','6c340b09a7087b06f0e34a21aefb9073')

def fetch_posters(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return f'https://image.tmdb.org/t/p/w500{poster_path}'
    return None

