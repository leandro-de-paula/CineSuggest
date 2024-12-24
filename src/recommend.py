
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

def recommend_movies_advanced(movie_title, movies, num_recommendations=5):
    # Create TF-IDF matrix for genres
    tfidf_vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    tfidf_matrix = tfidf_vectorizer.fit_transform(movies["genres"])
    tfidf_matrix = csr_matrix(tfidf_matrix)

    # Calculate cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix, dense_output=False)

    try:
        idx = movies[movies['title'].str.contains(movie_title, case=False)].index[0]
    except IndexError:
        return "Movie not found."

    sim_scores = list(enumerate(cosine_sim[idx].toarray().flatten()))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]

    similar_movies_idx = [i[0] for i in sim_scores]
    return movies["title"].iloc[similar_movies_idx].tolist()
