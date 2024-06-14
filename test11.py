import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import Isomap

data = pd.read_csv("test9.csv")
data_cy = data.copy()
target = data_cy['profit_level']


df_cleaned = data_cy.dropna()
features = df_cleaned.select_dtypes(include=[np.number]).columns.tolist()


df_scaled = df_cleaned[features]

isomap = Isomap(n_components=2)
data_reduced = isomap.fit_transform(df_scaled)
data_isomap = pd.DataFrame(data_reduced)
data_isomap['profit_level'] = target

data_isomap.to_csv('test11.csv', index=0)

plt.figure(figsize=(5, 3))
plt.scatter(data_reduced[:, 0], data_reduced[:, 1], alpha=0.5)
plt.title('Isomap Reduced Data')
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.grid(True)
plt.show()
