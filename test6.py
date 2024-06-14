import pandas as pd
import json
import re

data = pd.read_csv("test5.csv")
data_cy = data.copy()
data_cy['Director'] = ''
director_dict = {
    'name': [],
    'film': [],
    'boxoffice': []
}
df = pd.DataFrame(director_dict)
for i in range(len(data_cy)):
    crew_dict = json.loads(data_cy['crew'][i])
    crew_list = []
    for j in range(len(crew_dict)):
        if crew_dict[j]['job'] == 'Director':
            film_name = crew_dict[j]['name'] #film_name 是导演名字
            crew_list.append(film_name)
            new_data = {
                'name': film_name,
                'film': 1,
                'boxoffice': data_cy['revenue'][i]
            }
            if df['name'].isin([new_data['name']]).any():
                df.loc[df['name'] == film_name, 'film'] += 1
                df.loc[df['name'] == film_name, 'boxoffice'] += data_cy['revenue'][i]

            else:
                # 构造新行数据
                new_row = pd.DataFrame([new_data], columns=['name', 'film', 'boxoffice'])
                # 将新行数据连接到 DataFrame
                df = pd.concat([df, new_row], ignore_index=True)
    director = '|'.join(crew_list)
    print(director)
    data_cy.loc[data_cy.index == i, 'Director'] = director

print(df)

data = data_cy.copy()
data.to_csv('test6.csv', index=0)
df.to_csv('director.csv', index=0)
