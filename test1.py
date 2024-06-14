import pandas as pd
import csv

data = pd.read_csv("movies.csv")
data_new = data.drop(labels=['homepage', 'original_title', 'overview', 'spoken_languages', 'keywords', 'production_companies', 'status', 'tagline', 'movie_id', 'vote_average', 'vote_count', 'id', 'cast', 'release_date', 'production_countries', 'popularity'], axis=1)
data_new.to_csv("test1.csv", index=0)
