
# transforms.Normalize(） 归一化处理
from PIL import Image
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
import numpy as np

img = Image.open("F:/photo/grocery store/photo01.jpg")
print(img)
img = transforms.ToTensor()(img)
print(img)
img = transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])(img)
print(img)
img = np.transpose(img, (1, 2, 0))  # 显示的图片的通道维数需要调整到最后一位，imshow()才能显示
print(img.shape)
plt.axis('off')
plt.imshow(img)
plt.show()
