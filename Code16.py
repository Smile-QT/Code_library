
# 将图片数据转化成张量
from PIL import Image
import torchvision.transforms as transforms

img = Image.open("F:/photo/grocery store/photo01.jpg")
img = transforms.ToTensor()(img)
print(type(img))
