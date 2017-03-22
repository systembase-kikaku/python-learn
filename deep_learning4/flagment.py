import sys, os
sys.path.append(os.pardir)
import numpy as np
from common import mean_squared_error, cross_entropy_error

t = [0, 0, 1, 0, 0]
y1 = [0.1, 0.05, 0.6, 0.1, 0.1]
y2 = [0.1, 0.05, 0.1, 0.5, 0.1]

print(mean_squared_error(np.array(y1), np.array(t)))
print(mean_squared_error(np.array(y2), np.array(t)))

print(cross_entropy_error(np.array(y1), np.array(t)))
print(cross_entropy_error(np.array(y2), np.array(t)))
