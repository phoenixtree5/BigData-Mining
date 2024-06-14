import pandas as pd
import json
import re

data = pd.read_csv("test4.csv")
data_cy = data.copy()
data_cy.fillna('', inplace=True) #存在一个空
for i in range(len(data_cy)):
    genres = data_cy['genres'][i]
    if len(genres) == 0:
        genres_list = []
        print(genres)
        print(data_cy['title'][i])
        print(genres_list)
    else:
        print(genres)
        print(data_cy['title'][i])
        genres_list = re.findall(r'[^|]+', genres)
        print(genres_list)
        for j in range(len(genres_list)):
            data_cy.loc[data_cy.index == i, genres_list[j]] = 1
del data_cy['Musical']
data = data_cy.copy()
data.to_csv('test5.csv', index=0)
