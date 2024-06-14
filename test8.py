import pandas as pd
import json

data = pd.read_csv("test7.csv")
data_cy = data.copy()

del data_cy['Director']
del data_cy['genres']
del data_cy['crew']
del data_cy['revenue']
del data_cy['title']
print(data_cy.columns)

data = data_cy.copy()
data.to_csv('test8.csv', index=0)