
# transforms.ToTensor() 将给定图像转为Tensor
from PIL import Image
import matplotlib.pyplot as plt
import torchvision.transforms as transforms

img = Image.open("F:/photo/grocery store/photo01.jpg")
plt.imshow(img)
plt.show()
img = transforms.ToTensor()(img)
print(img)
