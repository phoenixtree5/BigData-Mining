import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

data = pd.read_csv("test9.csv")
data_cy = data.copy()

print(data_cy.isnull().sum())
data_cy = data_cy.dropna(axis=0)

features = data_cy.drop(columns=['profit_level'])
target = data_cy['profit_level']

pca = PCA(n_components=2)
principal_components = pca.fit_transform(features)
pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
pca_df['profit_level'] = target

plt.figure(figsize=(5, 3))
plt.scatter(pca_df['PC1'], pca_df['PC2'], c=pca_df['profit_level'], cmap='viridis', alpha=0.5)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA: profit_level')
plt.colorbar(label='Target')
plt.grid(True)
plt.show()

pca_df.to_csv('test10.csv', index=0)
