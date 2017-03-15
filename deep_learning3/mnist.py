import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    canvas = Image.new('RGB', (280, 28), (255, 255, 255))
    for i in range(len(img)):
        pil_img = Image.fromarray(np.uint8(img[i].reshape(28, 28)))
        canvas.paste(pil_img, (i * 28, 0))
    canvas.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)

img_show(x_test[0:10])
print(t_test[0:10])
