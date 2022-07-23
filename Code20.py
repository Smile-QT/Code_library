
# transforms.CenterCrop(size= 224)
# 将给定的PIL.Image进行中心切割，得到给定的size，size可以是tuple，(target_height, target_width)。size也可以是一个Integer，在这种情况下，切出来的图片的形状是正方形
from PIL import Image
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
import numpy as np

img = Image.open("F:/photo/grocery store/photo01.jpg")
img = transforms.ToTensor()(img)
(img) = transforms.CenterCrop(size=224)(img)
img = np.transpose(img, (1, 2, 0))
plt.imshow(img)
plt.show()


