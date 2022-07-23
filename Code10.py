
# 将给定图像随机裁剪为不同的大小和宽高比，然后缩放所裁剪得到的图像为制定的大小
# 由于是随机裁剪，所以最后得到的figure02，figure03，figure04都是不一样的
from PIL import Image
import matplotlib.pyplot as plt
import torchvision.transforms as transforms

img = Image.open("F:/photo/grocery store/photo01.jpg")
print("原图大小：", img.size)
data1 = transforms.RandomResizedCrop(224)(img)
print("随机裁剪后的大小:", data1.size)
data2 = transforms.RandomResizedCrop(224)(img)
data3 = transforms.RandomResizedCrop(224)(img)

plt.subplot(2, 2, 1), plt.imshow(img), plt.title("figure01")
plt.subplot(2, 2, 2), plt.imshow(data1), plt.title("figure02")
plt.subplot(2, 2, 3), plt.imshow(data2), plt.title("figure03")
plt.subplot(2, 2, 4), plt.imshow(data3), plt.title("figure04")
plt.axis('on')
plt.show()
