
from src.recommend import recommend_movies_advanced
from src.api import search_movie
from src.utils import load_movies

# Loading movies
movies = load_movies("data/movies.csv")

# Display recommendations based on similarity
print("Advanced recommendations for 'Toy Story':")
print(recommend_movies_advanced("Toy Story", movies))

# Search for movie details in the API
movie_details = search_movie("Inception")
print("\nInception movie details")
print(movie_details)

