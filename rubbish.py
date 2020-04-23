from sklearn.cluster import DBSCAN
import numpy as np
import util


arr = util.readDataPoint2("a3dataset.txt")
X = np.array(arr)
X = X.astype(np.float64)
clustering = DBSCAN(eps=1, min_samples=3).fit_predict(X)
for i in clustering:
    print(i)