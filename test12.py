import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

data = pd.read_csv("test11.csv") # 这里改成test10可以换为PCA的结果
data_cy = data.copy()
data_cy = data_cy.dropna(axis=0)

X = data_cy[['0', '1']]  # 换成PCA，这里要跟着换
y = data_cy['profit_level']

kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)

data_cy['Cluster'] = labels
plt.figure(figsize=(8, 6))

for label in np.unique(labels):
    cluster = X[labels == label]
    plt.scatter(cluster['0'], cluster['1'], label=f'Cluster {label + 1}')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], marker='o', s=200, color='k', label='Centroids')

plt.title('K-Means Clustering of PC1 and PC2 with Profit Levels')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.grid(True)
plt.show()

# 遍历每个 profit_level 的唯一值
for profit_level_label in data_cy['profit_level'].unique():
    # 根据 profit_level 进行筛选
    profit_level_data = data_cy[data_cy['profit_level'] == profit_level_label]
    # 获取每个 profit_level 内部聚类的频数
    cluster_counts = profit_level_data['Cluster'].value_counts().sort_index()
    # 提取聚类编号（x 轴位置）
    unique_clusters = cluster_counts.index
    # 获取每个聚类对应的频数（柱子高度）
    frequencies = cluster_counts.values
    # 绘制柱状图，每个聚类一个柱子，区分不同 cluster
    plt.bar(unique_clusters, frequencies, alpha=0.5, label=f'Level {profit_level_label}')

plt.title('Distribution of Cluster by profit_level')
plt.xlabel('Cluster')
plt.ylabel('Frequency')
plt.legend(title='Cluster')
plt.grid(True)
plt.show()