
# transforms.RandomRotation(degrees=15) 随机旋转
from PIL import Image
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
import numpy as np

img = Image.open("F:/photo/grocery store/photo01.jpg")
img = transforms.ToTensor()(img)
(img) = transforms.RandomRotation(degrees=15)(img)
img = np.transpose(img, (1, 2, 0))
plt.imshow(img)
plt.show()

