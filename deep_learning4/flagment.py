import sys, os
sys.path.append(os.pardir)
import numpy as np
from common import mean_squared_error, cross_entropy_error, \
  numerical_diff, numerical_gradient
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

print("ミニバッチ------------")

batch_mask = np.random.choice(x_train.shape[0], 10)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print("数値微分-------------")

def function_1(x):
    return 0.01*x**2 + 0.1*x

print(numerical_diff(function_1, 5))
print(numerical_diff(function_1, 10))

print("勾配---------------")

def function_2(x):
    return x[0]**2 + x[1]**2

print(numerical_gradient(function_2, np.array([3.0, 4.0])))
print(numerical_gradient(function_2, np.array([0.0, 2.0])))
print(numerical_gradient(function_2, np.array([3.0, 0.0])))
