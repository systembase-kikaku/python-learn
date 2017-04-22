import sys, os
sys.path.append(os.pardir)
import numpy as np
from common import mean_squared_error, cross_entropy_error
from dataset.mnist import load_mnist

t = [0, 0, 1, 0, 0]
y1 = [0.1, 0.05, 0.6, 0.1, 0.1]
y2 = [0.1, 0.05, 0.1, 0.5, 0.1]

print("2乗和誤差----------")
print(mean_squared_error(np.array(y1), np.array(t)))
print(mean_squared_error(np.array(y2), np.array(t)))

print("交差エントロピー誤差----------")
print(cross_entropy_error(np.array(y1), np.array(t)))
print(cross_entropy_error(np.array(y2), np.array(t)))

print("MNISTデータ------------")

(x_train, t_train) , (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape)
print(t_train.shape)
