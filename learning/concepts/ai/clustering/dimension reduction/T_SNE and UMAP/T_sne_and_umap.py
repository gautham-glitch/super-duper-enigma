from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

iris = load_iris()
X = iris.data
y = iris.target
labels = iris.target_names

x_scaled = StandardScaler().fit_transform(X)

from sklearn.manifold import TSNE
tsne = TSNE(random_state = 42)
T_SNE = tsne.fit_transform(x_scaled)

plt.figure(figsize = (8, 5))
sns.scatterplot(x = T_SNE[:, 0], y = T_SNE[:, 1], hue = labels[y])
plt.show()

import umap
U_map = umap.UMAP(n_neighbors = 10, min_dist = 0.1, random_state = 42)
U_map = U_map.fit_transform(x_scaled)

plt.figure(figsize = (8, 5))
sns.scatterplot(x = U_map[:, 0], y = U_map[:, 1], hue = labels[y])
plt.show()