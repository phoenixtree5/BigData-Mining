import pandas as pd
from imdb import Cinemagoer
import socket
import re
import time

data = pd.read_csv("test2_2.csv")
data_cy = data.copy()
ia = Cinemagoer()
count = 1
count_0 = 1  # 不能设置为0

for i in range(len(data_cy)):
    if str(data_cy['budget'][i]) == '0':
        title = data_cy['title'][i]
        movies = ia.search_movie(data_cy['title'][i])
        movie_id = movies[0].movieID
        movie = ia.get_movie(movie_id)
        if 'box office' in movie:
            if 'Budget' in movie['box office']:
                budget = movie['box office']['Budget']  #Garfield: A Tail of Two Kitties
                print("电影预算:", budget)
                number = re.findall(r'\d+', budget)
                numbers = ''.join(number)
                print("电影名称:", movie)
                print(numbers, type(numbers))
                data_cy.loc[data_cy.index == i, 'budget'] = int(numbers)
            else:
                print("未找到预算信息")
                print("电影名称:", movie)
                data_cy.loc[data_cy.index == i, 'budget'] = 1
        else:
            print("未找到预算信息")
            print("电影名称:", movie)
            data_cy.loc[data_cy.index == i, 'budget'] = 1
        count_0 = count_0 + 1
        if (count_0 % 15 == 0):
            time.sleep(10)
            data = data_cy.copy()
            data.to_csv('test2_1.csv', index=0)

    if str(data_cy['revenue'][i]) == '0':
        title = data_cy['title'][i]
        movies = ia.search_movie(data_cy['title'][i])
        movie_id = movies[0].movieID
        movie = ia.get_movie(movie_id)
        if 'box office' in movie:
            if 'Cumulative Worldwide Gross' in movie['box office']:
                revenue = movie['box office']['Cumulative Worldwide Gross']
                print("电影收入:", revenue)
                word = re.findall(r'[a-zA-Z]', revenue)
                print(word)
                #判断是否包含日期
                if not word:
                    number = re.findall(r'\d+', revenue)  # Imagine That
                    numbers = ''.join(number)
                    number_last = numbers
                    numb33ers_last = ''.join(number_last)
                else:
                    number = re.findall(r'\d+\,+', revenue)  # Imagine That
                    numbers = ''.join(number)
                    number_last = re.findall(r'\d+', numbers)
                    numbers_last = ''.join(number_last)
                print("电影名称:", movie)
                print(numbers_last)
                data_cy.loc[data_cy.index == i, 'revenue'] = int(numbers_last)
            else:
                print("未找到收入信息")
                print("电影名称:", movie)
                data_cy.loc[data_cy.index == i, 'revenue'] = 1
        else:
            print("未找到收入信息")
            print("电影名称:", movie)
            data_cy.loc[data_cy.index == i, 'revenue'] = 1
        count_0 = count_0 + 1
        if (count_0 % 20 == 0):
            time.sleep(10)
            data = data_cy.copy()
            data.to_csv('test2_2.csv', index=0)

    if data_cy['runtime'][i] == 0:
        title = data_cy['title'][i]
        movies = ia.search_movie(data_cy['title'][i])
        movie_id = movies[0].movieID
        movie = ia.get_movie(movie_id)
        if 'runtimes' in movie:
            runtime = movie['runtime']
            print("上映时间:", runtime)
            print(movie)
            data_cy.loc[data_cy.index == i, 'runtime'] = int(runtime[0])
        else:
            print("未找到时间信息")
            print("电影名称:", movie)  # Should've Been Romeo

    if str(data_cy['genres'][i]) == '[]':
        title = data_cy['title'][i]
        movies = ia.search_movie(data_cy['title'][i])
        movie_id = movies[0].movieID
        movie = ia.get_movie(movie_id)
        if 'genres' in movie:
            genres = movie['genres']
            print("风格:", genres)
            print(movie)
            genres_last = '|'.join(genres)
            data_cy.loc[data_cy.index == i, 'genres'] = genres_last
        else:
            print("未找到风格信息")
            print("电影名称:", movie)
    count = count + 1

data = data_cy.copy()
data.to_csv('test2_2.csv', index=0)
