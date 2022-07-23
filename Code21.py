
# transforms.Resize(size=256)
# 改变图片的像素大小
from PIL import Image
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
import numpy as np

img = Image.open("F:/photo/grocery store/photo01.jpg")
img = transforms.ToTensor()(img)
print(img.shape)
(img1) = transforms.Resize(size=[256, 256])(img)
(img2) = transforms.Resize(size=256)(img)
print(img1.shape)
print(img2.shape)
img = np.transpose(img, (1, 2, 0))
plt.imshow(img)
plt.show()
