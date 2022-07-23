
# 查看张量的维数
from PIL import Image
import torchvision.transforms as transforms

img = Image.open("F:/photo/grocery store/photo01.jpg")
img = transforms.ToTensor()(img)

print(img.size)
print(img.shape)
