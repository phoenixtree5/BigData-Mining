import pandas as pd
import json

data = pd.read_csv("test3_1.csv")
data_cy = data.copy()
list = []


def is_json(json_str):
    try:
        json.loads(json_str)
        return True
    except ValueError as e:
        return False


for i in range(len(data_cy)):
    result = is_json(data_cy['genres'][i])
    if result is True:
        genres_dict = json.loads(data_cy['genres'][i])
        genres_list = []
        # print(genres_dict)
        # print(type(genres_dict))
        # print(len(genres_dict))
        for j in range(len(genres_dict)):
            # print(genres_dict[j])
            # print(type(genres_dict[j]))
            # print(genres_dict[j]['name'])
            genres_list.append(genres_dict[j]['name'])
            if genres_dict[j]['name'] not in list:
                list.append(genres_dict[j]['name'])
            # print(genres_list)
        genres = '|'.join(genres_list)
        print(genres)
        data_cy.loc[data_cy.index == i, 'genres'] = genres

print(list)

for i in range(len(list)):
    data_cy[list[i]] = 0

data = data_cy.copy()
data.to_csv('test4.csv', index=0)
