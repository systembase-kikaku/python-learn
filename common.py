import numpy as np
from PIL import Image

def img_show(img):
    canvas = Image.new('RGB', (28 * len(img), 28), (255, 255, 255))
    for i in range(len(img)):
        pil_img = Image.fromarray(np.uint8(img[i].reshape(28, 28)))
        canvas.paste(pil_img, (i * 28, 0))
    canvas.show()

def mean_squared_error(y, t):
	return 0.5 * np.sum((y-t)**2)

def cross_entropy_error(y, t):
	if y.ndim == 1:
		t = t.reshape(1, t.size)
		y = y.reshape(1, y.size)

	if t.size == y.size:
		t = t.argmax(axis=1)

	batch_size = y.shape[0]
	return -np.sum(np.log(y[np.arange(batch_size), t])) / batch_size

def numerical_diff(f, x):
	h = 1e-4
	return (f(x+h) - f(x-h)) / (2*h)

def numerical_gradient(f, x):
	h = 1e-4
	grad = np.zeros_like(x)
	for idx in range(x.size):
		tmp_val = x[idx]
		x[idx] = tmp_val + h
		fxh1 = f(x)
		x[idx] = tmp_val - h
		fxh2 = f(x)
		grad[idx] = (fxh1 - fxh2) / (2 * h)
		x[idx] = tmp_val
	return grad
