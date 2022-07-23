
# transforms.RandomHorizontalFlip() 以给定的概率随机水平旋转给定的PIL的图像，默认为0.5
from PIL import Image
import matplotlib.pyplot as plt
import torchvision.transforms as transforms

img = Image.open("F:/photo/grocery store/photo01.jpg")
img1 = transforms.RandomHorizontalFlip(0.3)(img)
img2 = transforms.RandomHorizontalFlip(0.7)(img)
img3 = transforms.RandomHorizontalFlip(0.9)(img)

plt.subplot(2, 2, 1), plt.imshow(img), plt.title("figure01")
plt.subplot(2, 2, 2), plt.imshow(img1), plt.title("figure02")
plt.subplot(2, 2, 3), plt.imshow(img2), plt.title("figure03")
plt.subplot(2, 2, 4), plt.imshow(img3), plt.title("figure04")
plt.show()
