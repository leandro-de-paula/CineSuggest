
import os
import requests
from dotenv import load_dotenv

# Loading variables from .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

def search_movie(movie_title):
    url = f"{BASE_URL}/search/movie"
    params = {"api_key": API_KEY, "query": movie_title}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            return results[0]
        else:
            return "No movie found."
    else:
        return f"API error: {response.status_code}"
