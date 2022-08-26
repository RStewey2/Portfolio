import pandas as pd
import numpy as np

data = pd.read_csv('C:/Users/rstew/Downloads/iris.csv', header=0, names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Name'])
print(data)

sl_val = float(input("Enter Sepal Length :"))
sw_val = float(input("Enter Sepal Width :"))
pl_val = float(input("Enter Petal Length :"))
pw_val = float(input("Enter Petal Width :"))


X = data.drop("Name", axis=1)
X = X.values
y = data["Name"]
y = y.values
print(X)
print(y)
new_data_point = np.array([
    sl_val,
    sw_val,
    pl_val,
    pw_val
 ])
distances = np.linalg.norm(X - new_data_point, axis=1)
k = 5
nearest_neighbor_ids = distances.argsort()[:k]
print(nearest_neighbor_ids)
nearest_neighbor_names = y[nearest_neighbor_ids]
print(nearest_neighbor_names)
unique,pos = np.unique(nearest_neighbor_names,return_inverse=True)
counts = np.bincount(pos)
maxpos = counts.argmax()
print("This is likely an " + unique[maxpos])
