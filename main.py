import pandas as pd

# Load data
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

# Show top 5 first line for cada dataset 
print("Movies Dataset:")
print(movies.head())

print("\nRatings Dataset: ")
print(ratings.head())
