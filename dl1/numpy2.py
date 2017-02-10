import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
print(A * B)

X = np.array([[51, 55], [14, 19], [0, 4]])
print(X[0])
print(X[0][1])

for row in X:
    print(row)

print(X.flatten())
print(X.flatten()[[0, 2, 4]])
print(X > 15)
print(X[X>15])
