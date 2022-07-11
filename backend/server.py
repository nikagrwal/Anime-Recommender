
import re
import time
import logging
import numpy as np
import pandas as pd

from flask import Flask
from flask import make_response
from flask import request
from flask_cors import CORS

from sklearn.neighbors import NearestNeighbors


logging.basicConfig(level=logging.INFO, format="%(levelname)s  - %(message)s")
logger = logging.getLogger(__name__)

df_anime_all = pd.read_csv('anime.csv', dtype=str)

df_anime_all.rename(columns={'MAL_ID': 'anime_id'}, inplace=True)
df_split_rating = np.array_split(df_anime_all, 3)
df_anime = df_split_rating[0]
df_ratings = pd.read_csv('rating_complete.csv', dtype={
    "user_id": str,
    "anime_id": str,
    "rating": float
})

df_anime_ratings = df_anime.merge(df_ratings, on='anime_id')
df_anime_ratings = df_anime_ratings(usecols=["anime_id", "Name", "user_id", "rating"])

########################################################################

def get_all_anime():
    return (df_anime_all
                .loc[:, ["Name", "anime_id"]]
                .drop_duplicates()
                .to_json(orient="records"))

def similar_users_based_recommendation(ratings, new_user_id):
    model = NearestNeighbors(n_neighbors=7, algorithm='brute', metric='cosine')
    model.fit(ratings)

    # 1. Get neighbour users and their anime ratings
    distances, neighbour_users = model.kneighbors([ratings.loc[new_user_id]])
    neighbour_ratings = ratings.iloc[neighbour_users[0]]

    # 2. Filter down to keep only anime seen by at least one neighbour
    neighbour_rated_anime = neighbour_ratings.T[(neighbour_ratings != 0).any()].T

    # 3. Filter anime that user has not yet seen
    mask = neighbour_rated_anime.loc[new_user_id] == 0
    anime_not_seen_by_user = neighbour_rated_anime.loc[:, mask]

    # 4. Compute the neighours' mean ratings
    mean_ratings = anime_not_seen_by_user.mean().sort_values(ascending=False).head(40)
    return mean_ratings.to_frame().reset_index()

def similar_anime_embeding_based_recommendation(ratings, new_user_id):
    model = NearestNeighbors(n_neighbors=20, algorithm='brute', metric='cosine')
    model.fit(ratings.T) # train, with  anime as rows (T=transpose)

    selected_anime = ratings.loc[new_user_id] > 0.0
    selected_anime = ratings.columns[selected_anime]

    anime_embedding = ratings[selected_anime]
    
    res_df = pd.DataFrame()

    for ani in selected_anime:
        # Find k nearest neighbours and their distances:
        vector = ratings.loc[:, ani]
        distances, suggestions = model.kneighbors([vector])

        df = pd.DataFrame()
        df['score'] = distances.squeeze()
        df['Name'] = ratings.columns[suggestions.squeeze()]
        res_df = res_df.append(df, ignore_index=True)
    
    res_df = res_df.drop_duplicates('Name')
    res_df = res_df.loc[res_df.title.apply(lambda t: t not in selected_anime)]
    return res_df.sort_values(by="score") 

def get_recommendations(selected_anime, strategy="user_similarity"):
    # Simulated random id for a new user
    new_user_id = "UID_611"

    # Add user rated anime
    # Assert selected_anime to consists of records { Name: str, selected: boolean, rating: int }
    df_new_ratings = pd.DataFrame.from_records(selected_anime)
    df_new_ratings['user_id'] = new_user_id

    ratings_matrix = ( df_anime_ratings
        .append(df_new_ratings, ignore_index=True)
        .pivot_table(columns='Name', index='user_id', values='rating')
        .fillna(0)
    )

    recommendations = None

    if strategy == "similar_anime_ratings":
        recommendations = similar_users_based_recommendation(ratings_matrix, new_user_id)
    elif strategy == "similar_anime":
        recommendations = similar_anime_embeding_based_recommendation(ratings_matrix, new_user_id)
    else:
        recommendations = similar_users_based_recommendation(ratings_matrix, new_user_id)
 


########################################################################
#
#   REST API
#
########################################################################

app = Flask(__name__)
CORS(app)

@app.route('/api/anime', methods=['GET'])
def anime():
    animes = get_all_anime()
    return make_response(animes)

@app.route('/api/recommendations', methods=['POST'])
def recommendations():
    data = request.get_json()
    recommendations = get_recommendations(data['anime'], data['strategy'])
    return make_response(recommendations)

if __name__ == "__main__":
    app.run(port=5555, debug=True)

########################################################################