import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv("test8.csv")
data_cy = data.copy()

one_hot_encoded = pd.get_dummies(data_cy['original_language'], prefix='language') #one-hot 编码
data_cy = pd.concat([data_cy, one_hot_encoded], axis=1)
data_cy = data_cy.replace({True: 1, False: 0})
del data_cy['original_language']
print(data_cy.head())


scaler = MinMaxScaler() #标准化
features = ['budget', 'runtime', 'total_directed']
data_cy[features] = scaler.fit_transform(data_cy[features])
print(data_cy.head())

data = data_cy.copy()
data_cy.to_csv('test9.csv', index=0)



