import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

import warnings as w
w.filterwarnings("ignore")


np.random.seed(0)
X, y = make_blobs(5000, centers = [[4,4], [-2, -1], [2, -3], [1, 1]], cluster_std = 0.9)

k_means = KMeans(init = "k-means++", n_clusters = 4, n_init = 12)
k_means.fit(X)

k_means_labels = k_means.labels_
k_means_clust_center = k_means.cluster_centers_

fig = plt.figure(figsize = (6,4))
cols = plt.cm.tab10(np.linspace(0, 1, len(set(k_means_labels))))
ax = fig.add_subplot(1, 1, 1)

for k, col in zip(range(len([[4, 4], [-2, -1], [2, -3], [1, 1]])), cols):
    my_members = (k_means_labels == k)
    cluster_center = k_means_clust_center[k]
    ax.plot(X[my_members, 0], X[my_members, 1], 'w', markerfacecolor=col, marker='.',ms=10)
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,  markeredgecolor='k', markersize=6)

ax.set_title('KMeans')
ax.set_xticks(())
ax.set_yticks(())
plt.show()


