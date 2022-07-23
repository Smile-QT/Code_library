
# shape、size、type对于张量的作用
# shape:查看张量的维数
# size：查看的好像是img存在的内存位置
# type：查看img存放的数据类型，如int、float、tensor等
from PIL import Image
import torchvision.transforms as transforms

img = Image.open("F:/photo/grocery store/photo01.jpg")
img = transforms.ToTensor()(img)

print(img.shape)
print(img.size)
print(type(img))
