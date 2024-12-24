import pandas as pd

# Load data
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

# Recommendation based on genre
def recommend_movies(movie_title, num_recommendations=5):
    # Check if movie exists
    selected_movie = movies[movies["title"].str.contains(movie_title, case=False)]
    if selected_movie.empty:
        return "Movie not found"
    
    # Find genre and recommend similar movies
    genre = selected_movie.iloc[0]["genres"]
    recommendations = movies[movies["genres"] == genre].head(num_recommendations)
    return recommendations["title"].tolist()

# Test recommendations
print(recommend_movies("Toy Story"))
