import pandas as pd
import json

data = pd.read_csv("test6.csv")
data_cy = data.copy()
director = pd.read_csv("director.csv")
director_cy = director.copy()

data_cy['total_directed'] = 0
for i in range(len(data_cy)):
    crew_dict = json.loads(data_cy['crew'][i])
    crew_list = []
    director_number = 0
    director_film = 0
    for j in range(len(crew_dict)):
        if crew_dict[j]['job'] == 'Director':
            film_name = crew_dict[j]['name']  #导演姓名
            director_number += 1
            for k in range(len(director_cy)):
                if director_cy['name'][k] == film_name:
                    director_film += director_cy['film'][k]
    if director_number == 0:
        average = 0
    else:
        average = director_film / director_number
    data_cy.loc[data_cy.index == i, 'total_directed'] = int(average)
data = data_cy.copy()
data.to_csv('test7.csv', index=0)


